# Cold sonication + pulsed-agitation keg: system design analysis

Both points raised are correct and both are quantifiable. Pulsed agitation resolves the
flocculation risk essentially completely, and the batch-in-the-storage-vessel workflow
removes the two largest labor items from the hot/blender route — which are exactly the
messy ones.

All numbers are first-principles or task-time models with stated assumptions.

---

## 1. Pulsed agitation: the parameter has a wide safe window

A 7 µm matcha particle settles at **18.4 mm/h**. In a 250 mm keg column, the question for
pulsed stirring is how much clarified layer forms at the top between pulses, and what dose
error that causes when product is drawn.

| Gap between pulses | Clarified layer | Dose concentration error |
|---|---|---|
| 5 min | 1.5 mm | 0.6 % |
| **15 min** | **4.6 mm** | **1.9 %** |
| 30 min | 9.2 mm | 3.8 % |
| 60 min | 18.4 mm | 7.9 % |
| 120 min | 36.7 mm | 17.2 % |

**A 15-minute pulse interval costs under 2 % dose error** — well inside a ±10 % spec and
below the ~15–25 % perceptual threshold by a wide margin. Even hourly pulsing stays within
spec. The design is forgiving.

Re-homogenization after a pulse takes about **5 seconds**, so a 15-minute interval is a
**0.5 % duty cycle**. Practical consequences:

- Time-averaged shear drops from G ≈ 46 s⁻¹ (continuous) to **G ≈ 0.24 s⁻¹**.
- Stirrer energy input, already negligible, becomes irrelevant — no measurable heating.
- A simple interval timer on a stir plate is sufficient. No control loop needed.

### 1.1 This solves the flocculation risk

The re-flocculation concern from the continuous-stirring analysis was driven by
orthokinetic (shear-driven) collisions. Cutting time-averaged shear by ~190× moves the
aggregation half-time accordingly:

| Regime | Time for flocs to form (α = 0.01) |
|---|---|
| Continuous stirring (G = 46 s⁻¹) | **1.3 min** |
| Pulse every 5 min | 81 min |
| **Pulse every 15 min** | **234 min (~4 h)** |
| Pulse every 60 min | 802 min (~13 h) |
| No shear (Brownian only) | 4,187 min (~3 d) |

At a pessimistic α = 0.01, 15-minute pulsing gives a ~4 h half-time; at a more likely
α = 0.001 it is ~39 h. **Pulsing converts flocculation from a live design risk into a
non-issue for a service-day hold.** This is the single strongest argument for pulsed over
continuous, independent of the labor and energy considerations.

**Recommended starting point: pulse 5 s every 15 min.** Then measure — §5 item 1.

---

## 2. The thermal-route penalty, quantified

The objection that chilling introduces its own inconsistency is correct and was
under-weighted in the earlier analysis. Modeling the hot/blender route with realistic
operator variation (start temperature ±3 °C, blender self-heating, ice-bath effectiveness
varying 0.5–1.0, operator-dependent tending):

- **Chill time spans 0.16 h to 0.46 h between the 10th and 90th percentile** — nearly a
  3× spread on the same nominal procedure.
- **Thermal load CV ≈ 0.42.** Every batch receives a materially different heat exposure,
  which propagates into volatile loss and extraction-in-transit.

The cold sonication route has a mean thermal load near zero and no chill step, so this
variance term does not exist rather than being managed. **A batch-to-batch inconsistency
that cannot be eliminated by better technique is worse than one that can** — the ice bath
depends on ice quantity, ice age, ambient temperature, vessel wall thickness, and how
attentively someone stirs it. None of those are controlled in a working kitchen.

---

## 3. The parallel workflow: dose-then-sonicate-in-vessel

The workflow described — pre-dose a dozen storage vessels with powder and cold water,
sonicate each in its final container, cap, label, store — is materially better than the
one modeled earlier, because it eliminates the transfer step entirely.

Labor for 144 drinks (12 vessels × 12 drinks):

| Route | Prep labor | Items to wash |
|---|---|---|
| Cold + sonication, batched in-vessel | **28 min** | 13 (probe + 12 vessels) |
| Hot + blender | 80 min | 27 (blender jug, chill bowls, vessels) |

