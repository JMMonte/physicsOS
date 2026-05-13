# Reproducibility review — `2026-05-13-casimir-energy-budget`

Reviewer role: reproducibility (per AGENTS.md §2.6).
Date: 2026-05-13.
Reviewer env: `.venv/bin/python` (Python 3.13.7, numpy 2.4.4, scipy/pint/sympy
present).

## Re-run output (key numbers extracted, with line references)

Command:

```
cd /Users/joaomontenegro/Development/physicsOS && \
  .venv/bin/python audits/2026-05-13-casimir-energy-budget/audit.py
```

Exit status: 0. The matplotlib figure
`outputs/casimir-reservoir-and-drain-time.png` was produced.

Key numbers from the run (with the `audit.py` lines that produce them):

| value | result | source line(s) |
|---|---|---|
| chip area | 0.25 cm² (2.5×10⁻⁵ m²) | L62–63 |
| chip power | 37.50 μW | L64 |
| areal power | 1.500 W/m² (= 150.00 μW/cm²) | L65 |
| ℏc | 3.162×10⁻²⁶ J·m | L81 |
| `|E|/A` @ 0.5 nm | 3.467 J/m² | L86, L90–92 |
| `|E|/A` @ 1 nm   | 0.4334 J/m² (4.334×10⁻¹) | L86, L90–92 |
| `|E|/A` @ 10 nm  | 4.334×10⁻⁴ J/m² | L86, L90–92 |
| `|E|/A` @ 100 nm | 4.334×10⁻⁷ J/m² | L86, L90–92 |
| `|E|/A` @ 1 μm   | 4.334×10⁻¹⁰ J/m² | L86, L90–92 |
| drain @ 0.5 nm | 2.311 s | L91 |
| drain @ 1 nm   | 0.2889 s (≈ 289 ms) | L91 |
| drain @ 10 nm  | 2.889×10⁻⁴ s (≈ 289 μs) | L91 |
| drain @ 100 nm | 2.889×10⁻⁷ s (≈ 289 ns) | L91 |
| drain @ 1 μm   | 2.889×10⁻¹⁰ s (≈ 289 ps) | L91 |
| 10-yr reservoir requirement | 4.734×10⁸ J/m² | L99, L102 |
| 10-yr gap | 9.710×10⁻¹³ m (= 971 fm) | L100, L103 |
| photon energy @ 5 GHz | 3.313×10⁻²⁴ J | L111, L113 |
| Wilson 2011 rate | ~10⁵ photons/s ⇒ 3.313×10⁻¹⁹ W per mode | L114–116 |
| needed per μm² mode | 1.500×10⁻¹² W | L118, L120 |
| ratio need/Wilson | 4.528×10⁶ | L119, L121 |
| required `v/c` | 2.1×10³ | L122 |
| σ (computed from k, h, c) | 5.670×10⁻⁸ W·m⁻²·K⁻⁴ | L129 |
| σT⁴ @ 300 K | 459.3 W/m² | L130, L132 |
| claim/σT⁴ ratio | 3.266×10⁻³ | L134 |
| closed form `|E|/A` @ 10 nm | 4.333753×10⁻⁴ J/m² | L158, L161 |
| numerical integral | 4.333753×10⁻⁴ J/m² | L155–158, L162 |
| relative error | 3.181×10⁻⁸ | L159, L163 |

## README/script number-matching results

Every load-bearing number in the README appears in the script output, and the
two agree. Concretely:

