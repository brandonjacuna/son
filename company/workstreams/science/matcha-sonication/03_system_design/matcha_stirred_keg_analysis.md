# Continuously agitated keg + dosing unit: analysis

**Verdict: this is the right architecture, and it resolves the largest problem in the
system.** Continuous agitation eliminates hold drift, which contributed ~24× more
drink-to-drink variance than the entire whisk-to-sonication dispersion difference. It also
changes what sonication is *for* — see §4, which is the part worth reading if you already
expected §1 to work.

All results below are first-principles models with stated assumptions, not measurements.

---

## 1. Does gentle stirring actually keep matcha suspended?

Yes, with enormous margin. A 7 µm matcha particle settles at **5.1 µm/s**. A 50 mm impeller
in a ~4 L keg at the Zwietering just-suspended speed (~210 rpm) produces a bulk circulation
velocity of roughly **55 mm/s** — about **10,800× the settling velocity**.

The margin is so large that the requirement is qualitative rather than quantitative: *any*
continuous gentle circulation defeats settling for this particle size. Even the 45 µm
agglomerates that whisking leaves behind are held up with ~260× margin.

**Consequences:**

- Impeller speed is not a critical parameter. Run it slow.
- Stirrer heating is negligible: **+0.023 K over 8 hours** for the modeled duty. The keg
  stays at fridge temperature.
- A magnetic stir plate under a keg is mechanically simpler than an in-tank impeller and
  avoids a shaft seal. It is adequate at this scale.

---

## 2. The risk this introduces: shear-induced flocculation

Continuous stirring is not free of consequences. It moves particle collisions from
diffusion-driven (perikinetic) to shear-driven (orthokinetic), and orthokinetic dominates
above a velocity gradient of only ~0.014 s⁻¹. The modeled stirrer produces **G ≈ 46 s⁻¹**,
far above that.

At the modeled particle number density, collisions are frequent. Whether they *stick*
depends on the collision efficiency α, which is set by surface chemistry, not by the
stirrer:

| Collision efficiency α | Half-time to aggregate |
|---|---|
| 1.0 (no stabilization) | seconds |
| 0.01 | ~1.3 min |
| 0.001 (well-stabilized) | ~13 min |

**This is the key uncertainty in the whole design and it cannot be resolved analytically.**
Matcha in water carries some electrostatic and steric stabilization from its own proteins
and polysaccharides, so α is likely small — but "likely small" is not a number you can
build on.

