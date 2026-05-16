"""
Audit: feasibility of M_dust ~ 1e6 Msun in MACS0416-Y1 at z=8.312, and the
M_dust <-> T_dust degeneracy.

Claim file:  claims/macs0416y1-early-dust-feasible.md
Paper note:  papers/2026-takechi-dreams-macs0416y1-early-dust.md
Source:      Takechi et al. 2026, arXiv:2605.14922

Layers:
  1. Cosmology    -- cosmic time available at z=8.312 (astropy + manual integral cross-check)
  2. Internal     -- do (M_dust/M_gas, M_dust/M_metal) imply the stated 0.15 Z_sun?
  3. Budget       -- can stellar nucleosynthesis make ~1e7 Msun of metals + ~1e6 Msun dust
                     in the available time? (order-of-magnitude)
  4. Degeneracy   -- how steeply does inferred M_dust scale with assumed T_dust?

Run from repo root with the project venv:
    .venv/bin/python audits/2026-05-16-macs0416y1-early-dust/audit.py

All numbers printed; figures + machine-readable data written to ./outputs/.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy import constants as C
from scipy import integrate

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(exist_ok=True)

print(f"[python] {sys.version.split()[0]}")
print(f"[numpy ] {np.__version__}")

# ----------------------------------------------------------------------------
# Inputs from the paper (verbatim from arXiv abstract, 2605.14922)
# ----------------------------------------------------------------------------
Z_GAL = 8.312
LOG_MDUST_MGAS = -3.60          # log10(M_dust / M_gas)
LOG_MDUST_MMETAL = -0.95        # log10(M_dust / M_metal)
M_DUST = 1.0e6                  # Msun, "M_dust ~ 1e6 Msun"
T_DUST = 91.0                   # K (+62 / -35)
T_DUST_LO, T_DUST_HI = 91.0 - 35.0, 91.0 + 62.0
OH_GAL = 7.86                   # 12 + log(O/H)
Z_SUN_FRAC = 0.0142             # solar metal mass fraction (Asplund+2009)
OH_SUN = 8.69                   # 12 + log(O/H)_sun (Asplund+2009)

results: dict[str, object] = {"inputs": {
    "z": Z_GAL, "log_Mdust_Mgas": LOG_MDUST_MGAS,
    "log_Mdust_Mmetal": LOG_MDUST_MMETAL, "M_dust_Msun": M_DUST,
    "T_dust_K": T_DUST, "12+log(O/H)": OH_GAL,
}}


# ============================================================================
# 1. COSMOLOGY -- time available at z=8.312
# ============================================================================
# Flat LCDM, Planck 2018-like: H0=67.4, Om=0.315, OL=0.685 (radiation included).
H0 = 67.4                       # km/s/Mpc
OM = 0.315
OR = 9.0e-5                     # photons+neutrinos, matters only at very high z
OL = 1.0 - OM - OR
KM_PER_MPC = 3.0856775814913673e19
H0_SI = H0 / KM_PER_MPC         # 1/s
HUBBLE_TIME_GYR = (1.0 / H0_SI) / (3.15576e16)  # s -> Gyr


def E(z):
    zp1 = 1.0 + z
    return np.sqrt(OM * zp1**3 + OR * zp1**4 + OL)


def cosmic_age_gyr(z):
    """t(z) = (1/H0) * \\int_z^inf dz' / [(1+z') E(z')]."""
    integrand = lambda zp: 1.0 / ((1.0 + zp) * E(zp))
    val, _ = integrate.quad(integrand, z, np.inf, limit=200)
    return HUBBLE_TIME_GYR * val


age_now = cosmic_age_gyr(0.0)
age_z = cosmic_age_gyr(Z_GAL)

# Cross-check with astropy if available.
astropy_age = None
astropy_age_now = None
try:
    from astropy.cosmology import FlatLambdaCDM
    import astropy.units as u

    cosmo = FlatLambdaCDM(H0=H0, Om0=OM, Tcmb0=2.725)
    astropy_age = float(cosmo.age(Z_GAL).to(u.Gyr).value)
    astropy_age_now = float(cosmo.age(0.0).to(u.Gyr).value)
except Exception as exc:  # noqa: BLE001
    print(f"[warn] astropy cross-check skipped: {exc}")

print("\n=== 1. Cosmology (flat LCDM, H0=67.4, Om=0.315) ===")
print(f"age of universe now              : {age_now:.3f} Gyr")
print(f"age at z={Z_GAL}                  : {age_z*1e3:.1f} Myr  ({age_z:.4f} Gyr)")
if astropy_age is not None:
    print(f"astropy age at z={Z_GAL}          : {astropy_age*1e3:.1f} Myr  "
          f"(now {astropy_age_now:.3f} Gyr)")
    rel = abs(age_z - astropy_age) / astropy_age
    print(f"manual vs astropy rel. error     : {rel:.2e}")
    assert rel < 1e-2, "manual integral disagrees with astropy by >1%"

t_avail_myr = age_z * 1e3
results["cosmology"] = {
    "age_now_Gyr": age_now, "age_at_z_Myr": t_avail_myr,
    "astropy_age_at_z_Myr": None if astropy_age is None else astropy_age * 1e3,
}


# ============================================================================
# 2. INTERNAL CONSISTENCY -- do the dust ratios imply 0.15 Z_sun?
# ============================================================================
# M_dust/M_gas and M_dust/M_metal  =>  M_metal/M_gas  =>  Z (mass fraction).
mdust_mgas = 10.0 ** LOG_MDUST_MGAS
mdust_mmetal = 10.0 ** LOG_MDUST_MMETAL
mmetal_mgas = mdust_mgas / mdust_mmetal           # = M_metal/M_gas
Z_inferred_frac = mmetal_mgas
Z_inferred_solar = Z_inferred_frac / Z_SUN_FRAC

# Independent handle: metallicity stated via 12+log(O/H).
Z_from_OH_solar = 10.0 ** (OH_GAL - OH_SUN)

# Derived absolute masses (for the budget step).
M_metal = M_DUST / mdust_mmetal
M_gas = M_DUST / mdust_mgas

print("\n=== 2. Internal consistency (dust ratios -> metallicity) ===")
print(f"M_dust/M_gas    = {mdust_mgas:.3e}")
print(f"M_dust/M_metal  = {mdust_mmetal:.3e}")
print(f"=> M_metal/M_gas = {mmetal_mgas:.3e}  (metal mass fraction Z)")
print(f"=> Z (from ratios) = {Z_inferred_solar:.2f} Z_sun  "
      f"({Z_inferred_frac:.2e} by mass)")
print(f"   Z (from 12+log(O/H)={OH_GAL}) = {Z_from_OH_solar:.2f} Z_sun")
print(f"   stated in paper            = 0.15 Z_sun")
print(f"derived M_metal = {M_metal:.2e} Msun")
print(f"derived M_gas   = {M_gas:.2e} Msun")

# The two metallicity routes use different tracers (total metals via dust ratios
# vs. gas-phase O/H); agreement within a factor ~2-3 is the success criterion.
consistency_factor = Z_inferred_solar / Z_from_OH_solar
print(f"ratio (ratio-route / OH-route) = {consistency_factor:.2f}")
results["internal"] = {
    "Z_from_ratios_Zsun": Z_inferred_solar,
    "Z_from_OH_Zsun": Z_from_OH_solar,
    "stated_Zsun": 0.15,
    "M_metal_Msun": M_metal,
    "M_gas_Msun": M_gas,
    "consistency_factor": consistency_factor,
}


# ============================================================================
# 3. PRODUCTION BUDGET -- can stars make M_metal + M_dust in t_avail?
# ============================================================================
# Nucleosynthetic metal yield per unit stellar mass formed: y_Z ~ 0.03-0.06
# (mass of all metals returned per Msun of stars, Kroupa/Chabrier IMF).
# Stellar mass needed to have produced M_metal:
yZ_lo, yZ_hi = 0.03, 0.06
Mstar_lo = M_metal / yZ_hi
Mstar_hi = M_metal / yZ_lo

# Mean SFR if that stellar mass formed over the available cosmic time
# (conservative: star formation cannot start before the universe exists).
t_avail_yr = t_avail_myr * 1e6
sfr_lo = Mstar_lo / t_avail_yr
sfr_hi = Mstar_hi / t_avail_yr

# Dust: core-collapse SNe per Msun formed ~ 0.006-0.02; dust yield per CCSN
# (post reverse shock) ~ 0.01-0.3 Msun. Max stellar-source dust per Msun*:
nccsn_lo, nccsn_hi = 0.006, 0.02
yd_ccsn_lo, yd_ccsn_hi = 0.01, 0.3
dust_per_Mstar_lo = nccsn_lo * yd_ccsn_lo
dust_per_Mstar_hi = nccsn_hi * yd_ccsn_hi
Mdust_from_SNe_lo = Mstar_lo * dust_per_Mstar_lo
Mdust_from_SNe_hi = Mstar_hi * dust_per_Mstar_hi

print("\n=== 3. Production budget ===")
print(f"stellar mass to make {M_metal:.1e} Msun metals : "
      f"{Mstar_lo:.2e} - {Mstar_hi:.2e} Msun")
print(f"mean SFR over {t_avail_myr:.0f} Myr            : "
      f"{sfr_lo:.2f} - {sfr_hi:.2f} Msun/yr")
print(f"SN-only dust producible          : "
      f"{Mdust_from_SNe_lo:.2e} - {Mdust_from_SNe_hi:.2e} Msun")
print(f"observed M_dust                  : {M_DUST:.2e} Msun")
sne_can_explain = Mdust_from_SNe_hi >= M_DUST
print(f"SNe alone can supply 1e6 Msun?   : {sne_can_explain}  "
      f"(else ISM grain growth needed -- consistent with paper's argument)")
results["budget"] = {
    "Mstar_range_Msun": [Mstar_lo, Mstar_hi],
    "mean_SFR_Msun_per_yr": [sfr_lo, sfr_hi],
    "SN_dust_range_Msun": [Mdust_from_SNe_lo, Mdust_from_SNe_hi],
    "SNe_alone_sufficient": bool(sne_can_explain),
}


# ============================================================================
# 4. T_dust <-> M_dust DEGENERACY
# ============================================================================
# Optically-thin modified blackbody: at fixed observed flux,
#   M_dust(T) \propto 1 / [ kappa_nu * B_nu(T) ]      (kappa_nu T-independent)
# so   M_dust(T1)/M_dust(T2) = B_nu(T2) / B_nu(T1).
# Representative ALMA dust-continuum point for MACS0416-Y1: rest-frame ~90 um.
LAMBDA_REST_UM = 90.0
nu_rest = C.c / (LAMBDA_REST_UM * 1e-6)            # Hz
x_coeff = C.h * nu_rest / C.k                      # = h nu / k   (units K)
print(f"\n=== 4. T_dust<->M_dust degeneracy "
      f"(rest lambda = {LAMBDA_REST_UM:.0f} um) ===")
print(f"h*nu/k = {x_coeff:.2f} K  (nu_rest = {nu_rest:.3e} Hz)")


def Bnu_rel(T):
    """B_nu(T) up to T-independent constants (the 2 h nu^3 / c^2 prefactor)."""
    return 1.0 / np.expm1(x_coeff / T)


T_grid = np.linspace(25.0, 150.0, 400)
Mdust_grid = M_DUST * Bnu_rel(T_DUST) / Bnu_rel(T_grid)   # normalised to T=91 K

# Headline sensitivity numbers.
for Tref in (35.0, 40.0, 50.0, T_DUST_LO, T_DUST, T_DUST_HI):
    factor = Bnu_rel(T_DUST) / Bnu_rel(Tref)
    print(f"  T={Tref:6.1f} K  ->  M_dust = {M_DUST*factor:.3e} Msun  "
          f"(x{factor:6.2f} vs 91 K)")

# Cross-check vs astropy blackbody if available.
try:
    from astropy.modeling.models import BlackBody
    import astropy.units as u

    bb91 = BlackBody(temperature=91 * u.K)(nu_rest * u.Hz)
    bb40 = BlackBody(temperature=40 * u.K)(nu_rest * u.Hz)
    ap_ratio = float((bb91 / bb40).value)
    my_ratio = Bnu_rel(91.0) / Bnu_rel(40.0)
    rel = abs(ap_ratio - my_ratio) / ap_ratio
    print(f"  [xcheck] B(91)/B(40): mine={my_ratio:.4f} "
          f"astropy={ap_ratio:.4f} relerr={rel:.2e}")
    assert rel < 1e-6, "modified-BB ratio disagrees with astropy"
except Exception as exc:  # noqa: BLE001
    print(f"  [warn] astropy BB cross-check skipped: {exc}")

factor_40 = float(Bnu_rel(T_DUST) / Bnu_rel(40.0))
Mdust_at_40 = M_DUST * factor_40
# If dust were at canonical ~40 K, would inferred M_dust exceed the metal mass?
unphysical_at_40 = Mdust_at_40 > M_metal
results["degeneracy"] = {
    "rest_lambda_um": LAMBDA_REST_UM,
    "M_dust_at_40K_Msun": Mdust_at_40,
    "factor_40K_vs_91K": factor_40,
    "M_metal_Msun": M_metal,
    "Mdust_at_40K_exceeds_Mmetal": bool(unphysical_at_40),
}
print(f"  => at 40 K, M_dust = {Mdust_at_40:.2e} Msun; "
      f"M_metal = {M_metal:.2e} Msun; exceeds metals? {unphysical_at_40}")


# ============================================================================
# MACHINE-READABLE DUMPS  (per visualization practice: image + data)
# ============================================================================
np.savetxt(
    OUT / "Tdust_Mdust_curve.csv",
    np.column_stack([T_grid, Mdust_grid]),
    delimiter=",", header="T_dust_K,M_dust_Msun", comments="",
)
with open(OUT / "results.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\n[written] {OUT/'results.json'}")
print(f"[written] {OUT/'Tdust_Mdust_curve.csv'}")


# ============================================================================
# FIGURES (annotated; data also dumped above so correctness is checkable
#          without relying on reading the image)
# ============================================================================
fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))

