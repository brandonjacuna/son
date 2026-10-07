# Blender handoff brief — espresso batch fill station

**For:** a Claude Code session with Blender. **Deliverable:** photoreal renders of (a) the whole
back-of-house fill station on its counter, and (b) the gas-blanket assembly in high detail.

**Scope.** Back-of-house only: pull shots, chill each one inline, fill ONE keg at a time under an
oxygen-free gas blanket, hold it at ≤4 °C until it is carried to the front of house. **There is no
tap and no dispensing hardware in this scene** — that lives in the front area and is not designed.

Everything here is design intent, not a built object. Nothing has been measured or prototyped.

---

## 1. Files in this package

| File | What it is |
|---|---|
| `build_scene.py` | Parametric Blender build. Run it first; it produces the whole scene, 5 cameras and lighting. |
| `blender_component_schedule.csv` | Every part with dimensions, material key, and **provenance** — read this column. |
| `blender_placement.csv` | Plan footprints (x0, y0, L, W) in mm. |
| `fig_fill_station_layout.png` | Dimensioned plan + elevation. The authority on placement. |
| `fig_chiller_drawing.png` | Dimensioned coil and bath detail. |

**Read the `provenance` column before trusting any number:**

- `DERIVED` — computed from the thermal/fluid design. Exact. Changing these changes the engineering.
- `PUBLISHED` — real manufacturer specification, sourced. Trustworthy.
- `SET` — a design decision made here. Reasonable, adjustable.
- `VERIFY` — **representative envelope only.** The espresso machine, grinder, glycol pack and fill
  well are placeholder boxes at plausible sizes. Swap in real models or real drawings; do not
  present these as specified equipment.
- `CUSTOM` / `DESIGN_NOTE` — must be built, or carries a caveat. Read the note.

---

## 2. Coordinate system and units

Origin at the counter's **left end / front edge / floor**. +X right along the run (0–2000 mm),
+Y back toward the wall (0–650 mm), +Z up (floor 0, counter top 900 mm).

The script works in metres (`MM = 0.001`) because Blender's unit scale is 1 m = 1 BU. Every
dimension in the CSVs is millimetres.

---

## 3. The coil — the one part with no off-the-shelf equivalent

A helical 316L tube in a chilled glycol bath. Every number is `DERIVED` and exact:

| | |
|---|---|
| Tube | 4.4 mm OD × 0.7 mm wall → **3.0 mm bore** |
| Helix | Ø80 mm centreline, **9 turns**, **15.5 mm pitch** |
| Developed length | **2266 mm** |
| Rise over 9 turns | **139.5 mm** (first-to-last turn centres: 124.0 mm) |
| Gap between turns | **11.1 mm** — glycol flows between them; do not close this up |
| Internal volume | **16.0 mL** |

`build_coil()` generates it as a poly curve with a round bevel. For a cutaway, add a Solidify
modifier of 0.7 mm. Use `res=24` points per turn for wide shots, `res=48` for the detail camera.

**Flow is UPWARD. Inlet at the bottom, outlet at the top.** This is not arbitrary and it reversed
an earlier version of the design: espresso leaves the group head about 3× supersaturated with CO₂,
so the hot first third of the coil carries up to 35 % gas by volume. A CO₂ bubble rises at roughly
200–250 mm/s and the liquid moves at 207 mm/s — comparable speeds, so a downward-flowing coil can
stall bubbles and gas-lock. Model the drain valve at the low point.

Two coils, one per group head. A shared coil fails when both groups pull at once.

---

## 4. The gas blanket — model this in high detail

This is the component the whole system exists for, and it is worth the polygon budget.

### 4.1 What it is, and what it is not

The keg holds a **4 L batch in a 6 L vessel**, leaving **2.0 L of headspace** filled with a
nitrogen/CO₂ blend instead of air. Oxygen is what destroys batched espresso; excluding it is worth
roughly **+40 percentage points** of aroma-compound retention at 24 h, against essentially nothing
for chilling faster. The blanket is the product.

> **This is not nitro coffee.** No stout faucet, no restrictor plate, no cascade, no foam. A nitro
> dispense system would strip the coffee's CO₂ and is the opposite of what this design wants. If
> you have seen nitro cold-brew references, do not use them.

Vessel sizing matters and is easy to get wrong: a 19 L keg holding 4 L would carry **200 mg of
oxygen in its headspace even at 1 %** — about 166× the entire 6-hour ingress budget. Hence 6 L.

### 4.2 Parts to model (all in `build_keg_assembly()`)

| Part | Detail |
|---|---|
| Keg body | Ø229 × 279 mm, 304 stainless, brushed. Domed top and bottom, rolled handles. |
| Lid | Oval, bail-retained, with a **pull-ring pressure relief valve**. |
| Ball-lock posts ×2 | 19 mm hex, 28 mm tall, 76 mm apart. Gas post has a **notched collar**; liquid post is plain. |
| Quick disconnects | Ø26 × 52 mm. **Grey = gas, black = liquid** — the industry convention; get it right. |
| Liquid dip tube | Ø7.9 mm, to **5 mm off the floor**. This is the fill path. |
| Gas tube | Ø7.9 mm, **25 mm long** — stops in the headspace. If it reached the liquid it would sparge out the CO₂. |
| Liquid body | 4 L → **97 mm deep**. Very dark, slightly translucent at the meniscus. |
| Headspace | 2.0 L → **182 mm**. Render as a faint volumetric tint so it reads as *present*. |
| Sight-glass boss | Ø25 mm window in the wall at mid-liquid height. |
| O₂ sensor spot | Ø5 mm pink-orange disc bonded **inside** the glass. |
| Purge/vent manifold | 180 × 90 × 110 mm, 316 stainless. Custom. |
| Vent bubbler | Ø60 × 180 mm water-filled glass one-way vent. |

