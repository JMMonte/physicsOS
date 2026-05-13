---
slug: 2026-05-13-casimir-steelman-energy-ledger
claim: ../../claims/casimir-quantum-energy-chip-feasibility.md
conventions: SI; parallel-plate idealization with perfect-conductor reservoir at T=0; modulator at 300 K; "generous-to-the-claim" parameter choices throughout
verdict: contradicted
audit_layers: [dimensional, limits, order-of-magnitude, symbolic, numerical, data-comparison]
created: 2026-05-13
---

# Steelman energy-ledger audit of a Pinto-style Casimir engine

## Claim under audit

The prior audit ([../2026-05-13-casimir-energy-budget/](../2026-05-13-casimir-energy-budget/))
established that a static Casimir cavity cannot deliver 1.5 W/m² continuously,
that the dynamical Casimir effect cannot supply that power passively (boundary
velocity bound), and that a passive single-temperature device is forbidden by
the second law.

The press release does not describe a mechanism, but the only theoretical
loophole in the Casimir literature is the **Pinto-style modulated-boundary
cycle**: render the otherwise-conservative Casimir force non-conservative by
modulating a boundary property (refractive index, conductivity, geometry)
during the cycle, then collect the imbalance as electrical work. This audit
**steelmans** that mechanism: under maximally favorable assumptions, can a
Pinto-style Casimir engine deliver

> 1.5 W/m² of *net* electrical output from a 5 mm × 5 mm chip at ambient
> temperature, with no external power input

— the Casimir Inc. number transcribed verbatim from the press release
[`papers/2026-businesswire-casimir-press-release.md`](../../papers/2026-businesswire-casimir-press-release.md).

