"""
Audit of Dorrington & Olsen's EBPS single-trip delta-v thresholds.

The checked claim is the paper's statement that single-trip whole-asteroid
retrieval with Earth-based propellant supply (EBPS) has positive-NPV delta-v
limits near 1.8 km/s for chemical propulsion (Isp=450 s) and 4.5 km/s for
electric propulsion (Isp=3000 s).

The implementation follows the paper's Eqs. (1), (9), (20), (A.32)-(A.40),
Table 7, Table 10, Table 11, Appendix B, and the Section 5 settings
F_T=10 N and r=20%.
"""

from __future__ import annotations

import csv
import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy import constants as C
from scipy.optimize import brentq, minimize_scalar
import sympy as sp

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(exist_ok=True)

G0 = C.g  # m s^-2
YEAR = C.Julian_year  # s


@dataclass(frozen=True)
class Params:
    dry_spacecraft_kg: float = 1000.0
    mining_equipment_kg: float = 250.0
    maximum_capacity_kg: float = 160_000.0
    launch_cost_per_kg: float = 7469.88
    production_cost_per_kg: float = 300_000.0
    propellant_cost_per_kg: float = 0.0
    sale_fraction_of_launch_cost: float = 0.9
    operations_cost_per_year: float = 487_160.0
    discount_rate: float = 0.20
    thrust_n: float = 10.0
    tof_impulsive_year: float = 0.5
    capture_time_year: float = 0.0

    @property
    def dry_total_kg(self) -> float:
        return self.dry_spacecraft_kg + self.mining_equipment_kg

    @property
    def sale_price_per_kg(self) -> float:
        return self.sale_fraction_of_launch_cost * self.launch_cost_per_kg

    @property
    def maximum_bemr(self) -> float:
        return self.maximum_capacity_kg / self.dry_total_kg


P = Params()


def exhaust_velocity(isp_s: float) -> float:
    return G0 * isp_s


def exp_leg(delta_v_m_s: float, isp_s: float) -> float:
    return math.exp(delta_v_m_s / exhaust_velocity(isp_s))


def ebps_masses(delta_v_one_way_m_s: float, isp_s: float, return_mass_kg: float, p: Params = P) -> dict[str, float]:
    """Eqs. (A.32), (A.33), and (A.36) for DeltaV_EA = DeltaV_AE."""
    e1 = exp_leg(delta_v_one_way_m_s, isp_s)
    e2 = exp_leg(2.0 * delta_v_one_way_m_s, isp_s)
    mdry = p.dry_total_kg
    m0 = mdry * e2 + return_mass_kg * (e2 - e1)
    mp_total = mdry * (e2 - 1.0) + return_mass_kg * (e2 - e1)
    mp_ae = (mdry + return_mass_kg) * (e1 - 1.0)
    return {"m0": m0, "mp_total": mp_total, "mp_ae": mp_ae, "e1": e1, "e2": e2}


def ebps_duration_years(delta_v_one_way_m_s: float, isp_s: float, return_mass_kg: float, mode: str, p: Params = P) -> float:
    """Table 7 duration model for EBPS."""
    if mode == "chemical":
        return 2.0 * p.tof_impulsive_year + p.capture_time_year
    if mode == "electric":
        masses = ebps_masses(delta_v_one_way_m_s, isp_s, return_mass_kg, p)
        leg1_s = delta_v_one_way_m_s * masses["m0"] / p.thrust_n
        leg2_s = delta_v_one_way_m_s * (p.dry_total_kg + return_mass_kg + masses["mp_ae"]) / p.thrust_n
        return (leg1_s + leg2_s) / YEAR + p.capture_time_year
    raise ValueError(mode)


