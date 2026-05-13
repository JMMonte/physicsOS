# Source-fidelity review — 2026-05-13 Casimir energy-budget audit

## Sources checked

| # | Source as cited in audit | Verification method | Accessible? |
|---|---|---|---|
| 1 | Jaffe 2005, *Phys. Rev. D* 72, 021301(R); arXiv:hep-th/0503158 | WebFetch on arXiv abstract | Y |
| 2 | Chernodub 2013, *Phys. Rev. D* 87, 025021; arXiv:1207.3052 | WebFetch on arXiv abstract | Y |
| 3 | Pinto patent family — US 6,477,028 / 6,665,167 / 6,593,566 / 6,650,527 | WebSearch for 6,477,028; WebFetch on Google Patents for 6,665,167 | Partial (one rep. patent fetched in full; family confirmed by search) |
| 4 | White et al. 2026, *Phys. Rev. Research* 8, 013264; DOI 10.1103/l8y7-r3rm | APS abstract page returned 403; recovered via DOAJ + APS search snippet ("Emergent quantization from a dynamic vacuum") | Partial (abstract only, no full text) |
| 5 | Wilson et al. 2011, *Nature* 479, 376; arXiv:1105.4714 | WebFetch on arXiv abstract; Nature gated; PDF binary not parseable | Partial (abstract + setup confirmed; exact per-mode flux not independently retrieved) |

All citations resolve to real, correctly-identified works. No bibliographic fabrications.

## Fidelity issues found

**1. Jaffe 2005 — accurate.** Audit paraphrase: "The Casimir effect can be computed without ever invoking vacuum energy; the popular 'tap the vacuum' framing is a category error." Jaffe's abstract: "Casimir effects can be formulated and Casimir forces can be computed without reference to zero point energies." The audit's framing as "category error" is slightly stronger language than Jaffe's neutral phrasing, but is a fair reading of Jaffe's broader argument that Casimir physics is a relativistic interaction between charges/currents rather than evidence that ZPE is "real." No overreach.

**2. Chernodub 2013 — accurate.** Audit paraphrase: "Closest serious attempt at 'Casimir perpetual motion'; explicitly produces **no** usable work." Chernodub's own abstract calls the proposed devices a *perpetuum mobile of the fourth kind* that "do not produce any work" despite a permanently-rotating ground state. Audit's characterization matches the source's own self-description.

**3. Pinto patent family — accurate, with a minor framing nit.** Audit paraphrase: "The only theoretically plausible Casimir-engine route is boundary-property modulation, and no demonstration of net energy gain exists in 27 years." Verified against US 6,665,167B2 (representative of the family): the patent claims a method/apparatus, contains no experimental validation, and even hedges with "if a net gain of energy is not realized in practice…" Audit's "27 years" is rounded from 1999 (Pinto's initial publication, per the patent's own background) — defensible. The slightly stronger "only theoretically plausible" framing is the audit's editorial judgment, not a claim attributed to Pinto, so no fidelity issue.

**4. White et al. 2026 (PRR 013264) — accurate, and this is the key fidelity check.** Audit paraphrase: "The cited 'theoretical foundation' does not, in fact, address energy extraction." Independently confirmed: the paper is titled *"Emergent quantization from a dynamic vacuum"* and its content is a mathematical/isospectral mapping between an acoustic-dispersion model and the hydrogenic Coulomb spectrum. The DOAJ abstract explicitly contains nothing about energy harvesting, devices, work extraction, or power. The audit's central claim about White 2026 — that Casimir Inc.'s press release misrepresents it as theoretical support for a vacuum-energy chip — is well-supported by the source. Caveat: I could not access the APS-hosted full text (403). A devil's-advocate read would require the body of the paper to confirm there is no buried section on extraction, but title + abstract + DOAJ summary are aligned and contain no power/extraction language.

**5. Wilson et al. 2011 — accurate on setup; the numerical anchor used downstream (≈10⁵ photons/s per mode in the 4–6 GHz band, ≈3×10⁻¹⁹ W/mode) could not be independently verified from the abstract alone.** The audit's narrative §3 explicitly flags the per-mode rate as an OOM estimate derived from the published "few Kelvin per unit bandwidth," not a number lifted from the paper. The audit's qualitative claims (parametric SQUID modulation at ~11 GHz, boundary literally stationary, electrical-length modulated at a few percent of c, two-mode squeezing observed) are all confirmed verbatim by the abstract. The 4–6 GHz analysis band and the few-K noise temperature would need the body of the paper to verify; on the abstract alone I cannot flag a discrepancy, but I cannot fully confirm the OOM derivation either. The audit is appropriately hedged on this point ("OOM figure").

## Tier assignments to revisit

Audit does not assign explicit tier weights inside the README (those live in the claim ledger, which is stripped from the sandbox). Implicit tiers, judged against AGENTS.md §1.3:

- Jaffe 2005 → A (peer-reviewed PRD). Correct.
- Chernodub 2013 → A (peer-reviewed PRD). Correct.
- Wilson 2011 → S/A (replicated? Nature paper; DCE has been independently reproduced in optical-fiber analogue systems — borderline S). Either is defensible; A is conservative.
- White 2026 → A as a bibliographic object, but the audit correctly treats it as **off-topic** for the claim, which is the right move — it does not get evidentiary weight on the energy-extraction claim regardless of journal tier.
- Pinto patents → E-ish (patents are not peer-reviewed primary literature; they are intent-of-claim documents). The audit treats them as negative evidence about the practical track record, not as positive theory support, which is appropriate for a patent.

No tier inflation flagged.

## My independent verdict on the audit (based on source fidelity alone)

Every cited source says what the audit says it says, with the strongest finding being the verified mismatch between the PRR 2026 paper's actual content (hydrogenic-orbital isospectral mapping in an acoustic-dispersion model) and Casimir Inc.'s use of it as a theoretical foundation for vacuum-energy harvesting. The audit's representation of the cited literature is faithful and, where it makes an OOM estimate beyond the abstract (Wilson 2011 per-mode rate), it correctly flags the estimate as an OOM. No paraphrase overreaches; no equation is attributed where the source has none; no caveats are stripped that would change the inference.

Two minor accessibility gaps remain: (i) full text of PRR 8, 013264 was paywalled (APS 403), so I confirmed it is off-topic for energy extraction by abstract and DOAJ summary only; (ii) the Wilson 2011 per-mode photon-rate anchor used in §3 was not extracted from the abstract — the audit's own footnote acknowledges this is an OOM derivation. Neither gap changes the verdict.

## Final verdict

**all sources accurately represented**
