# Espresso chiller — detailed design package (Rev C)

**Installation:** back-of-kitchen batch production station — **Eversys Enigma E'4s** (Classic /
e'Barista espresso trim) · airpots carried to the front-bar Six Simple Machines **Freepour
Batch** for service
**Machine selection (2026-08-07):** quality-first survey across Eversys / Franke / Thermoplan /
WMF / Schaerer / Rex-Royal / Melitta; Enigma won on triangulated evidence — 24 g chambers +
e'Levelling + electronic tamp + closed-loop Extraction Time Control, Blank Street running a
specialty recipe (20 g → 40 g / ~35 s) chain-wide on this platform, La Cabra deploying it, and a
decade of champion-level engagement. Final gate: a bench trial with your beans at an Eversys NA
showroom (Northvale NJ / Pasadena CA). Dealer list ≈ **$35,160** (E'4s Classic) — machine capital,
separate from the chiller BOM.
**Basis:** "Chiller Design Recommendation.md" (study) + validated parametric model (`model/chiller_model.py`, 74/74 study values reproduced)
**Architecture:** coils inside a commercial glycol chiller's own reservoir under a CNC
"coil cassette" lid (selected in Rev B, carried into Rev C). Selected per the operator's criteria: labor-free, easy maintenance, built on
commercial products, elegant. **Availability rule: every purchased line is stocked on the
manufacturer's own shop or a major retailer.**
**Status:** Design for fabrication. Items marked **VERIFY** must be confirmed before cutting metal.

---

## 1. System overview

Two independent chilling coils — one per Enigma brew module — hang from a CNC-machined lid (the
**coil cassette**, with a capped spare position) inside the 7-gallon stainless reservoir of a
**Penguin Chillers 2/3 HP Stainless XL glycol chiller**, held at **+1 °C**. Each module's shot is
caught at its dual-spout outlet head by a fixed nitrogen-blanketed catch funnel, falls by gravity
through its 3.0 mm-bore 316L coil, and discharges below the liquid surface of a shared airpot
through a custom multi-port bung. When a batch is complete, the bung is swapped for the
Freepour's own stopper and the airpot docks into the front-bar Freepour Batch unchanged. Daily
labor: switch the chiller on and press the recipe button.

| Parameter | Value | Source |
|---|---|---|
| Machine | Eversys Enigma E'4s: 2 brew modules × 24 g chambers, dual-spout outlet per module (manual slide, ≤200 mm cup clearance), ETC grind feedback, 208 V/30 A/4.6 kW, 560 × 743 × 600 mm, 90 kg | Eversys datasheet V3.0 + manual (2026, archived PDFs) |
| Coils | **2** × (316L seamless, Ø4.76 mm OD × 0.89 mm wall — bore 2.98 mm; 2.20 m coiled ≈ 8¾ turns on Ø80 mm centerline) — one per brew module; cassette carries a capped spare position | Study §1, §3–4; DWG D1 |
| Coil duty (each) | 78 → 4 °C at 1.48 g/s; NTU 3.24; holdup 15.3 mL; residence 10.5 s. **Recipe envelope: ≤ 1.7 g/s per module** (e.g. 40 g out in ≥ 24 s; Blank Street-style 40 g/35 s = 1.14 g/s ✓) | Model (validated); §2.1 |
| Cold system | **Penguin 2/3 HP Stainless XL** — 7 gal (26.5 L) open 304 tank, 3,000 BTU/h (879 W) **rated at 28 °F**, flat two-piece lid, $1,999.99 | Mfr. spec sheet, verified |
| Bath | 26.5 L of 35 wt% USP propylene glycol at +1 °C; small in-tank circulator for uniformity | §6 |
| Triple-pull excursion | **0.34 K** (26.5 L bath; the 8 L remote-bath variant saw 1.13 K) | Hand-scaled from validated model |
| Capacity margin | 879 W at −2 °C vs 423 W required at 120 shots/h — **2.1×, at the actual operating temperature** | Mfr. rating + model duty |
| Storage vessel | **Fetco D041 3.0 L** (primary — US-stocked, officially Freepour-supported); Marco BRU 2.2 L via SSM order (alternate) | §2.3 |
| Station bench | **950–1000 mm** (custom-built; sets the gravity head — see §4) | §4 |
| Instrumentation | 3 × PT100 (2 coil outlets + bath) on one Pico PT-104 logger; monitoring only, no actuation | Study §6 |

As-built tube is the stock imperial 3/16 in OD × 0.035 in wall size (bore 2.98 mm), superseding
the study's nominal 3.0 × 0.7 mm — negligible effect on every validated result.

Nothing actively controls anything during a shot: the chiller's own thermostat holds the bath
inside a 12 K-wide safe window (study §2). The one cold-side fault that matters (compressor stuck
on) is covered by the bath-probe alarm (§11).

---

## 2. Integration findings that shape the build

### 2.1 The Enigma is recipe-native — the constraint moves to the recipe envelope
No shot-ending workaround is needed: the Enigma doses, levels, tamps, extracts, and ends shots by
its own volumetric recipes, with Extraction Time Control re-trimming the grinders in real time.
The chiller adds exactly one rule to recipe design: **per-module flow ≤ 1.7 g/s** (the 2.2 m coil
runs warm above it — study §5). Specialty-ratio recipes sit comfortably inside: 40 g out over
≥ 24 s clears it, and the Blank Street-style 20 g → 40 g / ~35 s reference runs at 1.14 g/s with
margin. Program batch beverages as single ~40 g pours per module (both spouts of one head into
one funnel); verify the flow rate against a scale and stopwatch at the bench trial (§14).

### 2.2 The Freepour fill workflow already matches this design
The Freepour Batch (Six Simple Machines Pty Ltd) never fills vessels in place: airpots are filled
elsewhere, the OEM pump-lid is discarded, SSM's reversible stopper (one stopper, flipped for
Fetco vs Marco necks) with dip tube goes in the bare neck, and the pot docks into the
under-counter frame where magnets connect the dip tube. Our chiller fills the airpot at the
station through our own bung (§7); the swap to the SSM stopper at service time is the same
gesture SSM's workflow already requires.

