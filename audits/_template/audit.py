"""
Audit script template.

Replace this docstring with: what is being audited, which claim file, which paper.
Run from the repo root with the project venv:

    .venv/bin/python audits/<date>-<slug>/audit.py

(If .venv is missing, run scripts/bootstrap.sh first.)

Print all results; save figures to ./outputs/.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import numpy as np
from scipy import constants as C

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(exist_ok=True)

SEED = 0
np.random.seed(SEED)
print(f"[seed] {SEED}")
print(f"[python] {sys.version.split()[0]}")
print(f"[numpy] {np.__version__}")


def main() -> int:
    # === 1. Dimensional analysis (use pint or astropy.units when possible) ===
    # ...

    # === 2. Limits / known cases ===
    # ...

    # === 3. The actual computation ===
    # ...

    # === 4. Convergence study, if numerical ===
    # for N in [10, 100, 1000, 10000]:
    #     result = compute(N)
    #     print(f"N={N}: result={result}")

    # === 5. Compare to cited source ===
    # cited_value = ...
    # rel_err = abs(result - cited_value) / abs(cited_value)
    # print(f"relative error vs cited: {rel_err:.3e}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
