## My independent verdict (formed BEFORE steelmanning)

My independent verdict is **minor issues for the narrow reproduction claim, but substantive caveats for any feasibility wording**.

The audit's code reproduces the rounded paper thresholds from the paper's EBPS equations: chemical zero-NPV limit `1.789314 km/s` and electric max-over-BEMR limit `4.434973 km/s` (`audit_script.py` lines 228-241; fresh rerun in `audit_raw_output.txt`). The methodology supports the narrow statement in `claim_statement_only.md`: "reproduction within \(0.1\,\mathrm{km\,s^{-1}}\), matching the paper's rounded statement."

However, the result depends on treating the threshold as an **unconstrained asymptotic BEMR/root-finding limit**, not as a full trade-study feasibility result with the Table 11 maximum capacity. The audit says it uses "Table 11 and Appendix B, trade-study numerical inputs" (`audit_premises_README.md` lines 43-45), but `Maximum capacity 160,000 kg` is not represented anywhere in `Params` (`audit_script.py` lines 34-47) or in the optimization bounds (`audit_script.py` lines 125-156). If the paper's capacity is enforced with the audit's own total dry mass \(1250\,\mathrm{kg}\), the maximum BEMR is \(160000/1250=128\), while the audit's electric optimum at its threshold is BEMR \(140.46\), i.e. return mass \(175,579\,\mathrm{kg}\) (`audit_script.py` lines 238-240). My spot check gives a capacity-constrained electric root of about `4.421694 km/s`, still within the claim's 0.1 km/s tolerance, but a capacity-constrained chemical positive-NPV root near `1.224824 km/s`, not `1.789314 km/s`. The chemical difference arises because the large-return-mass coefficient goes to zero at 1.789 km/s only in the \(M_R \to \infty\) sense; finite capital recovery at a 160,000 kg cap is much stricter.

One review-integrity note: the sandbox says the author's verdict is stripped (`audit_premises_README.md` line 9), but `audit_raw_output.txt` contains `[verdict] Confirmed...`. I ignored that for the verdict above, but it is an anchoring leak in the sandbox design.

## Strongest defense of the opposing position

The strongest defense against the audit's confirming posture is:

1. The paper's \(1.8/4.5\,\mathrm{km\,s^{-1}}\) language is not merely a reproduction of an algebraic singularity; it is presented in a trade study that includes physical sizing parameters, including `Maximum capacity 160,000 kg` in Table 11. If "economically feasible" is read literally, a BEMR solution that requires an impossible or excluded return mass should not count.

2. The audit equates "below the coefficient-zero limit" with "can produce positive economic returns" (`audit_premises_README.md` lines 91-102). This is true only if return mass is unbounded, and the paper itself discusses maximum capacity and spacecraft sizing. At any delta-v close to the limiting value, the required BEMR diverges. Therefore the mathematically correct threshold for the unconstrained model can still overstate the feasible region of the finite spacecraft trade study.

3. The electric threshold is found by maximizing over a broad artificial BEMR range (`audit_script.py` lines 125-140) rather than solving the paper's BEMR equation directly under stated capacity. Search-window convergence (`audit_premises_README.md` lines 130-136) only shows numerical stability of the chosen unconstrained optimization problem; it does not show that this is the same problem as "using their stated trade-study inputs."

4. The chemical threshold is especially vulnerable. The audit's chemical result uses a large-return-mass coefficient substitution (`audit_premises_README.md` lines 91-102; `audit_script.py` lines 117-122). That is a correct asymptotic limiting delta-v, but the phrase "positive-NPV threshold" is stronger than the math unless the audit explicitly states "unbounded return mass."

## Audit assumptions worth challenging

- **Unbounded return mass / no capacity constraint.** `Params` omits `maximum_capacity_kg` despite claiming Table 11 inputs (`audit_premises_README.md` lines 43-45; `audit_script.py` lines 34-47). `maximize_npv_over_bemr` optimizes over log10 BEMR windows up to \(10^5\) or \(10^6\) in convergence tests (`audit_script.py` lines 125-156, 244-250), far above the paper's 160,000 kg capacity if BEMR is based on the audit's \(m_\mathrm{dry}=1250\,\mathrm{kg}\).

