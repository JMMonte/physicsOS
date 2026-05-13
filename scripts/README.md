# scripts/

Reusable utilities for the physics agent. Keep these small, single-purpose, and well-documented.

## Current scripts

- [`new_paper.sh`](new_paper.sh) — scaffold a new paper note from the template.
- [`new_audit.sh`](new_audit.sh) — scaffold a new audit directory from the template.
- [`new_claim.sh`](new_claim.sh) — scaffold a new claim file from the template.
- [`fetch_arxiv.sh`](fetch_arxiv.sh) — fetch an arXiv abstract and metadata to seed a paper note.

## Conventions

- All scripts are POSIX-`sh` or `bash`, runnable from the repo root.
- Scripts write to stdout when possible; only create files when their primary purpose is scaffolding.
- No script should have side effects outside the repo. No network writes. Network reads (arXiv, DOI) are fine.
