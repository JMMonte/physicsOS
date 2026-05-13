#!/usr/bin/env python3
"""
Generate the three per-role prompts and the sandbox manifest.

Called by scripts/prepare-review.sh after it has copied protocol docs,
stripped the audit README, captured raw script output, and stripped the
claim file. Writes:

  <sandbox>/prompts/devil_advocate.md
  <sandbox>/prompts/source_fidelity.md
  <sandbox>/prompts/reproducibility.md
  <sandbox>/manifest.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path


# --- Prompt templates -----------------------------------------------------
#
# These are kept as Python format strings to avoid the bash-heredoc
# quoting pitfalls. The {sandbox}, {slug}, {root} placeholders are
# substituted via .format(). All other braces are doubled.

DEVIL_ADVOCATE = """\
You are a peer reviewer of an audit in the physicsOS computational-physics
workspace. Your role is to argue AGAINST the position the audit takes.

You are working in a SANDBOX. The audit's verdict, conclusion, prior
reviews, and changelog have been intentionally removed. You evaluate the
work from the premises and methodology alone.

Sandbox root: {sandbox}

Files available to you (paths relative to the sandbox root):
  - CLAUDE.md, AGENTS.md
  - audits_README.md, papers_README.md, claims_README.md
  - audit_premises_README.md   (audit methodology — verdict stripped)
  - audit_script.py            (the audit's Python code)
  - audit_raw_output.txt       (raw stdout of one fresh run of the script)
  - claim_statement_only.md    (claim statement only — ledger/confidence stripped)

You do NOT have access to the live repo at {root}. Do not try to read it.
You may use the protocol docs to understand the framework, and you may use
WebFetch / WebSearch / scripts/fetch_arxiv.sh (via Bash from within the
sandbox copy of the repo's scripts/ if available, or just via raw curl with
proper rate-limit handling) to fetch ORIGINAL CITED SOURCES — but do not
read the author's paper-note summaries in the live repo.

Your task:
  1. Read the audit's premises and code. Form your OWN independent verdict
     about whether the methodology and numerical results support refuting,
     supporting, or being inconclusive about the claim. Record this BEFORE
     steelmanning, so we can see whether the steelman exercise changes
     your view.
  2. Steelman the opposing position. Find the strongest defense of the
     side the audit's methodology pushes against. Identify every
     assumption that could be challenged.
  3. Find rhetorical overreach in the methodology sections — places where
     the prose is more confident than the math supports.
  4. For each cited source, FETCH THE ORIGINAL and compare what the audit
     asserts the source establishes against what it actually establishes.
  5. Identify any relevant literature the audit may have missed.

Write your review to: {sandbox}/_reports/devil_advocate.md

Structure:
  ## My independent verdict (formed BEFORE steelmanning)
  ## Strongest defense of the opposing position
  ## Audit assumptions worth challenging
  ## Overreach: prose vs math
  ## Citation-fidelity concerns (with which sources you fetched and how)
  ## Missing literature
  ## Final verdict (one of: substantive issues / minor issues / agree despite trying not to)

Be specific. Quote audit_premises_README.md passages and audit_script.py
line numbers. DO NOT read other reviewers' files in _reports/.

Return a short summary (under 250 words) of your top findings plus the
verdict.
"""

SOURCE_FIDELITY = """\
You are a peer reviewer of an audit in the physicsOS computational-physics
workspace. Your role is to verify that every source the audit cites
actually says what the audit claims it says.

You are working in a SANDBOX. The author's paper-note summaries are NOT
available — that's deliberate. You must fetch the original sources
yourself.

Sandbox root: {sandbox}

Files available:
  - CLAUDE.md, AGENTS.md, papers_README.md, audits_README.md, claims_README.md
  - audit_premises_README.md   (audit methodology — verdict stripped)
  - audit_script.py            (the audit's Python code)
  - audit_raw_output.txt       (raw stdout of one fresh run)
  - claim_statement_only.md    (claim statement only)

For each source named in the audit's "Sources used in the audit" section
(and any additional sources cited inline in numbered methodology
sections), do this:
  1. Fetch the actual source. arXiv: use the repo's scripts/fetch_arxiv.sh
     if accessible (it has a built-in rate-limit mutex), otherwise WebFetch
     on arxiv.org abstract pages. DOIs: WebFetch. NIST/CODATA: WebFetch.
  2. Read the source — at minimum the abstract, ideally the conclusions
     and the specific section the audit references.
  3. Compare what the audit says the source establishes against what the
     source actually establishes.
  4. Flag any of:
     - Paraphrase that overreaches the source's actual claim.
     - Cited equation that doesn't appear in the source, or differs.
     - Tier assignment that looks too high (per AGENTS.md §1.3).
     - Missing caveats the source includes but the audit omits.
     - Wrong direction of inference (source proves A; audit claims B).

Write your review to: {sandbox}/_reports/source_fidelity.md

Structure:
  ## Sources checked (path; accessible Y/N; method of verification)
  ## Fidelity issues found (one entry per source with the problem)
  ## Tier assignments to revisit
  ## My independent verdict on the audit (based on source fidelity alone)
  ## Final verdict (one of: all sources accurately represented /
                            minor mismatches / substantive misrepresentation)

If a source is paywalled or inaccessible, document the gap — do not
guess. When you flag an issue, quote both the audit's claim and the
source's actual statement.

DO NOT read other reviewers' files in _reports/.

Return a short summary (under 250 words).
"""

REPRODUCIBILITY = """\
You are a peer reviewer of an audit in the physicsOS computational-physics
workspace. Your role is to verify the audit's numbers and code reproduce,
and that load-bearing equations are correct.

You are working in a SANDBOX. The audit's verdict and result summary have
been removed from the README — derive what numbers are load-bearing from
the methodology sections and from audit_script.py.

Sandbox root: {sandbox}

Files available:
  - CLAUDE.md, AGENTS.md, audits_README.md
  - audit_premises_README.md   (audit methodology — verdict stripped)
  - audit_script.py            (the audit's Python code)
  - audit_raw_output.txt       (raw stdout captured at sandbox preparation)
  - claim_statement_only.md    (claim statement only)

You may run the audit script if you have access to the repo's venv at
{root}/.venv. If not, audit_raw_output.txt is the canonical reference run.

Your task:
  1. Re-run the audit script if you can (verifying audit_raw_output.txt).
     Otherwise use audit_raw_output.txt as ground truth.
  2. Cross-check every load-bearing number in the audit_premises_README.md
     (tables, ratios, scaling bounds, derived bounds) against the script
     output. List any mismatches with both values quoted.
  3. Re-derive at least one central equation in the audit from first
     principles. SymPy is fine. Confirm the derived result matches what
     the audit uses.
  4. Check the convergence study if present.
  5. Check dimensional analysis: walk through one full chain from formula
     to a numerical value, with units. Flag any unit error.
  6. Check the conventions header in the audit README matches the
     conventions used in audit_script.py.

Write your review to: {sandbox}/_reports/reproducibility.md

Structure:
  ## Re-run output (key numbers extracted, with line references)
  ## README/script number-matching results
  ## Equation re-derivation (which equation; method; result; agreement)
  ## Convergence / dimensional / convention checks
  ## My independent verdict on the audit
  ## Final verdict (one of: fully reproduces / numerical discrepancies /
                            equation errors)

Quote line numbers in audit_script.py. If a number disagrees, give both
values explicitly with their sources.

DO NOT read other reviewers' files in _reports/.

Return a short summary (under 250 words).
"""

ROLES = {
    "devil_advocate": DEVIL_ADVOCATE,
    "source_fidelity": SOURCE_FIDELITY,
    "reproducibility": REPRODUCIBILITY,
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--sandbox", required=True)
    p.add_argument("--repo-root", required=True)
    p.add_argument("--audit-slug", required=True)
    p.add_argument("--round", required=True, type=int)
    p.add_argument("--timestamp", required=True)
    p.add_argument("--strip-report", required=True,
                   help="JSON output of _strip_audit_readme.py")
    args = p.parse_args()

    sandbox = Path(args.sandbox)
    repo_root = Path(args.repo_root)

    # Write per-role prompts.
    for role, template in ROLES.items():
        text = template.format(
            sandbox=str(sandbox),
            root=str(repo_root),
            slug=args.audit_slug,
        )
        (sandbox / "prompts" / f"{role}.md").write_text(text, encoding="utf-8")

    # Git HEAD at sandbox creation.
    try:
        git_head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=repo_root, text=True
        ).strip()
    except subprocess.CalledProcessError:
        git_head = "n/a"

    # Enumerate every file in the sandbox with its SHA.
    files: list[dict] = []
    for root, _dirs, names in os.walk(sandbox):
        for name in names:
            if name == "manifest.json":
                continue
            full = Path(root) / name
            files.append({
                "path": str(full.relative_to(sandbox)),
                "sha256": sha256_file(full),
                "size_bytes": full.stat().st_size,
            })
    files.sort(key=lambda r: r["path"])

    try:
        strip_report = json.loads(args.strip_report) if args.strip_report.strip() else {}
    except json.JSONDecodeError:
        strip_report = {"_parse_error": "non-JSON strip report", "raw": args.strip_report}

    manifest = {
        "audit_slug": args.audit_slug,
        "review_round": args.round,
        "created_at_utc": args.timestamp,
        "sandbox_path": str(sandbox),
        "git_head_at_creation": git_head,
        "protocol_versions": {
            "CLAUDE.md_sha256": sha256_file(sandbox / "CLAUDE.md"),
            "AGENTS.md_sha256": sha256_file(sandbox / "AGENTS.md"),
        },
        "audit_artifacts": {
            "audit_script.py_sha256": sha256_file(sandbox / "audit_script.py"),
            "audit_premises_README.md_sha256": sha256_file(sandbox / "audit_premises_README.md"),
            "audit_raw_output.txt_sha256": sha256_file(sandbox / "audit_raw_output.txt"),
        },
        "stripping": {
            "stripped_frontmatter_fields": strip_report.get("stripped_frontmatter_fields", []),
            "stripped_sections": strip_report.get("stripped_sections", []),
        },
        "prompts": {
            f"{role}_sha256": sha256_file(sandbox / "prompts" / f"{role}.md")
            for role in ROLES
        },
        "files": files,
    }
    (sandbox / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
