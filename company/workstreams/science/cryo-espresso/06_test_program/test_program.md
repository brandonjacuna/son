# Validation programme for batched espresso: a staged test system

**Purpose.** Everything in this project so far is first-principles modelling. Not one number has
been measured. This document is the system that converts those models into evidence — or kills them
cheaply. It is organised as **gates**: each one asks a single question, has a pass criterion fixed
*before* it runs, and can stop the project.

**Design principle: the cheapest test of the most load-bearing claim goes first.** The ordering here
is deliberately not "build the thing then test it."

---

## 0. The audit that reshaped this programme

Before designing the tests I re-derived the prior work's load-bearing claims. Three results changed
what needs testing.

**0.1 The pivot away from cryogenics was justified — and now has a measured margin.** The claim that
oxygen exclusion matters far more than chilling speed holds until the activation energy of the
dominant degradation pathway reaches **119 kJ/mol**. The model assumed 60 ± 15, so the conclusion
survives to **four standard deviations**. For a thiol oxidation / Michael addition pathway, 119 is
implausibly high. The conclusion is robust, but it rests on a single parameter that has never been
measured in coffee — which is why G0 below measures the *consequence* of that parameter directly
rather than trusting it.

**0.2 "Chilling rate doesn't matter" is true only inside the range that was tested, and it is being
over-generalised.** The prior comparison was 1.5 s (cryo) against 10 s (plate heat exchanger), where
the gap is 0.28 pp — genuinely negligible. But extend the chill and the penalty grows fast:

| Time to complete the chill | Penalty vs. a 1.5 s chill |
|---|---|
| 10 s | 0.28 pp |
| 30 s | 0.92 pp |
| 1 min | 1.9 pp |
| 5 min | 9.0 pp |
| 20 min | 28.4 pp |

This converts a vague finding into **a hard design specification the earlier work never stated:
the chill must complete within 60 seconds. Below 60 s, additional speed is worth nothing; beyond a
few minutes it is worth a great deal.** That single line is the real engineering output of the
kinetics, and G1 is built to verify it.

**0.3 A failure mode nobody modelled: the coil runs two-phase.** Espresso leaves the group head
roughly **three times supersaturated** with CO₂ relative to its solubility at 78 °C. In the hot
first third of the coil that gas comes out of solution — up to **35 % gas by volume** — which is
slug flow in a 3 mm tube. It re-dissolves below about 30 °C, so it is not primarily a CO₂-loss
problem; it is a **flow-stability problem**. Two consequences:

- Residence time and heat transfer become erratic shot to shot.
- A CO₂ bubble rises at roughly 200–250 mm/s; the liquid moves at **207 mm/s**. The two are
  comparable, which means in a *downward*-flowing coil bubbles can stall indefinitely and gas-lock
  it. **This reverses the earlier "mount vertical, flow downward" recommendation. Flow must be
  upward**, with a drain valve at the low point for cleaning.

G2 exists specifically to look at this, through a transparent section, before anything is committed.

**0.4 One correction to my own work.** The earlier chiller document gave the glycol bath as "never
below −1 °C" in the bill of materials while the setpoint analysis put the freeze boundary at
−6.5 °C. The analysis is right and the BOM line was wrong; the usable window is **−6.5 to +5.2 °C**
with **+1 °C** nominal. I also found and fixed a units error in my own audit code (activation energy
in kJ/mol divided by a gas constant in J/mol·K) before producing the numbers above.

---

## 1. Design-state ladder

Where each piece of work sits, so "next state" means something specific:

| State | Meaning | Status |
|---|---|---|
| **D1 Concept** | Physics says it could work | Complete |
| **D2 Detailed design** | Dimensioned, real parts named, failure modes known | Complete — this round |
| **D3 Prototype** | Built once, bench-validated against spec | Gates G1–G3 |
| **D4 Pilot** | Makes real product, tested blind | Gates G4–G5 |
| **D5 Service-ready** | Survives a real bar; regulator satisfied | Gate G6 + R1 |

---

## 2. The gates

### G0 — Premise test, nothing built · 7 days · €0.8–2.8k

**The most important gate, and it requires no custom hardware at all.**

The entire system exists to exclude oxygen. If oxygen exclusion buys nothing measurable over 6 h,
no chiller and no keg design is worth building. That can be tested *now*, with homebrew equipment,
before a single part is fabricated.

- **Rig:** a commercial counter-flow wort chiller (or an ice-bath coil) to chill shots quickly, and
  two identical 5 L ball-lock kegs — one purged with blend gas to <1 % O₂, one deliberately left on
  air. Nothing custom.
- **Measure:** dissolved O₂ at seal and 6 h; 2-furfurylthiol and the thiol oxidation index at 0 and
  6 h only (12 GC-MS runs); a blind tetrad at 6 h with 20–30 staff and regulars.
