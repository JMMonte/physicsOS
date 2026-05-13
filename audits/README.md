# audits/

One directory per computational audit. An audit is a reproducible check of a physics claim — dimensional, symbolic, numerical, or comparison-to-data.

See [AGENTS.md §2](../AGENTS.md#2-computational-audit-protocol) for the full protocol.

## Directory naming

`<YYYY-MM-DD>-<slug>/`

Examples:
- `2026-05-13-blackbody-peak-wavelength/`
- `2026-05-13-hydrogen-fine-structure-numerical/`
- `2026-05-14-eht-shadow-vs-kerr-prediction/`

## Layout

Each audit directory contains at minimum:

```
README.md         ← claim, audit layers, result, verdict, citations
audit.py | .ipynb ← the actual computation
```

And optionally:

```
outputs/          ← plots, small CSVs (NOT large datasets — link to source)
requirements.txt  ← pinned versions, if reproducibility hinges on them
data/             ← only if small and the audit cannot be re-derived without it
```

## Verdict vocabulary

- `confirmed` — the audit reproduces the claim within stated tolerance.
- `confirmed-with-caveat` — reproduces in the stated regime; note the caveat.
- `contradicted` — the audit disagrees with the claim. Investigate before publishing the disagreement.
- `inconclusive` — the audit could not decide. Say why (numerical instability, regime mismatch, missing data).

The verdict goes in the audit's README front matter and is linked from any claim file that depends on it.

## Reproducibility checklist

Before marking an audit complete:

- [ ] Conventions header at top of audit README (see [memory/conventions.md](../memory/conventions.md)).
- [ ] All constants pulled from `scipy.constants` or `astropy.constants` — no magic numbers.
- [ ] Units checked end-to-end (use `pint` or `astropy.units` when feasible).
- [ ] At least one known-limit recovery shown.
- [ ] For numerical work: convergence study included.
- [ ] RNG seeds printed.
- [ ] Result compared against at least one cited source.
- [ ] Verdict line set.
