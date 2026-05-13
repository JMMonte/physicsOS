# claims/

A claim is a physics statement we are tracking the truth-value of. This folder is the agent's evolving belief network.

See [AGENTS.md §3](../AGENTS.md#3-claim-ledger-protocol) for the full protocol.

## Filename convention

`<short-slug>.md` — short, kebab-case, durable. Avoid timestamps; claims persist across years.

Examples:
- `cosmological-constant-positive.md`
- `muon-g2-anomaly.md`
- `graphene-dirac-cone-at-k-point.md`

## Lifecycle

```
open ──▶ supported ──▶ ...
   ╰──▶ contested ─┬─▶ refuted
                   ╰─▶ supported (after new evidence)
   ╰──▶ superseded (replaced by a more precise claim)
```

Mark `superseded` when a more precise claim replaces it; link forward.

## Confidence scoring

See [AGENTS.md §3.3](../AGENTS.md#33-confidence-rubric) for the protocol. In brief:

```
s_raw      = Σ (w_i · sign_i) / Σ w_i       ∈ [−1, +1]
s_base     = (s_raw + 1) / 2                ∈ [0, 1]

confidence = min(s_base, 0.10)   if any veto-R
           = max(s_base, 0.90)   if any veto-C (and no veto-R)
           = s_base               otherwise

If both veto-R and veto-C are present: status = "contested"; confidence = s_base.
```

`sign ∈ {+1, 0, -1}` for supports / mixed / contradicts; `w` is the source tier weight from [AGENTS.md §1.3](../AGENTS.md#13-source-weighting); audits enter with `w = 1.00`. Vetoes are categorical and rare — see §3.3 for the strict eligibility list.

This rubric is a structured heuristic, not a Bayesian update. Two high-tier sources in disagreement should surface in the prose, not just average out.

## Rule

**Never edit a claim's confidence without adding an evidence entry.** The ledger should always explain why confidence is what it is.
