---
title: Parametric economic modelling of asteroid mining architectures
authors: Scott Dorrington, John Olsen
year: 2026
venue: Acta Astronautica 241, 19-47
arxiv: n/a
doi: 10.1016/j.actaastro.2025.11.006
tier: A
read_depth: full
read_on: 2026-05-15
keywords: [asteroid-mining, space-resources, mission-architecture, economics, delta-v]
related_claims: [claims/dorrington-ebps-delta-v-thresholds.md]
related_audits: [audits/2026-05-15-dorrington-bemr-delta-v-thresholds/, audits/2026-05-15-dorrington-starship-launch-economics-sensitivity/]
---

# Parametric economic modelling of asteroid mining architectures

## One-line summary

Dorrington and Olsen formulate parametric economic metrics for asteroid-mining mission architectures and introduce a break-even mass ratio intended to expose delta-v regimes where positive economic return is impossible under the modeled assumptions.

## What it actually shows

- The paper models asteroid-mining mission economics as functions of mission, spacecraft, cost, revenue, propulsion, and returned-mass parameters.
- It compares architecture choices: whole-asteroid return versus in-situ processing; single-trip versus multi-trip retrieval; and propellant supplied from Earth, refueled in orbit, or produced from asteroid resources.
- It defines the break-even mass ratio (BEMR): the asteroid material mass required for zero profit or zero net present value, normalized by spacecraft dry mass.
- The authors argue BEMR is useful because it is invariant to spacecraft dry mass and can reveal delta-v limits where returns cannot become positive merely by scaling returned mass.
- Their numerical example sweeps specific impulse from 450 s to 3000 s and asteroid target delta-v up to 10 km/s.
- In the abstracted numerical study, single-trip architectures with all propellant supplied from Earth are feasible only below about 1.8 km/s for chemical propulsion and 4.5 km/s for electric propulsion.
- The authors find multi-trip retrieval of smaller shipments can outperform a single long-duration large shipment in profitability.
- The paper points to in-situ return propellant, maximizing per-trip returned material, and carrying reserve propellant as architecture choices that improve viability or reduce resource-risk exposure.

## Methods (briefly)

Parametric economic modeling and numerical break-even analysis across mission architectures, propulsion specific impulse, target delta-v, propellant logistics, and retrieved-mass assumptions. The EBPS single-trip threshold equations were checked against the full open-access article text associated with the DOI.

## Key equations / results

- BEMR is \(M_R^*/m_\mathrm{dry}\), the break-even return mass divided by total dry mass.
- The paper defines \(\Delta V_\mathrm{avg}=(\Delta V_{EA}+\Delta V_{AE})/2\), an average one-way transfer delta-v, and in Appendix B sets \(\Delta V_{EA}=\Delta V_{AE}\).
- Numerical sweep: \(I_{sp}=450\text{--}3000\,\mathrm{s}\); target asteroid \(\Delta v\le 10\,\mathrm{km\,s^{-1}}\).
- Reported limiting result for the modeled single-trip, Earth-propellant EBPS case: viable below \(\Delta v \approx 1.8\,\mathrm{km\,s^{-1}}\) for chemical propulsion and \(\Delta v \approx 4.5\,\mathrm{km\,s^{-1}}\) for electric propulsion.
- The in-repo audit confirms the paper's rounded unconstrained BEMR thresholds as \(1.789\,\mathrm{km\,s^{-1}}\) and \(4.435\,\mathrm{km\,s^{-1}}\), respectively, under the paper's cost/propulsion/duration settings.
- Enforcing the \(160{,}000\,\mathrm{kg}\) maximum-capacity value gives finite-capacity EBPS zero-NPV boundaries of \(1.225\,\mathrm{km\,s^{-1}}\) for chemical propulsion and \(4.422\,\mathrm{km\,s^{-1}}\) for electric propulsion.
- A Starship launch-economics sensitivity audit using \(\$90\,\mathrm{M}/(100\text{--}150\,\mathrm{t})=600\text{--}900\,\$/\mathrm{kg}\), while retaining \(c_\mathrm{sale}=0.9c_l\), finds no positive-NPV finite-capacity EBPS solution even at \(\Delta v=0\). The model's sale price falls with launch cost while \(c_\mathrm{prod}=300000\,\$/\mathrm{kg}\) stays fixed.