### 2.3 Vessel: Fetco D041 primary, and the bench height buys the head margin
**Fetco D041 3.0 L** — H 457 mm, W 181 mm, capacity 3.0 L (75 shots/pot), $122.99 at
WebstaurantStore / $154.99 Prima Coffee, officially Freepour-supported — is the vessel that
passes the availability rule. The Marco BRU 2.2 L is not US-stocked (UK/EU retail only; appears
to be a rebadged Elia BFJ-22S, 370–390 mm tall); it remains an alternate **ordered through SSM
with the Freepour system** (SSM supplies airpots "if specifically ordered").

Gravity head, cold-viscosity worst case (model): 47 cm needed at the 1.48 g/s design recipe,
62 cm at a 2.0 g/s fast double. Available head = funnel surface − full-pot surface:

| Bench height | Funnel surface | Fetco full (~430 mm) | 1.48 g/s (47 cm) | 2.0 g/s (62 cm) |
|---|---|---|---|---|
| 950 mm | ~1045 mm | available ~61 cm | ✓ | line-ball — funnel pools briefly at end of fill (benign, self-regulating) |
| **1000 mm ← spec** | ~1095 mm | available ~66 cm | ✓ | ✓ |

**Specify the station bench at 1000 mm** (also better production ergonomics than 910). Fills may
also simply stop at 2.6 L for fast-flow recipes at a lower bench. Between shots the siphon stays
primed (outlet submerged), so priming allowances apply only to an empty pot, when head is
abundant.

### 2.4 The Freepour prohibits solids — flag fines with SSM
Espresso fines settle; the Freepour draws from the bottom, and its manual says no solids. Cut
both our fill dip tubes and the SSM dip tube ~10 mm proud of the pot bottom, and follow one SSM
regimen exactly — plain coffee: **daily water rinse + weekly SSM Weekly Coffee Cleaner**; if SSM
classes espresso as acidic: **Daily Juice Line Cleaner, daily**. Fold both the fines question and
the regimen question into one **VERIFY with SSM** conversation (their branded cleaners are a
warranty condition).