Why it matters: flocs are fractal and loose (Dᶠ ≈ 2.1), so they settle far faster than
their mass suggests — a 50 µm floc settles ~8.7× faster than a primary particle. If
re-flocculation occurs, stirring will still hold the flocs up (§1's margin covers it), but
the product's *texture* changes and any draw taken from a poorly mixed zone drifts.

**How to test it cheaply:** hold two sonicated samples at 4 °C for 8 h — one stirred, one
still-then-gently-inverted before sampling. Measure turbidity or D90 on both at t = 0 and
t = 8 h. If the stirred sample's D90 has grown, α is not small and you need either lower
shear, intermittent rather than continuous stirring, or a re-dispersion step before service.

---

## 3. The new dominant variance source: the dosing line

Solving hold drift promotes the next problem, and it is one the keg architecture creates
rather than inherits.

**Product standing in the line between draws is not being agitated.** A typical 3 m × 6 mm
keg run holds **~85 mL — about 1.2 drink doses** — and that volume stratifies across the
tube's 6 mm diameter in roughly **20 minutes**.

Modeled effect, assuming 18 % of draws follow an idle gap long enough to matter:

| Configuration | Drink CV | Within ±10 % of target |
|---|---|---|
| Unagitated keg, long line | 0.402 | 15 % |
| **Stirred keg, long line** | **0.128** | **87 %** |
| **Stirred keg, short purged line** | **0.045** | **99 %** |

Revised variance budget for the stirred system:

| Source | Contribution |
|---|---|
| **Line stagnation (first draw after idle)** | **0.0165** |
| Dilution / ice | 0.0009 |
| Dose (pump) | 0.0004 |
| Hold drift | ≈0 — solved by stirring |

**The line is now the whole problem**, and it is worth roughly 40× the pump's contribution.
Design responses, in order of effectiveness:

1. **Minimize line volume.** A 0.5 m × 4 mm line holds 6.3 mL — under 10 % of a dose — and
   the stagnation term nearly vanishes. Mount the dosing head on the keg if possible.
2. **Purge the first draw after an idle gap**, or plumb a recirculating loop that returns
   line contents to the keg between draws. This is standard practice in beverage
   dispensing and is the robust fix.
3. **Orient the line vertically** where possible; a horizontal run stratifies across its
   full diameter and delivers a clean-then-concentrated slug.

---

## 4. What this does to the case for sonication

Uncomfortable but important: **the stirred keg reduces sonication's consistency
advantage to near zero.** Stirring holds up whisked agglomerates and sonicated particles
alike (§1), so the dispersion-state variance term that sonication used to eliminate is now
being handled mechanically by the stirrer, for any preparation method.

What remains, and it is a real thing, is **texture**:

| Preparation | Mass above the ~30 µm oral grit threshold |
|---|---|
| Chasen whisk | 4.8 % |
| Immersion blender | 3.9 % |
| Sonication | ~0 % |

Under continuous agitation, those agglomerates no longer settle out of a whisked
concentrate — they stay suspended and get **delivered into the cup**. So the stirred keg
paradoxically makes dispersion quality *more* perceptible, not less: settling used to
remove the clumps from the draw zone, and now nothing does.

**The reframed case for sonication in this architecture is mouthfeel and smoothness, not
dose consistency.** That is a defensible claim — it is exactly the attribute a high-end
café would care about — but it is a different claim from the one this project started with,
and it should be tested by a texture-focused sensory panel rather than by refractometry or
dose-variance measurement.

---

## 5. Revised system recommendation

| Component | Choice | Why |
|---|---|---|
| Dispersion | Sonication (cold, ~60 s/batch) | Complete deagglomeration → smoothest texture; no thermal load |
| Vessel | 4 L keg, refrigerated | Matches batch size to service day |
| Agitation | Magnetic stir plate, low speed, continuous | Eliminates hold drift with ~10,000× margin; negligible heating |
| **Line** | **As short as possible; recirculating loop or purge-first-draw** | **Now the dominant variance source** |
| Dosing | Volumetric pump | Small contributor, but cheap to get right |
| Milk/ice | Added after dosing, never sonicated | Avoids dairy off-flavor mechanism entirely |

Expected performance: **CV ≈ 0.045, ~99 % of drinks within ±10 % of target**, versus ~48 %
for made-to-order whisking under service pressure.

---

## 6. Priority test list, revised

1. **Flocculation check** (§2) — stirred vs. unstirred D90 or turbidity at 0 and 8 h. This
   is now the top open risk, and it is the one that could force a design change.
2. **Line stagnation measurement** — draw after a deliberate 30-minute idle, measure TDS or
   turbidity of the first 70 mL versus a steady-state draw. Directly quantifies §3.
3. **Texture sensory panel** (§4) — sonicated vs. whisked concentrate, both stirred, both
   dosed identically. This is now the primary efficacy question for sonication.
4. **PSD by laser diffraction** — still the cleanest confirmation of the mechanism.
5. Probe erosion over realistic duty cycles — unchanged, still the main hardware risk.

## 7. Assumptions to check

- Zwietering correlation is derived for stirred tanks with standard baffling; an unbaffled
  keg on a stir plate will circulate less efficiently. The margin is so large this is
  unlikely to matter, but the 55 mm/s figure is optimistic.
- Collision efficiency α is unmeasured and drives §2 entirely.
- The 18 % idle-draw fraction in §3 is assumed; substitute your own service pattern.
- The 30 µm grit threshold is a commonly cited approximate figure for oral detection of
  particulates and varies with matrix — in a viscous, sweetened, milk-based drink the
  effective threshold is likely higher, which would narrow sonication's texture advantage.
- Fractal dimension Dᶠ = 2.1 for flocs is a literature-typical value, not measured for
  matcha.
