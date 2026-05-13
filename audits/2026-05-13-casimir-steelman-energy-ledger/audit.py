"""
Steelman energy-ledger audit of a Pinto-style modulated-boundary Casimir engine,
charitably parameterized to match the Casimir Inc. "MicroSparc" claim
(5 mm x 5 mm chip, 1.5 V x 25 uA = 37.5 uW = 1.5 W/m^2 areal).

Claim under audit:
    Under maximally favorable assumptions, can a Pinto-style Casimir engine
    deliver 1.5 W/m^2 of *net* electrical output, with no external power input,
    from a 5 mm x 5 mm chip at ambient temperature?

The energy ledger:

    P_net = eta_collect * (P_extracted_max - P_drive_min)

where
    P_extracted_max:  the absolute upper bound on Casimir work per unit area
                      per cycle, assuming a 100% efficient cycle through
                      "perfect reflector <-> transparent" boundary states.
                      This is bounded by |E_Cas(d)|/A * f_mod.

    P_drive_min:      the unavoidable energy cost per cycle to drive the
                      boundary-property modulation. Two routes are considered:
                        (A) dielectric-loss heating in the modulator material
                            (e.g. InSb, tan delta ~ 0.014-0.017 at THz);
                        (B) latent heat of phase transition for a switchable
                            material (e.g. VO2 metal-insulator transition,
                            DeltaH ~ 45 J/g, T_c ~ 342 K).

Reproducibility:
    Run from the repo root with:

        .venv/bin/python audits/2026-05-13-casimir-steelman-energy-ledger/audit.py

    All intermediate values are printed. Figures and CSVs land in outputs/.

References (load-bearing, see paper notes / claim file):
    - Casimir 1948, KNAW 51, 793.
    - Lamoreaux 1997, PRL 78, 5.
    - Pinto 1999-2003 patents - see papers/1999-pinto-casimir-engine-patents.md
    - Moddel & Dmitriyeva 2019, Atoms 7, 51 - DOI 10.3390/atoms7020051.
    - Scandurra 2001 (no power from cyclic Casimir motion), cited in Moddel-D.
    - Berthier et al. 2008 - VO2 enthalpy ~45 J/g.
    - InSb THz tan delta 0.014-0.017 (Sci Rep 13, 45475-8).
    - White et al. 2026 PRR 8, 013264 - cited claim "theory paper"
      (does not address energy extraction; see paper note).
"""

from __future__ import annotations

import csv
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

# -------------------------------------------------------------------------
# Physical constants and claim parameters
# -------------------------------------------------------------------------
HBAR = C.hbar             # J s
C_LIGHT = C.c             # m/s
KB = C.k                  # J/K
EPS0 = C.epsilon_0        # F/m

# Casimir Inc. claim, transcribed from
# papers/2026-businesswire-casimir-press-release.md
CHIP_SIDE_M = 5e-3                                # 5 mm
CHIP_AREA = CHIP_SIDE_M ** 2                      # 25 mm^2 = 2.5e-5 m^2
CLAIM_V = 1.5                                     # V
CLAIM_I = 25e-6                                   # A
CLAIM_P = CLAIM_V * CLAIM_I                       # 37.5 uW
CLAIM_AREAL = CLAIM_P / CHIP_AREA                 # W/m^2

print()
print("=" * 70)
print("CLAIM PARAMETERS")
print("=" * 70)
print(f"chip area:           {CHIP_AREA:.3e} m^2 ({CHIP_AREA*1e6:.2f} mm^2)")
print(f"claimed P (chip):    {CLAIM_P*1e6:.2f} uW")
print(f"claimed areal P:     {CLAIM_AREAL:.2f} W/m^2")


def casimir_energy_per_area(d):
    """Static Casimir energy magnitude per area for perfect conductor
    parallel plates at T=0. Casimir 1948.

    E/A = - pi^2 hbar c / (720 d^3)

    Returns |E|/A in J/m^2.
    """
    return (np.pi ** 2 * HBAR * C_LIGHT) / (720.0 * d ** 3)


def casimir_pressure(d):
    """Casimir attractive pressure between perfect-conductor plates,
    P = dE/dV per area = pi^2 hbar c / (240 d^4). Units: Pa."""
    return (np.pi ** 2 * HBAR * C_LIGHT) / (240.0 * d ** 4)