| README claim | README text | Script output | Match |
|---|---|---|---|
| `\|E\|/A @ 0.5 nm` | "3.47 J/m²" | "3.467e+00" | yes (3-sig rounding) |
| `\|E\|/A @ 1 nm` | "0.433 J/m²" | "4.334e-01" | yes |
| `\|E\|/A @ 10 nm` | "4.33×10⁻⁴ J/m²" | "4.334e-04" | yes |
| `\|E\|/A @ 100 nm` | "4.33×10⁻⁷ J/m²" | "4.334e-07" | yes |
| `\|E\|/A @ 1 μm`  | "4.33×10⁻¹⁰ J/m²" | "4.334e-10" | yes |
| drain @ 0.5 nm | "2.31 s" | "2.311e+00 s" | yes |
| drain @ 1 nm   | "289 ms" | "2.889e-01 s" | yes |
| drain @ 10 nm  | "289 μs" | "2.889e-04 s" | yes |
| drain @ 100 nm | "289 ns" | "2.889e-07 s" | yes |
| drain @ 1 μm   | "289 ps" | "2.889e-10 s" | yes |
| 10-yr gap     | "d ≈ 9.7×10⁻¹³ m" | "9.710e-13 m" | yes |
| "below proton radius" | proton ≈ 0.84×10⁻¹⁵ m, gap ≈ 9.71×10⁻¹³ m | gap / proton ≈ 1156 × | quantitatively correct: gap is **~3 orders of magnitude LARGER than** the proton, not below it — see flag below |
| sanity rel. error | "3 × 10⁻⁸" | "3.181e-08" | yes |
| DCE need/Wilson ratio | "5 × 10⁶" | "4.528e+06" | yes (correct OOM, rounded a bit high; "≈ 5×10⁶" is a fair round) |
| required v/c | "≳ 2 × 10³" | "2.1e+03" | yes |
| σT⁴ @ 300 K | "≈ 459 W/m²" | "459.3 W/m²" | yes |

Numerical agreement is exact (modulo trivial rounding) for every value in the
README's table and prose.

**One prose/number inconsistency.** README §1, last sentence:

> "To last 10 years, the cavity would need d ≈ 9.7×10⁻¹³ m — three orders of
> magnitude **below the proton radius**."

The script (L100, L103–104) reports d = 9.710×10⁻¹³ m and the proton radius as
~0.84×10⁻¹⁵ m. Therefore d/r_p ≈ 9.71×10⁻¹³ / 0.84×10⁻¹⁵ ≈ **1156**, i.e. the
required gap is roughly **three orders of magnitude *above* the proton radius**,
not below. The number is right; the inequality direction in the README prose is
inverted. This does not change the audit's verdict (a sub-nm cavity gap is still
manifestly outside the regime in which the parallel-plate formula has any
physical meaning, and the script's own comment at L104 says only "for scale",
not "below"), but the README sentence as written is factually backwards. Suggest
either "three orders of magnitude *above* the proton radius — and still well
below any physically realizable plate separation" or simply removing the "below
the proton radius" framing in favour of "≈ 10⁻¹² m, far below any physically
realizable plate separation".

## Equation re-derivation

**Equation re-derived:** `E(d)/A = −π² ℏ c / (720 d³)` (audit.py L76, L86;
README §1).

**Method.** SymPy:

1. Confirmed Riemann ζ(−3) = 1/120 (the regularized sum
   `Σ_n n³ → ζ(−3)` is the standard route in the parallel-plate Casimir
   derivation). SymPy gives `sp.zeta(-3) == 1/120`.
2. The Casimir energy per area for two parallel perfect conductors at T=0 is
   the textbook result obtained by mode-summing the zero-point energy and
   subtracting the unbounded vacuum, yielding
   `E/A = -(π² ℏ c / 720) / d³`. The prefactor 720 = 6 × 120 arises from the
   k_∥ integration (a Γ-function ratio giving 1/6) combined with ζ(−3) = 1/120
   from the n-sum.
3. **Force consistency check (algebraic, not regularization).** Take the
   ansatz `E/A = −α ℏ c / d³` with α = π²/720 and differentiate:
   `−∂(E/A)/∂d = −3 α ℏ c / d⁴ = −π² ℏ c / (240 d⁴)`. SymPy returns
   `F/A = −π² c ℏ / (240 d⁴)`, in agreement with audit.py L143 (which states
   `F(d) = −π² ℏ c A / (240 d⁴)`). The 720/240 ratio is the algebraic
   `3 ⋅ 1/720 = 1/240`.
4. **Inverse integral consistency check.** SymPy:
   `∫_d^∞ π² ℏ c / (240 x⁴) dx = π² ℏ c / (720 d³)`, matching the formula used
   for the reservoir, and matching the numerical sanity check at L154–163.

**Result.** Formula matches the audit's usage in every appearance (L76, L86,
L100, L143, L154–158). Sign and coefficient are both correct.

## Convergence / dimensional / convention checks

### Convergence (numerical vs closed form)

The audit reports rel. error 3.18×10⁻⁸ at N = 100,000 on
`np.geomspace(d, 1e-2, N)` (L155, L163). I re-ran with coarser/finer grids:

