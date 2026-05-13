---
name: Conventions
description: Default unit systems, metric signature, and Fourier conventions used across audits and notes in this project.
type: project
---

# Conventions

Unless an audit explicitly overrides, assume:

- **Units**: SI for engineering / lab physics; natural units ($\hbar = c = 1$) for high-energy / field theory; Planck units when discussing quantum gravity. Always label which.
- **Metric signature**: $(-,+,+,+)$ ("mostly plus", MTW / Wald convention) unless a cited paper uses the opposite — in which case note the convention at the top of the audit.
- **Fourier transform**: $\tilde f(k) = \int f(x) e^{-ikx}\,dx$, with $2\pi$ in the inverse: $f(x) = \frac{1}{2\pi}\int \tilde f(k) e^{ikx}\,dk$.
- **Indices**: Greek $\mu,\nu,\dots$ for spacetime (0–3), Latin $i,j,\dots$ for spatial (1–3), Einstein summation throughout.
- **Constants**: pull from `scipy.constants` or `astropy.constants` — do not type literals.

When a source uses a different convention, **convert at the boundary** (in the paper note or audit README), not silently in the middle of a derivation.

**Why:** Half of all physics errors are convention errors. Pinning defaults here so we catch mismatches early.

**How to apply:** Open every audit's README with a one-line "Conventions: SI, mostly-plus, $f(\omega) = \int f(t)e^{-i\omega t} dt$" header. If a paper uses different conventions, transcribe the converted form in your note, not the original.
