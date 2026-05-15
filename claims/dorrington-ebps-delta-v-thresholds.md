---
slug: dorrington-ebps-delta-v-thresholds
status: supported
confidence: 1.00
opened: 2026-05-15
last_updated: 2026-05-15
tags: [asteroid-mining, economics, propulsion, npv, delta-v]
supersedes: none
superseded_by: none
---

# Dorrington-Olsen EBPS asteroid-mining thresholds are reproduced by the paper's equations

## Precise statement

Under Dorrington & Olsen's 2026 EBPS single-trip model for whole-asteroid retrieval with all propellant supplied from Earth, using their stated cost/propulsion/duration inputs
\(m_\mathrm{dry}=1250\,\mathrm{kg}\), \(c_l=7469.88\,\$/\mathrm{kg}\),
\(c_\mathrm{sale}=0.9c_l\), \(c_\mathrm{prod}=300000\,\$/\mathrm{kg}\),
\(c_p=0\,\$/\mathrm{kg}\), \(c_\mathrm{ops}=487160\,\$/\mathrm{yr}\),
\(r=20\%\), \(F_T=10\,\mathrm{N}\), \(T_\mathrm{OF,Imp}=0.5\,\mathrm{yr}\), and
\(\Delta V_{EA}=\Delta V_{AE}=\Delta V_\mathrm{avg}\), the unconstrained BEMR zero-NPV limiting average one-way transfer delta-v is approximately \(1.8\,\mathrm{km\,s^{-1}}\)
for chemical propulsion at \(I_{sp}=450\,\mathrm{s}\), and approximately
\(4.5\,\mathrm{km\,s^{-1}}\) for electric propulsion at \(I_{sp}=3000\,\mathrm{s}\).

Operational tolerance for this claim: reproduction within \(0.1\,\mathrm{km\,s^{-1}}\), matching the paper's rounded statement.

This claim does **not** assert finite-capacity positive NPV at those same limits. The linked audit separately records that enforcing \(M_\mathrm{max}=160000\,\mathrm{kg}\) gives \(1.225\,\mathrm{km\,s^{-1}}\) for chemical EBPS and \(4.422\,\mathrm{km\,s^{-1}}\) for electric EBPS.

## Why we are tracking this

The Dorrington-Olsen paper is one of the more technically useful recent asteroid-mining economics papers. Its headline EBPS result is easy to misread as a generic propulsion or finite-capacity feasibility limit; the tracked claim is narrower: whether the paper's published equations and model inputs actually reproduce the reported \(1.8/4.5\,\mathrm{km\,s^{-1}}\) zero-NPV BEMR thresholds.

## Evidence ledger

`Sign ∈ {+1, 0, −1}` (supports / mixed / contradicts). `Veto ∈ {—, R, C}` (none / refute-veto / confirm-veto). Vetoes are categorical — see [AGENTS.md §3.3](../AGENTS.md#33-confidence-rubric) for the strict criteria. Default is `—`.

| Date       | Source                                           | Tier | w    | Sign | Veto | Notes                          |
|------------|--------------------------------------------------|------|------|------|------|--------------------------------|
| 2026-05-15 | [Dorrington & Olsen 2026](../papers/2026-dorrington-parametric-economic-asteroid-mining.md) | A | 0.85 | +1 | — | Reports the rounded EBPS limits: \(<1.8\,\mathrm{km\,s^{-1}}\) chemical, \(\sim4.5\,\mathrm{km\,s^{-1}}\) electric. |
| 2026-05-15 | [audit: dorrington-bemr-delta-v-thresholds](../audits/2026-05-15-dorrington-bemr-delta-v-thresholds/) (verdict: `confirmed`) | — | 1.00 | +1 | — | Reproduces \(1.789\,\mathrm{km\,s^{-1}}\) and \(4.435\,\mathrm{km\,s^{-1}}\). Round 1 peer review: devil_advocate = minor issues; source_fidelity = minor mismatches; reproducibility = fully reproduces. |

Confidence calculation:

```
s_raw  = (+1·0.85 + +1·1.00) / (0.85 + 1.00)
       = 1.00
s_base = (1.00 + 1) / 2 = 1.00

no vetoes → confidence = 1.00
```

## Open sub-questions

- The finite-capacity chemical boundary is substantially lower than the unconstrained BEMR limit; this is a separate feasibility claim if we want to track it.
- ISPP and multi-trip thresholds remain unaudited.

## To read / to audit

- [ ] Open a separate claim for finite-capacity EBPS feasibility under \(M_\mathrm{max}=160000\,\mathrm{kg}\), seeded from the already-computed capacity-constrained output: \(1.225\,\mathrm{km\,s^{-1}}\) chemical and \(4.422\,\mathrm{km\,s^{-1}}\) electric.
- [ ] Audit the ISPP single-trip threshold \(\sim8.8\,\mathrm{km\,s^{-1}}\), including extraction mass, return-propellant production mass, and \(M_\mathrm{max}\) constraints.
- [ ] Audit the multi-trip claim that smaller repeated shipments can outperform one large single-trip return, using the paper's cumulative NPV equations.
- [ ] Run a parameter-sensitivity audit over sale price, launch cost, discount rate, thrust, and dry-mass scaling to identify which inputs dominate the EBPS/ISPP thresholds.
- [ ] Compare Dorrington-Olsen thresholds against Sonter 1997, Hein-Matheson-Fries 2020, and Dorrington-Olsen 2019 location-routing assumptions.

## Changelog

- 2026-05-15: opened. Initial status `open`, confidence 0.50 pending sandboxed review.
- 2026-05-15: completed sandboxed review round 1 for the linked audit. Added paper and audit evidence rows. Recomputed confidence: `s_raw=1.00`, no vetoes, confidence 1.00. Status `open` → `supported`.
- 2026-05-15: added follow-up audit TODOs for finite-capacity EBPS, ISPP, multi-trip NPV, sensitivity, and literature comparison.