The Debrief's writeup of the device adds a key detail not in the press
release: the cavity is described as having **two stationary plates** at
**~100 nm** separation with **electrically isolated micropillars** as
collection "antennas". White calls this a "quantum tunneling ratchet"
([4orbs / The Debrief](https://thedebrief.org/free-energy-from-the-vacuum-warp-drive-pioneer-unveils-battery-free-microsparc-that-allegedly-draws-power-from-the-quantum-vacuum/)).
This is not a Pinto cycle — it's a static-boundary tunneling story. But it
shares the same energetic obstruction either way: any static-boundary device
in a single-temperature bath is constrained by the second law, and the only
way around it is to actively modulate a boundary property. So a steelman of
the Pinto route is *also* a steelman of the only loophole that could
conceivably power MicroSparc.

## Sources used in the audit

- Casimir 1948, KNAW 51, 793 — the parallel-plate force formula.
- [Pinto 1999–2003 patents](../../papers/1999-pinto-casimir-engine-patents.md) — defines the modulated-boundary cycle.
- [Moddel & Dmitriyeva 2019, *Atoms* 7, 51](https://doi.org/10.3390/atoms7020051) — the most rigorous peer-reviewed survey of vacuum-energy extraction proposals. Concludes Pinto-style mechanical extraction fails because the Casimir force is conservative (citing Scandurra 2001), and reports an experimental "tantalizing but inconclusive" null at the level of expected power for the only loophole-class proposal (gas-flow). Most directly load-bearing for verdict: page 8 ("any attempt to obtain net power in a cyclic fashion from changing the spacing of Casimir cavity plates cannot work").
- [White et al. 2026, PRR 8, 013264](../../papers/2026-white-emergent-quantization-dynamic-vacuum.md) — the press release's cited theory paper. Does not discuss energy extraction (independently confirmed by all secondary commentary, including Hossenfelder and the substack technical review).
- Material data:
  - VO₂ MIT enthalpy ΔH ≈ 45 J/g (Berthier et al. 2008; aggregated values in [Bowman et al. 2020, PCCP](https://doi.org/10.1039/D0CP01929A)); density ρ_VO₂ = 4.34 g/cm³. Volumetric latent heat ΔH × ρ = 1.95×10⁸ J/m³.
  - InSb static permittivity ε_r ≈ 17 (standard handbook); THz loss tangent tan δ ≈ 0.014 ([Sci Rep 13, 45475-8, 2023](https://doi.org/10.1038/s41598-023-45475-8)); effective mass m_eff ≈ 0.014 m_e.

## Audit plan

Six layers, as enumerated in [AGENTS.md §2.2](../../AGENTS.md):

1. **Dimensional** — every step has machine-checked units via `pint`.
2. **Limits** — the static-reservoir baseline from the prior audit is recovered.
3. **Order-of-magnitude** — explicit, with sources for every material number.
4. **Symbolic** — the Pinto extraction upper bound and Drude-floor energy
   are derived in closed form.
5. **Numerical** — the audit script computes the ledger at a base point and
   sweeps (d, f_mod, ΔR) over 5×3×3 = 45 combinations.
6. **Data comparison** — compared to material-property measurements (loss
   tangents, latent heats, breakdown fields) from peer-reviewed sources.

Full computation in [`audit.py`](audit.py); raw numbers in
[`outputs/sensitivity.csv`](outputs/sensitivity.csv); headline figure in
[`outputs/ledger_vs_fmod.png`](outputs/ledger_vs_fmod.png).

## Result

### Best-case extracted power

A Pinto cycle that swings plate reflectivity from 0 → 1 → 0 once per cycle
at frequency f_mod, at a plate gap d, extracts at most the static Casimir
energy per area per cycle:

$$
P_{\text{extracted}} \le \frac{|E_{\text{Cas}}|}{A} \cdot f_{\text{mod}}
= \frac{\pi^2 \hbar c}{720\, d^3} \cdot f_{\text{mod}}.
$$

At the company-disclosed d = 100 nm, with an aggressive f_mod = 1 GHz and
unrealistically generous ΔR = 1:

| quantity | value |
|---|---|
| static |E|/A at 100 nm | 4.33×10⁻⁷ J/m² |
| P_extracted (ΔR=1, 1 GHz) | **4.33×10² W/m²** |
| Casimir Inc. claim | 1.5 W/m² |
| extracted / claim ratio | **289×** |

So far so good for the claim — *if* the cycle were free. It is not.

### Drive-cost lower bounds

Three independent, physically-motivated lower bounds on the energy that
*must* be paid each cycle to actually drive ΔR:

(A) **Drude carrier-swing floor.** To flip the modulator plate between
"transparent" (ω_p < ω_cavity) and "metallic" (ω_p ≥ ω_cavity) states for
the d = 100 nm cavity's photon scale (ω_cavity = πc/d ≈ 9.4×10¹⁵ rad/s),
the carrier density must swing by Δn ≈ 3.9×10²⁰ /cm³. Charging a 50 nm
modulator layer to this density requires surface charge σ = eΔn·h_mod
≈ 3.1 C/m², stored at E-field amplitude **2×10¹⁰ V/m** (about 7000× the
breakdown field of air and 2×10⁴× the breakdown field of bulk InSb). With
50% perfect-recovery oscillator efficiency:

$$
P_{\text{drive,Drude}} = \frac{1}{2}\cdot 2 f_{\text{mod}}\cdot \frac{\sigma^2}{2\varepsilon_0\varepsilon_r}
\approx 3 \times 10^{19}~\text{W/m}^2.
$$

(B) **Dielectric-loss floor.** At the field that produces the carrier
swing, the in-modulator dissipation is

$$
p_{\text{loss}} = \tfrac{1}{2}\omega\varepsilon_0\varepsilon_r \tan\delta\, E_0^2,
$$

giving P_drive,diel ≈ 1.4×10¹¹ W/m² with InSb tan δ = 0.014. (This floor
is largest where E₀ is largest; it does not "save" the small-gap cases.)

(C) **VO₂ latent-heat floor.** A switchable-material modulator (VO₂)
must be cycled through its metal-insulator transition twice per cycle.
With ΔH = 45 J/g, ρ = 4.34 g/cm³, h_mod = 50 nm:

$$
P_{\text{drive,VO}_2} = 2 f_{\text{mod}} \cdot \rho \Delta H \cdot h_{\text{mod}}
\approx 2 \times 10^{10}~\text{W/m}^2.
$$

These three floors are **independent obstructions** — a real device pays
**all three**, so the operative drive cost is max(A, B, C), not min.
For this audit, the most-favorable-to-the-claim assumption is to take
**min**, which still falls catastrophically short.

### Headline ledger (charitable: drive = min of three floors)

| quantity | value |
|---|---|
| P_extracted | 4.3×10² W/m² |
| P_drive_min (charitable) | 2×10¹⁰ W/m² (VO₂ floor) |
| P_net (best case) | **−2×10¹⁰ W/m²** |
| ratio drive / extracted | 4.5×10⁷ |

The drive cost exceeds the extracted Casimir power by a factor of
**~5 × 10⁷** even taking the *smallest* of three independent loss
mechanisms. The honest figure — drive = max of three — is worse by another
~10⁹ (Drude floor dominates).

### Sensitivity sweep

Across 5 × 3 × 3 = 45 (d, f_mod, ΔR) parameter combinations with
d ∈ {10, 30, 100, 300, 1000} nm, f_mod ∈ {0.1, 1, 10} GHz, ΔR ∈ {0.1, 0.5, 1.0}:

- **0 / 45** points yield net positive power.
- **0 / 45** points reach the claim of 1.5 W/m².
- The least-negative net power (largest gap, lowest frequency, full ΔR)
  is still −1.4 × 10⁶ W/m² — a six-order-of-magnitude deficit.

Raw table: [`outputs/sensitivity.csv`](outputs/sensitivity.csv).

## Independent peer-reviewed corroboration

This audit reproduces the conclusion of the only published systematic
survey of zero-point-energy-extraction proposals:

> "Any attempt to obtain power by cycling Casimir cavity spacing the
> energy gained in one part of the cycle must be paid back in another."
> — Moddel & Dmitriyeva, *Atoms* 7, 51 (2019), Conclusion §3.

Moddel's group at UC Boulder spent ~15 years and DARPA funding
(N66001-06-1-2026) attempting the only physically distinct loophole-class
proposal in the literature (atom-pumping through Casimir cavities) and
reported in 2019 that results are "tantalizing but unfortunately
inconclusive" — i.e., **null within experimental sensitivity**, despite
two decades of effort by an established academic group with patent
interests in the technology. Pinto-style mechanical extraction has had
**zero net-energy demonstrations in 27 years** since the first patent
filing (1999).

## Caveats and honest acknowledgments to the company

- We have steelmanned a mechanism the company has not actually claimed.
  The Debrief writeup describes the device as a "quantum tunneling ratchet"
  with **stationary** plates and tunneling micropillars — not a modulated
  boundary at all. We audited Pinto because it's the only theoretical
  loophole that survives basic physics; the company's actual mechanism
  description is even harder to motivate (a static-boundary device in a
  single-temperature bath is squarely forbidden by the second law).
- We did *not* exclude that the chip produces *some* output by a conventional
  mechanism (thermal harvesting, RF rectification, photovoltaic from
  ambient light, thermoelectric, piezoelectric from vibration). The
  prototype output mentioned in secondary press ("millivolts at picoamps")
  is well within the range of such conventional harvesting from a 25 mm²
  device. We audit only whether *Casimir extraction* explains the
  performance.
- The Drude floor (A) is sensitive to choice of m_eff and to whether the
  modulator needs to swing through full metallic threshold or some smaller
  contrast. Even an order-of-magnitude relaxation (e.g. ΔR = 0.1 instead of
  1, with the same drive-field) still leaves the deficit ≥ 10⁶.
- The VO₂ floor (C) assumes the entire 50 nm layer cycles. If only a thin
  sliver near a phase boundary cycles, that floor drops linearly with
  the cycled volume — but then the dielectric-loss floor (B) dominates.
- Real materials cannot be cycled at GHz through a thermally-driven phase
  transition; the thermal time constant of a 50 nm VO₂ film is ~μs, not
  ns. Treating the GHz-VO₂ case as the *steelman* is already physically
  impossible for thermal-driven mechanisms.

## Verdict

**CONTRADICTED.** Under the most favorable physically-motivated assumptions
— company-stated geometry (d=100 nm), aggressive cycle frequency (1 GHz),
unrealistic ΔR = 1, charitable minimum-of-three drive-cost lower bound — the
ledger gives net **−2 × 10¹⁰ W/m²**, a deficit of ~10 orders of magnitude
relative to the 1.5 W/m² claim. No parameter combination in a 45-point
sweep yields positive net power. This is consistent with the peer-reviewed
consensus (Moddel-Dmitriyeva 2019; Scandurra 2001) and with the empirical
record: 27 years of attempts, zero net-energy-positive demonstrations.

This audit does not establish a new categorical impossibility beyond what
the prior audit's 2nd-law and kinematic vetoes already provide; it
strengthens the verdict by showing that the *one* theoretical loophole the
prior audit explicitly flagged ("If Casimir Inc. is in fact running a
Pinto-style modulated-boundary engine, the energy-ledger problem becomes
paramount") fails even when steelmanned.

## How the company can rebut

To upgrade this audit toward `confirmed`, Casimir Inc. would need to
publish, at minimum, *all of*:

1. The cycle mechanism — what boundary property is modulated, by what driver,
   at what amplitude and frequency.
2. An energy ledger with measured input vs measured output, with calorimetric
   accounting of waste heat in the modulator (the steelman's killing-floor).
3. An independent replication.
4. A scaling prediction (output vs gap, vs T, vs frequency) consistent with
   their proposed mechanism.

The PRR 2026 paper does not provide any of these — see paper note for
why it cannot be cover for the device claim.

## Changelog

- 2026-05-13: audit created. Verdict: contradicted.
