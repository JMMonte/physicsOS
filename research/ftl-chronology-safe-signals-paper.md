---
slug: ftl-chronology-safe-signals-paper
status: planning
started: 2026-05-15
related_claims:
  - ../claims/mechanism-constrained-ftl-chronology-safe.md
  - ../claims/controllable-ftl-engineering-problem.md
related_audits:
  - ../audits/2026-05-15-preferred-frame-ftl-chronology/
  - ../audits/2026-05-15-ftl-causal-loop-kinematics/
---

# Paper Plan: Chronology-Safe Mechanism-Constrained FTL

## Working title

Chronology-safe faster-than-light propagation: separating constrained signal laws from reciprocal tachyonic communication

## Thesis

The statement "FTL violates causality" is too coarse. The antitelephone refutes unrestricted reciprocal sender-rest-frame FTL, but not every faster-than-`c` propagation law. A constrained mechanism with a global preferred/effective time function can be chronology-safe in the kinematic sense. The hard problem is not just causality; it is finding an operational, scalable mechanism that carries information or matter without violating energy-condition, quantum-inequality, backreaction, or Lorentz-violation constraints.

## Intended contribution

- Formalize the distinction between unrestricted reciprocal FTL and mechanism-constrained FTL.
- Present a minimal preferred/effective-frame model with an explicit time function.
- Show why the tachyonic antitelephone works for the first rule and fails for the second.
- Build a checklist for evaluating proposed FTL mechanisms without collapsing every case into the same slogan.
- Map the remaining route from chronology-safe signalling to practical human FTL capability.

## Current artifacts

- Claim: [mechanism-constrained FTL can be chronology-safe](../claims/mechanism-constrained-ftl-chronology-safe.md), currently `supported`, confidence `0.70`.
- Counterclaim: [controllable FTL is possible and should be treated as engineering](../claims/controllable-ftl-engineering-problem.md), currently `refuted`, confidence `0.10`.
- Audit: [preferred-frame FTL chronology](../audits/2026-05-15-preferred-frame-ftl-chronology/) shows a toy global-time-constrained model avoids the antitelephone. Not yet sandbox peer-reviewed.
- Audit: [FTL causal-loop kinematics](../audits/2026-05-15-ftl-causal-loop-kinematics/) shows unrestricted reciprocal sender-rest-frame FTL permits causal loops.

## Paper outline

1. **Introduction**
   - Motivate the ambiguity in "FTL".
   - State the target distinction: propagation faster than vacuum `c` versus arbitrary reciprocal FTL communication.

2. **The standard obstruction**
   - Reproduce the antitelephone setup.
   - Derive `beta > 2 alpha / (1 + alpha^2)` for sender-rest-frame reciprocal FTL.
   - Explain why this is a real obstruction, not just coordinate language.

3. **Constrained propagation laws**
   - Define a preferred/effective time function `T`.
   - Require every matter and FTL signal segment to satisfy `Delta T >= 0`.
   - Prove relay chains cannot close causally under this rule.

4. **Canonical examples and non-examples**
   - Scharnhorst/Casimir vacuum as a constrained effective-frame example.
   - Milonni-Svozil operational caveat: not a practical measured FTL signal.
   - Warp drives and wormholes as separate stress-energy/chronology problems, not solved by the toy model.

5. **Engineering capability checklist**
   - Information transfer, not merely phase or group velocity.
   - Stable causality under multi-device networks.
   - Explicit substrate/preferred frame.
   - Lorentz-violation bounds.
   - Energy conditions, quantum inequalities, and backreaction.
   - Scalability to macroscopic distance and payload, if transport is claimed.

6. **Research roadmap**
   - Short-term: finish literature survey and sandbox peer review.
   - Medium-term: audit multi-device constrained networks and Lorentz-violation bounds.
   - Long-term: evaluate concrete substrates for operational signalling.

7. **Conclusion**
   - Mechanism-constrained FTL is the honest loophole.
   - Practical human FTL remains unestablished.

## Research TODOs

- [ ] Run sandboxed peer review for `audits/2026-05-15-preferred-frame-ftl-chronology/`.
- [ ] Audit multi-device preferred/effective-frame networks for stable causality.
- [ ] Re-read Barton 1990 and Scharnhorst-Barton 1993; log paper notes.
- [ ] Quantify the Scharnhorst speed shift and reproduce the leading-order scale estimate.
- [ ] Audit Milonni-Svozil's operational no-measurement argument.
- [ ] Survey Bruneton-style superluminal classical-field causality criteria.
- [ ] Build a mechanism table: Scharnhorst/Casimir, metamaterials, k-essence/effective metrics, warp shells, wormholes, Lorentz-violating fields.
- [ ] Audit Lorentz-violation bounds for any proposed physical preferred-frame substrate.
- [ ] Add a short section comparing "signal FTL" versus "transport FTL."
- [ ] Decide target format: arXiv-style note, review article, or position paper with executable audits.

## Draft abstract

Faster-than-light propagation is often treated as synonymous with causal paradox. That identification is correct for unrestricted reciprocal sender-rest-frame signalling, but it is not model-independent. We separate the antitelephone obstruction from mechanism-constrained propagation laws. In a minimal model where all allowed superluminal signals advance a global preferred/effective time function, relay chains cannot form closed causal loops even though individual signals exceed the vacuum light speed in that frame. We compare this distinction with Scharnhorst-type effective propagation, chronology-protection arguments, and modern warp-drive stress-energy constraints. The result is not a practical FTL technology, but a sharper research criterion: viable FTL proposals must first specify a chronology-safe propagation law before engineering questions are meaningful.

## Changelog

- 2026-05-15: created initial paper plan and TODO list.
