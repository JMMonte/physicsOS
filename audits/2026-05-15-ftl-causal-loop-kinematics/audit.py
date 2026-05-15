"""
Audit: unrestricted reciprocal faster-than-light signalling in special
relativity permits a causal loop.

Conventions:
  - Natural units, c = 1, distances in light-years, times in years.
  - Metric signature is irrelevant; only Lorentz transformations are used.
  - alpha = u/c is the FTL signal speed in the sender's rest frame.
  - beta = v/c is the relative speed between inertial observers.

Run from repo root:
    /usr/bin/python3 audits/2026-05-15-ftl-causal-loop-kinematics/audit.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

try:
    import sympy as sp
except ImportError:  # pragma: no cover - repo requirements include sympy
    sp = None

try:
    import pint
except ImportError:
    pint = None

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(exist_ok=True)

SEED = 0
np.random.seed(SEED)
print(f"[seed] {SEED}")
print(f"[python] {sys.version.split()[0]}")
print(f"[numpy] {np.__version__}")
print(f"[sympy] {getattr(sp, '__version__', 'missing')}")
print(f"[pint] {getattr(pint, '__version__', 'missing')}")
print()


def beta_threshold(alpha: float) -> float:
    """Minimum beta for a round-trip tachyonic-antitelephone loop."""
    return 2.0 * alpha / (1.0 + alpha * alpha)


def loop_times(alpha: float, beta: float, separation_ly: float = 1.0) -> dict[str, float]:
    """Compute the two-leg FTL exchange.

    Frame S:
      A is at x=0.
      B moves in +x with speed beta and starts at x=L when A emits.
      A sends to B at speed alpha.

    Frame S':
      B receives, immediately sends a reply at speed alpha back toward A.

    If the reply reaches A at t_A_receive < 0 in A's frame, the exchange is
    a closed causal loop relative to A's own emission event.
    """
    if not (alpha > 1.0):
        raise ValueError("alpha must exceed 1 for FTL")
    if not (0.0 <= beta < 1.0):
        raise ValueError("beta must be in [0, 1)")
    if beta >= alpha:
        raise ValueError("beta must be smaller than alpha for interception setup")

    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    L = separation_ly

    # First leg in S: x_signal = alpha t, x_B = L + beta t.
    t1 = L / (alpha - beta)
    x1 = alpha * t1

    # Lorentz transform first-leg reception event into B frame S'.
    t1p = gamma * (t1 - beta * x1)
    x1p = gamma * (x1 - beta * t1)

    # Reply in S': x_reply = x1p - alpha (t' - t1p);
    # A's worldline in S': x_A' = -beta t'. Solve for intersection.
    t2p = (x1p + alpha * t1p) / (alpha - beta)
    x2p = -beta * t2p

    # Back to S. Since event 2 lies on A's worldline, x=0 and t=t2p/gamma.
    t2 = gamma * (t2p + beta * x2p)
    x2 = gamma * (x2p + beta * t2p)

    return {
        "gamma": gamma,
        "t1_S_year": t1,
        "x1_S_ly": x1,
        "t1_B_year": t1p,
        "x1_B_ly": x1p,
        "t2_B_year": t2p,
        "x2_B_ly": x2p,
        "t2_S_year": t2,
        "x2_S_ly": x2,
    }


def main() -> int:
    print("== DIMENSIONAL CHECK ==")
    if pint is not None:
        ureg = pint.UnitRegistry()
        t_term = 1.0 * ureg.second
        vx_over_c2 = (
            (1.0 * ureg.meter / ureg.second)
            * (1.0 * ureg.meter)
            / (1.0 * ureg.meter / ureg.second) ** 2
        )
        print(f"  Lorentz t term:        {t_term:~P}")
        print(f"  Lorentz v*x/c^2 term:  {vx_over_c2.to(ureg.second):~P}")
        print("  t' = gamma (t - v x / c^2) is dimensionally consistent.")
    else:
        print("  pint unavailable; manual unit check: (m/s)*m/(m/s)^2 = s.")
    print()

    print("== SYMBOLIC DERIVATION ==")
    print("  First-leg intercept in S: t1 = L / (alpha - beta), x1 = alpha t1.")
    print("  Transform to B frame, send reply at speed alpha, solve intersection with A.")
    if sp is not None:
        a, b, L = sp.symbols("a b L", positive=True)
        gamma = 1 / sp.sqrt(1 - b**2)
        t1 = L / (a - b)
        x1 = a * t1
        t1p = gamma * (t1 - b * x1)
        x1p = gamma * (x1 - b * t1)
        t2p = sp.simplify((x1p + a * t1p) / (a - b))
        numerator = sp.factor(sp.together(t2p / (gamma * L)).as_numer_denom()[0])
        print(f"  t2'/(gamma L) numerator: {numerator}")
        print("  Loop condition t2' < 0 gives beta > 2 alpha / (1 + alpha^2).")
    else:
        print("  SymPy unavailable; using closed-form derivation in README.")
    print()

    print("== LIMITS ==")
    for alpha in [1.001, 1.01, 1.1, 2.0, 10.0, 1.0e6]:
        print(f"  alpha={alpha:>10.3g}  beta_min={beta_threshold(alpha):.12g}")
    print("  alpha -> 1+: beta_min -> 1, so nearly-luminal FTL needs nearly-luminal frames.")
    print("  alpha -> infinity: beta_min -> 0, so arbitrarily fast signalling makes loops easy.")
    print()

    print("== EXAMPLE LOOP ==")
    alpha = 2.0
    beta = 0.9
    vals = loop_times(alpha, beta, 1.0)
    print(f"  alpha={alpha:.3f}, beta={beta:.3f}, L=1 light-year")
    print(f"  threshold beta_min={beta_threshold(alpha):.6f}; selected beta exceeds threshold: {beta > beta_threshold(alpha)}")
    for key in [
        "gamma",
        "t1_S_year",
        "x1_S_ly",
        "t1_B_year",
        "x1_B_ly",
        "t2_B_year",
        "x2_B_ly",
        "t2_S_year",
        "x2_S_ly",
    ]:
        print(f"  {key:>12}: {vals[key]: .12g}")
    print("  A receives the reply before A sent the original message if t2_S_year < 0.")
    print()

    print("== GRID CONVERGENCE CHECK ==")
    print("  Brute-force scan for first beta producing t2_S < 0.")
    for n in [1_000, 10_000, 100_000]:
        betas = np.linspace(0.0, 0.999999, n)
        mask = np.array([loop_times(alpha, float(b), 1.0)["t2_S_year"] < 0 for b in betas])
        first = betas[np.argmax(mask)] if mask.any() else float("nan")
        err = abs(first - beta_threshold(alpha))
        print(f"  N={n:>6}: beta_first={first:.9f}, abs_error={err:.3e}")
    print()

    print("== VERDICT INPUT ==")
    print("  For any alpha > 1, the threshold beta_min = 2 alpha/(1+alpha^2) is < 1.")
    print("  Therefore a reciprocal, unrestricted FTL signalling rule plus ordinary")
    print("  Lorentz transformations permits a closed causal loop.")
    print("  This audits the flat-spacetime signalling version of the claim, not")
    print("  constrained effective-medium effects such as Scharnhorst propagation.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
