# Chilling system design recommendation

Buildable specification for the inline espresso chiller, sized against the brewing parameters
already established: 18 g dose, 40 g beverage in 27 s (**1.48 g/s**), 78 °C at the spout,
9.5 % TDS, target outlet **4 °C**, peak throughput 60 shots/h.

This document is self-contained — it can be handed to a fabricator or a mechanical engineer
without the rest of the study.

---

## 1. Recommended configuration

**A helically coiled 316 stainless tube, immersed in a stirred propylene-glycol bath held at
+1 °C, with one dedicated coil per group head.**

| Parameter | Value | Basis |
|---|---|---|
| Tube material | 316L stainless, seamless | Food contact at pH ~5; no copper (prohibited for acidic foods, and a pro-oxidant for coffee lipids) |
| Tube bore | **3.0 mm ID**, 0.7 mm wall | Holdup vs. pressure-drop optimum (§4) |
| Coil length | **2.2 m** (~9 turns) | NTU 3.2 for 78 → 4 °C at 1.48 g/s |
| Coil diameter | **80 mm** | Dean-flow enhancement (§3) |
| Coolant | Food-grade propylene glycol/water, **+1 °C** | Freeze margin 3.1 K (§2) |
| Bath volume | **4 L**, stirred or pumped | 0.77 K rise per shot; absorbs the peak |
| Circulation | **~7 L/min** | 2 K rise across the coil at peak; agitation is the real requirement |
| Chiller | **300–400 W** (~0.1 hp) recirculating | Sized on the 192 W mean, not the 856 W transient |
| Holdup | **15 mL per coil** | 38 % of one shot (§4) |
| Residence time | ~10 s | Matches the 10 s chill assumed in the storage model |
| Pressure drop | ~4 kPa (0.6 psi) | Negligible; gravity feed is sufficient |

Duty: **428 W during a shot**, 11.5 kJ per shot, **192 W mean** at 60 shots/h.

---

## 2. The controlling constraint: wall temperature, not bulk temperature

The beverage freezes at **−0.9 to −0.4 °C**. What matters is not the glycol temperature or the
coffee's bulk temperature but the **inner-wall temperature at the cold end**, where the coffee is
already near 4 °C and the wall is closest to the coolant.

There is a counterintuitive result here worth stating explicitly:

> **Improving glycol-side heat transfer makes freezing *more* likely, not less.**

At a −5 °C glycol setpoint, raising the bath-side film coefficient from 800 to 3000 W/m²K drives the
inner wall from −1.2 °C to −3.4 °C. A better-stirred, colder bath is a *worse* design. The instinct
to "make the cold side as aggressive as possible" is exactly wrong, and it is the same instinct that
produced the liquid-nitrogen concept.

**Design rule: keep the glycol setpoint above −6 °C.** At +1 °C the minimum inner-wall temperature
is **+2.7 °C**, a **3.1 K margin** to the freezing point.

**The usable glycol window is −6.5 to +5.2 °C — about 12 K wide**, bounded below by wall freezing and
above by the coil length needed to still reach spec. A window that wide needs only an ordinary
thermostat; there is no need for fast closed-loop control, and no failure mode where a control fault
freezes the product.

---

## 3. Why a coil, not a straight tube

At 1.48 g/s in a 3 mm bore the flow is laminar (Re ≈ 750–1250), where a straight tube gives a fixed
Nusselt number of 3.66 and a poor film coefficient of ~756 W/m²K. Coiling the tube generates Dean
secondary circulation, which stirs the flow transversely without turbulence:

| Bore | Coil dia. | Dean number | h straight | h coiled | Gain |
|---|---|---|---|---|---|
| 3 mm | 60 mm | 281 | 756 | 3516 | **4.7×** |
| 3 mm | 100 mm | 218 | 756 | 3142 | **4.2×** |
| 4 mm | 80 mm | ~215 | 567 | ~2300 | **4.0×** |

