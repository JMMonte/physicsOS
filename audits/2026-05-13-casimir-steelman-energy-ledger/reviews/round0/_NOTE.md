# round0 — pre-sandbox historical reviews

These three reviews (`devil_advocate.md`, `source_fidelity.md`, `reproducibility.md`) were run **before** the sandboxed peer-review protocol existed (AGENTS.md §2.6 in its current form).

At the time of these reviews:
- Each reviewer subagent had full read access to `/Users/joaomontenegro/Development/physicsOS`.
- They could see the audit's `verdict: contradicted` frontmatter and conclusion-bearing sections.
- They could see the claim file's `status: refuted, confidence: 0.10`.
- They could see the audit-1 README (the prior audit in the same case) and its own findings.
- They could see the `examples/casimir-quantum-energy-chip.md` walkthrough.

These conditions mean the reviewers' independence is structurally compromised. They are kept for traceability but should not be treated as the authoritative peer review.

The actual peer review of this audit lives in `round1/` (and later rounds if any), where the reviewers were given a sandboxed view per AGENTS.md §2.6, with a forensic manifest recording exactly which files they had access to.

The findings these round0 reviewers produced were substantive and were folded into the audit's revision history (see the audit's changelog and the commit `2c25fdd`). What changed in moving to `round1/` was the *isolation* under which reviews are run, not the reviewers' diligence.
