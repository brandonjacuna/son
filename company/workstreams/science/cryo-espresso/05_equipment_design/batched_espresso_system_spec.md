# Batched espresso: a buildable system for a 4–6 hour hold

Design answer to "capture and preserve fresh-espresso quality, batch once per shift (6 h) or at
3–4 h intervals". Derived from the feasibility study's finding that **oxygen exclusion, not chilling
rate, governs quality** — and from the operational fact that what destroys a batch is not the
chilling method but the minutes the coffee spends hot while the batch accumulates.

---

## 1. The design in one paragraph

Pull shots normally. Each shot lands in a **closed, gas-purged manifold** and is chilled **inline as
it is pulled** by a small counter-flow heat exchanger, arriving at 4 °C within about ten seconds.
It accumulates in a **pre-purged, counter-pressured keg** that is never opened to air. The keg holds
under a **nitrogen/CO₂ blend** at a pressure chosen to keep the coffee's own dissolved CO₂ in
solution. At service, coffee is **dispensed under gas pressure** — the keg is never opened, so the
last cup sees the same headspace as the first. Crema is regenerated at the cup.

No cryogen. No open surfaces. No freezing. The entire hazard profile of the LN2 concept disappears,
and the quality outcome is — by the model — indistinguishable or better.

---

## 2. Why this shape, specifically

**2.1 Chill inline, never accumulate hot.** This is the single largest quality lever in the
operating pattern, and it is easy to get wrong. Chilling each shot as it is pulled costs a
degradation dose of **786 equivalent-seconds at 4 °C**. Letting shots accumulate hot for a
20-minute batching run and then chilling the batch costs **166,700 equivalent-seconds — 212× more**,
which is roughly 7.7× the entire dose of the subsequent 6-hour cold hold. A thermos-then-chill
workflow is worse still (194,800).

Put plainly: **the batching run itself can do more damage than the whole storage period.** Any design
that collects shots warm and chills at the end has lost before storage begins — and this is exactly
what most café batching improvisations do.

**2.2 Exclude oxygen from the first second.** At the 6-hour target, an inert headspace retains
**84 %** of 2-furfurylthiol (the roasty top-note marker) versus **56 %** under air — a 28-point gap
that widens to 39 points by 12 h. Oxygen solubility also rises 3.8× on cooling, so a chilled coffee
exposed to air absorbs oxygen far more readily than a hot one. The chilling path must therefore be
**closed**, not an open cascade over a cold surface.

**2.3 Counter-pressure, not vacuum.** Espresso arrives with ~1.25 g/L of dissolved CO₂, which carries
perceived brightness and tactile prickle. Holding that at 4 °C requires a CO₂ partial pressure of
**0.45 bar absolute**. Using a blend gas:

| Blend gas | Keg pressure to hold as-brewed CO₂ |
|---|---|
| 75/25 N₂/CO₂ ("beer gas") | ~12 psig |
| 70/30 N₂/CO₂ | ~7 psig |
| 60/40 N₂/CO₂ | ~2 psig |

A 70/30 blend at 7 psig is the practical choice: low enough for any keg, high enough to hold
carbonation, and low enough in CO₂ that it will not acidify the coffee measurably over 6 h. **Vacuum
is the wrong answer** — it strips 89 % of the CO₂ and 10–18 % more volatiles, and underperforms an
inert flush on every marker.

**2.4 Dispense without opening.** A single lid opening admits roughly **41 mg of oxygen** into the
headspace — about **34× the entire 6-hour ingress budget** for a 2 L batch. A batch that is opened
for service is no longer an inert batch after the first pour. Pressure dispense is not a
convenience feature; it is what makes the inert flush mean anything past the first cup.

---

## 3. Bill of materials

| Item | Spec | Notes |
|---|---|---|
| Inline chiller | Counter-flow or brazed-plate, 316 stainless, ~400 W at ΔT 74 K | Sized for continuous pulling; a small glycol bath or a recirculating chiller drives it |
| Coolant | Food-grade propylene glycol, −2 to 0 °C | Never below −1 °C at any wetted wall (freezing point margin) |
| Receiving manifold | Closed, purged, minimal internal volume, 316 stainless or PTFE | The portafilter-to-keg path must never see room air |
| Keg | 5 L Cornelius (or 2 L growler for small batches), ball-lock, pressure-rated | Rigid, never glass |
| Blend gas | 70/30 N₂/CO₂, regulator to 7 psig | A beer-gas cylinder and a two-stage regulator |
| Purge | Displacement fill into a CO₂- or N₂-flooded keg | Purge to <1 % headspace O₂ before first shot |
| Refrigeration | Under-counter, 2–4 °C, with a logging thermometer | Setpoint control matters more than the chiller's speed |
| Inline filter | 30–50 µm, on the fill path | Removes fast-settling fines |
| Dispense | Pressure tap, short line, chilled | Never open the keg |
| Optional QC | Luminescent O₂ sensor spot bonded inside the keg | Reads through the wall; verifies the flush without opening |

