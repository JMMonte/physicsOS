---
slug: 2026-05-15-dorrington-bemr-delta-v-thresholds
claim: ../../claims/dorrington-ebps-delta-v-thresholds.md
conventions: SI; impulsive ideal rocket equation; no metric/Fourier convention relevant
verdict: confirmed
audit_layers: [dimensional, limits, symbolic, numerical]
created: 2026-05-15
peer_reviewed: 2026-05-15
reviewer_verdicts:
  devil_advocate: minor issues
  source_fidelity: minor mismatches
  reproducibility: fully reproduces
---

# Dorrington-Olsen EBPS BEMR Delta-v Thresholds

Conventions: SI engineering units; ideal impulsive Tsiolkovsky rocket equation; \(\Delta v\) in \(\mathrm{m\,s^{-1}}\), \(I_{sp}\) in seconds, \(v_e=g_0 I_{sp}\).

## Claim under audit

Dorrington and Olsen report that, in their numerical break-even analysis, a single-trip asteroid-mining architecture with propellant supplied entirely from Earth is economically feasible only below target asteroid delta-vs of about \(1.8\,\mathrm{km\,s^{-1}}\) for chemical propulsion and \(4.5\,\mathrm{km\,s^{-1}}\) for electric propulsion. This audit tracks reproduction of the paper's rounded zero-NPV BEMR thresholds. It also separately checks the finite \(160{,}000\,\mathrm{kg}\) maximum-capacity constraint from Table 11.

The full text defines these delta-vs as the **average one-way transfer delta-v**:

\[
\Delta V_\mathrm{avg} = (\Delta V_{EA}+\Delta V_{AE})/2
\]

and Appendix B sets \(\Delta V_{EA}=\Delta V_{AE}\), hence \(\Delta V_\mathrm{tot}=2\Delta V_{EA}\).

## Source(s)

