# papers/

One markdown file per paper actually read. The folder is the agent's reading log and the substrate for every citation in `claims/`.

## Filename convention

`<year>-<first-author-lastname>-<short-slug>.md`

Examples:
- `2023-maldacena-eternal-traversable-wormhole.md`
- `2019-event-horizon-telescope-m87-shadow.md` (collaboration → use collaboration slug)
- `1998-perlmutter-supernova-cosmology.md`

## Rules

1. Use [`_template.md`](_template.md). Don't skip fields — empty fields invite cargo-cult notes.
2. The **"What it actually shows"** section is the most important. Distinguish the paper's real load-bearing result from its abstract framing. Marketing claims and theorems are not the same thing.
3. Note the **source tier** (see [AGENTS.md §1.3](../AGENTS.md#13-source-weighting)) in the frontmatter so claim-confidence calculations can be automated later.
4. If you only read the abstract, **do not create a paper note**. Note it in the relevant claim's "to read" list instead.
5. Update the file if you re-read the paper later. Notes are living documents; track revisions in the changelog.
