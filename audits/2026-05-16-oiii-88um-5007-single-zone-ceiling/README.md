---
slug: 2026-05-16-oiii-88um-5007-single-zone-ceiling
claim: claims/macs0416y1-oiii-ratio-anomaly.md
conventions: SI; O III 5-level atom (PyNeb 1.1.30); dust-free intrinsic emissivities; energy (flux) ratio
verdict: confirmed-with-caveat
audit_layers: [order-of-magnitude, numerical, internal-consistency, source-fidelity]
created: 2026-05-16
peer_reviewed: n/a
reviewer_verdicts:
  devil_advocate: n/a
  source_fidelity: n/a
  reproducibility: n/a
---

# Does [OIII]88μm/[OIII]5007 = 0.26 exceed the single-zone photoionization ceiling at MACS0416-Y1's measured T_e?

## Claim under audit

Takechi et al. 2026 (arXiv:2605.14922): "[OIII]88μm/[OIII]5007 = 0.26 ± 0.06 … above predictions from single ionized nebular models at any electron density … the [OIII]88μm and [OIII]5007 trace largely distinct regions, with the optical line suppressed in dusty nebulae."

Tested as the paper actually frames it — **conditional on the measured electron temperature**.

## Source(s)

- [paper note](../../papers/2026-takechi-dreams-macs0416y1-early-dust.md)
- arXiv:2605.14922 — abstract (verbatim via `scripts/fetch_arxiv.sh`) + full text for the measured T_e/n_e (sourced, not recalled): **Te[OIII] = 17300 ± 1500 K** (from [OIII]4363), **n_e = 730⁺¹⁵⁰₋₁₄₀ cm⁻³** (from [OII]3726/3729).
- Atomic data: O III radiative `o_iii_atom_FFT04-SZ00.dat` (Froese Fischer & Tachiev 2004; Storey & Zeippen 2000); collisional `o_iii_coll_SSB14.dat` (Storey, Sochi & Bautista 2014).

## Audit plan

Solve the O III 5-level atom (PyNeb) for the intrinsic energy-emissivity ratio R = ε(88μm)/ε(5007). Because R(same ion) is independent of O⁺⁺ abundance, it depends only on atomic physics + T_e + n_e. Fix T_e at the measured value (and its −1σ, the most generous to a high ratio), scan n_e ∈ [1,10⁶] cm⁻³, and find the single-zone ceiling. Cross-check atom (5007/4959 ≈ 2.98), the definitional ambiguity, and quantify the conditioning on T_e.

## 1. Atom sanity

5007/4959 = 2.984 at (15 kK, 10² cm⁻³) — matches the A-value-set theoretical ≈2.98. Line identifications correct (88μm = 883322 Å; 5007 = 5006.8 Å; 4363 = 4363.2 Å). n_crit(³P₁, 88μm upper) ≈ 5.9×10² cm⁻³; n_crit(¹D₂, 5007 upper) ≈ 8.2×10⁵ cm⁻³ — the large separation is *why* R is density-sensitive and why its ceiling is the low-density limit.

## 2. Numerical result (primary test, at measured T_e)

| Quantity | Value |
|---|---|
| Single-zone ceiling R, max over all n_e, at T_e=17300 K | **0.129** |
| Ceiling at T_e=15800 K (−1σ, most generous) | **0.151** |
| Single-zone R at the measured point (17300 K, 730 cm⁻³) | **0.037** |
| Observed | **0.26 ± 0.06** |
| Observed / ceiling(17300 K) | **2.0×** |
| Observed − ceiling(15800 K) | 0.109 (**1.8σ** of the measurement) |
| Reproducible by any single dust-free zone at measured T_e? | **No** |
| Ceiling if optical = (4959+5007) instead of 5007 | 0.113 → conclusion **robust** to that ambiguity |

The ceiling is exactly the n_e→0 limit (88μm is collisionally quenched above its ~600 cm⁻³ critical density; at the measured n_e=730 the single-zone ratio is only 0.037, ~7× below observed).

## 3. Source-fidelity / devil's-advocate finding (caveat, quantified)

The statement "above single-zone predictions at *any* electron density" is **only meaningful because T_e is independently pinned high by [OIII]4363**. R = ε(88)/ε(5007) falls steeply with T_e (5007 ∝ exp(−2.9×10⁴/T_e); 88μm T-flat). With T_e *free*, the single-zone ceiling reaches 0.26 for T_e ≲ **12200 K** and diverges at low T_e. The measured 17300 K sits well above that crossover, so the anomaly is real *given the measured temperature* — but it is a conditional, not an absolute, statement about O III. (My first pass scanned T_e freely and spuriously found 0.26 trivially reachable; sourcing the measured T_e from the full text corrected this.)

## Result

At the measured T_e = 17300 ± 1500 K, no single dust-free photoionized O III zone reproduces 0.26 at any n_e; the intrinsic ceiling is ≈0.13 (≤0.15 even at −1σ T_e). The observation is ~2× / ~1.8–2.2σ above that ceiling. This is consistent with the paper's interpretation that the optical [OIII]5007 is suppressed (dust and/or a physically distinct, denser/cooler optical-emitting zone), since extinction or zone-separation raises the observed 88μm/5007 above the single-zone intrinsic value.

## Verdict

`confirmed-with-caveat` — The paper's claim holds **as stated (conditional on the measured T_e)**: 0.26 exceeds the single-zone ceiling (≈0.13) by ~2×. Caveats: (1) significance is only ~1.8–2.2σ given the quoted ±0.06; (2) it is a fixed-T_e statement — not that O III can never yield 0.26; (3) assumes dust-free intrinsic emissivities, which is precisely the effect the paper invokes (so this supports, not tests, their dust-suppression reading); (4) PyNeb default atomic data — a different O III collision dataset could shift the ceiling at the ~10–20% level (not enough to close a 2× gap).

## Caveats and unresolved

- Did not run a full Cloudy/photoionization grid (ionization structure, density stratification); the 5-level single-zone ceiling is an upper bound on the single-zone prediction, which is the relevant quantity for the claim.
- The dust-suppression vs distinct-regions distinction is not resolved here — only that a single dust-free zone is insufficient.
- Atomic-data sensitivity not bracketed with alternate datasets (open follow-up).

## Changelog

- 2026-05-16: created. Verdict: confirmed-with-caveat. PyNeb 1.1.30 installed into `.venv` for vetted O III atomic data (logged tooling gap → resolved). Measured T_e/n_e sourced from arXiv full text.
