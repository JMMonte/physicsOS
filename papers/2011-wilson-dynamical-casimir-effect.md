---
title: Observation of the dynamical Casimir effect in a superconducting circuit
authors: C. M. Wilson, G. Johansson, A. Pourkabirian, M. Simoen, J. R. Johansson, T. Duty, F. Nori, P. Delsing
year: 2011
venue: Nature 479, 376–379
arxiv: 1105.4714
doi: 10.1038/nature10561
tier: A
read_depth: skim   # arXiv preprint fetched and skimmed; full Nature PDF not retrieved
read_on: 2026-05-13
keywords: [dynamical-casimir-effect, parametric-modulation, squid, superconducting-circuit, vacuum-fluctuations]
related_claims: [casimir-quantum-energy-chip-feasibility.md]
related_audits: [2026-05-13-casimir-energy-budget/, 2026-05-13-casimir-steelman-energy-ledger/]
---

# Observation of the dynamical Casimir effect in a superconducting circuit

## One-line summary

First unambiguous experimental observation of the dynamical Casimir effect (DCE) — vacuum photon production from a parametrically modulated boundary, with the boundary itself stationary.

## What it actually shows

- A 1D microwave transmission line is terminated by a SQUID whose effective inductance can be modulated very rapidly (~11 GHz) by an external flux drive. The SQUID's flux dependence makes its impedance look like a movable mirror, where the "effective" mirror velocity tracks $d\phi/dt$.
- Driving this boundary at $\omega_d / 2\pi \approx 11$ GHz produces real, detectable microwave photons in the analysis band 4–6 GHz, with the spectrum and correlations expected for DCE photon-pair production (one of the down-converted modes per drive photon).
- The published quantity is **power per unit bandwidth of a few kelvin** in the analysis band; the photon-pair correlations distinguish DCE from amplifier noise and from ordinary parametric amplification of pre-existing thermal photons.

### What the paper does **not** report

- A single number for "photons per second" produced. Order-of-magnitude estimates put the photon-flux scale at $\sim 10^4$–$10^5$ photons/s in the analysis band, but this is an inference from the reported "few K" power-per-unit-bandwidth, not a quoted measurement.
- A net energy gain. The DCE photons are paid for by the SQUID drive at $\omega_d$. The experiment demonstrates the *effect*; it does not propose, and its data does not support, any net energy extraction from the vacuum.

## Methods (briefly)

Coplanar-waveguide transmission line, $Z_0 \approx 50\,\Omega$. The terminating SQUID acts as a tunable boundary inductance; flux-pumping the SQUID at $\omega_d$ modulates the effective electrical length of the cavity at the same rate. The drive is well above the natural resonance, putting the device in the parametric-amplifier regime. Photon detection is heterodyne in a 4–6 GHz analysis band. Photon-pair correlations (cross-quadrature variances exceeding the vacuum noise level) are the smoking gun.

## Key equations / results

- DCE photon production rate for the slow-boundary limit (mechanical regime, included for completeness; Wilson et al. cite but do not test this directly):
  $$
  \Gamma_{\text{DCE}}^{\text{mech}} \sim \frac{\omega_d}{12\pi}\left(\frac{v_{\text{eff}}}{c_0}\right)^2
  $$
  where $v_{\text{eff}} = (d L_{\text{eff}}/dt)/(\partial L_{\text{eff}}/\partial x)$ is the *effective* mirror velocity inferred from the SQUID modulation, not a literal physical velocity. In Wilson's device, $v_{\text{eff}}/c_0 \approx 0.05$ — far from relativistic, but in the parametric regime that is sufficient because the cavity geometry amplifies the response.

- Power spectral density:
  $$
  S_P(\omega) \sim k_B T_{\text{eff}} \quad \text{with } T_{\text{eff}} \approx \text{few K}
  $$
  in the analysis band, consistent with DCE photon production.

## Assumptions and regime of validity

- 1D cavity geometry; results do not directly translate to 3D parallel plates.
- The "effective mirror" is a transmission-line model; whether the same effect can be realized in a true 3D Casimir cavity at the same efficiency is open.
- Cryogenic operation (~50 mK). The effect itself is not temperature-dependent in principle, but the signal-to-noise relies on suppressing thermal photons.

## Caveats / open issues

- Replicated by independent groups (Lähteenmäki et al. 2013 PNAS in a different superconducting platform) — confirms the effect is real, not an instrument artifact.
- All replications operate in the parametric regime; **no experiment to date has demonstrated DCE from a literally moving mechanical mirror at the speeds required to produce detectable photon flux**.

## How it informs the Casimir Inc. claim

This is the canonical experimental reference for DCE in [audit 1](../audits/2026-05-13-casimir-energy-budget/) §3. The role it plays there:

- The mechanical-DCE scaling $(v/c)^2$ implies that a literally-moving-mirror DCE chip would need relativistic boundary motion — kinematically impossible for a solid-state device. The audit's "v/c ≳ 2 × 10³" figure is the OOM-extrapolation from the Wilson experiment, taken as the photon-rate baseline.
- However, Wilson's actual experiment is *parametric*. The parametric regime does not need $v/c \gtrsim 1$; the cost moves to the modulation drive, which the [steelman audit](../audits/2026-05-13-casimir-steelman-energy-ledger/) shows fails by 7–10 orders of magnitude across every parameter combination.
- A Casimir Inc.-style chip operating in the parametric DCE regime is therefore not refuted by §3's mechanical bound alone; it is refuted by §3 + the steelman ledger together.

## Citations to chase

- Lähteenmäki et al. 2013, *PNAS* 110, 4234 — independent replication / extension.
- Lambrecht, Reynaud — earlier theoretical DCE work in the parametric regime.
- Davis 1975, Fulling–Davies 1976 — foundational DCE theory.

## Changelog

- 2026-05-13: created in response to a source-fidelity peer-review finding (the audit cited Wilson without a paper note).
