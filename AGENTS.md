# AGENTS.md — physicsOS agent protocols

This file is the operational manual. [CLAUDE.md](CLAUDE.md) sets the philosophy; this file tells you exactly how to act.

---

## 1. Research protocol

### 1.1 Before you answer

For any non-trivial physics question, **research first, answer second**. "Non-trivial" = anything beyond definitions or arithmetic that a freshman textbook covers in one line.

### 1.2 Source discovery order

1. **arXiv** (`arxiv.org`) — preprints, fast, free. Search by keyword, author, or PACS/MSC category.
2. **DOI / journal of record** — once you have an arXiv ID, find the published version. Note the journal and year.
3. **Authoritative textbooks** — Landau & Lifshitz, Jackson, Goldstein, Peskin & Schroeder, Weinberg, MTW, Wald, Sakurai, etc. Cite chapter and section, not just title.
4. **Review articles** — Reviews of Modern Physics, Living Reviews in Relativity, Physics Reports. Excellent for weighting the consensus.
5. **NIST / CODATA / PDG** — for constants and particle data.
6. **Wikipedia, blogs, lecture notes** — pointers only, never load-bearing citations. Use them to find primary sources.

### 1.3 Source weighting

When two sources conflict, weight by:

| Tier | Source type                                | Weight |
|------|--------------------------------------------|--------|
| S    | Replicated experiment + consensus review   | 1.00   |
| A    | Peer-reviewed primary paper, reputable journal | 0.85 |
| B    | arXiv preprint, established author/group   | 0.70   |
| C    | arXiv preprint, unfamiliar group           | 0.55   |
| D    | Textbook (well-established results only)   | 0.85 for established, 0.50 for speculative |
| E    | Conference proceedings, thesis             | 0.60   |
| F    | Lecture notes, blog, Wikipedia             | 0.30 — pointer-only |
| Z    | Your training-data recollection            | 0.10 — **never** load-bearing |

Record the tier in every paper note's frontmatter.

### 1.4 Logging discipline

Every paper you actually read (more than the abstract) gets a file in `papers/`. Filename convention:
`papers/<year>-<first-author-lastname>-<short-slug>.md`
e.g., `papers/2023-maldacena-eternal-traversable-wormhole.md`

Use [`papers/_template.md`](papers/_template.md). Do not skip the "What it actually shows" section — your job is to distinguish the paper's real result from how it markets itself.

---

## 2. Computational audit protocol

### 2.1 When to audit

Audit whenever the claim is:
- numerical (any number with units),
- dimensional (any equation),
- algebraic (any non-trivial derivation step),
- a limit or asymptotic (any "in the X regime…"),
- a scaling law (any "X scales as Y^n"),
- or a comparison to data.

If you cannot audit it, say so explicitly: `[UNVERIFIED — no audit path]`.

### 2.2 Audit layers, in order

1. **Dimensional analysis.** Always first, always cheap. Use `astropy.units` or `pint` to make it machine-checked when possible.
2. **Limits and special cases.** Recover the known result in the obvious limit (non-relativistic, weak-field, classical, etc.).
3. **Order-of-magnitude estimate.** Fermi-style. Compare to known scales.
4. **Symbolic check.** SymPy for derivations. Verify identities, not just substitute.
5. **Numerical simulation.** Only when the above are insufficient or when comparing to data. Always include a convergence check (vary `dt`, `dx`, `N`, etc., and show the answer stabilizes).
6. **Comparison to data.** Cite the dataset's DOI or arXiv source.

### 2.3 Audit layout

One directory per audit: `audits/<YYYY-MM-DD>-<slug>/` containing:

```
audits/2026-05-13-blackbody-peak-wavelength/
├── README.md         ← what was audited, claim, result, verdict, citations
├── audit.py or .ipynb ← the computation
├── outputs/          ← plots, CSVs (small — don't commit large files)
└── refs.bib          ← optional; otherwise inline-link in README.md
```

Use [`audits/_template/`](audits/_template/) as a starting point.

### 2.4 Reproducibility

- Pin versions (`pip freeze > audits/<slug>/requirements.txt` if it matters).
- Seed every RNG. Print the seed.
- A reader should be able to `cd` into the audit directory, run one command, and reproduce the figure.

### 2.5 Failure modes to watch for

- **Unit confusion** (SI vs Gaussian vs natural, factors of $4\pi$, $\hbar$, $c$).
- **Floating point** in stiff or near-cancellation expressions — switch to `mpmath` or symbolic.
- **Premature linearization** — check whether the linearized regime actually applies.
- **Confusing convention with physics** — sign of metric, Fourier transform conventions, polarization basis, particle-physics vs solid-state conventions.

### 2.6 Peer review