def ebps_npv(delta_v_one_way_m_s: float, isp_s: float, bemr: float, mode: str, p: Params = P) -> float:
    """Eq. (A.40), with return mass parameterized as BEMR * m_dry."""
    mdry = p.dry_total_kg
    mr = bemr * mdry
    masses = ebps_masses(delta_v_one_way_m_s, isp_s, mr, p)
    t = ebps_duration_years(delta_v_one_way_m_s, isp_s, mr, mode, p)

    variable_return_cost = (p.launch_cost_per_kg + p.propellant_cost_per_kg) * (masses["e2"] - masses["e1"])
    fixed_cost_per_dry_kg = (
        (p.production_cost_per_kg + p.launch_cost_per_kg)
        + (p.launch_cost_per_kg + p.propellant_cost_per_kg) * (masses["e2"] - 1.0)
    )
    return (
        mr * (p.sale_price_per_kg / ((1.0 + p.discount_rate) ** t) - variable_return_cost)
        - mdry * fixed_cost_per_dry_kg
        - p.operations_cost_per_year * t
    )


def zero_profit_lim_delta_v(isp_s: float, p: Params = P) -> float:
    """Paper Eq. (28), returned in m/s."""
    ratio = p.sale_price_per_kg / (p.launch_cost_per_kg + p.propellant_cost_per_kg)
    x = 0.5 * (1.0 + math.sqrt(1.0 + 4.0 * ratio))
    return exhaust_velocity(isp_s) * math.log(x)


def chemical_zero_npv_lim_delta_v(isp_s: float, p: Params = P) -> float:
    """Chemical EBPS NPV limit, since T is independent of return mass."""
    ratio = p.sale_price_per_kg / ((1.0 + p.discount_rate) ** (2.0 * p.tof_impulsive_year + p.capture_time_year))
    ratio /= p.launch_cost_per_kg + p.propellant_cost_per_kg
    x = 0.5 * (1.0 + math.sqrt(1.0 + 4.0 * ratio))
    return exhaust_velocity(isp_s) * math.log(x)


def maximize_npv_over_bemr(
    delta_v_one_way_m_s: float,
    isp_s: float,
    mode: str,
    p: Params = P,
    log_bounds: tuple[float, float] = (-3.0, 5.0),
    xatol: float = 1e-8,
) -> dict[str, float]:
    """Find the best positive-NPV opportunity at a fixed delta-v."""
    def objective(log10_bemr: float) -> float:
        bemr = 10.0**log10_bemr
        return -ebps_npv(delta_v_one_way_m_s, isp_s, bemr, mode, p)

    res = minimize_scalar(objective, bounds=log_bounds, method="bounded", options={"xatol": xatol})
    bemr = 10.0**res.x
    return {"bemr_at_max_npv": bemr, "max_npv": -res.fun}


def electric_zero_npv_lim_delta_v(
    isp_s: float,
    p: Params = P,
    log_bounds: tuple[float, float] = (-3.0, 5.0),
    xatol: float = 1e-8,
    root_xtol: float = 1e-8,
) -> dict[str, float]:
    """Threshold where max_BEMR NPV crosses zero."""
    def f(delta_v_km_s: float) -> float:
        return maximize_npv_over_bemr(delta_v_km_s * 1000.0, isp_s, "electric", p, log_bounds, xatol)["max_npv"]

    root_km_s = brentq(f, 0.1, 20.0, xtol=root_xtol, rtol=root_xtol)
    optimum = maximize_npv_over_bemr(root_km_s * 1000.0, isp_s, "electric", p, log_bounds, xatol)
    return {"delta_v_lim_km_s": root_km_s, **optimum}


def capacity_constrained_lim_delta_v(isp_s: float, mode: str, p: Params = P) -> dict[str, float]:
    """Threshold where max NPV over 0 < BEMR <= capacity/dry_mass crosses zero."""
    upper = math.log10(p.maximum_bemr)

    def f(delta_v_km_s: float) -> float:
        return maximize_npv_over_bemr(delta_v_km_s * 1000.0, isp_s, mode, p, (-3.0, upper), 1e-8)["max_npv"]

    root_km_s = brentq(f, 0.1, 20.0, xtol=1e-8, rtol=1e-8)
    optimum = maximize_npv_over_bemr(root_km_s * 1000.0, isp_s, mode, p, (-3.0, upper), 1e-8)
    return {"delta_v_lim_km_s": root_km_s, **optimum, "max_bemr_allowed": p.maximum_bemr}