### 2.5 Machine facts the station depends on (Eversys datasheets V3.0 + manual, archived)
Enigma E'4s Classic: **560 W × 743 H × 600 D mm, 90 kg**; one 208 V / 30 A / 4.6 kW circuit (far
lighter than the Strada's 50 A); water G3/8 in at 2.5–4.0 bar, **≥ 200 L/h**, spec 5–8 °dGH /
≤ 6 °dKH / pH 7.0–7.2 / Cl ≤ 0.1 mg/L (water treatment is a warranty condition — budget it);
drain Ø22 mm hose to a ≥ Ø56 mm siphon with continuous fall; **≥ 250 mm clearance above the
machine** for hopper refill (≈ 2.0 m total height over a 1 m bench); ambient 10–32 °C. Two
outlet heads (~one module ≈ 280 mm apart — **measure**), each manual-slide with **≤ 200 mm cup
clearance**; spout-to-spout pitch within a head is **unpublished — measure at the demo** before
machining funnels (§14). No under-bench machine hardware (no external pump — the under-bench
zone belongs entirely to the chiller, N2, airpot bay, and water treatment).

### 2.6 Outlet rinses are session-boundary events — the diverter is a session valve, not a shot valve

What the Enigma discharges through its coffee outlets, per the manual: a mandatory hot-water
rinse at **power-on**, a rinse at **switch-off**, an optional pre-heat rinse after **~10 min
idle** (service-enabled), service-configurable interval rinses ("after x minutes unused or y
products"), and the scheduled **daily ~12-min clean** (hot cleaning-ball solution + steam).
**None of these fire between back-to-back shots during active batching** (operator-confirmed
framing, 2026-08-07); post-shot spout drips are product, not rinse water, and belong in the
batch. The funnel diverter (BATCH / WASTE, detented) therefore operates **per session, not per
shot**: WASTE is the resting state (power-on/switch-off rinses and the daily clean fall to the
tray unattended); flick to BATCH once at session start, back to WASTE at session end. Residual
mid-session paths — the 10-min idle rinse during a lull, and product-count interval rinses —
are closed at service setup (configure idle/interval rinses off or beyond session length for
the batching profile, §14) with the valve as insurance; if a pause will exceed ~5 min, flick
WASTE. (The Strada's portafilter constraints — swing arcs, kidney slots — are deleted: there is
no portafilter, and the funnels are fixed, permanently plumbed catches.)

---

## 3. Thermal design (validated model, Rev B values)

The model reproduces every study value (max deltas 0.118 K outlet / 0.030 K wall / 10 mm length);
conventions in `model/README.md`. Rev B applies it to the XL's larger bath:

- **Bath 26.5 L**: triple-pull excursion **0.34 K** (vs 1.13 K in the 8 L remote-bath variant) —
  the bath barely notices a simultaneous three-group pull. Duty unchanged: 232 / 328 / 423 W at
  60 / 90 / 120 shots/h including heat leak.
- **Chiller**: 879 W at −2 °C (manufacturer rating at temperature — no derating guesswork).
  Enigma duty: both modules running specialty recipes back-to-back ≈ 2 × 1.1–1.5 g/s ≈
  **660–860 W sustained** — inside the 879 W envelope, with the 26.5 L bath absorbing bursts
  (a full 75-shot pot at maximum pace ≈ 13 min ≈ ≤ 1.7 K excursion, recovered between pots).
  Only continuous multi-pot production beyond ~250 shots/h argues for the 1 HP XL step. Pulldown of 26.5 L from 25 °C: roughly 50–70 min —
  switch on an hour ahead, or leave it running (duty ≈ heat leak ≈ tens of watts when idle).
- **Freeze safety**: setpoint +1 °C sits mid-window (−6.5 to +5.2 °C usable). Worst flowing
  cold-end wall +1.8 °C; stagnant holdup waits at bath temperature, ~10 s to equilibrate.
- **CIP**: 500 mL/min → Re ≈ 3500 (≥ the study's 424 mL/min / Re 3000 minimum).

Model outputs and plots (bore/setpoint/recipe validation, duty curves): `model/outputs/`.

---

## 4. Station arrangement (drawing D3)

Floor datum; custom bench at **1000 mm** (spec §2.3; 950 mm acceptable with the fill cap noted):

| Element | Elevation | Note |
|---|---|---|
| Funnel free surface | ~1100–1180 mm | fixed catch under each module's dual-spout head; the manual-slide spout (≤ 200 mm clearance) lets the funnel sit high — every cm of slide is a cm of gravity head |
| Bench top / underside | 1000 / ~960 mm | custom station bench |
| Cassette stubs / inverted-U crest | ~820 / ~800 mm | stubs rise through the bench access hatch |
| Chiller tank rim (unit height) | 787 mm | Penguin XL stands on the floor — no stand needed |
| Glycol level | ~757 mm | ~30 mm below rim |
| Coil (in tank) | ~730 → ~630 mm | axis vertical, inlet top, flow downward |
| Fetco bung / neck | ~470 mm | continuously downhill from the U-crest ✓ |
| Airpot on floor | 0 mm | beside the chiller; slides out after unplugging jumpers |

**The hatch:** the Penguin XL (457 × 457 × 787 mm, 75 lb) sits on the floor under the bench,
directly behind/beside the machine, with a **≥ 420 × 420 mm access hatch** in the benchtop above
its tank. The cassette lid lifts out through the hatch — all three coils withdraw together for
inspection or descale. The three drop lines run from the funnels through Ø25 mm bench holes
(positions per **measured** group spacing) and down through the hatch zone onto the cassette
stubs; every hot-side run ≤ 40 cm and continuously downhill (funnel necks exit rearward over the
tray lip — lip height is a measure-first item, §14).

**The over-rim exit (the one physics trade):** product leaves each coil upward through the
cassette lid via a small inverted-U cresting ~40 mm above the glycol level (~800 mm elevation),
then falls continuously to the airpot bung. Once primed — first shot of a session, driven by
~25+ cm of funnel-to-crest head — the U is hydraulically invisible. It holds ~2 mL that gravity
cannot drain; the end-of-batch **N2 purge clears it** (the study requires the purge regardless).
If Penguin's tank wall proves drillable on inspection, a low bulkhead restores strictly-downhill
as a refinement — not assumed.

**Under-bench zone:** chiller (needs condenser airflow — leave the louvered faces ≥ 100 mm
clear), LM rotary pump (12 × 12 × 12 in ventilated), N2 cylinder clamped to the frame, airpot bay
with slide-out floor position, CIP shelf. Power: chiller 110–120 V / 3.9 A ordinary outlet;
machine NEMA 6-50; logger USB to any laptop/NUC.

## 5. Coil module — fabrication spec (×3) (drawing D1)

Unchanged from the reviewed drawing except **quantity: 2 (+ material for a spare)** — D1 is
architecture-independent: 316L seamless 3/16 in × 0.035 in wall, ASTM A213 annealed; wound on
Ø72–75 mm mandrel to Ø80 ± 5 mm centerline; ~8¾–9 turns, pitch 8–10 mm, stack ≤ 100 mm;
developed ≈ 2.48 m, **cut 2.6 m, trim at fit-up**; legs formed last (note 8); ≥ 95 % bore
retention, no kinks; degrease + citric passivate per A967. Fittings: Swagelok 3/16 in 316
compression (SS-300 series) + bored-through RTD glands. Both legs pass through the cassette lid;
the outlet leg rises alongside the coil to the inverted-U.

## 6. The coil cassette (drawing D5)

A CNC-machined flat plate replacing the Penguin XL's rear lid section (the stock lid is already a
flat two-piece plate with pass-throughs — **get the lid drawing / tank interior dims from Penguin
before machining, §14**):

- **Material:** 25 mm HDPE (food-safe, insulating, machinable) or 316 plate; gasketed to the rim.
- **Carries:** three coil stations on an **in-line 120 mm pitch row** (envelope Ø85 mm each —
  fits the estimated ~340 mm tank with room beside the row for the circulator; recheck pitch vs
  the Penguin interior + evaporator position): stations 1–2 active, **station 3 a capped spare**;
  per station an inlet stub + outlet pass-through with the inverted-U bend; the T4 bath RTD
  gland; lifting handles; a Ø50 mm glycol top-up port with cap.
- **Circulator:** the XL ships without pumps — add one small submersible circulator (bayite
  BYT-7A015 class, 8 L/min) beside the coil row, cable through a lid gland, jetting along the
  coils for bath uniformity (h_o ≈ 1500 W/m²K assumption; verify with the commissioning outlet
  logs).
- **Glycol:** 35 wt% USP propylene glycol in distilled water, ~9–10 L concentrate for 26.5 L.
- The front lid section stays stock for future servicing of the tank.

## 7. Airpot interface — multi-port bung + gas (drawings D7, D2)

Machined food-grade silicone or PTFE-faced acetal plug for the **Fetco D041 neck — neck ID is
published nowhere; machine from a measured pot** (§14). SSM's own reversible stopper proves a
stepped bung can serve both Fetco and Marco necks if the Marco alternate is ever ordered.

- **2 × fill dip tubes** (3/16 in 316, one per coil) to 10 mm off the pot bottom, tips cut 45°;
  discharge below the liquid surface from the first ~100 mL onward.
- **1 × gas port** teed to an N2 trickle (0.5–1 L/min during fill) and a free vent; valve closed
  and vent capped for storage after the batch.
- **Jumpers — the designed disconnect:** each cassette outlet connects to its bung dip tube
  through a short food-grade silicone push-fit jumper. Unplug three jumpers by hand, lift the
  bung ~350 mm clear, swap in the SSM stopper, carry the pot to the front bar. Compression
  fittings are assembly joints and are never touched in operation. The jumper is also the CIP
  waste point (§10).

### 7.1 Nitrogen system (drawing D4)

One **40 cu ft beverage-grade N2 cylinder** (CGA580, secured upright to the station frame) → beer-gas
nitrogen regulator set to a **10 psi header** → 4-port manifold → three independently metered legs,
each: isolation ball valve → needle valve → rotameter → check valve → termination.

| Leg | Duty | Flow | Termination |
|---|---|---|---|
| A — funnel blankets | continuous while batching | ~1.0 L/min total (≈0.33/funnel, balanced by 0.5 mm lid orifices) | 1/8 in lines to the three funnel-lid galleries |
| B — bung sweep | during fill only | 0.5–1 L/min | QD to the bung gas tee; **vent always open while gas flows** |
| C — coil purge | ~40–60 s per coil, per event | ~0.1 L/min (plug advances ~0.25 m/s in the 3 mm bore) | QD to the tapered purge stopper seated in the funnel mouth |

**Rules:** the airpot is a vacuum flask, not a pressure vessel — nothing ever sees more than
~0.5 psi at a vessel; the bung vent is a low-crack one-way check (outflow only), capped for
storage. Purge = 3 coil volumes ≈ 60 mL, entering at the funnel and pushing forward over the
inverted-U into the pot (start of session: clears air; end of session: recovers the held product).
**Consumption ≈ 2 scf per 40-min session** → a 40 cu ft cylinder lasts ~2–4 weeks at daily
batching; swap at any welding/beverage gas supplier.

## 8. Inlet interface — blanketed catch funnel (×2) (drawing D6)

One fixed CNC 316 catch per brew module (×2): an oval catch cup spanning **both spouts of that
module's outlet head** (spout pitch measured at the demo, §14), ~30 mL surge volume, sitting on
**locating tabs** on the drip tray with a **rear-exiting continuously-downsloping neck**. The
spout head slides manually — set it low over the funnel for splash-free capture (or higher to
add gravity head; the funnel lid's twin openings are simple slots sized to the measured spout
positions, since nothing ever swings through them). N2 gallery in the lid as per D4.
**Diverter (§2.6):** the neck feeds a mini 3-way valve — BATCH to the 3/16 ID silicone drop
line, WASTE to a short stub over the tray — detented, **WASTE resting state**, operated once
per session. The valve's ~1–2 mL passage is part of the CIP path (flick through both positions
during the rinse). The lid (316 or PTFE disc) carries two spout slots and an **annular gas gallery**: N2
enters a 10-32 port into a perimeter groove and issues through 6–8 × 0.5 mm holes angled down at
the liquid surface — a gentle inert curtain, with excess gas flowing *out* through the spout
slots so room air never flows in (detail on drawing D4). For purge events the lid lifts off and
a **tapered silicone purge stopper** (with 1/4 in barb, leg C) seats in the funnel mouth —
self-sealing at the ~0.3 psi purge pressure. The funnel is the system's surge buffer
(§2.3). A sealed portafilter quick-dock remains a future option (removes the head constraint
entirely; per-shot docking gesture; not v1).

