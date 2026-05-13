# Reproducibility review — 2026-05-13-casimir-steelman-energy-ledger

Reviewer: cross-context subagent (reproducibility role)
Date: 2026-05-13
Environment: project venv at `/Users/joaomontenegro/Development/physicsOS/.venv`,
Python 3.13.7, NumPy 2.4.4, SciPy stack, pint.

Invocation:

```
cd /Users/joaomontenegro/Development/physicsOS
.venv/bin/python audits/2026-05-13-casimir-steelman-energy-ledger/audit.py
```

Script ran cleanly to completion. Both output artifacts were regenerated:
`outputs/sensitivity.csv` (45 data rows + header) and `outputs/ledger_vs_fmod.png`.

## Re-run output (key numbers extracted, with line references)

Reproduced numbers from the run (line numbers refer to `audit.py`):

| Quantity | Script output | Source location |
|---|---|---|
| seed | 0 | line 60–62 |
| Casimir \|E\|/A at d=100 nm | 4.334e−7 J/m² | `casimir_energy_per_area` (line 92–100), printed lines 124, 135 |
| Casimir pressure at 100 nm | 1.300e+1 Pa | `casimir_pressure` line 103–106, printed 136 |
| ω_cavity = πc/d | 9.418e+15 rad/s | line 238, printed 241 |
| Required Δn (carrier swing) | 3.902e+26 /m³ = 3.902e+20 /cm³ | line 240 |
| σ surface charge | 3.126 C/m² | line 246 |
| U_capacitor_per_area | 3.246e+10 (printed as J/m²) | line 251 — see "convention checks" |
| E0 drive field | 2.077e+10 V/m | line 269, printed 270 |
| P_extracted (1 GHz, dR=1, 100 nm) | 4.334e+2 W/m² | line 173, printed 176 |
| P_drive (Drude, as reported) | 3.246e+19 W/m² | line 260, printed 262 |
| p_loss volumetric | 2.855e+18 W/m³ | line 278, printed 281 |
| P_drive (dielectric, areal) | 1.428e+11 W/m² | line 279, printed 282 |
| P_drive (VO₂ latent) | 1.953e+10 W/m² | line 305, printed 306 |
| P_net headline (min of three) | −1.953e+10 W/m² | line 354 |
| Sweep, # P_net > 0 | 0 / 45 | line 526 |
| Sweep, # P_net > claim | 0 / 45 | line 527 |
| Least-negative sweep P_net | −1.428e+6 W/m² (d=1000 nm, f=0.1 GHz) | sorted top of sweep_rows |
| pint E/A check | 4.334e−7 J/m² | line 483 |
| pint p_loss check | 2.855e+18 W/m³ | line 490 |

## README/script number-matching results

Every load-bearing number in the README cross-checks against the script output
within rounding of the printed precision:

| README claim | README value | Script value | Match? |
|---|---|---|---|
| Static \|E\|/A at 100 nm | 4.33×10⁻⁷ J/m² | 4.334e−7 | ✓ |
| P_extracted (ΔR=1, 1 GHz) | 4.33×10² W/m² | 4.334e+2 | ✓ |
| Extracted/claim ratio | 289× | 4.334e2/1.5 = 288.9 | ✓ |
| ω_cavity | ≈9.4×10¹⁵ rad/s | 9.418e+15 | ✓ |
| Carrier swing Δn | ≈3.9×10²⁰ /cm³ | 3.902e+20 | ✓ |
| Surface charge σ | ≈3.1 C/m² | 3.126 | ✓ |
| E-field amplitude | 2×10¹⁰ V/m | 2.077e+10 | ✓ |
| E₀ / air-breakdown | ~7000× | 6923× | ✓ |
| E₀ / InSb-breakdown | ~2×10⁴× | 2.08e+4 | ✓ |
| P_drude floor (as reported by script) | ~3×10¹⁹ W/m² | 3.246e+19 | ✓ (but see convention check below — there is a dimensional error in the formula) |
| P_dielectric floor | ≈1.4×10¹¹ W/m² | 1.428e+11 | ✓ |
| P_VO₂ floor | ≈2×10¹⁰ W/m² | 1.953e+10 | ✓ |
| P_net headline (best of) | −2×10¹⁰ W/m² | −1.953e+10 | ✓ |
| Drive/extracted (charitable) | 4.5×10⁷ | 1.953e10 / 4.334e2 = 4.506e7 | ✓ |
| Sweep result | 0 / 45 positive net | 0 / 45 (confirmed in CSV and stdout) | ✓ |
| Sweep result | 0 / 45 above claim | 0 / 45 | ✓ |
| Least-negative net | −1.4×10⁶ W/m² | −1.428e+6 | ✓ |

