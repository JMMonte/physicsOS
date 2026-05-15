---
slug: controllable-ftl-engineering-problem
status: refuted
confidence: 0.10
opened: 2026-05-15
last_updated: 2026-05-15
tags: [ftl, causality, special-relativity, general-relativity, warp-drive, wormholes]
supersedes: none
superseded_by: none
---

# Controllable FTL is possible and should be treated as an engineering problem

## Precise statement

Under currently established physics (special relativity, quantum field theory, and classical/semiclassical general relativity), controllable faster-than-light communication or transportation between asymptotic inertial observers can be built from ordinary positive-energy matter without producing causal loops, requiring exotic stress-energy, or introducing a preferred-frame/mechanism-constrained propagation rule that blocks reciprocal use. Therefore, FTL should primarily be treated as an engineering problem rather than a fundamental-physics obstruction.

This claim does **not** include merely semantic or constrained cases: anomalous group velocities that carry no signal, effective-medium speed shifts with a preferred frame, cosmological recession speeds, or subluminal warp shells. A proposed preferred-frame FTL mechanism would be a different claim: it may avoid the flat-spacetime antitelephone audit, but it would no longer be "ordinary engineering" inside established Lorentz-invariant physics.

## Why we are tracking this

The user asserted: "ftl is possible and should be treated an engineering problem." This is a non-obvious claim with direct conflicts against relativistic causality, energy conditions, and the status of warp-drive/wormhole literature.

## Evidence ledger

| Date       | Source                                                                                                           | Tier | w    | Sign | Veto | Notes                                                                 |
|------------|------------------------------------------------------------------------------------------------------------------|------|------|------|------|-----------------------------------------------------------------------|
| 2026-05-15 | [Alcubierre 1994](../papers/1994-alcubierre-warp-drive.md)                                                       | A    | 0.85 | 0    | --   | Formal GR metric permits apparent superluminal travel, but requires exotic matter and no build process. |
| 2026-05-15 | [Ford and Roman 1996](../papers/1996-ford-roman-qft-constrains-wormholes.md)                                     | A    | 0.85 | -1   | --   | Quantum inequalities make macroscopic traversable wormholes extremely constrained. |
| 2026-05-15 | [Olum 1998](../papers/1998-olum-superluminal-negative-energies.md)                                                | A    | 0.85 | -1   | --   | Superluminal travel, under an operational GR definition and generic-condition assumption, requires WEC violation. |
| 2026-05-15 | [Liberati, Sonego, and Visser 2002](../papers/2002-liberati-faster-than-c-signals-causality.md)                  | A    | 0.85 | 0    | --   | Constrained faster-than-c effects need not automatically make CTCs; does not support arbitrary FTL engineering. |
| 2026-05-15 | [Bobrick and Martire 2021](../papers/2021-bobrick-physical-warp-drives.md)                                       | A    | 0.85 | -1   | --   | Positive-energy warp construction is subluminal; superluminal shells remain hypothetical. |
| 2026-05-15 | [Lentz 2021](../papers/2021-lentz-breaking-warp-barrier.md)                                                       | A    | 0.85 | +1   | --   | Strongest support: positive-energy superluminal soliton ansatz, but dynamics/sourcing/horizons unresolved. |
| 2026-05-15 | [Santiago, Schuster, and Visser 2022](../papers/2022-santiago-generic-warp-drives-nec.md)                        | A    | 0.85 | -1   | --   | Physically reasonable warp drives generically violate NEC/WEC; directly rebuts positive-energy narrative. |
| 2026-05-15 | [Fuchs et al. 2024](../papers/2024-fuchs-constant-velocity-physical-warp-drive.md)                               | A    | 0.85 | 0    | --   | New positive-energy warp solution is explicitly constant-velocity subluminal; acceleration still unresolved. |
| 2026-05-15 | [Garattini and Zatrimaylov 2025](../papers/2025-garattini-positive-energy-warp-de-sitter.md)                    | B    | 0.70 | 0    | --   | De Sitter positive-Eulerian-density loophole, but local NEC/WEC violations remain and travel is impractical. |
| 2026-05-15 | [Celmaster and Rubin 2025](../papers/2025-celmaster-lentz-wec-violations.md)                                    | C    | 0.55 | -1   | --   | Direct preprint rebuttal to Lentz: negative Eulerian energy and derivation errors. |
| 2026-05-15 | [Rodal 2026](../papers/2026-rodal-predominantly-positive-warp-drive.md)                                         | A    | 0.85 | 0    | --   | Reduces energy-condition stress but still quantifies negative-energy requirements. |
| 2026-05-15 | [Le 2026](../papers/2026-le-observer-robust-warp-energy-conditions.md)                                          | C    | 0.55 | -1   | --   | Observer-robust preprint finds single-frame checks miss WEC/DEC violations in warp metrics. |
| 2026-05-15 | [Rodal 2026 screening](../papers/2026-rodal-birefringent-screening-fast-warp.md)                                | C    | 0.55 | -1   | --   | Reduced weak-birefringent screening model disfavors fast Type-I warp walls. |
| 2026-05-15 | [audit: ftl-causal-loop-kinematics](../audits/2026-05-15-ftl-causal-loop-kinematics/) (verdict: `contradicted`) | --   | 1.00 | -1   | R    | Categorical only for unrestricted reciprocal FTL signalling: Lorentz kinematics permits a causal loop. |

