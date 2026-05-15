"""
Starship launch-economics sensitivity for Dorrington-Olsen EBPS.

This is not a new asteroid-mining architecture model. It changes only
Dorrington and Olsen's launch-cost parameter c_l, keeps their coupling
c_sale = 0.9 c_l, and reruns the already-audited EBPS threshold equations.
"""

from __future__ import annotations

import csv
import importlib.util
import math
import sys
from pathlib import Path

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(exist_ok=True)

BASE_AUDIT = Path(__file__).resolve().parents[1] / "2026-05-15-dorrington-bemr-delta-v-thresholds" / "audit.py"
spec = importlib.util.spec_from_file_location("dorrington_ebps_audit", BASE_AUDIT)
if spec is None or spec.loader is None:
    raise RuntimeError(f"could not import {BASE_AUDIT}")
base = importlib.util.module_from_spec(spec)
sys.modules["dorrington_ebps_audit"] = base
spec.loader.exec_module(base)


def root_or_none(fn):
    try:
        return fn()
    except ValueError:
        return None


def max_npv_capacity(delta_v_km_s: float, isp_s: float, mode: str, p) -> dict[str, float]:
    upper = math.log10(p.maximum_bemr)
    return base.maximize_npv_over_bemr(delta_v_km_s * 1000.0, isp_s, mode, p, (-3.0, upper), 1e-8)


def summarize_scenario(label: str, launch_cost_per_kg: float) -> dict[str, float | str]:
    p = base.Params(launch_cost_per_kg=launch_cost_per_kg)
    chem_cap = root_or_none(lambda: base.capacity_constrained_lim_delta_v(450.0, "chemical", p))
    elec_cap = root_or_none(lambda: base.capacity_constrained_lim_delta_v(3000.0, "electric", p))
    elec_unconstrained = base.electric_zero_npv_lim_delta_v(3000.0, p)
    chem_zero_roots = base.positive_bemr_roots(0.0, 450.0, "chemical", p)
    elec_zero_roots = base.positive_bemr_roots(0.0, 3000.0, "electric", p)
    chem_zero_cap = max_npv_capacity(0.0, 450.0, "chemical", p)
    elec_zero_cap = max_npv_capacity(0.0, 3000.0, "electric", p)

    return {
        "scenario": label,
        "launch_cost_per_kg_usd": launch_cost_per_kg,
        "sale_price_per_kg_usd": p.sale_price_per_kg,
        "max_capacity_kg": p.maximum_capacity_kg,
        "max_bemr_allowed": p.maximum_bemr,
        "chemical_unconstrained_zero_npv_km_s": base.chemical_zero_npv_lim_delta_v(450.0, p) / 1000.0,
        "electric_unconstrained_zero_npv_km_s": elec_unconstrained["delta_v_lim_km_s"],
        "electric_unconstrained_bemr_at_limit": elec_unconstrained["bemr_at_max_npv"],
        "chemical_capacity_zero_npv_km_s": "" if chem_cap is None else chem_cap["delta_v_lim_km_s"],
        "electric_capacity_zero_npv_km_s": "" if elec_cap is None else elec_cap["delta_v_lim_km_s"],
        "chemical_capacity_max_npv_at_zero_dv_usd": chem_zero_cap["max_npv"],
        "electric_capacity_max_npv_at_zero_dv_usd": elec_zero_cap["max_npv"],
        "chemical_required_bemr_at_zero_dv": "" if not chem_zero_roots else chem_zero_roots[0],
        "electric_required_bemr_at_zero_dv": "" if not elec_zero_roots else elec_zero_roots[0],
    }


def zero_dv_requirements(label: str, launch_cost_per_kg: float, capacity_kg: float, mode: str) -> dict[str, float | str]:
    p = base.Params(launch_cost_per_kg=launch_cost_per_kg, maximum_capacity_kg=capacity_kg)
    if mode == "chemical":
        t_year = 2.0 * p.tof_impulsive_year + p.capture_time_year
    elif mode == "electric":
        t_year = 0.0
    else:
        raise ValueError(mode)
    present_revenue_per_return_kg = p.sale_price_per_kg / ((1.0 + p.discount_rate) ** t_year)
    fixed_cost_without_production = p.launch_cost_per_kg
    operations = p.operations_cost_per_year * t_year
    max_cprod = (
        p.maximum_capacity_kg * present_revenue_per_return_kg - operations
    ) / p.dry_total_kg - fixed_cost_without_production
    required_capacity = (
        (p.production_cost_per_kg + p.launch_cost_per_kg) * p.dry_total_kg + operations
    ) / present_revenue_per_return_kg
    return {
        "scenario": label,
        "mode": mode,
        "launch_cost_per_kg_usd": p.launch_cost_per_kg,
        "sale_price_per_kg_usd": p.sale_price_per_kg,
        "capacity_kg": p.maximum_capacity_kg,
        "present_revenue_per_return_kg_usd": present_revenue_per_return_kg,
        "max_production_cost_for_break_even_usd_per_kg": max_cprod,
        "required_capacity_at_paper_production_cost_kg": required_capacity,
        "required_bemr_at_paper_production_cost": required_capacity / p.dry_total_kg,
    }


