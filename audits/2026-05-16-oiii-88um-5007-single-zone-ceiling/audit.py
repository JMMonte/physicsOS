"""
Audit: is [OIII]88um / [OIII]5007 = 0.26 +/- 0.06 above the single-zone
photoionization ceiling for MACS0416-Y1 *at its measured electron temperature*?

Claim file:  claims/macs0416y1-oiii-ratio-anomaly.md
Paper note:  papers/2026-takechi-dreams-macs0416y1-early-dust.md
Source:      Takechi et al. 2026, arXiv:2605.14922

Paper's measured constraints (sourced from arXiv full text, NOT recalled):
  Te[OIII] = 17300 +/- 1500 K   (from [OIII]4363)
  n_e      = 730 (-140/+150) cm^-3   (from [OII]3726/3729)
  observed [OIII]88um/[OIII]5007 = 0.26 +/- 0.06
The paper's statement is conditional: AT Te=17300 K, "the observed ratio
cannot be reproduced for any electron density." So the correct test is:
fix T_e at the measured value (with its 1sigma range), scan n_e fully, find
the single-zone ceiling, compare to 0.26.

KEY PHYSICS / why the conditioning matters: 5007 (1D2->3P2) has E/k ~ 2.9e4 K,
so eps(5007) ~ exp(-2.9e4/T_e) -- extremely T_e-sensitive. 88um (3P1->3P0)
has E/k ~ 160 K -- T_e-flat. Hence R == eps(88)/eps(5007) FALLS steeply with
T_e. With T_e free, R is unbounded at low T_e (documented below as a caveat);
the claim is only meaningful because [OIII]4363 pins T_e high (17300 K).

Atomic data (PyNeb defaults, recorded for source fidelity):
  radiative   : o_iii_atom_FFT04-SZ00.dat  (Froese Fischer & Tachiev 2004;
                Storey & Zeippen 2000)
  collisional : o_iii_coll_SSB14.dat       (Storey, Sochi & Bautista 2014)

O III levels (1-indexed): 1:3P0 2:3P1 3:3P2 4:1D2 5:1S0
  88um=2->1  52um=3->2  5007=4->3  4959=4->2  4363=5->4

Run from repo root with the project venv:
    .venv/bin/python audits/2026-05-16-oiii-88um-5007-single-zone-ceiling/audit.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

import pyneb as pn

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(exist_ok=True)

print(f"[python] {sys.version.split()[0]}")
print(f"[numpy ] {np.__version__}")
print(f"[pyneb ] {pn.__version__}")

# --- Paper's measured values (sourced from arXiv:2605.14922 full text) ------
OBS, OBS_ERR = 0.26, 0.06
TE_MEAS, TE_ERR = 17_300.0, 1_500.0
NE_MEAS = 730.0

O3 = pn.Atom("O", 3)
print(f"[atom  ] {O3.atomFile}")
print(f"[coll  ] {O3.collFile}")

L = {"88um": (2, 1), "52um": (3, 2), "5007": (4, 3),
     "4959": (4, 2), "4363": (5, 4)}


def eps(line, tem, den):
    i, j = L[line]
    return O3.getEmissivity(tem=tem, den=den, lev_i=i, lev_j=j)


def R_of(tem, den):
    """Intrinsic (dust-free) [OIII]88um/[OIII]5007 energy-emissivity ratio."""
    return eps("88um", tem, den) / eps("5007", tem, den)


# ---------------------------------------------------------------------------
# 0. Atom sanity
# ---------------------------------------------------------------------------
print("\n=== 0. Atom sanity ===")
r_doublet = eps("5007", 1.5e4, 1e2) / eps("4959", 1.5e4, 1e2)
print(f"[OIII]5007/4959 @ (15000K,1e2) = {r_doublet:.3f}  (theory ~2.98)")
assert 2.85 < r_doublet < 3.10, "5007/4959 off -- bad atom data"
for name, (i, j) in L.items():
    print(f"  {name:5s} {i}->{j}: lambda = {O3.wave_Ang[i-1, j-1]:.1f} Ang")
ncrit_88 = float(O3.getCritDensity(tem=TE_MEAS, level=2))
ncrit_5007 = float(O3.getCritDensity(tem=TE_MEAS, level=4))
print(f"  n_crit(3P1, 88um upper)  @17300K = {ncrit_88:.3e} cm^-3")
print(f"  n_crit(1D2, 5007 upper)  @17300K = {ncrit_5007:.3e} cm^-3")

# ---------------------------------------------------------------------------
# 1. PRIMARY TEST: fixed measured T_e, scan n_e fully
# ---------------------------------------------------------------------------
logn = np.linspace(0.0, 6.0, 601)
n_e = 10.0 ** logn

# Most-generous-to-0.26 choice: lower 1sigma T_e (cooler -> 5007 weaker -> R up).
TE_LO = TE_MEAS - TE_ERR          # 15800 K
TE_HI = TE_MEAS + TE_ERR          # 18800 K

R_meas = R_of(TE_MEAS, n_e)
R_lo = R_of(TE_LO, n_e)           # cooler -> highest ceiling
R_hi = R_of(TE_HI, n_e)

ceil_meas = float(R_meas.max())   # max over all n_e at Te=17300
ceil_lo = float(R_lo.max())       # max over all n_e at Te=15800 (most generous)
R_at_point = float(R_of(TE_MEAS, NE_MEAS))

print("\n=== 1. Single-zone ceiling at the MEASURED T_e ===")
print(f"Te = {TE_MEAS:.0f} +/- {TE_ERR:.0f} K ; scan n_e in [1,1e6] cm^-3")
print(f"max single-zone R @ Te=17300 K (any n_e)      = {ceil_meas:.4f}")
print(f"max single-zone R @ Te=15800 K (-1s, generous) = {ceil_lo:.4f}")
print(f"single-zone R at measured (Te=17300, ne=730)   = {R_at_point:.4f}")
print(f"observed                                       = {OBS} +/- {OBS_ERR}")

# The ceiling is the low-density limit (88um quenched above its n_crit).
assert R_meas[0] == ceil_meas, "ceiling should be the n_e->0 limit"

# How far is the observation above the most-generous ceiling?
gap = OBS - ceil_lo
gap_sigma = gap / OBS_ERR                        # in measurement sigma
factor = OBS / ceil_meas
reproducible = ceil_lo >= (OBS - OBS_ERR)
print(f"observed/ceiling(@17300)   = {factor:.2f}x")
print(f"observed - ceiling(@15800) = {gap:.4f}  ({gap_sigma:.1f} sigma)")
print(f"reproducible by ANY single dust-free zone at measured T_e? "
      f"{reproducible}")

# Robustness to the 5007-vs-(4959+5007) definitional ambiguity:
# using the doublet only makes the optical side larger -> R smaller ->
# the conclusion strengthens.
R_doublet_ceiling = float(
    (eps("88um", TE_LO, n_e)
     / (eps("5007", TE_LO, n_e) + eps("4959", TE_LO, n_e))).max())
print(f"ceiling if optical=(4959+5007) @15800K = {R_doublet_ceiling:.4f} "
      f"(<= 5007-only ceiling, conclusion robust)")

# ---------------------------------------------------------------------------
# 2. CAVEAT QUANTIFIED: with T_e FREE the claim would be false
# ---------------------------------------------------------------------------
T_grid = np.linspace(5_000.0, 30_000.0, 251)
ceil_vs_T = np.array([R_of(T, n_e).max() for T in T_grid])  # low-den limit(T)
# T_e at which the single-zone ceiling equals the observed 0.26:
i_cross = int(np.argmin(np.abs(ceil_vs_T - OBS)))
T_cross = float(T_grid[i_cross])
print("\n=== 2. Caveat: T_e dependence of the ceiling ===")
print(f"single-zone ceiling reaches 0.26 only if T_e <= ~{T_cross:.0f} K")
print(f"=> claim holds ONLY because [OIII]4363 pins T_e=17300 K (>> {T_cross:.0f} K)")

# ---------------------------------------------------------------------------
# Dumps
# ---------------------------------------------------------------------------
results = {
    "observed": {"ratio": OBS, "err": OBS_ERR},
    "measured_inputs": {"Te_K": TE_MEAS, "Te_err_K": TE_ERR,
                        "ne_cm3": NE_MEAS},
    "atomic_data": {"radiative": O3.atomFile, "collisional": O3.collFile,
                    "pyneb": pn.__version__},
    "ceiling_at_Te17300_anyne": ceil_meas,
    "ceiling_at_Te15800_generous": ceil_lo,
    "R_at_measured_point": R_at_point,
    "observed_over_ceiling": factor,
    "gap_above_generous_ceiling": gap,
    "gap_sigma": gap_sigma,
    "reproducible_single_zone": bool(reproducible),
    "ceiling_doublet_def_15800K": R_doublet_ceiling,
    "Te_for_ceiling_eq_026_K": T_cross,
    "sanity_5007_over_4959": float(r_doublet),
}
with open(OUT / "results.json", "w") as f:
    json.dump(results, f, indent=2)
np.savetxt(
    OUT / "R_vs_ne_atTe.csv",
    np.column_stack([n_e, R_lo, R_meas, R_hi]),
    delimiter=",",
    header="n_e_cm3,R_Te15800,R_Te17300,R_Te18800", comments="",
)
np.savetxt(
    OUT / "ceiling_vs_Te.csv",
    np.column_stack([T_grid, ceil_vs_T]),
    delimiter=",", header="T_e_K,single_zone_ceiling_R", comments="",
)
print(f"\n[written] {OUT/'results.json'}")
print(f"[written] {OUT/'R_vs_ne_atTe.csv'}")
print(f"[written] {OUT/'ceiling_vs_Te.csv'}")

# ---------------------------------------------------------------------------
# Figures (image + machine-readable data dumped above)
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(1, 2, figsize=(13.5, 5.4))

# Panel A: R vs n_e at the measured T_e (+/-1sigma), vs observed band.
ax[0].plot(n_e, R_meas, color="navy", lw=2, label="T_e = 17300 K (measured)")
ax[0].plot(n_e, R_lo, color="teal", lw=1.6, ls="--",
           label="T_e = 15800 K (-1sigma, generous)")
ax[0].plot(n_e, R_hi, color="darkorange", lw=1.6, ls="--",
           label="T_e = 18800 K (+1sigma)")
ax[0].axhline(OBS, color="crimson", lw=1.8, label="observed 0.26")
ax[0].axhspan(OBS - OBS_ERR, OBS + OBS_ERR, color="crimson", alpha=0.15)
ax[0].axvline(NE_MEAS, color="grey", ls=":", label="measured n_e=730")
ax[0].scatter([NE_MEAS], [R_at_point], color="navy", zorder=5, s=55)
ax[0].annotate(f"single-zone\nceiling {ceil_meas:.3f}",
               xy=(1.5, ceil_meas), xytext=(3, ceil_meas + 0.06),
               fontsize=9, color="navy",
               arrowprops=dict(arrowstyle="->", color="navy"))
ax[0].set_xscale("log")
ax[0].set_xlabel("n_e [cm^-3]")
ax[0].set_ylabel("R = eps(88um)/eps(5007)")
ax[0].set_title("At measured T_e, 0.26 unreachable for ANY n_e")
ax[0].legend(fontsize=8, loc="upper right")
ax[0].grid(alpha=0.3, which="both")
ax[0].set_ylim(0, max(OBS + 0.1, ceil_lo * 1.4))

# Panel B: ceiling vs T_e -- shows the claim is a fixed-T_e statement.
ax[1].plot(T_grid / 1e3, ceil_vs_T, color="darkgreen", lw=2)
ax[1].axhline(OBS, color="crimson", lw=1.8, label="observed 0.26")
ax[1].axhspan(OBS - OBS_ERR, OBS + OBS_ERR, color="crimson", alpha=0.15)
ax[1].axvspan((TE_MEAS - TE_ERR) / 1e3, (TE_MEAS + TE_ERR) / 1e3,
              color="navy", alpha=0.15, label="measured T_e=17300+/-1500")
ax[1].scatter([T_cross / 1e3], [OBS], color="crimson", zorder=5, s=55)
ax[1].annotate(f"ceiling=0.26 only\nif T_e<~{T_cross/1e3:.1f} kK",
               xy=(T_cross / 1e3, OBS), xytext=(T_cross / 1e3 + 3, OBS + 0.9),
               fontsize=9, color="crimson",
               arrowprops=dict(arrowstyle="->", color="crimson"))
ax[1].set_yscale("log")
ax[1].set_xlabel("T_e [10^3 K]")
ax[1].set_ylabel("single-zone ceiling R (n_e->0)")
ax[1].set_title("Ceiling falls steeply with T_e (5007 is T-sensitive)")
ax[1].legend(fontsize=8, loc="upper right")
ax[1].grid(alpha=0.3, which="both")

fig.suptitle("MACS0416-Y1 [OIII]88um/5007 single-zone audit -- "
             "arXiv:2605.14922  (O III FFT04/SZ00 + SSB14)",
             fontsize=11, y=1.02)
fig.tight_layout()
fig.savefig(OUT / "oiii_ratio_audit.png", dpi=140, bbox_inches="tight")
print(f"[written] {OUT/'oiii_ratio_audit.png'}")

print("\n=== VERDICT INPUT ===")
print(f"At Te=17300K: ceiling={ceil_meas:.3f}, observed=0.26 "
      f"-> {factor:.1f}x above, {gap_sigma:.1f}sigma; "
      f"reproducible={reproducible}")
print(f"Caveat: with T_e free, ceiling reaches 0.26 at T_e<~{T_cross:.0f} K")
print("=== DONE ===")