## 9. Instrumentation

3 × PT100 Class A 1/8 in (2 coil outlets in bored-through tees + 1 bath probe in the cassette
gland) → one **Pico PT-104** (Saelig/TEquipment, $809): outlet probes verify chill and flow
implicitly; the bath probe verifies the thermostat and provides the < −4 °C stuck-compressor
alarm. Budget route: Inkbird IBS-TH2 bath trending only. Nothing actuates anything.

## 10. Cleaning and sanitation

- **Daily:** N2-purge coils to the airpot; peristaltic CIP (Kamoer dosing pump, 500 mL/min ≈
  Re 3500) with espresso detergent through funnel → coil → **waste at the bung jumper** (clamp
  the 1.5 in TC waste adapter onto the unplugged jumper; run the three coils sequentially); rinse
  to neutral. No compression fitting is ever opened for cleaning.
- **Weekly:** acid descale of the product path. **Periodic:** lift the cassette — all three
  coils out in one motion for inspection/back-flush.
- **Airpots:** the SSM regimen confirmed in §2.4.
- **Glycol side:** closed and stock; glycol per Penguin's schedule; the chiller remains a
  serviceable commercial appliance (1-yr warranty; extensions $229.99 / 2 yr, $339.99 / 3 yr).

## 11. Operating workflow (batch day)