- **Dry-mass denominator ambiguity.** The audit sets `dry_total_kg = 1000 + 250` (`audit_script.py` lines 34-50) and uses BEMR \(=M_R/m_\mathrm{dry,total}\) (`audit_script.py` lines 91-95). The paper supports using total dry mass in its definitions, but its prose also repeatedly says "spacecraft dry mass" and Table 11 separately lists spacecraft dry mass and mining equipment. This matters for the capacity challenge: BEMR \(140.46\) corresponds to \(175,579\,\mathrm{kg}\) under the audit's denominator, but \(140,463\,\mathrm{kg}\) under a 1000 kg denominator.

- **The paper's own typo/discrepancy is handled one way without quantifying effect.** The audit uses `7469.88 $/kg` (`audit_script.py` line 38), matching Appendix B, while Table 11 text extraction shows `7468.88`. This is negligible numerically, but a citation-fidelity report should mention it because the audit claims Table 11 inputs.

- **Low-thrust duration model is accepted as-is.** The electric duration is coded as \(\Delta V m/F_T\) for both legs (`audit_script.py` lines 83-87). That follows the paper's simplified Table 7 form, but it assumes constant thrust, no power variation with heliocentric distance, no propellant mass-flow/thrust coupling beyond the simple impulse relation, and no trajectory geometry constraints. This is acceptable for reproducing the paper, but not for defending physical feasibility.

- **No direct numerical check against Fig. 9 contours or Table 12 construction.** The audit compares final rounded thresholds, but it does not digitize or otherwise compare BEMR curves from Fig. 9. If the paper's plotted thresholds were read from a finite contour/graph rather than solved as an unconstrained optimizer, this could matter.

- **Root bracketing assumes a single crossing and positive opportunity at low delta-v.** `electric_zero_npv_lim_delta_v` calls `brentq(f, 0.1, 20.0)` (`audit_script.py` line 154). It does not scan for multiple roots or document monotonicity of max NPV over delta-v. This is probably fine here but is an implicit assumption.

## Overreach: prose vs math

- `audit_premises_README.md` lines 91-92: "At large \(M_R\), the sign of the coefficient... determines whether increasing return mass can ever recover the fixed capital cost." Correct, but it should say "in the unbounded-return-mass model." Otherwise the statement reads like a finite feasibility test.

- `audit_premises_README.md` lines 120-128: "The script maximizes \(NPV(\Delta V, BEMR)\) over BEMR..." This omits that the optimizer is bounded only by artificial search windows, not by Table 11 capacity or spacecraft design constraints.

- `audit_premises_README.md` lines 130-136: "The electric threshold is stable under optimizer and search-window changes." This is true for the chosen optimizer but does not validate the missing physical bound. Stability is numerical, not methodological.

- `audit_premises_README.md` lines 140-143: "The audit treats the paper's trade-study inputs as the claim's regime." This is overconfident because a named trade-study input, maximum capacity, is not included. The statement should be narrowed to "cost, propulsion, dry-mass, discount, and thrust inputs."

- `audit_script.py` lines 362-366 prints a verdict in stdout. Besides leaking anchoring information into the sandbox, this makes `audit_raw_output.txt` not verdict-stripped.

## Citation-fidelity concerns (with which sources you fetched and how)

Fetched/checked:

- ScienceDirect OA landing page for Dorrington & Olsen, *Acta Astronautica* 241, 19-47, DOI `10.1016/j.actaastro.2025.11.006`, via web search/open. It confirms the DOI, open-access status, abstract, and headline thresholds.
- User-provided PDF at `/tmp/codex-remote-attachments/.../1-main.pdf`, checked with `pdfinfo`; title/DOI/pages match the ScienceDirect article.
- Sandbox `source_dorrington_olsen.txt`, apparently text extracted from the same PDF, searched and line-numbered with `rg`, `sed`, and `nl`.

Fidelity checks:

- **Average one-way delta-v:** Audit lines 20-26 match the paper. The source defines \(\Delta V_\mathrm{avg}=(\Delta V_{EA}+\Delta V_{AE})/2\) and calls it average one-way transfer delta-v (`source_dorrington_olsen.txt` lines 754-760).

