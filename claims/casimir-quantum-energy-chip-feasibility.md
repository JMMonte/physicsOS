---
slug: casimir-quantum-energy-chip-feasibility
status: refuted
confidence: 0.10
opened: 2026-05-13
last_updated: 2026-05-13 (second pass)
tags: [casimir, vacuum-energy, zero-point, free-energy, startup, sonny-white]
supersedes: none
superseded_by: none
---

# Casimir Inc.'s "MicroSparc" chip delivers 1.5 W/m² continuously by harvesting quantum-vacuum energy

## Precise statement

The claim being tracked is, as stated in Casimir Inc.'s 2026-05-12 press release:

> A 5 mm × 5 mm semiconductor "MicroSparc" chip produces **1.5 V at 25 μA continuously** (≈ 37.5 μW, **1.5 W/m² areal**), with **no degradation and no replacement cycle**, by harvesting energy from "quantum vacuum fields" via "engineered Casimir cavities."

Operationally: a passive, ambient-temperature, solid-state device with no external power input delivers continuous electrical work to a load indefinitely.

## Why we are tracking this

Casimir Inc. raised $12M in a May 2026 seed round on this claim. The founder, Dr. Harold "Sonny" White, was the lead of NASA's Eagleworks lab (associated with the EmDrive and "Q-thruster" claims, neither of which survived replication). The cited theoretical paper is real and peer-reviewed (PRR 2026) but does not actually address energy extraction. The question is whether *any* part of the physical claim survives standard scrutiny.

## Evidence ledger

| Date       | Source                                                                                            | Tier | w    | Sign | Veto | Notes                                                                                                |
|------------|---------------------------------------------------------------------------------------------------|------|------|------|------|------------------------------------------------------------------------------------------------------|
| 2026-05-13 | [Casimir Inc. press release](../papers/2026-businesswire-casimir-press-release.md)                | F    | 0.30 | +1   | —    | Primary claim source. Marketing, not science; pointer-only weight.                                   |
| 2026-05-13 | [White et al. 2026, PRR](../papers/2026-white-emergent-quantization-dynamic-vacuum.md)            | A    | 0.85 | 0    | —    | Deep-read confirms: cited as theory but contains zero energy-extraction content. Multiple independent reviews concur. |
| 2026-05-13 | [Jaffe 2005, PRD](../papers/2005-jaffe-casimir-without-vacuum-energy.md)                          | A    | 0.85 | −1   | —    | Casimir effect derivable without vacuum energy; "harvest the vacuum" is wrong framing.               |
| 2026-05-13 | [Chernodub 2013, PRD](../papers/2013-chernodub-rotating-casimir-perpetual-motion.md)              | A    | 0.85 | −1   | —    | Closest serious "Casimir perpetual motion" proposal; produces no usable work.                        |
| 2026-05-13 | [Pinto patents 1999–2003](../papers/1999-pinto-casimir-engine-patents.md)                         | F    | 0.30 | 0    | —    | Prior art; theoretical loophole exists but no demonstration in 27 years.                             |
| 2026-05-13 | [Moddel & Dmitriyeva 2019, *Atoms*](../papers/2019-moddel-dmitriyeva-zpe-extraction.md)           | A    | 0.85 | −1   | —    | Peer-reviewed survey concludes Pinto-class cyclic extraction "cannot succeed because the Casimir force is conservative"; own gas-flow experiment null. |
| 2026-05-13 | [audit: casimir-energy-budget](../audits/2026-05-13-casimir-energy-budget/) (verdict: `contradicted`) | —    | 1.00 | −1   | **R** | Categorical: 2nd-law violation for a passive device + kinematic impossibility (DCE needs v>c).      |
| 2026-05-13 | [audit: casimir-steelman-energy-ledger](../audits/2026-05-13-casimir-steelman-energy-ledger/) (verdict: `contradicted`) | — | 1.00 | −1 | — | Pinto loophole steelmanned with charitable parameters. Best of three independent drive-cost floors exceeds extracted Casimir power by 10⁷–10¹⁰× across 45-point parameter sweep; 0/45 yield net positive. Audit fails on numerical ledger, not on categorical obstruction (the prior audit already supplied that), so no additional veto. |

