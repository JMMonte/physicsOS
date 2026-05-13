---
slug: 2026-05-13-casimir-energy-budget
claim: ../../claims/casimir-quantum-energy-chip-feasibility.md
conventions: SI; parallel-plate idealization; perfect conductors at T=0 for reservoir bound; 300 K for thermal context
verdict: contradicted
audit_layers: [dimensional, limits, order-of-magnitude, symbolic, numerical, data-comparison]
created: 2026-05-13
peer_reviewed: 2026-05-13
peer_reviewed_rounds:
  round0: 2026-05-13 (pre-sandbox; see round0/_NOTE.md)
  round1: 2026-05-13 (sandboxed per AGENTS.md §2.6)
reviewer_verdicts:
  devil_advocate: minor issues       # round1; round0 was 'substantive issues' on a pre-revision audit
  source_fidelity: all sources accurately represented   # round1; round0 was 'minor mismatches' (caught Wilson missing paper note — invisible to a sandboxed reviewer by design)
  reproducibility: fully reproduces  # consistent across rounds
---

# Casimir energy-budget audit of the Casimir Inc. "MicroSparc" chip

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
- Wilson et al. 2011, *Nature* 479, 376 (arXiv:1105.4714) — [paper note](../../papers/2011-wilson-dynamical-casimir-effect.md). First experimental observation of the dynamical Casimir effect, in a parametrically modulated superconducting circuit.

## Audit plan

Five orthogonal checks. Any one of these refuting the claim is enough; all five do.

### 1. Casimir static reservoir — instantaneous bound

Between perfectly conducting parallel plates at T=0:

$$
\frac{|E(d)|}{A} = \frac{\pi^2 \hbar c}{720\, d^3}
$$

This is the **instantaneous** energy per unit area available between the plates at gap $d$ — i.e., the upper bound on the energy a *static* cavity could deliver as it relaxes from gap $d$ to 0. It is not by itself a power bound: a cycling engine could in principle deliver this energy repeatedly. The power bound for a cycling engine is set instead by the per-cycle work $\Delta E_{\text{cycle}}$ and the cycle frequency — see §5 (Conservativity) and the [companion steelman audit](../2026-05-13-casimir-steelman-energy-ledger/) for the cycling case.

Numerical values of the static reservoir (full ledger in `audit.py`):

| gap $d$ | $|E|/A$ | drain time at 1.5 W/m² (one-shot) |
|---------|---------|-----------------------------------|
| 0.5 nm  | 3.47 J/m²        | 2.31 s    |
| 1 nm    | 0.433 J/m²       | 289 ms    |
| 10 nm   | 4.33 × 10⁻⁴ J/m² | 289 μs    |
| 100 nm  | 4.33 × 10⁻⁷ J/m² | 289 ns    |
| 1 μm    | 4.33 × 10⁻¹⁰ J/m²| 289 ps    |

For a 10-year *one-shot* drain at the claimed power (i.e., draining the static reservoir continuously without cycling), the cavity would need $d \approx 9.7 \times 10^{-13}\,\mathrm{m}$ — about $10^3 \times$ larger than the proton radius (~0.84 fm) but still **subatomic by every other relevant length scale** (Bohr radius ~5.3 × 10⁻¹¹ m, internuclear spacing in any solid). The parallel-plate Casimir formula assumes plate separations far larger than plate-material microstructure scales; it has no physical meaning here.

The static reservoir does not refute the claim by itself — the claim survives if the cavity is cycled. §3 and §4 below address the two routes to cycling that don't immediately collapse into Pinto-style modulation (the energy ledger of which is handled by the [steelman audit](../2026-05-13-casimir-steelman-energy-ledger/)).

### 2. Limit and convergence check

Numerical $\int_d^\infty F(x)/A\,dx$ vs closed-form $|E|/A$ at $d=10$ nm: relative error $3 \times 10^{-8}$. Reservoir math is correct.

### 3. Dynamical Casimir effect (DCE) — the mechanical-boundary bound

