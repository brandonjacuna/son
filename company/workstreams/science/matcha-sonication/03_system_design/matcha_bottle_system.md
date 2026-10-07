# Bottled concentrate in a bartender's well: system analysis

**This is better than the keg, and the reason is structural rather than incremental.** The
dosing line was the dominant variance source in the keg architecture — ~1.2 doses of
product sitting unagitated between draws, stratifying in ~20 minutes. **Bottles have no
line.** That term goes to zero by construction, not by engineering.

The keg's stir plate was solving a problem that bottles solve more simply: a bottle is
shaken by the person picking it up, so agitation is coupled to use rather than scheduled
against it.

All numbers are first-principles or task models with stated assumptions.

---

## 1. Head-to-head

| System | Composite CV | Drinks within ±10 % |
|---|---|---|
| Keg + pump + line | 0.130 | **56 %** |
| Bottle + free pour | 0.084 | 77 % |
| **Bottle + measured pour spout** | **0.040** | **99 %** |

The bottle system beats the keg even with sloppy free pouring, and beats it decisively with
a measured spout. The keg's precision pump was dosing accurately *from a line that had
already stratified* — precision applied downstream of the error.

---

## 2. The controlling variable is the pour, not the shake

This is the actionable finding, and it inverts the intuition that shaking discipline is the
thing to train.

| Pour method | Shake every pour | Shake most pours | Shake occasionally |
|---|---|---|---|
| Jigger / portioned spout | 99.9 % | 97.8 % | 92.9 % |
| Measured pour spout | 99.4 % | 97.1 % | 91.9 % |
| Free pour, trained | 77.5 % | 75.8 % | 72.3 % |
| Free pour, rushed | 51.6 % | 51.4 % | 50.2 % |

**Moving from free pour to a measured spout gains ~22 points. Perfecting shake compliance
gains ~7.** And critically: a free-pour system cannot be rescued by shaking discipline —
the rushed free-pour row sits at ~51 % regardless.

The reason shake compliance matters so little is geometry. In a 750 mL bottle (170 mm
liquid column), 30 minutes unshaken produces only a **5.7 % dose error**, because the
clarified layer is small relative to a tall column. At the realistic pour cadence of a
service well, stratification simply does not have time to develop.

**Specify a portioned pour spout or jigger. That single decision is worth more than every
agitation refinement discussed so far.**

---

## 3. Bottle size: taller is more forgiving

Same diameter, more height means a longer column and proportionally less stratification
error for the same idle time.

| Size | Doses | Column | Error if unshaken 30 min | Bottles/day at 144 drinks |
|---|---|---|---|---|
| 250 mL | 3.6 | 57 mm | **19.4 %** | 41 |
| 375 mL | 5.4 | 85 mm | 12.1 % | 27 |
| **750 mL** | **10.7** | **170 mm** | **5.7 %** | **14** |
| 1000 mL | 14.3 | 226 mm | 4.2 % | 11 |

**750 mL is the sweet spot** — inside spec even with a missed shake, a familiar form factor
for a bar well, dishwasher-compatible, and 14 bottles covers a 144-drink day. Below 375 mL
the short column makes stratification a real error source; above 1 L the bottle becomes
awkward to shake one-handed, which attacks the compliance the design depends on.

---

## 4. What bottles fix that the keg did not

- **No line, no dead legs, no biofilm risk.** Keg lines need a caustic/acid cleaning cycle;
  bottles go in the dishwasher. Estimated daily cleaning: ~6 min for bottles versus ~18 min
  for a keg plus line.
- **Agitation is coupled to use.** No timer, no stir plate, no duty cycle to tune. Picking
  the bottle up *is* the mixing step, and the Reynolds number during a single inversion is
  ~24,000 — fully turbulent, complete re-homogenization in one or two inversions.
- **Batch isolation.** One bad batch contaminates one bottle, not the whole keg. This also
  makes FIFO rotation and per-batch labeling trivial.
- **Failure is visible.** A stratified bottle can be seen through the glass. A stratified
  line cannot.
- **The vessel is still the reactor.** Sonicate directly in the bottle, cap, label, chill —
  the in-vessel workflow carries over intact and now has no transfer step at all.