- [paper note](../../papers/2026-dorrington-parametric-economic-asteroid-mining.md)
- Dorrington & Olsen, "Parametric economic modelling of asteroid mining architectures", *Acta Astronautica* 241, 19-47, DOI: [10.1016/j.actaastro.2025.11.006](https://doi.org/10.1016/j.actaastro.2025.11.006).
- Full article text from the open-access PDF associated with the DOI.

## Audit plan

The audit implements the Earth-based propellant supply (EBPS) single-trip equations from the paper:

- Eq. (20), Tsiolkovsky rocket equation;
- Eq. (A.32), EBPS launch mass;
- Eq. (A.33), EBPS propellant mass;
- Eq. (A.36), asteroid-to-Earth propellant mass;
- Eq. (A.40), EBPS total NPV;
- Eq. (28), zero-profit limiting delta-v;
- Table 7, EBPS mission-duration model;
- Table 11 and Appendix B, trade-study numerical inputs.

Layers:

- dimensional check of the rocket-equation quantities;
- zero-\(\Delta v\) and small-\(\Delta v\) limits;
- symbolic reproduction of the zero-profit and chemical zero-NPV threshold;
- numerical maximization over BEMR for the electric zero-NPV threshold;
- convergence check on the electric threshold;
- finite-capacity check with \(M_\mathrm{max}=160{,}000\,\mathrm{kg}\);
- parameter-scope check documenting how the result moves when the paper's model inputs are intentionally changed.

## 1. Dimensional analysis

The ideal rocket equation uses

\[
R = \frac{m_0}{m_f}=\exp\left(\frac{\Delta v}{g_0 I_{sp}}\right).
\]

\(g_0 I_{sp}\) has units \(\mathrm{m\,s^{-2}}\cdot\mathrm{s}=\mathrm{m\,s^{-1}}\), so \(\Delta v/(g_0 I_{sp})\) is dimensionless. A break-even mass ratio is a mass divided by a mass, so it is dimensionless.

The script uses `scipy.constants.g` for \(g_0\).

## 2. Limits / special cases

The script verifies:

- \(\Delta v=0\Rightarrow e^{\Delta v/v_e}=1\), launch mass equals dry mass, and propellant mass is zero.
- In chemical EBPS, the duration is fixed at \(2T_\mathrm{OF,Imp}+T_\mathrm{cap}=1\,\mathrm{yr}\) under the paper's settings.
- In electric EBPS, the low-thrust duration goes to zero at \(\Delta v=0\), since the paper's simplified duration model is \(T\sim \Delta v\,m/F_T\).

## 3. Symbolic

For EBPS, Eq. (A.40) can be written as

\[
NPV=M_R\left[
\frac{c_\mathrm{sale}}{(1+r)^T}
-(c_l+c_p)\left(e^{\Delta V_\mathrm{tot}/v_e}-e^{\Delta V_{EA}/v_e}\right)
\right]
-m_\mathrm{dry}\left[
(c_\mathrm{prod}+c_l)+(c_l+c_p)\left(e^{\Delta V_\mathrm{tot}/v_e}-1\right)
\right]
-c_\mathrm{ops}T .
\]

At large \(M_R\), the sign of the coefficient multiplying \(M_R\) determines whether increasing return mass can ever recover the fixed capital cost. The limiting delta-v occurs when that coefficient is zero.

For zero profit, discounting is ignored and the paper gives Eq. (28):

\[
\Delta V_\mathrm{lim}=v_e\ln\left[
\frac{1}{2}
\left(1+\sqrt{1+\frac{4c_\mathrm{sale}}{c_l+c_p}}\right)
\right].
\]

For zero NPV in the chemical case, the same derivation applies with \(c_\mathrm{sale}\rightarrow c_\mathrm{sale}(1+r)^{-T}\), because \(T=1\,\mathrm{yr}\) is independent of \(M_R\).

The script verifies the algebra symbolically with SymPy by setting \(y=\exp(\Delta V_{EA}/v_e)\) and \(q=c_\mathrm{sale}/(c_l+c_p)\). The threshold condition becomes

\[
y^2-y-q=0,
\]

whose positive root is

\[
y=\frac{1}{2}\left(1+\sqrt{1+4q}\right),
\]

recovering Eq. (28) with zero symbolic residual.

## 4. Numerical

For the electric case, \(T\) depends on \(M_R\) through Table 7:

\[
T =
\frac{\Delta V_{EA}}{F_T}m_0+
\frac{\Delta V_{AE}}{F_T}\left(m_\mathrm{dry}+M_R+m_{p,AE}\right),
\]

converted from seconds to years. The script maximizes \(NPV(\Delta V, BEMR)\) over \(BEMR=M_R/m_\mathrm{dry}\) and finds where that maximum crosses zero.

The electric threshold is stable under optimizer and search-window changes:

| log10 BEMR window | optimizer tolerance | threshold |
|---|---:|---:|
| \([-2,4]\) | \(10^{-6}\) | \(4.434973610\,\mathrm{km\,s^{-1}}\) |
| \([-3,5]\) | \(10^{-8}\) | \(4.434972991\,\mathrm{km\,s^{-1}}\) |
| \([-4,6]\) | \(10^{-10}\) | \(4.434972991\,\mathrm{km\,s^{-1}}\) |

## 5. Finite-capacity check

Table 11 also gives \(M_\mathrm{max}=160{,}000\,\mathrm{kg}\). With the audit's total dry mass \(m_\mathrm{dry}=1250\,\mathrm{kg}\), this implies \(BEMR_\mathrm{max}=128\). Enforcing \(0 < BEMR \le 128\) gives:

| Case | Capacity-constrained zero-NPV threshold |
|---|---:|
| EBPS chemical, \(I_{sp}=450\,\mathrm{s}\) | \(1.225\,\mathrm{km\,s^{-1}}\) |
| EBPS electric, \(I_{sp}=3000\,\mathrm{s}\) | \(4.422\,\mathrm{km\,s^{-1}}\) |

Thus the paper's rounded electric threshold is essentially unchanged at the \(0.1\,\mathrm{km\,s^{-1}}\) level, while the chemical \(1.8\,\mathrm{km\,s^{-1}}\) threshold is an unconstrained/asymptotic BEMR limit rather than a finite-capacity positive-NPV boundary for the \(160{,}000\,\mathrm{kg}\) demonstration spacecraft.

## Result

Using the paper's inputs:

- \(m_\mathrm{dry}=1250\,\mathrm{kg}\);
- \(M_\mathrm{max}=160000\,\mathrm{kg}\), used only in the finite-capacity check;
- \(c_l=7469.88\,\$/\mathrm{kg}\);
- \(c_\mathrm{sale}=0.9c_l=6722.89\,\$/\mathrm{kg}\);
- \(c_\mathrm{prod}=300000\,\$/\mathrm{kg}\);
- \(c_p=0\,\$/\mathrm{kg}\);
- \(c_\mathrm{ops}=487160\,\$/\mathrm{yr}\);
- \(r=20\%\);
- \(F_T=10\,\mathrm{N}\);
- \(T_\mathrm{OF,Imp}=0.5\,\mathrm{yr}\).

The audit obtains:

| Case | Recomputed threshold | Paper value |
|---|---:|---:|
| EBPS chemical, \(I_{sp}=450\,\mathrm{s}\), zero-profit | \(1.997\,\mathrm{km\,s^{-1}}\) | not the headline NPV threshold |
| EBPS chemical, \(I_{sp}=450\,\mathrm{s}\), zero-NPV | \(1.789\,\mathrm{km\,s^{-1}}\) | \(\sim1.8\,\mathrm{km\,s^{-1}}\) |
| EBPS electric, \(I_{sp}=3000\,\mathrm{s}\), zero-profit | \(13.315\,\mathrm{km\,s^{-1}}\) | not the headline NPV threshold |
| EBPS electric, \(I_{sp}=3000\,\mathrm{s}\), zero-NPV, max over BEMR | \(4.435\,\mathrm{km\,s^{-1}}\) | \(\sim4.5\,\mathrm{km\,s^{-1}}\) |
| EBPS chemical, finite \(M_\mathrm{max}=160000\,\mathrm{kg}\) | \(1.225\,\mathrm{km\,s^{-1}}\) | separate capacity-bound check |
| EBPS electric, finite \(M_\mathrm{max}=160000\,\mathrm{kg}\) | \(4.422\,\mathrm{km\,s^{-1}}\) | separate capacity-bound check |

## Verdict

`confirmed` — the audit reproduces the paper's EBPS headline BEMR thresholds to rounding: \(1.789\,\mathrm{km\,s^{-1}}\approx1.8\,\mathrm{km\,s^{-1}}\) and \(4.435\,\mathrm{km\,s^{-1}}\approx4.5\,\mathrm{km\,s^{-1}}\), using the paper's equations and cost/propulsion/duration inputs. The finite-capacity check is recorded separately and narrows the chemical positive-NPV boundary for the \(160{,}000\,\mathrm{kg}\) example spacecraft.

## Scope and unresolved

- The audit checks the EBPS single-trip threshold claim only, not ISPP or multi-trip architectures.
- The paper's Table 12 appears to contain a unit typo for the chemical EBPS row (`m/s` instead of `km/s`); surrounding text and abstract use `km/s`.
- Table 7 prints \(\Delta V_{EA}\) in the electric return-leg duration term where \(\Delta V_{AE}\) is physically implied by \(m_{p,AE}\). The audit uses \(\Delta V_{AE}\); this has no numerical effect under Appendix B's \(\Delta V_{EA}=\Delta V_{AE}\) assumption.
- Table 11 prints \(c_l=7468.88\,\$/\mathrm{kg}\), while Appendix B's Falcon 9 calculation and prose give \(7469.88\,\$/\mathrm{kg}\). The audit uses Appendix B's value; the discrepancy is negligible at the reported precision.
- The audit treats the paper's cost/propulsion/duration inputs as the claim's regime. A separate scope-sensitivity output records how the result changes if those inputs are intentionally changed.

## Issues surfaced by peer review

Round 1 reports are in [round1/](round1/).

- Devil's advocate: flagged that the audit reproduced the paper's unconstrained BEMR thresholds but did not enforce the \(160{,}000\,\mathrm{kg}\) maximum capacity from Table 11. Resolution: added `maximum_capacity_kg`, `capacity_constrained_thresholds.csv`, and §5 above. The claim remains confirmed for the narrow reproduction statement; finite-capacity feasibility is now separated.
- Devil's advocate: flagged that `audit_raw_output.txt` leaked the author verdict into the review sandbox. Resolution: removed the verdict print from `audit.py`; future sandbox raw output will contain numbers only.
- Source fidelity: flagged the Table 7 \(\Delta V_{EA}/\Delta V_{AE}\) return-leg symbol and Table 11/App. B launch-cost mismatch. Resolution: documented both in Scope.
- Reproducibility: fully reproduced; no numerical, equation, dimensional, or convention errors found.

## Reproduction

Run:

```bash
python3 audits/2026-05-15-dorrington-bemr-delta-v-thresholds/audit.py
```

Outputs:

- `outputs/ebps_npv_thresholds.csv`
- `outputs/electric_threshold_convergence.csv`
- `outputs/capacity_constrained_thresholds.csv`
- `outputs/scope_sensitivity.csv`

## Changelog

- 2026-05-15: audit created from abstract/metadata only. Verdict: inconclusive.
- 2026-05-15: updated from the full article text and implemented the EBPS NPV model. Verdict: confirmed-with-caveat.
- 2026-05-15: added SymPy derivation check, electric root convergence check, and scope-sensitivity output. Verdict: confirmed.
- 2026-05-15: completed sandboxed peer review round 1. Added finite-capacity check and documented source-fidelity findings. Verdict unchanged: confirmed for the narrow BEMR-threshold reproduction claim.
