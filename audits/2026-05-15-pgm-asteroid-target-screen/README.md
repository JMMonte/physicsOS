---
slug: 2026-05-15-pgm-asteroid-target-screen
claim: n/a
conventions: SI; PGM grades in ppm by mass; prices in USD
verdict: inconclusive
audit_layers: [dimensional, order-of-magnitude, numerical]
created: 2026-05-15
peer_reviewed: n/a
reviewer_verdicts:
  devil_advocate: n/a
  source_fidelity: n/a
  reproducibility: n/a
---

# PGM Asteroid Target Screen

## Claim under audit

There may be known asteroid targets with sufficiently high platinum-group-metal content to make asteroid mining economically worthwhile.

This screen asks a narrower question: do currently identified targets already have enough evidence to be treated as mine-ready PGM ore bodies?

## Source(s)

- [Sanchez et al. 2021](../../papers/2021-sanchez-metal-rich-neas-1986-da-2016-ed85.md), DOI: [10.3847/PSJ/ac235f](https://doi.org/10.3847/PSJ/ac235f), arXiv: [2109.13950](https://arxiv.org/abs/2109.13950).
- [Cannon et al. 2023](../../papers/2023-cannon-precious-structural-metals-asteroids.md), DOI: [10.1016/j.pss.2022.105608](https://doi.org/10.1016/j.pss.2022.105608).
- [Elvis 2014](../../papers/2014-elvis-how-many-ore-bearing-asteroids.md), DOI: [10.1016/j.pss.2013.11.008](https://doi.org/10.1016/j.pss.2013.11.008), arXiv: [1312.4450](https://arxiv.org/abs/1312.4450).
- Ostro et al. 1991, "Asteroid 1986 DA: Radar evidence for a metallic composition", *Science* 252, 1399-1404, DOI: [10.1126/science.252.5011.1399](https://doi.org/10.1126/science.252.5011.1399); NASA NTRS summary: [19920003664](https://ntrs.nasa.gov/citations/19920003664).
- JPL/Lance Benner NEA rendezvous delta-v table, last update 2026-05-08: [echo.jpl.nasa.gov](https://echo.jpl.nasa.gov/lance/delta_v.rendezvous.h.html).
- Current spot-price scale used for arithmetic: Trading Economics platinum, palladium, and rhodium pages, queried 2026-05-15.

## Audit plan

1. Check the value scale for PGM grades in raw asteroid material.
2. Screen named targets against three necessary conditions:
   - metal-rich evidence;
   - PGM-grade evidence;
   - accessibility.
3. Identify what an assay mission must measure before calling a target mineable.

## 1. Dimensional analysis

PGM grade in ppm by mass is

\[
g_\mathrm{ppm}=10^6 M_\mathrm{PGM}/M_\mathrm{bulk}.
\]

Gross raw-bulk value is

\[
V_\mathrm{bulk}=g_\mathrm{ppm}\times10^{-6}P_\mathrm{PGM},
\]

where \(P_\mathrm{PGM}\) is a pure-metal price in \(\$/\mathrm{kg}\). The result is \(\$/\mathrm{kg}\) of raw bulk material.

## 2. Order-of-magnitude

Spot-price scale used in this screen:

| Metal | Price used | Converted price |
|---|---:|---:|
| Pt | \(2029.40\,\$/\mathrm{troy\,oz}\) | \(65246.7\,\$/\mathrm{kg}\) |
| Pd | \(1435.00\,\$/\mathrm{troy\,oz}\) | \(46136.3\,\$/\mathrm{kg}\) |
| Rh | \(9975.00\,\$/\mathrm{troy\,oz}\) | \(320703.7\,\$/\mathrm{kg}\) |

Cannon et al. give iron-meteorite total PGM grades of \(\sim6\text{--}230\,\mathrm{ppm}\), with median \(\sim40.78\,\mathrm{ppm}\).

Therefore raw-bulk value is small unless material is processed or concentrated:

| Grade case | Raw-bulk value if all PGMs priced as Pt | Raw-bulk value if all PGMs priced as Rh |
|---|---:|---:|
| \(10\,\mathrm{ppm}\) Ostro 1986 DA assumption | \(0.65\,\$/\mathrm{kg}\) | \(3.21\,\$/\mathrm{kg}\) |
| \(40.78\,\mathrm{ppm}\) Cannon median iron meteorite | \(2.66\,\$/\mathrm{kg}\) | \(13.08\,\$/\mathrm{kg}\) |
| \(230\,\mathrm{ppm}\) Cannon high iron meteorite | \(15.01\,\$/\mathrm{kg}\) | \(73.76\,\$/\mathrm{kg}\) |

This is the critical sanity check: a PGM-return architecture cannot economically return undifferentiated asteroid bulk. It must process large bulk masses and return refined PGMs or high-grade concentrate.

## 3. Target screen

| Target | Composition evidence | PGM evidence | JPL \(\Delta v\) from LEO | Screen verdict |
|---|---|---|---:|---|
| 6178 (1986 DA) | radar metallic plus NIR metal-rich; \(\sim85\%\) metal / \(\sim15\%\) pyroxene | inferred from meteoritic metal analogs; no direct assay | \(7.157\,\mathrm{km\,s^{-1}}\) | best known PGM prospecting target, not mine-ready |
| 2016 ED85 | NIR spectrum similar to 1986 DA; no radar confirmation | inferred from metal-rich analogs; no direct assay | \(7.376\,\mathrm{km\,s^{-1}}\) | prospecting watchlist, less secure than 1986 DA |
| 7474 (1992 TC) | reported M-type; modern composition not audited here | no PGM-grade evidence found in this screen | \(5.619\,\mathrm{km\,s^{-1}}\) | characterization candidate, not mine-ready |

Elvis estimates that under a stringent \(D\gtrsim100\,\mathrm{m}\), \(\Delta v<4.5\,\mathrm{km\,s^{-1}}\) criterion, only roughly \(10\) PGM ore-bearing NEOs exist in the modeled population. Relaxing to \(\Delta v\sim5.7\,\mathrm{km\,s^{-1}}\) increases the expected number by about an order of magnitude, but target identity remains uncertain.

## Result

Known targets do not yet establish a mineable PGM ore body.

The most credible named target is 6178 (1986 DA), because it has both radar and NIR evidence for high metal content. However, its PGM grade is inferred, not assayed; its JPL rendezvous delta-v is \(7.157\,\mathrm{km\,s^{-1}}\); and the economics require beneficiation/refining rather than returning bulk material.

2016 ED85 is a weaker analog of 1986 DA because it lacks radar confirmation. 7474 (1992 TC) is interesting mainly because its JPL delta-v is lower, \(5.619\,\mathrm{km\,s^{-1}}\), but this audit did not find load-bearing modern PGM-grade evidence for it.

## Verdict

`inconclusive` -- plausible PGM-rich prospecting targets exist, especially 6178 (1986 DA), but no known target currently has the evidence needed to call it economically mineable. The limiting missing data are direct PGM grade, heterogeneity, physical mining properties, beneficiation yield, and a target-specific trajectory/return architecture.

## Caveats and unresolved

- JPL delta-v values are screening approximations, not optimized mission designs.
- Current spot prices are volatile and not a demand curve; market absorption is unaudited.
- This audit does not model Starship refueling, aerocapture, sample return capsules, or reusable transfer vehicles.
- This audit does not validate 7474 (1992 TC)'s taxonomy from primary spectroscopy.
- PGM composition is not a single metal price; the Pt/Pd/Rh cases are bounding examples.

## Reproduction

Run:

```bash
python3 audits/2026-05-15-pgm-asteroid-target-screen/audit.py
```

Outputs:

- [outputs/pgm_prices.csv](outputs/pgm_prices.csv)
- [outputs/pgm_grade_value_scale.csv](outputs/pgm_grade_value_scale.csv)
- [outputs/target_screen.csv](outputs/target_screen.csv)

## Changelog

- 2026-05-15: audit created. Verdict: inconclusive.
