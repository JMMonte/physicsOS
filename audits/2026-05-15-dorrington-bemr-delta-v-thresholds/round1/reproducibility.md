## Re-run output (key numbers extracted, with line references)

I re-ran the sandbox copy with:

```bash
/srv/shared/physicsOS/.venv/bin/python audit_script.py
```

The run completed successfully and reproduced `audit_raw_output.txt` numerically. The only difference is path-local: the re-run wrote outputs under the sandbox `outputs/`, while `audit_raw_output.txt` was captured from the live repo path.

Key extracted numbers:

- Runtime constants: Python 3.12.3, NumPy 2.4.4, SymPy 1.14.0, `g0=9.80665 m/s^2`, Julian year `31557600 s`; constants are defined at audit_script.py:30-31 and printed at audit_script.py:193-198.
- Inputs: `m_dry,total=1250 kg`, `c_l=7469.88 $/kg`, `c_sale=6722.89 $/kg`, `c_prod=300000 $/kg`, `c_p=0 $/kg`, `c_ops=487160 $/yr`, `r=0.20`, `F_T=10 N`; parameter defaults are audit_script.py:34-47, printed at audit_script.py:201-205.
- Zero-delta-v limits: `m0=1250.0 kg`, `mp_total=0.0 kg`, `mp_ae=0.0 kg`, `e1=e2=1.0`, chemical `T=1.000000 yr`, electric `T=0.000000 yr`; computed by audit_script.py:68-87 and printed at audit_script.py:222-225.
- Symbolic residual: `0`; symbolic check is audit_script.py:159-176 and printed at audit_script.py:214-220.
- Thresholds: chemical Eq. (28) zero-profit `1.997280 km/s`; chemical zero-NPV `1.789314 km/s`; electric Eq. (28) zero-profit `13.315197 km/s`; electric zero-NPV max-over-BEMR `4.434973 km/s`, with `BEMR=140.462877`; threshold routines are audit_script.py:110-156 and printed at audit_script.py:228-241.
- Sample NPV checks from the generated CSV: at `delta_v=1.8 km/s`, chemical max NPV is `-396598253.890 USD` at `BEMR=0.001000`; at `delta_v=4.5 km/s`, electric max NPV is `-11842901.963 USD` at `BEMR=136.665505`; at `delta_v=5.0 km/s`, electric max NPV is `-90963215.044 USD` at `BEMR=111.226089`. These are generated at audit_script.py:279-318.

## README/script number-matching results

No numerical mismatches found between `audit_premises_README.md` and the sandbox re-run.

- README conventions/input claim: SI units, `Delta v` in `m/s`, `Isp` in seconds, `v_e=g0 Isp`. Script uses `G0 = scipy.constants.g` at audit_script.py:30, `exhaust_velocity = G0 * Isp` at audit_script.py:60-61, and passes delta-v internally in `m/s`.
- README zero-delta-v limits match script output: `e1=e2=1`, launch mass equals dry mass, propellant mass zero, chemical duration `1 yr`, electric duration `0 yr`. Implemented at audit_script.py:68-87 and printed at audit_script.py:222-225.
- README symbolic equation `y^2-y-q=0`, positive root `(1+sqrt(1+4q))/2`, and zero residual match script lines audit_script.py:159-176 and output.
- README convergence table matches the generated `outputs/electric_threshold_convergence.csv`:
  - `[-2,4]`, `xatol=1e-6`: README `4.434973610 km/s`; CSV `4.434973610448252 km/s`.
  - `[-3,5]`, `xatol=1e-8`: README `4.434972991 km/s`; CSV `4.434972990557981 km/s`.
  - `[-4,6]`, `xatol=1e-10`: README `4.434972991 km/s`; CSV `4.434972990557979 km/s`.
- Claim-statement rounded thresholds are also reproduced within the stated `0.1 km/s` tolerance: chemical `1.789314 km/s -> 1.8 km/s`; electric `4.434973 km/s -> 4.5 km/s`.

## Equation re-derivation (which equation; method; result; agreement)

Re-derived the large-return-mass EBPS threshold equation used for Eq. (28).

From the README's EBPS NPV form, the coefficient of `M_R` is