No numerical mismatches between README tables and script output as printed.

## Equation re-derivation (which equation; method; result; agreement)

Re-derived three of the four load-bearing equations symbolically with SymPy
(independent of the script), then numerically substituted:

1. **Casimir energy per area** `|E|/A = π² ℏc / (720 d³)` (line 100).
   Standard zeta-regularized parallel-plate result. Numerical evaluation at
   d = 100 nm gives 4.3338e−7 J/m². **Matches script.**

2. **Casimir pressure** `P_Cas = π² ℏc / (240 d⁴)` (line 106). Confirmed by
   symbolic differentiation: `−d/dd[−π² ℏc/(720 d³)] = π² ℏc/(240 d⁴)`.
   At 100 nm gives 13.00 Pa. **Matches script.**

3. **Dielectric-loss volumetric** `p_loss = (1/2) ω ε₀ ε_r tan δ E₀²`
   (line 278). Standard from Im[ε] = ε_r tan δ. With E₀ = σ/(ε₀ ε_r), ω = 2π·1 GHz,
   ε_r = 17, tan δ = 0.014, gives 2.855e+18 W/m³, and times h_mod = 50 nm gives
   1.428e+11 W/m². **Matches script.**

4. **VO₂ latent-heat floor** `P = 2 f_mod ρ ΔH h_mod` (line 305). Trivially
   correct: ρ·ΔH = 1.953e+8 J/m³ (matches script print at line 304); times
   2·f_mod·h_mod = 2·10⁹·5e−8 gives 1.953e+10 W/m². **Matches script.**

5. **Drude carrier-swing electrostatic floor** (line 251, 260). The chain
   ω_cav = πc/d, Δn = ε₀ m_eff ω_cav²/e², σ = e Δn h_mod, all match my
   symbolic substitution numerically. However the *next* step has a unit
   problem — see "Dimensional / convention checks" below.

## Sensitivity-sweep verification

- The 5 × 3 × 3 = 45 sweep produces a 46-line CSV
  (`outputs/sensitivity.csv`: header + 45 data rows, confirmed via `wc -l`).
- All 45 rows confirmed via independent Python read of CSV:
  - 0 rows have `P_net_W_per_m2 > 0` (sweep loop at line 361–394).
  - 0 rows have `P_net_W_per_m2 > 1.5` (claim threshold).
  - Most positive (least-negative) net: d=1000 nm, f=0.1 GHz, dR=0.1 → −1.428e+6 W/m²,
    matching README's "−1.4 × 10⁶ W/m²" for largest gap, lowest frequency.
  - (README says "full ΔR" gives the least-negative; in this CSV all three ΔR
    values at d=1000 nm, f=0.1 GHz tie at exactly −1.427524e+06 because the
    operative cost is the gap-independent dielectric-loss floor, which doesn't
    depend on ΔR. The dR=1 row is the most generous on the *extracted* side but
    the dominant drive term washes it out. Minor README imprecision, not an
    error.)
- **Density of the sweep.** The coverage is 3 frequency decades (0.1–10 GHz) and
  2 gap decades (10–1000 nm). The conclusion is robust by orders of magnitude
  (least-negative point is still ~10⁶ W/m² in the red), so the coarseness of the
  grid is not load-bearing. A denser sweep cannot change the sign of net power
  unless an unbounded parameter is added — and the analytic gap-scaling
  `|E|/A ∝ 1/d³` shows extracted plummets at large d while the dielectric floor
  only drops as 1/d⁴ (through Δn ∝ 1/d²), so smaller gaps make the imbalance
  worse, not better. The sweep is informatively dense.

## Dimensional / convention checks

**Convention header check.** Front-matter says: "SI; parallel-plate idealization
with perfect-conductor reservoir at T=0; modulator at 300 K". The script uses SI
throughout (scipy.constants `hbar`, `c`, `epsilon_0`; SI units everywhere), the
perfect-conductor T=0 parallel-plate Casimir formula at line 100, and the
modulator-at-300-K is implicit in the InSb/VO₂ material parameters (room-T
values). **Conventions match.**