- **Pass:** inert arm retains ≥20 pp more 2-furfurylthiol at 6 h **and** the tetrad is significant
  at p<0.05. One without the other is a weak pass.
- **Fail means:** stop. The project ends here for under €3k, with nothing built and nothing wasted.

### G1 — Dry thermal rig · 3 days · €0.9–2.6k

- **Question:** does the coil chill 1.48 g/s from 78 °C to 4 °C, and where is the real freeze boundary?
- **Rig:** glycol bath + coil + controlled hot-water feed. RTDs at inlet, outlet and bath; a balance
  logging mass against time. No coffee — water only, so it is cheap and repeatable.
- **Sweep:** flow 1.0–3.0 g/s; glycol setpoint +4 down to −8 °C.
- **Pass:** outlet ≤4.0 °C at 1.48 g/s with glycol at or above −2 °C; **chill complete inside 60 s**
  (the spec from §0.2); no ice at the design setpoint.
- **Fail means:** the Dean-flow heat-transfer estimate is wrong. Lengthen the coil — do **not** drop
  the glycol setpoint, which is the tempting and wrong fix.

### G2 — Wet rig with espresso · 4 days · €0.4–1.2k

- **Question:** does real espresso flow stably through the coil, and does the coil change the coffee?
- **Rig:** G1 rig plus a real group head, **a transparent inspection section at the coil inlet and
  mid-point**, phone video at high frame rate, and a dye-trace loop.
- **Measure:** slug/two-phase behaviour on video; outlet temperature stability over ≥30 consecutive
  shots; carryover by dye trace; TDS in versus out; mass balance per shot.
- **Pass:** no gas lock; outlet temperature SD ≤1.0 K over 30 shots; TDS shift <2 % relative;
  carryover <50 % of one shot.
- **Fail means:** the two-phase risk is real. Fixes in order of cost: reverse or re-orient the flow,
  add a back-pressure regulator (~1.5–2 bar), or enlarge the bore of the hot section only.

### G3 — Packaging integrity · 5 days · €0.7–2.2k

- **Question:** can the keg hold below 1 % oxygen for 6 h *through real dispensing*?
- **Rig:** purged keg with a **bonded optical oxygen sensor spot read through the wall** — the only
  way to measure this without destroying the sample you are measuring.
- **Measure:** dissolved and headspace O₂ at seal, 1, 2, 4, 6 h; the O₂ step per dispense event;
  pressure decay; dissolved CO₂ at seal and at 6 h.
- **Pass:** dissolved O₂ rise ≤0.6 mg/L over 6 h **including ≥20 dispense events**; pressure decay
  <1 psi/h; CO₂ within 20 % of as-brewed.
- **Fail means:** a plumbing problem, not a concept problem. Fix fittings and the purge sequence.

### G4 — Chemistry hold trial · 14 days · €3.5–11k

The confirmatory version of G0, on the real system, with enough replication to publish or to justify
capital.

- **Arms:** inline-chilled + inert flush vs inline-chilled + air headspace, both at 4 °C. Three batch
  replicates. Destructive sampling — one vessel per timepoint per arm per replicate.
- **Measure:** thiol oxidation index (paired TCEP-reduced and unreduced aliquots) as the primary
  endpoint; 2-furfurylthiol and methanethiol by HS-SPME-GC-MS **extracted at 30 °C, not 40–60 °C**,
  because a hot incubation manufactures the very compounds being measured; plus dissolved O₂, CO₂,
  TDS, pH, turbidity. Timepoints 0, 2, 4, 6 h.
- **Pass:** the arms separate at p<0.01, with the inert arm retaining ≥25 pp more 2-furfurylthiol at 6 h.
- **Note on power:** this design is powered for the oxygen effect and **not** for a chilling-rate
  effect. Do not add a chilling-rate arm here and then report a non-significant result as evidence
  of equivalence — it would be underpowered by construction.

### G5 — Sensory · 10 days · €2.5–9k

- **Design:** tetrad, not triangle — about a third of the panel for the same information
  (~61–65 assessments at d′ = 1.0 against ~202–215; budget with the larger figure).
- **Panel:** 60–80 espresso drinkers × 2 tetrads each, as a central-location test. No training needed.
- **Blinding:** batched product has no crema, which is an obvious visual cue. Serve every arm —
  including the fresh reference — in opaque lidded cups under low light, with crema skimmed from all
  arms. State the validity cost openly: this answers "do these liquids differ in flavour", not "do
  these drinks differ as products."
- **Temperature:** every arm to 65 ± 1.5 °C with the *same* dwell, including the fresh reference.
  Temperature is the easiest confound to introduce and the hardest to notice afterwards.
- **Matrices:** neat, a 6 oz milk drink, and iced. Matrix × treatment interaction is a primary
  endpoint, not a nuisance term — parity in milk with a difference neat is a commercially meaningful
  result, not a failure.

### G6 — Service pilot · 21 days · €1.2–4k

