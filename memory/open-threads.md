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
