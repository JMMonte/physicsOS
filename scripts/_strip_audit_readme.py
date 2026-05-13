#!/usr/bin/env python3
"""
Strip an audit README to the "premises only" view that a sandboxed peer
reviewer should see.

Removes:
  - Frontmatter fields:  verdict, peer_reviewed, reviewer_verdicts
  - Sections (by H2 heading, case-insensitive):
      Result, Verdict, Issues surfaced by peer review,
      Caveats and unresolved, How the company can rebut, Changelog
  - In the "Sources used in the audit" section, paper-note links are
    rewritten to point at the original source URL/DOI. The reviewer is
    expected to fetch the source themselves rather than read the
    author-mediated paper note.

Usage:
  scripts/_strip_audit_readme.py <audit-README> <repo-root> <output-path>

Prints a JSON summary of what was stripped to stdout (used by
prepare-review.sh to populate the manifest).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STRIPPED_FRONTMATTER_FIELDS = {
    "verdict",
    "peer_reviewed",
    "reviewer_verdicts",
}

# H2 headings to remove (case-insensitive; match is on the heading text only).
STRIPPED_SECTIONS = {
    "result",
    "verdict",
    "issues surfaced by peer review",
    "caveats and unresolved",
    "how the company can rebut",
    "changelog",
}


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_block, body). frontmatter_block is empty if absent."""
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text
    fm = text[: end + 5]
    body = text[end + 5 :]
    return fm, body


def strip_frontmatter_fields(fm: str) -> tuple[str, list[str]]:
    """Drop YAML fields whose key (or whose dotted-prefix) is in the strip list.

    Handles simple scalar fields ('key: value') and block fields
    ('key:\n  child: value') — block continuation is identified by
    leading indentation."""
    if not fm:
        return fm, []

    lines = fm.split("\n")
    out: list[str] = []
    stripped: list[str] = []
    skip_block_indent = -1

    for line in lines:
        # Inside a continuation block of a stripped field?
        if skip_block_indent >= 0:
            stripped_leading = len(line) - len(line.lstrip(" "))
            if line.strip() == "" or stripped_leading > skip_block_indent:
                # still inside the stripped field's block
                continue
            else:
                skip_block_indent = -1  # block ended

        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:(.*)$", line)
        if m:
            key = m.group(1)
            rest = m.group(2)
            if key in STRIPPED_FRONTMATTER_FIELDS:
                stripped.append(key)
                # Inline value? Skip just this line. Else start block-skip.
                if rest.strip() == "":
                    skip_block_indent = len(line) - len(line.lstrip(" "))
                continue
        out.append(line)

    return "\n".join(out), stripped


def split_sections(body: str) -> list[tuple[str | None, str]]:
    """Split body into [(heading_or_None, text), ...] by H2 headings.

    Content before the first H2 is returned with heading=None.
    """
    parts: list[tuple[str | None, str]] = []
    current_heading: str | None = None
    current_lines: list[str] = []
    for line in body.split("\n"):
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            # Flush the previous section.
            parts.append((current_heading, "\n".join(current_lines)))
            current_heading = m.group(1)
            current_lines = [line]
        else:
            current_lines.append(line)
    parts.append((current_heading, "\n".join(current_lines)))
    return parts


def strip_sections(body: str) -> tuple[str, list[str]]:
    """Drop sections whose H2 heading (case-insensitive) is in STRIPPED_SECTIONS."""
    parts = split_sections(body)
    kept: list[str] = []
    stripped: list[str] = []
    for heading, text in parts:
        if heading is None:
            kept.append(text)
            continue
        if heading.strip().lower() in STRIPPED_SECTIONS:
            stripped.append(heading)
            continue
        kept.append(text)
    return "\n".join(kept), stripped


def read_paper_note_source(note_path: Path) -> dict[str, str]:
    """Extract bibliographic identifiers from a paper note's frontmatter."""
    if not note_path.exists():
        return {}
    text = note_path.read_text(encoding="utf-8")
    fm, _ = split_frontmatter(text)
    out: dict[str, str] = {}
    for line in fm.split("\n"):
        m = re.match(r"^(arxiv|doi|venue|title|year):\s*(.+?)\s*$", line, re.IGNORECASE)
        if m:
            out[m.group(1).lower()] = m.group(2).strip()
    return out