---

## 5. New considerations bottles introduce

### 5.1 Light exposure — use amber glass

A bar well is illuminated, and matcha's green color comes from chlorophylls that
photodegrade, with catechins also light-sensitive. Modeling an 8 h exposure at typical bar
illuminance, **amber glass reduces the 400–500 nm dose by ~89 %** relative to clear.

Clear glass is the aesthetic default and the wrong choice here. If the visual of green
bottles matters for the bar's presentation, keep clear bottles for display and amber for
the working stock, or store clear bottles in a covered well.

### 5.2 Thermal — the well is not a refrigerator

A 750 mL bottle out of chill has a warming time constant of **~2.5 h**:

| Time out of chill | Bottle temperature |
|---|---|
| 15 min | 5.5 °C |
| 30 min | 6.9 °C |
| 1 h | 9.3 °C |
| 2 h | 12.9 °C |

Comfortable for a service well *if the bottle returns to chilled storage*, which is the
normal bar-well pattern. But a bottle left out through a slow afternoon crosses into
temperatures where quality and food-safety hold assumptions weaken. **Set a rule: bottle
out of the well for more than an hour goes back to chill or gets discarded.** This is the
one operational discipline the bottle system genuinely requires.

### 5.3 Headspace oxidation

A bottle averages ~50 % headspace over its service life, and that air is refreshed at every
pour. Catechins oxidize at the air interface. Over a service day this is likely minor, but
it is a real difference from a sealed keg under gas pressure. Mitigations if it proves to
matter: smaller bottles decanted more often (trading against §3), or filling to minimize
initial headspace and using the bottle within a defined window.

---

## 6. Revised system specification

| Component | Specification |
|---|---|
| Dispersion | Probe sonication, food-grade, cold water, in-bottle |
| Vessel | **750 mL amber glass**, swing-top or screw cap |
| Batch flow | Pre-dose powder + cold water → sonicate in bottle → cap → label → chill |
| Storage | Chilled well; return to cold storage if out > 1 h |
| Agitation | **Shake before pour** (2 inversions); no mechanical system required |
| **Dosing** | **Portioned pour spout or jigger — the highest-leverage choice in the system** |
| Milk / ice | Added after pour; probe never touches dairy |

Expected: **CV ≈ 0.040, ~99 % of drinks within ±10 %**, against ~48 % for made-to-order
whisking under service pressure.

This is simpler than the keg system, cheaper, easier to clean, easier to train, and more
accurate. It also removes the last piece of equipment that needed tuning.

---

## 7. Revised priority tests

1. **Portioned spout versus free pour, measured.** Pour 30 doses each way, weigh every one,
   compute CV. Costs an afternoon and a scale, and validates the highest-leverage claim in
   this document.
2. **Stratification in the real bottle.** Fill, chill, leave unshaken 30 and 60 min, then
   draw top and bottom samples for TDS. Confirms §2's geometry argument in the actual vessel.
3. **Amber versus clear over a service day.** Two bottles, same batch, one in the lit well
   and one covered; compare color (L\*a\*b\*) and taste at 8 h.
4. **Texture sensory panel** — sonicated versus whisked, both bottled and identically
   poured. With dosing equalized, texture is sonication's remaining claim.
5. **Probe erosion** over realistic cycles — unchanged, and the in-bottle workflow raises
   immersion count, so it matters more here than in a single-batch design.

---

## 8. Assumptions

- Pour CVs (free pour 0.08 trained / 0.14 rushed; measured spout 0.03; jigger 0.02) are
  typical bar-service figures, not measured for your staff — test 1 replaces them.
- Bottle diameter fixed at 75 mm for the size comparison; a narrower bottle at the same
  volume is taller and more forgiving still.
- Settling uses 7 µm at 4 °C; the coarse tail settles faster, so §3's errors are somewhat
  optimistic.
- Light-dose modeling uses representative transmittances for clear and amber glass and a
  typical back-bar illuminance; it ranks the two, and does not predict a degradation rate.
- Warming model assumes still air at 20 °C and no radiant load; a bottle in direct light or
  near equipment warms faster.
