# Espresso chiller — parametric engineering model

Parametric model of the inline espresso chiller (helically coiled 3.0 × 0.7 mm
316L tube, 80 mm coil, stirred propylene-glycol bath at +1 °C), validated
against the completed design study, then extended to the real installation: a
La Marzocco Strada X with **three group heads and three independent coils in
one shared bath**.

## How to run

```
cd "/Users/brandonacuna/Espresso Chiller/model"
/private/tmp/claude-501/-Users-brandonacuna-Espresso-Chiller/01e10f36-6c4a-4b63-a2f7-ab5c191fd43f/scratchpad/venv/bin/python chiller_model.py
```

(any Python ≥ 3.10 with `numpy` and `matplotlib` works; the venv above already
has both). The script exits 0 only if validation passes. The study CSVs must
sit one directory up (they do).

## Outputs (`outputs/`)

| File | What it is |
|---|---|
| `validation.csv` | Every row of all three study CSVs: study value vs model value vs delta vs tolerance. 74/74 pass. |
| `three_group_sizing.csv` | Bath-volume sweep (4–12 L: triple-pull excursion, 2 K recovery times) and duty table (60/90/120 shots/h with heat leak and chiller sizing). |
| `layout_head.csv` | Gravity-head requirement vs flow rate (coil dP, fittings, dip submergence, total drop). |
| `validation_overlay.png` | Model curves over study points, three panels (bore / setpoint / recipe sweeps). |
| `bath_transient.png` | 60-min 90 shot/h rush-hour simulation with three triple pulls: bath temperature (0.5 K thermostat band) + instantaneous load and chiller duty. |
| `chiller_sizing.png` | Required extraction vs shots/h with de-rated chiller capacity lines; recommended 1000 W unit marked. |
| `layout_head.png` | Required spout-to-airpot drop vs flow rate; 95 cm installation recommendation marked. |

## Physics

- **Coiled laminar Nusselt**: Manlapaz–Churchill (1981), constant-wall-T form,
  De = Re·√(d/D); coil pitch negligible (He ≈ De). Straight-tube limit
  Nu → 3.657 is self-tested.
- **Outlet**: NTU with the bath as an infinite reservoir,
  T_out = T_g + (T_in − T_g)·exp(−NTU), NTU = U·A_i/(ṁ·cp).
- **Hydraulics**: Hagen–Poiseuille (plus an optional integrated variant with
  local μ(T) and White's laminar curvature factor).
- **Stagnant cool-down**: lumped capacitance + a radial finite-difference
  cross-check.

## Property-evaluation conventions (what reproduces the study)

Each convention was identified by inverse-fitting the study tables and then
verified against **every** row of all three CSVs (see `validation.csv`):

1. **Viscosity μ(T)**: Arrhenius fit μ = A·exp(B/T_K) through the two study
   endpoints (0.50 mPa·s @ 78 °C, 2.6 mPa·s @ 4 °C).
2. **h_i used in U** (sizing/outlet): Re, De, Pr at **one fixed reference
   temperature T_ref = 43.8 °C** (μ_ref = 0.974 mPa·s). T_ref is calibrated
   once so U(design point) = 915.0 W/m²K exactly; it lands ~3 K above the
   arithmetic-mean bulk temperature (41 °C) and then reproduces the *entire*
   bore sweep (< 0.3 % in Nu) and recipe sweep (< 1 %) with no further
   freedom. Using 41 °C instead misses the 2.5 mm length by 0.055 m.
3. **Resistance chain** (inner-area basis):
   `1/U = 1/h_i + d_i·ln(d_o/d_i)/(2·k_wall) + 1/h_o` — cylindrical log-mean
   wall term (k_316L = 15 W/m·K), but the glycol film (h_o = 1500 W/m²K) taken
   **without** the A_i/A_o area credit. The strict area-corrected form
   provably cannot reproduce the study (it would require effective Nu to
   *increase* with bore across the sweep); the study's U values are only
   consistent with the uncorrected film term, which is the conservative
   choice. A flag (`outer_area_correction=True`) enables the strict form
   (U(design) → ~1146 W/m²K, required length → 1.73 m).
4. **Cold-end wall temperature**: T_w = T_out − U_loc·(T_out − T_g)/h_i with
   h_i and U_loc evaluated **locally at the outlet temperature**
   (μ ≈ 2.6 mPa·s → h_i,cold ≈ 1939 W/m²K). Matches every published wall
   temperature to ≤ 0.03 K.
5. **Pressure drop**: Hagen–Poiseuille, straight tube, **whole tube at the
   cold viscosity 2.6 mPa·s** (cold-soaked worst case, no curvature factor)
   — reproduces all five published values to < 5 %. The physically detailed
   integrated version gives ~3.8 kPa at the design point (the study's 4.2 kPa
   is the conservative convention).
6. **Stagnant cool-down**: lumped, external (wall + glycol) resistance only:
   τ ≈ 2.1 s, 99 % complete at 9.6 s ≈ the study's "~9 s". The radial FD
   cross-check (Bi ≈ 3.4) puts the *centreline* at 99 % at ~21 s — the study
   number is the lumped estimate.

## Validation result

Binding tolerances all met: outlet ≤ 0.15 K (max |Δ| = 0.118 K, the 2.96 g/s
shared-coil row), wall ≤ 0.15 K (max 0.030 K), length ≤ 0.05 m (max 0.010 m),
holdup ≤ 0.5 mL (max 0.06 mL), dP ≤ 15 % (max 4.3 %).

## Three-group results (La Marzocco Strada X)

- **Bath**: 35 wt% propylene glycol (ρ 1035 kg/m³, cp 3700 J/kg·K).
  **8 L recommended** — absorbs a 3-simultaneous pull (3 × 11.5 kJ / 27 s) as
  a 1.13 K adiabatic excursion (4 L would see 2.25 K). Cross-check: the
  study's 2-group 856 W transient into 4 L = 1.51 K (study said 1.5 K).
- **Duty**: 232 / 328 / 423 W at 60 / 90 / 120 bar-total shots/h, including a
  40 W heat-leak allowance (insulated 8 L bath, 25 mm foam, ~11 W envelope at
  ΔT 24 K + ~20 W stirrer/pump dissipation + margin).
- **Chiller**: compressor chillers are rated at ~20 °C bath; assume 50 %
  capacity at ~0 °C (typical 40–60 %). A **1000 W-rated (≈1/3 hp) unit**
  gives ~500 W at the +1 °C bath — 18 % margin over the 120 shot/h peak.
  Recovery from a 2 K excursion (8 L): ~2.2 min idle, ~6 min while serving
  90 shots/h.
- **Rush-hour simulation** (90 shots/h, three triple pulls, 0.5 K on/off
  thermostat band): bath stays within **+0.74…+2.08 °C**, chiller duty cycle
  ~65 %. The wall-freeze limit (−6.5 °C glycol) is never approached — 7.2 K
  of margin; worst flowing cold-end wall +1.8 °C, worst stagnant wall = bath
  = +0.74 °C, both far above the −0.4 °C beverage freezing point.
- **Gravity-head layout**: at the 2.0 g/s worst case the coil takes 5.6 kPa
  (cold-viscosity convention) ≈ 57 cm of column; + 30 cm dip-tube submergence
  + 5 cm fitting allowance ⇒ **92 cm required drop. Recommend ≥ 95 cm:
  machine on the counter, bath + airpot under the counter, airpot liquid
  surface ≥ 95 cm below the spout.** (Note: once the siphon is primed the
  submergence term cancels for matched densities, so 92 cm is conservative —
  it covers priming/start-up.)