DCE has two distinguishable regimes, and this audit's bound applies cleanly to only one.

**Mechanical regime.** If photon production comes from a literally moving mirror with peak velocity $v$, the production rate scales as $(v/c)^2$ for $v \ll c$ — the slow-boundary perturbative limit. Order-of-magnitude estimate from the Wilson et al. (2011) parametric experiment puts DCE rates near $10^5$ photons/s per mode in the 4–6 GHz analysis band ($\sim 3 \times 10^{-19}$ W per mode at the band center; the published quantity is power per unit bandwidth of a few Kelvin, from which we estimate the per-mode photon rate as an OOM figure — see [Wilson 2011 paper note](../../papers/2011-wilson-dynamical-casimir-effect.md)). Scaling that benchmark up to the claim's $\sim 1.5 \times 10^{-12}$ W per 1 μm² mode requires a $5 \times 10^6 \times$ boost. Under $(v/c)^2$ scaling that demands $v/c \gtrsim 2 \times 10^3$ — **kinematically impossible**. A solid-state chip with no relativistic moving parts cannot reach this regime.

**Parametric regime.** Wilson 2011 itself was *parametric*: the effective boundary impedance was modulated by driving a SQUID at ~11 GHz with the boundary literally stationary. In this regime the figure of merit is the modulation index and rate, not $v/c$, and $(v/c)^2$ scaling does **not** apply. A solid-state device with electronically modulated boundaries is in principle a parametric DCE engine.

**But parametric DCE does not rescue the claim**, because the energy that appears as DCE photons must come from somewhere: the modulation drive. The parametric regime moves the energy-balance question from "where do the photons come from" to "does the modulation drive deliver more than it extracts." That is exactly the question the [steelman audit](../2026-05-13-casimir-steelman-energy-ledger/) addresses, and its answer is no by 7–10 orders of magnitude across every parameter choice it tries.

So §3's bound, narrowly stated, is: **a passive chip with no parametric drive cannot produce useful DCE power via mechanical boundary motion alone**. The broader claim — that no DCE-based route closes the energy ledger at the advertised areal power — depends on §3 plus the steelman ledger taken together.

### 4. Thermal/second-law check — under the company's stated configuration

The press release describes the device as **passive**, **continuously operating**, **without external power input**, **without replacement cycle**, and at **ambient temperature** with no stated thermal gradient. Under that explicitly stated configuration:

- At 300 K, the chip sits in a blackbody environment with radiative flux $\sigma T^4 \approx 459\,\mathrm{W/m^2}$.
- The second law (Kelvin–Planck statement) forbids any device, in equilibrium with a single-temperature reservoir, from delivering net work to an external load. The advertised 1.5 W/m² is small relative to $\sigma T^4$, but the issue is not the magnitude — it is that any positive net work output is forbidden.

A reviewer might object that a sub-micron Casimir cavity is not in single-T equilibrium with free space at all wavelengths, because the cavity-interior mode density is suppressed for long-wavelength modes — i.e., the environment is *spectrally* structured. This is correct but does not save the claim: the second law applies to *macroscopic* energy balance with the surroundings, and the chip-as-a-whole must satisfy energy conservation with its environment regardless of mode-density details inside. The spectral asymmetry between cavity-interior and free-space modes is itself part of the static Casimir energy (§1), which is exhausted by §1's bound.

**Conditional scope of this argument.** If Casimir Inc. is in fact running with a hidden power input — a thermal gradient, an RF pump, a chemical reaction in the chip — the second-law argument does not apply to that device, but the device would no longer match the press release's stated configuration. The audit is auditing the claim *as stated*. The R-veto in the linked claim file fires on the conjunction (configuration as stated + 2nd-law forbids it); it would lift if the company changes the stated configuration to admit an external power input, but at that point the steelman ledger of audit 2 takes over and contradicts the claim again on quantitative grounds.

### 5. Conservativity

