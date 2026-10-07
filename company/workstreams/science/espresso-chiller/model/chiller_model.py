#!/usr/bin/env python
"""
Parametric engineering model of the inline espresso chiller
===========================================================

Reproduces and extends the completed design study:
  "Chiller Design Recommendation.md"  (spec + assumptions, section 8)
  "Chiller Coil Sizing.csv"           (bore sweep)
  "Chiller Setpoint Window.csv"       (glycol setpoint sweep)
  "Chiller Recipe Robustness.csv"     (outlet vs flow rate)

Physics
-------
* Coiled laminar Nusselt: Manlapaz-Churchill (1981), constant-wall-temperature
  form, with Dean number De = Re*sqrt(d/D).  Straight-tube limit Nu -> 3.657
  as He -> 0 (self-tested below).
* Overall U on the INNER area; outlet via NTU with the bath as an infinite
  reservoir: T_out = T_g + (T_in - T_g)*exp(-NTU),  NTU = U*A_i/(mdot*cp).
* Cold-end inner-wall temperature: T_w = T_local - U_loc*(T_local - T_g)/h_i
  evaluated with cold-end (outlet-temperature) properties.
* Hagen-Poiseuille pressure drop; lumped stagnant cool-down; CIP Reynolds.

Property-evaluation conventions (reverse-engineered from the study; each was
identified by inverse-fitting the published tables, then verified against
EVERY row of all three CSVs -- see validation.csv):

  C1. Viscosity mu(T): Arrhenius fit  mu = A*exp(B/T_K)  through the two
      published endpoints (0.50 mPa.s @ 78 C, 2.6 mPa.s @ 4 C).
  C2. h_i used in U (sizing/outlet): Re, De, Pr evaluated at ONE fixed
      reference temperature T_ref.  T_ref is calibrated once so that
      U(design point) = 915.0 W/m2K exactly; the result is T_ref = 43.8 C
      (mu_ref = 0.974 mPa.s), i.e. ~3 K above the arithmetic-mean bulk
      temperature (78+4)/2 = 41 C.  This single convention reproduces the
      whole bore sweep (5 bores, <0.3% in Nu) and the whole recipe sweep
      (5 flows, <1% in Nu).  Evaluating at exactly 41 C instead misses the
      2.5 mm length by 0.055 m, so the calibrated T_ref is retained and
      documented rather than silently fudged.
  C3. Resistance chain (inner-area basis):
          1/U = 1/h_i + d_i*ln(d_o/d_i)/(2*k_wall) + 1/h_o
      i.e. proper cylindrical log-mean wall term, but the glycol film taken
      as 1/h_o WITHOUT the A_i/A_o area credit.  The strict area-corrected
      form (A_i/A_o)/h_o provably cannot reproduce the study: it would
      require the effective Nu to INCREASE with bore diameter across the
      bore sweep, which no laminar-coil correlation does.  The study's
      numbers are only consistent with the uncorrected film term
      (equivalently: h_o = 1500 W/m2K referenced to the inner area).  This
      is the conservative choice, since A_o > A_i.  With the strict form,
      U(design) would be ~1146 W/m2K and the required length 1.73 m.
  C4. Cold-end wall temperature: h_i and U evaluated LOCALLY at the outlet
      bulk temperature (mu ~ 2.6 mPa.s -> h_i,cold ~ 1939 W/m2K,
      U_loc ~ 819 W/m2K).  Reproduces every wall temperature in both CSVs
      to <= 0.03 K.  (Note: the study's U_avg=915 paired with the implied
      h_i ~ 2170 gives the same U/h ratio -- the ratio is what the formula
      uses.)
  C5. Pressure drop: Hagen-Poiseuille, straight tube, with the WHOLE tube at
      the cold viscosity 2.6 mPa.s (cold-soaked coil worst case, no Dean
      friction correction).  Reproduces all five published dP values to
      <5%.  A physically-detailed alternative (local mu(T(x)) integrated
      along the tube, White's laminar curvature factor) is also implemented
      (dp_integrated); it gives ~3.8 kPa at the design point vs the study's
      conservative 4.2 kPa -- the two omissions partially offset.
  C6. Stagnant cool-down: lumped capacity, external chain wall+glycol only
      (tau = rho*cp*d/(4*U_ext) ~ 2.1 s); "reaches bath temperature" =
      99% complete = tau*ln(100) ~ 9.6 s, matching the study's ~9 s.  A
      radial 1-D finite-difference solution (internal gradients, Bi ~ 3.4)
      is included as a cross-check: centreline 99% at ~21 s
      (bulk-mean ~19 s).

Run:
  /private/tmp/claude-501/-Users-brandonacuna-Espresso-Chiller/01e10f36-6c4a-4b63-a2f7-ab5c191fd43f/scratchpad/venv/bin/python chiller_model.py

Outputs -> model/outputs/: validation.csv, three_group_sizing.csv,
layout_head.csv, validation_overlay.png, bath_transient.png,
chiller_sizing.png, layout_head.png
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass, field, replace
from pathlib import Path

import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent          # .../Espresso Chiller/model
STUDY = BASE.parent                             # .../Espresso Chiller
OUT = BASE / "outputs"

G = 9.81  # m/s2


# ----------------------------------------------------------------------------
# Fluid properties (study section 8: coffee treated as water-like)
# ----------------------------------------------------------------------------
@dataclass
class Fluid:
    rho: float = 1010.0      # kg/m3
    cp: float = 3900.0       # J/kg.K
    k: float = 0.62          # W/m.K
    mu_hot: float = 0.50e-3  # Pa.s at T_hot
    T_hot: float = 78.0      # C
    mu_cold: float = 2.6e-3  # Pa.s at T_cold
    T_cold: float = 4.0      # C

    def __post_init__(self):
        # Arrhenius fit mu = A*exp(B/T_K) through the two endpoints (C1)
        self._B = math.log(self.mu_cold / self.mu_hot) / (
            1.0 / (self.T_cold + 273.15) - 1.0 / (self.T_hot + 273.15)
        )
        self._A = self.mu_hot / math.exp(self._B / (self.T_hot + 273.15))

    def mu(self, T_C):
        """Dynamic viscosity, Pa.s, at temperature T_C (deg C)."""
        return self._A * np.exp(self._B / (np.asarray(T_C, dtype=float) + 273.15))

    def prandtl(self, T_C):
        return self.cp * self.mu(T_C) / self.k


# ----------------------------------------------------------------------------
# Correlations
# ----------------------------------------------------------------------------
def nu_manlapaz_churchill(De, Pr):
    """Manlapaz-Churchill (1981) laminar Nusselt for a helical coil,
    constant wall temperature version.  He ~ De because the coil pitch term
    (b/(pi*D))^2 ~ 3e-4 is negligible for 4.4 mm tube on an 80 mm coil.

        Nu = [ (3.657 + 4.343/x1)^3 + 1.158*(He/x2)^(3/2) ]^(1/3)
        x1 = (1 + 957/(He^2 Pr))^2 ,   x2 = 1 + 0.477/Pr

    Straight-tube limit: Nu -> 3.657 as He -> 0.
    """
    He = np.asarray(De, dtype=float)
    Pr = np.asarray(Pr, dtype=float)
    x1 = (1.0 + 957.0 / (He**2 * Pr + 1e-300)) ** 2
    x2 = 1.0 + 0.477 / Pr
    return ((3.657 + 4.343 / x1) ** 3 + 1.158 * (He / x2) ** 1.5) ** (1.0 / 3.0)


def white_friction_ratio(De):
    """White (1929) laminar curved/straight friction-factor ratio (used only
    by the physically-detailed dp_integrated; the study's dP convention C5
    does not apply it)."""
    De = np.asarray(De, dtype=float)
    r = np.ones_like(De)
    m = De > 11.6
    r[m] = 1.0 / (1.0 - (1.0 - (11.6 / De[m]) ** 0.45) ** (1.0 / 0.45))
    return r


# ----------------------------------------------------------------------------
# Parametric coil model
# ----------------------------------------------------------------------------
@dataclass
class Coil:
    d_i: float = 3.0e-3        # bore, m
    t_wall: float = 0.7e-3     # wall thickness, m
    D_coil: float = 0.080      # coil (helix) diameter, m
    L: float = 2.17            # tube length, m
    mdot: float = 1.48e-3      # kg/s
    T_in: float = 78.0         # C at the spout
    T_g: float = 1.0           # glycol bath temperature, C
    h_o: float = 1500.0        # glycol-side film coefficient, W/m2K
    k_wall: float = 15.0       # 316L, W/m.K
    fluid: Fluid = field(default_factory=Fluid)
    T_ref: float | None = None # h_i property temperature (C); None -> calibrated
    outer_area_correction: bool = False  # False = study convention (C3)

    # -- geometry -------------------------------------------------------
    @property
    def d_o(self):
        return self.d_i + 2.0 * self.t_wall

    @property
    def A_i(self):
        return math.pi * self.d_i * self.L

    @property
    def turns(self):
        return round(self.L / (math.pi * self.D_coil))

    def holdup_m3(self):
        return math.pi / 4.0 * self.d_i**2 * self.L

    def residence_s(self):
        return self.holdup_m3() * self.fluid.rho / self.mdot

    # -- film coefficients ---------------------------------------------
    def h_inner_at(self, T_eval):
        """Coffee-side film coefficient with properties at T_eval (C)."""
        f = self.fluid
        mu = f.mu(T_eval)
        Re = 4.0 * self.mdot / (math.pi * self.d_i * mu)
        De = Re * math.sqrt(self.d_i / self.D_coil)
        Pr = f.cp * mu / f.k
        Nu = nu_manlapaz_churchill(De, Pr)
        return float(Nu) * f.k / self.d_i

    def R_outside(self):
        """Wall + glycol film resistance on the inner-area basis (C3)."""
        R_wall = self.d_i * math.log(self.d_o / self.d_i) / (2.0 * self.k_wall)
        if self.outer_area_correction:
            R_film = (self.d_i / self.d_o) / self.h_o   # strict textbook form
        else:
            R_film = 1.0 / self.h_o                     # study convention
        return R_wall + R_film

    def U_from_hi(self, h_i):
        return 1.0 / (1.0 / h_i + self.R_outside())

    def U(self):
        """Overall coefficient on the inner area, fixed-T_ref convention (C2)."""
        Tref = self.T_ref if self.T_ref is not None else T_REF_CAL
        return self.U_from_hi(self.h_inner_at(Tref))

    # -- thermal performance -------------------------------------------
    def NTU(self):
        return self.U() * self.A_i / (self.mdot * self.fluid.cp)

    def outlet_C(self):
        return self.T_g + (self.T_in - self.T_g) * math.exp(-self.NTU())

    def required_length(self, T_out=4.0):
        NTU = math.log((self.T_in - self.T_g) / (T_out - self.T_g))
        return NTU * self.mdot * self.fluid.cp / (self.U() * math.pi * self.d_i)

    def wall_cold_C(self, T_local=None):
        """Inner-wall temperature at the cold end (C4): local properties at
        the outlet bulk temperature."""
        if T_local is None:
            T_local = self.outlet_C()
        h_i = self.h_inner_at(T_local)
        U_loc = self.U_from_hi(h_i)
        return T_local - U_loc * (T_local - self.T_g) / h_i

    # -- hydraulics -----------------------------------------------------
    def dp_study_Pa(self):
        """Study convention C5: Hagen-Poiseuille, straight tube, whole tube
        at the cold viscosity (cold-soaked worst case)."""
        Q = self.mdot / self.fluid.rho
        return 128.0 * self.fluid.mu_cold * self.L * Q / (math.pi * self.d_i**4)

    def dp_integrated_Pa(self, n=400):
        """Physically-detailed dP: local mu(T(x)) along the exponential NTU
        temperature profile, times White's laminar curvature factor."""
        f = self.fluid
        x = (np.arange(n) + 0.5) / n
        T = self.T_g + (self.T_in - self.T_g) * np.exp(-self.NTU() * x)
        mu = f.mu(T)
        Re = 4.0 * self.mdot / (math.pi * self.d_i * mu)
        De = Re * math.sqrt(self.d_i / self.D_coil)
        Q = self.mdot / f.rho
        dpdx = 128.0 * mu * Q / (math.pi * self.d_i**4) * white_friction_ratio(De)
        return float(np.mean(dpdx) * self.L)

    def cip(self, v=1.0, mu_w=1.0e-3, rho_w=998.0):
        """CIP flush at velocity v (m/s) with cleaning water (~20 C)."""
        Q = v * math.pi / 4.0 * self.d_i**2
        return {"flow_mL_min": Q * 6.0e7, "Re": rho_w * v * self.d_i / mu_w}

    # -- stagnant cool-down (C6) ---------------------------------------
    def stagnant_cooldown(self):
        """Coffee at rest in the tube.  Lumped: tau = rho*cp*d/(4*U_ext) with
        U_ext = wall + glycol film only; t99 = tau*ln(100).  Cross-check:
        radial 1-D FD with internal conduction (Bi = U_ext*r/k ~ 3.4)."""
        f = self.fluid
        U_ext = 1.0 / self.R_outside()
        tau = f.rho * f.cp * self.d_i / (4.0 * U_ext)
        t99_lumped = tau * math.log(100.0)

        # radial FD cross-check (explicit, cylindrical)
        r_o = self.d_i / 2.0
        N = 60
        r = np.linspace(0.0, r_o, N)
        dr = r[1] - r[0]
        alpha = f.k / (f.rho * f.cp)
        dt = 0.2 * dr**2 / alpha
        T = np.full(N, 4.0)          # start at chilled-outlet temperature
        Tg, T0 = self.T_g, 4.0
        t, t99_center, t99_mean = 0.0, None, None
        while t < 60.0 and (t99_center is None or t99_mean is None):
            lap = np.zeros(N)
            lap[1:-1] = (T[2:] - 2 * T[1:-1] + T[:-2]) / dr**2 + (
                (T[2:] - T[:-2]) / (2 * dr)) / r[1:-1]
            lap[0] = 4.0 * (T[1] - T[0]) / dr**2          # symmetry at r=0
            T[:-1] += alpha * dt * lap[:-1]
            # Robin boundary: -k dT/dr = U_ext (T_s - Tg)
            T[-1] = (T[-2] + dr * U_ext / f.k * Tg) / (1.0 + dr * U_ext / f.k)
            t += dt
            Tmean = float(np.sum(0.5 * (T[1:] + T[:-1]) * 0.5 * (r[1:] + r[:-1]))
                          / np.sum(0.5 * (r[1:] + r[:-1])))  # area-weighted mean
            if t99_center is None and abs(T[0] - Tg) < 0.01 * (T0 - Tg):
                t99_center = t
            if t99_mean is None and abs(Tmean - Tg) < 0.01 * (T0 - Tg):
                t99_mean = t
        return {"tau_lumped_s": tau, "t99_lumped_s": t99_lumped,
                "t99_fd_center_s": t99_center, "t99_fd_mean_s": t99_mean,
                "Bi": U_ext * r_o / f.k}


