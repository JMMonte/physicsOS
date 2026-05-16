---
slug: macs0416y1-oiii-ratio-anomaly
status: supported
confidence: 0.81
opened: 2026-05-16
last_updated: 2026-05-16
tags: [high-redshift, MACS0416-Y1, OIII, nebular-diagnostics, dust-extinction, photoionization]
supersedes: none
superseded_by: none
---

# In MACS0416-Y1, the observed [OIII]88μm/[OIII]5007 = 0.26±0.06 exceeds the single-zone, dust-free photoionization ceiling at the measured T_e, implying differential suppression of the optical line and/or physically distinct emitting regions

## Precise statement

For MACS0416-Y1 (z=8.312) with measured Te[OIII] = 17300 ± 1500 K (from [OIII]4363) and n_e = 730⁺¹⁵⁰₋₁₄₀ cm⁻³ (from [OII]3726/3729), the intrinsic O III emissivity ratio ε(88μm)/ε(5007) of a single dust-free photoionized zone has a **maximum over all n_e of ≈0.13** at T_e=17300 K (≤0.15 even at the −1σ T_e of 15800 K). The observed 0.26 ± 0.06 lies a factor ≈2 (≈1.8–2.2σ) above this ceiling and cannot be produced by any single dust-free zone at the measured temperature. This is consistent with the optical [OIII]5007 being suppressed (dust extinction and/or a distinct denser/cooler optical-emitting zone). Regime/caveats: conditional on the [OIII]4363-based T_e (with T_e free the ceiling would reach 0.26 for T_e ≲ 12200 K); single-zone 5-level treatment (no full photoionization grid); PyNeb default O III atomic data.

## Why we are tracking this

Third headline claim of Takechi et al. 2026 and an open sub-question of [[macs0416y1-early-dust-feasible]]. It affects how JWST optical + ALMA FIR [OIII] are combined at high z; if single-zone analyses are invalid here, metallicity/ISM inferences that mix the two lines need care.

## Evidence ledger

`Sign ∈ {+1, 0, −1}`. `Veto ∈ {—, R, C}`. Default `—`.

| Date       | Source                                                                      | Tier | w    | Sign | Veto | Notes                                                                                  |
|------------|-----------------------------------------------------------------------------|------|------|------|------|----------------------------------------------------------------------------------------|
| 2026-05-16 | [paper note](../papers/2026-takechi-dreams-macs0416y1-early-dust.md)         | B    | 0.70 | +1   | —    | Reports ratio 0.26±0.06 + measured Te=17300, ne=730; asserts >single-zone at any n_e   |
| 2026-05-16 | [audit](../audits/2026-05-16-oiii-88um-5007-single-zone-ceiling/)            | —    | 1.00 | +1   | —    | Independent PyNeb 5-level: ceiling ≈0.13 @ measured T_e; 0.26 is ~2× above; robust to 5007-vs-doublet definition |
| 2026-05-16 | [audit](../audits/2026-05-16-oiii-88um-5007-single-zone-ceiling/)            | —    | 1.00 | 0    | —    | Caveat: exceedance only ~1.8–2.2σ for ±0.06; conditional on T_e (free-T_e the claim fails ≲12200 K); dust-free assumption is the paper's own mechanism |

Confidence calculation:
```
s_raw  = (0.70·(+1) + 1.00·(+1) + 1.00·(0)) / (0.70 + 1.00 + 1.00)
       = 1.70 / 2.70 ≈ 0.630
s_base = (0.630 + 1) / 2 ≈ 0.815

no vetoes → confidence = 0.81
```
status `supported`: the ceiling result is independently and robustly reproduced (clean atomic physics; conclusion survives the definitional ambiguity and a −1σ-T_e generous test). Held at 0.81, not higher, because the exceedance is only ~2σ given the quoted measurement error, and the result is conditional on the measured T_e and on dust-free intrinsic emissivities.

## Open sub-questions

- Full photoionization grid (Cloudy) with density/ionization stratification — does a realistic single model still undershoot 0.26?
- Atomic-data sensitivity: bracket the ceiling with alternative O III collision-strength sets (~10–20% level expected; insufficient to close a 2× gap, to be confirmed).
- Dust extinction vs genuinely distinct regions — what A_V on the optical line reconciles 0.26, and is it consistent with the SED?
- Robustness of Te=17300 K (the linchpin): is the [OIII]4363 detection/blend secure?

## To read / to audit

- [ ] Cloudy single-zone grid for O III 88μm/5007 at Te=17300 K.
- [ ] Storey & Sochi / alternative O III atomic datasets — re-run ceiling.
- [ ] Tamura et al. 2019 (prior MACS0416-Y1 [OIII]88μm) — cross-check fluxes.

## Changelog

- 2026-05-16: opened. Paper note (B) + audit. Initial confidence 0.81; status `supported`. Note: first audit pass scanned T_e freely and was corrected after sourcing measured Te=17300 K from the full text.
