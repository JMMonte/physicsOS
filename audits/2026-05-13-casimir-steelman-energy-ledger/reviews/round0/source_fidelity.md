# Source-fidelity review — 2026-05-13-casimir-steelman-energy-ledger

Reviewer: source-fidelity subagent, fresh context. Read only the audit
README, audit.py, AGENTS.md, CLAUDE.md, and the paper-notes the audit
links. Did not read other reviewers' files.

## Sources checked

| # | Source (as cited by audit) | Path / DOI | Accessible? | Method of verification |
|---|---|---|---|---|
| 1 | Moddel & Dmitriyeva 2019, *Atoms* 7, 51 | `papers/2019-moddel-dmitriyeva-zpe-extraction.md` ; DOI 10.3390/atoms7020051 ; arXiv 0910.5893 | Y (arXiv preprint PDF; MDPI HTML blocked 403; APS-style abstract via `scripts/fetch_arxiv.sh`) | Fetched arXiv preprint PDF, ran pdftotext, searched for every quoted phrase. The arXiv-deposited version is the published-equivalent v3 (per paper-note frontmatter). |
| 2 | White et al. 2026, *Phys. Rev. Research* 8, 013264 | `papers/2026-white-emergent-quantization-dynamic-vacuum.md` ; DOI 10.1103/l8y7-r3rm | **N** (APS Cloudflare 403; same gap the paper-note itself documents) | Attempted direct fetch of journal abstract page and the journals.aps.org abstract URL; both returned 403. Verified the closely related 2015 NTRS precursor (DOI 10.4236/jmp.2015.69136) via SciRP page — that *is* accessible and contains no energy-extraction discussion. |
| 3 | Casimir 1948, KNAW 51, 793 | only the parallel-plate force formula | Not separately fetched | Formula is textbook canonical (e.g., Milonni, *The Quantum Vacuum*, ch. 7); used only as the Casimir energy/pressure functional form. No fidelity issue. |
| 4 | Pinto 1999–2003 patents | `papers/1999-pinto-casimir-engine-patents.md` | Not separately fetched | Paper-note is correctly tagged tier-F; not load-bearing. The actual mechanism description (modulated-boundary cycle) is re-described in Moddel-D §2.2, which I read (lines 301–347 of preprint). Verified consistent. |
| 5 | Scandurra 2001 (no power from cyclic Casimir motion) | mentioned only as cited in Moddel-D | Not separately fetched | Audit and note correctly attribute via Moddel-D ref [34]. Moddel-D §2.2 (lines 341–345 of preprint) summarises Scandurra's result; audit's use of it is consistent with that summary. |
| 6 | Berthier et al. 2008 (VO₂ ΔH ≈ 45 J/g) | cited inline only in audit README | Not directly fetched | Cross-checked via Bowman et al. 2020 PCCP (see #7). |
| 7 | Bowman et al. 2020 PCCP (VO₂ enthalpy aggregation) | DOI 10.1039/D0CP01929A | Y (RSC abstract page) | Fetched abstract. The paper reports a *DFT-calculated* enthalpy difference ΔE₀ = −44.2 meV/formula-unit, "similar to the experimental value." Converting: 44.2 meV × N_A / (83 g/mol) ≈ 51 J/g — in the same neighbourhood as the audit's 45 J/g (Berthier 2008 experimental). Minor mismatch: see Fidelity issues. |
| 8 | Sci Rep 13 (2023), DOI 10.1038/s41598-023-45475-8 — InSb tan δ ≈ 0.014 | cited in audit README §"Material data" and audit.py line 226 | Y (HTML accessible) | Fetched Nature article HTML, grepped for any "tan delta", "loss tangent", "0.014" — paper does not state a loss-tangent value. It uses a Drude model with ε_∞ = 15.68 and γ = π×10¹¹ rad/s. The audit's quoted 0.014 is not in this source. See Fidelity issues #1. |
| 9 | Iannuzzi et al. PRL 2003 ; Chen et al. PRA 2007 (carrier-density swing required for O(1) reflectivity contrast) | audit.py comments lines 222–223 | Not in `papers/`; not directly fetched | Load-bearing-ish: justifies the Drude-floor methodology. Should have a paper-note. See Fidelity issues #4. |
| 10 | InSb breakdown field ~10⁶ V/m ; air breakdown ~3×10⁶ V/m | audit.py lines 273–275 | Not cited | Used as sanity comparison ("would arc / vaporize") — uncited but appears in the README at line 110 as a load-bearing comparison ("7000× the breakdown field of air"). See Fidelity issues #2. |
| 11 | InSb effective mass m_eff ≈ 0.014 m_e | audit.py line 239 ; README "Material data" | Standard value | Sci Rep 2023 paper uses 0.015 m_e in the Drude denominator — close enough; "standard handbook" range is 0.013–0.015. Minor (within source noise). |
| 12 | InSb static permittivity ε_r ≈ 17 | README "Material data" ; audit.py line 225 | Standard | Sci Rep 2023 uses ε_∞ = 15.68 (high-frequency); the audit's 17 is the *static* value, also standard. Distinct quantities — audit could be clearer about which, but the value used in the loss-tangent formula is the *static* one which is appropriate for ε(ω→low). No issue. |

## Fidelity issues found

### #1 — InSb tan δ = 0.014 attribution to Sci Rep 2023 is not a direct quote from that paper

**Audit/note claim** (audit README, "Material data"):
> "InSb static permittivity ε_r ≈ 17 (standard handbook); THz loss tangent
> tan δ ≈ 0.014 ([Sci Rep 13, 45475-8, 2023](https://doi.org/10.1038/s41598-023-45475-8))"

**Audit.py line 226**:
```python
tan_delta_InSb = 0.014     # low-loss end of InSb THz range (Sci Rep 2023)
```

**What the source actually says**: The Sci Rep 2023 paper (Yaqoob et al.,
"Thermally tunable electromagnetic surface waves supported by graphene
loaded indium antimonide (InSb) interface") models InSb with a Drude
permittivity using ε_∞ = 15.68 and damping constant γ = π × 10¹¹ rad/s. It
does **not** state a numerical loss tangent of 0.014 (or any explicit
tan δ value) for InSb.

**Why this matters, but not catastrophically**: The 0.014 figure is in the
right ballpark for low-loss InSb at THz when computed from Drude parameters
in many sources, but as cited it overreaches what *this specific paper*
prints. The audit's substantive conclusion is robust: the dielectric-loss
floor (P_drive,diel) is set by the field amplitude (which is dictated by
the Drude carrier-swing requirement), and varying tan δ over the full
plausible range 0.005–0.05 changes that floor by less than an order of
magnitude — still leaves a >10⁸ deficit vs the claim. So the
load-bearing-ness of the *specific* 0.014 is low. The citation should
either be widened (e.g., add the canonical Palik handbook for InSb
THz-range dielectric data) or weakened (the Sci Rep 2023 paper provides
the *Drude parameters* from which tan δ can be derived, not the tan δ
itself).

### #2 — InSb breakdown field ~10⁶ V/m and air breakdown ~3×10⁶ V/m: uncited

**Audit README claim** ("Drive-cost lower bounds (A)"):
> "stored at E-field amplitude **2×10¹⁰ V/m** (about 7000× the breakdown
> field of air and 2×10⁴× the breakdown field of bulk InSb)."

**Audit.py** lines 273–275 print the same comparison.

**Source check**: No reference in the paper-notes or audit for either
breakdown number. Air-breakdown 3×10⁶ V/m is canonical (Paschen curve at
1 atm, mm gap); bulk-InSb breakdown ~10⁶ V/m is less obviously canonical
— literature values for InSb vary by 10× depending on doping, geometry,
and thin-film vs bulk. The comparison is rhetorically strong but is the
*only* unsourced quantitative comparison flagged in the README's "headline
ledger" prose. **Recommendation**: cite a handbook or measurement (e.g.,
Sze, *Physics of Semiconductor Devices*, ch. 2; or a specific paper on
InSb breakdown). The conclusion ("modulator would arc / vaporize") is
unchanged by reasonable revisions of these numbers but the discipline
should be tightened.

### #3 — Bowman et al. 2020 PCCP cited as "aggregated values" but is a DFT paper

**Audit README claim** ("Material data"):
> "VO₂ MIT enthalpy ΔH ≈ 45 J/g (Berthier et al. 2008; aggregated values in
> [Bowman et al. 2020, PCCP](https://doi.org/10.1039/D0CP01929A))"

**What Bowman 2020 actually says** (abstract, verbatim from RSC page):
> "We compare various calculation methods to determine the electronic
> structures and energy differences of the phases of VO2. … An enthalpy
> difference of ΔE₀ = −44.2 meV per formula unit, similar to the
> experimental value, is obtained if the randomly oriented spins of the
> paramagnetic rutile phase are treated by a non-collinear spin density
> functional calculation."

**Issue**: Bowman 2020 is primarily a DFT paper, not an aggregator of
experimental ΔH values for VO₂. Its result ΔE₀ = −44.2 meV/f.u. ≈ 51 J/g
(by my conversion using formula mass 83 g/mol) is *close to* the audit's
45 J/g but is itself a DFT *calculation* claimed to be "similar to the
experimental value" without giving the experimental value in the abstract.
The note "aggregated values" overstates what Bowman provides.

**Why this matters, but not catastrophically**: the audit's ΔH = 45 J/g
falls within the experimental scatter of ~45–60 J/g commonly reported for
bulk VO₂ MIT (Berthier 1968, Mlyuka 2007, and others). The VO₂ floor at
45 J/g is 2×10¹⁰ W/m²; at 51 J/g it would be 2.3×10¹⁰ — same order, same
conclusion. **Recommendation**: either replace "aggregated values in
Bowman" with a citation that actually aggregates (a review of VO₂ MIT
thermodynamics), or recast as "consistent with DFT estimate in Bowman 2020
(≈51 J/g per formula-unit conversion)".

### #4 — Iannuzzi PRL 2003 and Chen PRA 2007 cited in audit.py but no paper-notes

**Audit.py** lines 222–223:
```python
# (Pinto/Iannuzzi/Esquivel-Sirvent et al. all
# require carrier-density swings of this order to get O(1) reflectivity
# contrast; see Iannuzzi et al. PRL 2003 and Chen et al. PRA 2007.)
```

**Issue**: These citations underwrite the methodological claim that the
"Drude floor" Δn required for full reflectivity swing is in fact of the
magnitude the audit computes. No `papers/` note exists for either source.
Per AGENTS.md §1.4, "every paper you actually read (more than the
abstract) gets a file in `papers/`" — and per §4, "every numeric result …
should be followed by either a paper link, an audit link, or the marker
`[UNVERIFIED]`." The Drude-floor methodology is internally consistent
(it derives the *minimum* carrier density to make ω_p ≥ ω_cavity), so the
substantive claim does not collapse if these sources are mis-cited — but
the citations as printed are not verifiable.

**Recommendation**: either add paper notes for Iannuzzi 2003 and Chen 2007
(both arXiv-accessible) confirming the Δn requirement, or recast the audit
comment to make clear that the Δn is derived from first principles in the
audit and the named papers are only secondary corroboration.

### #5 — White et al. 2026 PRR inaccessible; load-bearing negative claim relies on indirect verification

**Audit README claim** ("Sources used in the audit"):
> "White et al. 2026, PRR 8, 013264 — the press release's cited theory
> paper. Does not discuss energy extraction (independently confirmed by
> all secondary commentary, including Hossenfelder and the substack
> technical review)."

**What I could verify**: APS journal landing-page and abstract page both
return HTTP 403 (Cloudflare). The paper-note itself (`papers/2026-white-…`)
explicitly documents this gap and reconstructs the paper's content from
(a) the 2015 NTRS/SciRP precursor (DOI 10.4236/jmp.2015.69136), which I
*was* able to fetch — confirmed it contains no energy-extraction section
and has the 1/r⁴ density profile and COMSOL eigenfrequency analysis the
note describes, and (b) multiple independent technical commentaries.

**Issue**: This is a documented gap, not a misrepresentation. The audit's
negative claim ("does not discuss energy extraction") cannot be checked
against the source directly. The paper-note's tier-A assignment for the
mathematical content is appropriate; its tier-Z down-grade for the
"engineered Casimir cavities produce usable electrical energy"
interpretation is appropriate. **The only concrete fidelity risk is that
the published 2026 paper diverges from the 2015 precursor in ways the
secondary commentaries did not capture.** This is unlikely (four
independent reviews converging) but cannot be ruled out without journal
access. The paper-note flags this in its changelog and provenance section
— honest discipline.

### #6 — Audit-README quote attributed to Moddel-D Conclusion §3 — verbatim match confirmed

**Audit README quote**:
> "Any attempt to obtain power by cycling Casimir cavity spacing the
> energy gained in one part of the cycle must be paid back in another."
> — Moddel & Dmitriyeva, *Atoms* 7, 51 (2019), Conclusion §3.

**Moddel-D arXiv 0910.5893, §3 Conclusions** (preprint lines 769–771):
> "In any attempt to obtain power by cycling Casimir cavity spacing the
> energy gained in one part of the cycle must be paid back in another."

**Verdict**: verbatim match (audit drops the introductory "In"). ✓

### #7 — Audit-README "page 8" attribution — verbatim match confirmed

**Audit README claim** ("Sources used in the audit"):
> "Most directly load-bearing for verdict: page 8 ('any attempt to obtain
> net power in a cyclic fashion from changing the spacing of Casimir
> cavity plates cannot work')."

**Moddel-D preprint line 347** (page 8 → 9 boundary):
> "Generalizing from the conservative nature of the Casimir force, it
> appears that any attempt to obtain net power in a cyclic fashion from
> changing the spacing of Casimir cavity plates cannot work."

**Verdict**: verbatim match. The page-8 attribution is accurate (sentence
spans pages 8–9 in the arXiv-formatted preprint). ✓

## Tier assignments to revisit

- **Moddel & Dmitriyeva 2019 (tier A)** — paper-note's tier-A is well-
  justified: peer-reviewed Atoms (MDPI), open-access, methodologically
  conservative. The note also correctly flags the COI (Jovion Corp stock),
  which cuts *toward* the audit's direction (negative finding from a
  sympathetic source is conservatively stronger). Keep tier A.
