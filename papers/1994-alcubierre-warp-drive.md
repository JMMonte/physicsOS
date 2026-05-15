---
title: "The warp drive: hyper-fast travel within general relativity"
authors: Alcubierre
year: 1994
venue: "Class. Quantum Grav. 11, L73-L77"
arxiv: gr-qc/0009013
doi: 10.1088/0264-9381/11/5/001
tier: A
read_depth: skim
read_on: 2026-05-15
keywords: [warp-drive, general-relativity, exotic-matter, ftl]
related_claims: [claims/controllable-ftl-engineering-problem.md]
related_audits: [audits/2026-05-15-ftl-causal-loop-kinematics/]
---

# The warp drive: hyper-fast travel within general relativity

## One-line summary

Alcubierre constructs an exact GR metric with apparent arbitrarily large travel speed relative to distant observers, but the construction requires exotic stress-energy.

## What it actually shows

- The paper is a proof of existence for a spacetime geometry, not an engineering mechanism for producing that geometry.
- The spaceship remains locally timelike inside a bubble; the "FTL" is global/asymptotic, from contraction of space in front and expansion behind.
- The metric is chosen first; the stress-energy tensor is then inferred from Einstein's equations.
- The inferred stress-energy violates ordinary energy-condition expectations. The paper explicitly flags the need for exotic matter.
- The paper does not solve formation, acceleration, steering, stopping, or stability of the bubble.

## Methods (briefly)

ADM-style construction of a spacetime metric containing a moving bubble with a nearly flat interior, followed by inspection of the associated stress-energy.

## Key equations / results

The line element is the Alcubierre warp metric, schematically

```text
ds^2 = -dt^2 + [dx - v_s(t) f(r_s) dt]^2 + dy^2 + dz^2
```

with bubble velocity `v_s(t)` and shape function `f(r_s)`. The relevant result for this claim is qualitative: the geometry permits global apparent speed greater than `c` while demanding exotic matter.

## Assumptions and regime of validity

- Classical general relativity.
- Prescribed metric; no realistic matter model or creation process.
- Asymptotically flat exterior.
- No quantum-gravity completion.

## Caveats / open issues

The paper is often cited as "FTL is allowed by GR." That is too loose. It shows a metric ansatz is algebraically allowed by Einstein's equations if one accepts the required stress-energy. It does not show that known matter can source it.

## How it informs the FTL engineering claim

This is the canonical steelman source. It supports the weaker statement "GR admits formal superluminal-looking geometries." It does not support the stronger claim that FTL is currently an engineering problem under known matter physics.

## Citations to chase

- Olum 1998, arXiv:gr-qc/9805003.
- Pfenning and Ford 1997, "The unphysical nature of warp drive."
- Santiago, Schuster, and Visser 2022, arXiv:2105.03079.

## Changelog

- 2026-05-15: created. Read depth: skim.