# ----------------------------------------------------------------------------
# T_ref calibration (C2): one scalar fitted so U(design) = 915.0 W/m2K
# ----------------------------------------------------------------------------
def calibrate_T_ref(target_U=915.0):
    c = Coil(T_ref=0.0)  # placeholder; overwritten in loop
    lo, hi = 4.0, 78.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if replace(c, T_ref=mid).U() < target_U:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


T_REF_CAL = calibrate_T_ref()   # ~43.8 C


# ----------------------------------------------------------------------------
# Self-tests (straight-tube limit + design-point checks)
# ----------------------------------------------------------------------------
def self_test():
    nu0 = float(nu_manlapaz_churchill(1e-9, 5.0))
    assert abs(nu0 - 3.657) < 1e-3, f"He->0 limit broken: {nu0}"
    c = Coil()
    assert abs(c.U() - 915.0) < 0.5, c.U()
    assert abs(c.NTU() - 3.242) < 0.01, c.NTU()
    assert abs(c.outlet_C() - 4.01) < 0.02, c.outlet_C()
    assert abs(c.wall_cold_C() - 2.74) < 0.02, c.wall_cold_C()
    print(f"[self-test] Nu(He->0) = {nu0:.3f}  |  design point: "
          f"U = {c.U():.1f} W/m2K, NTU = {c.NTU():.3f}, "
          f"outlet = {c.outlet_C():.2f} C, cold wall = {c.wall_cold_C():.2f} C  "
          f"(T_ref = {T_REF_CAL:.2f} C, mu_ref = {c.fluid.mu(T_REF_CAL)*1e3:.3f} mPa.s)")