# -------------------------------------------------------------------------
# 1. Generosity baseline: full-collapse Casimir reservoir vs cycling
# -------------------------------------------------------------------------
print()
print("=" * 70)
print("STEP 1: Static Casimir reservoir baseline (refresh of prior audit)")
print("=" * 70)

D_TABLE = [1e-9, 1e-8, 1e-7, 1e-6]  # m
print(f"{'gap d':>10s}  {'|E|/A (J/m^2)':>16s}  {'P_Cas (Pa)':>14s}  "
      f"{'drain @1.5 W/m^2':>20s}")
for d in D_TABLE:
    e_area = casimir_energy_per_area(d)
    pcas = casimir_pressure(d)
    drain_s = e_area / CLAIM_AREAL
    print(f"{d*1e9:>8.1f} nm  {e_area:>16.3e}  {pcas:>14.3e}  "
          f"{drain_s*1e3:>16.3e} ms")

# This recovers the prior-audit result. We use d = 100 nm as the company's
# stated cavity gap (per The Debrief writeup, which is the most detailed
# public-source description of the device).
D_NOM = 100e-9
E_AREA_NOM = casimir_energy_per_area(D_NOM)
P_CAS_NOM = casimir_pressure(D_NOM)
print()
print(f"Nominal gap d = {D_NOM*1e9:.0f} nm")
print(f"  |E|/A static = {E_AREA_NOM:.3e} J/m^2")
print(f"  P_Cas        = {P_CAS_NOM:.3e} Pa  ({P_CAS_NOM*1e-3:.2f} kPa)")


# -------------------------------------------------------------------------
# 2. Pinto-style modulated-boundary extracted power
# -------------------------------------------------------------------------
print()
print("=" * 70)
print("STEP 2: Best-case extracted power from boundary-property modulation")
print("=" * 70)

# In a Pinto cycle, the cavity boundary property is modulated between two
# states A and B with different Casimir energies E_A < E_B. Net mechanical
# work extracted per cycle, per area, is at MOST
#   W_extract/A = |E_A - E_B| = f(d) * delta_R
# where delta_R is the swing in plate reflectivity (0 -> 1).
#
# Generous-to-the-claim assumption:
#   delta_R = 1  (full swing perfect-conductor -> transparent),
#   100% efficient collection (eta_collect = 1),
#   no Q-loss in the resonator,
#   no dissipative coupling to load.
#
# Even with delta_R = 1, the BEST cycle extracts at most |E_Cas|/A per cycle.

def pinto_extract_per_area_per_cycle(d, dR):
    """Upper bound on extracted work per unit area per cycle.
    Linear in reflectivity swing dR in [0, 1]; saturates at full Casimir
    energy. This is overly generous: real Lifshitz-formula modulation of a
    finite-conductivity plate gives O(0.1) of the perfect-conductor energy
    even at full optical contrast (Pinto 1999; Iannuzzi et al.)."""
    return casimir_energy_per_area(d) * np.clip(dR, 0.0, 1.0)


F_MOD = 1.0e9  # Hz; 1 GHz modulation: very aggressive for a real material
DR = 1.0       # generous: full reflectivity swing per half-cycle

P_extract_max = pinto_extract_per_area_per_cycle(D_NOM, DR) * F_MOD
print(f"Modulation frequency f_mod = {F_MOD:.1e} Hz")
print(f"Reflectivity swing dR      = {DR}")
print(f"Extracted power upper bound (areal): {P_extract_max:.3e} W/m^2")
print(f"   ... vs claim 1.5 W/m^2:           {P_extract_max/CLAIM_AREAL:.3e} ratio")

# Note: this UPPER bound is already in the same order of magnitude as the
# claim when the modulation frequency is pushed to 1 GHz, simply because the
# 100 nm-gap reservoir per cycle (4.33e-7 J/m^2) is small but the cycle rate
# is high. So this is the regime in which the company's number is at least
# *kinematically thinkable* -- before counting the drive cost.


# -------------------------------------------------------------------------
# 3. Drive-cost A: dielectric-loss heating in a real modulator
# -------------------------------------------------------------------------
print()
print("=" * 70)
print("STEP 3A: Drive cost from dielectric loss (InSb-class modulator)")
print("=" * 70)

