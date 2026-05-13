---
title: Extraction of Zero-Point Energy from the Vacuum — Assessment of Stochastic Electrodynamics-Based Approach as Compared to Other Methods
authors: G. Moddel, O. Dmitriyeva
year: 2019
venue: Atoms 7(2), 51 (MDPI; peer-reviewed)
arxiv: 0910.5893 (preprint version; published version is v3-equivalent)
doi: 10.3390/atoms7020051
tier: A   # Peer-reviewed primary paper, reputable journal. Note: Moddel's group has commercial interests (Jovion Corp, disclosed), but the analytical content is conventional thermodynamics + electromagnetism and the paper's conclusion is *negative for the technology*, which weakly counter-balances the conflict.
read_depth: deep   # Full text read via pdftotext extraction of arXiv preprint.
read_on: 2026-05-13
keywords: [casimir, vacuum-energy, zero-point, pinto-cycle, stochastic-electrodynamics, conservativity, second-law]
related_claims: [casimir-quantum-energy-chip-feasibility.md]
related_audits: [2026-05-13-casimir-energy-budget/, 2026-05-13-casimir-steelman-energy-ledger/]
---

# Moddel & Dmitriyeva 2019 — peer-reviewed survey of ZPE-extraction proposals

## One-line summary

A systematic peer-reviewed assessment of every category of proposed
zero-point-energy extraction device. The authors conclude that the two
classes most often promoted (nonlinear-rectification of ZPF noise, and
mechanical extraction via Casimir cavity cycles) are forbidden by
detailed balance and by the conservativity of the Casimir force; their
own gas-pumping-through-Casimir-cavity experiment (the third class,
stochastic-electrodynamics-based) returned "tantalizing but
inconclusive" results — null at the level of the predicted power, with
power output below detection threshold.

## What it actually shows

### The three classes

1. **Nonlinear rectification of ZPF noise (Valone-class).**
   Treated rigorously. Detailed balance forbids extracting net work
   from a noise source in equilibrium with its surroundings, regardless
   of how clever the rectifier — a result rederived for ZPE in §2.1,
   citing Sokolov 1998, Nikulov, Allahverdyan & Nieuwenhuizen.
   **Verdict in the paper: forbidden.**

2. **Mechanical extraction via Casimir cycles (Pinto-class).**
   The Casimir force, at fixed boundary properties, is the gradient of
   a potential — it is conservative. Pinto's cycle (close, modulate
   plate property, separate) attempted to render it non-conservative.
   Scandurra (2001) analyzed each step of the cycle and showed the
   property-modulation step costs at least as much as the Casimir step
   extracts. The conservativity has since been *acknowledged by Pinto
   himself* (Am. Sci. 102, 280, 2014, "Engines powered by the forces
   between atoms"). **Verdict in the paper: cannot work for cyclic
   power.**

   Quote, §3 Conclusions, p. 16:

   > "The force exhibited between opposing plates of a Casimir cavity
   > have led to attempts to make use of the potential energy to
   > obtain power. This cannot succeed because the Casimir force is
   > conservative. In any attempt to obtain power by cycling Casimir
   > cavity spacing the energy gained in one part of the cycle must be
   > paid back in another."

3. **Pumping atoms through Casimir cavities (Stochastic-ED–class).**
   The authors' own experimental program. In SED, atomic ground states
   are sustained by ZPF absorption/emission balance. Inside a Casimir
   cavity, ZPF mode density is suppressed, so an atom's "natural"
   ground state shifts. Pumping atoms in and out of the cavity might
   then transfer energy to/from the ZPF reservoir. Authors built and
   tested an apparatus: He, Ar, Xe through gold-coated and uncoated
   polycarbonate nanopore membranes, looking for excess radiation
   emission downstream.

   Experimental result (§2.3.9, 2.3.11):
   - Some radiation observed, but **much lower than predicted** (size
     and shape of nanopores inconsistent).
   - Most emission came from uncoated dielectric membranes, opposite
     to the expectation that metal-walled cavities should be more
     effective. Authors attribute to thermal emissivity differences,
     not vacuum extraction.
   - Highest emission from helium, opposite the expected wavelength-
     resonance ordering.
   - Henriques' independent attempt at the same concept: null
     (possibly detection-limited).

   **Verdict in the paper: "tantalizing but unfortunately
   inconclusive."** No net energy extraction demonstrated. Authors
   leave open whether the null is fundamental or technological.

### Bottom-line conclusion (paper's §3, paraphrased)

> Our apparent lack of clear success in extracting energy from the
> vacuum thus far leads to two possible conclusions. Either fundamental
> constraints beyond what have been discussed here and the nature of
> ZPE preclude extraction, or it is feasible and we just need to find
> a suitable technology.

This is the position of the *most sympathetic-to-the-idea* peer-
reviewed analysis in the field. The disclosed conflict of interest
(G.M. owns stock in Jovion Corp., a company set up to commercialize
the gas-flow harvesting technology) cuts toward bias *in favor of*
positive findings — so the paper's negative-or-inconclusive verdict
is conservatively more credible than a similar verdict from an
unaffiliated party.

## What it does *not* show

- Does not rule out that *some* energy-density gradient in vacuum
  geometry might in principle be tappable; it just observes that 60+
  years of literature have produced no demonstrably working device.
- Does not discuss the dynamical Casimir effect as a power source.
- Does not directly bear on stochastic-electrodynamics derivations of
  hydrogenic states (the conceptual cousin of the White et al. 2026
  paper).

## How it informs the Casimir Inc. claim

This is the **load-bearing peer-reviewed independent corroboration**
for the audits in this repository:

- It validates the prior audit's
  (`2026-05-13-casimir-energy-budget/`) conservativity argument by
  appeal to the Scandurra result and Pinto's own published
  acknowledgment of conservativity.
- It validates the steelman audit's
  (`2026-05-13-casimir-steelman-energy-ledger/`) conclusion that no
  net-energy-positive Casimir engine has been demonstrated in the 27
  years (1999–2026) since the Pinto patents — Moddel and his
  collaborators are arguably the most prolific experimental group in
  the niche and have produced no net-positive result.
- It establishes the *prior probability* against a working Casimir
  energy harvester at the time of Casimir Inc.'s 2026 announcement:
  multiple decades of failed attempts, including ones with DARPA
  funding (the paper's funding disclosure cites DARPA SPAWAR Grant
  N66001-06-1-2026).

In the claim ledger, this paper is the single most weighty
*independent* anti-claim signal among the cited literature.

## Citations to chase (relevant)

- Scandurra, M. (2001) — analysis of Pinto cycle steps showing
  conservativity. (Not separately fetched; cited via Moddel.)
- Pinto, F. (2014) "Engines powered by the forces between atoms,"
  *American Scientist* 102, 280 — Pinto's own follow-up
  acknowledging conservativity.
- Henriques, A. (independent gas-flow null result, cited as [55] in
  Moddel-D).
- Forward 1984 — original coiled-Casimir energy-extraction proposal
  (extracts the static reservoir once; no cyclic power).

## Changelog

- 2026-05-13: created. Full text read; key conclusions and citations
  extracted.