# ----------------------------------------------------------------------------
# TASK 2 -- validation against the three study CSVs
# ----------------------------------------------------------------------------
def read_csv(name):
    with open(STUDY / name, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def validate():
    rows = []           # sweep, row, quantity, study, model, delta, tol, pass
    binding = {"length_m": 0.05, "holdup_mL": 0.5, "wall_C": 0.15,
               "outlet_C": 0.15}   # dP handled as relative 15%

    def add(sweep, rid, qty, study, model, tol, rel=False):
        delta = model - study
        ok = (abs(delta) <= tol * abs(study)) if rel else (abs(delta) <= tol)
        rows.append({"sweep": sweep, "row": rid, "quantity": qty,
                     "study": study, "model": round(model, 4),
                     "delta": round(delta, 4),
                     "tolerance": (f"{tol*100:.0f}%" if rel else tol),
                     "pass": "yes" if ok else "NO"})
        return ok

    all_ok = True

    # ---- bore sweep -------------------------------------------------------
    for r in read_csv("Chiller Coil Sizing.csv"):
        ID = float(r["ID_mm"])
        c = Coil(d_i=ID * 1e-3, L=float(r["length_m"]))
        rid = f"{ID:g} mm"
        all_ok &= add("bore", rid, "length_m", float(r["length_m"]),
                      c.required_length(4.0), binding["length_m"])
        all_ok &= add("bore", rid, "holdup_mL", float(r["holdup_mL"]),
                      c.holdup_m3() * 1e6, binding["holdup_mL"])
        all_ok &= add("bore", rid, "dP_kPa", float(r["dP_kPa"]),
                      c.dp_study_Pa() / 1e3, 0.15, rel=True)
        all_ok &= add("bore", rid, "wall_cold_C", float(r["wall_cold_C"]),
                      c.wall_cold_C(), binding["wall_C"])
        add("bore", rid, "U_W_m2K", float(r["U"]), c.U(), 0.01, rel=True)
        add("bore", rid, "residence_s", float(r["residence_s"]),
            c.residence_s(), 0.1)
        add("bore", rid, "turns", float(r["turns"]), float(c.turns), 0.5)
        add("bore", rid, "pct_of_shot", float(r["pct_of_shot"]),
            c.holdup_m3() * 1e6 / 40.0 * 100.0, 1.0)

    # ---- setpoint window --------------------------------------------------
    for r in read_csv("Chiller Setpoint Window.csv"):
        Tg = float(r["glycol_C"])
        c = Coil(T_g=Tg)
        rid = f"Tg={Tg:g} C"
        all_ok &= add("setpoint", rid, "length_m", float(r["length_for_4C_m"]),
                      c.required_length(4.0), binding["length_m"])
        all_ok &= add("setpoint", rid, "wall_min_C", float(r["wall_min_C"]),
                      c.wall_cold_C(T_local=4.0), binding["wall_C"])
        add("setpoint", rid, "margin_to_freeze_K", float(r["margin_to_freeze_K"]),
            c.wall_cold_C(T_local=4.0) + 0.4, binding["wall_C"])
        all_ok &= add("setpoint", rid, "outlet_C",
                      float(r["outlet_at_fixed_2p17m_C"]),
                      c.outlet_C(), binding["outlet_C"])

    # ---- recipe robustness ------------------------------------------------
    for r in read_csv("Chiller Recipe Robustness.csv"):
        g = float(r["flow_g_s"])
        c = Coil(mdot=g * 1e-3)
        rid = f"{g:g} g/s"
        all_ok &= add("recipe", rid, "outlet_C", float(r["outlet_C"]),
                      c.outlet_C(), binding["outlet_C"])
        add("recipe", rid, "NTU", float(r["NTU"]), c.NTU(), 0.05)

    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "validation.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # summary of the binding tolerances
    def maxd(pred):
        return max(abs(r["delta"]) for r in rows if pred(r))

    summary = {
        "max_length_delta_m": maxd(lambda r: r["quantity"].startswith("length")),
        "max_wall_delta_K": maxd(lambda r: "wall" in r["quantity"]),
        "max_outlet_delta_K": maxd(lambda r: r["quantity"] == "outlet_C"),
        "max_holdup_delta_mL": maxd(lambda r: r["quantity"] == "holdup_mL"),
        "max_dP_delta_pct": max(abs(r["delta"] / r["study"]) * 100 for r in rows
                                if r["quantity"] == "dP_kPa"),
    }
    print(f"[validation] {'PASS' if all_ok else 'FAIL'} -- "
          + ", ".join(f"{k} = {v:.3f}" for k, v in summary.items()))
    if not all_ok:
        for r in rows:
            if r["pass"] == "NO":
                print("   FAILED:", r)
    return rows, summary, all_ok


# ----------------------------------------------------------------------------
# TASK 3 -- three-group installation (La Marzocco Strada X, one shared bath)
# ----------------------------------------------------------------------------
# Bath: 35 wt% propylene glycol
GLY_RHO, GLY_CP = 1035.0, 3700.0        # kg/m3, J/kg.K
SHOT_KJ, SHOT_S = 11.5e3, 27.0           # J per shot, shot duration
SHOT_W = SHOT_KJ / SHOT_S                # ~426 W per active shot
HEAT_LEAK_W = 40.0   # assumption: insulated 8 L bath at +1 C in a 25 C room:
                     # ~0.35 m2 envelope with 25 mm closed-cell foam
                     # (U ~ 1.3 W/m2K incl. lid/penetrations) ~ 11 W, plus
                     # stirrer/pump motor dissipation ~ 20 W, plus margin.
DERATE_0C = 0.50     # assumption: compressor chillers are rated at ~20 C bath;
                     # capacity at 0 C is typically 40-60% of rating -> use 50%.
RATED_W = 1000.0     # recommended unit: ~1000 W @ 20 C (1/3 hp class)
CAP_AT_BATH_W = RATED_W * DERATE_0C      # ~500 W available at ~0..+1 C


def bath_heat_capacity_J_K(V_L):
    return V_L * 1e-3 * GLY_RHO * GLY_CP


def three_group_tables():
    # -- bath volume sweep: 3 simultaneous shots, adiabatic excursion --------
    bath_rows = []
    for V in np.arange(4.0, 12.0 + 0.001, 1.0):
        C = bath_heat_capacity_J_K(V)
        exc = 3.0 * SHOT_KJ / C
        rec_idle = 2.0 * C / (CAP_AT_BATH_W - HEAT_LEAK_W)
        rec_busy = 2.0 * C / (CAP_AT_BATH_W - (90 * SHOT_KJ / 3600.0 + HEAT_LEAK_W))
        bath_rows.append({"section": "bath_sweep", "bath_L": V,
                          "heat_capacity_kJ_K": round(C / 1e3, 2),
                          "excursion_3simul_K": round(exc, 3),
                          "recovery_2K_idle_s": round(rec_idle, 0),
                          "recovery_2K_at_90shots_h_s": round(rec_busy, 0)})
    # cross-check vs study: 856 W x 27 s into 4 L -> 1.5 K
    chk = 856.0 * 27.0 / bath_heat_capacity_J_K(4.0)
    print(f"[3-group] study cross-check: 2-group 856 W transient into 4 L = "
          f"{chk:.2f} K (study: 1.5 K)")

    # -- duty table ----------------------------------------------------------
    duty_rows = []
    for sph in (60, 90, 120):
        mean_w = sph * SHOT_KJ / 3600.0
        tot = mean_w + HEAT_LEAK_W
        duty_rows.append({"section": "duty", "shots_per_h": sph,
                          "mean_shot_load_W": round(mean_w, 1),
                          "heat_leak_W": HEAT_LEAK_W,
                          "required_extraction_at_bath_W": round(tot, 1),
                          "required_rated_at_20C_W": round(tot / DERATE_0C, 0),
                          "recommended_rated_W": RATED_W,
                          "capacity_at_bath_W": CAP_AT_BATH_W,
                          "margin_pct": round((CAP_AT_BATH_W / tot - 1) * 100, 0)})
    return bath_rows, duty_rows


def rush_hour_sim(V_L=8.0, dt=0.5, t_end=3600.0):
    """Worst-case rush hour: 90 bar-total shots/h on 3 groups, including three
    3-simultaneous events; on/off chiller thermostat with a 0.5 K band."""
    starts = [(20.0 + 44.0 * k, 1) for k in range(81)]          # 81 singles
    starts += [(600.0, 3), (1500.0, 3), (2400.0, 3)]            # 3 triples
    C = bath_heat_capacity_J_K(V_L)
    n = int(t_end / dt)
    t = np.arange(n) * dt
    load = np.full(n, HEAT_LEAK_W)
    for t0, k in starts:
        i0, i1 = int(t0 / dt), int(min(t0 + SHOT_S, t_end) / dt)
        load[i0:i1] += k * SHOT_W
    T = np.empty(n)
    duty = np.zeros(n)
    T[0], on = 1.0, False
    setpoint, band = 1.0, 0.5
    for i in range(1, n):
        if T[i - 1] >= setpoint + band / 2:
            on = True
        elif T[i - 1] <= setpoint - band / 2:
            on = False
        duty[i] = CAP_AT_BATH_W if on else 0.0
        T[i] = T[i - 1] + (load[i] - duty[i]) * dt / C
    return t, T, load, duty, starts


def layout_table():
    """Gravity-head check: coil is gravity-fed from the group spout into a
    submerged dip tube in the airpot.  Required drop (task accounting):
        dP_coil(2.0 g/s, cold-mu worst case) + 30 cm dip submergence
        + fitting allowance (0.5 kPa; laminar K-losses are <0.1 kPa at
        0.28 m/s, so 0.5 kPa is generous).
    Physics note: with the outlet submerged, steady siphon flow cancels the
    submergence term for matched densities -- keeping it (per the brief) is
    conservative double-counting, appropriate for priming/start-up."""
    fl = Fluid()
    sub_cm, fit_Pa = 30.0, 500.0
    rows = []
    for g in np.arange(1.0, 2.21, 0.1):
        c = Coil(mdot=g * 1e-3)
        dp_c = c.dp_study_Pa()
        head_coil = dp_c / (fl.rho * G) * 100.0        # cm of column
        head_fit = fit_Pa / (fl.rho * G) * 100.0
        total = head_coil + head_fit + sub_cm
        rows.append({"flow_g_s": round(g, 2),
                     "dP_coil_kPa_coldmu": round(dp_c / 1e3, 2),
                     "dP_coil_kPa_integrated": round(c.dp_integrated_Pa() / 1e3, 2),
                     "head_coil_cm": round(head_coil, 1),
                     "head_fittings_cm": round(head_fit, 1),
                     "submergence_cm": sub_cm,
                     "total_required_drop_cm": round(total, 1)})
    return rows


# ----------------------------------------------------------------------------
# TASK 4 -- plots
# ----------------------------------------------------------------------------
BLUE, ORANGE, GREEN = "#1f6f8b", "#d9822b", "#3a7d44"
SLATE, GRID = "#3d4a52", "#e3e7ea"

plt.rcParams.update({
    "figure.dpi": 110, "savefig.dpi": 200, "font.size": 9.5,
    "axes.titlesize": 10, "axes.labelsize": 9.5, "axes.edgecolor": SLATE,
    "axes.labelcolor": SLATE, "text.color": SLATE, "xtick.color": SLATE,
    "ytick.color": SLATE, "axes.grid": True, "grid.color": GRID,
    "grid.linewidth": 0.8, "legend.frameon": False,
})


def style(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_axisbelow(True)


def plot_validation_overlay():
    fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.0))

    # (a) bore sweep: required length
    bore = read_csv("Chiller Coil Sizing.csv")
    ids = np.arange(2.3, 5.25, 0.05)
    L = [Coil(d_i=i * 1e-3).required_length(4.0) for i in ids]
    ax = axes[0]
    ax.plot(ids, L, color=BLUE, lw=2, label="model", zorder=2)
    ax.scatter([float(r["ID_mm"]) for r in bore],
               [float(r["length_m"]) for r in bore],
               s=42, facecolor="white", edgecolor=SLATE, lw=1.4,
               label="study", zorder=3)
    ax.set_xlabel("tube bore (mm)")
    ax.set_ylabel("length for 78 → 4 °C at 1.48 g/s (m)")
    ax.set_title("Bore sweep: lengths agree within 10 mm", loc="left")
    ax.legend(loc="upper right")
    style(ax)

    # (b) setpoint window: required length vs glycol temperature
    sp = read_csv("Chiller Setpoint Window.csv")
    tg = np.arange(-0.25, 3.3, 0.05)
    Lg = [Coil(T_g=g).required_length(4.0) for g in tg]
    ax = axes[1]
    ax.plot(tg, Lg, color=BLUE, lw=2, label="model", zorder=2)
    ax.scatter([float(r["glycol_C"]) for r in sp],
               [float(r["length_for_4C_m"]) for r in sp],
               s=42, facecolor="white", edgecolor=SLATE, lw=1.4,
               label="study", zorder=3)
    ax.axvline(1.0, color=GREEN, lw=1.2, ls=":")
    ax.annotate("+1 °C setpoint", xy=(1.0, 2.75), color=GREEN,
                fontsize=8.5, ha="left", xytext=(1.12, 2.78))
    ax.set_xlabel("glycol setpoint (°C)")
    ax.set_ylabel("length for 4 °C outlet (m)")
    ax.set_title("Setpoint window: lengths agree within 6 mm", loc="left")
    ax.legend(loc="upper left")
    style(ax)

    # (c) recipe robustness: outlet vs flow at fixed 2.17 m coil
    rc = read_csv("Chiller Recipe Robustness.csv")
    gg = np.arange(1.0, 3.21, 0.02)
    To = [Coil(mdot=g * 1e-3).outlet_C() for g in gg]
    ax = axes[2]
    ax.plot(gg, To, color=BLUE, lw=2, label="model", zorder=2)
    ax.scatter([float(r["flow_g_s"]) for r in rc],
               [float(r["outlet_C"]) for r in rc],
               s=42, facecolor="white", edgecolor=SLATE, lw=1.4,
               label="study", zorder=3)
    ax.axhline(4.0, color=ORANGE, lw=1.2, ls="--")
    ax.annotate("4 °C spec", xy=(2.9, 4.0), xytext=(2.62, 4.55),
                color=ORANGE, fontsize=8.5)
    ax.set_xlabel("flow rate (g/s)")
    ax.set_ylabel("outlet temperature (°C)")
    ax.set_title("Recipe sweep: outlets agree within 0.12 K", loc="left")
    ax.legend(loc="upper left")
    style(ax)

    fig.suptitle("One property convention reproduces all three study sweeps "
                 "within tolerance", x=0.01, ha="left", fontsize=12,
                 fontweight="bold", color=SLATE)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT / "validation_overlay.png")
    plt.close(fig)