A tighter coil gives more enhancement. **80 mm is the recommended compromise** — most of the
available gain, without the wall-thinning and kinking risk of bending 3 mm tube to a 60 mm radius.

The practical consequence: coiling cuts the required tube length from **3.7 m to 2.2 m** and the
holdup from 26 mL to 15 mL. Coiling also *improves* the freeze margin, because a higher coffee-side
coefficient pulls the inner wall toward the coffee temperature and away from the glycol.

---

## 4. Bore selection: holdup is the binding constraint

| Bore | Length | Turns | Holdup | % of a shot | Δp | Wall min. |
|---|---|---|---|---|---|---|
| 2.5 mm | 2.43 m | 10 | 11.9 mL | 30 % | 9.7 kPa | +2.9 °C |
| **3.0 mm** | **2.17 m** | **9** | **15.4 mL** | **38 %** | **4.2 kPa** | **+2.7 °C** |
| 3.5 mm | 1.99 m | 8 | 19.2 mL | 48 % | 2.1 kPa | +2.6 °C |
| 4.0 mm | 1.86 m | 7 | 23.4 mL | 58 % | 1.1 kPa | +2.5 °C |
| 5.0 mm | 1.68 m | 7 | 33.0 mL | 82 % | 0.4 kPa | +2.3 °C |

**Holdup is what matters, and it is why the bore must be small.** Every millilitre left in the coil
between shots is coffee that sits stagnant, in contact with metal, at bath temperature. At 3.0 mm the
holdup is 15 mL — 38 % of a shot — and stagnant coffee reaches bath temperature within ~9 s, so it is
cold, not warm, while it waits. At 5 mm the coil holds 82 % of a shot, which means roughly the last
shot's-worth of coffee is always one shot behind: a first-in-first-out lag that smears batch identity
and makes the first pour of a session stale by construction.

**3.0 mm ID is the recommendation.** Pressure drop is trivial at any of these bores, so the choice is
driven entirely by holdup, with a floor set by fouling risk (below ~2.5 mm, coffee fines and scale
become a blockage concern).

---

## 5. One coil per group — do not share

A single coil sized for one group **fails** when two groups pull simultaneously:

| Recipe | Flow | Outlet | Verdict |
|---|---|---|---|
| Ristretto 18 → 28 g / 22 s | 1.27 g/s | 2.9 °C | pass |
| **Standard 18 → 40 g / 27 s** | **1.48 g/s** | **4.0 °C** | **pass (design point)** |
| Lungo 18 → 60 g / 32 s | 1.88 g/s | 6.5 °C | fail — needs its own coil |
| Fast double 18 → 40 g / 20 s | 2.00 g/s | 7.4 °C | fail |
| Two groups, shared coil | 2.96 g/s | 14.1 °C | **fail badly** |

**Verdict rule, stated explicitly:** the pass/fail column is the single test `outlet ≤ 6.0 °C`.
Lungo at 6.5 °C fails it. An earlier draft of this table called that row "marginal", which
disagreed with `chiller_recipe_robustness.csv` and with the figure generated from the same check;
the table now matches them.

Doubling the flow through a fixed coil halves the NTU, and the outlet runs 10 K warm. Sizing one
shared coil for simultaneous doubles would require ~3.7 m and 26 mL of holdup — worse on both counts
than two independent 2.2 m coils.

**Recommendation: one coil per group head, both immersed in the same bath.** The bath's total duty is
unchanged (the same kJ arrive either way); only the peak becomes simultaneous, at 856 W, which a 4 L
bath absorbs as a 1.5 K excursion. This also keeps each group's shot compositionally distinct until
the manifold — useful if the two groups run different recipes.

**Note the sensitivity:** the design tolerates ristretto and standard recipes comfortably, but a
lungo or a fast-flowing shot lands warm. If your bar runs long shots routinely, size the coil for
your *fastest* expected flow rate, not your nominal one.