Confidence calculation per [AGENTS.md section 3.3](../AGENTS.md#33-confidence-rubric):

```text
s_raw  = (0*0.85 + -1*0.85 + -1*0.85 + 0*0.85 + -1*0.85 + +1*0.85 + -1*0.85 + 0*0.85
          + 0*0.70 + -1*0.55 + 0*0.85 + -1*0.55 + -1*0.55 + -1*1.00)
       / (8*0.85 + 0.70 + 0.55 + 0.85 + 0.55 + 0.55 + 1.00)
       = -5.20 / 11.00
       = -0.473
s_base = (-0.473 + 1) / 2 = 0.264

R-veto present from the kinematic audit
=> confidence = min(0.264, 0.10) = 0.10
```

The R-veto is scoped narrowly: it applies to the ordinary "controllable reciprocal FTL signal" interpretation, where the obstruction is a kinematic causal loop. It does not by itself refute preferred-frame or mechanism-constrained FTL rules. The broader warp/wormhole side is weighed down by high-tier negative evidence but not by a single absolute no-go theorem covering every speculative quantum-gravity completion.

## Open sub-questions

- Can any quantum-gravity theory provide a chronology-safe, controllable, macroscopic FTL channel without reducing to a preferred-frame or effective-medium effect?
- Are there experimentally accessible negative-energy configurations beyond Casimir-scale local effects that evade known quantum inequalities?
- Can Lentz-type or Fell-Heisenberg-type positive-energy warp claims survive observer-invariant energy-condition analysis?
- Can a subluminal positive-energy warp shell become useful propulsion without hidden negative energy during acceleration?
- Do 2025-2026 irrotational/de Sitter constructions survive a full observer-robust audit and chronology analysis?

## To read / to audit

- [ ] Morris, Thorne, and Yurtsever 1988, DOI 10.1103/PhysRevLett.61.1446.
- [ ] Pfenning and Ford 1997, "The unphysical nature of warp drive."
- [ ] Hawking 1992, "Chronology protection conjecture."
- [ ] Barcelo, Finazzi, and Liberati 2010, "On the impossibility of superluminal travel: the warp drive lesson."
- [ ] Fell and Heisenberg 2021, "Positive Energy Warp Drive from Hidden Geometric Structures."
- [ ] Benford, Book, and Newcomb 1970, "The Tachyonic Antitelephone."
- [ ] Feinberg 1967, "Possibility of Faster-Than-Light Particles."
- [ ] Bilaniuk, Deshpande, and Sudarshan 1962, "`Meta` Relativity"; Bilaniuk and Sudarshan 1969, "Causality and Space-like Signals."

## Changelog

- 2026-05-15: opened. Initial status `refuted`, confidence 0.10. Evidence includes the canonical Alcubierre steelman, Lentz positive-energy steelman, Olum/Ford-Roman/Santiago negative-energy constraints, Bobrick-Martire/Fuchs positive-energy subluminal context, and a local kinematic audit showing unrestricted reciprocal FTL signalling creates a causal loop.
- 2026-05-15: round1 peer review of the kinematic audit completed. Devil's advocate found a substantive scope issue: the R-veto only applies to unrestricted reciprocal FTL signalling, not preferred-frame or mechanism-constrained propagation. Claim wording and veto note narrowed accordingly; confidence unchanged because the tracked statement is the ordinary reciprocal engineering interpretation.
- 2026-05-15: corrected literature freshness after user pointed out that current date is 2026. Added 2025-2026 sweep: Garattini-Zatrimaylov 2025, Celmaster-Rubin 2025, Rodal 2026, Le 2026, and Rodal's March 2026 weak-birefringent screening preprint. Recomputed `s_base` from 0.272 to 0.264; final confidence remains 0.10 due to the scoped R-veto.
