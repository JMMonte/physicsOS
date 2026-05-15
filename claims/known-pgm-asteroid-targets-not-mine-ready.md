---
slug: known-pgm-asteroid-targets-not-mine-ready
status: supported
confidence: 0.86
opened: 2026-05-15
last_updated: 2026-05-15
tags: [asteroid-mining, pgm, targets, prospecting]
supersedes: none
superseded_by: none
---

# Known PGM-rich asteroid targets are prospecting candidates, not mine-ready ore bodies

## Precise statement

As of 2026-05-15, currently identified PGM-relevant asteroid targets, especially 6178 (1986 DA), 2016 ED85, and 7474 (1992 TC), do not have enough public evidence to be treated as economically mineable PGM ore bodies. 6178 (1986 DA) is the strongest known prospecting candidate because it has radar and near-IR evidence for high metal content, but its PGM grade, heterogeneity, mining mechanics, beneficiation yield, and target-specific return economics remain unmeasured.

Operational tolerance: this claim is about public evidence for mine-readiness, not whether the bodies contain large total inventories of metal.

## Why we are tracking this

The rare-metals asteroid-mining thesis depends on specific target quality. "Metal-rich" is not equivalent to "economically mineable PGM ore." This claim prevents PGM inventory estimates from being confused with validated ore bodies.

## Evidence ledger

`Sign ∈ {+1, 0, −1}` (supports / mixed / contradicts). `Veto ∈ {—, R, C}` (none / refute-veto / confirm-veto). Vetoes are categorical — see [AGENTS.md §3.3](../AGENTS.md#33-confidence-rubric).

| Date | Source | Tier | w | Sign | Veto | Notes |
|---|---|---:|---:|---:|---|---|
| 2026-05-15 | [Sanchez et al. 2021](../papers/2021-sanchez-metal-rich-neas-1986-da-2016-ed85.md) | A | 0.85 | +1 | — | Supports 1986 DA and 2016 ED85 as metal-rich candidates, but does not directly assay PGM grade or mineability. |
| 2026-05-15 | [Cannon et al. 2023](../papers/2023-cannon-precious-structural-metals-asteroids.md) | A | 0.85 | +1 | — | Shows realistic PGM grades are ppm-scale and beneficiation is first-order; high older estimates are not supported. |
| 2026-05-15 | [Elvis 2014](../papers/2014-elvis-how-many-ore-bearing-asteroids.md) | A | 0.85 | +1 | — | Estimates PGM ore-bearing NEOs are rare and strongly delta-v sensitive. |
| 2026-05-15 | [audit: pgm-asteroid-target-screen](../audits/2026-05-15-pgm-asteroid-target-screen/) (verdict: `inconclusive`) | — | 1.00 | 0 | — | Screens known candidates and records the missing mine-readiness data; not counted as positive evidence under the audit-verdict mapping because its own verdict is inconclusive. |

Confidence calculation:

```
s_raw  = (0.85 + 0.85 + 0.85 + 0*1.00) / (0.85 + 0.85 + 0.85 + 1.00)
       = 2.55 / 3.55
       = 0.718
s_base = (0.718 + 1) / 2 = 0.859

no vetoes -> confidence = 0.86
```

## Open sub-questions

- What Starship-native architecture can return refined PGMs or high-grade concentrate from a target like 1986 DA?
- What assay payload can measure PGM grade, metal/silicate heterogeneity, regolith mechanics, and beneficiation yield in one mission?
- Are there lower-delta-v M/X-type targets with radar or high-quality near-IR evidence comparable to 1986 DA?

## To read / to audit

- [ ] Primary spectroscopy/taxonomy for 7474 (1992 TC).
- [ ] Cross-match JPL delta-v table with MITHNEOS/SMASS metal-rich classifications.
- [ ] Audit an assay/prospecting mission architecture for 1986 DA and a lower-delta-v characterization candidate.
- [ ] Build a PGM market-depth model for returned Pt/Pd/Rh/Ir/Ru/Os supply.

## Changelog

- 2026-05-15: opened from PGM target-screen audit. Status `supported`, confidence 1.00.
- 2026-05-15: public-prep review corrected the audit ledger row to `Sign=0` because the linked audit's verdict is `inconclusive` under [AGENTS.md section 3.3](../AGENTS.md#33-confidence-rubric). Confidence recomputed to 0.86; status remains `supported`.
