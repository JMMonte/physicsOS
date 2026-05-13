---
slug: <kebab-case-slug>
status: <open | supported | contested | refuted | superseded>
confidence: <0.00–1.00>
opened: <YYYY-MM-DD>
last_updated: <YYYY-MM-DD>
tags: [<tag1>, <tag2>]
supersedes: <slug or "none">
superseded_by: <slug or "none">
---

# <one-line statement of the claim>

## Precise statement

<full statement, with units, regime of validity, and any quantitative tolerance.>

E.g.: "The 21cm hyperfine transition frequency of neutral hydrogen at rest is 1420.40575 MHz, accurate to ≤ 1 Hz at laboratory temperatures."

## Why we are tracking this

<one paragraph: the originating question or contradiction.>

## Evidence ledger

`Sign ∈ {+1, 0, −1}` (supports / mixed / contradicts). `Veto ∈ {—, R, C}` (none / refute-veto / confirm-veto). Vetoes are categorical — see [AGENTS.md §3.3](../AGENTS.md#33-confidence-rubric) for the strict criteria. Default is `—`.

| Date       | Source                                           | Tier | w    | Sign | Veto | Notes                          |
|------------|--------------------------------------------------|------|------|------|------|--------------------------------|
| YYYY-MM-DD | [paper note](../papers/<slug>.md)                | A    | 0.85 | +1   | —    | reports value X ± σ            |
| YYYY-MM-DD | [audit](../audits/<slug>/)                       | —    | 1.00 | +1   | —    | dimensional + numerical confirm |
| YYYY-MM-DD | [paper note](../papers/<other-slug>.md)          | B    | 0.70 | −1   | —    | reports inconsistent value Y    |

Confidence calculation:
```
s_raw  = (+1·0.85 + +1·1.00 + −1·0.70) / (0.85 + 1.00 + 0.70)
       = 1.15 / 2.55 ≈ 0.451
s_base = (0.451 + 1) / 2 ≈ 0.726

no vetoes → confidence = 0.73
```

If any row has `Veto=R`: confidence is capped at 0.10. If any row has `Veto=C` (and no `R`): confidence is floored at 0.90. If both: set status to `contested` and use `s_base` unmodified.

## Open sub-questions

- <thing not yet resolved>
- <regime not yet checked>

## To read / to audit

- [ ] <paper to find and log>
- [ ] <audit to design>

## Changelog

- YYYY-MM-DD: opened. Initial confidence <x>.
- YYYY-MM-DD: added evidence <source>; confidence <old> → <new>.