# To make the plate reflectivity swing by dR via permittivity modulation,
# the plate's complex dielectric must actually be cycled. There are two
# rigorous lower bounds on the energy cost per cycle:
#
#  (i) "Drude floor" -- the Drude plasma frequency must be cycled across
#      the relevant cavity wavelength. The plasma frequency is set by free
#      carrier density n: omega_p^2 = n*e^2/(eps0*m_eff). To make the plate
#      go from "transparent" (omega_p < omega_cavity) to "reflective"
#      (omega_p > omega_cavity), the carrier density must change by an
#      amount Delta_n on the order of the critical density. For the cavity
#      to support a Casimir mode at d=100 nm, the relevant photon energy is
#      hbar*c/d ~ 2 eV, corresponding to a plasma frequency requirement of
#      n ~ 3e21 /cm^3 = 3e27 /m^3. (This is the "metallic" threshold.)
#      Charging a 50 nm modulator layer to this carrier density requires
#      surface charge sigma = e * Delta_n * h_mod. The electrostatic energy
#      cost stored per chip area is
#         U/A = sigma^2 * h_mod / (2 eps0 eps_r)        [J/m^2],
#      i.e. (energy density inside the capacitor) * (modulator thickness).
#      This is the IRREDUCIBLE work per half-cycle just to put the charge
#      there (and pull it back). [Dimensional bug fixed 2026-05-13 after
#      reproducibility peer review caught the missing h_mod factor.]
#
#  (ii) "Loss-tangent floor" -- once the carrier density swings, the
#       resulting AC dissipation in the modulator is
#         p_loss = (1/2) omega eps0 eps_r tan_delta * E0^2
#       where E0 is the field amplitude in the modulator. We take E0 = the
#       field that actually accomplishes (i), i.e. E0 = sigma/(eps0 eps_r).
#       This is the loss in the modulator alone, not counting external
#       driver inefficiency (added later).
#
# Both floors must be paid. We compute both and use the LARGER as the
# operative minimum cost. (Pinto/Iannuzzi/Esquivel-Sirvent et al. all
# require carrier-density swings of this order to get O(1) reflectivity
# contrast; see Iannuzzi et al. PRL 2003 and Chen et al. PRA 2007.)

eps_r_InSb = 17.0          # static dielectric constant of InSb
tan_delta_InSb = 0.014     # low-loss end of InSb THz range (Sci Rep 2023)
h_mod = 50e-9              # modulator layer thickness, 50 nm (thin film)

# Casimir energy volumetric density inside the cavity (only used for ref)
u_cas_volumetric = E_AREA_NOM / D_NOM       # J/m^3
print(f"Casimir energy density at d=100 nm: u_Cas = {u_cas_volumetric:.3e} J/m^3")

# Floor (i): Drude carrier-swing electrostatic energy
# Critical plasma carrier density to make plate reflective at cavity-relevant
# photon energy. For d = 100 nm, the lowest cavity-mode photon energy is
# omega_cavity ~ pi c / d, so the plasma frequency needed satisfies
# omega_p >= omega_cavity. We take Delta_n equal to that critical density.
omega_cavity = np.pi * C_LIGHT / D_NOM      # ~9.4e15 rad/s for 100 nm
m_eff_InSb = 0.014 * C.m_e                  # InSb effective mass
Delta_n = EPS0 * m_eff_InSb * omega_cavity ** 2 / C.e ** 2
print(f"Cavity-mode angular freq omega_cavity = {omega_cavity:.3e} rad/s")
print(f"Required carrier swing Delta_n        = {Delta_n:.3e} /m^3  "
      f"({Delta_n * 1e-6:.3e} /cm^3)")

# Surface charge needed across the 50 nm layer
sigma_surf = C.e * Delta_n * h_mod          # C/m^2
print(f"Surface charge needed per cycle   sigma = {sigma_surf:.3e} C/m^2")

# Electrostatic energy stored in the modulator capacitor (per chip area,
# per half-cycle, linear-dielectric limit). The energy density inside the
# capacitor is sigma^2 / (2 eps0 eps_r) [J/m^3]; integrating over the
# modulator thickness h_mod gives the areal energy [J/m^2].
U_capacitor_per_area = sigma_surf ** 2 * h_mod / (2.0 * EPS0 * eps_r_InSb)
print(f"Electrostatic energy stored per cycle per area: "
      f"U = {U_capacitor_per_area:.3e} J/m^2")

