# Source fidelity review — 2026-05-13-casimir-energy-budget

Reviewer role: verify that every source cited by the audit and its paper-notes
says what the audit claims it says. Sources fetched fresh where accessible.

## Sources checked

| Source | Paper-note | Accessible? | Method of verification |
|---|---|---|---|
| Jaffe 2005, *PRD* 72, 021301(R) (arXiv hep-th/0503158) | `papers/2005-jaffe-casimir-without-vacuum-energy.md` | Y (abstract) | `scripts/fetch_arxiv.sh hep-th/0503158` |
| Chernodub 2013, *PRD* 87, 025021 (arXiv 1207.3052) | `papers/2013-chernodub-rotating-casimir-perpetual-motion.md` | Y (abstract) | `scripts/fetch_arxiv.sh 1207.3052` |
| Pinto patents US 6,477,028 / 6,665,167 / 6,593,566 / 6,650,527 | `papers/1999-pinto-casimir-engine-patents.md` | Partial (Y for 6,477,028 and 6,665,167 via Google Patents; 6,593,566 / 6,650,527 not individually verified) | WebFetch on `patents.google.com` |
| White et al. 2026, *PRR* 8, 013264 (DOI 10.1103/l8y7-r3rm) | `papers/2026-white-emergent-quantization-dynamic-vacuum.md` | N (PRR PDF Cloudflare-gated — paper-note already documents the gap and reconstructs content from the 2015 NTRS precursor + four independent technical commentaries) | None this session — gap inherited from paper-note's own provenance section |
| Wilson et al. 2011, *Nature* 479, 376 (arXiv 1105.4714) | Cited only in `audits/.../README.md` §3 (no paper-note exists) | Y (arXiv preprint full text fetched and read) | WebFetch on `arxiv.org/pdf/1105.4714v1` (`pdftotext` to extract) |
| Casimir, Inc. press release 2026-05-12 | `papers/2026-businesswire-casimir-press-release.md` | N (BusinessWire HTTP/2 RST on direct fetch, as the paper-note already records) | None this session — paper-note explicitly relied on aggregator summaries |
| Constants σ_SB, ℏ, c (CODATA, used in §4) | implicit | Y (scipy.constants; sanity check `σT⁴` at 300 K = 459.30 W/m²) | local Python check |

## Fidelity issues found

### Wilson et al. 2011 — missing paper-note, and one numeric paraphrase that overreaches the source