| N | numerical integral (J/m²) | rel. error |
|---:|---:|---:|
| 100 | 4.474552×10⁻⁴ | 3.249×10⁻² |
| 1,000 | 4.335134×10⁻⁴ | 3.188×10⁻⁴ |
| 10,000 | 4.333766×10⁻⁴ | 3.182×10⁻⁶ |
| 100,000 | 4.333753×10⁻⁴ | 3.181×10⁻⁸ |
| 1,000,000 | 4.333753×10⁻⁴ | 3.181×10⁻¹⁰ |

Convergence is **real**: error scales as ~1/N² (trapezoid rule on a smooth
integrand on a log grid), bottoming out near double-precision floor. Reducing
the upper limit from 10⁻² m to 10⁻⁴ m at N = 10⁵ does not change the answer to
plotted precision (residual rel. error is dominated by truncation of the tail,
which is 10⁻³³–10⁻³⁴ relative to the dominant near-d region — i.e. negligible).

The sanity check at L154–163 is therefore genuine, not a tuned-for-show
agreement.

### Dimensional analysis (one chain, with units)

Using `pint`:

- `ℏ = 1.054571817×10⁻³⁴ J·s`, `c = 2.99792458×10⁸ m/s`, `d = 10⁻⁸ m`.
- `|E|/A = π² ℏ c / (720 d³)`
  - `[ℏ c] = J·m`; `[d³] = m³`; so `[|E|/A] = J/m² ✓`.
  - Numerical: `4.333753×10⁻⁴ J/m²` — matches script (L161).
- `t_drain = (|E|/A) / P_areal`
  - `[J/m²] / [W/m²] = [s] ✓`.
  - Numerical: `2.889×10⁻⁴ s` — matches script.
- `|F|/A = π² ℏ c / (240 d⁴)`
  - `[J·m] / [m⁴] = J/m³ = N/m² = Pa ✓`.
  - Numerical at d = 10 nm: 1.30×10⁵ Pa (≈ 1 atm) — order of magnitude
    consistent with textbook quotes.
- Stefan–Boltzmann from k_B, h, c (audit.py L129):
  `σ = 2π⁵ k_B⁴ / (15 h³ c²) = 5.670×10⁻⁸ W·m⁻²·K⁻⁴ ✓` (CODATA).
  `σT⁴ @ 300 K = 459.3 W/m² ✓`.
- Photon energy at 5 GHz: `ℏ · 2π · 5×10⁹ Hz = 3.313×10⁻²⁴ J ✓`.

No unit errors found.

### Conventions

README frontmatter (L4): `SI; parallel-plate idealization; perfect conductors at
T=0 for reservoir bound; 300 K for thermal context`.

audit.py docstring (L19): `Conventions: SI throughout. Constants from scipy.`

The script:

- pulls `ℏ, c, k_B, h` from `scipy.constants` (L33–40), all SI — matches.
- uses the perfect-conductor T=0 parallel-plate formula at L86 for the
  reservoir — matches "perfect conductors at T=0".
- uses 300 K only for the σT⁴ thermal context at L128 — matches.
- DCE section (L108–122) at 5 GHz cavity — order-of-magnitude probe, no
  convention required beyond SI; matches.

Conventions header is consistent with the implementation.

## Verdict

**Fully reproduces.**

The script runs cleanly on the project venv. Every load-bearing number in the
README's tables and prose (reservoir energies, drain times, 10-year gap, DCE
ratio and v/c bound, σT⁴, sanity rel. error) matches the script output to the
significant figures quoted. The central equation `E/A = −π² ℏ c / (720 d³)` and
its derivative `F/A = −π² ℏ c / (240 d⁴)` are re-derived by SymPy and confirmed
analytically; the integral relation
`∫_d^∞ (π² ℏ c / 240) x⁻⁴ dx = π² ℏ c / (720 d³)` holds exactly. Numerical
convergence of the sanity integral is genuine (~1/N²). Dimensional analysis
through one full chain (`ℏ c / d³ → J/m²`, then `/ (W/m²) → s`) checks out, as
does σT⁴ via k_B, h, c.

**One minor prose flag, not affecting the verdict:** the README states the
10-year gap is "three orders of magnitude below the proton radius", but the
numbers (9.71×10⁻¹³ m vs 0.84×10⁻¹⁵ m) place it three orders of magnitude
**above** the proton radius. The argument the audit is making (that this is
not a physically realizable plate separation) is still correct; the comparison
is just inverted in the prose.
