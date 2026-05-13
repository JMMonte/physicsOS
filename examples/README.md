# Examples

Curated walkthroughs of the physicsOS protocol applied to real claims.

Each example is a single Markdown file in this directory that ties together the structural artifacts — the claim file, the audits, the paper notes — into a narrative a reader can follow start to finish. The artifacts themselves stay in their normal homes (`claims/`, `audits/`, `papers/`) so the example *is* the protocol, not a copy of it.

## Index

| Example | Domain | Verdict | Confidence |
|---|---|---|---|
| [Casimir Inc.'s "Quantum Energy Chip"](casimir-quantum-energy-chip.md) | quantum vacuum / energy harvesting | `refuted` | 0.10 |

## Adding a new example

When a claim is interesting enough to walk a new reader through:

1. Make sure the artifacts are already in place: a `claims/<slug>.md` file, at least one audit under `audits/<date>-<slug>/`, and paper notes for the load-bearing sources.
2. Create `examples/<short-slug>.md` here. Use the existing Casimir walkthrough as a template. Keep it under ~250 lines — the structural artifacts hold the detail; the walkthrough holds the story.
3. Add a row to the index table above.
4. Optionally link from the [root README](../README.md) if it's the kind of example a new reader should see first.
