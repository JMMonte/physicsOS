## Sources checked (path; accessible Y/N; method of verification)

| Audit source path | Accessible? | Method of verification |
|---|---:|---|
| `../../papers/2002-liberati-faster-than-c-signals-causality.md` | Y | Checked arXiv abstract and PDF for `gr-qc/0107091`; checked journal landing page for Annals of Physics 298 (2002) 167-185, DOI `10.1006/aphy.2002.6233`. |
| `../../papers/1998-olum-superluminal-negative-energies.md` | Y | Checked arXiv abstract and PDF for `gr-qc/9805003`; checked APS landing page for Phys. Rev. Lett. 81, 3567 (1998), DOI `10.1103/PhysRevLett.81.3567`. |

No additional sources were cited inline in the numbered methodology sections.

## Fidelity issues found (one entry per source with the problem)

### Liberati, Sonego, and Visser 2002

Audit claim: "for the caution that causality depends on the FTL propagation law, not just on the phrase 'faster than c.'"

Source check: accurate. The article's abstract says causality cannot be assessed generically without specifying tachyonic-propagation features, and its conclusion says causal paradoxes depend on tachyons lacking a fixed speed in a given reference frame. This is exactly the caution the audit attributes to the source.

No overreach found. Important nuance retained by the audit: Liberati et al. do not claim all FTL effects generate loops; they emphasize constrained cases such as Scharnhorst propagation can be benign.

### Olum 1998

Audit claim: "for the wider GR result that superluminal travel requires weak-energy-condition violation under Olum's definition."

Source check: mostly accurate, but slightly incomplete. Olum proves the result under his definition and an additional assumption: "assuming the generic condition." In the body, the theorem is stated for spacetimes satisfying Condition 1 and the generic condition on the relevant path, and concludes that they violate the WEC somewhere on that path.

This is a minor caveat omission, not a reversal. The audit's phrasing correctly restricts the claim to "under Olum's definition," but it should say "under Olum's definition and generic-condition assumption." The source also explicitly notes this does not make superluminal travel impossible in all senses, since quantum fields need not obey the WEC; the audit does not claim otherwise.

## Tier assignments to revisit

No tier downgrade indicated from source fidelity.

Both papers have journal-of-record publications in reputable peer-reviewed journals: Liberati/Sonego/Visser in Annals of Physics and Olum in Physical Review Letters. Under AGENTS.md section 1.3, tier A is appropriate if these are logged as peer-reviewed primary papers. The caveat on Olum affects wording, not source tier.

## My independent verdict on the audit (based on source fidelity alone)

The audit's use of Liberati/Sonego/Visser is faithful: the paper supports the methodological caution that "FTL" alone is not enough to decide causality; the propagation law matters.

The audit's use of Olum is directionally faithful but should include the generic-condition assumption whenever the theorem is summarized. Since Olum is used only for wider GR context, not as a load-bearing input to the flat-spacetime tachyonic-antitelephone calculation, this is not a substantive source misrepresentation.

## Final verdict

minor mismatches