1. Chiller runs continuously (or on ≥ 1 h ahead for 26.5 L pulldown); verify bath +1 °C on the log.
2. N2-purge each coil (3 volumes ≈ 46 mL); seat the bung in a clean Fetco; N2 trickle on.
3. Machine on → power-on rinse falls to WASTE → **flick both diverters to BATCH** → run the
   saved batch recipe back-to-back on both modules — 75 shots per Fetco pot, no per-shot valve
   touches (§2.6; pauses > ~5 min: flick WASTE). The RTD log verifies every shot's outlet
   ≤ 6 °C.
4. Batch done: N2 off, vent capped → unplug jumpers, swap to SSM stopper → carry to the Freepour.
5. Daily CIP (§10).

**Failure modes:** fouled coil → outlet drifts warm (visible in log; degrades safely); chiller
fault-off → 26.5 L warms very slowly, shots read warm, no freeze path; blocked coil → funnel
overflows to the drip tray (benign); **compressor stuck on** → bath can fall below setpoint
toward refrigeration equilibrium — the T4 alarm at −4 °C fires well before the −6.5 °C
wall-freeze boundary, and commissioning step 3 confirms that boundary empirically.

## 12. Bill of materials

**`BOM.csv`** — every purchased line from the manufacturer's shop or a major retailer, with
sources and confidence. Totals (summed from the line items): **~$5.5 k** with the PT-104 lab
logger, **~$4.1 k** with budget instrumentation (incl. the full D4 gas train and the three
funnel diverters). The chiller is now half the parts cost — the price of buying the entire cold
system as one warranted commercial appliance. Excludes fabrication labor (coils, cassette,
funnels, bungs, station frame) and the machine/Freepour (owned).