def symbolic_threshold_check() -> dict[str, str | float]:
    """Use SymPy to derive Eq. (28) from the large-return-mass coefficient."""
    y, q = sp.symbols("y q", positive=True)
    # EBPS with DeltaV_tot = 2 DeltaV_EA has return-mass coefficient:
    # c_sale - (c_l + c_p)(y^2 - y). Setting q = c_sale/(c_l+c_p)
    # gives y^2 - y - q = 0.
    roots = sp.solve(sp.Eq(y**2 - y - q, 0), y)
    positive_root = sp.simplify(roots[1])
    expected = sp.Rational(1, 2) * (1 + sp.sqrt(1 + 4 * q))
    residual = sp.simplify(positive_root - expected)
    numeric_residual = float(residual.subs(q, sp.Rational(9, 10)))
    return {
        "equation": "y**2 - y - q = 0",
        "positive_root": str(positive_root),
        "expected_eq28_root": str(expected),
        "symbolic_residual": str(residual),
        "numeric_residual_at_q_0p9": numeric_residual,
    }


def positive_bemr_roots(delta_v_one_way_m_s: float, isp_s: float, mode: str, p: Params = P) -> list[float]:
    """Locate BEMR roots where NPV=0 by scanning log-spaced BEMR values."""
    xs = np.linspace(-3.0, 5.0, 1200)
    vals = [ebps_npv(delta_v_one_way_m_s, isp_s, 10.0**x, mode, p) for x in xs]
    roots: list[float] = []
    for xa, xb, fa, fb in zip(xs[:-1], xs[1:], vals[:-1], vals[1:]):
        if fa == 0.0:
            roots.append(10.0**xa)
        elif fa * fb < 0.0:
            root_log = brentq(lambda z: ebps_npv(delta_v_one_way_m_s, isp_s, 10.0**z, mode, p), xa, xb)
            roots.append(10.0**root_log)
    return roots