**Issue A (logging discipline).** The audit's §3 (Dynamical Casimir effect bound) leans heavily on
Wilson et al. 2011, *Nature* 479, 376 (arXiv 1105.4714), and uses a specific photon-flux
number (`~10⁵ photons/s`, encoded as `wilson_flux = 1e5` at `audit.py:114`) and a specific
frequency (`5 GHz`, `omega = 2*pi*5e9` at `audit.py:110`). Per AGENTS.md §1.4 ("Every paper
you actually read … gets a file in `papers/`"), this paper should have a note in `papers/`.
It does not. The audit therefore cites a numeric claim with no logged source artifact.

**Issue B (overreach).** The audit README §3 states:

> "Wilson et al. (2011, *Nature* 479, 376) experimentally demonstrated DCE in a
> superconducting circuit at ~5 GHz, producing roughly 10⁵ photons/s"

The Wilson 2011 preprint (which I fetched and read in full) does **not** quote a "10⁵ photons/s"
production rate. What the paper actually reports is a *power per unit bandwidth* — quoting
the paper directly: "the produced photons roughly double the noise level, suggesting a
power per unit bandwidth of a few Kelvin … This implies an enhancement of the photon
production rate by a factor of 1000–2000, consistent with what we observe." The 10⁵
photons/s figure is plausible as an order-of-magnitude estimate (and `audit.py:114`'s
comment `# OOM, Wilson et al. 2011` correctly flags it as such), but the README's
unhedged paraphrase ("producing roughly 10⁵ photons/s") presents this as a measurement
quoted in Wilson, which it is not. Recommended fix: rewrite as "Wilson et al. obtain a
DCE photon rate of order 10⁵ s⁻¹ in our band of interest, inferred OOM from the reported
power per unit bandwidth — see `audit.py:114` for the figure used."

**Issue C (frequency).** The audit's "5 GHz cavity" is approximately right but slightly
imprecise. Wilson's *drive* frequency is ~11 GHz; the *analysis* (photon-emission) band
is 4–6 GHz (`"the analysis band of 4-6 GHz"`, `"n = 0.008 at 5 GHz, the center of our
analysis band"`). The audit's choice of 5 GHz as the photon energy is therefore
defensible (center of the emission band), but the prose in README §3 conflates the two:
"DCE in a superconducting circuit at ~5 GHz" reads as a description of the device, when
it is actually the band center of the down-converted photons. Minor; does not change the
v/c argument.

**Issue D (kinematic claim — direction of inference is fine).** The audit's conclusion
("DCE rate scales as $(v/c)^2$ for slow boundaries") is supported by the paper, which
states explicitly: `Γ_DCE = (ω_d / 12π)(v_e/c_0)²`. The kinematic-impossibility argument
(`v/c ≳ 2 × 10³`) follows from the OOM photon-rate baseline. If Issue B is fixed by
acknowledging the OOM nature of the baseline, this conclusion still stands; if not, the
2 × 10³ figure has an order-of-magnitude uncertainty inherited from the unsourced 10⁵/s.

### Audit README §1 — direction of the proton-radius comparison is wrong

**Issue E (arithmetic / direction).** The README states:

> "To last **10 years**, the cavity would need $d \approx 9.7 \times 10^{-13}\,\mathrm{m}$
> — three orders of magnitude **below the proton radius**."

The proton charge radius is ≈ 0.84 × 10⁻¹⁵ m. Therefore
9.7 × 10⁻¹³ m / 0.84 × 10⁻¹⁵ m ≈ 1.16 × 10³ — the required gap is about three orders of
magnitude **above** the proton radius, not below. (`audit.py:104` correctly prints
`proton radius: ~0.84e-15 m for scale` without taking sides; the error is in the prose.)
The audit's actual point — "no physical meaning at that scale" — is unchanged either way,
because 1 pm gaps for parallel-plate Casimir are subatomic in *atomic-radius* terms
(Bohr radius ~5.3 × 10⁻¹¹ m); the formula assumes plate separations far larger than
plate-material microstructure scales. But the cited comparison to the proton radius
points the wrong way and should be corrected.

### Pinto patents — accurate but check the patent numbers

**Issue F (minor).** The paper-note lists four patent numbers (US 6,477,028 / 6,665,167 /
6,593,566 / 6,650,527). I verified 6,477,028 and 6,665,167 directly via Google Patents
and both are indeed Pinto and indeed describe boundary-property-modulated Casimir
engines, exactly as the note characterizes them. I did not independently verify 6,593,566
and 6,650,527 this session; the note's characterization of them is consistent with the
broader Pinto patent family, but a thorough review should pull each one. No content
discrepancy detected with what was verifiable.

### Jaffe 2005 — accurately represented

The paper-note's headline claim that "Casimir effects can be formulated and Casimir forces
can be computed without reference to zero point energies … The Casimir force (per unit
area) between parallel plates vanishes as α, the fine structure constant, goes to zero"
is **a near-verbatim restatement of the published abstract**, which I retrieved via
`fetch_arxiv.sh`. The note's interpretive framing ("the popular 'tap the vacuum' framing
is a category error") is a fair gloss, though slightly stronger than Jaffe's own
language; Jaffe writes that the standard derivation is one of several formulations.
Acceptable as a paraphrase given the audit's purpose. No fidelity issue.

### Chernodub 2013 — accurately represented

The paper-note's claim that "the device produces no useful work ('perpetuum mobile of the
fourth kind')" is **directly supported by the published abstract**:

> "The suggested 'zero-point driven' devices … correspond to a perpetuum mobile of a new,
> fourth kind: They do not produce any work despite the fact that their equilibrium
> (ground) state corresponds to a permanent rotation."

No fidelity issue.

### White et al. 2026 — paper-note already self-flags the access gap

The paper-note's own provenance section openly states that the PRR PDF is Cloudflare-gated
and that content was reconstructed from (1) the 2015 NTRS precursor paper White et al.,
*J. Mod. Phys.* 6, 1308 (2015), (2) four independent secondary commentaries, and (3) the
published abstract. This is honest disclosure; the limitation is acknowledged not buried.

The note's most load-bearing claim ("The paper contains no statement that could be read,
however charitably, as supporting energy extraction from the vacuum") is supported by
multiple independent reviewers being quoted to the same effect, including a sympathetic
source (e-catworld). As source-fidelity, this looks responsible. The audit's use is
limited and conservative: it cites White only to refute the marketing assertion that
PRR provides "the theoretical foundation" for the device, which is the same direction of
inference as the paper-note. **One caveat I cannot remove this session**: the PRR PDF
itself remains unread by anyone in this repo. If a future reviewer obtains it and
discovers an energy-extraction discussion that escaped the secondary reviewers, this
conclusion would need revisiting.

### BusinessWire press release — also self-flagged

The paper-note explicitly notes the direct fetch failed (HTTP/2 RST) and that the claim
list is recovered from four named aggregators. This is acceptable per AGENTS.md (the
press release is tier-F and pointer-only anyway), and the audit's use of the numbers is
limited to (1.5 V × 25 μA, 5 mm × 5 mm, "continuous"), which is the same set quoted by
every aggregator. No fidelity issue beyond the access gap the note already documents.

## Tier assignments to revisit

- **Jaffe 2005 (tier A)** — appropriate. PRD is a tier-A journal.
- **Chernodub 2013 (tier A)** — appropriate. PRD is a tier-A journal.
- **Pinto patents (tier F)** — appropriate. Patents are not peer-reviewed physics. The
  note's framing as "prior-art context only" is correct.
- **White et al. 2026 (tier A for the math, tier Z for the energy-extraction
  interpretation)** — the paper-note's split-tier treatment is unusual but defensible
  and well-documented: the published math gets A; the unstated-in-paper marketing claim
  gets Z. I would not flag this as too high, **provided** the audit only relies on the
  tier-A part (it does — it cites White only to deny the energy-extraction reading,
  which is what tier Z permits).
- **BusinessWire press release (tier F)** — appropriate.
- **Wilson 2011** — has no paper-note, so no recorded tier. If logged, it should be
  tier A (Nature is a tier-A journal; the result is a peer-reviewed experimental
  demonstration).

## Verdict

**Minor mismatches.** Every cited source that I could verify says broadly what the
paper-notes claim it says. The substantive issues are:

1. Wilson 2011 has no paper-note in `papers/` despite being load-bearing for §3 (Issue A).
2. The audit's "10⁵ photons/s" figure is an order-of-magnitude estimate the README
   presents as if it were a quoted measurement (Issue B).
3. The "three orders of magnitude below the proton radius" comparison in §1 points the
   wrong way; the gap is ~10³ × *larger* than the proton radius, not smaller (Issue E).

None of these change the audit's verdict. The reservoir bound, the conservativity
argument, and the second-law argument are independent of the Wilson-rate paraphrase and
the proton-radius slip. But the README needs three small corrections and one new paper
note for the audit to be a clean exemplar of the AGENTS.md citation discipline.