## Assumptions and regime of validity

The results are architecture- and cost-model dependent. The paper's published abstract indicates dependence on spacecraft dry mass, mission delta-v, propulsion specific impulse, propellant sourcing, return mass, revenues, costs, and net-present-value assumptions. The accessible text does not expose enough equations to audit sensitivity to market price, launch cost, discount rate, processing yield, asteroid composition uncertainty, or operational risk.

## Caveats / open issues

- EBPS single-trip equations, NPV threshold algebra, convergence of the electric root, and propulsion mass-fraction calculations were audited; ISPP and multi-trip cases were not.
- The headline delta-v thresholds are conditional on the authors' numerical assumptions, especially launch cost, sale price, discount rate, thrust, and low-thrust duration model. They are not universal physical limits.
- Market demand and price for returned/in-space resources can dominate the economics; the accessible abstract does not provide enough detail to assess those assumptions.
- Resource uncertainty matters: carrying reserve propellant is recommended because target resource availability may differ from expectations.

## How it informs the asteroid-mining economics claims

This is useful for evaluating whether asteroid mining architectures fail because of propulsion logistics before extraction technology or market demand become the limiting factors. A peer-reviewed audit of the EBPS threshold claim is logged at [audits/2026-05-15-dorrington-bemr-delta-v-thresholds/](../audits/2026-05-15-dorrington-bemr-delta-v-thresholds/) and feeds [claims/dorrington-ebps-delta-v-thresholds.md](../claims/dorrington-ebps-delta-v-thresholds.md). A separate Starship sensitivity audit is logged at [audits/2026-05-15-dorrington-starship-launch-economics-sensitivity/](../audits/2026-05-15-dorrington-starship-launch-economics-sensitivity/).

## Citations to chase

- Sonter, "The technical and economic feasibility of mining the near-earth asteroids", Acta Astronautica 41, 637-647, doi:10.1016/S0094-5765(98)00087-3.
- Hein, Matheson, Fries, "A techno-economic analysis of asteroid mining", Acta Astronautica 168, 104-115, doi:10.1016/j.actaastro.2019.05.009.
- Dorrington and Olsen, "A location-routing problem for the design of an asteroid mining supply chain network", Acta Astronautica 157, 350-373, doi:10.1016/j.actaastro.2018.08.040.

## Audit queue

- [ ] finite-capacity EBPS feasibility under \(M_\mathrm{max}=160000\,\mathrm{kg}\).
- [ ] ISPP single-trip threshold \(\sim8.8\,\mathrm{km\,s^{-1}}\).
- [ ] multi-trip NPV / repeated smaller shipment advantage.
- [ ] full threshold sensitivity to \(c_\mathrm{sale}\), \(r\), \(F_T\), \(m_\mathrm{dry}\), and \(M_\mathrm{max}\). Partial \(c_l\) sensitivity with \(c_\mathrm{sale}=0.9c_l\) is logged in the Starship audit.
- [ ] comparison against Sonter 1997, Hein-Matheson-Fries 2020, and Dorrington-Olsen 2019.

## Changelog

- 2026-05-15: created. Read depth: skim.
- 2026-05-15: linked partial audit of reported delta-v thresholds.
- 2026-05-15: updated note after reading the full article text; EBPS threshold audit now confirms the paper's headline values.
- 2026-05-15: linked supported claim and added finite-capacity distinction surfaced by peer review.
- 2026-05-15: added audit queue for follow-up work.
- 2026-05-15: linked Starship launch-economics sensitivity audit.