def rewrite_source_links(body: str, repo_root: Path) -> str:
    """In the 'Sources used in the audit' H2 section, replace paper-note
    markdown links with raw bibliographic identifiers, with a sandbox-
    note explaining that the paper-note summary is intentionally not
    available."""
    parts = split_sections(body)
    out_parts: list[tuple[str | None, str]] = []
    for heading, text in parts:
        if heading and heading.strip().lower().startswith("sources used"):
            text = _rewrite_sources_block(text, repo_root)
        out_parts.append((heading, text))
    # Reassemble
    return "\n".join(t for _, t in out_parts)


def _rewrite_sources_block(text: str, repo_root: Path) -> str:
    link_re = re.compile(r"\[([^\]]*?paper note[^\]]*?)\]\(([^)]+)\)")

    def replace(match: re.Match[str]) -> str:
        rel_path = match.group(2)
        # Resolve relative path. Audit READMEs are at audits/<slug>/README.md
        # and use "../../papers/..."; we resolve against repo_root/papers.
        note_path = (repo_root / "audits" / "_resolved" / "README.md").parent.parent
        # Just trust the path: strip leading "../../"
        clean = rel_path.replace("../", "")
        full = repo_root / clean
        ids = read_paper_note_source(full)
        bits: list[str] = []
        if "arxiv" in ids and ids["arxiv"].lower() not in ("n/a", "na"):
            bits.append(f"arXiv:{ids['arxiv']}")
        if "doi" in ids and ids["doi"].lower() not in ("n/a", "na"):
            bits.append(f"DOI {ids['doi']}")
        if "venue" in ids:
            bits.append(ids["venue"])
        joined = "; ".join(bits) if bits else "(no machine-readable identifier in paper-note frontmatter)"
        return f"original source: {joined}"

    rewritten = link_re.sub(replace, text)
    # Append a sandbox notice if the section was modified.
    if rewritten != text:
        rewritten = rewritten.rstrip() + (
            "\n\n> **Sandbox notice.** The above citations originally linked "
            "to paper-note summaries in `papers/`. Those summaries are "
            "intentionally not provided to the reviewer; fetch the original "
            "sources via `scripts/fetch_arxiv.sh` (for arXiv IDs) or "
            "WebFetch (for DOIs/URLs) and evaluate the audit's claims about "
            "each source against the source itself.\n"
        )
    return rewritten


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: _strip_audit_readme.py <audit-README> <repo-root> <output-path>", file=sys.stderr)
        return 2
    audit_readme = Path(sys.argv[1]).resolve()
    repo_root = Path(sys.argv[2]).resolve()
    output_path = Path(sys.argv[3]).resolve()

    text = audit_readme.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    fm_clean, fm_stripped = strip_frontmatter_fields(fm)
    body_clean, sections_stripped = strip_sections(body)
    body_clean = rewrite_source_links(body_clean, repo_root)

    # Add a "premises-only" notice at the top of the body.
    notice = (
        "\n> **Stripped for review.** This README is a sandbox-curated, "
        "premises-only view of the audit. The author's Result, Verdict, "
        "Caveats, prior peer-review findings, How-to-rebut, and Changelog "
        "sections have been removed so that the reviewer evaluates the "
        "methodology and intermediate work without anchoring on the author's "
        "conclusion. The methodology sections (§1, §2, ...) are preserved "
        "verbatim. Paper-note links in the 'Sources used' section have been "
        "replaced with raw bibliographic identifiers; fetch the originals.\n\n"
    )
    out_text = fm_clean + notice + body_clean
    output_path.write_text(out_text, encoding="utf-8")

    print(json.dumps({
        "input": str(audit_readme),
        "output": str(output_path),
        "stripped_frontmatter_fields": fm_stripped,
        "stripped_sections": sections_stripped,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