**Full dimensional chain (pint, independent of the script).** I walked through
the chain ω_cav → Δn → σ → E₀ → U → P_drude with `pint` units enforced at
each step. Reproduced numerical values match the script exactly through E₀.
**But** at the `U_capacitor_per_area` step (line 251), `sigma²/(2 ε₀ ε_r)` has
dimensions `[mass]/([time]²·[length]) = J/m³`, **not J/m² as the variable name
and print statement claim**. Pint refuses to convert it to J/m².

Mechanically: the energy per *area* of a parallel-plate capacitor with surface
charge σ and dielectric thickness `t` is
`U/A = σ² t / (2 ε₀ ε_r)` — i.e., an extra factor of `t`. With the modulator
thickness `h_mod = 50 nm`, the *correct* U/A is
3.246e+10 × 5e−8 = **1.62×10³ J/m²**, not 3.246e+10 J/m². Equivalently, the
script as written is computing a volumetric energy density and treating it as
an areal one.

Consequence: the reported **P_drude = 3.246e+19 W/m²** is too large by a factor
of `1/h_mod ≈ 2×10⁷`. The corrected Drude floor is

```
P_drude_corrected ≈ (1−η) · (σ² h_mod / (2 ε₀ ε_r)) · 2 f_mod
                 ≈ 0.5 · 1.62e+3 · 2 · 1e9
                 ≈ 1.6×10¹² W/m².
```

**Impact on the verdict.** The headline ledger uses `min(P_drude, P_diel, P_VO₂)`
(line 347), and the min is VO₂ (1.95×10¹⁰), so the charitable headline
(−2×10¹⁰ W/m²) is unchanged. The "honest" ledger uses `max(...)` and the script
quotes "another ~10⁹" worse than min — which becomes "another ~10²" after
correction (max becomes 1.6×10¹² vs min 1.95×10¹⁰). The corrected Drude is
still ~10⁹× larger than P_extracted (4.33×10²), so **the verdict CONTRADICTED is
unchanged**, but the README's prose claim that the "honest figure" is "worse by
another ~10⁹ (Drude floor dominates)" overstates by ~7 orders of magnitude.

Other dimensional checks are clean: the explicit `pint` block in the script
(lines 477–491) successfully converts `|E|/A` to J/m² and `p_loss` to W/m³ —
that is, the formulas the script chose to pint-check are correct. The pint check
just does not cover the Drude-capacitor step where the error sits.

**Sweep-row impact.** The sweep at line 374 has the same `U_cap_ = sigma_**2 /
(2 * EPS0 * eps_r_InSb)` formula, so every `P_drive_drude_W_per_m2` column in
`outputs/sensitivity.csv` is high by ~`1/h_mod ≈ 2×10⁷`. The `P_net` column,
however, uses `min(P_drude_, P_diel_, P_VO2_)` (line 385) and Drude is never the
min in any row (it is at minimum ~75× larger than the dielectric floor), so
`P_net` is unaffected. The 0/45 result stands.

## Verdict

**Numerical discrepancies.** The script runs cleanly and every printed number
matches the README. However, the Drude carrier-swing electrostatic-floor
formula on line 251 (and replicated at line 374) confuses energy per volume
with energy per area: it omits the factor `h_mod`. The reported P_drude of
3.2×10¹⁹ W/m² is therefore high by a factor `1/h_mod ≈ 2×10⁷`; the correct
value is ~1.6×10¹² W/m².

This does not change the audit's CONTRADICTED verdict — even corrected, the
Drude floor (1.6×10¹²) is still ~4×10⁹× the extracted power (4.33×10²), the
charitable `min`-of-three headline (VO₂-limited at −1.95×10¹⁰ W/m²) is
unchanged, and the 0/45 sweep result is unchanged. It does affect the
quantitative prose: the README's "drive = max of three… worse by another ~10⁹"
overstates the Drude-dominant deficit by ~7 decades. The Drude floor still
dominates the three, but by ~10× not ~10⁹×.

Recommendation: replace line 251 with
`U_capacitor_per_area = sigma_surf**2 * h_mod / (2.0 * EPS0 * eps_r_InSb)`
(and similarly in the sweep at line 374), re-run, and adjust the README's
"~10⁹" prose accordingly.
