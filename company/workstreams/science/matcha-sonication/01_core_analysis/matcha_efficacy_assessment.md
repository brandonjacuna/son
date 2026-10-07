# Ultrasonic dispersion of matcha concentrate: efficacy assessment

**Question.** Does probe sonication of a cold matcha–water concentrate produce a
technically superior product to hot-water preparation (chasen or blender), independent of
commercial or customer-perception considerations?

**Verdict.** Yes on mechanism, with one large caveat that reframes the whole workflow.
Sonication is the only method examined that reliably exceeds the cohesive strength holding
matcha agglomerates together, and cold operation is a genuine and previously unaccounted
advantage — not a tolerance but a *preference* of the physics. The caveat is that no
dispersion method defeats gravity over a service day (§4), so the concentrate needs
agitation before draw regardless of how it was made.

All figures are first-principles models with stated assumptions, not measurements. Their
role is to rank mechanisms and size effects before you spend bench time. Section 6 lists
what must be measured to confirm each.

---

## 1. Mechanistic efficacy: does the method break clumps at all?

The question is whether applied stress exceeds the tensile strength of an agglomerate.
Modeling agglomerate strength with the Rumpf expression for van-der-Waals-bound clusters
(Hamaker constant 5×10⁻²¹–2×10⁻²⁰ J for organics in water, contact separation 0.3–0.5 nm,
porosity 0.40–0.65, primary particle 5–10 µm) gives a required stress of:

| Percentile | Cohesive strength |
|---|---|
| 5th | 23 Pa |
| 50th | 64 Pa |
| 95th | 174 Pa |

Applied stress from each method, evaluated on a 45 µm agglomerate:

| Method | Applied stress | Fraction of agglomerates surviving |
|---|---|---|
| Chasen whisk (5 W into 70 mL) | 22 Pa | **96 %** |
| Immersion blender (150 W into 1 L) | 36 Pa | **83 %** |
| Probe sonication, far-field estimate | 2.9×10⁴ Pa | **~0 %** |

Turbulent stress was computed from the energy dissipation rate, choosing the viscous or
inertial subrange expression according to whether the agglomerate is below or above the
Kolmogorov length (~5 µm for the whisk case at 80 °C). The 45 µm agglomerates of interest sit
well above that boundary for every method, so all arms are evaluated in the inertial subrange;
whisking is marginal because its applied stress (22 Pa) falls inside the cohesive-strength
distribution, not because of where it sits relative to the Kolmogorov scale.

**This is the central result.** Whisking and blending operate at stresses of the same order
as agglomerate strength, so they break the weakest clusters and leave the rest. Sonication
operates roughly **450× above the median cohesive strength**, which is a categorical
difference, not an incremental one. The prediction is not "sonication disperses somewhat
better" but "sonication disperses essentially completely while mechanical methods leave a
distribution of survivors."

The far-field figure is deliberately conservative — 1 % of the calculated near-tip acoustic
pressure amplitude, to account for attenuation across a 1 L vessel. Even at that discount
the margin is three orders of magnitude.

---

## 2. Cold operation: the variable that changes the comparison

This is the strongest point in favor of the method and it works through three independent
mechanisms.

### 2.1 Cavitation gets stronger as water gets colder

Cavitation intensity depends on the difference between ambient pressure and vapor pressure
— the pressure driving bubble collapse. Vapor pressure rises steeply with temperature, so
hot water produces vapor-cushioned bubbles that collapse weakly.

| Water temperature | Driving pressure (relative to 20 °C) |
|---|---|
| 4 °C | 1.01 |
| 80 °C | 0.54 |

**Collapse is ~1.9× more energetic in a 4 °C batch than an 80 °C one.** Sonication is
therefore *most* effective in exactly the condition where whisking is *least* effective —
cold water, where there is no thermal assist to particle wetting and dispersion. Every
mechanical method has the opposite temperature dependence.

### 2.2 The hot route has a self-heating problem the cold route does not

Measured as adiabatic temperature rise for a 1 L batch:

| Method | Temperature rise |
|---|---|
| Countertop blender, 60 s | **+17 K** |
| Immersion blender, 60 s | +2.2 K |
| Probe sonication, 30 s at 20 W | **+0.14 K** |

A countertop blender is a 1 kW device dumping nearly all of it into the liquid as heat.
This is your point, quantified: the blender route does not merely start hot, it actively
heats, and the sonication route is thermally almost inert.

### 2.3 Thermal exposure and aroma retention

Matcha's aroma is carried by volatiles whose Henry's-law constants rise steeply with
temperature — they partition out of solution and are lost to headspace. Integrating a
van't Hoff volatility index (ΔH_sol ≈ 50 kJ/mol) over each preparation trajectory:

| Route | Time to reach 6 °C | Thermal load (equiv. min at 100 °C) | Relative volatile loss |
|---|---|---|---|
| Hot + blender, refrigerator chill | 8.4 h | 9.9 | **9.4×** |
| Hot + blender, ice bath | 0.74 h | 1.5 | 1.7× |
| Cold + sonication | 0.44 h | 0.8 | 1.0× (reference) |

The refrigerator-chill route is the one most likely to be used in practice and the worst
performer by a wide margin — a 1 L batch cooling passively spends hours in the range where
volatiles strip. **An ice bath recovers most of the gap**, which is important: it means the
aroma advantage is largely an argument for *rapid chilling*, and only partly an argument
for sonication specifically. Do not overclaim this one.