**The sight glass is a real design catch, not decoration.** Optical oxygen sensor spots are read
*through* a transparent wall. A stainless keg is opaque, so the instrumented keg needs a welded
window. Modelling it correctly makes the render technically honest.

### 4.3 The fill sequence — this drives the hardware

Worth understanding before modelling the manifold, because it is why the vent exists.

**You cannot gravity-fill a pressurised keg.** At the 11.7 psig working setpoint the keg needs
8.14 m of liquid head to push into; the spout sits 645 mm above the keg post. A 13× shortfall. So:

1. **Purge the empty keg** with **4 headspace volumes (≈24 L)** of blend gas → 0.38 % residual O₂.
   (3 volumes gives 1.04 %, which misses the <1 % target — an earlier spec said 3; it was wrong.)
2. **Fill at atmospheric pressure** through the dip tube. Displaced gas leaves through the gas post
   and the **vent bubbler**, which lets gas out but stops air diffusing back in. The keg is never
   open to air because it is already full of blend gas.
3. **Seal and pressurise** the headspace to **11.7 psig** with the same blend — this sets the CO₂
   partial pressure to 0.45 bar and holds the coffee's own carbonation.
4. The keg goes to front-of-house. Hold at ≤4 °C throughout.

Gas budget ≈ **29.6 L per batch**; a 20 cu ft cylinder covers about **19 batches**.

**Gas spec:** standard "beer gas" / Guinness gas, **25 % CO₂ / 75 % N₂**. Order it by composition,
never by the two-number shorthand — a UK "30/70" means 30 % CO₂ while one US blender calls 70 % CO₂
its "lager blend", and getting that backwards over-carbonates the coffee.

A **bench scale under the keg** reads batch mass live: 4.04 kg = 100 shots.

---

## 5. Materials

| Key | Base colour | Metallic | Roughness | Notes |
|---|---|---|---|---|
| `steel_304_brushed` | 0.62, 0.63, 0.64 | 1.0 | 0.35 | Anisotropic brush, vertical on the keg body |
| `steel_316L_bright` | 0.70, 0.71, 0.72 | 1.0 | 0.18 | The coil — brighter, drawn-tube finish |
| `coffee_dark` | 0.07, 0.035, 0.018 | 0 | 0.15 | α 0.92, IOR 1.36. Very dark, not black |
| `blanket_gas` | 0.55, 0.78, 0.88 | 0 | 1.0 | α 0.10. A hint, not a fog bank |
| `glass_clear` | 0.95, 0.97, 0.98 | 0 | 0.02 | α 0.08, IOR 1.52 |
| `plastic_grey` / `plastic_black` | 0.52 / 0.04 | 0 | 0.55 / 0.50 | Gas and liquid disconnects |
| `stone_honed` | 0.78, 0.76, 0.72 | 0 | 0.45 | Counter |
| `foam_closed_cell` | 0.16, 0.17, 0.18 | 0 | 0.85 | Bath jacket |

Add fine fingerprint and water-spot roughness variation to the stainless. Perfectly clean steel
reads as CGI; a working bar surface does not.

---

## 6. Shots

`add_cameras()` creates five. Requested first:

1. **`CAM_station_wide`** — 35 mm, the whole station on the counter. The brief's main ask.
2. **`CAM_station_34`** — 50 mm three-quarter from the right.
3. **`CAM_blanket_hero`** — 85 mm, f/4, keg at close range with the cutaway live, so liquid level,
   headspace, dip tube and gas tube all read at once. **This is the detail shot.**
4. **`CAM_blanket_top`** — 60 mm looking down on the two posts, disconnects and manifold.
5. **`CAM_coil_detail`** — 100 mm, f/4, coil in the bath. Render once with the bath wall hidden.

Cycles, 256 samples with denoising, 2400 × 1600, AgX view transform.

Suggestions worth taking: a cutaway variant of the keg (boolean a 90° wedge out of the body) reads
far better than a transparent shell; and a second blanket render with the gas volume tinted more
strongly than physical makes the point even though it is not photoreal.

---

## 7. Known gaps — do not invent these

- **Espresso machine, grinder, glycol pack, fill well are placeholder boxes** at plausible sizes.
  Replace with real assets or drawings. Do not let a render imply a specific product.
- **Tube bore is a design optimum, not a catalogue item.** 3.0 mm may not be a stocked size. If the
  real bore differs, the coil length changes and the model must be regenerated.
- **Plumbing runs between coil outlet and keg post are not specified** — route them plausibly and
  flag that you did. `coil_endpoints_mm()` gives the coil ends.
- **The purge manifold is a size envelope, not a design.** Internal porting is not worked out.
- **No electrical, no drainage, no splash zone** has been considered.

If something needed to complete a shot is not in the schedule, model it, and say in your reply that
you invented it. A render that quietly fills gaps is worse than one with a stated hole, because
this package may end up in front of a fabricator.