## 13. Prototype and commissioning sequence

The architecture makes the prototype the product:

0. **Bench trial at Eversys North America** (Northvale NJ / Pasadena CA) with your beans: dial
   the batch recipe to taste — this is the quality gate the machine was chosen on — and while
   there, take the §14 measurements (head/spout pitch and spacing, tray geometry, slide range,
   recipe flow rate on a scale, rinse behavior). Buy the machine on the cup, not the brochure.
1. **Buy the XL, wind one coil, hang it from a temporary lid blank** (plywood/HDPE offcut), run
   one module's saved recipe across the real beverages. If outlet runs warm, lengthen the coil —
   never drop the setpoint (study §7).
2. **Dye-trace the holdup** (count pours to clear) — confirms the ~15 mL FIFO lag incl. hot side.
3. **Walk the setpoint down** until wall ice appears — confirm the −6.5 °C boundary, then return
   to +1 °C and set the T4 alarm at −4 °C.
4. **Machine the real cassette** (with Penguin's lid/tank drawings + measured fit), install both
   coils, run both modules simultaneously — expect a barely visible bath excursion on the log
   (≤ ~0.4 K).
5. **Airpot + gas side:** bung fit to the measured Fetco neck, N2 sweep, 75-shot fill, stopper
   swap drill.
6. **Dock and dispense** through the Freepour at the front bar; confirm pour quality and the SSM
   cleaning regimen fit.

## 14. Verify-before-build list

| # | Item | Why it matters | How |
|---|---|---|---|
| 1 | Enigma outlet-head spacing (est. ~280 mm module pitch — unpublished) + spout-to-spout pitch within each head | funnel positions, twin catch openings | measure at the Eversys NA demo |
| 2 | Spout slide range and chosen working height (≤ 200 mm clearance) | funnel height, splash, head budget | set at the demo / commissioning |
| 3 | **Penguin XL interior tank dims + lid drawing** | cassette machining, coil fit | phone Penguin before ordering |
| 4 | **Fetco D041 neck ID** (published nowhere) | bung machining | measure a pot in hand |
| 5 | SSM: espresso/fines acceptability + which cleaning regimen | warranty, sanitation cadence | ask SSM |
| 6 | Bath uniformity with one circulator (h_o ≈ 1500 assumption) | outlet temps at spec | commissioning outlet logs |
| 7 | Tube cert: annealed 316L A213 | winding without kinks | order paperwork |
| 8 | **Batch-recipe flow ≤ 1.7 g/s per module** for every beverage you'll batch (incl. the bench-trial quality recipe) | coil outlet ≤ spec (§2.1) | scale + stopwatch at the bench trial |
| 9 | Enigma drip-tray lip height + tray geometry (unpublished) | funnel neck downhill rule, locating tabs | measure at the demo |
| 10 | Rinse triggers + volumes: configure idle/interval rinses for the batching profile; measure one power-on rinse | diverter workflow §2.6 | Eversys service setup + one-time measurement |
| 11 | Bench height final (1000 mm spec) | head budget §2.3 | station design freeze |
| 12 | Water treatment to Eversys spec (5–8 °dGH, ≤ 6 °dKH carbonate, pH 7.0–7.2, Cl ≤ 0.1 mg/L) | machine warranty + extraction consistency | water report + treatment selection |

## 15. Alternates considered (kept for the record)

- **Remote-bath variant (Rev A):** chiller + separate 8 L insulated pot, fully designed and
  adversarially reviewed in the 2026-08-07 Rev A of this package; falls back into play only if
  the XL tank surprises on interior dims. Its numbers: 1.13 K triple-pull excursion, Penguin 1/3 hp
  (1.25 gal tank — too small to host coils, fine as a remote cold source).
- **Ice-bath / jockey-box:** minimum capex (~$1.3 k), zero refrigeration, structurally
  freeze-proof — rejected on daily labor and elegance; remains the cheapest possible
  taste-validation prototype (any stainless-coil jockey box).
- **Beer flash cooler (Lindr/UBC class):** fully integrated commercial box, but internal coils
  hold 250–350 mL (6–8 shots of FIFO smear vs our 15 mL) — the study's §4 bore logic is exactly
  why we wind our own.

## 16. References

- Study: `Chiller Design Recommendation.md` + 3 CSVs · Model: `model/` (validated) ·
  Drawings: `drawings/D1–D4` · BOM: `BOM.csv`
- Penguin 2/3 HP Stainless XL: penguinchillers.com/products/2-3-hp-xl-glycol-chiller + spec-sheet
  PDF (verified vs Brewers Hardware, Delta Brewing, Florida Brewing)
- Strada X: LM manual MAN.35.1, product page, 2025 brochure (lamarzoccousa.com)
- Freepour Batch: SSM manuals D00164 A01 / D00162 A04 (sixsimplemachines.com.au)
- Fetco D041: fetco.com/dispensers/p/d041 + Use-and-Care PDF; WebstaurantStore; Prima Coffee

*Engineering guidance, not a certified design. Food-contact fabrication should be reviewed
against local food-equipment requirements; pressure-test assemblies before service (study §8).*
