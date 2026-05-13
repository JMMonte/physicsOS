---
slug: 2026-05-13-casimir-energy-budget
claim: ../../claims/casimir-quantum-energy-chip-feasibility.md
conventions: SI; parallel-plate idealization; perfect conductors at T=0 for reservoir bound; 300 K for thermal context
verdict: contradicted
audit_layers: [dimensional, limits, order-of-magnitude, symbolic, numerical, data-comparison]
created: 2026-05-13
---

# Casimir energy-budget audit of the Casimir Inc. "MicroSparc" chip

> **Worked example (audit 1 of 2).** This is the first-pass audit in the physicsOS worked example. It establishes the categorical obstructions to the claim. See [`../../README.md`](../../README.md) for the framing and the [companion steelman audit](../2026-05-13-casimir-steelman-energy-ledger/) for the second pass.

## Claim under audit

> The "MicroSparc" chip (5 mm × 5 mm) produces **1.5 V at 25 μA continuously**
> (≈ 37.5 μW, areal power **1.5 W/m²**), with **no degradation and no
> replacement cycle**, by harvesting "quantum vacuum" energy from engineered
> Casimir cavities.

Source: Casimir Inc. press release, 2026-05-12 — see
[`papers/2026-businesswire-casimir-press-release.md`](../../papers/2026-businesswire-casimir-press-release.md).

## Sources used in the audit

- Jaffe 2005, *Phys. Rev. D* 72, 021301(R) — [paper note](../../papers/2005-jaffe-casimir-without-vacuum-energy.md). The Casimir effect can be computed without ever invoking vacuum energy; the popular "tap the vacuum" framing is a category error.
- Chernodub 2013, *Phys. Rev. D* 87, 025021 — [paper note](../../papers/2013-chernodub-rotating-casimir-perpetual-motion.md). Closest serious attempt at "Casimir perpetual motion"; explicitly produces **no** usable work.
- Pinto 1999–2003 patent family — [paper note](../../papers/1999-pinto-casimir-engine-patents.md). The only theoretically plausible Casimir-engine route is boundary-property modulation, and no demonstration of net energy gain exists in 27 years.
- White et al. 2026, *Phys. Rev. Research* 8, 013264 — [paper note](../../papers/2026-white-emergent-quantization-dynamic-vacuum.md). The cited "theoretical foundation" does not, in fact, address energy extraction.

## Audit plan

Five orthogonal checks. Any one of these refuting the claim is enough; all five do.

### 1. Casimir static reservoir size

Between perfectly conducting parallel plates at T=0:

$$
\frac{|E(d)|}{A} = \frac{\pi^2 \hbar c}{720\, d^3}
$$

This is an **upper bound** on the energy a real cavity could deliver as it relaxes from gap $d$ to 0. Numerical values (full ledger in `audit.py`):

| gap $d$ | $|E|/A$ | drain time at 1.5 W/m² |
|---------|---------|------------------------|
| 0.5 nm  | 3.47 J/m²        | 2.31 s    |
| 1 nm    | 0.433 J/m²       | 289 ms    |
| 10 nm   | 4.33 × 10⁻⁴ J/m² | 289 μs    |
| 100 nm  | 4.33 × 10⁻⁷ J/m² | 289 ns    |
| 1 μm    | 4.33 × 10⁻¹⁰ J/m²| 289 ps    |

To last **10 years**, the cavity would need $d \approx 9.7 \times 10^{-13}\,\mathrm{m}$ — three orders of magnitude **below the proton radius**. The parallel-plate Casimir formula has no physical meaning at that scale.

### 2. Limit and convergence check

Numerical $\int_d^\infty F(x)/A\,dx$ vs closed-form $|E|/A$ at $d=10$ nm: relative error $3 \times 10^{-8}$. Reservoir math is correct.

### 3. Dynamical Casimir effect (DCE) bound

Wilson et al. (2011, *Nature* 479, 376) experimentally demonstrated DCE in a superconducting circuit at ~5 GHz, producing roughly $10^5$ photons/s — i.e., ~$3 \times 10^{-19}$ W per mode. The claim requires ~$1.5 \times 10^{-12}$ W per 1 μm² mode: a $5 \times 10^{6}\times$ boost in photon-production rate. DCE rate scales as $(v/c)^2$ for slow boundaries, so closing this gap requires boundary velocities $v/c \gtrsim 2 \times 10^3$ — i.e., **kinematically impossible** ($v < c$). A passive solid-state chip with no relativistic moving parts cannot pump DCE.

### 4. Thermal/second-law check

At 300 K, the chip sits in a blackbody bath of $\sigma T^4 \approx 459\,\mathrm{W/m^2}$. The advertised 1.5 W/m² is small *compared to* this bath, but that is not a permission — it is a problem. The second law forbids extracting net work from a single-temperature reservoir with a passive device. Any net power output requires either (i) a temperature gradient or (ii) an active modulation that costs more energy than is delivered. The press release describes neither.

### 5. Conservativity

The Casimir force at fixed boundary properties is the gradient of a potential. Closed cycles in plate separation alone net **zero work**. The only known theoretical loophole is Pinto-style modulation of a boundary property; even there, no replicated experiment has shown net energy gain in 27 years. The press release supplies no mechanism, no ledger, no demonstration.

## Result

The advertised performance is inconsistent with every relevant physical bound:

- The static reservoir at any meaningful plate gap is at least **4 orders of magnitude** too small to deliver the advertised power continuously, even ignoring the cycling requirement.
- The cycling requirement adds the conservative-force obstruction.
- DCE pumping requires boundary motion well beyond the speed of light.
- Passive operation in a single-T bath is forbidden by the second law.
- The cited theoretical paper does not address energy extraction.

## Verdict

**CONTRADICTED.** The claim of continuous, degradation-free, ambient-temperature, passive 1.5 W/m² extraction from "quantum vacuum fields" is incompatible with the Casimir effect as currently understood, with the dynamical Casimir effect demonstrated to date, and with the second law of thermodynamics.

## Caveats and unresolved

- This audit treats the chip as a parallel-plate static cavity at T=0 (for the reservoir bound) and as a passive device at 300 K (for the thermal check). The company has disclosed neither the geometry nor any mechanism beyond marketing language, so a more specific audit is not possible from public information.
- If Casimir Inc. is in fact running a Pinto-style modulated-boundary engine, the audit's conservativity argument can be partly relaxed — but the energy-ledger problem (modulation drive ≥ extracted power) then becomes paramount, and remains unanswered in the public record.
- The audit does **not** rule out that the chip produces *some* output by ordinary means (thermal energy harvesting, photovoltaic, RF rectification, thermoelectric). It rules out that the output, if real, comes from "quantum vacuum" in the sense any physicist would recognize.

## How the company can rebut

For this audit to be revised toward `supported`, Casimir Inc. would need to publish (at minimum) **all of**:

1. A peer-reviewed paper describing the cavity geometry, boundary materials, and mode structure.
2. A complete energy ledger: input power (modulation drive, biases, optical pump, etc.) vs delivered electrical output, with uncertainties.
3. An independent replication by a non-affiliated experimental group.
4. A measurable, falsifiable scaling prediction (output vs gap, vs temperature, vs cavity area) consistent with their stated mechanism.

The PRR 2026 paper is, on its own, not a rebuttal. It is an analytic curiosity in a separate problem (hydrogenic spectrum from a fluid analog) and contains no statement about device operation.

## Changelog

- 2026-05-13: audit created. Verdict: contradicted.
