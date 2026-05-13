#!/usr/bin/env python3
"""
Strip a claim file to the "statement only" view that a sandboxed peer
reviewer should see. Drops the frontmatter (status/confidence), the
evidence ledger, the changelog — everything that contains the verdict
or its derivation.

Usage: scripts/_strip_claim_file.py <claim-file> <output-path>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

KEEP_SECTIONS = {"precise statement", "why we are tracking this"}


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: _strip_claim_file.py <claim-file> <output-path>", file=sys.stderr)
        return 2
    src = Path(sys.argv[1]).read_text(encoding="utf-8")
    out_path = Path(sys.argv[2])

    # Drop frontmatter entirely.
    if src.startswith("---\n"):
        end = src.find("\n---\n", 4)
        body = src[end + 5 :] if end != -1 else src
    else:
        body = src

    parts: list[tuple[str | None, str]] = []
    heading: str | None = None
    buf: list[str] = []
    for line in body.split("\n"):
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            parts.append((heading, "\n".join(buf)))
            heading = m.group(1)
            buf = [line]
        else:
            buf.append(line)
    parts.append((heading, "\n".join(buf)))

    out_blocks: list[str] = []
    for h, text in parts:
        if h is None:
            out_blocks.append(text)
            continue
        if h.strip().lower() in KEEP_SECTIONS:
            out_blocks.append(text)

    notice = (
        "\n> **Stripped for review.** This is a sandbox-curated view of the "
        "claim file. The frontmatter (status, confidence), evidence ledger, "
        "to-read list, and changelog have been removed so that the reviewer "
        "sees only the claim itself.\n\n"
    )
    out_path.write_text(notice + "\n".join(out_blocks).rstrip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
