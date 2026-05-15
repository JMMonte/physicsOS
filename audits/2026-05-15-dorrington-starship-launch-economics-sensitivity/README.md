---
slug: 2026-05-15-dorrington-starship-launch-economics-sensitivity
claim: n/a
conventions: SI; Dorrington-Olsen EBPS cost model
verdict: confirmed-with-caveat
audit_layers: [dimensional, limits, numerical]
created: 2026-05-15
peer_reviewed: n/a
reviewer_verdicts:
  devil_advocate: n/a
  source_fidelity: n/a
  reproducibility: n/a
---

# Dorrington-Olsen Starship Launch-Economics Sensitivity

## Claim under audit

Starship launch economics may improve the Dorrington-Olsen asteroid-mining case, but only if the architecture/model changes more than the launch-cost scalar \(c_l\). This audit separates three cases:

- retaining the paper's market assumption \(c_\mathrm{sale}=0.9c_l\);
- asking what production cost or return capacity would be needed at Starship launch prices;
- decoupling sale price from launch cost, as would be needed for a non-LEO commodity, cislunar propellant, construction feedstock, or other market with its own price.

This audit checks that claim inside the paper's own model.

## Source(s)

- Base model audit: [../2026-05-15-dorrington-bemr-delta-v-thresholds/](../2026-05-15-dorrington-bemr-delta-v-thresholds/)
- Dorrington & Olsen, "Parametric economic modelling of asteroid mining architectures", *Acta Astronautica* 241, 19-47, DOI: [10.1016/j.actaastro.2025.11.006](https://doi.org/10.1016/j.actaastro.2025.11.006).
- SpaceX Starship page: payload capacity \(100-150\,\mathrm{t}\) fully reusable to orbit, [spacex.com/vehicles/starship](https://www.spacex.com/vehicles/starship/index.html?abc=).
- Voyager Technologies 2025 10-K: one future launch commitment for \(\$90.0\,\mathrm{M}\), [SEC filing](https://www.sec.gov/Archives/edgar/data/0001788060/000162828026016543/voyg-20251231.htm).

## Audit plan

Use the already-audited EBPS implementation and first vary only \(c_l\):

- baseline: \(c_l=7469.88\,\$/\mathrm{kg}\);
- Starship public high cost: \(\$90\,\mathrm{M}/100\,\mathrm{t}=900\,\$/\mathrm{kg}\);
- Starship public low cost: \(\$90\,\mathrm{M}/150\,\mathrm{t}=600\,\$/\mathrm{kg}\).

The Dorrington-Olsen market coupling is retained:

\[
c_\mathrm{sale}=0.9c_l .
\]

All other paper inputs are unchanged.

Then compute zero-\(\Delta v\) break-even requirements and a decoupled-sale-price sensitivity.

## 1. Dimensional analysis

\(\$90\,\mathrm{M}/100\,\mathrm{t}\) and \(\$90\,\mathrm{M}/150\,\mathrm{t}\) both reduce to \(\$/\mathrm{kg}\). These replace \(c_l\), while \(c_\mathrm{sale}\), \(c_\mathrm{prod}\), and \(c_p\) remain \(\$/\mathrm{kg}\). The NPV expression therefore remains dimensionally unchanged from the base audit.

## 2. Limits / special cases

For chemical EBPS, the unconstrained large-return-mass zero-NPV threshold depends on

\[
\frac{c_\mathrm{sale}}{(1+r)^T(c_l+c_p)} .
\]

With \(c_p=0\) and \(c_\mathrm{sale}=0.9c_l\), this ratio is independent of \(c_l\). Therefore the unconstrained chemical threshold must remain \(1.789\,\mathrm{km\,s^{-1}}\) when only \(c_l\) is changed.

Finite-capacity feasibility is different: lower \(c_l\) also lowers revenue per returned kg, but the paper's fixed production cost \(c_\mathrm{prod}=300000\,\$/\mathrm{kg}\) is unchanged. If \(c_\mathrm{sale}\) is decoupled from \(c_l\), Starship reduces cost without automatically reducing revenue.

## 3. Numerical

The audit imports the peer-reviewed EBPS implementation and recomputes:

- unconstrained chemical zero-NPV threshold;
- unconstrained electric zero-NPV threshold, maximizing over BEMR;
- finite-capacity thresholds under \(M_\mathrm{max}=160000\,\mathrm{kg}\);
- maximum finite-capacity NPV at \(\Delta v=0\);
- break-even production cost and required return capacity at \(\Delta v=0\);
- finite-capacity thresholds for fixed sale prices independent of Starship launch cost.

Outputs:

- [outputs/starship_launch_cost_sensitivity.csv](outputs/starship_launch_cost_sensitivity.csv)
- [outputs/starship_zero_dv_requirements.csv](outputs/starship_zero_dv_requirements.csv)
- [outputs/starship_decoupled_sale_price_sensitivity.csv](outputs/starship_decoupled_sale_price_sensitivity.csv)

## Result

| Scenario | \(c_l\) | \(c_\mathrm{sale}\) | Chemical unconstrained | Electric unconstrained | Finite-capacity positive-NPV threshold |
|---|---:|---:|---:|---:|---|
| Dorrington-Olsen baseline | \(7469.88\,\$/\mathrm{kg}\) | \(6722.89\,\$/\mathrm{kg}\) | \(1.789\,\mathrm{km\,s^{-1}}\) | \(4.435\,\mathrm{km\,s^{-1}}\) | chemical \(1.225\,\mathrm{km\,s^{-1}}\), electric \(4.422\,\mathrm{km\,s^{-1}}\) |
| Starship, \(\$90\,\mathrm{M}/100\,\mathrm{t}\) | \(900\,\$/\mathrm{kg}\) | \(810\,\$/\mathrm{kg}\) | \(1.789\,\mathrm{km\,s^{-1}}\) | \(1.116\,\mathrm{km\,s^{-1}}\) | none within \(M_\mathrm{max}=160000\,\mathrm{kg}\) |
| Starship, \(\$90\,\mathrm{M}/150\,\mathrm{t}\) | \(600\,\$/\mathrm{kg}\) | \(540\,\$/\mathrm{kg}\) | \(1.789\,\mathrm{km\,s^{-1}}\) | \(0.791\,\mathrm{km\,s^{-1}}\) | none within \(M_\mathrm{max}=160000\,\mathrm{kg}\) |

At \(\Delta v=0\), the finite-capacity NPV is already negative in both Starship cases because the model's sale price collapses with launch cost while \(c_\mathrm{prod}=300000\,\$/\mathrm{kg}\) remains fixed.

Zero-\(\Delta v\) break-even requirements under \(c_\mathrm{sale}=0.9c_l\):

| Scenario | Mode | Capacity assumed | Max \(c_\mathrm{prod}\) for break-even | Required capacity at \(c_\mathrm{prod}=300000\,\$/\mathrm{kg}\) |
|---|---|---:|---:|---:|
| Starship, \(\$90\,\mathrm{M}/100\,\mathrm{t}\) | chemical | \(160000\,\mathrm{kg}\) | \(85110\,\$/\mathrm{kg}\) | \(557944\,\mathrm{kg}\) |
| Starship, \(\$90\,\mathrm{M}/100\,\mathrm{t}\) | electric | \(160000\,\mathrm{kg}\) | \(102780\,\$/\mathrm{kg}\) | \(464352\,\mathrm{kg}\) |
| Starship, \(\$90\,\mathrm{M}/150\,\mathrm{t}\) | chemical | \(160000\,\mathrm{kg}\) | \(56610\,\$/\mathrm{kg}\) | \(836083\,\mathrm{kg}\) |
| Starship, \(\$90\,\mathrm{M}/150\,\mathrm{t}\) | electric | \(160000\,\mathrm{kg}\) | \(68520\,\$/\mathrm{kg}\) | \(695833\,\mathrm{kg}\) |

If sale price is not forced to fall with Starship launch price, the result flips:

| Scenario | \(c_l\) | Fixed \(c_\mathrm{sale}\) | Chemical finite-capacity threshold | Electric finite-capacity threshold |
|---|---:|---:|---:|---:|
| Starship, \(100\,\mathrm{t}\), sale price held at paper baseline | \(900\,\$/\mathrm{kg}\) | \(6722.89\,\$/\mathrm{kg}\) | \(3.963\,\mathrm{km\,s^{-1}}\) | \(6.432\,\mathrm{km\,s^{-1}}\) |
| Starship, \(150\,\mathrm{t}\), sale price held at paper baseline | \(600\,\$/\mathrm{kg}\) | \(6722.89\,\$/\mathrm{kg}\) | \(4.651\,\mathrm{km\,s^{-1}}\) | \(6.594\,\mathrm{km\,s^{-1}}\) |
| Starship, \(100\,\mathrm{t}\), sale price fixed | \(900\,\$/\mathrm{kg}\) | \(5000\,\$/\mathrm{kg}\) | \(3.052\,\mathrm{km\,s^{-1}}\) | \(5.050\,\mathrm{km\,s^{-1}}\) |
| Starship, \(150\,\mathrm{t}\), sale price fixed | \(600\,\$/\mathrm{kg}\) | \(5000\,\$/\mathrm{kg}\) | \(3.677\,\mathrm{km\,s^{-1}}\) | \(5.193\,\mathrm{km\,s^{-1}}\) |

## Verdict

`confirmed-with-caveat` -- a Starship-native conclusion is architecture-dependent. If one merely substitutes Starship launch prices while retaining \(c_\mathrm{sale}=0.9c_l\), the EBPS material-resale case worsens because revenue falls with launch cost. If sale price is decoupled from Earth launch cost, Starship-like \(c_l=600\text{--}900\,\$/\mathrm{kg}\) improves finite-capacity thresholds substantially. A proper Starship architecture therefore must model both sides: launch/logistics cost and the actual in-space market price.

## Caveats and unresolved

- The \(\$90\,\mathrm{M}\) figure is a public contract/accounting commitment, not a general SpaceX Starship price sheet.
- The \(100-150\,\mathrm{t}\) payload bracket is to LEO/earth orbit and is not orbit-equivalent to every Dorrington-Olsen launch-cost interpretation.
- This audit keeps \(c_\mathrm{prod}\), dry mass, operations cost, discount rate, propulsion, and capacity fixed. Starship could plausibly lower spacecraft manufacturing, assembly, and logistics costs too; that is a separate architecture audit.
- The result does not address in-space propellant, construction material, or rare-material markets whose sale price is decoupled from Earth launch cost.

## Reproduction

Run:

```bash
python3 audits/2026-05-15-dorrington-starship-launch-economics-sensitivity/audit.py
```

## Changelog

- 2026-05-15: audit created. Verdict: contradicted for the narrow \(c_\mathrm{sale}=0.9c_l\) substitution.
- 2026-05-15: extended to include zero-\(\Delta v\) requirements and decoupled sale-price cases. Verdict: confirmed-with-caveat.