def main() -> int:
    print(f"[python] {sys.version.split()[0]}")
    print(f"[numpy] {np.__version__}")
    print(f"[sympy] {sp.__version__}")
    print(f"[scipy.constants] g0={G0:.12g} m/s^2, Julian_year={YEAR:.12g} s")
    print("[seed] n/a: deterministic calculation")
    print()

    print("[paper inputs]")
    print(f"m_dry,total={P.dry_total_kg:.0f} kg (1000 kg spacecraft + 250 kg mining equipment)")
    print(f"M_max={P.maximum_capacity_kg:.0f} kg, max BEMR={P.maximum_bemr:.6f}")
    print(f"c_l={P.launch_cost_per_kg:.2f} $/kg, c_sale=0.9*c_l={P.sale_price_per_kg:.2f} $/kg")
    print(f"c_prod={P.production_cost_per_kg:.2f} $/kg, c_p={P.propellant_cost_per_kg:.2f} $/kg")
    print(f"c_ops={P.operations_cost_per_year:.2f} $/yr, r={P.discount_rate:.2f}, F_T={P.thrust_n:.1f} N")
    print()

    print("[dimensional]")
    print("Eq. (20): exp(DeltaV / (g0 Isp)) is dimensionless.")
    print("Eq. (A.40): NPV terms are kg * $/kg or $/yr * yr, hence dollars.")
    print("Table 7 electric duration: DeltaV [m/s] * mass [kg] / thrust [N] = seconds.")
    print()

    sym = symbolic_threshold_check()
    print("[symbolic]")
    print(f"large-return coefficient equation: {sym['equation']}")
    print(f"positive root: {sym['positive_root']}")
    print(f"Eq. (28) root: {sym['expected_eq28_root']}")
    print(f"symbolic residual: {sym['symbolic_residual']}")
    print()

    print("[limits]")
    print(f"DeltaV=0, EBPS masses for BEMR=1: {ebps_masses(0.0, 450.0, P.dry_total_kg)}")
    print(f"DeltaV=0, chemical T={ebps_duration_years(0.0, 450.0, P.dry_total_kg, 'chemical'):.6f} yr")
    print(f"DeltaV=0, electric T={ebps_duration_years(0.0, 3000.0, P.dry_total_kg, 'electric'):.6f} yr")
    print()

    chem_zero_profit = zero_profit_lim_delta_v(450.0) / 1000.0
    chem_zero_npv = chemical_zero_npv_lim_delta_v(450.0) / 1000.0
    elec_zero_profit = zero_profit_lim_delta_v(3000.0) / 1000.0
    elec_zero_npv = electric_zero_npv_lim_delta_v(3000.0)
    chem_capacity = capacity_constrained_lim_delta_v(450.0, "chemical")
    elec_capacity = capacity_constrained_lim_delta_v(3000.0, "electric")

    print("[thresholds]")
    print(f"chemical Isp=450 s, Eq. (28) zero-profit limit: {chem_zero_profit:.6f} km/s")
    print(f"chemical Isp=450 s, zero-NPV limit with T=1 yr, r=20%: {chem_zero_npv:.6f} km/s")
    print(f"electric Isp=3000 s, Eq. (28) zero-profit limit: {elec_zero_profit:.6f} km/s")
    print(
        "electric Isp=3000 s, zero-NPV max-over-BEMR limit: "
        f"{elec_zero_npv['delta_v_lim_km_s']:.6f} km/s "
        f"(BEMR at max={elec_zero_npv['bemr_at_max_npv']:.6f})"
    )
    print(
        "capacity-constrained chemical Isp=450 s, zero-NPV limit: "
        f"{chem_capacity['delta_v_lim_km_s']:.6f} km/s "
        f"(max BEMR={chem_capacity['max_bemr_allowed']:.6f})"
    )
    print(
        "capacity-constrained electric Isp=3000 s, zero-NPV limit: "
        f"{elec_capacity['delta_v_lim_km_s']:.6f} km/s "
        f"(max BEMR={elec_capacity['max_bemr_allowed']:.6f})"
    )
    print()

    convergence_rows = []
    for lower, upper, xatol, root_xtol in [
        (-2.0, 4.0, 1e-6, 1e-6),
        (-3.0, 5.0, 1e-8, 1e-8),
        (-4.0, 6.0, 1e-10, 1e-10),
    ]:
        conv = electric_zero_npv_lim_delta_v(3000.0, P, (lower, upper), xatol, root_xtol)
        convergence_rows.append(
            {
                "log10_bemr_lower": lower,
                "log10_bemr_upper": upper,
                "optimizer_xatol": xatol,
                "root_xtol": root_xtol,
                "delta_v_lim_km_s": conv["delta_v_lim_km_s"],
                "bemr_at_max_npv": conv["bemr_at_max_npv"],
                "max_npv_usd": conv["max_npv"],
            }
        )

    conv_path = OUT / "electric_threshold_convergence.csv"
    with conv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(convergence_rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(convergence_rows)

    print("[convergence]")
    for r in convergence_rows:
        print(
            f"log10 BEMR [{r['log10_bemr_lower']:.0f}, {r['log10_bemr_upper']:.0f}], "
            f"xatol={r['optimizer_xatol']:.0e}: "
            f"delta_v={r['delta_v_lim_km_s']:.9f} km/s, "
            f"BEMR={r['bemr_at_max_npv']:.6f}"
        )
    print()

    rows = []
    for case, mode, isp, dv_km_s in [
        ("chemical_at_paper_limit", "chemical", 450.0, 1.8),
        ("electric_at_paper_limit", "electric", 3000.0, 4.5),
        ("electric_at_5_km_s", "electric", 3000.0, 5.0),
    ]:
        opt = maximize_npv_over_bemr(dv_km_s * 1000.0, isp, mode)
        roots = positive_bemr_roots(dv_km_s * 1000.0, isp, mode)
        for bemr in [10.0, 61.0, 80.0, 100.0, opt["bemr_at_max_npv"]]:
            rows.append(
                {
                    "case": case,
                    "mode": mode,
                    "isp_s": isp,
                    "delta_v_one_way_km_s": dv_km_s,
                    "bemr": bemr,
                    "duration_years": ebps_duration_years(dv_km_s * 1000.0, isp, bemr * P.dry_total_kg, mode),
                    "npv_usd": ebps_npv(dv_km_s * 1000.0, isp, bemr, mode),
                    "max_npv_usd": opt["max_npv"],
                    "bemr_at_max_npv": opt["bemr_at_max_npv"],
                    "roots": ";".join(f"{r:.9g}" for r in roots),
                }
            )

    csv_path = OUT / "ebps_npv_thresholds.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print("[sample NPV checks]")
    for case in sorted({r["case"] for r in rows}):
        subset = [r for r in rows if r["case"] == case]
        first = subset[0]
        print(
            f"{case}: roots={first['roots'] or 'none'}, "
            f"max_NPV={first['max_npv_usd']:.3f} USD at BEMR={first['bemr_at_max_npv']:.6f}"
        )
    print(f"[output] wrote {csv_path}")
    print(f"[output] wrote {conv_path}")
    print()

    capacity_rows = [
        {
            "mode": "chemical",
            "isp_s": 450.0,
            "capacity_kg": P.maximum_capacity_kg,
            "max_bemr_allowed": chem_capacity["max_bemr_allowed"],
            "capacity_constrained_zero_npv_km_s": chem_capacity["delta_v_lim_km_s"],
            "bemr_at_max_npv": chem_capacity["bemr_at_max_npv"],
            "max_npv_usd": chem_capacity["max_npv"],
        },
        {
            "mode": "electric",
            "isp_s": 3000.0,
            "capacity_kg": P.maximum_capacity_kg,
            "max_bemr_allowed": elec_capacity["max_bemr_allowed"],
            "capacity_constrained_zero_npv_km_s": elec_capacity["delta_v_lim_km_s"],
            "bemr_at_max_npv": elec_capacity["bemr_at_max_npv"],
            "max_npv_usd": elec_capacity["max_npv"],
        },
    ]
    capacity_path = OUT / "capacity_constrained_thresholds.csv"
    with capacity_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(capacity_rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(capacity_rows)
    print("[capacity-constrained check]")
    for r in capacity_rows:
        print(
            f"{r['mode']}: zero-NPV limit={r['capacity_constrained_zero_npv_km_s']:.6f} km/s, "
            f"BEMR at max={r['bemr_at_max_npv']:.6f}, max allowed={r['max_bemr_allowed']:.6f}"
        )
    print(f"[output] wrote {capacity_path}")
    print()

    sensitivity_rows = []
    for label, params in [
        ("paper_total_dry_1250kg", P),
        ("spacecraft_only_1000kg", Params(mining_equipment_kg=0.0)),
        ("lower_thrust_2N", Params(thrust_n=2.0)),
        ("zero_discount", Params(discount_rate=0.0)),
    ]:
        try:
            electric = electric_zero_npv_lim_delta_v(3000.0, params)
            electric_limit = electric["delta_v_lim_km_s"]
            electric_bemr = electric["bemr_at_max_npv"]
        except ValueError:
            electric_limit = float("nan")
            electric_bemr = float("nan")
        sensitivity_rows.append(
            {
                "case": label,
                "dry_total_kg": params.dry_total_kg,
                "thrust_n": params.thrust_n,
                "discount_rate": params.discount_rate,
                "chemical_zero_npv_km_s": chemical_zero_npv_lim_delta_v(450.0, params) / 1000.0,
                "electric_zero_npv_km_s": electric_limit,
                "electric_bemr_at_limit": electric_bemr,
            }
        )

    sensitivity_path = OUT / "scope_sensitivity.csv"
    with sensitivity_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(sensitivity_rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(sensitivity_rows)

    print("[scope sensitivity]")
    for r in sensitivity_rows:
        print(
            f"{r['case']}: chemical={r['chemical_zero_npv_km_s']:.6f} km/s, "
            f"electric={r['electric_zero_npv_km_s']:.6f} km/s"
        )
    print(f"[output] wrote {sensitivity_path}")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