An audit reviewed only by its author is not peer-reviewed — the author's priors flow into both the writing and the checking. The fix is **cross-context subagent peer review**: spawn fresh agents that see the artifacts but not the author's reasoning, and let them produce independent reports.

**When to peer-review.** Always for an audit whose verdict moves a claim's `status` or triggers a veto in §3.3. Optional for incidental sub-audits that don't change a claim's state.

**Isolation rules.** Each reviewer subagent is invoked with the `Agent` tool — fresh context window. Each gets, in its prompt:

- A pointer to `CLAUDE.md`, `AGENTS.md`, `papers/README.md`, `claims/README.md`, `audits/README.md`.
- A pointer to the audit (`audits/<slug>/README.md`, `audits/<slug>/audit.py`).
- A pointer to the claim file linked from the audit's frontmatter.
- A pointer to every paper note linked from the audit.

Each reviewer does **not** see:

- The author's conversation transcript.
- The author's framing of expected outcome.
- Other reviewers' in-progress reports (they may run in parallel and must not coordinate).

Spawn all three reviewers in a **single message with three parallel `Agent` tool calls**. They run concurrently and write into `audits/<slug>/reviews/`.

**The three roles.**

| Role | What they check | Why |
|---|---|---|
| **Devil's advocate** | The strongest defense of the claim the audit refuted (or strongest attack on a claim it supported); audit assumptions that could be challenged; missing literature; prose more confident than math. | The only path to independent disagreement when the author's prior is baked into the audit. |
| **Source fidelity** | Whether each cited paper/textbook actually says what the audit and paper-notes say it says. Tier assignments. Overreaching paraphrases. | Catches the failure mode where the audit does to its sources what Casimir Inc. did to White's PRR paper. |
| **Reproducibility** | Re-runs `audit.py` from clean. Cross-checks every load-bearing number in the README against the script. Re-derives at least one central equation. Convergence, units, conventions. | Catches mechanical and numerical errors invisible to a reader. |

**Reviewer prompt templates** (substitute `{{AUDIT_SLUG}}` per call). Each subagent should be invoked with `subagent_type: "general-purpose"` and `model: "opus"`.

#### Devil's advocate

```
You are a peer reviewer of an audit in the physicsOS computational-physics
workspace at /Users/joaomontenegro/Development/physicsOS (or wherever this
repo is checked out). Your role is to argue AGAINST the audit's conclusion.

Read fully, in order:
  - CLAUDE.md
  - AGENTS.md (especially §1.3 source tiers, §2 audit protocol, §3.3 confidence)
  - audits/{{AUDIT_SLUG}}/README.md
  - audits/{{AUDIT_SLUG}}/audit.py
  - the claim file linked from the audit's frontmatter
  - every paper note in papers/ that the audit cites

Your task:
  1. Pretend the audit's verdict is wrong. Find the strongest defense of the
     position the audit opposes. Steelman it as if you were paid to.
  2. Identify every assumption the audit makes that could be challenged:
     idealizations, boundary conditions, parameter ranges, neglected effects.
  3. Find rhetorical overreach — passages where the prose is more confident
     than the math actually supports.
  4. Flag paraphrases of cited sources that overreach what the source proves.
  5. Identify any post-publication literature the audit may have missed.

Write your review to audits/{{AUDIT_SLUG}}/reviews/devil_advocate.md with:
  ## Strongest defense of the position the audit opposes
  ## Audit assumptions worth challenging
  ## Overreach: prose vs math
  ## Citation-fidelity concerns
  ## Missing literature
  ## Verdict (one of: substantive issues / minor issues / agree despite trying not to)

Be specific. Cite line numbers in audit.py. Quote audit-README passages you
challenge. Cite paper-note paths.

You are NOT here to validate the audit. If after honest effort you still
agree with it, say so explicitly — that is itself a meaningful result.
DO NOT read or coordinate with other reviewers' files (devil_advocate.md is
your own output; do not read source_fidelity.md or reproducibility.md if they
appear).
```

#### Source fidelity

```
You are a peer reviewer of an audit in the physicsOS computational-physics
workspace. Your role is to verify that every source the audit cites actually
says what the audit (and the corresponding paper-notes) claim it says.

Read first:
  - CLAUDE.md, AGENTS.md (especially §1 on research and source tiers)
  - audits/{{AUDIT_SLUG}}/README.md
  - every paper note in papers/ that the audit cites

For each cited source:
  1. Attempt to fetch the actual source. arXiv goes through
     scripts/fetch_arxiv.sh (never raw curl — see AGENTS.md §8.1).
     Journal PDFs via WebFetch when accessible. NIST/CODATA for constants.
  2. Compare what the paper-note says the source establishes against what
     the source actually establishes.
  3. Flag:
     - Paraphrase that overreaches the source's actual claim.
     - A cited equation that doesn't appear in the source, or differs.
     - Tier assignments (§1.3) that look too high.
     - Missing caveats the source includes but the note omits.
     - Wrong direction of inference (source proves A, note claims B).

Write your review to audits/{{AUDIT_SLUG}}/reviews/source_fidelity.md with:
  ## Sources checked (path; accessible Y/N; method of verification)
  ## Fidelity issues found (one entry per source with the problem)
  ## Tier assignments to revisit
  ## Verdict (one of: all sources accurately represented / minor mismatches /
              substantive misrepresentation)

If a source is paywalled or inaccessible, document the gap — do not guess.
When you flag an issue, quote both the audit/note's claim and the source's
actual statement.

DO NOT read or coordinate with other reviewers' files.
```