Approximate cost: a used Cornelius keg, a beer-gas regulator and cylinder, a brazed-plate exchanger
and a small recirculating chiller. This is a low-thousands build, not a capital project, and every
component is standard beverage or lab hardware with established food-contact status.

---

## 4. Batch sizing for the two operating patterns

| Pattern | Hold | Shots | Batch volume | Brew run | Vessel |
|---|---|---|---|---|---|
| Once per shift, moderate bar (25/h) | 6 h | 150 | 6.0 L | ~75 min | 2 × 5 L keg |
| Every 3–4 h, moderate bar | 4 h | 100 | 4.0 L | ~50 min | 1 × 5 L keg |
| Once per shift, busy bar (45/h) | 6 h | 270 | 10.8 L | ~135 min | 3 × 5 L keg |
| Every 3–4 h, busy bar | 4 h | 180 | 7.2 L | ~90 min | 2 × 5 L keg |

Inline chiller duty is ~380 W at a continuous pull rate — a small recirculating chiller, not a
cryogenic system.

**Recommendation: the 3–4 h interval, not the once-per-shift 6 h batch.** The retention curve is
steep early: the marker holds 93 % at 2 h and 84 % at 6 h under inert. Splitting into two smaller
batches keeps the served product on the flat part of the curve, halves the exposure of any single
batch to a flush failure, and reduces the batch size to a single keg. **Smaller, more frequent
batches are strictly better on quality and on risk;** the only cost is a second setup per shift.

---

## 5. What this system does not fix

Two limits are inherent to batching and no equipment solves them:

- **Crema does not survive.** It is a CO₂ foam; chilling raises CO₂ solubility ~7× and dissolves the
  bubbles from the inside. Plan to regenerate at the cup — a fresh crema float, a short shake, or a
  nitro/blend-gas charge on dispense.
- **Beyond ~12 h you have a different product.** Retention falls to 71 % at 12 h even under inert.
  For 4–6 h, this system is genuinely good. For 24 h+, sell it as cold coffee, not as held espresso.

Both argue for using the batch in **milk and iced drinks**, where crema and CO₂ prickle matter least,
and keeping fresh shots for neat orders. That split is likely the correct commercial answer
regardless of hardware.

---

## 6. Food safety — read this before building

**Sealed, refrigerated, oxygen-excluded coffee is reduced-oxygen packaging of a TCS food.** Espresso
sits at pH ~5.15 and water activity ~0.99, above both barrier thresholds, and there is no lethality
step anywhere in the process. The target organism is non-proteolytic *Clostridium botulinum*, which
grows down to 3.0–3.3 °C — below normal café refrigeration — and reduced-oxygen packaging suppresses
the spoilage flora that would otherwise make a bad batch obvious.

A 4–6 hour hold is well inside the conventional 4-hour/short-duration safety envelope and is
far less exposed than the 24–72 h ambitions the original concept implied. But the requirements still
apply:

- Hold at **≤4 °C** with a logging thermometer and an alarm, not a dial setting.
- **Same-shift discard.** Date/time-mark every keg; never carry a batch overnight.
- Keep a written procedure covering purge verification, chill-exit temperature, and discard time.
- **Talk to your local health authority before serving from this system.** Requirements vary by
  jurisdiction, and a reduced-oxygen process in a retail food setting may require an accepted HACCP
  plan or a variance even at short hold times.

This is analytical and engineering guidance, not a food-safety certification. Have the process
reviewed by a qualified food-safety professional and your regulator before it serves a customer.

---

## 7. Validation — prove it before you commit

The trial design from the feasibility study reduces neatly here, because the hypothesis is now
narrow and cheap to test:

1. **Two arms:** inline-chilled + inert-flushed keg versus inline-chilled + air headspace, both at
   4 °C, tasted at 0, 4 and 6 h.
2. **Tetrad test, not triangle** — about a third the panel for the same information (~61–65
   assessments at d′ = 1.0; budget with the larger figure).
3. **60–80 espresso drinkers, 2 tetrads each**, as a central-location test. No trained panel needed.
4. **Serve blind in opaque cups**, temperature-matched, with crema skimmed from every arm including
   the fresh reference — otherwise the panel is judging appearance, not flavour.
5. **One instrumental check:** headspace O₂ at seal and at service, which verifies the flush actually
   worked and separates "the gas system failed" from "the coffee aged".

The model predicts a large, easily detected difference. If your panel cannot find it, the flush is
failing somewhere — and that measurement tells you where.
