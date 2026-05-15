---
slug: 2026-05-15-ftl-causal-loop-kinematics
claim: ../../claims/controllable-ftl-engineering-problem.md
conventions: natural units c=1; 1+1D Lorentz transformations; inertial frames; reciprocal FTL signalling rule
verdict: contradicted
audit_layers: [dimensional, limits, symbolic, numerical]
created: 2026-05-15
peer_reviewed: 2026-05-15
reviewer_verdicts:
  devil_advocate: substantive issues
  source_fidelity: minor mismatches
  reproducibility: fully reproduces
---

# FTL causal-loop kinematics audit

## Claim under audit

Controllable faster-than-light signalling or travel can be treated as an engineering problem under established relativistic physics, rather than as a fundamental-physics obstruction.

This audit checks the flat-spacetime signalling subclaim:

> A reciprocal, unrestricted FTL communication rule can coexist with ordinary Lorentz invariance without allowing a causal loop.

## Source(s)

- [Liberati, Sonego, and Visser 2002](../../papers/2002-liberati-faster-than-c-signals-causality.md) for the caution that causality depends on the FTL propagation law, not just on the phrase "faster than c."
- [Olum 1998](../../papers/1998-olum-superluminal-negative-energies.md) for the wider GR result that superluminal travel requires weak-energy-condition violation under Olum's definition and generic-condition assumption.

## Audit plan

The audit derives and numerically checks the tachyonic-antitelephone condition. In natural units, let `alpha = u/c > 1` be the FTL signal speed in the sender's rest frame and `beta = v/c` be the relative speed of two inertial observers. A sends an FTL signal to receding B; B immediately replies with the same FTL rule in B's rest frame. The question is whether the reply can reach A before A's original emission.

## 1. Dimensional analysis

The Lorentz transform for time is

```text
t' = gamma (t - v x / c^2).
```

`v x / c^2` has units `(m/s) m / (m/s)^2 = s`, matching `t`. The script checks this with `pint` when available and falls back to the manual unit chain otherwise.

## 2. Limits / special cases

The derived loop threshold is

```text
beta > 2 alpha / (1 + alpha^2).
```

Limits:

- `alpha -> 1+`: `beta_min -> 1`; barely-superluminal signals need nearly luminal frame separation.
- `alpha -> infinity`: `beta_min -> 0`; arbitrarily fast signals allow loops for modest boosts.
- `beta = 0`: no relativity of simultaneity, hence no loop in this construction.

## 3. Order-of-magnitude

For `alpha = 2`, the threshold is `beta_min = 0.8`. A civilization able to make reciprocal `2c` signals could produce the worked-example causal loop using inertial platforms at `0.9c` relative speed. The exact minimum is any `beta > 0.8`; `0.9c` is just a convenient value above threshold.

## 4. Symbolic

Frame `S`: A is at `x=0`; B starts at `x=L` and recedes with speed `beta`. A sends a signal with speed `alpha`.

First-leg intercept:

```text
t1 = L / (alpha - beta)
x1 = alpha t1
```

Transform to B's rest frame:

```text
t1' = gamma (t1 - beta x1)
x1' = gamma (x1 - beta t1)
```

B replies leftward at speed `alpha`; A's worldline in B's frame is `x_A' = - beta t'`. Solving the intersection gives

```text
t2' = gamma L [2 alpha - beta (1 + alpha^2)] / (alpha - beta)^2.
```

For the second reception event on A's worldline, transforming back to A's frame gives `t2 = t2' / gamma`, so the sign is unchanged. Thus `t2' < 0`, and therefore A receives the reply before the original emission on A's own worldline, when

```text
beta > 2 alpha / (1 + alpha^2).
```

Because `2 alpha / (1 + alpha^2) < 1` for every `alpha > 1`, some Lorentz-allowed inertial boost closes the loop if the same reciprocal FTL rule remains available in the boosted sender frame.

## 5. Numerical

See [`audit.py`](audit.py). The worked example uses `alpha = 2`, `beta = 0.9`, and `L = 1 light-year`.

Key output:

```text
threshold beta_min=0.800000; selected beta exceeds threshold: True
t1_S_year:  0.909090909091
x1_S_ly:    1.81818181818
t2_S_year: -0.413223140496
```

The brute-force grid-resolution scan approaches the symbolic threshold:

```text
N=  1000: beta_first=0.800800000, abs_error=8.000e-04
N= 10000: beta_first=0.800079208, abs_error=7.921e-05
N=100000: beta_first=0.800007200, abs_error=7.200e-06
```

## 6. Comparison to data

No data comparison is relevant. This is a kinematic audit.

## Result

For any reciprocal FTL signal speed `alpha > 1`, there exists an ordinary subluminal inertial boost `beta < 1` such that the two-leg signal exchange reaches A before A's original emission.

## Verdict

`contradicted` -- the audited subclaim fails. The modeled reciprocal sender-rest-frame FTL rule plus Lorentz invariance permits a causal loop, so that specific rule cannot be treated as an ordinary engineering feature under established special relativity.

## Caveats and unresolved

- This audit does not rule out preferred-frame FTL rules, one-way FTL rules, or constrained effective-metric effects such as Scharnhorst propagation. Liberati-Sonego-Visser are explicit that model details matter.
- This audit does not by itself rule out every curved-spacetime or quantum-gravity construction. That wider claim is handled in the ledger by Olum 1998, Ford-Roman 1996, Bobrick-Martire 2021, Santiago-Schuster-Visser 2022, and Fuchs et al. 2024.
- The R-veto from this audit is therefore scoped only to unrestricted reciprocal FTL signalling under ordinary Lorentz transformations. A preferred-frame or mechanism-constrained FTL proposal would need a separate claim and audit.

### Issues surfaced by peer review (2026-05-15)

This audit was peer-reviewed under [AGENTS.md section 2.6](../../AGENTS.md#26-peer-review). Reports are in [`round1/`](round1/).

- **Devil's advocate**: found a substantive scope issue. The algebra refutes only the reciprocal sender-rest-frame FTL rule, not every preferred-frame, effective-metric, one-way, curved-spacetime, or quantum-gravity proposal. Fixed: the verdict, caveats, and claim-file R-veto language now state this scope explicitly.
- **Source fidelity**: found a minor mismatch. Olum 1998 was summarized without the generic-condition assumption. Fixed: the source summary now includes that assumption.
- **Reproducibility**: fully reproduced the script output, symbolic threshold, worked example, grid-resolution scan, dimensional check, and conventions. No code changes required.

## Changelog

- 2026-05-15: audit created. Verdict: contradicted.
- 2026-05-15: round1 sandboxed peer review completed. Revisions narrowed scope wording around the R-veto and added Olum's generic-condition caveat. Verdict unchanged.