# This energy is recovered at the end of each half-cycle in the ideal limit,
# but the driver-amp/oscillator efficiency loss eats a fraction each pass.
# For a real RF oscillator, losses are typically O(1) -- assume 50% recovery
# (the rest dissipates), so the per-cycle loss is U/2.
osc_recovery = 0.5
P_drive_drude = (1.0 - osc_recovery) * U_capacitor_per_area * 2.0 * F_MOD
# factor 2 because we charge+discharge per cycle
print(f"Drive cost (Drude floor) per chip area: "
      f"P_drude = {P_drive_drude:.3e} W/m^2")
print(f"   ... vs claim:        {P_drive_drude/CLAIM_AREAL:.3e} ratio")
print(f"   ... vs extracted:    {P_drive_drude/P_extract_max:.3e} ratio")

# Floor (ii): in-modulator dielectric dissipation at the same field
# amplitude that produced the carrier swing.
E0_drive = sigma_surf / (EPS0 * eps_r_InSb)         # V/m, field that holds sigma
print(f"Required drive E-field amplitude E0 = {E0_drive:.3e} V/m  "
      f"({E0_drive*h_mod:.3e} V across {h_mod*1e9:.0f} nm)")
# Sanity-check vs InSb breakdown field (~1e6 V/m for thin films) and the
# free-air breakdown field (3e6 V/m).
print(f"   ... InSb breakdown ~ 1e6 V/m; air breakdown ~ 3e6 V/m")
print(f"   ... E0 / InSb-breakdown ratio: {E0_drive / 1e6:.3e}")

omega = 2 * np.pi * F_MOD
p_loss_volumetric = 0.5 * omega * EPS0 * eps_r_InSb * tan_delta_InSb * E0_drive ** 2
P_drive_areal_diel = p_loss_volumetric * h_mod
print(f"Dielectric-loss heating per chip area:")
print(f"   p_loss volumetric = {p_loss_volumetric:.3e} W/m^3")
print(f"   P_drive areal     = {P_drive_areal_diel:.3e} W/m^2")
print(f"   ... vs claim:        {P_drive_areal_diel/CLAIM_AREAL:.3e} ratio")
print(f"   ... vs extracted:    {P_drive_areal_diel/P_extract_max:.3e} ratio")


# -------------------------------------------------------------------------
# 4. Drive-cost B: latent heat of phase transition (VO2-class modulator)
# -------------------------------------------------------------------------
print()
print("=" * 70)
print("STEP 3B: Drive cost from phase-transition latent heat (VO2)")
print("=" * 70)

# VO2 MIT enthalpy: 45 J/g, density 4.34 g/cm^3, so volumetric latent heat
# dH = 45 * 4.34e6 J/m^3 = 1.95e8 J/m^3. Cycling at f_mod through the
# transition twice per cycle imposes an irreducible thermal cost of
#   p_VO2 = 2 * f_mod * dH * h_mod  [W/m^2 chip area]
# (assuming the entire 50 nm modulator layer is driven through the
# transition each half-cycle).
rho_VO2 = 4340.0           # kg/m^3
dH_per_kg = 45.0e3         # J/kg = 45 J/g
dH_volumetric = rho_VO2 * dH_per_kg
print(f"VO2 phase-transition enthalpy density: dH = {dH_volumetric:.3e} J/m^3")
P_drive_areal_VO2 = 2.0 * F_MOD * dH_volumetric * h_mod
print(f"P_drive areal (VO2 cycling at f_mod): {P_drive_areal_VO2:.3e} W/m^2")
print(f"   ... vs claim:                       {P_drive_areal_VO2/CLAIM_AREAL:.3e} ratio")
print(f"   ... vs extracted:                   {P_drive_areal_VO2/P_extract_max:.3e} ratio")

# Sanity: a VO2 modulator cycled at 1 GHz is ALREADY physically impossible --
# the thermal relaxation time of a 50 nm VO2 film is microseconds, not
# nanoseconds, so it cannot actually be cycled at GHz. We are giving the
# claim every benefit of the doubt by computing the steady-state energy
# cost as if the cycling were possible.


# -------------------------------------------------------------------------
# 5. Ohmic-loss floor for an electrical driver
# -------------------------------------------------------------------------
print()
print("=" * 70)
print("STEP 3C: Ohmic-loss floor for an electrical driver")
print("=" * 70)

