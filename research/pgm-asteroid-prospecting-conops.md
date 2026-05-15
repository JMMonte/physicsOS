# PGM Asteroid Prospecting CONOPS

Created: 2026-05-15

## Purpose

Define a concept of operations for determining whether a candidate metal-rich asteroid is economically mineable for platinum-group metals (PGMs).

This is a **prospecting CONOPS**, not a production-mining CONOPS. The first mission should retire grade/recoverability uncertainty, not attempt bulk extraction.

## Governing Premise

Known candidates such as 6178 (1986 DA) are plausible metal-rich targets but not validated ore bodies. Radar and near-IR data can indicate metal-rich composition, but the mining decision requires:

- PGM grade by mass;
- heterogeneity and nugget distribution;
- metal/silicate partitioning;
- surface and subsurface mechanical properties;
- beneficiation yield;
- returnable product form;
- target-specific trajectory and campaign economics.

Sources:

- Sanchez et al. 2021, 1986 DA and 2016 ED85 characterization, DOI: [10.3847/PSJ/ac235f](https://doi.org/10.3847/PSJ/ac235f), arXiv: [2109.13950](https://arxiv.org/abs/2109.13950).
- Cannon et al. 2023, PGM grades in asteroid analogs, DOI: [10.1016/j.pss.2022.105608](https://doi.org/10.1016/j.pss.2022.105608).
- PGM target-screen audit: [../audits/2026-05-15-pgm-asteroid-target-screen/](../audits/2026-05-15-pgm-asteroid-target-screen/).

## Gate 0: Remote Target Downselect

Goal: reduce the candidate set before launching hardware.

Inputs:

- JPL/MPC orbit and delta-v screening;
- optical/NIR spectra for X/M-type or metal-rich signatures;
- thermal inertia / albedo constraints;
- radar albedo and circular polarization ratio where available;
- size, rotation state, binary status, and encounter geometry.

Candidate classes:

- **Tier 1**: metal-rich evidence plus radar confirmation, e.g. 6178 (1986 DA).
- **Tier 2**: metal-rich spectrum but no radar confirmation, e.g. 2016 ED85.
- **Tier 3**: lower delta-v candidates with weak/old metal-rich taxonomy, e.g. 7474 (1992 TC), requiring modern characterization.

Decision rule:

- Do not launch an assay mission unless the target has either radar metallicity evidence or high-quality modern spectra plus acceptable mission windows.

Known screening issue:

- 1986 DA is compositionally strong but JPL's 2026 rendezvous screen gives \(\Delta v=7.157\,\mathrm{km\,s^{-1}}\), above the low-delta-v region used in Elvis-style ore-count estimates.

## Gate 1: Reconnaissance Orbiter

Goal: determine whether the object is worth touching.

Starship role:

- Heavy launch to LEO can reduce launch-cost pressure and support a larger SEP spacecraft, larger aperture instruments, redundant landers, and a return capsule.
- Starship does not by itself solve asteroid rendezvous, sampling, or refining. Use solar electric propulsion or a chemical/SEP hybrid after LEO deployment.

Core spacecraft:

- Solar electric propulsion bus;
- optical navigation and autonomous proximity operations;
- high-gain telecom;
- sample-return capsule if Gate 2 is included on the same launch.

Remote-sensing payload:

- multispectral/near-IR imaging spectrometer for silicate/metal proxies;
- thermal IR radiometer/spectrometer for thermal inertia and surface texture;
- gamma-ray and neutron spectrometer for bulk elemental constraints, following Psyche-type payload logic;
- magnetometer for remanent magnetization / metallic-body context;
- radar transponder or bistatic radar support if Earth-based geometry is insufficient;
- laser altimeter / lidar for shape, slopes, and navigation hazards.

Mission analogs:

- Psyche carries a multispectral imager, magnetometer, and gamma-ray/neutron spectrometer for a metal-rich asteroid investigation [NASA Psyche overview](https://science.nasa.gov/mission/psyche/mission-overview/), [JPL Psyche](https://www.jpl.nasa.gov/missions/psyche/).
- Radar was decisive for the metallic interpretation of 1986 DA [NASA NTRS](https://ntrs.nasa.gov/citations/19920003664), [JPL](https://www.jpl.nasa.gov/news/near-earth-metal-asteroid-discovered/).

Recon operations:

1. Approach phase: optical navigation and unresolved lightcurve refinement.
2. Global survey: shape, spin, mass estimate via spacecraft tracking, surface morphology.
3. Composition mapping: correlate metal-rich spectral regions with thermal and radar-like properties.
4. Hazard mapping: boulders, slopes, spin environment, ejecta risk.
5. Site selection: choose at least three sites with different spectral/thermal/radar signatures.

Gate 1 exit criteria:

- density and surface evidence remain compatible with high metal fraction;
- at least one accessible site has stable navigation geometry;
- predicted sampleability is acceptable;
- no evidence that the surface is dominated by silicate regolith too thick to assay metal-rich material.

## Gate 2: In-Situ Assay Landers

Goal: measure grade and recoverability locally.

Deploy \(3\text{--}6\) small landers/hoppers across distinct terrains. The point is heterogeneity: one point sample is not enough for ore-body validation.

Payload per lander:

- microscopic imager;
- XRF or APXS for major/trace elemental chemistry;
- LIBS or laser-ablation mass spectrometry for metal grains and PGM proxies;
- magnetometer / magnetic susceptibility sensor;
- mini drill or corer to \(\sim10\text{--}50\,\mathrm{cm}\);
- scoop or abrasion tool;
- penetrometer / shear vane / anchor force sensor;
- grain-size and cohesion measurement;
- optional micro-thermal processing cell.

Operational questions:

- Are PGMs hosted in separable metal grains, refractory nuggets, or dispersed phases?
- Does grade vary by terrain enough to target "sweet spots"?
- Can material be excavated and handled in microgravity?
- Does magnetic/electrostatic separation concentrate metal meaningfully?
- Is the surface a metal-rich body, or merely a metal-rich spectral veneer?

Gate 2 exit criteria:

- measured PGM-relevant trace-metal proxies consistent with a pre-set ore threshold;
- beneficiation factor demonstrated in situ;
- mechanical properties allow excavation and anchoring;
- grade heterogeneity mapped well enough to plan a pilot extraction site.

## Gate 3: Sample Return / Concentrate Return

Goal: ground-truth the assay and calibrate remote instruments.

Mission analogs:

- OSIRIS-REx used a touch-and-go sample-acquisition system and returned asteroid material in a sample-return capsule; its instrument suite included imaging, lidar, thermal emission, visible/IR spectroscopy, and X-ray spectroscopy [OSIRIS-REx instruments](https://asteroidmission.org/objectives/instruments/), [NASA TAGSAM release](https://www.nasa.gov/news-release/nasas-osiris-rex-spacecraft-successfully-touches-asteroid/).
- Hayabusa2 demonstrated asteroid touchdown, sample return, rovers/landers, an impactor, LIDAR, near-IR, thermal IR, sampler, and re-entry capsule [JAXA Hayabusa2](https://global.jaxa.jp/projects/sas/hayabusa2/index.html), [NASA Hayabusa2](https://science.nasa.gov/mission/hayabusa-2/).

Preferred returned material:

- not raw bulk unless the mission is purely scientific;
- several kilograms of representative bulk material;
- grams-to-kg of in-situ separated concentrate if feasible;
- sealed witness plates / contamination monitors.

Ground-lab measurements:

- full PGM assay: Pt, Pd, Rh, Ir, Ru, Os, Au;
- mineralogical host phases;
- grain-size distribution;
- magnetic/electrostatic separation tests;
- thermal/mechanical processing tests;
- recovery efficiency and concentrate grade;
- contamination and volatility controls.

Gate 3 exit criteria:

- demonstrated concentrate with known PGM grade and recovery efficiency;
- remote/in-situ measurements calibrated to lab assay;
- revised resource model supports or rejects a pilot operation.

## Gate 4: Pilot Beneficiation Demonstrator

Goal: prove tonnes-per-year processing physics, not commercial scale.

Hardware:

- anchored or free-flying mining head;
- excavation or abrasion system;
- comminution only if necessary;
- magnetic separation;
- electrostatic/density/thermal separation experiments;
- concentrate storage;
- dust control and rejected-tailings handling;
- power system sized for continuous operation.

Pilot scale:

- process \(10^2\text{--}10^4\,\mathrm{kg}\) raw material;
- return \(10^0\text{--}10^2\,\mathrm{kg}\) concentrate or refined product if justified;
- measure throughput, wear, power, losses, and grade variability.

Gate 4 exit criteria:

- measured processing cost and recovery efficiency close the NPV model under conservative market-price assumptions;
- target can supply enough material without destroying operations through dust, spin, ejecta, or anchoring failure;
- returned product has a terrestrial buyer specification.

## Gate 5: Commercial Extraction Campaign

Only after Gate 4.

Architecture options:

- repeated small concentrate returns to avoid flooding PGM markets;
- reusable SEP tug plus Earth-entry capsules;
- in-space staging/refueling if it actually reduces total campaign cost;
- local beneficiation with Earth refining;
- eventual local refining only if power, reagent, and waste constraints are solved.

Commercial product:

- refined PGMs or certified high-grade concentrate;
- not undifferentiated asteroid bulk.

Market constraint:

- annual returned mass must be tied to demand curves for Pt/Pd/Rh/Ir/Ru/Os, not just spot prices.

## Critical Measurements

The minimum measurement set before claiming mineability:

| Measurement | Why it matters |
|---|---|
| PGM grade by element | Revenue model; Pt/Pd/Rh basket changes value by orders of magnitude |
| Host phase / grain size | Determines whether beneficiation is easy or hard |
| Metal/silicate distribution | Remote metal-rich classification is not enough |
| Heterogeneity map | Determines whether there are mineable zones |
| Regolith cohesion and bearing strength | Anchoring/excavation feasibility |
| Dust/ejecta behavior | Operations risk |
| Concentration factor | Whether raw ppm material can become returnable product |
| Recovery efficiency | Converts resource inventory into recoverable reserve |
| Throughput/power | Determines production cost |
| Target-specific trajectory | Determines campaign cadence and return mass |

## Current Best CONOPS

For 6178 (1986 DA):

1. Do not start with a mining spacecraft.
2. Send a Starship-launched SEP reconnaissance/prospecting mission.
3. Carry Psyche-like global instruments, OSIRIS-REx/Hayabusa2-like proximity operations capability, and multiple small assay landers.
4. Return a calibrated sample/concentrate.
5. Decide on pilot beneficiation only after lab assay confirms grade and separability.

For lower-delta-v M/X candidates:

1. First run a ground-based/radar/spectral campaign to upgrade taxonomy.
2. If metal-rich evidence survives, send a cheaper flyby/rendezvous characterization mission.
3. Promote to assay only if composition evidence approaches 1986 DA quality.

## Open Audits

- Cross-match MITHNEOS/SMASS metal-rich candidates against the JPL 2026 delta-v table.
- Define ore-threshold criteria: minimum grade, recovery efficiency, and market-price floor.
- Build a PGM demand/price-impact model.
- Evaluate whether Starship + SEP makes 1986 DA cadence acceptable despite \(\Delta v=7.157\,\mathrm{km\,s^{-1}}\).
