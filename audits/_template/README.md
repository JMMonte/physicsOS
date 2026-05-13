---
slug: <YYYY-MM-DD>-<short-slug>
claim: <claims/slug.md>
conventions: <SI | natural | Planck>; <metric signature>; <Fourier convention if relevant>
verdict: <confirmed | confirmed-with-caveat | contradicted | inconclusive>
audit_layers: [<dimensional>, <limits>, <order-of-magnitude>, <symbolic>, <numerical>, <data-comparison>]
created: <YYYY-MM-DD>
---

# <human title of the audit>

## Claim under audit

<verbatim statement, with units and regime. Quote the source.>

## Source(s)

- [<paper note>](../../papers/<slug>.md)
- <textbook §x.y if applicable>

## Audit plan

<which layers (§2.2 of AGENTS.md) will be applied, in what order, and why.>

## 1. Dimensional analysis

<show units balance. Use pint/astropy.units when possible.>

## 2. Limits / special cases

<recover the known result in the obvious limit.>

## 3. Order-of-magnitude

<Fermi-style estimate.>

## 4. Symbolic (if applicable)

<SymPy block or link to `audit.py`.>

## 5. Numerical (if applicable)

<link to `audit.py` / `audit.ipynb`. Show convergence: vary dt/dx/N and demonstrate stability.>

## 6. Comparison to data (if applicable)

<dataset DOI; what was compared; residuals/figures.>

## Result

<number with units and uncertainty, or symbolic expression, or qualitative outcome.>

## Verdict

`<confirmed | ...>` — <one sentence justification.>

## Caveats and unresolved

<anything the audit did not establish; regimes not covered; numerical concerns left open.>

## Changelog

- YYYY-MM-DD: audit created. Verdict: <…>.