- **White et al. 2026 PRR (split tier A / tier Z)** — the paper-note's
  split assignment is appropriate and conservative. Tier A for the
  mathematical isospectrality result; tier Z for the
  energy-extraction interpretation that the press release pins on it.
  Keep as-is.
- **Pinto 1999–2003 patents (tier F)** — appropriate; patents are not
  peer-reviewed and the note is used only as prior-art pointer. Keep.
- **Bowman 2020 PCCP** — implicitly tier A in audit citation, but the
  paper's actual contribution is DFT, not aggregation. Tier appropriate
  *if* used for "DFT confirms experimental ΔH"; the audit's framing
  ("aggregated values") slightly overreaches. No down-grade needed; just
  recast the citation language.
- **Sci Rep 2023 (Yaqoob et al.)** — peer-reviewed Sci Rep, tier ≈ A
  for the Drude model parameters it actually publishes. The audit's use
  of it as the source for "tan δ = 0.014" is *not* a direct quote from
  the paper — see Fidelity issue #1. The tier assignment is fine; the
  citation is what's loose.

## Verdict

**Minor mismatches.** The audit's load-bearing peer-reviewed citation
(Moddel & Dmitriyeva 2019) is verified verbatim — both the Conclusion §3
quote and the page-8 "any attempt to obtain net power in a cyclic fashion
…" quote match the source exactly, the DARPA grant disclosure
(N66001-06-1-2026) matches, the abstract reproduces, and Moddel-D's §2.2
description of the Pinto cycle is the basis for the audit's steelman
formulation. The audit's central energetic argument — Casimir force is
conservative; any cyclic extraction requires a non-conservative
modulation; that modulation pays at least the Casimir energy back —
faithfully reproduces Moddel-D's case and the in-paper attribution to
Scandurra (2001), with Pinto's own subsequent acknowledgment (Pinto 2014).
The verdict (`contradicted`) is supported by the source at face value.

The flagged issues are *citation discipline* rather than substantive
misrepresentation:

1. The InSb tan δ = 0.014 number is cited to a Sci Rep 2023 paper that
   provides Drude parameters but not that specific value directly.
2. The InSb / air breakdown-field comparisons in the README's "drive cost"
   prose are uncited.
3. The "Bowman 2020 aggregated values" framing slightly overstates a paper
   that is principally a DFT calculation.
4. The Iannuzzi 2003 and Chen 2007 references in audit.py comments are not
   backed by paper-notes (AGENTS.md §1.4 expects one).
5. The White et al. 2026 PRR paper is inaccessible; the audit's negative
   claim ("does not discuss energy extraction") rests on multiple
   independent secondary reviews plus the 2015 precursor, which I verified
   does not discuss energy extraction. Honest gap, not a misrepresentation.

None of these issues changes the audit's verdict. The substantive
conclusion — that the steelmanned Pinto cycle has a drive-cost lower
bound that exceeds the extracted Casimir power by ≥10⁷ across the parameter
sweep — is robust to varying tan δ, breakdown-field, and ΔH by factors of
10 each. The audit is fundamentally honest about what its sources
establish.