Confidence calculation per [AGENTS.md §3.3](../AGENTS.md#33-confidence-rubric):

```
s_raw  = (+1·0.30 + 0·0.85 + −1·0.85 + −1·0.85 + 0·0.30 + −1·0.85 + −1·1.00 + −1·1.00)
       / (0.30 + 0.85 + 0.85 + 0.85 + 0.30 + 0.85 + 1.00 + 1.00)
       = (0.30 − 0.85 − 0.85 − 0.85 − 1.00 − 1.00) / 6.00
       = −4.25 / 6.00
       = −0.708
s_base = (−0.708 + 1) / 2 = 0.146

veto-R present (prior audit's categorical 2nd-law + kinematic obstruction)
→ confidence = min(0.146, 0.10) = 0.10
```

The veto is unchanged from the prior round: the prior audit's categorical
findings (continuous passive 1.5 W/m² from a single-temperature equilibrium
forbidden by the second law; DCE pumping forbidden by v<c) already cap the
confidence at 0.10. The new evidence — the Moddel-Dmitriyeva peer-reviewed
survey and the steelman audit — pushes `s_base` further down (from 0.211 to
0.146) but does not change the rubric-capped final confidence.

The steelman audit deliberately does *not* trigger an additional R-veto: its
contradiction is a quantitative 10-order-of-magnitude ledger failure, not a
new categorical impossibility, and the rubric reserves vetoes for
"obstruction in principle, not in practice" ([AGENTS.md §3.3](../AGENTS.md#33-confidence-rubric)).
The ledger failure is sufficient on its own to keep the claim refuted; the
veto from the prior audit handles the in-principle obstruction.

## Open sub-questions

- Is the chip producing *any* measurable output, and if so via what conventional mechanism (thermal harvesting, RF rectification, photovoltaic, thermoelectric)? The claim "1.5 V × 25 μA out of nothing" is refuted; "1.5 V × 25 μA out of a chip that calls itself a Casimir device but is in fact a thermoelectric" is a *different* claim that this file does not address.
- Is there a Pinto-style modulated-boundary mechanism Casimir Inc. has not disclosed? If so, the energy ledger of the modulation drive becomes the new question, and it is also unanswered.
- Does the company plan to publish anything peer-reviewed about the device itself, as opposed to background theory?

## To read / to audit

- [ ] Lamoreaux 1997 (PRL 78, 5–8) — first precision measurement of the Casimir force, for reservoir-bound calibration.
- [ ] Wilson et al. 2011 (*Nature* 479, 376) — direct experimental DCE result, for tighter DCE-bound numbers.
- [ ] Cole & Puthoff 1993 (PRE 48, 1562) — the ZPE-extraction paper most often cited by proponents; needs a critical paper-note.
- [ ] Any independent measurement of a MicroSparc chip, when one becomes public.

## Changelog

- 2026-05-13: opened. Initial status `refuted`, confidence 0.04 via an ad-hoc haircut on a weighted average.
- 2026-05-13: rubric formalized (AGENTS.md §3.3 introduced). Recomputed under the new rubric: `s_base = 0.211`, `veto-R` triggered by the audit's categorical findings, so `confidence = 0.10`. Status unchanged (`refuted`).
- 2026-05-13 (second pass): added two new pieces of evidence.
  (a) Deep-read of the White et al. 2026 PRR paper note: confirmed via four independent technical reviews (Hossenfelder, hejon07 substack, e-catworld, 4orbs) and the 2015 NTRS precursor that the paper contains no energy-extraction content. Sign unchanged at 0 (neutral); strengthened with explicit corroboration.
  (b) Added Moddel & Dmitriyeva 2019, *Atoms* 7, 51 — the most authoritative peer-reviewed survey of ZPE extraction proposals. Pinto-class verdict: cannot work because Casimir force is conservative (citing Scandurra 2001). Sign −1, weight 0.85.
- 2026-05-13 (peer review): audit 1 (energy-budget) was peer-reviewed by three subagents per AGENTS.md §2.6. Verdicts: devil_advocate = substantive issues; source_fidelity = minor mismatches; reproducibility = fully reproduces. The devil's advocate surfaced that the original §3 DCE argument misapplied $(v/c)^2$ scaling to the parametric regime, and that §4's second-law argument is conditional on the company's stated passive configuration rather than unconditional. The audit was revised to address both findings (§3 now distinguishes mechanical from parametric DCE; §4 makes the conditionality explicit). The R-veto on the audit's ledger row survives: under the company's *stated* configuration the second law fires categorically, and any modified configuration with an external power input is independently refuted by the steelman audit. Verdict and confidence unchanged.
  (c) Added second audit `2026-05-13-casimir-steelman-energy-ledger/`: steelman of the Pinto loophole with charitable parameters (d=100 nm, f=1 GHz, ΔR=1, InSb+VO₂ modulator). Three independent drive-cost floors all exceed extracted Casimir power by 10⁷–10¹⁰×; 0 / 45 parameter combinations in the sweep yield net positive power. Sign −1, no additional veto (the ledger failure is quantitative, not categorical).
  Recomputed: `s_base = 0.146`, veto-R unchanged → `confidence = 0.10`. Status unchanged (`refuted`). No literature search uncovered any peer-reviewed Casimir-engine experimental demonstration with net positive output in the 27 years since Pinto's first patent (1999).
