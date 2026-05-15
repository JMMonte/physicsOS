---
slug: mechanism-constrained-ftl-chronology-safe
status: supported
confidence: 0.70
opened: 2026-05-15
last_updated: 2026-05-15
tags: [ftl, causality, preferred-frame, effective-metric, chronology-protection]
supersedes: none
superseded_by: none
---

# Mechanism-constrained FTL can be chronology-safe

## Precise statement

Under established relativistic causality analysis, a faster-than-`c` propagation law can be chronology-safe if the mechanism is constrained by a global preferred/effective time function and all allowed matter worldlines and FTL signal curves advance that time. This statement is about causal consistency only. It does not assert that humanity currently knows how to build a macroscopic FTL communicator or spacecraft.

This claim excludes unrestricted reciprocal sender-rest-frame FTL, which is tracked and refuted in [controllable-ftl-engineering-problem](controllable-ftl-engineering-problem.md). It also excludes semantic cases where no information or payload propagates faster than the relevant signal cone.

## Why we are tracking this

The previous FTL claim was refuted for the ordinary unrestricted reciprocal interpretation, but its peer review and Liberati-Sonego-Visser's analysis left a narrower loophole: causality depends on the propagation law. The user asked to track that narrower claim and use it to understand what a realistic path toward FTL capability would require.

## Evidence ledger

| Date       | Source                                                                                                                   | Tier | w    | Sign | Veto | Notes |
|------------|--------------------------------------------------------------------------------------------------------------------------|------|------|------|------|-------|
| 2026-05-15 | [Liberati, Sonego, and Visser 2002](../papers/2002-liberati-faster-than-c-signals-causality.md)                          | A    | 0.85 | +1   | --   | Causality depends on the FTL propagation law; Scharnhorst-type constrained effects can be benign. |
| 2026-05-15 | [Scharnhorst 1990](../papers/1990-scharnhorst-light-between-plates.md)                                                    | A    | 0.85 | +1   | --   | Canonical constrained QED/effective-medium faster-than-c calculation; not unrestricted FTL. |
| 2026-05-15 | [Milonni and Svozil 1990](../papers/1990-milonni-svozil-impossibility-scharnhorst-measurement.md)                        | A    | 0.85 | 0    | --   | Operational caveat: Scharnhorst is not a practical measured FTL signalling route. |
| 2026-05-15 | [Hawking 1992](../papers/1992-hawking-chronology-protection.md)                                                          | A    | 0.85 | 0    | --   | Supports chronology-protection constraints; not a constructive FTL mechanism. |
| 2026-05-15 | [Kay, Radzikowski, and Wald 1997](../papers/1997-kay-radzikowski-wald-cauchy-horizon-qft.md)                             | A    | 0.85 | 0    | --   | QFT pathologies at compactly generated Cauchy horizons; constrains time-machine formation. |

Confidence calculation per [AGENTS.md section 3.3](../AGENTS.md#33-confidence-rubric):

```text
s_raw  = (+1*0.85 + +1*0.85 + 0*0.85 + 0*0.85 + 0*0.85)
       / (0.85 + 0.85 + 0.85 + 0.85 + 0.85)
       = 1.70 / 4.25
       = 0.400
s_base = (0.400 + 1) / 2 = 0.700

no vetoes
=> confidence = 0.70
```

No C-veto is assigned: the claim is supported, but not by replicated experimental confirmation or by a broad no-free-parameter derivation of a real FTL technology.

Draft local audit: [preferred-frame-ftl-chronology](../audits/2026-05-15-preferred-frame-ftl-chronology/) gives a `confirmed-with-caveat` result for a toy global-time-constrained propagation law. It is not counted in the confidence score until sandboxed peer review is run.

## Open sub-questions

- Can any constrained FTL mechanism be made operational at macroscopic distance with information transfer, not just phase/group velocity behavior?
- Can multiple constrained regions be arranged without destroying stable causality?
- Can a mechanism-constrained route carry matter or only signals?
- If the mechanism requires a preferred frame, what physical field or boundary condition defines it?
- Can such a mechanism coexist with existing Lorentz-invariance bounds?
- Can it be scaled without violating quantum inequalities, energy conditions, or backreaction constraints?

## Research TODOs

Paper-plan thread: [research/ftl-chronology-safe-signals-paper.md](../research/ftl-chronology-safe-signals-paper.md).

- [ ] Run sandboxed peer review for [preferred-frame-ftl-chronology](../audits/2026-05-15-preferred-frame-ftl-chronology/).
- [ ] Audit multi-device preferred/effective-frame networks for stable causality.
- [ ] Re-read and log Barton 1990 plus Scharnhorst-Barton 1993.
- [ ] Quantify the Scharnhorst speed shift and audit Milonni-Svozil's operational no-measurement argument.
- [ ] Survey Bruneton-style superluminal classical-field causality criteria.
- [ ] Build a candidate-mechanism table separating signal FTL, transport FTL, effective-medium artifacts, and chronology-unsafe cases.
- [ ] Audit Lorentz-violation bounds for any proposed preferred-frame substrate.
- [ ] Draft an arXiv-style note once the preferred-frame audit has sandboxed peer review.

## To read / to audit

- [ ] Barton 1990, "Faster-than-c light between parallel mirrors. The Scharnhorst effect rederived," DOI 10.1016/0370-2693(90)91224-Y.
- [ ] Scharnhorst and Barton 1993, "QED between parallel mirrors: Light signals faster than c, or amplified by the vacuum," DOI 10.1088/0305-4470/26/8/024.
- [ ] Bruneton 2007, "On causality and superluminal behavior in classical field theories."
- [ ] Audit multi-device preferred-frame networks for stable causality, not just a single two-leg relay.
- [ ] Audit Lorentz-violation bounds for any preferred-frame physical field proposed as the FTL substrate.

## Changelog

- 2026-05-15: opened at `supported`, confidence 0.70. Evidence supports the narrow causal claim that constrained faster-than-c propagation can avoid the antitelephone, while leaving practical FTL capability open. Added a draft local audit but did not count it in confidence pending sandboxed peer review.
- 2026-05-15: added explicit research TODOs and linked the paper-plan thread at [research/ftl-chronology-safe-signals-paper.md](../research/ftl-chronology-safe-signals-paper.md).
