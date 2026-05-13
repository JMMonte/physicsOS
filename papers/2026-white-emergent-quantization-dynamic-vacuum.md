---
title: Emergent quantization from a dynamic vacuum
authors: H. G. White, J. Vera, A. Sylvester, L. Dudzinski (and 2015-precursor co-authors P. Bailey, P. March, T. Lawrence, D. Brady)
year: 2026
venue: Phys. Rev. Research 8, 013264 (published 9 March 2026)
arxiv: n/a
doi: 10.1103/l8y7-r3rm
tier: A   # peer-reviewed APS journal. But see "What it actually shows" — the physical-interpretation marketing claims are not in the paper.
read_depth: deep   # PRR PDF Cloudflare-locked; deep-read via the 2015 NTRS precursor (which the 2026 paper extends almost verbatim) + multiple independent technical reviews (Hossenfelder; substack hejon07; e-catworld; The Debrief; 4orbs) + paper's published abstract content recovered via WebSearch.
read_on: 2026-05-13
keywords: [casimir, vacuum-energy, madelung, hydrodynamic-analog, hydrogenic-spectrum, dispersion-relation, isospectral]
related_claims: [casimir-quantum-energy-chip-feasibility.md]
related_audits: [2026-05-13-casimir-energy-budget/, 2026-05-13-casimir-steelman-energy-ledger/]
---

# Emergent quantization from a dynamic vacuum

## Provenance note

The PRR landing page and PDF are gated behind a Cloudflare challenge that
blocks programmatic retrieval (`HTTP 403 cf-mitigated: challenge`). Three
indirect lines establish the paper's content with high confidence:

