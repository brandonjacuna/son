# Final system specification: cold-sonicated matcha concentrate, bottled, counter-chilled

A built-in chilled section closes the last open operational risk and removes a variance
term that had not been modeled before. The system is now **balanced** — no single dominant
error source remains — which is the point at which further engineering stops paying.

---

## 1. What the built-in chill fixes

### 1.1 It removes the discard rule

The previous design required an operational rule: *bottle out of the well more than an
hour goes back to chill or gets discarded*, because a 750 mL bottle warms with a ~2.5 h time
constant and reaches 9.3 °C in an hour, 12.9 °C in two.

A counter-integrated chilled section holds the bottle at temperature between pours. The
rule disappears — not because the risk is accepted, but because the mechanism that created
it is gone. **Removing a rule that depends on staff vigilance is worth more than any
refinement that depends on staff vigilance.**

Microbial hold margin follows the same logic. Using a standard psychrotroph growth model,
generation time at 4 °C is ~15 h versus ~2.3 h at 13 °C — roughly a **6× difference in
growth rate** across the range an unchilled bottle would drift through in an afternoon.
Constant chill keeps the whole service day in the slow regime.

### 1.2 It removes a pour-drift term I had not modeled

This is the finding worth flagging, because it works in a direction that is easy to miss.

Water viscosity falls sharply with temperature — 1.55 mPa·s at 4 °C, 1.20 at 13 °C, 1.00 at
20 °C. A pour spout is a viscosity-sensitive flow restriction, so **warm concentrate pours
faster and a timed or free pour delivers more of it**:

| Bottle temperature | Pour volume vs. a 4 °C calibration |
|---|---|
| 4 °C | — |
| 8 °C | +4.2 % |
| 13 °C | **+9.4 %** |
| 20 °C | **+16.4 %** |

A bottle drifting between 4 °C and 13 °C over a shift contributes a pour CV of ~0.026 all by
itself, and it is **systematic, not random** — every drink poured late in a warm stretch is
over-poured together. That is exactly the failure mode a consistency program is trying to
prevent, and it is invisible without a thermometer.

Constant-temperature storage eliminates it. It also means **any pour calibration you
establish stays valid**, which is what makes a measured spout trustworthy over a shift.

### 1.3 It lets you use clear glass

Amber glass was recommended to cut light exposure. A counter-recessed chilled section is
substantially darker than an open back-bar shelf, and a closed under-counter unit is darker
still. Relative 400–500 nm dose over 8 h:

| Location | Clear glass | Amber glass |
|---|---|---|
| Open back-bar shelf | 2,160 | 240 |
| Counter-recessed well | 288 | 32 |
| Closed under-counter | 36 | 4 |

**Clear glass in a recessed chilled well receives less light than amber glass on an open
shelf.** If the visual of green bottles matters to the bar's presentation, the built-in
chill buys that back. Amber remains the safer choice if the section is lit or glass-fronted.

---

## 2. Final variance budget

With the built-in chill and a measured pour spout:

| Source | Contribution | Share |
|---|---|---|
| Pour (measured spout) | 0.00090 | 50 % |
| Missed shake (10 % of pours) | 0.00045 | 25 % |
| Dilution / ice in the build | 0.00041 | 23 % |
| Bottle temperature drift | 0.00006 | 3 % |

**No term dominates.** Compare this to earlier iterations where line stagnation or hold
drift was 20–40× everything else. A balanced budget means the system is finished as a
design problem: further gains require attacking three roughly equal terms simultaneously,
which is rarely worth it.

Expected performance:

| Configuration | CV | Within ±10 % |
|---|---|---|
| Ambient shelf, free pour | 0.090 | 75 % |
| Ice-bath tub, free pour | 0.090 | 74 % |
| Built-in chill, free pour | 0.085 | 77 % |
| **Built-in chill, measured spout** | **0.041** | **98 %** |
| Built-in chill, jigger | 0.035 | 99 % |

**The pour spout remains the single highest-leverage decision** — it gains ~22 points where
the chill gains ~2. The chill's value is not in the average; it is in removing a systematic
drift and an operational rule. Both matter more than the on-spec percentage suggests.

---

## 3. Final specification

| Component | Specification | Why |
|---|---|---|
| Dispersion | Probe sonication, food-grade, cold water, **in-bottle** | Complete deagglomeration; +0.14 K thermal load; vessel is the reactor |
| Bottle | 750 mL glass; clear acceptable in a recessed well, amber if lit | 170 mm column tolerates a missed shake (5.7 % error at 30 min) |
| Batch flow | Pre-dose powder + cold water → sonicate → cap → label → chill | No transfer step; one shared surface (the probe) |
| Storage | **Counter-integrated chilled section, 3–5 °C** | Constant temperature; no discard rule; slow microbial regime |
| Agitation | Two inversions before pour | Re ≈ 24,000 per inversion; fully re-homogenizes |
| **Dosing** | **Portioned pour spout or jigger** | **Highest-leverage decision in the system** |
| Milk / ice | Added after pour | Probe never contacts dairy |

Expected: **CV ≈ 0.041, ~98 % of drinks within ±10 % of target**, versus ~48 % for
made-to-order whisking under service pressure. Prep labor ~28 min per 144 drinks against
~80 min for a hot/blender route.

---

## 4. What remains genuinely unresolved

Three items, none of which the equipment can settle:

1. **Does sonication produce a perceptibly smoother drink than whisking?** With dose
   consistency now handled by bottling and portioned pouring, texture is sonication's
   remaining claim. Modeled mass above the ~30 µm grit threshold: whisked 4.8 %, blended
   3.9 %, sonicated ~0 %. **This needs a blind texture panel and it is the primary open
   efficacy question.**
2. **Probe erosion in an abrasive suspension.** Unmodeled throughout. The in-bottle workflow
   raises immersion count (one per bottle, not one per batch), so it matters more here than
   in any earlier design. Measure tip mass loss over a few hundred cycles.
3. **Hold-window validation.** How long a bottle actually holds at 3–5 °C before texture,
   color, or flavor shifts. Constant chill makes a longer window plausible but does not
   demonstrate one.

---

## 5. Test order, final

1. **Portioned spout vs. free pour** — 30 pours each, weigh every one, compute CV. An
   afternoon and a scale; validates the highest-leverage claim in the system.
2. **Blind texture panel** — sonicated vs. whisked, both bottled, both pump-poured, n = 30
   triangle test. The primary remaining efficacy question.
3. **Hold study** — one bottle sampled at 0, 4, 8, 24 h in the actual chilled section:
   color (L\*a\*b\*), TDS, and taste. Defines the usable window.
4. **PSD by laser diffraction** — cleanest mechanistic confirmation, if a lab is reachable.
5. **Probe erosion** over realistic duty cycles.

---

## 6. Assumptions

- Pour-flow viscosity exponent (n ≈ 0.35) is a transitional-regime estimate; the *direction*
  and rough magnitude are robust, the exact percentages are not. Test 1 measures the real
  value.
- Pour CVs are typical bar-service figures, not measured for your staff.
- Growth-model generation times are for a reference psychrotroph in a permissive medium and
  are a **relative** illustration of why constant chill matters, not a shelf-life prediction
  for this product. A validated hold time requires actual microbial testing — this is a food
  safety determination for a qualified process authority or your health department, not
  something to infer from a model.
- Light-dose figures use representative illuminances and glass transmittances; they rank
  locations, they do not predict a degradation rate.
- Settling and stratification use 7 µm at the stated temperature; the coarse tail settles
  faster, so stratification errors are modestly optimistic.
