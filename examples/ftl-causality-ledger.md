# FTL Causality Ledger

This walkthrough shows how physicsOS handles a claim that is too broad to answer with a slogan:

> "FTL is possible and should be treated as an engineering problem."

The repo splits that into two tracked claims. The broad engineering claim is refuted under established relativistic physics, while a narrower mechanism-constrained chronology claim stays open and supported.

## Artifacts

| Artifact | Role | Current state |
|---|---|---|
| [claims/controllable-ftl-engineering-problem.md](../claims/controllable-ftl-engineering-problem.md) | Broad reciprocal FTL engineering claim | `refuted`, confidence 0.10 |
| [audits/2026-05-15-ftl-causal-loop-kinematics/](../audits/2026-05-15-ftl-causal-loop-kinematics/) | Kinematic antitelephone audit | `contradicted`, sandbox peer-reviewed |
| [claims/mechanism-constrained-ftl-chronology-safe.md](../claims/mechanism-constrained-ftl-chronology-safe.md) | Narrow preferred/effective-time loophole | `supported`, confidence 0.70 |
| [audits/2026-05-15-preferred-frame-ftl-chronology/](../audits/2026-05-15-preferred-frame-ftl-chronology/) | Toy preferred-frame chronology audit | `confirmed-with-caveat`, not yet peer-reviewed |
| [research/ftl-chronology-safe-signals-paper.md](../research/ftl-chronology-safe-signals-paper.md) | Paper-plan thread | planning |

## What Changed During The Investigation

The first audit checked unrestricted reciprocal sender-rest-frame FTL in flat spacetime. It derives the loop condition
`beta > 2 alpha / (1 + alpha^2)` and verifies it numerically in [the audit README](../audits/2026-05-15-ftl-causal-loop-kinematics/README.md). That is a categorical kinematic obstruction for the broad claim, so the claim ledger assigns a scoped R-veto and caps confidence at 0.10.

Sandboxed peer review then forced a scope correction. The audit refutes unrestricted reciprocal FTL signalling, not every possible effective-medium, preferred-frame, curved-spacetime, or quantum-gravity construction. That correction is recorded in the audit's [round1 reports](../audits/2026-05-15-ftl-causal-loop-kinematics/round1/) and in the claim changelog.

The narrowed question became: can a faster-than-`c` propagation rule be chronology-safe if every allowed signal advances a global preferred/effective time? The current ledger says yes as a causal-consistency statement, but not as a practical engineering result. That distinction is tracked in [mechanism-constrained-ftl-chronology-safe.md](../claims/mechanism-constrained-ftl-chronology-safe.md).

## Source Backbone

The ledger separates three kinds of literature:

- Classical FTL steelmen: [Alcubierre 1994](../papers/1994-alcubierre-warp-drive.md), [Lentz 2021](../papers/2021-lentz-breaking-warp-barrier.md), and later positive-energy warp papers.
- Constraint literature: [Ford and Roman 1996](../papers/1996-ford-roman-qft-constrains-wormholes.md), [Olum 1998](../papers/1998-olum-superluminal-negative-energies.md), [Bobrick and Martire 2021](../papers/2021-bobrick-physical-warp-drives.md), and [Santiago, Schuster, and Visser 2022](../papers/2022-santiago-generic-warp-drives-nec.md).
- Chronology and constrained propagation: [Liberati, Sonego, and Visser 2002](../papers/2002-liberati-faster-than-c-signals-causality.md), [Scharnhorst 1990](../papers/1990-scharnhorst-light-between-plates.md), [Milonni and Svozil 1990](../papers/1990-milonni-svozil-impossibility-scharnhorst-measurement.md), [Hawking 1992](../papers/1992-hawking-chronology-protection.md), and [Kay, Radzikowski, and Wald 1997](../papers/1997-kay-radzikowski-wald-cauchy-horizon-qft.md).

## Current Narrative

The broad "FTL is just engineering" claim is not supported. The strongest obstruction is not a vague appeal to impossibility; it is an explicit causal-loop audit plus a literature ledger showing that known warp-drive and wormhole routes remain constrained by energy conditions, quantum inequalities, horizons, or chronology protection.

The honest loophole is narrower: a mechanism-constrained FTL rule with a global time function can be chronology-safe in a toy model. That does not establish a macroscopic communicator or spacecraft. It defines the next research target: identify a real substrate, prove stable causality for networks of devices, and audit energy-condition, backreaction, and Lorentz-violation constraints.