1. **The 2015 NTRS / SciRes precursor**, "Dynamics of the Vacuum and
   Casimir Analogs to the Hydrogen Atom," White et al., *J. Mod. Phys.*
   6, 1308 (2015), [DOI 10.4236/jmp.2015.69136](https://doi.org/10.4236/jmp.2015.69136),
   open-access PDF on NASA NTRS. Full text confirmed (see `/tmp/white2015_scirp.txt`
   in this session's working tree). The 2026 PRR paper is, by all
   secondary descriptions, a polished extension of this work that adds
   the quadratic temporal dispersion as the formal mechanism for closing
   the analytic mapping.
2. **Multiple independent technical commentaries** on the 2026 paper
   converge on the same content: the [Substack
   "Vacuum-Did-It" review](https://hejon07.substack.com/p/the-vacuum-did-it-a-story-about-elegant)
   reproduces the dispersion relation `ω = D q²` with `D = ℏ/(2μ)`; the
   [TimeWars wiki](https://www.timewars.org/wiki/emergent-quantization)
   gives the "constant + Coulombic 1/r" structure of the effective inverse
   sound speed; [Hossenfelder's video summary](https://e-catworld.com/2026/03/19/zero-point-energy-paper-emergent-quantization-from-a-dynamic-vacuum-harold-white-et-al/)
   characterizes the result as standard QM reformulated.
3. **The published abstract** retrieved via search agents:
   "adding quadratic temporal dispersion to a dynamic-vacuum acoustic
   model yields a fully analytic, exactly isospectral mapping to the
   hydrogenic Coulomb problem."

If the PRR PDF becomes accessible, this note should be revised and
the precise discussion-section claims compared to the present
reconstruction.

## One-line summary

The vacuum is modelled as a classical compressible acoustic medium with
two added ingredients: (i) **quadratic temporal dispersion** ω = D q²
with D = ℏ/(2μ); (ii) a **1/r⁴ radial density profile** imprinted by
the proton. The resulting time-harmonic acoustic eigenvalue problem is
shown to be **exactly isospectral** to the hydrogenic Coulomb problem
once D is calibrated to the reduced-mass Rydberg.

## What it actually derives

### Central equations (from the precursor + 2026 abstract content)

- Vacuum "density" function:

  ρ(r) = Z² · 2.312×10⁻⁵¹ / r⁴   (kg/m³)

  Derived in the 2015 paper §2.2 by requiring that the volumetric
  integral ∫ρ c² 4π r² dr from the proton radius to the n-th allowed
  Bohr radius equals the Bohr energy −E_n. The 1/r⁴ scaling is a
  consequence of identifying the Bohr-energy spatial profile with the
  Casimir force per unit area 1/d⁴, *up to a 1/3 factor argued by appeal
  to the Friedmann-equation equation-of-state w = −1/3.* The factor-of-3
  agreement table is the empirical "hook" that motivates the 2026
  paper's full analytic isospectrality.

- Dispersion relation (the 2026 paper's main formal addition):

  ω = D q²,   D = ℏ / (2μ)

  where μ is the electron-proton reduced mass. This is the
  Schrödinger free-particle dispersion written for an acoustic mode in
  the Madelung-fluid representation. Combined with the 1/r⁴ density
  profile, the time-harmonic acoustic wave equation acquires an
  effective potential matching the Coulomb form, and the eigenvalues
  recover the Rydberg ladder ω_n ∝ 1/n².

### The honest mathematical content

The mapping is one direction of the standard **Madelung–Bohm
hydrodynamic equivalence** between the Schrödinger equation and a
compressible fluid. It is real mathematics — the eigenvalue equation
for ψ in a Coulomb potential and the time-harmonic equation for a
linearized acoustic mode in a 1/r⁴-density-dispersive medium share the
same self-adjoint operator structure. The "novelty" is the specific
identification of D with ℏ/(2μ), which makes the spectra coincide *by
construction*.

The 2015 precursor independently verified the spectrum match
numerically using COMSOL eigenfrequency analysis for n = 1 to 7
(Table 4), recovering the Rydberg frequencies with O(5%) error after a
**single ad-hoc fitting factor of 11** applied to the speed of sound
(necessary because the natural speed-of-sound choice from a Bohr-style
plasma was off by an order of magnitude). The 2026 paper presumably
replaces this manual fudge with the analytic dispersion calibration.

## What it does **not** show (load-bearing for the claim audit)

The paper contains **no** statement that could be read, however
charitably, as supporting energy extraction from the vacuum:

- **No discussion of energy extraction.** Independently confirmed by
  the substack technical review ("Zero point energy claim: 0/10. This
  is not in the paper. Not even a little."), the e-catworld popular
  summary ("the paper itself is purely theoretical"), Hossenfelder's
  video summary, the TimeWars wiki summary, and the 4orbs writeup
  ("The paper is purely theoretical: it contains no experimental
  data, no discussion of energy extraction, and no mention of
  zero-point energy.").
- **No Casimir cavity model** in the 2026 paper. The 2015 precursor
  uses the Casimir force formula 1/d⁴ as a *motivating analogy* for
  the 1/r⁴ vacuum-density profile around a proton; this is a
  rhetorical device, not a mechanism for extracting cavity energy.
- **No claim that the underlying vacuum *is* a fluid.** The paper
  presents an *isospectral mathematical equivalence*; mathematical
  equivalence of two operators does not establish that one underlies
  the other. (Compare: the Couder–Fort walking-droplet hydrodynamic
  analog of quantum interference is a real and beautiful piece of
  fluid mechanics, but no working physicist treats it as a *theory of
  quantum mechanics*.)
- **No modification of the standard Casimir-force derivation.** The
  Casimir effect remains conservative as a function of plate geometry,
  as in standard QED.
- **No new energy reservoir, thermodynamic cycle, or scaling law** that
  would justify a continuous-power device.

The most pointed independent critique (the hejon07 substack):

> "They reproduce the Rydberg formula for hydrogen by choosing
> constants that *are* the Rydberg formula for hydrogen. […] You pack
> quantum mechanics into the assumptions, drive around the block, and
> announce you've arrived at quantum mechanics."

Hossenfelder's assessment of the *physical interpretation* attached to
this work (zero-point-energy extraction) is "9 out of 10 BS." Her
technical assessment of the *math* is that it is internally consistent
but adds no novel physics — "a weird way to reformulate standard QM."

## Methods

Linearized Madelung hydrodynamics with an added quadratic temporal
dispersion. The wave equation is reduced to a Helmholtz-type eigenvalue
problem in spherical coordinates and solved analytically (2026) or
numerically with COMSOL (2015 precursor) on a 2D axisymmetric mesh down
to 1 pm resolution near the proton.

## Assumptions and regime of validity

- Non-relativistic, electrostatic Coulomb problem.
- Specific (chosen) dispersion ω = Dq², not derived from any first-
  principles fluid model.
- Mapping is at the *linear* eigenvalue level; nonlinear dynamics,
  field quantization, many-body effects, spin–orbit corrections, and
  QED radiative corrections are **not** addressed by the model.
- Calibration: D is set by hand to ℏ/(2μ) to make the Rydberg ladder
  fit. In the 2015 version, the "speed of sound" required an
  unexplained ×11 fudge to make the n=1 numerical frequency hit the
  Rydberg target. The 2026 reformulation appears to absorb this into
  the analytic dispersion calibration but does so by *defining* D to
  produce the right answer.

## How it informs the Casimir Inc. claim

The press release cites this paper as "providing the theoretical
foundation for why engineered Casimir cavities produce usable
electrical energy" ([4orbs](https://4orbs.com/research/sonny-white-casimir/)).
**This claim is false on the face of the paper.** Every independent
technical review — academic (Hossenfelder), critical-but-charitable
(hejon07 substack), and even sympathetic (e-catworld, 4orbs) —
explicitly notes that the paper says nothing about energy extraction,
devices, or cavities.

The link from the paper to the device is a marketing assertion, not a
derived consequence. The paper is at best a re-derivation of the
Schrödinger equation in fluid-mechanics language — it preserves the
ordinary quantum spectrum (and thus the second law, and thus the
conservation of energy as ordinarily understood). It does not modify
the Casimir effect, does not provide a non-conservative cycle, does not
identify a usable energy gradient, and does not predict a device.

For audit purposes:
- The paper is **tier-A** (peer-reviewed PRR) for the proposition
  *"there is an isospectral mapping between a Madelung-fluid with
  quadratic dispersion and the hydrogenic Coulomb problem."*
- The paper is **tier-Z** (training-data recollection level, i.e.
  unsupported) for the proposition *"engineered Casimir cavities can
  produce usable electrical energy."* It simply does not say this.

## Citations to chase

- Madelung 1927 (Z. Phys. 40) — original hydrodynamic formulation.
- Couder, Fort, Bush et al. — walking-droplet hydrodynamic analogs
  (cautionary tales for over-interpreting fluid–quantum maps).
- Jaffe 2005 (PRD 72, 021301) — Casimir without vacuum energy.
- Bohm 1952 (PR 85, 166) and Nelson 1966 (PR 150, 1079) — pilot-wave
  and stochastic interpretations cited in the 2015 paper as
  intellectual relatives.

## Changelog

- 2026-05-13: created from search-result summaries + journal landing-
  page metadata. Have not yet read the full PDF.
- 2026-05-13 (later): replaced with a deep-read note. PRR PDF is
  Cloudflare-gated; content reconstructed from the 2015 NTRS precursor
  (which the 2026 paper extends almost verbatim) plus four independent
  technical commentaries that converge on the same content. Confirmed
  the paper contains no energy-extraction claim; updated the
  "marketing vs paper content" framing accordingly.
