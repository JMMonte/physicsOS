"""
Audit: can Casimir, Inc.'s "MicroSparc" chip deliver 37.5 μW continuously
from a 5 mm × 5 mm cavity, by harvesting "quantum vacuum" energy?

Tested against:
1. Casimir reservoir size — total energy per unit area stored in the
   inter-plate field as a function of plate gap d.
2. Drain time — at the advertised areal power, how long can a static
   cavity supply that power before exhausting the reservoir?
3. Dynamical Casimir effect (DCE) lower bound — if the cavity is being
   "pumped" by moving a boundary, the boundary must move at relativistic
   speeds to produce milliwatt-per-square-meter power. Check that.
4. Thermal equilibrium check — at room temperature, the cavity is bathed
   in blackbody radiation. A passive device cannot extract net work from
   a single-temperature reservoir (second law). For context: how much
   blackbody power per m² is *in* the visible-band cavity modes?
5. Conservativity of the static Casimir force.

Conventions: SI throughout. Constants from scipy.

Run:   /usr/bin/python3 audit.py
Output figure: outputs/casimir-reservoir-and-drain-time.png
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

try:
    from scipy import constants as C
except ImportError:  # fall back to literals so audit runs without scipy
    class _C:
        hbar = 1.054_571_817e-34
        c = 299_792_458.0
        k = 1.380_649e-23
        h = 6.626_070_15e-34
    C = _C()

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(exist_ok=True)

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAVE_PLT = True
except ImportError:
    HAVE_PLT = False

SEED = 0
np.random.seed(SEED)
print(f"[seed] {SEED}")
print(f"[python] {sys.version.split()[0]}  numpy {np.__version__}")
print()


# ----------------------------- Claim --------------------------------------

CHIP_SIDE_M = 5e-3
CHIP_AREA_M2 = CHIP_SIDE_M ** 2
P_CHIP_W = 1.5 * 25e-6                       # 1.5 V × 25 μA = 37.5 μW
P_AREAL = P_CHIP_W / CHIP_AREA_M2            # W/m²

print("== CLAIM ==")
print(f"  chip area:    {CHIP_AREA_M2*1e4:.3g} cm²  ({CHIP_AREA_M2:.3g} m²)")
print(f"  chip power:   {P_CHIP_W*1e6:.2f} μW")
print(f"  areal power:  {P_AREAL:.3f} W/m²  (= {P_AREAL*1e2:.2f} μW/cm²)")
print()


# ---------------------- 1. Casimir reservoir size --------------------------
# Energy per unit area between perfectly conducting parallel plates at T=0:
#     E(d)/A = -π² ℏ c / (720 d³)
# We use the magnitude as the upper bound on energy the cavity could
# deliver as it relaxes from gap d to 0.

print("== CASIMIR RESERVOIR ==")
print(f"  ℏc = {C.hbar*C.c:.3e} J·m")
print(f"  |E(d)|/A = π² ℏ c / (720 d³)")
print()

def E_per_area(d):
    return (np.pi**2) * C.hbar * C.c / (720.0 * d**3)

d_values = np.array([0.5e-9, 1e-9, 10e-9, 100e-9, 1e-6])
print(f"  {'gap d':>12} | {'|E|/A (J/m²)':>14} | {'drain time @ claim':>22}")
for d in d_values:
    e = E_per_area(d); t = e / P_AREAL
    print(f"  {d*1e9:>10.2f} nm | {e:>14.3e} | {t:>20.3e} s")
print()


# ---------------- 2. Hypothetical gap for 10-year drain --------------------

T_target_s = 10 * 365.25 * 24 * 3600
E_needed = P_AREAL * T_target_s
d_needed = ((np.pi**2) * C.hbar * C.c / (720.0 * E_needed)) ** (1/3)
PROTON_RADIUS = 0.84e-15  # m, charge radius
print("== HYPOTHETICAL: gap for 10-year reservoir drain at the claim ==")
print(f"  required reservoir: {E_needed:.3e} J/m²")
print(f"  required gap d:     {d_needed:.3e} m  ({d_needed*1e15:.3e} fm)")
print(f"  proton radius:      {PROTON_RADIUS:.3e} m  (gap is {d_needed/PROTON_RADIUS:.1e}× proton radius)")
print(f"  Bohr radius:       ~5.29e-11 m  (gap is {d_needed/5.29e-11:.1e}× Bohr radius — i.e., subatomic)")
print()


# ---------------------- 3. Dynamical Casimir effect ------------------------

omega = 2 * np.pi * 5e9                # 5 GHz cavity
E_photon_5GHz = C.hbar * omega
print("== DCE FEASIBILITY ==")
print(f"  photon energy at 5 GHz:   {E_photon_5GHz:.3e} J")
wilson_flux = 1e5                       # OOM, Wilson et al. 2011
wilson_power = wilson_flux * E_photon_5GHz
print(f"  Wilson 2011 DCE rate:    ~{wilson_flux:.1e} photons/s  ≈ {wilson_power:.3e} W per mode")
mode_area = 1e-12                       # 1 μm² — generous
power_per_mode_needed = P_AREAL * mode_area
ratio = power_per_mode_needed / wilson_power
print(f"  needed per μm² mode:     {power_per_mode_needed:.3e} W")
print(f"  ratio need/demonstrated: {ratio:.3e}")
print(f"  DCE scales as (v/c)² → required v/c ≳ {np.sqrt(ratio):.2g}  (relativistic boundary motion)")
print()


# ---------------------- 4. Thermal context (300 K) -------------------------

T_room = 300.0
sigma_SB = 2*(np.pi**5)*(C.k**4) / (15 * C.h**3 * C.c**2)
P_BB = sigma_SB * T_room**4
print("== THERMAL CONTEXT (300 K) ==")
print(f"  σT⁴ blackbody flux:  {P_BB:.1f} W/m²")
print(f"  claimed areal power: {P_AREAL:.3f} W/m²")
print(f"  ratio claim/σT⁴:     {P_AREAL/P_BB:.3e}")
print("  Note: a passive device in equilibrium with a single-T bath delivers")
print("  zero net work (2nd law). σT⁴ above just sets the radiative scale.")
print()


# ---------------------- 5. Conservativity ---------------------------------

print("== CONSERVATIVITY ==")
print("  Static Casimir force F(d) = -π² ℏ c A / (240 d⁴) = -∂E/∂d.")
print("  Any closed cycle in d nets zero work.")
print("  Pinto-style boundary-property modulation can break conservativity,")
print("  but the modulation drive is itself a power input. The press release")
print("  supplies no energy ledger and no demonstrated mechanism.")
print()


# ------------------------- Convergence / sanity ---------------------------
# Verify our reservoir integral by integrating |F|/A from d to ∞:
# ∫_d^∞ π² ℏ c / (240 x⁴) dx = π² ℏ c / (720 d³).
d_test = 10e-9
x = np.geomspace(d_test, 1e-2, 100000)
F_over_A = (np.pi**2) * C.hbar * C.c / (240.0 * x**4)
E_integral = np.trapezoid(F_over_A, x)
E_closed_form = E_per_area(d_test)
rel_err = abs(E_integral - E_closed_form) / E_closed_form
print("== SANITY: closed-form vs numerical integral ==")
print(f"  closed form |E|/A @ d=10 nm: {E_closed_form:.6e} J/m²")
print(f"  numerical integral:          {E_integral:.6e} J/m²")
print(f"  relative error:              {rel_err:.3e}")
print()


# ----------------------------- Plot ---------------------------------------

if HAVE_PLT:
    d_axis = np.logspace(-10, -6, 200)
    e_axis = E_per_area(d_axis)
    t_axis = e_axis / P_AREAL

    fig, ax1 = plt.subplots(figsize=(7.5, 5))
    ax1.set_xscale("log"); ax1.set_yscale("log")
    ax1.plot(d_axis*1e9, e_axis, color="tab:blue", label="|E|/A reservoir")
    ax1.set_xlabel("plate gap d  (nm)")
    ax1.set_ylabel("|E|/A  (J/m²)", color="tab:blue")
    ax1.tick_params(axis="y", labelcolor="tab:blue")

    ax2 = ax1.twinx()
    ax2.set_yscale("log")
    ax2.plot(d_axis*1e9, t_axis, color="tab:red", linestyle="--",
             label=f"drain time @ {P_AREAL:.2g} W/m²")
    ax2.set_ylabel("drain time (s)", color="tab:red")
    ax2.tick_params(axis="y", labelcolor="tab:red")

    for t_ref, label in [(1.0, "1 s"), (60, "1 min"), (3600, "1 h"),
                         (86400, "1 day"), (T_target_s, "10 yr")]:
        ax2.axhline(t_ref, color="0.7", linewidth=0.5)
        ax2.text(d_axis[0]*1e9 * 1.1, t_ref*1.1, label, fontsize=8, color="0.4")

    ax1.set_title("Casimir static reservoir vs claimed 1.5 W/m² draw")
    fig.tight_layout()
    fig.savefig(OUT / "casimir-reservoir-and-drain-time.png", dpi=150)
    print(f"[plot] {OUT/'casimir-reservoir-and-drain-time.png'}")
else:
    print("[plot] matplotlib unavailable; skipping figure.")


# --------------------------- Verdict --------------------------------------

print()
print("== VERDICT ==")
print("  CONTRADICTED. The 'no degradation, no replacement cycle' continuous-")
print("  power claim is incompatible with: (a) the Casimir static reservoir")
print("  at any physically meaningful gap, (b) the dynamical Casimir effect")
print("  in a passive semiconductor chip, and (c) the second law for a")
print("  passive device in equilibrium with a single-T environment. The")
print("  cited theoretical paper (PRR 2026) does not address energy")
print("  extraction at all. See README §'How company can rebut'.")