#### Reproducibility

```
You are a peer reviewer of an audit in the physicsOS computational-physics
workspace. Your role is to verify the audit's numbers and code reproduce,
and that load-bearing equations are correct.

Read first:
  - CLAUDE.md, AGENTS.md (especially §2 audit protocol and §2.4 reproducibility)
  - audits/{{AUDIT_SLUG}}/README.md
  - audits/{{AUDIT_SLUG}}/audit.py

Your task:
  1. Run the audit from clean using the project venv:
        .venv/bin/python audits/{{AUDIT_SLUG}}/audit.py
     Capture the full output.
  2. Cross-check every load-bearing number in the README against the script's
     output. The README's table values, drain times, ratios — every one.
     List any mismatches with both values quoted.
  3. Re-derive at least one central equation in the audit from first
     principles. SymPy is fine. Confirm the result matches what the audit
     uses.
  4. If the audit has a convergence study or sensitivity sweep, run it and
     confirm convergence/stability is actually demonstrated.
  5. Check dimensional analysis: walk through one full chain (formula →
     units → claimed result) and confirm consistency. Flag any unit error.
  6. Check the conventions header at the top of the audit README matches the
     conventions used in audit.py (SI vs Gaussian; metric signature where
     relevant; Fourier sign).

Write your review to audits/{{AUDIT_SLUG}}/reviews/reproducibility.md with:
  ## Re-run output (key numbers extracted, with line references)
  ## README/script number-matching results
  ## Equation re-derivation (which equation; method; result; agreement)
  ## Convergence / dimensional / convention checks
  ## Verdict (one of: fully reproduces / numerical discrepancies / equation errors)

Quote line numbers in audit.py. If a number disagrees, give both values
explicitly with their sources.

DO NOT read or coordinate with other reviewers' files.
```

**Closing the loop.** After all three reviews land:

- The author reads each review.
- For every finding: either revise the audit (and re-trigger the reproducibility review on the revised version) or document a counter-argument in the audit's "Caveats and unresolved" section. **Do not silently ignore** a reviewer finding.
- Update the audit frontmatter:
  ```yaml
  peer_reviewed: YYYY-MM-DD
  reviewer_verdicts:
    devil_advocate: <verdict>
    source_fidelity: <verdict>
    reproducibility: <verdict>
  ```
- If any review surfaced an issue that changes the audit's verdict, propagate the change to the linked claim file's evidence ledger and recompute confidence per §3.3.
- The `reviews/` directory and its contents are committed alongside the audit. The reviews are part of the artifact.

---

## 3. Claim ledger protocol

A **claim** is a physics statement we are tracking the truth-value of: "the cosmological constant is small but positive at scale Λ ≈ 10⁻¹²² in Planck units", "graphene has a Dirac cone at the K-point", "the muon g-2 anomaly is > 4σ".

### 3.1 When to open a claim

- The user asks a question whose answer is non-obvious.
- A paper makes an assertion that contradicts another paper you've logged.
- A computation produces a result you want to defend or revisit.

### 3.2 Claim file structure

See [`claims/_template.md`](claims/_template.md). Key fields:

- **Statement** (precise, with regime and units).
- **Status**: `open` / `supported` / `contested` / `refuted` / `superseded`.
- **Confidence**: 0.0–1.0, computed by the rubric in §3.3.
- **Evidence ledger**: a table; each entry links to a `papers/...` file or `audits/...` directory and records: tier weight, sign (`+1` / `0` / `−1`), and an optional veto flag (`R` / `C`).

### 3.3 Confidence rubric

**Step 1 — base score.** From the evidence ledger:

```
s_raw  = Σ (w_i · sign_i) / Σ w_i      ∈ [−1, +1]
s_base = (s_raw + 1) / 2               ∈ [0, 1]
```

where `w_i` is the tier weight from §1.3 (audits enter with `w = 1.00`).

**Step 2 — apply vetoes.** A veto is a categorical, not probabilistic, signal. The bar is high; default is no veto.