def plot_bath_transient(t, T, load, duty, V_L):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10.5, 6.2), sharex=True,
                                   gridspec_kw={"height_ratios": [1.4, 1]})
    tm = t / 60.0
    ax1.axhspan(0.75, 1.25, color=GRID, alpha=0.6, lw=0)
    ax1.plot(tm, T, color=BLUE, lw=1.6)
    ax1.axhline(-6.5, color=ORANGE, lw=1.4, ls="--")
    ax1.annotate("wall-freeze limit −6.5 °C",
                 xy=(30, -6.5), xytext=(30, -5.6), color=ORANGE,
                 fontsize=9, ha="center")
    ax1.annotate(f"bath never leaves +{T.min():.1f} to +{T.max():.1f} °C\n"
                 f"(margin to freeze limit: {T.min() + 6.5:.1f} K)",
                 xy=(30, 0.4), color=BLUE, fontsize=9, ha="center", va="top")
    ax1.annotate("thermostat band ±0.25 K", xy=(51.5, 0.42), fontsize=8,
                 color=SLATE, ha="center", va="top")
    ax1.set_ylabel("bath temperature (°C)")
    ax1.set_ylim(-7.5, 2.6)
    ax1.set_title(f"An {V_L:.0f} L bath rides a 90 shot/h rush (three triple "
                  f"pulls) between +{T.min():.1f} and +{T.max():.1f} °C "
                  "— 7 K above the freeze limit", loc="left")
    style(ax1)

    ax2.fill_between(tm, load, step="mid", color=BLUE, alpha=0.30, lw=0)
    ax2.plot(tm, load, drawstyle="steps-mid", color=BLUE, lw=0.9,
             label="heat into bath (shots + leak)")
    ax2.plot(tm, duty, drawstyle="steps-mid", color=GREEN, lw=1.3,
             label="chiller extraction (on/off)")
    ax2.annotate("triple pulls", xy=(10.2, 1330), xytext=(15.0, 1520),
                 color=SLATE, fontsize=8.5,
                 arrowprops=dict(arrowstyle="-", color=SLATE, lw=0.8))
    ax2.set_xlabel("time (min)")
    ax2.set_ylabel("power (W)")
    ax2.set_ylim(0, 1950)
    ax2.legend(loc="upper right", fontsize=8.5)
    ax2.set_title(f"Instantaneous load peaks at {load.max()/1e3:.1f} kW for "
                  "seconds; the 500 W chiller only has to match the "
                  f"{load.mean():.0f} W mean", loc="left")
    style(ax2)

    fig.tight_layout()
    fig.savefig(OUT / "bath_transient.png")
    plt.close(fig)


