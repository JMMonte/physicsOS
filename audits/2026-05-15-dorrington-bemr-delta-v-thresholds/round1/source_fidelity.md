## Sources checked (path; accessible Y/N; method of verification)

- Dorrington & Olsen, "Parametric economic modelling of asteroid mining architectures", *Acta Astronautica* 241 (2026) 19-47, DOI `10.1016/j.actaastro.2025.11.006`; accessible Y. Verified through the official ScienceDirect DOI landing page (`https://www.sciencedirect.com/science/article/pii/S0094576525007659`) and the attached open-access PDF at `/tmp/codex-remote-attachments/019e2965-84a6-7bd0-b655-d6c527ea2b41/4FA5EBC2-C074-46F9-A0DD-446B473EA1B9/1-main.pdf`. I extracted the PDF text with `pdftotext` and checked ambiguous equations/tables against rendered PDF pages.
- User-provided PDF `/tmp/codex-remote-attachments/019e2965-84a6-7bd0-b655-d6c527ea2b41/4FA5EBC2-C074-46F9-A0DD-446B473EA1B9/1-main.pdf`; accessible Y. Metadata matches the same Acta Astronautica article and DOI.
- Hidden paper note path `../../papers/2026-dorrington-parametric-economic-asteroid-mining.md`; accessible N in sandbox by design. I did not rely on it.

## Fidelity issues found (one entry per source with the problem)

### Dorrington & Olsen, Acta Astronautica 241

Mostly accurate representation. The audit correctly represents the main source on:

- The article identity, DOI, open-access status, authors, journal, volume, and pages.
- The headline result that single-trip EBPS is feasible only below about 1.8 km/s for chemical propulsion and 4.5 km/s for electric propulsion. The ScienceDirect abstract states those same rounded thresholds for the single-trip, propellant-from-Earth scenario.
- The definition of `Delta V_avg`. The audit says the full text defines it as `(Delta V_EA + Delta V_AE)/2` and calls it the average one-way transfer delta-v. Eq. (1) in the paper matches this, and the surrounding prose uses the phrase "average one-way transfer delta-V".
- Appendix B's equal-leg assumption. The audit says Appendix B sets `Delta V_EA = Delta V_AE`, hence `Delta V_tot = 2 Delta V_EA`; Appendix B states this same equality.
- Eq. (20), the Tsiolkovsky rocket equation. The paper writes the final-to-initial mass ratio as an exponential with negative `Delta V / v_e`, equivalent to the audit/script's `m0/mf = exp(Delta v / v_e)`.
- Eqs. (A.32), (A.33), (A.36), and (A.40), as implemented in the audit for the equal-delta-v EBPS case.
- Eq. (28), the zero-profit limiting delta-v expression. The audit's algebraic root matches the paper's equation.
- The trade-study values for dry masses, propulsion Isp ranges, thrusts, sale price fraction, production cost, operations cost, and 20% discount-rate context.

Minor mismatches:

1. **Table 7 electric duration: audit substitutes `Delta V_AE` where the printed table appears to show `Delta V_EA`.**

   Audit claim:
   > For the electric case, `T = Delta V_EA/F_T m0 + Delta V_AE/F_T (m_dry + M_R + m_p,AE)`, converted from seconds to years.

   Source statement:
   Table 7's EBPS electric-propulsion duration row shows the second leg with `Delta V_EA/F_T`, not `Delta V_AE/F_T`, before `(m_dry + M_R + m_p,AE)`.

   Assessment: This is likely a paper typo or a physically obvious correction by the audit, because the second term is the asteroid-to-Earth leg and carries `m_p,AE`. It has no numerical effect in this audit because Appendix B assumes `Delta V_EA = Delta V_AE`. Still, as a source-fidelity matter, the audit should note that it is correcting/interpreting Table 7 rather than copying it exactly.

2. **Table 11 launch cost differs from Appendix B; the audit uses Appendix B's value.**

   Audit/script input:
   > `c_l = 7469.88 $/kg`

   Source statements:
   Table 11 prints `Specific Launch Cost c_L` as `7468.88 $/kg`; Appendix B computes Falcon 9 `$62M / 8300 kg` and gives `$7,469.88/kg`.

   Assessment: The audit's value is consistent with Appendix B arithmetic and text, but not with the printed Table 11. Because the audit cites "Table 11 and Appendix B" as the numerical inputs, it should explicitly document the internal inconsistency. The effect is negligible for the rounded 1.8/4.5 km/s thresholds.

No substantive overreach found. The audit correctly narrows the paper's headline statement to the EBPS single-trip, whole-asteroid-retrieval scenario using the paper's trade-study regime. It does not improperly generalize the result to all asteroid mining architectures.

## Tier assignments to revisit

- Dorrington & Olsen should be Tier A under AGENTS.md: a peer-reviewed primary paper in *Acta Astronautica*. The audit/source list does not expose frontmatter tier in the sandbox, but any Tier A assignment would be appropriate.
- The hidden in-repo paper note should not itself be load-bearing evidence. The audit appears to cite the DOI and PDF directly, so no tier issue if the paper note is treated only as local reading history.
- The user-provided PDF is not an independent source; it is a copy of the same open-access article. It should not be double-counted in an evidence ledger.

## My independent verdict on the audit (based on source fidelity alone)

The audit is source-faithful on the central claim and on the equations needed to reproduce the EBPS thresholds. The two issues above are minor source-fidelity mismatches: one likely correction of a printed Table 7 symbol, and one paper-internal numerical typo/inconsistency in Table 11 versus Appendix B. Neither changes the audit's equal-leg reproduction, but both should be documented in the audit caveats or methodology notes.

## Final verdict (one of: all sources accurately represented / minor mismatches / substantive misrepresentation)

minor mismatches