# If the drive is an RF or DC bias, the driver electronics have a minimum
# quiescent power. Real RF GHz oscillators driving impedance-matched loads
# have wall-plug-to-RF efficiencies of 10-50%. Assuming 50% (best class-D),
# even if the AC drive could be made loss-free at the cavity, the chip
# electronics burn at least P_drive_areal_diel * 2 to run the oscillator.
#
# We skip the explicit calc -- this floor is a constant multiplier on the
# above and only worsens the ratio. Recorded for completeness.
osc_efficiency = 0.5
print(f"GHz oscillator efficiency floor: {osc_efficiency*100:.0f}%")
print(f"   ... at most ~2x penalty on P_drive_areal_diel.")
print(f"   ... already dominated by the dielectric/latent-heat term above.")


# -------------------------------------------------------------------------
# 6. Net power and sensitivity sweep
# -------------------------------------------------------------------------
print()
print("=" * 70)
print("STEP 4: Net power and sensitivity sweep")
print("=" * 70)

P_drive_best = min(P_drive_drude, P_drive_areal_diel, P_drive_areal_VO2)
P_net = P_extract_max - P_drive_best
print(f"P_extract_max         = {P_extract_max:.3e} W/m^2")
print(f"P_drive (Drude floor) = {P_drive_drude:.3e} W/m^2")
print(f"P_drive (diel loss)   = {P_drive_areal_diel:.3e} W/m^2")
print(f"P_drive (VO2 latent)  = {P_drive_areal_VO2:.3e} W/m^2")
print(f"P_drive_best (min)    = {P_drive_best:.3e} W/m^2")
print(f"P_net (best of)       = {P_net:.3e} W/m^2")
print(f"P_net / claim         = {P_net/CLAIM_AREAL:.3e}")

# Sweep: vary d_nom, f_mod, dR, h_mod; tabulate net to outputs/sensitivity.csv
print()
print("--- Sensitivity sweep ---")
sweep_rows = []
for d_nm in [10, 30, 100, 300, 1000]:
    for f_ghz in [0.1, 1.0, 10.0]:
        for dR_ in [0.1, 0.5, 1.0]:
            d_ = d_nm * 1e-9
            f_ = f_ghz * 1e9
            omega_ = 2 * np.pi * f_
            E_area_ = casimir_energy_per_area(d_)
            P_ext_ = E_area_ * dR_ * f_

            # Drude floor at this gap
            omega_cav_ = np.pi * C_LIGHT / d_
            Delta_n_ = EPS0 * m_eff_InSb * omega_cav_ ** 2 / C.e ** 2
            sigma_ = C.e * Delta_n_ * h_mod
            U_cap_ = sigma_ ** 2 * h_mod / (2.0 * EPS0 * eps_r_InSb)
            P_drude_ = (1.0 - osc_recovery) * U_cap_ * 2.0 * f_

            # Dielectric-loss floor at the field producing that swing
            E0_ = sigma_ / (EPS0 * eps_r_InSb)
            p_loss_vol_ = 0.5 * omega_ * EPS0 * eps_r_InSb * tan_delta_InSb * E0_ ** 2
            P_diel_ = p_loss_vol_ * h_mod

            # VO2 latent heat floor (gap-independent: cost is in the modulator)
            P_VO2_ = 2.0 * f_ * dH_volumetric * h_mod

            P_drive_ = min(P_drude_, P_diel_, P_VO2_)
            P_net_ = P_ext_ - P_drive_
            sweep_rows.append({
                "d_nm": d_nm, "f_GHz": f_ghz, "dR": dR_,
                "P_ext_W_per_m2": P_ext_,
                "P_drive_drude_W_per_m2": P_drude_,
                "P_drive_diel_W_per_m2": P_diel_,
                "P_drive_VO2_W_per_m2": P_VO2_,
                "P_net_W_per_m2": P_net_,
            })

csv_path = OUT / "sensitivity.csv"
with open(csv_path, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(sweep_rows[0].keys()))
    w.writeheader()
    for row in sweep_rows:
        w.writerow({k: (f"{v:.6e}" if isinstance(v, float) else v)
                    for k, v in row.items()})

