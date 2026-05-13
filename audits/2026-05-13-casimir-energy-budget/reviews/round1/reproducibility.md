# Reproducibility review — 2026-05-13-casimir-energy-budget

## Re-run output (key numbers extracted, with line references)

Re-ran `audit_script.py` with `/Users/joaomontenegro/Development/physicsOS/.venv/bin/python`. Stdout is byte-identical to `audit_raw_output.txt` modulo the outputs/ path (script writes to `/tmp/outputs/...` when run from /tmp). All printed values match exactly:

- `audit_script.py:62-65` → claim: 0.25 cm² area, 37.50 μW, 1.500 W/m².
- `audit_script.py:85-92` → reservoir table at d ∈ {0.5, 1, 10, 100, 1000} nm: |E|/A = {3.467, 4.334e-1, 4.334e-4, 4.334e-7, 4.334e-10} J/m²; drain times {2.311, 2.889e-1, 2.889e-4, 2.889e-7, 2.889e-10} s.
- `audit_script.py:98-106` → 10-yr drain ⇒ d ≈ 9.710e-13 m (≈ 1.2e3 × proton radius, ≈ 1.8e-2 × Bohr radius).
- `audit_script.py:112-124` → DCE: E_γ@5GHz=3.313e-24 J, Wilson rate→3.313e-19 W/mode, need/demonstrated ratio = 4.528e6, √ratio ≈ 2.1e3.
- `audit_script.py:130-136` → σT⁴(300 K) = 459.3 W/m²; claim/σT⁴ = 3.27e-3.
- `audit_script.py:156-165` → numerical ∫F/A vs closed-form |E|/A at d=10 nm: rel.err = 3.18e-8.

## README/script number-matching results

Walked every load-bearing number in `audit_premises_README.md` §1–§4 against the script output and against an independent recomputation. All match:

| README quantity | README value | Script/recompute | Status |
|---|---|---|---|
| |E|/A @ 0.5 nm | 3.47 J/m² | 3.467e+00 J/m² | match |
| |E|/A @ 1 nm | 0.433 J/m² | 4.334e-01 J/m² | match |
| |E|/A @ 10 nm | 4.33e-4 J/m² | 4.334e-04 J/m² | match |
| |E|/A @ 100 nm | 4.33e-7 J/m² | 4.334e-07 J/m² | match |
| |E|/A @ 1 μm | 4.33e-10 J/m² | 4.334e-10 J/m² | match |
| Drain @ 0.5 nm | 2.31 s | 2.311 s | match |
| Drain @ 1 nm | 289 ms | 2.889e-1 s | match |
| Drain @ 10/100 nm / 1 μm | 289 μs / 289 ns / 289 ps | 2.889e{-4,-7,-10} s | match |
| 10-yr drain gap | 9.7e-13 m | 9.710e-13 m | match |
| ~10³ × proton radius | qualitative | 1.2e3× | match |
| DCE relative-error sanity | 3 × 10⁻⁸ | 3.18e-8 | match |
| √ratio v/c bound | ≳ 2 × 10³ | 2.13e3 | match |
| σT⁴ @ 300 K | ≈ 459 W/m² | 459.3 W/m² | match |

No mismatches.

## Equation re-derivation

**Equation:** |E(d)|/A = π² ℏ c / (720 d³) (`audit_script.py:85-86`).

**Method:** (a) re-derived the force from this energy by d/dd: |F|/A = 3 π² ℏ c / (720 d⁴) = π² ℏ c / (240 d⁴), reproducing `audit_script.py:145`'s force expression. (b) re-integrated that force from d to ∞: ∫_d^∞ π² ℏ c / (240 x⁴) dx = π² ℏ c / (720 d³), recovering the energy. (c) Independently evaluated at d = 1 nm with SI constants: 4.333753e-01 J/m², agreeing with the script.

**Stefan–Boltzmann cross-check:** the script writes σ = 2π⁵k⁴/(15 h³ c²) (`:131`). Standard form σ = π²k⁴/(60 ℏ³ c²); substituting ℏ³ = h³/(2π)³ gives σ = 2π⁵k⁴/(15 h³ c²). Numerical value 5.670374e-08 W/m²/K⁴ — matches CODATA. Conventions agreement confirmed.

## Convergence / dimensional / convention checks

- **Convergence:** numerical integral of |F|/A from 10 nm to 10 mm matches closed-form |E|/A to 3.18e-8 relative error — consistent with trapezoidal error on a smooth ∼1/x⁴ integrand over 100 000 log-spaced samples.
- **Dimensional chain (full):** [ℏ]=J·s, [c]=m/s, [ℏc]=J·m. [ℏc/d³]=J/m². Plugging d=1 nm: π²·(1.0546e-34)(2.998e8)/(720·(1e-9)³) = 0.4334 J/m². Drain time = (J/m²)/(W/m²) = s = 0.4334/1.5 = 0.289 s. Units consistent end-to-end.
- **Conventions:** README header says "SI; parallel-plate idealization; perfect conductors at T=0 for reservoir bound; 300 K for thermal context". Script uses SI scipy constants, parallel-plate formula (`:85`), T=0 reservoir, and T=300 K only for blackbody context (`:130`). Conventions match.

## My independent verdict on the audit

The audit is numerically and algebraically tight. The central identities (Casimir energy density, force, Stefan–Boltzmann) are correct in form and value; every README-quoted number reproduces from the script and from independent recomputation; the convergence sanity passes; units are consistent. The DCE photon-rate (1e5 photons/s/mode) is an OOM placeholder from Wilson 2011 and the audit flags it as such — appropriate caveat; conclusion is insensitive to a 10× swing because the ratio is 4.5e6. The §4 thermal argument is properly scoped (Kelvin–Planck on a single-T reservoir) and the README correctly notes the spectral-structure objection and rebuts it. §5 conservativity correctly notes the Pinto loophole and defers quantitative ledger to the steelman audit.

## Final verdict

**fully reproduces**