def plot_chiller_sizing():
    sph = np.arange(0, 141, 1)
    req = sph * SHOT_KJ / 3600.0 + HEAT_LEAK_W
    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    ax.plot(sph, req, color=BLUE, lw=2.2,
            label="required extraction at +1 °C bath")
    for rated, col, name in ((600.0, ORANGE, "600 W-rated unit"),
                             (1000.0, GREEN, "1000 W-rated unit (recommended)"),
                             (1500.0, SLATE, "1500 W-rated unit")):
        cap = rated * DERATE_0C
        ax.axhline(cap, color=col, lw=1.4, ls="--")
        ax.annotate(f"{name}: {cap:.0f} W at bath", xy=(2, cap + 8),
                    color=col, fontsize=8.5)
    for s in (60, 90, 120):
        r = s * SHOT_KJ / 3600.0 + HEAT_LEAK_W
        ax.scatter([s], [r], s=40, facecolor="white", edgecolor=BLUE,
                   lw=1.4, zorder=3)
        ax.annotate(f"{s}/h: {r:.0f} W", xy=(s, r), xytext=(s + 2, r - 42),
                    fontsize=8.5, color=BLUE)
    ax.set_xlabel("bar-total shots per hour (3 groups)")
    ax.set_ylabel("mean thermal load incl. 40 W heat leak (W)")
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 820)
    ax.set_title("A 1000 W-rated (20 °C) chiller keeps ~500 W at the "
                 "+1 °C bath — 18% margin over a 120 shot/h bar",
                 loc="left")
    ax.legend(loc="lower right", fontsize=8.5)
    style(ax)
    fig.tight_layout()
    fig.savefig(OUT / "chiller_sizing.png")
    plt.close(fig)


