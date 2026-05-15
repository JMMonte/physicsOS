---
slug: 2026-05-15-preferred-frame-ftl-chronology
claim: ../../claims/mechanism-constrained-ftl-chronology-safe.md
conventions: natural units c=1; 1+1D preferred-frame coordinates; signals always advance preferred time
verdict: confirmed-with-caveat
audit_layers: [dimensional, limits, symbolic, numerical]
created: 2026-05-15
peer_reviewed: null
reviewer_verdicts: {}
---

# Preferred-frame FTL chronology audit

## Claim under audit

Mechanism-constrained faster-than-light propagation can be chronology-safe if the mechanism defines a global preferred/effective time and signals are only allowed to propagate forward in that time.

This audit checks a deliberately narrow model:

> In a 1+1D spacetime with preferred coordinates `(T, X)`, an FTL signal has speed `alpha > 1` only in the preferred frame and every signal edge satisfies `Delta T >= 0`. Ordinary matter worldlines are subluminal and also advance `T`.

## Source(s)

- [Liberati, Sonego, and Visser 2002](../../papers/2002-liberati-faster-than-c-signals-causality.md) for the claim that causality depends on the propagation law and that constrained Scharnhorst-type effects can be benign.
- [Scharnhorst 1990](../../papers/1990-scharnhorst-light-between-plates.md) as the canonical effective-medium/effective-frame faster-than-c example.
- [Milonni and Svozil 1990](../../papers/1990-milonni-svozil-impossibility-scharnhorst-measurement.md) for the operational caveat that Scharnhorst does not give a measured practical FTL signal.
- [Hawking 1992](../../papers/1992-hawking-chronology-protection.md) and [Kay, Radzikowski, and Wald 1997](../../papers/1997-kay-radzikowski-wald-cauchy-horizon-qft.md) for the wider chronology-protection constraints.

## Audit plan

Compare two rules on the same geometry:

1. Dangerous rule: each sender may emit at speed `alpha` in its own inertial rest frame. This is the antitelephone rule audited in [`2026-05-15-ftl-causal-loop-kinematics`](../2026-05-15-ftl-causal-loop-kinematics/).
2. Constrained rule: signals propagate at speed `alpha` only relative to a preferred/effective frame and always advance the preferred time `T`.

## 1. Dimensional analysis

The constrained signal law is

```text
Delta T = |Delta X| / u
```

with units `m / (m/s) = s`. The script checks this with `pint` when available.

## 2. Limits / special cases

For a two-leg exchange with A at `X=0`, B initially at `X=L`, and B receding at speed `beta`, the preferred-frame return time is

```text
T2 = 2 L / (alpha - beta).
```

Limits:

- `alpha -> 1+`: the signal becomes barely superluminal; `T2` remains positive.
- `alpha -> infinity`: the channel approaches preferred-frame simultaneity; `T2 -> 0+`, not `T2 < 0`.
- `beta = 0`: `T2 = 2L/alpha`, ordinary outward and return propagation in the preferred frame.

## 3. Order-of-magnitude

For the same numbers used in the antitelephone audit, `alpha = 2`, `beta = 0.9`, and `L = 1 light-year`, the unrestricted reciprocal rule returns to A at `t = -0.413223140496 years`, while the preferred-frame constrained rule returns at `T = 1.81818181818 years`.

## 4. Symbolic

Preferred frame:

```text
X_A = 0
X_B = L + beta T
X_signal = alpha T
```

First-leg intercept:

```text
T1 = L / (alpha - beta)
X1 = alpha T1
```

B replies leftward under the same preferred-frame mechanism:

```text
X_reply = X1 - alpha (T - T1)
```

Intersect with A at `X=0`:

```text
T2 = T1 + X1/alpha
   = 2 L / (alpha - beta)
```

For `alpha > 1`, `0 <= beta < 1`, and `L > 0`, `T2 > 0`.

More generally, any relay chain has

```text
Delta T_total = sum_i (|Delta X_i| / alpha_i + wait_i) >= 0.
```

If `T` increases along ordinary matter curves and all allowed FTL signal curves, then `T` is a time function for the enlarged causal graph. A closed causal curve would require returning to the same event with strictly increasing `T`, which is impossible.

## 5. Numerical

See [`audit.py`](audit.py). Key output from the worked comparison:

```text
alpha=2.000, beta=0.900, L=1 light-year
T1_pref_year:  0.909090909091
X1_pref_ly:    1.81818181818
t1_B_year:    -1.66847806451
T2_pref_year:  1.81818181818
unrestricted reciprocal sender-frame return: -0.413223140496 yr
preferred-frame constrained return:           1.81818181818 yr
```

The negative `t1_B_year` illustrates the coordinate-ordering trap: in B's Lorentz coordinates, the first reception event can be assigned a time before A's emission, but the mechanism does not use B's inertial rest frame as its signalling frame.

Grid scan for `alpha = 2`:

```text
N=  1000: min_T2=1, max_T2=1.999998, any_negative=False
N= 10000: min_T2=1, max_T2=1.999998, any_negative=False
N=100000: min_T2=1, max_T2=1.999998, any_negative=False
```

## 6. Comparison to data

No direct data comparison is relevant. This is a kinematic and causal-order audit, not an experimental claim.

## Result

The preferred-frame constrained rule avoids the tachyonic antitelephone because every allowed signal and every allowed matter relay advances the same global time coordinate.

## Verdict

`confirmed-with-caveat` -- the narrow causal claim is confirmed for the modeled rule. A mechanism-constrained FTL channel with a global time function can be chronology-safe in this kinematic sense.

## Caveats and unresolved

- This is not a practical FTL engineering route. It supplies a consistency condition a route must satisfy.
- A real mechanism must identify the preferred/effective frame, its domain of validity, how emitters couple to it, and why no arrangement of multiple devices destroys stable causality.
- This audit does not show that Scharnhorst propagation is measurable or usable. Milonni and Svozil argue against that operational interpretation.
- This audit does not solve warp-drive or wormhole energy-condition constraints.
- This audit has not yet gone through sandboxed peer review under [AGENTS.md section 2.6](../../AGENTS.md#26-peer-review). It is not used for a veto.

## Changelog

- 2026-05-15: audit created. Verdict: confirmed-with-caveat.