- **Equations used:** The audit's EBPS mass and NPV equations align with Appendix A.3 as far as the text extraction permits. The source gives the launch-mass relation around lines 3428-3439, total propellant relation around 3451-3461, return-leg propellant relation around 3529-3536, and total NPV around 3618-3654. The script's corresponding implementation is `ebps_masses` (`audit_script.py` lines 68-76) and `ebps_npv` (`audit_script.py` lines 91-107). I did not find an equation-transcription error in the load-bearing EBPS terms.

- **Duration model:** The audit follows Table 7's chemical/electric split. The source Table 7 gives chemical \(2T_{OF,Imp}+T_{cap}\) and an electric \(\Delta V/F_T\) mass-duration expression (`source_dorrington_olsen.txt` lines 1450-1524). The code implements this at `audit_script.py` lines 79-87.

- **Trade-study inputs:** The audit matches Appendix B for launch cost (`$7,469.88/kg`, source lines 4030-4038) and dry total (`1250 kg`, source lines 4073-4081), but Table 11's extracted value is `$7468.88/kg` (`source_dorrington_olsen.txt` lines 2039-2075). The audit also omits Table 11 `Maximum capacity 160,000 kg` (`source_dorrington_olsen.txt` lines 2047-2063).

- **Threshold wording:** The source states the chemical and electric limits in the abstract, Section 5.6, and Table 12. Section 5.6 says chemical below 1.8 km/s and electric around 4.5 km/s (`source_dorrington_olsen.txt` lines 2506-2516). Table 12 lists chemical as `< 1.8 m/s` (`source_dorrington_olsen.txt` lines 2558-2576), which the audit reasonably identifies as a unit typo because surrounding source text uses km/s.

- **Scope/future-work caveat:** The paper itself warns the numerical example uses a single parameter set and calls for sensitivity analysis (`source_dorrington_olsen.txt` lines 2748-2756), and it flags simplifying assumptions in delta-v/time-of-flight modeling (`source_dorrington_olsen.txt` lines 2757-2768). The audit's scope section acknowledges parameter sensitivity only partially.

## Missing literature

For the narrow reproduction claim, no additional literature is strictly required beyond the original Dorrington-Olsen paper. For the stronger "feasible/infeasible" language, the audit should at least triangulate against:

- Sonter, "The technical and economic feasibility of mining the near-earth asteroids," *Acta Astronautica* 41, 637-647 (1997). This is a classic NPV/probabilistic feasibility baseline cited by Dorrington-Olsen.
- Hein, Matheson & Fries, "A techno-economic analysis of asteroid mining," *Acta Astronautica* 168, 104-115 (2020), DOI `10.1016/j.actaastro.2019.05.009`; also arXiv:1810.03836. Useful for sensitivity to spacecraft cost, resource/product assumptions, and technology improvements.
- Calla, Fries & Welch, "Asteroid mining with small spacecraft and its economic feasibility," arXiv:1808.05099. Useful for alternative small-spacecraft cost architecture.
- Sanchez & McInnes, "Assessment on the feasibility of future shepherding of asteroid resources," *Acta Astronautica* 73, 49-66 (2012), DOI `10.1016/j.actaastro.2011.12.010`. Relevant to the population/delta-v resource map behind the "few/no asteroids below threshold" implications.
- Edelbaum, "Propulsion requirements for controllable satellites," *ARS Journal* 31(8), 1079-1089 (1961). Relevant if the audit wants to defend or critique the simplified low-thrust \(\Delta V m/F\) duration model rather than merely reproduce it.

## Final verdict (one of: substantive issues / minor issues / agree despite trying not to)

**Minor issues** for the narrow claim "the paper's equations and stated cost/propulsion inputs reproduce rounded \(1.8/4.5\,\mathrm{km\,s^{-1}}\) zero-NPV limiting thresholds."

**Substantive issues** if the audit is used to support broader wording that the architecture is actually economically feasible up to those delta-vs under all Table 11 trade-study inputs. The omitted `Maximum capacity 160,000 kg` is the main reason: with the audit's \(1250\,\mathrm{kg}\) dry-mass denominator, the electric optimum at the reported threshold exceeds capacity, and the chemical finite-capacity positive-NPV boundary is much lower than 1.8 km/s. The audit should explicitly distinguish an unconstrained asymptotic BEMR limit from finite-capacity feasibility.