---

## 6. Fabrication and integration notes

**Coil forming.** Wind 3.0 × 0.7 mm seamless 316L on an 80 mm mandrel; use a tube bender with an
internal mandrel or fill with sand/low-melt alloy to prevent bore collapse. Target ≥95 % bore
retention through the bends — a kinked coil converts a laminar design into an unpredictable one.

**Orientation.** Mount the coil axis **vertical, flow downward**, so the tube drains completely by
gravity and gas purging sweeps the full bore. A horizontal coil traps liquid in each turn.

**Inlet.** The portafilter-to-coil path must be closed and short. Every millilitre of hot coffee
exposed to air before the coil is oxygen uptake at the worst moment. A silicone or PTFE spout adapter
into a purged inlet fitting is sufficient; the goal is no free surface.

**Outlet.** Discharge below the liquid level in the receiving keg (a dip tube), not splashing into
headspace. Splashing a chilled, oxygen-hungry liquid through an inert headspace still entrains gas
and disrupts the fill.

**Cleaning.** Design for CIP. At 1.0 m/s flush velocity the coil sees Re ≈ 3000 (transitional) at
**424 mL/min** — achievable with a small peristaltic or diaphragm pump. Specify tri-clamp or
compression fittings at both ends so the coil can be removed and back-flushed. Coffee oils polymerise
on stainless over time; plan a caustic or dedicated espresso-detergent cycle daily and an acid
descale cycle on the glycol side schedule.

**Purge.** Three coil volumes is ~46 mL of gas — negligible from any cylinder. Purge the coil with
the same blend gas used in the keg before the first shot of a batch, and again before cleaning.

**Instrumentation.** A thermocouple or RTD at the coil outlet is the single most useful sensor: it
verifies both the chill and the flow rate implicitly. Log it. A second probe in the bath verifies the
setpoint. Neither needs to actuate anything — this is a monitoring system, not a control system.

---

## 7. What to prototype first

1. **Build one coil and measure the outlet temperature across your actual shot recipes.** The
   correlations here are standard (Manlapaz-Churchill for coiled laminar flow, Hagen-Poiseuille for
   pressure drop) but the effective coffee-side coefficient depends on the real fluid's viscosity and
   on the fines it carries. Expect the measured outlet to land within a few kelvin of prediction; if
   it runs warm, lengthen the coil rather than dropping the glycol setpoint.
2. **Verify holdup behaviour with a dye trace** — how much of the previous shot appears in the next.
   That tells you the real first-in-first-out lag and whether 3 mm is tight enough for your cadence.
3. **Check the freeze margin empirically** by walking the glycol setpoint down until you see ice.
   The predicted boundary is −6.5 °C; confirm it before trusting the 12 K window.
4. **Only then integrate the keg and gas side.** Chilling and packaging fail independently; debug
   them separately.

---

## 8. Assumptions and limits

- Coffee treated as water-like (ρ 1010 kg/m³, cp 3900 J/kg·K, k 0.62 W/m·K, µ 0.50 mPa·s hot /
  2.6 mPa·s cold). At 9.5 % TDS this is good to a few percent; the viscosity ratio matters more than
  the absolute value.
- Glycol-side coefficient assumed 1500 W/m²K, typical for a stirred bath around an immersed coil.
  The sizing is insensitive to this — the coffee side dominates the resistance — but the *freeze
  margin* is sensitive to it, in the direction described in §2.
- Freezing point taken as −0.9 to −0.4 °C from two independent colligative estimates. The 3.1 K
  design margin comfortably covers that spread.
- Fouling not modelled. A fouled coil runs warm, not cold, so fouling degrades performance safely —
  but it does drift the outlet temperature, which is why the outlet probe matters.

*Engineering guidance, not a certified design. Have any food-contact fabrication reviewed against
your local food-equipment requirements, and pressure-test the assembly before service use.*