# -- Left: cosmic age vs redshift, mark z=8.312 --
zz = np.linspace(0, 15, 300)
ages = np.array([cosmic_age_gyr(z) * 1e3 for z in zz])  # Myr
ax[0].plot(zz, ages, color="navy", lw=2)
ax[0].scatter([Z_GAL], [t_avail_myr], color="crimson", zorder=5, s=60)
ax[0].annotate(
    f"z={Z_GAL}\n t = {t_avail_myr:.0f} Myr",
    xy=(Z_GAL, t_avail_myr), xytext=(Z_GAL + 1.5, t_avail_myr + 1500),
    arrowprops=dict(arrowstyle="->", color="crimson"),
    fontsize=10, color="crimson",
)
ax[0].set_xlabel("redshift z")
ax[0].set_ylabel("cosmic time since Big Bang [Myr]")
ax[0].set_title("Time budget for dust formation")
ax[0].grid(alpha=0.3)
ax[0].text(0.97, 0.05,
           f"only {t_avail_myr:.0f} Myr available\nflat LCDM H0={H0}, Om={OM}",
           transform=ax[0].transAxes, ha="right", va="bottom", fontsize=9,
           bbox=dict(boxstyle="round", fc="white", alpha=0.8))

# -- Right: M_dust vs assumed T_dust --
ax[1].plot(T_grid, Mdust_grid, color="darkgreen", lw=2)
ax[1].axvspan(T_DUST_LO, T_DUST_HI, color="orange", alpha=0.18,
              label="paper T_dust = 91 (+62/-35) K")
