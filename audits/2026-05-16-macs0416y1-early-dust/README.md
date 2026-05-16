---
slug: 2026-05-16-macs0416y1-early-dust
claim: claims/macs0416y1-early-dust-feasible.md
conventions: SI; flat ΛCDM (H0=67.4, Ωm=0.315, ΩΛ≈0.685, +radiation); optically-thin modified blackbody
verdict: confirmed-with-caveat
audit_layers: [order-of-magnitude, numerical, data-comparison, internal-consistency]
created: 2026-05-16
peer_reviewed: n/a
reviewer_verdicts:
  devil_advocate: n/a
  source_fidelity: n/a
  reproducibility: n/a
---

# MACS0416-Y1 (z=8.312): is ~10⁶ M☉ of dust feasible, and how T_dust-dependent is it?

## Claim under audit

From Takechi et al. 2026 (arXiv:2605.14922), verbatim from abstract:
"…explaining these low dust mass ratios as well as its small dust mass, M_dust ∼ 10⁶ M☉. The intense UV radiation from the AGN may contribute to a high dust temperature of T_dust ≃ 91⁺⁶²₋₃₅ K…", with log(M_dust/M_gas) = −3.60, log(M_dust/M_metal) = −0.95, 12+log(O/H) = 7.86 (≈0.15 Z☉).

Two questions:
1. Is ~10⁶ M☉ of dust *physically feasible* in the cosmic time available at z=8.312?
2. How strongly does the inferred M_dust depend on the (very uncertain) assumed T_dust?

## Source(s)

- [paper note](../../papers/2026-takechi-dreams-macs0416y1-early-dust.md)
- arXiv:2605.14922 abstract (fetched verbatim via `scripts/fetch_arxiv.sh`).

## Audit plan

Order-of-magnitude + numerical, four layers: (1) cosmic time at z=8.312 (manual ∫ vs astropy); (2) internal consistency — do the two dust ratios reproduce the stated metallicity; (3) stellar production budget for metals + dust; (4) modified-blackbody M_dust↔T_dust sensitivity, cross-checked against astropy's blackbody.

## 1–3. Order-of-magnitude / numerical

See `audit.py`; outputs in `outputs/` (`results.json`, `Tdust_Mdust_curve.csv`, `audit_summary.png`).

![MACS0416-Y1 early-dust audit: (left) cosmic time vs redshift, marking 604 Myr at z=8.312; (right) inferred M_dust vs assumed T_dust, showing the steep degeneracy and that a canonical ~40 K solution would exceed the total metal mass (purple dashed, unphysical).](outputs/audit_summary.png)

*Figure — Left: only 604 Myr of cosmic time is available at z=8.312. Right: at fixed observed flux, inferred M_dust falls ×11 going from 40→91 K; the 40 K point sits above the metal-mass ceiling, so the high T_dust is required for the budget to close. Data behind this figure: `outputs/Tdust_Mdust_curve.csv`, `outputs/results.json`.*

**Cosmology.** Flat ΛCDM gives cosmic age **603.9 Myr** at z=8.312 (manual quadrature vs astropy: rel. err 7.8×10⁻⁵). That is the entire dust-formation budget.

**Internal consistency.** From the two stated ratios, M_metal/M_gas = 10^(−3.60) / 10^(−0.95) = 2.24×10⁻³ → **Z ≈ 0.16 Z☉**, vs **0.15 Z☉** independently from 12+log(O/H)=7.86. Agreement to 7% — the dust/gas/metal numbers are mutually consistent. Implied absolute masses: M_metal ≈ 8.9×10⁶ M☉, M_gas ≈ 4.0×10⁹ M☉.

**Production budget.** Making 8.9×10⁶ M☉ of metals needs only ~1.5–3.0×10⁸ M☉ of stars (yield y_Z≈0.03–0.06) → **mean SFR ≈ 0.25–0.49 M☉/yr** over 604 Myr. Entirely modest. SN-only dust supply (CCSN rate 0.006–0.02 /M☉, post-reverse-shock yield 0.01–0.3 M☉) brackets **9×10³ – 1.8×10⁶ M☉**: the *optimistic* end reaches 10⁶ M☉, so SNe can plausibly supply it, and the paper's appeal to additional ISM grain growth near the critical metallicity is reasonable but not strictly required by the budget.

## 4. M_dust ↔ T_dust degeneracy

Optically thin: M_dust ∝ 1/B_ν(T_dust) at fixed flux ⇒ M_dust(T₁)/M_dust(T₂) = B_ν(T₂)/B_ν(T₁). At rest-frame 90 μm (h ν/k = 159.9 K), normalised to 10⁶ M☉ at 91 K:

| T_dust [K] | inferred M_dust [M☉] | ×(vs 91 K) |
|-----------:|---------------------:|-----------:|
| 35 | 1.99×10⁷ | 19.9 |
| 40 | 1.11×10⁷ | 11.1 |
| 50 | 4.90×10⁶ |  4.9 |
| 56 (−1σ) | 3.42×10⁶ |  3.4 |
| 91 | 1.00×10⁶ |  1.0 |
| 153 (+1σ) | 3.85×10⁵ |  0.38 |

Modified-BB ratio matches astropy's `BlackBody` to 6×10⁻¹⁶.

**Key result:** if the dust were at a *canonical* ~40 K instead of 91 K, the inferred dust mass would be **1.1×10⁷ M☉ — larger than the total metal mass (8.9×10⁶ M☉)**, which is unphysical (dust cannot exceed the metals it is made from). So the unusually high T_dust is not merely a fitted parameter: a high T_dust is *required* for the dust budget to close. This is an independent argument supporting the paper's high-T_dust conclusion.

## Result

- Time at z=8.312: **603.9 Myr** (robust).
- Stated dust ratios are internally consistent with 0.15 Z☉ (to 7%).
- ~10⁶ M☉ dust is **feasible** within the stellar budget at a modest SFR (~0.3–0.5 M☉/yr); no "too much dust too early" tension.
- M_dust is **steeply T_dust-dependent** (×11 from 91→40 K); the small dust mass and the high T_dust are physically locked together — a cooler dust solution overproduces dust beyond the metal budget.

## Verdict

`confirmed-with-caveat` — The paper's small-dust / high-T_dust picture is internally consistent and physically feasible, and the high T_dust is independently *required* by the metal-mass ceiling. Caveat: this rests on the adopted rest-90 μm point, single-T modified-BB, β, κ_ν, and the [CII]→M_gas calibration; the absolute M_dust remains uncertain by a factor of several through T_dust alone.

## Caveats and unresolved

- Representative rest wavelength (90 μm) approximate; the *shape* of the M_dust(T) curve is robust but the exact crossover with M_metal shifts with the true ν and β.
- Gas/metal masses inherit the paper's [CII]→M_gas conversion; not independently audited here.
- The [OIII]88μm/5007 anomaly (third headline claim) is **not** audited here — separate audit if pursued.
- SN dust yields and CCSN rates are order-of-magnitude; not a precise chemical-evolution model.

## Changelog

- 2026-05-16: audit created. Verdict: confirmed-with-caveat. Cosmology cross-checked vs astropy; modified-BB vs astropy BlackBody.
