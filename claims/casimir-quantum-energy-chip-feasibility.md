---
slug: casimir-quantum-energy-chip-feasibility
status: refuted
confidence: 0.10
opened: 2026-05-13
last_updated: 2026-05-13
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
| 2026-05-13 | [White et al. 2026, PRR](../papers/2026-white-emergent-quantization-dynamic-vacuum.md)            | A    | 0.85 | 0    | —    | Cited as theoretical foundation but does not address energy extraction at all.                       |
| 2026-05-13 | [Jaffe 2005, PRD](../papers/2005-jaffe-casimir-without-vacuum-energy.md)                          | A    | 0.85 | −1   | —    | Casimir effect derivable without vacuum energy; "harvest the vacuum" is wrong framing.               |
| 2026-05-13 | [Chernodub 2013, PRD](../papers/2013-chernodub-rotating-casimir-perpetual-motion.md)              | A    | 0.85 | −1   | —    | Closest serious "Casimir perpetual motion" proposal; produces no usable work.                        |
| 2026-05-13 | [Pinto patents 1999–2003](../papers/1999-pinto-casimir-engine-patents.md)                         | F    | 0.30 | 0    | —    | Prior art; theoretical loophole exists but no demonstration in 27 years.                             |
| 2026-05-13 | [audit: casimir-energy-budget](../audits/2026-05-13-casimir-energy-budget/) (verdict: `contradicted`) | —    | 1.00 | −1   | **R** | Categorical: 2nd-law violation for a passive device + kinematic impossibility (DCE needs v>c).      |

Confidence calculation per [AGENTS.md §3.3](../AGENTS.md#33-confidence-rubric):

```
s_raw  = (+1·0.30 + 0·0.85 + −1·0.85 + −1·0.85 + 0·0.30 + −1·1.00) / (0.30 + 0.85 + 0.85 + 0.85 + 0.30 + 1.00)
       = −2.40 / 4.15
       = −0.578
s_base = (−0.578 + 1) / 2 = 0.211

veto-R present (audit establishes a categorical obstruction)
→ confidence = min(0.211, 0.10) = 0.10
```

The veto fires because the audit establishes that **continuous passive 1.5 W/m² extraction from a single-temperature equilibrium is forbidden by the second law**, and the DCE-pumping alternative is forbidden by the kinematic bound `v < c`. These are categorical, not probabilistic, obstructions. Per the rubric they cap the confidence at 0.10 regardless of how many neutral or weakly-positive entries appear elsewhere in the ledger.

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