def decoupled_sale_scenario(label: str, launch_cost_per_kg: float, sale_price_per_kg: float) -> dict[str, float | str]:
    p = base.Params(
        launch_cost_per_kg=launch_cost_per_kg,
        sale_fraction_of_launch_cost=sale_price_per_kg / launch_cost_per_kg,
    )
    chem_cap = root_or_none(lambda: base.capacity_constrained_lim_delta_v(450.0, "chemical", p))
    elec_cap = root_or_none(lambda: base.capacity_constrained_lim_delta_v(3000.0, "electric", p))
    elec_unconstrained = base.electric_zero_npv_lim_delta_v(3000.0, p)
    return {
        "scenario": label,
        "launch_cost_per_kg_usd": launch_cost_per_kg,
        "sale_price_per_kg_usd": p.sale_price_per_kg,
        "chemical_unconstrained_zero_npv_km_s": base.chemical_zero_npv_lim_delta_v(450.0, p) / 1000.0,
        "electric_unconstrained_zero_npv_km_s": elec_unconstrained["delta_v_lim_km_s"],
        "chemical_capacity_zero_npv_km_s": "" if chem_cap is None else chem_cap["delta_v_lim_km_s"],
        "electric_capacity_zero_npv_km_s": "" if elec_cap is None else elec_cap["delta_v_lim_km_s"],
    }


def main() -> int:
    print(f"[python] {sys.version.split()[0]}")
    print("[seed] n/a: deterministic calculation")
    print(f"[base_audit] {BASE_AUDIT}")
    print()

    scenarios = [
        ("Dorrington-Olsen baseline", 7469.88),
        ("Starship public price, 100 t LEO", 90_000_000.0 / 100_000.0),
        ("Starship public price, 150 t LEO", 90_000_000.0 / 150_000.0),
    ]
    rows = [summarize_scenario(label, cost) for label, cost in scenarios]

    path = OUT / "starship_launch_cost_sensitivity.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    requirement_rows = []
    for label, launch_cost in scenarios[1:]:
        for capacity in [150_000.0, 160_000.0, 500_000.0, 1_000_000.0]:
            for mode in ["chemical", "electric"]:
                requirement_rows.append(zero_dv_requirements(label, launch_cost, capacity, mode))

    requirements_path = OUT / "starship_zero_dv_requirements.csv"
    with requirements_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(requirement_rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(requirement_rows)

    baseline_sale_price = base.P.sale_price_per_kg
    decoupled_rows = [
        decoupled_sale_scenario("Starship 100 t, sale price held at Dorrington baseline", 900.0, baseline_sale_price),
        decoupled_sale_scenario("Starship 150 t, sale price held at Dorrington baseline", 600.0, baseline_sale_price),
        decoupled_sale_scenario("Starship 100 t, sale price fixed at $5000/kg", 900.0, 5000.0),
        decoupled_sale_scenario("Starship 150 t, sale price fixed at $5000/kg", 600.0, 5000.0),
    ]
    decoupled_path = OUT / "starship_decoupled_sale_price_sensitivity.csv"
    with decoupled_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(decoupled_rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(decoupled_rows)

    print("[inputs]")
    print("Starship public bracket used here: $90M / (100-150 t) = $600-$900/kg to LEO.")
    print("Dorrington-Olsen coupling retained: c_sale = 0.9 c_l.")
    print()

    print("[results]")
    for r in rows:
        chem_cap = r["chemical_capacity_zero_npv_km_s"]
        elec_cap = r["electric_capacity_zero_npv_km_s"]
        print(
            f"{r['scenario']}: c_l={r['launch_cost_per_kg_usd']:.2f} $/kg, "
            f"c_sale={r['sale_price_per_kg_usd']:.2f} $/kg"
        )
        print(
            "  unconstrained thresholds: "
            f"chemical={r['chemical_unconstrained_zero_npv_km_s']:.6f} km/s, "
            f"electric={r['electric_unconstrained_zero_npv_km_s']:.6f} km/s"
        )
        print(
            "  finite-capacity thresholds: "
            f"chemical={chem_cap if chem_cap != '' else 'none'}, "
            f"electric={elec_cap if elec_cap != '' else 'none'}"
        )
        print(
            "  zero-dv capacity max NPV: "
            f"chemical={r['chemical_capacity_max_npv_at_zero_dv_usd']:.3f} USD, "
            f"electric={r['electric_capacity_max_npv_at_zero_dv_usd']:.3f} USD"
        )
    print()
    print("[zero-dv break-even requirements]")
    for r in requirement_rows:
        if r["capacity_kg"] in (160_000.0, 1_000_000.0):
            print(
                f"{r['scenario']}, {r['mode']}, capacity={r['capacity_kg']:.0f} kg: "
                f"max c_prod={r['max_production_cost_for_break_even_usd_per_kg']:.3f} $/kg; "
                f"required capacity at paper c_prod={r['required_capacity_at_paper_production_cost_kg']:.3f} kg"
            )
    print()
    print("[decoupled sale price sensitivity]")
    for r in decoupled_rows:
        print(
            f"{r['scenario']}: c_l={r['launch_cost_per_kg_usd']:.2f} $/kg, "
            f"c_sale={r['sale_price_per_kg_usd']:.2f} $/kg, "
            f"capacity thresholds chemical={r['chemical_capacity_zero_npv_km_s']:.6f} km/s, "
            f"electric={r['electric_capacity_zero_npv_km_s']:.6f} km/s"
        )
    print()
    print(f"[output] wrote {path}")
    print(f"[output] wrote {requirements_path}")
    print(f"[output] wrote {decoupled_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