**64 % less labor, and roughly half the washing.** The decisive detail is *where* the hot
route spends its time: **chilling and washing the blender alone account for 40 % of the hot
route's labor.** Those are the two steps the cold in-vessel workflow deletes outright —
not optimizes, deletes.

Three structural advantages worth naming:

1. **The vessel is the reactor.** Sonicating in the final container removes a transfer, a
   dirty intermediate, and a contamination point. The blender route cannot do this — the
   jug is not the storage vessel.
2. **The probe is the only shared surface.** A rinse between vessels (~12 s) versus washing
   a blender jug between batches (~70 s). This ratio is why the labor gap widens with
   batch count rather than amortizing away.
3. **The process is serial-parallel.** Weighing and filling all vessels first, then
   sonicating in sequence, is a clean assembly-line flow. The hot route interleaves
   heating, blending, chilling, and transferring, each with its own wait state.

---

## 4. Revised system specification

| Component | Specification | Rationale |
|---|---|---|
| Powder + water | Pre-dosed into final storage vessels, cold water | Vessel is the reactor; no transfer step |
| Dispersion | Probe sonication, food-grade, ~45 s per vessel | Complete deagglomeration; +0.14 K thermal load |
| Between vessels | Probe rinse, ~12 s | Only shared food-contact surface; matcha + water only |
| Storage | Capped, labeled, refrigerated | Hold within a service day |
| Agitation | **Pulse ~5 s every 15 min** | 1.9 % dose error; 190× less shear than continuous |
| Line | Short, or recirculating/purge-first-draw | **Still the dominant variance source** |
| Dosing | Volumetric pump | Small but cheap to control |
| Milk / ice | Added after dosing | Probe never touches dairy |

Note that §1's improvement does **not** change the standing conclusion from the line
analysis: a 3 m × 6 mm line holds ~1.2 doses that stratify in ~20 min regardless of how
well the keg is stirred. **The line remains the top consistency problem in the system**,
and pulsed agitation slightly worsens it in one specific way — if a pulse fires while
product sits in the line, the keg is homogenized and the line is not, so the mismatch
between them is at its largest right after a pulse. Purging the first draw after an idle
gap handles this; it is the same fix as before, now with one more reason.

---

## 5. Revised priority tests

1. **Pulse-interval validation.** Hold a sonicated batch 8 h at 4 °C under 15-min pulsing.
   Measure D90 (or turbidity) at 0, 4, 8 h, and take a top-draw and bottom-draw TDS at each
   point. Confirms both the flocculation prediction (§1.1) and the stratification
   prediction (§1) in one experiment. **Highest value test in the program.**
2. **Line stagnation.** First-draw-after-idle TDS versus steady-state draw. Quantifies the
   remaining dominant term.
3. **Texture sensory panel.** Sonicated versus whisked concentrate, both pulsed, both
   pump-dosed. With dose consistency equalized by the keg, texture is the residual claim
   for sonication and should be tested as such.
4. **PSD by laser diffraction.** Cleanest confirmation of the dispersion mechanism.
5. **Probe erosion** over realistic duty cycles in an abrasive suspension. Still the main
   hardware unknown, and the in-vessel workflow raises the cycle count (one immersion per
   vessel rather than one per batch), so this matters more under this design than the
   earlier one.

---

## 6. Assumptions

- Settling velocity uses 7 µm at 4 °C; the D90 tail settles ~2× faster, so §1's dose errors
  are optimistic by roughly that factor for the coarse fraction. The 15-min interval retains
  margin even so.
- Mixing time (~5 s) is a correlation estimate for an unbaffled vessel; measure it by dye or
  by top/bottom TDS convergence.
- Collision efficiency α remains unmeasured; §1.1 brackets it at 0.01 and 0.001.
- Labor times are estimates for a trained operator and will shift with real build-out — the
  *ratio* between routes is more robust than the absolute minutes, since the structural
  difference (no transfer, no chill, one shared surface) does not depend on the estimates.
- The 40 % chilling-plus-washing share of the hot route follows from those same estimates;
  it is the figure most worth replacing with a stopwatch measurement.
