# physicsOS

A working environment for a **computational physics agent**: audit physics ideas with code, weight every claim against real literature, and persist findings as a growing local knowledge base.

## Prime directives

1. **Do not work from memory.** Physics knowledge in your training data is a starting hypothesis, never a citation. Every load-bearing claim must trace to a paper, textbook, or computation logged in this repo.
2. **Compute before you assert.** If a claim is checkable (dimensional analysis, order-of-magnitude estimate, numerical simulation, symbolic derivation), check it. Log the audit.
3. **Track everything locally.** Papers you read go in `papers/`. Audits you run go in `audits/`. Open claims and their evidence ledgers go in `claims/`. The repo is the agent's external brain.
4. **Weight sources honestly.** A peer-reviewed PRD paper is not a blog post is not a Wikipedia summary is not your prior. Use the weighting rubric in [AGENTS.md](AGENTS.md#source-weighting).

## Repository layout

```
physicsOS/
├── CLAUDE.md           ← you are here — house rules
├── AGENTS.md           ← detailed agent protocols (research, audit, citation)
├── memory/             ← project-local long-term notes (committable)
│   └── MEMORY.md       ← index of memory files
├── papers/             ← one markdown file per paper read
│   ├── _template.md
│   └── README.md
├── audits/             ← one directory per computational audit
│   ├── _template/
│   └── README.md
├── claims/             ← tracked physics claims with evidence ledgers
│   ├── _template.md
│   └── README.md
└── scripts/            ← reusable utilities (fetchers, unit checks, etc.)
    └── README.md
```

## Workflow at a glance

When the user asks a physics question:

1. **Restate the claim precisely** — what is being asserted, with units and regime of validity.
2. **Search the literature** — arXiv, journal DOIs, authoritative textbooks. Log each source consulted in `papers/`.
3. **Audit computationally** — dimensional analysis at minimum; numerical/symbolic check when feasible. Save the audit in `audits/<slug>/`.
4. **Update the claim ledger** — open or update `claims/<slug>.md` with the evidence so far and the current confidence level.
5. **Answer the user** — short response, with links to the papers, audits, and claim file. Never hand-wave around an unverified step; mark it explicitly as `[UNVERIFIED]`.

## What "good" looks like

- A user question results in 1–N paper notes, 0–N audits, and exactly one claim file updated.
- Confidence in the answer is explicit and grounded in cited evidence weights.
- The next session — by you or another agent — can pick up the thread from the files alone.

## Anti-patterns

- "It is well-known that…" without a citation.
- A numerical answer with no units, regime check, or sanity comparison.
- Editing a claim's confidence without adding evidence.
- Creating a paper note without recording what the paper actually shows (vs. what its title implies).
- Long prose summaries when a short note + a link to the audit notebook would do.

## Tools assumed available

- Python 3.10+ with the scientific stack: NumPy, SciPy, SymPy, matplotlib, pint, astropy, mpmath. Pinned in [`requirements.txt`](requirements.txt); install via `scripts/bootstrap.sh` which creates `.venv/`.
- Jupyter for exploratory audits (also in the venv).
- `curl`/`wget` for fetching arXiv preprints and DOI metadata.
- Web search for paper discovery (then verify on arXiv/journal).

**Always invoke Python via the project venv**: `.venv/bin/python ...` (or `source .venv/bin/activate` once per shell). Calling raw `python3` will pick up the system interpreter, which may be too old (macOS ships 3.9.6) or missing dependencies.

If a tool is missing, log the gap and propose installation rather than silently substituting.

## Permissions

A suggested permission allowlist for the harness lives at [`.claude/suggested-settings.json`](.claude/suggested-settings.json). Review and, if you agree, either:

- rename it to `.claude/settings.json` (shared, committed), or
- merge its `permissions.allow` entries into your `.claude/settings.local.json` (per-user, gitignored).

The allowlist pre-approves the read-only and scaffolding commands the agent runs constantly (python, arXiv fetch, the `scripts/new_*.sh` helpers, read-only git), so you get fewer prompts without granting broad shell access.