The Casimir force at fixed boundary properties is the gradient of a potential. Closed cycles in plate separation alone net **zero work**. The only known theoretical loophole is Pinto-style modulation of a boundary property; even there, no replicated experiment has shown net energy gain in 27 years. The press release supplies no mechanism, no ledger, no demonstration.

## Result

The advertised performance is inconsistent with every relevant physical bound when taken jointly:

- The static reservoir (§1) at any physically meaningful plate gap is far too small to deliver the advertised power as a one-shot drain, ruling out the trivial "tiny vacuum tank" interpretation.
- The conservative-force obstruction (§5) means a cycle in plate separation alone nets zero work, so any continuous-power story must add boundary-property modulation.
- Mechanical DCE (§3, narrow reading) requires relativistic boundary motion that a solid-state chip cannot deliver.
- Parametric DCE / Pinto-style modulation (§3 broad reading, §5) is theoretically the only loophole — and the [steelman audit](../2026-05-13-casimir-steelman-energy-ledger/) shows its energy ledger fails by 7–10 orders of magnitude under maximally charitable parameters.
- Under the company's *stated* passive ambient-temperature configuration (§4), the second law forbids net work output.
- The cited theoretical paper (White 2026 PRR) makes no statement about energy extraction.

## Verdict

**CONTRADICTED.** The claim of continuous, degradation-free, ambient-temperature, passive 1.5 W/m² extraction from "quantum vacuum fields" is incompatible with the Casimir effect as currently understood, with the dynamical Casimir effect demonstrated to date, and with the second law of thermodynamics.

## Caveats and unresolved

- This audit treats the chip as a parallel-plate static cavity at T=0 (for the reservoir bound) and as a passive device at 300 K (for the thermal check). The company has disclosed neither the geometry nor any mechanism beyond marketing language, so a more specific audit is not possible from public information.
- If Casimir Inc. is in fact running a Pinto-style modulated-boundary engine, the audit's conservativity argument can be partly relaxed — but the energy-ledger problem (modulation drive ≥ extracted power) then becomes paramount, and is addressed in the [steelman audit](../2026-05-13-casimir-steelman-energy-ledger/).
- The audit does **not** rule out that the chip produces *some* output by ordinary means (thermal energy harvesting, photovoltaic, RF rectification, thermoelectric). It rules out that the output, if real, comes from "quantum vacuum" in the sense any physicist would recognize.

### Issues surfaced by peer review (2026-05-13)