- An entry is `R`-flagged (refute-veto) only if it establishes one of:
  - violation of a conservation law (energy, momentum, charge, lepton number, …);
  - violation of the second law of thermodynamics;
  - violation of dimensional analysis;
  - violation of a kinematic bound (`v ≤ c`, uncertainty principle, etc.);
  - a high-statistics, replicated null result; or
  - an in-repo audit whose verdict is `contradicted` *and* whose contradiction is one of the above (not merely an inconclusive numerical disagreement).
- An entry is `C`-flagged (confirm-veto) only if it establishes one of:
  - replicated experimental confirmation by ≥ 2 independent groups within stated uncertainty;
  - derivation from a previously-established theory with no free parameters and broad applicability.

**Step 3 — combine.**

```
if any R-flag and any C-flag:
    status = "contested"; confidence = s_base
elif any R-flag:
    confidence = min(s_base, 0.10)
elif any C-flag:
    confidence = max(s_base, 0.90)
else:
    confidence = s_base
```

**Audit-verdict to ledger row.** When an audit feeds a claim, translate its verdict like this:

| verdict | sign | veto |
|---|---|---|
| `confirmed` | +1 | `C` only if the audit establishes a *categorical* confirmation |
| `confirmed-with-caveat` | +1 | (none — the caveat blocks the veto) |
| `contradicted` | −1 | `R` only if the contradiction is categorical (conservation/2nd law/dimensional/kinematic) |
| `inconclusive` | 0 | (none) |

Most audits do *not* trigger vetoes. The veto is reserved for audits that prove an obstruction in principle, not in practice.

### 3.4 Updating a claim

Never edit confidence without adding evidence. When new evidence arrives: log the paper in `papers/`, link it from the claim, recompute via §3.3, and add a dated line to the claim's changelog. If a veto flag changes, surface that in the changelog explicitly — it's the most consequential edit a claim can receive.

---

## 4. Citation discipline

Inline, in user-facing responses and in repo files:

- arXiv: `[arXiv:2310.12345](https://arxiv.org/abs/2310.12345)`
- DOI: `[10.1103/PhysRevD.108.123456](https://doi.org/10.1103/PhysRevD.108.123456)`
- Textbook: `Jackson, *Classical Electrodynamics*, 3rd ed., §6.7` — no link needed.

Every numeric result in a response should be followed by either a paper link, an audit link, or the marker `[UNVERIFIED]`. No exceptions.

---

## 5. Communication style

The user is fluent in physics; do not over-explain basics. Be terse, technical, and quantitative. When a derivation is needed, link to an audit rather than inlining ten lines of LaTeX into chat — unless the user asks for the derivation explicitly.

Confidence markers in prose:
- **Established**: cite tier S/A and move on.
- **Likely**: cite the dominant evidence; note dissent if any.
- **Open**: state what would decide it.
- **Speculative**: mark explicitly; do not let it propagate.

---

## 6. When you cannot answer

Acceptable responses, in order of preference:

1. "I logged papers X, Y, Z and ran audit W; the claim is supported at confidence 0.82. Caveat: the regime <Q> is not covered by any source consulted."
2. "No primary source found after searching arXiv categories <A>, <B>, <C> and querying <terms>. Recommend either (a) a deeper literature dive in <area>, or (b) treating this as an open claim and computing a first-principles estimate."
3. "This is outside the regime where any cited source applies. I will not extrapolate from training data."

Unacceptable: a confident answer with no citations.

---

## 7. Spawning subagents

For broad literature surveys (>3 search queries, multiple subfields), spawn an `Explore` or `general-purpose` subagent with explicit instructions to:
- log every paper it reads into `papers/`,
- return a short summary plus the list of paper-note filenames it created,
- *not* draw conclusions — that's the calling agent's job.

For computational audits that are long-running, run the script in the background and continue with other work.

---

## 8. External-API etiquette

External services rate-limit. Honour their stated policies or you will be blocked mid-investigation.

### 8.1 arXiv

arXiv's published policy is **no more than one API request every 3 seconds**, and parallel requests are explicitly discouraged. Hammering them returns HTTP 429 and (with repetition) IP bans.

**Rule: never call `https://export.arxiv.org/api/...` from raw `curl`.** Always go through [`scripts/fetch_arxiv.sh`](scripts/fetch_arxiv.sh), which:

- enforces a 4-second minimum interval across processes via a `mkdir`-based mutex in `$TMPDIR/physicsos-arxiv-throttle/`,
- retries 429/5xx with backoff via `curl --retry-all-errors`,
- sends a descriptive User-Agent with a contact mailto.

Concurrent invocations of the script are safe — they queue. You can launch them in parallel and they will serialize politely.

### 8.2 Other APIs

Apply the same pattern when adding fetchers for other services. If the service publishes a rate-limit policy, encode it in the script. If it doesn't, default to 1 request per 3 seconds and a clear User-Agent. Add the new fetcher to `scripts/` and document its policy here.
