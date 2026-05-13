# round0 — pre-sandbox historical reviews

These three reviews (`devil_advocate.md`, `source_fidelity.md`, `reproducibility.md`) were run **before** the sandboxed peer-review protocol existed (AGENTS.md §2.6 in its current form).

At the time of these reviews:
- Each reviewer subagent had full read access to `/Users/joaomontenegro/Development/physicsOS`.
- They could see the audit's `verdict: contradicted` frontmatter and the conclusion-bearing sections (`## Result`, `## Verdict`, `## How the company can rebut`).
- They could see the claim file's `status: refuted, confidence: 0.10` and the full evidence ledger.
- They could see the `examples/casimir-quantum-energy-chip.md` walkthrough narrating the conclusion.

These conditions mean the reviewers' independence is structurally compromised: they were "fresh-context" only in the sense that they did not see the author's conversation, but the live repo itself encoded the conclusion they were asked to evaluate. They are kept here for traceability but should not be treated as the authoritative peer review.

The actual peer review of this audit lives in `round1/` (and later rounds if any), where the reviewers were given a sandboxed view per AGENTS.md §2.6, with a forensic manifest recording exactly which files they had access to.

The findings these round0 reviewers produced were substantive and were folded into the audit's revision history (see the audit's changelog and the prior commits `0548ed0`, `85250eb`, `2c25fdd`). What changed in moving to `round1/` was the *isolation* under which reviews are run, not the reviewers' diligence.