```text
c_sale/(1+r)^T - (c_l+c_p) [exp(DeltaV_tot/v_e) - exp(DeltaV_EA/v_e)].
```

For Eq. (28), ignore discounting and set `DeltaV_EA = DeltaV_AE = DeltaV`, hence `DeltaV_tot = 2 DeltaV`. Let `y = exp(DeltaV/v_e)` and `q = c_sale/(c_l+c_p)`. Setting the coefficient to zero gives:

```text
c_sale - (c_l+c_p)(y^2-y) = 0
y^2 - y - q = 0
y = (1 + sqrt(1+4q))/2
DeltaV_lim = v_e ln(y).
```

This matches audit_script.py:161-168 exactly.

For the chemical zero-NPV version, `T=2*0.5+0=1 yr` is independent of return mass, so replace `q` by `q/(1+r)^T`. With `c_sale=0.9 c_l`, `c_p=0`, `r=0.2`, `T=1`, `q'=0.9/1.2=0.75`. For `Isp=450 s`, `v_e=9.80665*450=4412.9925 m/s`, so:

```text
y = (1 + sqrt(1+4*0.75))/2 = 1.5
DeltaV = 4412.9925 ln(1.5) = 1789.314481 m/s = 1.789314481 km/s.
```

This agrees with the script's chemical zero-NPV output and with audit_script.py:117-122.

## Convergence / dimensional / convention checks

Convergence check: the electric threshold is stable across the three requested log-BEMR windows and optimizer/root tolerances. The maximum spread is `4.434973610448252 - 4.434972990557979 = 6.19890273e-7 km/s`, far below the claim tolerance. The first row has `max_npv=-114.82 USD` at the root, while the tighter rows are `~2.3e-5 USD`; this is consistent with looser root tolerance, not a threshold shift. The convergence loop is audit_script.py:244-276.

Dimensional chain checked for the electric duration at the limiting point. At `DeltaV=4434.972990557981 m/s`, `Isp=3000 s`, `v_e=29419.95 m/s`, `BEMR=140.462877`, and `m_dry=1250 kg`, the script's mass formulas at audit_script.py:68-76 give `M_R=175578.596 kg`, `e1=1.162702607`, `e2=1.351877352`, `m0=34904.883 kg`, and `m_p,AE=28770.474 kg`. The Table 7 duration terms at audit_script.py:83-87 are:

```text
leg1 = DeltaV*m0/F_T = 4434.972990557981 m/s * 34904.883 kg / 10 N
     = 15480221.297 s

leg2 = DeltaV*(m_dry+M_R+m_p,AE)/F_T
     = 91182632.240 s

T = (leg1+leg2)/31557600 = 3.379941869 yr.
```

Units are correct because `N = kg m s^-2`, so `(m s^-1)*kg/N = s`. No unit error found.

Convention check: README frontmatter says SI, impulsive ideal rocket equation, no metric/Fourier convention; the body says one-way average delta-v with `DeltaV_EA=DeltaV_AE`. The script consistently uses SI `m/s` internally, `km/s` only for printed/root-search presentation, `Isp` in seconds, and `v_e=g0 Isp` at audit_script.py:60-65. Equal-leg convention is explicit in `ebps_masses` at audit_script.py:68-76 via `e1=exp(DeltaV_one_way/v_e)` and `e2=exp(2*DeltaV_one_way/v_e)`, and in the electric duration at audit_script.py:83-87 by using the same one-way delta-v for both legs. The conventions match.

## My independent verdict on the audit

The audit reproduces its numerical outputs in the sandbox, the README's load-bearing numbers match the script and generated CSVs, the central large-return-mass threshold equation is correct under the stated equal-leg EBPS convention, and the electric root is well converged. I found no numerical, dimensional, or convention mismatch.

One minor process note: `audit_raw_output.txt` appears to have been generated from the live repo script path rather than the sandbox copy, as shown by output paths under `/srv/shared/physicsOS/...`; the sandbox re-run writes to `/tmp/.../outputs/`. This is not a numerical discrepancy.

## Final verdict (one of: fully reproduces / numerical discrepancies / equation errors)

fully reproduces