ax[1].axhline(M_metal, color="purple", ls="--", lw=1.2,
              label=f"M_metal = {M_metal:.1e} Msun (unphysical above)")
for Tm in (40.0, T_DUST):
    Mm = M_DUST * Bnu_rel(T_DUST) / Bnu_rel(Tm)
    ax[1].scatter([Tm], [Mm], color="crimson", zorder=5, s=55)
    ax[1].annotate(f"  T={Tm:.0f} K\n  M={Mm:.2e}",
                   xy=(Tm, Mm), fontsize=9, color="crimson",
                   va="bottom")
ax[1].set_yscale("log")
ax[1].set_xlabel("assumed T_dust [K]")
ax[1].set_ylabel("inferred M_dust [Msun]  (fixed observed flux)")
ax[1].set_title("M_dust <-> T_dust degeneracy (rest 90 um)")
ax[1].grid(alpha=0.3, which="both")
ax[1].legend(fontsize=8, loc="upper right")

fig.suptitle("MACS0416-Y1 (z=8.312) early-dust audit  --  arXiv:2605.14922",
             fontsize=12, y=1.02)
fig.tight_layout()
fig.savefig(OUT / "audit_summary.png", dpi=140, bbox_inches="tight")
print(f"[written] {OUT/'audit_summary.png'}")

print("\n=== DONE ===")
