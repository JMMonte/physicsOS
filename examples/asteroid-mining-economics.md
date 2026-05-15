# Asteroid Mining Economics And PGM Target Readiness

This walkthrough ties together the asteroid-mining branch of the repo: a reproduction audit of a recent economic model, a launch-cost sensitivity check, and a separate PGM target-readiness claim.

## Artifacts

| Artifact | Role | Current state |
|---|---|---|
| [claims/dorrington-ebps-delta-v-thresholds.md](../claims/dorrington-ebps-delta-v-thresholds.md) | Reproduction claim for Dorrington-Olsen EBPS thresholds | `supported`, confidence 1.00 |
| [audits/2026-05-15-dorrington-bemr-delta-v-thresholds/](../audits/2026-05-15-dorrington-bemr-delta-v-thresholds/) | EBPS threshold reproduction audit | `confirmed`, sandbox peer-reviewed |
| [audits/2026-05-15-dorrington-starship-launch-economics-sensitivity/](../audits/2026-05-15-dorrington-starship-launch-economics-sensitivity/) | Starship launch-cost sensitivity audit | `confirmed-with-caveat` |
| [claims/known-pgm-asteroid-targets-not-mine-ready.md](../claims/known-pgm-asteroid-targets-not-mine-ready.md) | PGM target-readiness claim | `supported`, confidence 0.86 |
| [audits/2026-05-15-pgm-asteroid-target-screen/](../audits/2026-05-15-pgm-asteroid-target-screen/) | First-pass named-target screen | `inconclusive` |
| [research/pgm-asteroid-prospecting-conops.md](../research/pgm-asteroid-prospecting-conops.md) | Prospecting mission concept | working plan |

## Economic Model Thread

[Dorrington and Olsen 2026](../papers/2026-dorrington-parametric-economic-asteroid-mining.md) report EBPS single-trip break-even thresholds near `1.8 km/s` for chemical propulsion and `4.5 km/s` for electric propulsion. The audit reproduces those rounded values from the paper's equations and inputs: `1.789 km/s` and `4.435 km/s` in [the audit result table](../audits/2026-05-15-dorrington-bemr-delta-v-thresholds/README.md).

Peer review added an important narrative distinction. The headline thresholds are unconstrained BEMR thresholds. Enforcing the paper's `160000 kg` capacity leaves the electric case nearly unchanged at the paper's precision but lowers the chemical finite-capacity boundary to `1.225 km/s`, also recorded in [the same audit](../audits/2026-05-15-dorrington-bemr-delta-v-thresholds/README.md).

The Starship sensitivity audit then asks a narrower question: what happens if the launch-cost scalar changes but the paper's sale-price coupling `c_sale = 0.9 c_l` is retained? The answer is not "Starship fixes it." Under that coupling, lowering `c_l` also lowers revenue per returned kilogram, while production cost remains fixed. Decoupling sale price from Earth launch cost reverses the conclusion, which is why the audit's verdict is [confirmed-with-caveat](../audits/2026-05-15-dorrington-starship-launch-economics-sensitivity/README.md).

## Target-Readiness Thread

The target ledger asks a different question: are currently known metal-rich targets mine-ready PGM ore bodies? The answer is no. [Sanchez et al. 2021](../papers/2021-sanchez-metal-rich-neas-1986-da-2016-ed85.md) make 6178 (1986 DA) and 2016 ED85 credible prospecting candidates, [Cannon et al. 2023](../papers/2023-cannon-precious-structural-metals-asteroids.md) sets a lower and more realistic PGM-grade prior, and [Elvis 2014](../papers/2014-elvis-how-many-ore-bearing-asteroids.md) explains why accessible ore-bearing NEOs should be rare.

The [PGM target-screen audit](../audits/2026-05-15-pgm-asteroid-target-screen/) is intentionally not counted as positive evidence in the claim rubric because its verdict is `inconclusive`. It is still useful operationally: it identifies 1986 DA as the strongest prospecting target, not a validated ore body, and records the missing data that a prospecting mission must measure.

## Current Narrative

The asteroid-mining story is not "impossible" and not "ready." The economic model can be reproduced, but the thresholds are conditional on architecture and market assumptions. Starship-class launch pricing helps only when the architecture and sale-price model change coherently. On the resource side, metal-rich candidates exist, but public data do not yet establish PGM grade, heterogeneity, beneficiation yield, or target-specific return economics.

The next credible move is prospecting, not mining. The current CONOPS sends instruments and assay landers to retire grade and recoverability uncertainty before any production campaign is treated as economically meaningful.
