# physicsOS

A working environment for a **computational physics agent**.

The premise is simple: when an AI agent makes a physics claim, it should be backed by a paper you can read, an audit you can re-run, and a confidence number you can recompute. Not assistant priors. Not "as is well known…". An auditable trail or it didn't happen.

physicsOS is the file layout, the protocols, and the tooling that make that trail cheap to produce and durable across sessions. The agent reads research papers and logs them, runs computational checks and saves them, tracks physics statements as a living ledger of evidence, and weights everything against a tier of source authority. The repository becomes the agent's external brain.

---

## Why

Physics is unusually well-suited to an "audit-everything" agent loop:

- **Dimensions are checkable.** A claim with mismatched units is wrong before any further argument.
- **Limits are checkable.** A formula that doesn't recover the known result in the obvious regime is wrong.
- **Numerics are reproducible.** A simulation with a seed and a pinned environment can be re-run by anyone, anywhere.
- **The literature is open.** arXiv, the journals of record, NIST, CODATA, PDG — most primary sources are freely accessible.

Yet typical LLM physics output is none of that: a confident paragraph with no citations, no sanity-check, no record of what was actually consulted. physicsOS is an attempt to fix that, file by file.

---

## Quick start

```bash
git clone <this-repo> physicsOS
cd physicsOS
scripts/bootstrap.sh          # creates .venv with the scientific stack
```

Run the worked example to verify everything is wired up:

```bash
.venv/bin/python audits/2026-05-13-casimir-energy-budget/audit.py
.venv/bin/python audits/2026-05-13-casimir-steelman-energy-ledger/audit.py
```

Both should print intermediate values and a final verdict line ending in `CONTRADICTED`. Plots land in each audit's `outputs/` directory.

To start a new investigation:

```bash
scripts/new_paper.sh 2024 smith my-paper-slug    # scaffold a paper note
scripts/new_audit.sh my-audit-slug               # scaffold an audit dir
scripts/new_claim.sh my-claim-slug               # scaffold a claim file
```

Open the resulting templates and fill them in.

---

## Repository tour

| Path | What's there |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | Prime directives for any agent working in this repo. Don't work from memory; compute before asserting; weight sources honestly. |
| [`AGENTS.md`](AGENTS.md) | The operational manual: research order, source-tier weighting, audit protocol, confidence rubric, citation discipline, external-API etiquette. |
| [`papers/`](papers/) | One Markdown note per paper actually read. Frontmatter records the source tier; the body separates what the paper *shows* from how it markets itself. |
| [`audits/`](audits/) | One directory per computational audit. README + `audit.py` + `outputs/`. Reproducible: clone, bootstrap, run. |
| [`claims/`](claims/) | One file per tracked physics statement. Has an evidence ledger linking back to papers and audits, plus a confidence score recomputed under a transparent rubric. |
| [`memory/`](memory/) | Project-local long-term notes (conventions, open threads). Distinct from any per-user agent memory. |
| [`scripts/`](scripts/) | Bootstrap, scaffolding helpers, rate-limit-safe fetchers. |
| [`requirements.txt`](requirements.txt) | Pinned scientific Python stack (numpy 2, scipy, sympy, matplotlib, pint, astropy 7, mpmath). |

---

## Worked example: a $12M "Quantum Energy Chip"

On 2026-05-12, the company **Casimir, Inc.** announced a $12M seed round for a 5 mm × 5 mm semiconductor chip ("MicroSparc") claimed to deliver **1.5 V × 25 μA continuously** by "harvesting energy from quantum vacuum fields" via "engineered Casimir cavities." Founder: Dr. Harold "Sonny" White, formerly of NASA Eagleworks (EmDrive, "Q-thrusters"). Cited theoretical foundation: White et al., *Phys. Rev. Research* 8, 013264 (2026).

The repository contains a complete two-pass audit of that claim, end to end. It is the canonical example of what the protocol produces:

- **Claim file** — [`claims/casimir-quantum-energy-chip-feasibility.md`](claims/casimir-quantum-energy-chip-feasibility.md). Status: `refuted`. Confidence: 0.10, rubric-capped. Eight-row evidence ledger.
- **Audit 1: energy budget** — [`audits/2026-05-13-casimir-energy-budget/`](audits/2026-05-13-casimir-energy-budget/). Establishes the categorical obstructions: static Casimir reservoir at d=10 nm drains in 289 μs at the claimed power; dynamical Casimir effect would require boundary velocity `v/c > 2000`; passive operation in a single-temperature bath is forbidden by the second law.
- **Audit 2: steelman energy ledger** — [`audits/2026-05-13-casimir-steelman-energy-ledger/`](audits/2026-05-13-casimir-steelman-energy-ledger/). Assumes the only theoretical loophole (Pinto-style modulated-boundary engine) and computes the best-case net power under maximally favorable parameters. Across a 45-point parameter sweep, **0 / 45 combinations yield positive net output**; minimum drive cost exceeds extracted Casimir work by **4.5 × 10⁷×**.
- **Six paper notes** under [`papers/`](papers/) covering the press release, the cited PRR paper (deep-read via the 2015 NTRS precursor + multiple independent reviews because the PRR PDF is Cloudflare-gated), Jaffe's 2005 PRD paper that derives the Casimir effect *without* invoking vacuum energy, Chernodub's "perpetual motion of the fourth kind" paper, Pinto's patent family, and Moddel & Dmitriyeva's 2019 *Atoms* survey of ZPE-extraction proposals.

You can read the conclusion in one paragraph (top of the claim file), inspect the math in one Python script per audit, follow each cited source through to a structured note, or recompute the confidence from the ledger using the formula in [AGENTS.md §3.3](AGENTS.md#33-confidence-rubric). The agent's reasoning is not hiding anywhere.

This is what the protocol is supposed to produce on every claim worth tracking.

---

## The protocol in one screen

1. **Research first.** arXiv, journal of record, authoritative textbooks. Every paper actually read goes in `papers/` with a structured note. Source tiers (S → F) are recorded in the frontmatter.
2. **Audit before asserting.** Six layers in order: dimensional analysis, limits, order-of-magnitude, symbolic, numerical, comparison to data. Each audit directory contains a README, an `audit.py`, and a verdict line. Reproducibility checklist included.
3. **Track claims explicitly.** Each physics statement worth following gets a `claims/<slug>.md` file with a precise statement, regime of validity, evidence ledger, and confidence computed via [§3.3](AGENTS.md#33-confidence-rubric).
4. **Confidence rubric.** Weighted base score in [0,1], with **veto rules** for categorical evidence (a conservation-law violation, a 2nd-law violation, a `v ≤ c` violation, a replicated null result, or an audit verdict `contradicted` for one of these reasons caps the confidence at 0.10; replicated independent confirmation floors it at 0.90).
5. **Cite or mark `[UNVERIFIED]`.** No load-bearing number in agent prose without a link to a paper note, an audit, or the explicit unverified tag.

Full details in [AGENTS.md](AGENTS.md).

---

## Design notes for agent builders

A few choices that matter:

- **Project memory ≠ harness memory.** [`memory/`](memory/) is committable, shared, and version-controlled. It records conventions (unit system, metric signature, Fourier sign) and durable threads. Per-user, per-session agent memory lives elsewhere and is not part of this repo.
- **The repository *is* the agent's working state.** When a session ends, the next agent — human or otherwise — should be able to pick up the thread from the files alone. No reliance on context window survival.
- **Vetoes are categorical.** The confidence rubric refuses to let a strong physical obstruction get averaged away by many neutral citations. This matters: real "extraordinary claims" almost always run into a single hard physical wall, not a probabilistic mismatch.
- **External APIs are throttled at the script layer, not the agent layer.** `scripts/fetch_arxiv.sh` enforces arXiv's stated rate limit via a `mkdir` mutex shared across processes. Agents call the script; the script handles politeness. New fetchers should follow the same pattern.
- **Open in the literal sense.** The agent reads only open-access sources or sources the user is already entitled to. Paywalled PDFs are noted but not auto-circumvented.

---

## Status

Early. The protocol has been validated on one substantial worked example (the Casimir Inc. claim, with two independent audits and eight ledger entries) and a handful of tooling problems caught along the way. The tier-2 items in [memory/open-threads.md](memory/open-threads.md) are the obvious next things — a repo linter, a reading queue, and a generalized fetcher pattern for Crossref / INSPIRE / NIST.

Pull requests are welcome. The most useful contributions are probably:

- New claim files with their backing papers + audits (showing the protocol works on more than one example).
- Improvements to the audit template (helpers for `pint` setup, dimensional sanity, convergence study boilerplate).
- New fetchers for non-arXiv literature sources, following the throttle-and-retry pattern in [`scripts/fetch_arxiv.sh`](scripts/fetch_arxiv.sh).
- Critiques of the confidence rubric (it is a structured heuristic, not a theorem; it should evolve).

---

## License

MIT. See [LICENSE](LICENSE).
