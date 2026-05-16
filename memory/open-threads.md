---
name: Open threads
description: Ongoing investigations that span multiple sessions and have not yet collapsed to a single claim file.
type: project
---

# Open threads

Each entry: short title, current state, pointer to the most recent artifact (paper note, audit, or claim).

## Chronology-safe constrained FTL
- Started: 2026-05-15
- Current state: Narrow claim is `supported` at confidence 0.70; draft preferred-frame audit exists but needs sandboxed peer review before it can feed confidence.
- Latest artifact: [paper plan](../research/ftl-chronology-safe-signals-paper.md)
- Next step: Run sandboxed peer review for [preferred-frame-ftl-chronology](../audits/2026-05-15-preferred-frame-ftl-chronology/), then audit multi-device stable causality.

## MACS0416-Y1 (z=8.312) — early dust, high T_dust, [OIII] anomaly
- Started: 2026-05-16
- Current state: All three headline claims of Takechi et al. 2026 (arXiv:2605.14922) audited. Synthesis: the paper is internally self-consistent (dust/gas/metal/metallicity cross-check to 7%) and the ~10⁶ M☉ dust is comfortably feasible (no "too much dust too early" tension — it is a *small*, budget-easy dust mass). The two genuinely unusual results each survive independent computation but are **load-bearing on a single tightly-constrained anchor**: (a) the small M_dust requires T_dust≈91 K — a canonical 40 K would push dust above the metal mass (unphysical), so high T_dust is *required*, not arbitrary; (b) [OIII]88μm/5007=0.26 exceeds the single-zone dust-free ceiling (~0.13) only because [OIII]4363 pins T_e=17300 K (with T_e free it is trivially reproducible). Both supported at conf 0.81; each exceedance is only ~2σ given quoted errors. Scientific risk is not internal inconsistency but sensitivity to those two anchor measurements.
- Latest artifacts: [early-dust claim](../claims/macs0416y1-early-dust-feasible.md), [OIII-ratio claim](../claims/macs0416y1-oiii-ratio-anomaly.md), audits `2026-05-16-macs0416y1-early-dust/` and `2026-05-16-oiii-88um-5007-single-zone-ceiling/`, [paper note](../papers/2026-takechi-dreams-macs0416y1-early-dust.md)
- Next step: stress the anchors, not the dust budget — (1) robustness of the [OIII]4363-based T_e (detection/blend security); (2) T_dust/β degeneracy from the actual ALMA photometry; (3) Cloudy single-zone grid + alternate O III atomic data for the [OIII] ceiling.

### Resolved
- **arXiv API rate-limit handling** (2026-05-13): `scripts/fetch_arxiv.sh` now enforces a cross-process 4s minimum interval via a `mkdir` mutex and retries 429/5xx via `curl --retry-all-errors`. Tested: 3 parallel calls serialize to ~8s total with no 429s. See [AGENTS.md section 8.1](../AGENTS.md#81-arxiv).

Template entry:

```
## <title>
- Started: YYYY-MM-DD
- Current state: <one sentence>
- Latest artifact: [link](path)
- Next step: <one sentence>
```
