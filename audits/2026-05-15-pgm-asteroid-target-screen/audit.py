"""
PGM asteroid target screen.

This audit is a first-pass screen, not a mission design. It combines:
- current spot-price scale for Pt, Pd, Rh;
- Cannon et al. PGM grade bounds for iron meteorites;
- published target evidence for 1986 DA, 2016 ED85, and 1992 TC;
- JPL's May 2026 LEO-to-rendezvous delta-v table.
"""

from __future__ import annotations

import csv
from pathlib import Path

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(exist_ok=True)

TROY_OZ_PER_KG = 32.1507465686

METAL_PRICES_USD_PER_TOZ = {
    "Pt": 2029.40,
    "Pd": 1435.00,
    "Rh": 9975.00,
}

PGM_GRADE_CASES_PPM = {
    "Ostro_1986_DA_assumption": 10.0,
    "Cannon_iron_meteorite_low": 6.0,
    "Cannon_iron_meteorite_median": 40.78,
    "Cannon_iron_meteorite_90th_percentile": 107.86,
    "Cannon_iron_meteorite_high": 230.0,
}

TARGETS = [
    {
        "target": "6178 (1986 DA)",
        "composition_evidence": "radar metallic + NIR metal-rich; ~85% metal / ~15% pyroxene",
        "pgm_evidence": "inferred from meteoritic metal analogs; no direct assay",
        "delta_v_from_leo_km_s": 7.157,
        "source_quality": "strong composition, weak PGM-grade, high delta-v",
        "screen_verdict": "best known PGM prospecting target, not mine-ready",
    },
    {
        "target": "2016 ED85",
        "composition_evidence": "NIR spectrum similar to 1986 DA; no radar confirmation",
        "pgm_evidence": "inferred from metal-rich analogs; no direct assay",
        "delta_v_from_leo_km_s": 7.376,
        "source_quality": "moderate composition, weak PGM-grade, high delta-v",
        "screen_verdict": "prospecting watchlist, less secure than 1986 DA",
    },
    {
        "target": "7474 (1992 TC)",
        "composition_evidence": "reported M-type; not checked here against modern spectroscopy",
        "pgm_evidence": "no PGM-grade evidence found in this screen",
        "delta_v_from_leo_km_s": 5.619,
        "source_quality": "better accessibility, weak composition/PGM evidence",
        "screen_verdict": "characterization candidate, not a mine-ready target",
    },
]


def value_per_kg_bulk(grade_ppm: float, pure_metal_price_usd_per_kg: float) -> float:
    return grade_ppm * 1e-6 * pure_metal_price_usd_per_kg


def main() -> int:
    price_rows = []
    for metal, price_toz in METAL_PRICES_USD_PER_TOZ.items():
        price_rows.append(
            {
                "metal": metal,
                "price_usd_per_troy_oz": price_toz,
                "price_usd_per_kg": price_toz * TROY_OZ_PER_KG,
            }
        )

    prices_path = OUT / "pgm_prices.csv"
    with prices_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(price_rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(price_rows)

    value_rows = []
    for grade_label, grade_ppm in PGM_GRADE_CASES_PPM.items():
        for metal, price_toz in METAL_PRICES_USD_PER_TOZ.items():
            price_kg = price_toz * TROY_OZ_PER_KG
            value_rows.append(
                {
                    "grade_case": grade_label,
                    "total_pgm_grade_ppm": grade_ppm,
                    "all_pgm_priced_as": metal,
                    "pure_metal_price_usd_per_kg": price_kg,
                    "raw_bulk_value_usd_per_kg": value_per_kg_bulk(grade_ppm, price_kg),
                    "pgm_kg_per_1000_t_bulk": grade_ppm,
                    "gross_value_per_1000_t_bulk_usd": grade_ppm * price_kg,
                }
            )

    values_path = OUT / "pgm_grade_value_scale.csv"
    with values_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(value_rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(value_rows)

    target_path = OUT / "target_screen.csv"
    with target_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(TARGETS[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(TARGETS)

    print("[prices]")
    for row in price_rows:
        print(f"{row['metal']}: {row['price_usd_per_kg']:.3f} USD/kg")
    print()

    print("[raw bulk value scale]")
    for grade in ["Ostro_1986_DA_assumption", "Cannon_iron_meteorite_median", "Cannon_iron_meteorite_high"]:
        subset = [r for r in value_rows if r["grade_case"] == grade]
        low = min(r["raw_bulk_value_usd_per_kg"] for r in subset)
        high = max(r["raw_bulk_value_usd_per_kg"] for r in subset)
        print(f"{grade}: {low:.3f}-{high:.3f} USD/kg raw bulk, depending on PGM basket")
    print()

    print("[target screen]")
    for target in TARGETS:
        print(
            f"{target['target']}: dv={target['delta_v_from_leo_km_s']:.3f} km/s; "
            f"{target['screen_verdict']}"
        )
    print()

    print(f"[output] wrote {prices_path}")
    print(f"[output] wrote {values_path}")
    print(f"[output] wrote {target_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
