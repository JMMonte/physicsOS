# Casimir Inc.'s "Quantum Energy Chip"

A worked example of the physicsOS protocol applied to a real, current claim. The investigation produced one claim file, two independent audits, six paper notes, and an evidence-weighted confidence score — all reproducible from this repository.

| Field | Value |
|---|---|
| **Claim** | A 5 mm × 5 mm semiconductor chip outputs 1.5 V × 25 μA continuously by "harvesting quantum vacuum energy" via "engineered Casimir cavities." |
| **Source** | Casimir, Inc. press release, 2026-05-12 (BusinessWire), announcing a $12M oversubscribed seed round. |
| **Founder** | Dr. Harold "Sonny" White (ex-NASA Eagleworks; EmDrive, "Q-thrusters"). |
| **Status** | `refuted` |
| **Confidence** | **0.10** (rubric-capped via [AGENTS.md §3.3](../AGENTS.md#33-confidence-rubric)) |
| **Tracked at** | [`claims/casimir-quantum-energy-chip-feasibility.md`](../claims/casimir-quantum-energy-chip-feasibility.md) |

---

## Why this example is worth reading

The claim is a near-textbook "extraordinary claims" case: a static, ambient-temperature, passive solid-state device delivers continuous electrical power indefinitely, with no external energy input, on the basis of an exotic-sounding mechanism. The protocol's job is not to dismiss it by category but to produce an auditable trail through the actual physics, the actual literature, and an actual computational ledger.

That trail is what this example is.

## How the protocol unfolded

### Step 1 — Restate precisely

The press release's marketing language is converted to a falsifiable physics statement at the top of the [claim file](../claims/casimir-quantum-energy-chip-feasibility.md#precise-statement): chip area 5×5 mm, output 1.5 V × 25 μA, areal power **1.5 W/m²**, lifetime "no degradation, no replacement cycle" → operationally indefinite, passive, ambient.

### Step 2 — Survey the literature

Six [paper notes](../papers/) were created:

- [**Casimir Inc. press release**](../papers/2026-businesswire-casimir-press-release.md) — primary source, Tier F (marketing).
- [**White et al. 2026, *Phys. Rev. Research***](../papers/2026-white-emergent-quantization-dynamic-vacuum.md) — the company's cited theoretical foundation. The PRR PDF is Cloudflare-gated; content reconstructed via the 2015 NTRS precursor and four independent technical reviews (including Hossenfelder's). The paper is a Madelung-fluid isospectral mapping between a classical acoustic medium and the hydrogenic Coulomb problem. It contains **zero discussion of Casimir cavities, energy extraction, or any device claim**.
- [**Jaffe 2005, *Phys. Rev. D***](../papers/2005-jaffe-casimir-without-vacuum-energy.md) — shows the Casimir effect is derivable as a QED matter-matter force without invoking vacuum energy at all. The popular "harvest the vacuum" framing is a category error the field has moved past.
- [**Chernodub 2013, *Phys. Rev. D***](../papers/2013-chernodub-rotating-casimir-perpetual-motion.md) — the closest serious proposal of "Casimir perpetual motion." Author is explicit that it produces no usable work.
- [**Pinto patents 1999–2003**](../papers/1999-pinto-casimir-engine-patents.md) — the only theoretical loophole (modulated boundary properties to make the cycle non-conservative). 27 years of patents, zero commercialization.
- [**Moddel & Dmitriyeva 2019, *Atoms***](../papers/2019-moddel-dmitriyeva-zpe-extraction.md) — the authoritative peer-reviewed survey. Verdict on Pinto-class extraction: "cannot succeed because the Casimir force is conservative."

### Step 3 — Audit 1: energy budget

[`audits/2026-05-13-casimir-energy-budget/`](../audits/2026-05-13-casimir-energy-budget/) — verdict `contradicted`. Establishes the **categorical obstructions**:

- **Static reservoir.** Between perfect conductors at zero temperature, the available Casimir energy per unit area is `|E|/A = π² ℏ c / (720 d³)`. At d=10 nm this is 4.3 × 10⁻⁴ J/m² — the reservoir drains in **289 microseconds** at the claimed 1.5 W/m². For 10-year operation, the gap would need to be ~10⁻¹² m, three orders of magnitude below the proton radius.
- **Dynamical Casimir effect.** Closing the gap to Wilson et al.'s 2011 demonstration requires boundary velocities `v/c ≳ 2 × 10³` — kinematically impossible.
- **Second law.** A passive device in equilibrium with a single-temperature bath delivers zero net work, by definition.

Reproducible end-to-end:

```bash
.venv/bin/python audits/2026-05-13-casimir-energy-budget/audit.py
```

### Step 4 — Audit 2: steelman the loophole

The first audit's bounds assume the cavity is static. The only theoretical escape is a Pinto-style modulated-boundary engine: cycle a plate property (refractive index, conductivity) during the cycle to make the Casimir force non-conservative, then collect the imbalance. [`audits/2026-05-13-casimir-steelman-energy-ledger/`](../audits/2026-05-13-casimir-steelman-energy-ledger/) — verdict `contradicted` — steelmans this with charitable parameters and computes the **quantitative ledger**:

| Quantity | Value |
|---|---|
| Extracted Casimir power (d=100 nm, f=1 GHz, ΔR=1) | 433 W/m² |
| Drive cost — Drude carrier swing | 3.2 × 10¹⁹ W/m² |
| Drive cost — InSb dielectric loss | 1.4 × 10¹¹ W/m² |
| Drive cost — VO₂ latent heat | 2.0 × 10¹⁰ W/m² |
| **Net (best case)** | **−2.0 × 10¹⁰ W/m²** |
| Claim | +1.5 W/m² |

Across a 45-point sweep over (gap, frequency, modulation depth), **0 / 45 combinations yield positive net power**. The smallest of the three drive-cost floors exceeds extracted Casimir work by **4.5 × 10⁷×**.

The Drude requirement alone implies an E-field of 2 × 10¹⁰ V/m across the modulator — roughly 7000× the dielectric breakdown of air. The chip would arc and vaporize before it could pump.

### Step 5 — Compute the confidence

The [claim's evidence ledger](../claims/casimir-quantum-energy-chip-feasibility.md#evidence-ledger) has eight rows (press release + five paper notes + two audits). Under the [§3.3 rubric](../AGENTS.md#33-confidence-rubric):

```
s_raw  = (sum of w·sign) / (sum of w)  =  −4.25 / 6.00  =  −0.708
s_base = (−0.708 + 1) / 2              =  0.146

audit 1 carries veto-R (categorical: 2nd law + v<c)
→ confidence = min(0.146, 0.10) = 0.10
```

The veto is what does the load-bearing work. Audit 1's findings are categorical — not "the numbers don't match" but "this configuration is forbidden in principle." The rubric is designed so a single such finding caps confidence regardless of how many neutral citations exist elsewhere. Audit 2's 10-orders-of-magnitude ledger failure does *not* add a second veto (the failure is quantitative, not in-principle), but it pushes `s_base` down anyway and would refute the claim by itself even if no veto had been triggered.

## What would change the verdict

The audit READMEs both list explicit "how the company can rebut" sections. In summary, Casimir Inc. would need to publish — peer-reviewed, with independent replication — **all of**:

1. The cavity geometry, mode structure, and boundary materials.
2. A complete energy ledger: every input (modulation drive, biases, optical pump, thermal gradient) vs delivered electrical output, with uncertainties.
3. A falsifiable scaling prediction (output vs gap, frequency, area, temperature) consistent with their stated mechanism.

Until that exists, the claim's confidence stays at 0.10.

## What this example demonstrates about the protocol

- **Speed of refutation.** From "this press release dropped" to a verdict-bearing audit took one focused session, all artifacts logged.
- **Composability.** A second-pass audit added new evidence without invalidating the first; the rubric handled the combination mechanically.
- **Honest failure modes.** When arXiv rate-limited the fetcher and when the PRR PDF was Cloudflare-gated, those were logged as constraints rather than hidden. The fetcher was hardened (see [AGENTS.md §8.1](../AGENTS.md#81-arxiv)); the PRR content was reconstructed via the 2015 NTRS precursor with the reconstruction process documented in the paper note.
- **The audit produced reusable infrastructure.** The hardened arXiv fetcher, the pinned scientific Python environment, the formalized confidence rubric — all came out of running this one example to completion.

## Reproducing this example

From a fresh clone:

```bash
git clone https://github.com/JMMonte/physicsOS
cd physicsOS
scripts/bootstrap.sh
.venv/bin/python audits/2026-05-13-casimir-energy-budget/audit.py
.venv/bin/python audits/2026-05-13-casimir-steelman-energy-ledger/audit.py
```

Both audits should print intermediate values and conclude `CONTRADICTED`. The claim's confidence is recomputable directly from the ledger using the formula above.