One bar, three weeks, staff trained but not supervised, batching twice per shift at the 3–4 h
interval. Log chill-exit temperature at 1 Hz, headspace O₂ at every seal, discard events, staff
minutes per batch, complaints, cleaning compliance.
**Pass:** zero food-safety deviations, ≥95 % of batches in spec, ≤35 staff-minutes per batch.

### R1 — Regulatory clearance · 30 days · €0.5–5k · **gates G6**

Sealed, refrigerated, oxygen-excluded coffee is **reduced-oxygen packaging of a time/temperature
control for safety food**. Espresso sits at pH ≈ 5.15 and water activity ≈ 0.99 — above both barrier
thresholds — with no lethality step anywhere in the process, and the target organism
(non-proteolytic *Clostridium botulinum*) grows down to 3.0–3.3 °C, below normal café refrigeration.

A 4–6 h same-shift hold is a far more comfortable position than the 24–72 h the original concept
implied, but the requirement does not disappear. Submit a written HACCP plan and process description
to your local authority; a variance may be required. **This must clear before G6 serves a paying
customer.** No laboratory result substitutes for it.

*Analytical and engineering guidance only — not legal, regulatory or food-safety advice. Have the
process reviewed by a qualified food-safety professional and your regulator.*

---

## 3. One rig serves G1–G3

Build this once; it covers three gates.

| Element | Specification | Why |
|---|---|---|
| Glycol bath | 4 L, insulated, with circulation pump | 0.77 K rise per shot — absorbs the 856 W two-group peak |
| Chiller | 300–400 W at 0 °C | Sized on the 192 W mean, not the 428 W per-shot transient |
| Test coil | 3.0 mm bore × 2.2 m, 9 turns on Ø80 mm, 316L | The design under test |
| **Transparent section** | 50 mm of clear PFA or glass at inlet and mid-coil | **The only way to see the two-phase behaviour from §0.3** |
| Temperature | 3 × class-A RTD (inlet, outlet, bath), 1 Hz logger | Outlet trace is the primary signal across all three gates |
| Mass | Bench balance, 0.1 g, logged | Gives flow rate without a flow meter |
| Oxygen | Optical sensor spot bonded inside the keg + reader | Non-invasive; a Clark electrode destroys the measurement |
| Back-pressure | Adjustable regulator, 0–3 bar, on the coil outlet | The first fix to try if G2 shows slug flow |

**Instrument the thing you are most likely to be wrong about.** Here that is the coil outlet
temperature trace and the transparent section — between them they answer G1 and G2.

---

## 4. Decision rules, fixed before any data exists

1. **G0 fails → stop the project.** Do not rationalise a null into "we should build it properly and
   retest." The premise was the thing being tested.
2. **G1 fails → lengthen the coil.** Do not chase the setpoint colder; that is how you freeze product.
3. **G2 shows slug flow → fix orientation first, back-pressure second, bore third.** Cheapest first.
4. **G3 fails → it is a fittings problem.** Do not conclude the inert concept is unworkable.
5. **G4 fails after G0 passed → suspect the method**, not the concept; check the SPME incubation
   temperature and the oxidation-index aliquot handling before touching the design.
6. **G5 null in milk but positive neat → the commercial answer narrows to neat service**, which is
   the opposite of the usual assumption and should change the business case rather than end it.
7. **R1 not cleared → G6 does not run.** Not negotiable.

---

## 5. What this programme costs

| Milestone | Cumulative | What you know at that point |
|---|---|---|
| G0 | €0.8–2.8k | Whether the premise is real — with nothing built |
| G0–G3 | €2.8–8.8k | The hardware works and holds oxygen |
| G0–G4 | €6.3–19.8k | The chemistry is confirmed on the real system |
| G0–G5 | €8.8–28.8k | People can taste it |
| Everything | €10.5–37.8k | It survives service and the regulator |

94 days if run strictly serially; roughly 60 with G5 recruitment overlapping G4, and R1 started
early — **R1 should be initiated during G4**, since 30 days of authority turnaround is the longest
pole and costs almost nothing to start.

Total coffee required: **38.5 kg roasted**.

---

## 6. What is still unmeasured after all of this

Worth stating plainly, because the programme deliberately does not chase everything:

- **The activation energy itself.** G0 and G4 measure its *consequence* over 6 h, which is what
  matters commercially, but neither pins Ea. If you ever want to extrapolate beyond 6 h, you need
  retention at two hold temperatures, which is a different and larger experiment.
- **Whether a plate heat exchanger would do just as well as the coil.** The audit says the two should
  be indistinguishable (0.28 pp). This programme does not test it, because confirming equivalence
  needs ~149 assessments and the answer would not change the build. If you want that answer, it is an
  equivalence test and must be designed as one.
- **Shelf life beyond 6 h.** Deliberately out of scope: the regulatory position makes a longer hold a
  different project.