# Print a compact summary: best (most positive) net in the sweep
sweep_rows.sort(key=lambda r: r["P_net_W_per_m2"], reverse=True)
print("Top-5 most-favorable parameter choices in the sweep:")
print(f"{'d nm':>5s} {'f GHz':>6s} {'dR':>4s}  {'P_ext':>11s}  {'P_drive':>11s}  {'P_net':>11s}")
for row in sweep_rows[:5]:
    print(f"{row['d_nm']:>5d} {row['f_GHz']:>6.2f} {row['dR']:>4.2f}  "
          f"{row['P_ext_W_per_m2']:>11.3e}  "
          f"{min(row['P_drive_diel_W_per_m2'], row['P_drive_VO2_W_per_m2']):>11.3e}  "
          f"{row['P_net_W_per_m2']:>11.3e}")
print(f"[wrote sensitivity.csv -> {csv_path}]")


# -------------------------------------------------------------------------
# 7. Make the headline figure
# -------------------------------------------------------------------------
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Plot: extracted vs drive vs net, as f_mod swept at d=100 nm, dR=1
f_mod_arr = np.logspace(7, 11, 200)  # 10 MHz to 100 GHz
omega_arr = 2 * np.pi * f_mod_arr
P_ext_arr = E_AREA_NOM * DR * f_mod_arr

# Drude floor (gap-fixed at D_NOM)
omega_cav_nom = np.pi * C_LIGHT / D_NOM
Delta_n_nom = EPS0 * m_eff_InSb * omega_cav_nom ** 2 / C.e ** 2
sigma_nom = C.e * Delta_n_nom * h_mod
U_cap_nom = sigma_nom ** 2 / (2.0 * EPS0 * eps_r_InSb)
P_drude_arr = (1.0 - osc_recovery) * U_cap_nom * 2.0 * f_mod_arr

# Dielectric-loss floor at field producing the swing
E0_arr_nom = sigma_nom / (EPS0 * eps_r_InSb)
p_loss_vol_arr = 0.5 * omega_arr * EPS0 * eps_r_InSb * tan_delta_InSb * E0_arr_nom ** 2
P_diel_arr = p_loss_vol_arr * h_mod

# VO2 latent-heat floor
P_VO2_arr = 2.0 * f_mod_arr * dH_volumetric * h_mod

P_drive_arr = np.minimum(np.minimum(P_drude_arr, P_diel_arr), P_VO2_arr)
P_net_arr = P_ext_arr - P_drive_arr

fig, ax = plt.subplots(figsize=(8, 5))
ax.loglog(f_mod_arr, P_ext_arr, "b-", lw=2,
          label="P_extracted (upper bound, dR=1)")
ax.loglog(f_mod_arr, P_drude_arr, "m-", lw=1.5,
          label="P_drive (Drude carrier swing)")
ax.loglog(f_mod_arr, P_diel_arr, "r--", lw=1.5,
          label=f"P_drive (InSb dielectric loss tan d={tan_delta_InSb})")
ax.loglog(f_mod_arr, P_VO2_arr, "g--", lw=1.5,
          label="P_drive (VO2 latent heat)")
ax.axhline(CLAIM_AREAL, color="k", lw=1, ls=":",
           label=f"Casimir Inc. claim ({CLAIM_AREAL:.1f} W/m^2)")
ax.set_xlabel("Modulation frequency f_mod (Hz)")
ax.set_ylabel("Power per chip area (W/m^2)")
ax.set_title(f"Steelman Casimir-engine ledger, d={D_NOM*1e9:.0f} nm, "
             f"dR={DR:.1f}, h_mod={h_mod*1e9:.0f} nm")
ax.legend(loc="lower right", fontsize=8)
ax.grid(True, which="both", alpha=0.3)
fig.tight_layout()
fig_path = OUT / "ledger_vs_fmod.png"
fig.savefig(fig_path, dpi=140)
plt.close(fig)
print(f"[wrote {fig_path}]")


# -------------------------------------------------------------------------
# 8. Dimensional check (machine-readable, with pint)
# -------------------------------------------------------------------------
print()
print("=" * 70)
print("STEP 5: Dimensional check (pint)")
print("=" * 70)
import pint
ureg = pint.UnitRegistry()
hbar_q = HBAR * ureg.joule * ureg.second
c_q = C_LIGHT * ureg.meter / ureg.second
d_q = D_NOM * ureg.meter
E_per_A_q = (np.pi ** 2 * hbar_q * c_q) / (720 * d_q ** 3)
print(f"E/A pint check: {E_per_A_q.to(ureg.joule / ureg.meter ** 2):~P}")
assert E_per_A_q.dimensionality == (ureg.joule / ureg.meter ** 2).dimensionality

