"""
Audit: a preferred-frame faster-than-light signalling rule can be
chronology-safe in the narrow kinematic sense.

Conventions:
  - Natural units, c = 1, distances in light-years, times in years.
  - Preferred/effective frame coordinates are (T, X).
  - alpha = u/c > 1 is the signal speed in the preferred frame.
  - beta = v/c is the speed of a receiver relative to the preferred frame.
  - Signals must always satisfy Delta T >= 0 in the preferred frame.

Run from repo root:
    /usr/bin/python3 audits/2026-05-15-preferred-frame-ftl-chronology/audit.py
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

SEED = 1
np.random.seed(SEED)
print(f"[seed] {SEED}")
print(f"[python] {sys.version.split()[0]}")
print(f"[numpy] {np.__version__}")
print(f"[sympy] {getattr(sp, '__version__', 'missing')}")
print(f"[pint] {getattr(pint, '__version__', 'missing')}")
print()


def preferred_frame_roundtrip(alpha: float, beta: float, separation_ly: float = 1.0) -> dict[str, float]:
    """Two-leg exchange when the FTL rule is defined only in a preferred frame.

    Preferred frame P:
      A is at X=0.
      B moves in +X with speed beta and starts at X=L when A emits at T=0.
      A sends to B at speed alpha in P.
      B immediately replies leftward at speed alpha in P, not in B's rest frame.

    This is the same geometry as the antitelephone audit except for the
    load-bearing rule: the return pulse is constrained by the preferred frame.
    """
    if not (alpha > 1.0):
        raise ValueError("alpha must exceed 1 for FTL")
    if not (0.0 <= beta < 1.0):
        raise ValueError("beta must be in [0, 1)")
    if beta >= alpha:
        raise ValueError("beta must be smaller than alpha for the first interception setup")

    L = separation_ly
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)

    # First leg in P: X_signal = alpha T, X_B = L + beta T.
    T1 = L / (alpha - beta)
    X1 = alpha * T1

    # B-frame coordinates for the first-leg reception event. These are not
    # used by the mechanism, but they show the coordinate-ordering trap.
    t1_B = gamma * (T1 - beta * X1)
    x1_B = gamma * (X1 - beta * T1)

    # Reply constrained in P: X_reply = X1 - alpha (T - T1).
    T2 = T1 + X1 / alpha
    X2 = 0.0

    return {
        "gamma": gamma,
        "T1_pref_year": T1,
        "X1_pref_ly": X1,
        "t1_B_year": t1_B,
        "x1_B_ly": x1_B,
        "T2_pref_year": T2,
        "X2_pref_ly": X2,
    }


def reciprocal_sender_frame_return_time(alpha: float, beta: float, separation_ly: float = 1.0) -> float:
    """Return time in A's frame for the unrestricted reciprocal antitelephone rule."""
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    L = separation_ly
    t1 = L / (alpha - beta)
    x1 = alpha * t1
    t1p = gamma * (t1 - beta * x1)
    x1p = gamma * (x1 - beta * t1)
    t2p = (x1p + alpha * t1p) / (alpha - beta)
    x2p = -beta * t2p
    return gamma * (t2p + beta * x2p)


def main() -> int:
    print("== DIMENSIONAL CHECK ==")
    if pint is not None:
        ureg = pint.UnitRegistry()
        dx_over_u = (1.0 * ureg.meter) / (2.0 * ureg.meter / ureg.second)
        print(f"  Delta X / u: {dx_over_u.to(ureg.second):~P}")
        print("  Preferred-frame signal time Delta T = |Delta X| / u has time units.")
    else:
        print("  pint unavailable; manual unit check: m/(m/s) = s.")
    print()

    print("== SYMBOLIC DERIVATION ==")
    print("  Preferred-frame rule: every signal edge obeys Delta T = |Delta X| / alpha >= 0.")
    print("  Every ordinary subluminal worldline also has monotonically increasing T.")
    if sp is not None:
        a, b, L = sp.symbols("a b L", positive=True)
        T1 = L / (a - b)
        X1 = a * T1
        T2 = sp.simplify(T1 + X1 / a)
        print(f"  Round-trip return in preferred frame: T2 = {sp.factor(T2)}")
        print("  For alpha > 1, 0 <= beta < 1, L > 0, this is strictly positive.")
    else:
        print("  SymPy unavailable; using closed-form derivation in README.")
    print()

    print("== LIMITS ==")
    beta = 0.9
    L = 1.0
    for alpha in [1.001, 1.01, 1.1, 2.0, 10.0, 1.0e6]:
        vals = preferred_frame_roundtrip(alpha, beta if beta < alpha else 0.9 * alpha, L)
        print(f"  alpha={alpha:>10.6g}  beta={beta if beta < alpha else 0.9 * alpha:.6g}  T2={vals['T2_pref_year']:.12g} yr")
    print("  alpha -> infinity gives preferred-frame simultaneity, T2 -> 0+, not T2 < 0.")
    print()

    print("== WORKED COMPARISON ==")
    alpha = 2.0
    beta = 0.9
    vals = preferred_frame_roundtrip(alpha, beta, 1.0)
    reciprocal_t2 = reciprocal_sender_frame_return_time(alpha, beta, 1.0)
    print(f"  alpha={alpha:.3f}, beta={beta:.3f}, L=1 light-year")
    for key in [
        "gamma",
        "T1_pref_year",
        "X1_pref_ly",
        "t1_B_year",
        "x1_B_ly",
        "T2_pref_year",
        "X2_pref_ly",
    ]:
        print(f"  {key:>14}: {vals[key]: .12g}")
    print(f"  unrestricted reciprocal sender-frame return: {reciprocal_t2: .12g} yr")
    print("  preferred-frame constrained return:          "
          f"{vals['T2_pref_year']: .12g} yr")
    print()

    print("== GRID CHECK ==")
    print("  Scan beta in [0, 0.999999] for alpha=2. Preferred-frame return stays positive.")
    for n in [1_000, 10_000, 100_000]:
        betas = np.linspace(0.0, 0.999999, n)
        returns = np.array([preferred_frame_roundtrip(alpha, float(b), 1.0)["T2_pref_year"] for b in betas])
        print(
            f"  N={n:>6}: min_T2={returns.min():.12g}, "
            f"max_T2={returns.max():.12g}, any_negative={bool(np.any(returns < 0.0))}"
        )
    print()

    print("== RANDOM RELAY CHECK ==")
    print("  Synthetic relay chain: Delta T_i = |Delta X_i|/alpha_i + wait_i.")
    for n_edges in [10, 100, 1000]:
        alphas = 1.0 + 99.0 * np.random.random(n_edges)
        distances = 10.0 * np.random.random(n_edges)
        waits = 0.01 * np.random.random(n_edges)
        dts = distances / alphas + waits
        total = float(np.sum(dts))
        print(f"  edges={n_edges:>4}: total_Delta_T={total:.12g}, any_negative_edge={bool(np.any(dts < 0.0))}")
    print()

    print("== VERDICT INPUT ==")
    print("  A global preferred/effective time T that increases on every allowed")
    print("  matter worldline and every FTL signal curve is a time function.")
    print("  The antitelephone loop is blocked because relays cannot choose the")
    print("  reciprocal sender-rest-frame rule; all signal chains have Delta T >= 0.")
    print("  This supports chronology safety for this constrained rule only. It does")
    print("  not establish a practical, macroscopic, controllable FTL drive.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