A separate consequence: the hot route must pass through the 60→21 °C range where food-safety
cooling limits apply (~2.7 h by refrigerator in this model, ~0.24 h in an ice bath). The
cold route never enters that range at all, which removes a control point rather than
managing it.

---

## 3. What sonication does *not* do

Restating from the prior analysis, because it bounds the claim:

- **No meaningful extraction increase.** Matcha is milled to 5–10 µm; intraparticle
  equilibration takes ~0.07 s. There is no unextracted interior for cavitation to reach.
  Expect low single-digit uplift, below the ~15–25 % perceptual threshold for concentration
  differences. **No dose reduction is available.**
- **No foam.** Irrelevant here by design — it collapses on mixing.
- **No thermal degradation risk in either direction.** A burst delivers ~1–9 J/mL against
  720–2,880 J/mL in the catechin-degradation literature.

---

## 4. The limit that applies to every method: gravity

Modeling a bimodal particle population (primary particles plus surviving agglomerates,
6 % of mass agglomerated before treatment) and settling it by Stokes' law in a 200 mm
column at 4 °C:

| Treatment | Mass above 25 µm after treatment | Suspended fraction at mid-height, 8 h |
|---|---|---|
| Chasen whisk | 2.7 % | 10 % |
| Immersion blender | 1.0 % | 10 % |
| Sonication | ~0 % | 11 % |

**Sonication wins decisively on agglomerate removal and barely at all on hold stability.**
The reason is that a well-dispersed 7 µm particle still settles a 200 mm column in ~11 h,
so by 8 h *every* preparation has lost most of its suspended mass from the draw zone. The
earlier framing — that dispersion quality buys a stable hold — was too optimistic. It buys
freedom from *visible clumps and rapid stratification*, not freedom from settling.

**Practical consequences:**

1. **The concentrate must be agitated before each draw, or stored in a form that keeps it
   moving** (stir plate, recirculating dispenser, or simply a shake). This is not a defect
   of sonication; it is a property of a 7 µm suspension in water.
2. **Vessel geometry is a design variable.** Settling time scales with column height, so a
   tall narrow vessel holds far better than a wide shallow one. This is a free improvement.
3. **Shorter hold windows are better.** Consider batching twice a day rather than once.
4. Adding a hydrocolloid would stabilize the suspension but changes the product; out of
   scope here, worth knowing it exists.

---

## 5. Overall efficacy verdict

| Dimension | Sonication vs. hot-water mechanical prep |
|---|---|
| Agglomerate breakup | **Strongly superior** — categorical, ~450× stress margin |
| Cold-water capability | **Strongly superior** — 1.9× better cavitation cold; blender heats +17 K |
| Aroma/volatile retention | **Superior**, but an ice bath closes most of the gap |
| Thermal load on the product | **Superior** — near-zero self-heating, no 60→21 °C transit |
| Extraction yield / dose reduction | **No advantage** |
| Hold stability over 8 h | **Marginal advantage only** — gravity dominates |
| Consistency of a batch | Superior by construction (one batch, one dispersion state) |

The efficacy case is real and rests on two legs: **complete deagglomeration** and **cold
processing**. The second is what your last message added, and it is stronger than expected
— cold is not a compromise the method tolerates, it is the regime where cavitation performs
best and where every competing method performs worst.

---

## 6. What must be measured to confirm this

Ranked by how much they could change the verdict.

1. **Particle size distribution by laser diffraction**, all treatments, same powder. The
   direct test of §1. Report D50 and D90; the D90 is where the difference should appear.
   *This is the single measurement that confirms or kills the mechanism claim.* If a
   university or contract lab is reachable, do this first.
2. **Turbidity or transmittance decay over 8 h**, tall vessel, 4 °C, all treatments —
   tests §4 and tells you the real agitation interval.
3. **Aroma retention by headspace GC-MS or a trained panel**, cold-sonicated vs.
   hot-blended vs. hot-blended-then-ice-bathed. The three-way comparison is essential;
   omitting the ice-bath arm will overstate sonication's advantage.
4. **Refractometer TDS at equal powder**, to confirm §3's prediction of no extraction gain.
   Cheap; do it alongside everything else.
5. **Sonication dose-response** — 5, 10, 20, 40 s at fixed power, measuring D90. Find the
   plateau; running past it wastes energy and probe life for nothing.
6. **Probe wear**, given a solids suspension: mass loss and tip inspection over a
   realistic number of cycles.

## 7. Assumptions worth checking before trusting the numbers

- Rumpf strength assumes van der Waals bonding only. Matcha contains lipids and proteins
  that may form stronger bridges, which would raise required stress — this would *widen*
  sonication's advantage, not narrow it.
- The far-field acoustic estimate is a 1 % attenuation assumption, not a measurement.
  Actual field distribution in a vessel is highly non-uniform; scale-up beyond ~1 L needs
  either recirculation or flow-cell geometry.
- The 6 % agglomerated-mass assumption drives §4's ranking; it should be replaced with a
  measured PSD.
- The volatile index is a relative ranking of thermal exposure, not a predicted percentage
  loss of any specific aroma compound.
- Cavitation intensity also depends on dissolved gas content, which differs between fresh
  cold tap water and boiled-then-cooled water. Boiled water is degassed and will cavitate
  differently — control for this by using the same water source across arms.