def plot_layout_head(rows, min_drop_cm, rec_drop_cm):
    g = [r["flow_g_s"] for r in rows]
    tot = [r["total_required_drop_cm"] for r in rows]
    coil = [r["head_coil_cm"] for r in rows]
    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    ax.plot(g, tot, color=BLUE, lw=2.2,
            label="required drop (coil dP + 30 cm dip + fittings)")
    ax.plot(g, coil, color=BLUE, lw=1.2, ls=":",
            label="coil dP alone (cold-viscosity worst case)")
    ax.axhline(rec_drop_cm, color=GREEN, lw=1.6, ls="--")
    ax.annotate(f"recommended installation drop: {rec_drop_cm:.0f} cm "
                "(bath + airpot under the counter)",
                xy=(1.02, rec_drop_cm + 1.5), color=GREEN, fontsize=8.5)
    i20 = min(range(len(g)), key=lambda i: abs(g[i] - 2.0))
    ax.scatter([2.0], [tot[i20]], s=46, facecolor="white",
               edgecolor=ORANGE, lw=1.6, zorder=3)
    ax.annotate(f"worst case 2.0 g/s: {tot[i20]:.0f} cm", xy=(2.0, tot[i20]),
                xytext=(1.72, tot[i20] - 11), color=ORANGE, fontsize=9)
    ax.set_xlabel("shot flow rate (g/s)")
    ax.set_ylabel("required spout-to-airpot-surface drop (cm of column)")
    ax.set_ylim(0, 115)
    ax.set_title("Gravity feed needs "
                 f"{min_drop_cm:.0f} cm of drop at the 2.0 g/s worst case "
                 "— put the bath under the counter", loc="left")
    ax.legend(loc="lower right", fontsize=8.5)
    style(ax)
    fig.tight_layout()
    fig.savefig(OUT / "layout_head.png")
    plt.close(fig)


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    self_test()

    # ---- Task 2: validation ----
    _, summary, ok = validate()

    # extra design-point diagnostics
    c = Coil()
    cd = c.stagnant_cooldown()
    print(f"[design] holdup {c.holdup_m3()*1e6:.1f} mL, residence "
          f"{c.residence_s():.1f} s, dP(study conv) {c.dp_study_Pa()/1e3:.2f} kPa, "
          f"dP(integrated+White) {c.dp_integrated_Pa()/1e3:.2f} kPa")
    cip = c.cip()
    print(f"[design] CIP at 1.0 m/s: {cip['flow_mL_min']:.0f} mL/min, "
          f"Re = {cip['Re']:.0f} (study: ~3000 at 424 mL/min)")
    print(f"[design] stagnant cool-down: lumped tau {cd['tau_lumped_s']:.2f} s, "
          f"t99 {cd['t99_lumped_s']:.1f} s (study ~9 s); FD cross-check "
          f"Bi {cd['Bi']:.2f}, centreline t99 {cd['t99_fd_center_s']:.1f} s, "
          f"bulk-mean t99 {cd['t99_fd_mean_s']:.1f} s")

    # ---- Task 3: three-group installation ----
    bath_rows, duty_rows = three_group_tables()
    t, T, load, duty, _ = rush_hour_sim(V_L=8.0)
    # worst flowing wall temperature: slowest recipe (coldest outlet) at the
    # coldest bath the thermostat ever allows; worst stagnant wall = bath temp
    worst_wall = Coil(T_g=float(T.min()), mdot=1.27e-3).wall_cold_C()
    print(f"[3-group] rush-hour sim (8 L): bath {T.min():.2f}..{T.max():.2f} C, "
          f"chiller duty cycle {float(np.mean(duty > 0))*100:.0f}%, "
          f"freeze-limit margin {T.min()+6.5:.1f} K; worst flowing cold-end "
          f"wall (ristretto at coldest bath) {worst_wall:.2f} C; worst "
          f"stagnant wall = bath = {T.min():.2f} C, both >> -0.4 C freeze")

    with open(OUT / "three_group_sizing.csv", "w", newline="") as fh:
        keys = list(bath_rows[0].keys()) + [k for k in duty_rows[0] if k != "section"]
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(bath_rows)
        w.writerows(duty_rows)

    # ---- Task 3: gravity-head layout ----
    lay = layout_table()
    i20 = min(range(len(lay)), key=lambda i: abs(lay[i]["flow_g_s"] - 2.0))
    min_drop = lay[i20]["total_required_drop_cm"]
    rec_drop = 95.0  # recommendation: round the 92 cm worst case up
    print(f"[layout] worst case 2.0 g/s: coil dP "
          f"{lay[i20]['dP_coil_kPa_coldmu']:.2f} kPa -> required drop "
          f"{min_drop:.0f} cm; recommend >= {rec_drop:.0f} cm "
          "(machine on counter, bath + airpot below; airpot liquid surface "
          ">= 95 cm below the spout)")
    with open(OUT / "layout_head.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(lay[0].keys()))
        w.writeheader()
        w.writerows(lay)

    # ---- Task 4: plots ----
    plot_validation_overlay()
    plot_bath_transient(t, T, load, duty, 8.0)
    plot_chiller_sizing()
    plot_layout_head(lay, min_drop, rec_drop)
    print("[plots] wrote validation_overlay.png, bath_transient.png, "
          "chiller_sizing.png, layout_head.png")
    print(f"[done] validation {'PASS' if ok else 'FAIL'}; outputs in {OUT}")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