eps0_q = EPS0 * ureg.farad / ureg.meter
E0_q = E0_drive * ureg.volt / ureg.meter
omega_q = omega * ureg.hertz
p_loss_q = 0.5 * omega_q * eps0_q * eps_r_InSb * tan_delta_InSb * E0_q ** 2
print(f"p_loss pint: {p_loss_q.to(ureg.watt / ureg.meter ** 3):~P}")
assert p_loss_q.to(ureg.watt / ureg.meter ** 3).magnitude > 0


# -------------------------------------------------------------------------
# 9. Verdict
# -------------------------------------------------------------------------
print()
print("=" * 70)
print("VERDICT")
print("=" * 70)
print(f"At the most favorable single-point parameters (d=100 nm, f=1 GHz,")
print(f"dR=1, h_mod=50 nm), with three independent drive-cost lower bounds:")
print(f"   P_extracted    = {P_extract_max:.3e} W/m^2")
print(f"   P_drive(Drude) = {P_drive_drude:.3e} W/m^2")
print(f"   P_drive(diel)  = {P_drive_areal_diel:.3e} W/m^2")
print(f"   P_drive(VO2)   = {P_drive_areal_VO2:.3e} W/m^2")
print(f"   P_drive_min    = {P_drive_best:.3e} W/m^2")
print(f"   P_net (best)   = {P_net:.3e} W/m^2")
print(f"   claim          = {CLAIM_AREAL:.3e} W/m^2")
print()
print(f"Drive cost / extracted power ratio = "
      f"{P_drive_best / P_extract_max:.3e}")
print()
print(f"--- The Drude-floor sanity check ---")
print(f"E0 field needed across the 50 nm modulator: {E0_drive:.3e} V/m")
print(f"This is {E0_drive/3e6:.3e}x the breakdown field of air (3e6 V/m)")
print(f"and exceeds the breakdown field of bulk InSb (~1e6 V/m) by ~{E0_drive/1e6:.0e}x.")
print(f"The modulator would arc / vaporize long before this field can be sustained.")
print()
print("Sensitivity sweep: across 5x3x3 = 45 (d, f, dR) combinations,")
print(f"the maximum net areal power is {sweep_rows[0]['P_net_W_per_m2']:.3e} W/m^2.")

# Now check: how many sweep points yield net > claim?
positives = [r for r in sweep_rows if r["P_net_W_per_m2"] > 0]
above_claim = [r for r in sweep_rows if r["P_net_W_per_m2"] > CLAIM_AREAL]
print(f"# sweep points with P_net > 0:        {len(positives)} / {len(sweep_rows)}")
print(f"# sweep points with P_net > claim:    {len(above_claim)} / {len(sweep_rows)}")

if above_claim:
    print()
    print("WARNING: The sweep shows some apparently feasible regions.")
    print("Examine outputs/sensitivity.csv. Note that the Drude/diel/VO2")
    print("floors are INDEPENDENT lower bounds; the operative cost is whichever")
    print("is LARGEST, not smallest. We took min for the steelman, which is")
    print("intentionally over-generous. The 'most-favorable' rows are the")
    print("ones where the smallest of three loss mechanisms happens to be")
    print("small -- but the actual experiment pays all three.")
    print()
    print("To check the *honest* ledger, recompute with P_drive = max():")
    for r in sweep_rows[:5]:
        P_drive_honest = max(r["P_drive_drude_W_per_m2"],
                             r["P_drive_diel_W_per_m2"],
                             r["P_drive_VO2_W_per_m2"])
        P_net_honest = r["P_ext_W_per_m2"] - P_drive_honest
        print(f"   d={r['d_nm']:>4d}nm f={r['f_GHz']:>5.2f}GHz dR={r['dR']:.2f}: "
              f"P_ext={r['P_ext_W_per_m2']:.2e}, "
              f"P_drive_max={P_drive_honest:.2e}, "
              f"P_net_honest={P_net_honest:.2e} W/m^2")