This audit was peer-reviewed under [AGENTS.md §2.6](../../AGENTS.md#26-peer-review). Reports in [`round0/`](round0/) (pre-sandbox; see `round0/_NOTE.md`) and [`round1/`](round1/) (sandboxed). The substantive findings and their resolution:

- **Devil's advocate**: pointed out that the §3 DCE argument as originally written misapplied the slow-mirror $(v/c)^2$ scaling to the parametric DCE regime that Wilson 2011 actually demonstrates. Fixed: §3 now distinguishes the mechanical regime (where the $(v/c)^2$ bound is valid) from the parametric regime (where it isn't, but where the steelman audit's energy ledger takes over). The original "kinematically impossible" framing was retained only for mechanical DCE.
- **Devil's advocate**: argued §4's second-law claim is conditional on the chip being passive in single-T equilibrium, not unconditional. Fixed: §4 now states this explicitly. The R-veto in the linked claim file still fires under the company's stated configuration; the conditionality is on what the company claims, not on the second law itself.
- **Devil's advocate**: argued §1's reservoir-drain framing is a strawman for a cycling engine. Fixed: §1 now labels the static reservoir as an *instantaneous* bound, not a power bound, and explicitly points at the steelman audit for the cycling case.
- **Source-fidelity reviewer**: caught that Wilson 2011 was cited without a paper note (AGENTS.md §1.4 violation) and that "~10⁵ photons/s" was presented as a direct measurement when it is an order-of-magnitude estimate. Fixed: paper note added at [`papers/2011-wilson-dynamical-casimir-effect.md`](../../papers/2011-wilson-dynamical-casimir-effect.md); §3 prose now hedges as OOM.
- **Two reviewers independently**: caught a prose direction-error claiming the 10-year-drain gap is "three orders of magnitude below the proton radius" when it is in fact about three orders **above**. Fixed: §1 prose corrected; the conclusion (subatomic, formula meaningless) is unchanged because the gap is still far below all relevant solid-state length scales.
- **Reproducibility reviewer**: confirmed that the script runs from clean, all load-bearing numbers match, the closed-form Casimir reservoir formula re-derives correctly under SymPy, and convergence of the numerical integral scales as $1/N^2$ as expected. No code or equation changes needed.
- **Devil's advocate**: flagged missing literature (Lähteenmäki 2013 parametric DCE, Lambrecht–Reynaud 2000, Klimchitskaya–Mostepanenko–Mohideen RMP 2009, Munday–Capasso–Parsegian 2009, Scandurra 2001, Forward 1984). The most consequential is Lähteenmäki 2013 (parametric DCE counterexample to the original §3 framing); the §3 rewrite addresses the conceptual point. A dedicated Lähteenmäki paper-note remains a TODO. The others would tighten the audit but are not load-bearing for the verdict.

The peer-review process did not change the audit's verdict (`contradicted`). It tightened the argument's framing and surfaced one missing paper note. The overall conclusion of the claim file (`refuted`, confidence 0.10) is unchanged because the R-veto justification — second law under the stated configuration — survives the conditional rewrite, and the steelman audit independently kills the parametric loophole.

## How the company can rebut

For this audit to be revised toward `supported`, Casimir Inc. would need to publish (at minimum) **all of**:

1. A peer-reviewed paper describing the cavity geometry, boundary materials, and mode structure.
2. A complete energy ledger: input power (modulation drive, biases, optical pump, etc.) vs delivered electrical output, with uncertainties.
3. An independent replication by a non-affiliated experimental group.
4. A measurable, falsifiable scaling prediction (output vs gap, vs temperature, vs cavity area) consistent with their stated mechanism.

The PRR 2026 paper is, on its own, not a rebuttal. It is an analytic curiosity in a separate problem (hydrogenic spectrum from a fluid analog) and contains no statement about device operation.

## Changelog

- 2026-05-13: audit created. Verdict: contradicted.
- 2026-05-13: peer-reviewed by three subagents (devil's advocate, source fidelity, reproducibility) per AGENTS.md §2.6. Reviews in [`round0/`](round0/). §1, §3, §4, and the "Result" summary revised to address devil's-advocate and source-fidelity findings; Wilson 2011 paper note added; proton-radius prose direction corrected. Verdict unchanged.
- 2026-05-13: round1 peer review — first run under the sandboxed protocol (AGENTS.md §2.6 rewritten this session). The three reviewers were spawned against a curated `/tmp/` sandbox with the audit's verdict, prior reviews, claim status/confidence, and examples walkthrough programmatically stripped. Reports in [`round1/`](round1/) alongside `_sandbox_manifest.json` (SHA-256s of every file the reviewer had access to, plus protocol-doc SHAs and git HEAD at sandbox creation). Reviewer verdicts: `devil_advocate: minor issues` (round0 was `substantive issues`); `source_fidelity: all sources accurately represented` (round0 was `minor mismatches`); `reproducibility: fully reproduces` (consistent across rounds). The shift in devil-advocate severity reflects two effects: (a) the audit was already revised between rounds in response to round0's findings, so round1 was reviewing a tighter document; (b) the sandbox removed prior-review context, so round1 could not see what had already been resolved. The shift in source-fidelity severity is structural: round0 caught "Wilson 2011 has no paper-note" (an AGENTS.md §1.4 hygiene violation) by reading the paper notes directory; round1 had no paper notes to check, so that class of finding is invisible to it by design. Round1 caught additional details round0 missed (most notably a minor Wilson-band frequency annotation, and rhetorical overreach in the Jaffe paraphrase) — different lenses, different findings, both substantive. Verdict and claim confidence unchanged.
