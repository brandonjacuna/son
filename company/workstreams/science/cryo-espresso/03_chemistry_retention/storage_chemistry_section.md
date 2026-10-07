# Storage chemistry and shelf-life kinetics of batched espresso

*Feasibility section, cryo-plate espresso chilling study. Track: storage chemistry.*
*All shared baseline assumptions adopted as issued; deviations are flagged in §0.2.*

---

## 0. Summary and scope

### 0.1 The headline result

**The chilling rate is not the design variable. Oxygen exclusion is.**

Across a balanced factorial spanning chill time constants τ ∈ {1.5, 10, 300, 1200 s}, hold
temperatures {4, 24, 65 °C}, three atmospheres and hold times to 72 h, the first-order
variance share attributable to **chilling rate is ≤ 3.3 %** for every marker, and **0.0–0.1 %**
when the comparison is restricted to the cryo-plate (τ = 1.5 s) against a plate heat exchanger
(τ = 10 s). Over the entire 840-cell comparator matrix the largest median-retention difference
between the cryo-plate and a 10 s plate heat exchanger is **1.05 percentage points**, on
2-furfurylthiol at 2 h hold, against a 5–95 % credible band on that same quantity **62
percentage points wide**. The marginal benefit of cryogenic chilling over a conventional plate
heat exchanger is **not merely small — it is roughly 60× smaller than the model's own
uncertainty**, and would be undetectable in any realistic sensory panel.

The same model says the levers that *do* work are cheap:

| Intervention | 2-FFT retention at 24 h (median) | Δ vs air baseline |
|---|---|---|
| Cryo-plate + air headspace | 0.110 | — |
| Cryo-plate + vacuum (50 mbar) | 0.448 | **+34 pp** |
| Cryo-plate + N₂/Ar to <1 % O₂ | 0.510 | **+40 pp** |
| Plate HX + N₂/Ar to <1 % O₂ | 0.508 | +40 pp |
| Ice bath + N₂/Ar to <1 % O₂ | 0.418 | +31 pp |

An inert-gas flush is worth roughly **40 percentage points** of thiol retention at 24 h. Going
from a 10 s plate heat exchanger to a 1.5 s cryo-plate is worth **0.17 percentage points**. The
expensive part of the proposed system is not doing the work.

### 0.2 Deviations from the shared baseline

- Beverage density and heat capacity are used as issued (ρ = 1010 kg/m³, cₚ = 3900 J/kg/K).
  Viscosity is **not** in the shared baseline; I take μ_brew = 1.7 × μ_water (see §4.1), which
  matters for the Stokes calculations only.
- Dissolved CO₂ taken at the mid-range of the issued estimate, **1.25 g/L**, with the
  justification and consequences in §5.
- The cryo-plate temperature trajectory is my own placeholder pending the thermal track's
  number: a linear plunge 78 °C → 3 °C over a 1.5 s film residence, then relaxation to the 4 °C
  hold with a 60 s vessel time constant. §2.3 shows the conclusion is insensitive to this
  choice across three orders of magnitude in τ, so the thermal track's actual number will not
  change it.

---

## 1. Pathway map and control-regime ranking

### 1.1 The seven reaction pathways plus one physical loss

Batched espresso changes by pathways that differ by **five orders of magnitude in rate**. The
useful organising question is not "does this pathway occur" — they all do — but "which control
variable is its bottleneck on a 0–72 h timescale". Ranking by 25 °C half-life in air:

| Rank | Pathway / marker | Control regime | t½ at 25 °C, air | Relevant on 0–72 h? |
|---|---|---|---|---|
| 1 | **2-furfurylthiol** (roasty-sulfury) | **OXYGEN-limited, and fast** | **1.2 h** | Dominant |
| 2 | Strecker aldehydes | Mixed temperature/time | 64 h | Marginal |
| 3 | 2,3-butanedione (buttery) | Mixed temperature/time | 96 h | Marginal |
| 4 | Lipid oxidation (emulsion) | Oxygen-limited, slow | 640 h | Negligible <72 h |
| 5 | Chlorogenic acid lactone hydrolysis | Time-limited | ~3900 h (163 d) | Negligible <72 h |
| 6 | Melanoidin / residual Maillard browning | Temperature-limited (Ea ≈ 110 kJ/mol) | ~6400 h | Negligible unless held hot |
| 7 | Acid formation / pH drift | Temperature-limited | ~7400 h | Negligible <72 h |
| 8 | 5-CQA isomerisation | Temperature-limited, pH-gated | ~19 000 h | Negligible at pH 5.1 |
| — | *Headspace partitioning (physical, not a reaction)* | *Process-limited* | *see §5.2* | *Only under vacuum* |

**The ranking collapses the problem.** Ranks 5–8 have half-lives of weeks to years at any
temperature ≤ 24 °C; nothing the chiller does in the first 60 seconds can matter to them,
because they will not have measurably progressed by the time the product is served. Ranks 2–4
sit at the edge of relevance. **Rank 1 is the entire problem** — and it is oxygen-limited, not
temperature-limited.

### 1.2 Pathway-by-pathway grounding

**(a) Thiol oxidation — 2-furfurylthiol.** This is the correct marker and it is severe. In fresh
brew, 84 % of available 2-furfurylthiol is lost over 60 min of storage, alongside
72 % of methanethiol and 68 % of 3-methyl-1H-pyrrole. Critically for this design, the
mechanism is **not** simple headspace escape: 2-FFT is reduced through a
combination of reversible chemical binding and irreversible losses, with bound 2-FFT released by
cysteine addition, demonstrating that reversible binding is the dominant mechanism of loss in
natural coffee brew. The binding partner is Maillard-derived:
2-furfurylthiol was the thiol most affected by melanoidin addition, its
concentration falling by a factor of 16, with stable-isotope dilution assays confirming rapid loss
of all thiols with increasing time while keeping brew warm in a thermos flask, and NMR/LC-MS
evidence that thiols are covalently bound to coffee melanoidins via Maillard-derived pyrazinium
compounds. A parallel route runs through quinones: quinones as the
oxidation products of hydroxyhydroquinone were found to actively bind 2-furfurylthiol, accounting
for its loss. Both routes require an oxidant to generate the electrophile — which is why
this pathway is oxygen-gated rather than merely thermal, and why the same paper found
cysteine at 0.045 g/L and ascorbic acid at 0.05 g/L directly protected aroma
during storage.

**(b) CGA lactone hydrolysis and CQA isomerisation.** Real but slow.
Ten coeluting chlorogenic acid lactones were identified as the top
predictive features for flavour instability in RTD coffee, with eight decreasing significantly
over four months of storage; the degradation of 3-O-caffeoyl-γ-quinide and 4-O-caffeoyl-γ-quinide
significantly impacted flavour stability at subthreshold concentrations. Four months, not
four hours — this is a months-scale pathway. For the CQAs, the pH dependence is the key gate:
3-, 4- and 5-CQA remain stable at acidic pH and become unstable at neutral
and alkaline pH, with degradation increasing with alkalinity, and
the rate constant is higher at higher pH over pH 5.0–9.0 at 37 °C.
Espresso at pH ~5.1 sits at the stable end of that range. I therefore assign CGA lactone
hydrolysis Ea ≈ 80 ± 15 kJ/mol and 5-CQA Ea ≈ 85 ± 20 kJ/mol as **class-typical
ester/depside hydrolysis values** — these are engineering estimates, not measured coffee-brew
activation energies, because the cited work reports Weibull-form kinetics at single temperatures
rather than an Arrhenius fit.

**(c) Acid formation and pH drift.** Slow and temperature-gated. In industrial cold brew,
the pH value decreased during storage and colour changed significantly in
brightness — over 90–270 day timescales. Under high-pressure processing,
both unprocessed and HPP samples showed changes in pH, titratable acidity and
colour stability after 60 days at 23 °C. Sixty days at 23 °C is the relevant benchmark; a
72 h hold at 4 °C is ~1/500th of that thermal dose.

**(d) Strecker aldehydes and dicarbonyls.** The controlling reference here is a 30-day brew
storage study: changes in the volatile fraction of Arabica brews stored at
4 and 25 °C were, in general, slower and less pronounced at refrigeration temperature, with stored
brews losing aroma intensity and freshness and acquiring rancid notes mainly at 25 °C. The
dicarbonyl pool has an additional sink independent of oxygen: melanoidins from
coffee are able to scavenge α-dicarbonyl compounds. My rate constants for these two markers
are **engineering estimates anchored to that 4 vs 25 °C contrast**, not fitted values.

**(e) Lipid oxidation.** Espresso carries a real lipid load —
espresso and boiled coffee reach 60–160 mg lipids per 150 mL cup, versus
under 7 mg for paper-filtered brew, with triglycerides and diterpene alcohol esters at 86.6–92.9 %
and 6.5–12.5 % of total lipids. That is **0.4–1.1 g/L**, above the 0.1–0.2 g/L figure in
the task brief; I use 0.5 g/L as the working value and note the discrepancy for the mass-transfer
track. Autoxidation is the most strictly oxygen-dependent pathway in the set (φ_O₂ = 0.95) but is
also slow: the rancid notes in the reference study took 30 days at 25 °C to appear, and at 4 °C
did not.

**(f) Residual Maillard chemistry.** Only matters in a warm-held product. Ea for Maillard browning
in model systems runs ~100–130 kJ/mol; I use 110 ± 20 kJ/mol. At that Ea, dropping from 65 °C to
4 °C slows the reaction by a factor of ~1400. This is the one pathway for which the *hot-hold*
comparator is genuinely disqualifying, and it is also the pathway for which chilling of any kind —
fast or slow — solves the problem completely.

**(g) Physical headspace partitioning.** Separated out and treated as an equilibrium, not a rate;
see §5.2. It is negligible in a sealed vessel and **significant only under vacuum**, where it
becomes a design liability rather than a benefit.

---

## 2. Arrhenius model driven by an actual temperature history

### 2.1 Governing equations

Each marker decays by pseudo-first-order kinetics with an oxygen-dependent rate split:

$$\frac{dC_i}{dt} = -k_i\big(T(t),\,[\mathrm{O}_2](t)\big)\,C_i$$

$$k_i(T,[\mathrm{O}_2]) = k_{i,\mathrm{ref}}\exp\!\left[-\frac{E_{a,i}}{R}\left(\frac{1}{T}-\frac{1}{T_\mathrm{ref}}\right)\right]
\left[(1-\phi_{\mathrm{O}_2,i}) + \phi_{\mathrm{O}_2,i}\left(\frac{[\mathrm{O}_2]}{[\mathrm{O}_2]_\mathrm{ref}}\right)^{n_i}\right]$$

with T_ref = 298.15 K and [O₂]_ref = 8.42 mg/L (air saturation at 25 °C). The bracketed term is
the load-bearing structure: **φ_O₂ is the fraction of the air-saturated rate carried by the
oxygen-dependent branch**, so setting the atmosphere to inert does not switch the pathway off, it
reduces it to its (1 − φ_O₂) anoxic floor. For 2-FFT, φ_O₂ = 0.75 ± 0.12 and n = 0.7 — sub-first
order because the rate-limiting step is quinone/pyrazinium *formation*, which saturates.

Retention at time t is the exponential of the accumulated rate integral,

$$R_i(t) = \exp\!\left[-\int_0^{t} k_i\big(T(\tau),[\mathrm{O}_2](\tau)\big)\,d\tau\right] \times \Pi_i$$

where Π_i is the physical partitioning retention factor of §5.2. **The integral, not a setpoint,
is what the model evaluates** — the chilling transient and the hold both enter through T(τ), which
is what makes the "first 60 seconds are decisive" claim testable.

### 2.2 Oxygen mass balance

Oxygen is a depleting inventory shared between liquid and headspace, not a fixed label. With
headspace ratio h = V_gas/V_liq, Henry-law partitioning S(T) [mg/L per unit O₂ mole fraction] and
the ideal-gas headspace capacity G(T,h) = h·M_O₂/(RT):

$$\frac{d\,n_{\mathrm{O}_2,\mathrm{tot}}}{dt} = -k_{\mathrm{O}_2}(T)\,\frac{S(T)}{S(T)+G(T,h)}\,n_{\mathrm{O}_2,\mathrm{tot}},
\qquad [\mathrm{O}_2]_\mathrm{liq} = \frac{n_{\mathrm{O}_2,\mathrm{tot}}}{S+G}\,S$$

k_O₂ is an engineering estimate: a 12 h half-life for dissolved O₂ at 25 °C with Ea = 55 kJ/mol,
representing the aggregate consumption by phenolics. Its basis is stoichiometric — see §2.5.

### 2.3 Temperature histories

Five trajectories, all starting at the issued spout temperature of 78 °C:

| Arm | T(t) | Hold | Chill-phase thermal dose |
|---|---|---|---|
| Hot thermos | exponential, τ = 120 s | 65 °C | **15.4 equivalent-hours at 4 °C** |
| Ambient bench | exponential, τ = 1200 s | 24 °C | **36.5 equiv-h** |
| Ice bath | exponential, τ = 300 s | 4 °C | **5.96 equiv-h** |
| Plate heat exchanger | linear, 10 s | 4 °C | **0.141 equiv-h (509 s)** |
| **LN₂ cryo-plate** | linear, 1.5 s, then 60 s vessel relaxation | 4 °C | **0.021 equiv-h (75 s)** |

*Thermal dose* is ∫exp[−(Ea/R)(1/T − 1/277.15)]dt over the chilling transient with Ea = 60 kJ/mol
— the reaction time the transient costs you, expressed in equivalent seconds at the 4 °C hold.

**This table is the whole argument, and it is legible before any Monte Carlo runs.** The
cryo-plate saves 434 equivalent-seconds relative to the plate heat exchanger. The plate heat
exchanger saves 21 000 equivalent-seconds relative to an ice bath, and 131 000 relative to bench
cooling. Against a 72 h (259 200 s) hold, the cryo-plate's advantage is **0.17 % of the total
thermal dose**. The first 60 seconds are decisive *only* in the comparison between chilling and
not chilling — not in the comparison between fast chilling and very fast chilling.

### 2.4 Monte Carlo uncertainty propagation

400 draws per comparator cell (200 for the factorial). Ea ~ Normal(μ, σ) truncated to
[25, 150] kJ/mol; φ_O₂ ~ Normal truncated to [0,1]; k_ref lognormal with geometric SD 1.5 for
literature-anchored markers and 2.0 for pure engineering estimates. Reported quantities are
medians with 5–95 % credible bands. **Kinetic-parameter uncertainty is the single largest
variance component in most cells** (46–89 % for the slow markers) — an honest reflection of the
fact that measured coffee-brew activation energies for these pathways largely do not exist.

### 2.5 Is the oxygen budget even limiting?

A sealed 1 L vessel with a 20 % headspace at 4 °C holds:

- **air:** 13.1 mg/L dissolved + 59.0 mg/L in headspace = **72.1 mg O₂ per litre = 2252 µmol/L**
- **vacuum (50 mbar):** 3.60 mg/L total
- **N₂/Ar to <1 % O₂:** 2.75 mg/L total

Against a 2-FFT pool of ~0.88 µmol/L (0.1 mg/L), air-headspace oxygen is in **2600-fold molar
excess**. Oxygen never runs out on the thiol's account. What *can* deplete it is the bulk
reducing-substrate pool: CGAs at ~2.5 g/L are ~7056 µmol/L, a **3.1× molar excess over the
oxygen**. This is why k_O₂ is finite and why the air-headspace arm shows dissolved O₂ falling
only from 8.7 to 7.9 mg/L over 24–72 h at 4 °C: the antioxidant pool consumes O₂ slowly at
refrigerated temperature, so **the O₂ is still there for the whole hold**. Reducing the
headspace ratio helps but does not substitute for flushing — at V_g/V_l = 0.002 (a completely
filled vessel), 24 h 2-FFT retention rises only from 0.095 to 0.239, versus 0.510 with an inert
flush.

**Design consequence, and it is counter-intuitive:** cooling *increases* dissolved oxygen. Air
saturation is 3.49 mg/L at 78 °C and 13.11 mg/L at 4 °C — **a 3.8× increase in the oxidative
driving force**. A cryo-plate that flash-chills espresso into an open collection vessel under
air is actively loading the product with oxygen at the exact moment it makes that oxygen most
soluble. **Chilling under air is partially self-defeating.**

---

## 3. Comparator matrix and variance decomposition

### 3.1 Predicted retention

Full 5 × 3 × 7 × 8 matrix (chill × atmosphere × hold time × marker, 840 rows with medians and
5–95 % bands) in `comparator_matrix.csv`. Median retention at 24 h:

| Marker | Thermos 65 °C, air | Bench, air | Ice bath, air | Plate HX, air | **Cryo, air** | Plate HX, inert | **Cryo, inert** |
|---|---|---|---|---|---|---|---|
| 2-furfurylthiol | 0.000 | 0.000 | 0.066 | 0.108 | **0.110** | 0.508 | **0.510** |
| Strecker aldehydes | 0.036 | 0.759 | 0.944 | 0.954 | **0.955** | 0.964 | **0.964** |
| 2,3-butanedione | 0.063 | 0.836 | 0.969 | 0.977 | **0.977** | 0.983 | **0.984** |
| Lipid integrity | 0.924 | 0.979 | 0.993 | 0.994 | **0.994** | 0.999 | **0.999** |
| CGA lactones | 0.831 | 0.994 | 0.999 | 1.000 | **1.000** | 1.000 | **1.000** |
| Colour stability | 0.625 | 0.992 | 0.999 | 1.000 | **1.000** | 1.000 | **1.000** |
| pH stability | 0.857 | 0.996 | 0.999 | 1.000 | **1.000** | 1.000 | **1.000** |
| 5-CQA | 0.956 | 0.999 | 1.000 | 1.000 | **1.000** | 1.000 | **1.000** |

Read the last four columns. **The cryo and plate-HX columns are identical to three decimal
places on every row.** The inert columns differ from the air columns by 40 points on the marker
that matters.

### 3.2 The chilling-transient cost, isolated

Retention at t = 0 — i.e. what the chilling trajectory alone costs, before any hold:

| Marker | Thermos | Bench | Ice bath | Plate HX | Cryo-plate |
|---|---|---|---|---|---|
| 2-furfurylthiol | 0.594 | 0.882 | **0.966** | **0.966** | **0.966** |
| Strecker aldehydes | 0.525 | 0.799 | **0.935** | **0.935** | **0.935** |

The ice bath, plate HX and cryo-plate arms are **indistinguishable at t = 0** to three decimals.
Once the transient is faster than ~5 minutes, further speed buys nothing, because the residual
3.4 % thiol loss is incurred in the portafilter and the spout — upstream of any chiller. The
78 °C spout temperature in the shared baseline means the beverage has *already* spent time hot
before it reaches the plate.

### 3.3 Variance decomposition

First-order (main-effect) variance shares of log-retention, over a balanced factorial with
chilling rate and hold temperature varied **orthogonally** (so the two are separable, which they
are not in the comparator matrix where cold-hold arms are also fast-chill arms):

| Marker | Chilling rate | Hold temperature | Oxygen | Hold time | Parameter uncertainty | Interactions |
|---|---|---|---|---|---|---|
| 2-furfurylthiol | **0.1 %** | 64.9 % | 2.7 % | 12.4 % | 12.8 % | 7.1 % |
| Strecker aldehydes | **0.0 %** | 39.5 % | 6.4 % | 5.4 % | 31.0 % | 17.7 % |
| 2,3-butanedione | **0.0 %** | 25.4 % | 0.0 % | 10.2 % | 46.6 % | 17.7 % |
| CGA lactones | **0.0 %** | 17.2 % | 0.0 % | 7.5 % | 61.2 % | 14.2 % |
| Lipid integrity | **0.0 %** | 10.6 % | 6.2 % | 5.1 % | 66.0 % | 12.2 % |
| Colour stability | **0.0 %** | 17.5 % | 0.0 % | 7.2 % | 61.1 % | 14.2 % |
| pH stability | **0.0 %** | 9.8 % | 0.0 % | 4.0 % | 78.2 % | 7.9 % |
| 5-CQA | **0.0 %** | 4.9 % | 0.0 % | 2.1 % | 89.0 % | 4.0 % |

Restricted to the arms a café would actually choose between — **all held at 4 °C** — the
decomposition for 2-FFT becomes: chilling rate **3.3 %**, oxygen **14.6 %**, hold time
**27.5 %**, parameter uncertainty 45.3 %, interactions 9.3 %. Chilling rate rises from 0.1 % to
3.3 % only because the temperature axis has been removed; it remains the smallest controllable
term. Restricted further to τ ≤ 10 s — the cryo-versus-plate-HX contrast specifically —
chilling rate falls to **0.0 %**.

### 3.4 Verdict on the marginal benefit of cryogenic chilling

**The marginal benefit of the cryo-plate over a 10 s plate heat exchanger is within model
uncertainty, and by a wide margin.**

- Largest median difference anywhere in the 840-cell matrix: **1.05 pp** (2-FFT, 2 h hold).
- Median difference at the nominal 24 h service point: **0.17 pp**.
- 5–95 % credible band width on that same quantity: **~62 pp**.
- Ratio of signal to model uncertainty: **≈ 1:60**.

This conclusion is robust to the cryo-plate's exact trajectory. §2.3 shows that varying τ across
three orders of magnitude (1.5 s to 1200 s) moves the answer materially only when τ exceeds
~100 s. **If the thermal track's real τ comes back anywhere below 10 s, nothing here changes.**

I want to be explicit that this is the answer the model gives, not a hedge: **the cryogenic
chilling is not doing the work the design assumes it is doing.** The claim that "the first 60
seconds are decisive" is *true* — but the decisive comparison inside those 60 seconds is
chilling versus a hot hold, not 1.5 s versus 10 s. A €50 nitrogen regulator captures ~40
percentage points of thiol retention; the cryogenic apparatus captures ~0.2.

![Predicted marker retention versus hold time]({{artifact:cd8dfd23-8e4e-45b3-ad5b-845156bd0f05}})

![Sensitivity decomposition]({{artifact:73d2ea7c-e20d-40f4-8cff-720784f2c189}})

---

## 4. Emulsion and colloid stability

### 4.1 Stokes creaming and sedimentation

For a sphere of radius a in creeping flow (Re ≪ 1, verified: Re < 10⁻⁴ for all cases):

$$v = \frac{2}{9}\frac{(\rho_p - \rho_f)\,g\,a^2}{\mu}$$

Brew viscosity: μ_brew = 1.7 × μ_water (engineering estimate; espresso viscosity is elevated over
filter brew at 9.5 % TDS — physical measurements across eight extraction methods
covering density, pH, conductivity and viscosity confirm espresso as the most concentrated
case — but I do not have a measured value at this TDS, so the multiplier carries ±0.2).
This gives μ = 2.6 mPa·s at 4 °C and 1.5 mPa·s at 24 °C: **cooling alone slows all colloidal
motion by 1.7×**, which is a genuine (if modest) stability benefit of cold storage.

Time to traverse a 150 mm liquid depth:

| Particle | d (µm) | v at 4 °C (mm/h) | Traverse time at 4 °C | at 24 °C |
|---|---|---|---|---|
| Oil droplet, crema emulsion | 0.5 | −0.017 (cream) | **8650 h** | 5260 h |
| Oil droplet, typical | 2 | −0.28 | **541 h** | 329 h |
| Oil droplet, large | 10 | −6.9 | **21.6 h** | 13.2 h |
| Oil droplet, flocculated | 30 | −62 | **2.4 h** | 1.5 h |
| Fines, sub-micron | 0.5 | +0.081 (settle) | **1841 h** | 1077 h |
| Fines, 5 µm | 5 | +8.1 | **18.4 h** | 10.8 h |
| Fines, 20 µm | 20 | +130 | **1.15 h** | 0.67 h |
| Fines, 50 µm (basket bypass) | 50 | +815 | **0.18 h** | 0.11 h |

Full table with Péclet numbers in `colloid_stability.csv`. ρ_oil = 920 kg/m³, ρ_fines = 1450
kg/m³ (hydrated cell-wall material) are engineering estimates.

**Findings:**

1. **The emulsion itself is stable over the whole hold window.** Sub-micron and 2 µm droplets
   have Pe ≈ 0.004 and 1.0 respectively — Brownian motion competes with or dominates gravity, and
   the traverse times are 500–8000 h. Coffee lipid emulsions are stabilised by surface-active
   melanoidin and protein-like material; the espresso foaming fraction
   subdivides into a high-molecular-weight polysaccharide fraction and a lower-MW
   protein/melanoidin fraction, the latter with greater foaming capability and the former
   contributing foam stability. **Resuspension for the emulsion is not required.**

2. **The fines are a different story and they are the real problem.** Anything above ~20 µm
   clears the vessel depth in **under 1.2 h**. At 60 shots/hour into a shared batch, a visible
   sediment layer forms within the first hour of the service day. **The product will require
   resuspension at service** — and resuspension of a cold, CO₂-supersaturated liquid is a foaming
   event (§5.1).

3. **Flocculation is the failure mode to watch on the emulsion side.** A single 30 µm floc creams
   in 2.4 h. The emulsion is stable *as long as it stays deflocculated*; freeze-concentration
   (§4.3) is precisely the mechanism that flocculates it.

### 4.2 Cold-storage sediment and haze as a customer-visible defect

This is a documented, mechanism-characterised RTD-coffee defect, and it is worse for espresso
than for the products in which it was studied. RTD coffee products
often experience sedimentation that compromises product quality and consumer acceptance; two
mechanisms operate — galactomannan crystallisation and protein–polyphenol interactions — with
high-temperature extraction promoting galactomannan crystallisation and mannose enrichment in the
sediments, and low-temperature extraction favouring protein–polyphenol aggregation.
Espresso is a **93 °C extraction at 9 bar** — squarely in the galactomannan-crystallisation
regime, and at the highest solids concentration of any brew method. The underlying insolubility
is well established: galactomannan is the main polysaccharide component of
the insoluble fractions of coffee extracts and is probably responsible for sediment
formation.

Galactomannan crystallisation is **promoted by cold**, so this defect is a direct cost of the
cold-hold strategy that the chilling design does nothing to address. Mitigations exist and are
documented — Rohapect B1L and Galactomannanase ACH gave the highest sediment
reduction at 0.3 and 0.1 mg protein/g substrate — but adding a mannanase to café espresso
is a product-formulation decision well outside this device's scope. **The realistic mitigation is
mechanical: filter the batch at ~30–50 µm before storage, and specify agitation at service.**

### 4.3 Freeze-concentration on the cryo-plate: the significant risk

This is where cryogenic chilling introduces a failure mode that gentler methods do not have.

**Freezing point of the beverage.** With TDS = 96.0 g/L, taking ~55 % of solids as low-MW
(caffeine 194, trigonelline 137, CQAs 354, sugars 180, organic acids 90–192; number-average
M ≈ 250 g/mol) and melanoidins as osmotically negligible per gram, the osmotically active
molality is 0.233 mol/kg water and the colligative depression is

$$\Delta T_f = K_f\, m = 1.86 \times 0.233 = \mathbf{0.43\ K} \quad\Rightarrow\quad T_f \approx \mathbf{-0.43\ ^\circ C}$$

**This is the finding: espresso freezes essentially at 0 °C.** A 9.5 % TDS beverage is
colligatively almost as dilute as water. There is no meaningful freezing-point buffer.

**Ice fraction and freeze-concentration.** Following the freezing-point curve to the maximally
freeze-concentrated state (vitrification at ~80 % w/w solids, T_g′ ≈ −35 °C, engineering
estimate for a carbohydrate/melanoidin extract):

| Wall/liquid temperature | Ice fraction | Unfrozen-phase TDS |
|---|---|---|
| −0.43 °C | 0.00 | 9.5 % |
| −0.7 °C | 0.38 | 15.3 % |
| −1.0 °C | 0.57 | 21.9 % |
| −2.0 °C | 0.78 | 43.8 % |
| ≤ −5 °C | 0.88 | **80 % (maximally freeze-concentrated)** |

**Two degrees below zero concentrates the unfrozen phase 4.6-fold.** Five degrees below zero
takes it to a syrup. And the plate in this design is coupled to a **77 K** LN₂ bath through a
**single continuous metal body with no specified thermal break** — a boundary condition 350 K
below the freezing point of the product.

**Will the film reach 0 °C?** The liquid thermal diffusivity is α = k/(ρcₚ) = 1.57 × 10⁻⁷ m²/s.
The conduction time for a falling film of thickness δ is τ_cond ≈ δ²/(π²α):

| Film thickness | Conduction time |
|---|---|
| 0.3 mm | **58 ms** |
| 0.5 mm | 161 ms |
| 1.0 mm | 644 ms |
| 2.0 mm | 2.6 s |

Against a film residence time of order 1 s, **a sub-millimetre film is thermally thin — the
liquid at the wall equilibrates to the wall temperature in tens of milliseconds.** If any part
of the plate surface sits below −0.43 °C, ice nucleates there. Given a 77 K sink and no thermal
break, the plate surface will not merely dip below −0.43 °C; it will be hundreds of degrees
below it unless the thermal track demonstrates otherwise. **My working expectation is that the
espresso freezes on contact, and the "falling film" becomes a growing ice crust.**

**Why freeze-concentration breaks the emulsion irreversibly.** The classic mechanism, and every
step of it applies here:

1. Ice growth rejects solutes into a shrinking unfrozen phase, concentrating TDS 4.6× at −2 °C
   and ~8× at the maximally freeze-concentrated state.
2. The oil droplets are **also** rejected from the ice, so they are forced into that same
   shrinking volume — droplet number concentration rises by the same factor. Collision frequency
   scales as the square of number density, so a 4.6× concentration is a **~21× increase in
   collision rate**.
3. The concentrated phase has vastly higher ionic strength, which compresses the electrical
   double layer and **removes electrostatic stabilisation** from the melanoidin-coated droplets.
4. Ice crystals mechanically press droplets together at grain boundaries — the classic
   freeze-thaw destabilisation geometry.
5. Coffee lipid is ~87–93 % triglyceride and **crystallises in this temperature range**, so
   droplets contain solid fat. Partial coalescence — where a fat crystal from one droplet pierces
   the interfacial film of another — is the fastest and **least reversible** emulsion-breaking
   mechanism known in dairy and confectionery systems. Cooling to 4 °C alone puts coffee oil
   below its crystallisation range; freezing guarantees it.

Steps 3–5 are **not reversed by thawing**. Coalesced droplets do not re-divide. The visible
consequence at service is oil separation — an oil slick or ring at the cup surface — plus loss of
crema-forming material, since the same surface-active fraction stabilises both the emulsion and
the foam.

**Design correction:** the plate surface must be held **above 0 °C at every point wetted by
beverage**, with margin — I recommend a **+4 °C surface-temperature floor**, giving ~4.4 K of
margin against the −0.43 °C freezing point to cover surface-temperature non-uniformity and
transient overshoot between shots. Since the shared baseline specifies no thermal break, **a
thermal break, or active surface-temperature control, is a requirement, not an option.** That
is a finding I am handing to the thermal track.

A second-order consequence, worth flagging: any ice that forms and *stays* on the plate between
shots becomes a freeze-concentrated syrup layer at 80 % solids sitting on the food-contact
surface between service cycles. That is a cleaning and food-safety issue for the safety track.

---

## 5. CO₂, headspace and the physical-loss term

### 5.1 CO₂ inventory

At the working estimate of 1.25 g/L (28.4 mmol/L) — justified as mid-range for espresso, which is
strongly supersaturated because the carbon dioxide formed during roasting is
responsible for crema formation in espresso and the 9 bar extraction retains far more CO₂
than an atmospheric brew — the vessel consequences are:

| Storage condition | Headspace p(CO₂) | Dissolved CO₂ retained |
|---|---|---|
| Sealed, 4 °C, V_g/V_l = 0.20 | **0.40 atm (5.9 psi)** | 1.10 g/L (88 %) |
| Sealed, 24 °C, V_g/V_l = 0.20 | **0.66 atm (9.7 psi)** | 1.01 g/L (81 %) |
| Sealed, 4 °C, V_g/V_l = 0.05 | 0.44 atm (6.4 psi) | 1.21 g/L (97 %) |
| Vacuum, 50 mbar, 4 °C | 0.05 atm | **0.14 g/L (11 %)** |

**Three consequences.**

*(a) A sealed storage vessel is a pressure vessel.* 5.9 psi at 4 °C, rising to 9.7 psi if the
vessel warms to ambient. Modest, but it is not zero and the vessel must be rated for it — and if
a batch is sealed warm and then chilled, the pressure *falls*, which can collapse a soft vessel
or draw air in through a marginal seal. **Seal integrity under a partial vacuum is the failure
mode**, and it is exactly the failure mode that lets oxygen in. Handing to the safety track.

*(b) Vacuum storage destroys the CO₂ and therefore the crema.* Pulling to 50 mbar removes 89 % of
the dissolved CO₂ and evolves **12.9 L of gas per litre of beverage** at that pressure (646 mL at
STP). This is not a slow leak — it is vigorous outgassing from a supersaturated, surfactant-rich
liquid, i.e. **violent foaming**. A vacuum-storage design must accommodate roughly 13 vessel
volumes of gas evolution and the foam that comes with it. The product that emerges is
decarbonated and will not form crema.

*(c) The inert flush has a milder version of the same problem.* Three headspace volumes of N₂
(0.6 L per L of beverage) strips a meaningful CO₂ fraction. **Flush gently, through the headspace
only, never sparged through the liquid.** An argon flush at low flow, or better, displacement
filling with the vessel pre-purged, avoids most of the loss.

### 5.2 Physical partitioning loss, isolated from reaction

Treating volatile loss as an equilibrium rather than a rate, with air/water partition coefficient
K_aw(T) = K_aw(298)·exp[(ΔH_solv/R)(1/298 − 1/T)], ΔH_solv = 45 kJ/mol:

$$\Pi_i = \underbrace{\frac{1}{1 + K_{aw,i}\,h}}_{\text{sealed equilibration}} \times \underbrace{\exp\!\left(-K_{aw,i}\,\frac{V_\text{swept}}{V_l}\right)}_{\text{purge / outgassing}}$$

| Marker | Sealed air | N₂ flush (0.6 L/L swept) | **Vacuum (12.9 L/L swept)** |
|---|---|---|---|
| 2-furfurylthiol | 0.998 | 0.994 | **0.905** |
| Strecker aldehydes | 0.997 | 0.988 | **0.820** |
| 2,3-butanedione | 1.000 | 1.000 | 0.993 |

**Physical loss is negligible in a sealed or gently-flushed vessel and becomes significant only
under vacuum**, where the CO₂ outgassing sweeps 12.9 L of gas per litre through the product and
carries volatiles with it. This is why the vacuum arm underperforms the inert arm in §3.1 (0.448
vs 0.510 for 2-FFT at 24 h) despite having comparable residual oxygen: **vacuum wins the
chemistry and loses the physics.**

**Recommendation: inert gas, not vacuum.** N₂ or Ar to <1 % O₂ delivers the oxygen exclusion
without the decarbonation, the foaming, the volatile stripping, or the vessel-collapse risk.

---

## 6. Failure modes, corrections, and what the other tracks need

### 6.1 Failure modes identified

1. **Freezing and freeze-concentration on the plate** (§4.3) — beverage freezes at −0.43 °C; a
   plate coupled to 77 K with no thermal break will be far below that; irreversible emulsion
   breaking by partial coalescence.
2. **Cold-chilling under air loads the product with oxygen** (§2.5) — O₂ solubility rises 3.8×
   from 78 °C to 4 °C, so a fast chill into air is partially self-defeating.
3. **Fines sedimentation within 1.2 h** (§4.1) — customer-visible layer forming during the
   service day, requiring resuspension.
4. **Cold-promoted galactomannan crystallisation haze** (§4.2) — a documented RTD defect that
   espresso's high-temperature, high-solids extraction makes worse, and which cold storage
   promotes.
5. **Vacuum storage decarbonates the product and strips volatiles** (§5.1, §5.2) — 89 % CO₂ loss,
   12.9 L/L gas evolution, 10–18 % additional volatile loss.
6. **Sealed-vessel pressure cycling** (§5.1) — 5.9 psi cold to 9.7 psi warm; a chilled sealed
   vessel can go sub-atmospheric and draw air past a marginal seal.
7. **2-FFT is gone in hours regardless** (§3.1) — even the best arm (cryo + inert + 4 °C) holds
   only 51 % of the roasty thiol at 24 h and 14 % at 72 h. **No storage strategy in this matrix
   makes 72 h espresso taste like fresh espresso.**

### 6.2 Design corrections

1. **Specify a thermal break or active surface-temperature control** with a plate-surface floor
   of **+4 °C** everywhere wetted. Not optional.
2. **Flush with N₂ or Ar to <1 % O₂ headspace. Do not use vacuum.** This is the single
   highest-value intervention in the whole system, worth ~40 pp of thiol retention at 24 h.
3. **Fill vessels to minimum headspace** (V_g/V_l ≤ 0.05) *in addition to* flushing — worth a
   further few points and reduces the O₂ reservoir 4×.
4. **Reconsider whether the cryogenic apparatus is justified at all.** A 10 s plate heat exchanger
   delivers retention indistinguishable from the cryo-plate on every marker, with no LN₂ logistics,
   no cryogenic burn hazard, no asphyxiation risk, no freeze-concentration failure mode, and no
   thermal-break requirement. If the design goal is beverage quality, this analysis does not
   support the cryogenic approach.
5. **Filter the batch at 30–50 µm before storage** and specify gentle agitation at service.
6. **Set the practical shelf life at 6–12 h, not 72 h**, if fresh-espresso character is the target.
   At 12 h under inert atmosphere at 4 °C the model gives 2-FFT retention ~0.71 (median). Beyond
   24 h the product is a different beverage — perfectly acceptable as cold coffee, but it is not a
   held espresso shot.

### 6.3 Numbers other tracks must reuse

**To the thermal track:** the plate surface temperature floor is **+4 °C** at every wetted point;
the beverage freezing point is **−0.43 °C** with only 0.43 K of colligative buffer. A
sub-millimetre film equilibrates to the wall in **58 ms**, so surface temperature — not bulk
plate temperature — is the controlling variable. My chill trajectory placeholder (78 °C → 3 °C
linear over 1.5 s, 60 s vessel relaxation to 4 °C) should be replaced with your measured T(t),
but §2.3 shows the storage-chemistry conclusion is insensitive to any τ below ~10 s.

**To the mass-transfer track:** dissolved O₂ at air saturation is **3.49 mg/L at 78 °C and
13.11 mg/L at 4 °C** — cooling raises the O₂ driving force 3.8×, so the open falling-film
geometry is an oxygen-absorption device. I need your estimate of O₂ uptake across the film during
the ~1 s of exposure; if it approaches saturation my air-arm predictions are optimistic.
Espresso lipid load is **0.4–1.1 g/L** (from measured per-cup data), higher than the 0.1–0.2 g/L
in the brief. CO₂ evolution during a vacuum pull-down is **12.9 L per L of beverage at 50 mbar**.

**To the safety track:** a sealed storage vessel reaches **0.40 atm (5.9 psi) CO₂ overpressure at
4 °C, rising to 0.66 atm (9.7 psi) at 24 °C**. A vessel sealed hot and then chilled goes
sub-atmospheric — seal-integrity failure admits oxygen and defeats the flush. Any ice that
persists on the plate between shots becomes an 80 % w/w solids syrup layer on a food-contact
surface.

---

## 7. Uncertainties and what would reduce them

1. **No measured activation energies exist for most of these pathways in coffee brew.** Six of
   eight Ea values are class-typical engineering estimates with ±15–20 kJ/mol standard
   deviations. This is the largest single uncertainty and it dominates the variance decomposition
   (46–89 % for slow markers). *It does not change the conclusion*: chilling rate's share is
   ≤3.3 % under **every** Ea draw, because the argument is a thermal-dose argument, not an
   Ea-sensitive one.
2. **The 2-FFT rate constant is anchored to one study.** The 84 %/60 min figure is from a single
   brew system at unstated cooling profile; I back-extrapolated to 25 °C assuming Ea = 60 kJ/mol
   and a ~40 °C mean transient. A factor-of-2 error here shifts all t₅₀ values by 2× but changes
   no ranking.
3. **φ_O₂ for 2-FFT (0.75 ± 0.12) is an inference, not a measurement.** The mechanism is
   quinone/pyrazinium binding, which requires an oxidant, but the anoxic floor has not been
   measured in brew. If the true φ_O₂ were 0.4, the inert-flush benefit halves — to ~20 pp,
   still two orders of magnitude above the cryo benefit.
4. **k_O₂ (12 h half-life at 25 °C) is unmeasured.** Its stoichiometric justification (§2.5) is
   sound but the rate is a guess. A faster k_O₂ would make sealed air-headspace storage
   self-limiting after the first day, improving the air arm at long hold times.
5. **A large fraction of 2-FFT loss is reversible binding, not destruction** — the cysteine-release
   evidence is unambiguous. My model treats all loss as decay of the *available* pool, which is
   the sensorially correct quantity, but it means "retention" here is availability, not total
   2-FFT. It also means a cysteine or ascorbate addition at service could partially reverse the
   loss, an intervention entirely outside the chilling architecture.
6. **Emulsion droplet size distribution is an engineering estimate.** I found no PubMed-indexed
   measurement of espresso oil droplet size. The 0.5–10 µm range is inferred from the beverage's
   optical opacity and general emulsion behaviour. If real droplets are predominantly >10 µm, the
   creaming timescale drops to ~20 h and resuspension becomes mandatory for the emulsion too.
7. **The freezing analysis assumes ideal colligative behaviour** at 9.5 % w/w. Real activity
   coefficients would shift ΔT_f modestly — but the depression is 0.43 K against a 350 K driving
   force, so no plausible non-ideality changes the conclusion that the beverage freezes.
8. **The 80 % w/w maximally-freeze-concentrated solids and T_g′ ≈ −35 °C are estimates** for a
   carbohydrate/melanoidin system, not measurements on espresso.

---

## 8. References

All identifiers verified against PubMed. Where I state a value is an engineering estimate, no
citation is offered because none exists.

1. PMID **31174781** — Aroma binding and stability in brewed coffee: a case study of
   2-furfurylthiol. *Food Chemistry* (2019). doi:10.1016/j.foodchem.2019.05.175
2. PMID **11782201** — Chemical interactions between odor-active thiols and melanoidins involved
   in the aroma staling of coffee beverages. *J Agric Food Chem* (2002). doi:10.1021/jf010823n
3. PMID **32283367** — Enhancement of coffee brew aroma through control of the aroma staling
   pathway of 2-furfurylthiol. *Food Chemistry* (2020). doi:10.1016/j.foodchem.2020.126754
4. PMID **18422327** — Changes in volatile compounds and overall aroma profile during storage of
   coffee brews at 4 and 25 °C. *J Agric Food Chem* (2008). doi:10.1021/jf703731x
5. PMID **35763924** — Identification of subthreshold chlorogenic acid lactones that contribute to
   flavor instability of ready-to-drink coffee. *Food Chemistry* (2022).
   doi:10.1016/j.foodchem.2022.133555
6. PMID **23298331** — Degradation kinetics of chlorogenic acid at various pH values.
   *J Agric Food Chem* (2013). doi:10.1021/jf304105w
7. PMID **27405173** — Degradation kinetics of chlorogenic, cryptochlorogenic and neochlorogenic
   acid at neutral and alkaline pH. *Acta Pharm Sin* (2016).
8. PMID **41353822** — Coffee beverage sedimentation: from roasting effects to storage stability.
   *Food Chemistry* (2025). doi:10.1016/j.foodchem.2025.147387
9. PMID **26050180** — Sediments in coffee extracts: composition and control by enzymatic
   hydrolysis. *Food Chemistry* (2008). doi:10.1016/j.foodchem.2008.01.029
10. PMID **37893733** — Effect of cold brew coffee storage in industrial production on the
    physical-chemical characteristics of final product. *Foods* (2023). doi:10.3390/foods12203840
11. PMID **38231670** — High-pressure processing for cold brew coffee: safety and quality under
    refrigerated and ambient storage. *Foods* (2023). doi:10.3390/foods12234231
12. PMID **38370052** — Shelf life of cold brew coffee and the influence of extraction temperature.
    *Food Sci Nutr* (2024). doi:10.1002/fsn3.3812
13. PMID **8477916** — Lipid content and composition of coffee brews prepared by different methods.
    *Food Chem Toxicol* (1993). doi:10.1016/0278-6915(93)90076-b
14. PMID **15537326** — Investigations on the high molecular weight foaming fractions of espresso
    coffee. *J Agric Food Chem* (2004). doi:10.1021/jf049013c
15. PMID **32410507** — Unravelling the science of coffee foam: a comprehensive review.
    *Crit Rev Food Sci Nutr* (2020). doi:10.1080/10408398.2020.1765136
16. PMID **31496242** — Melanoidins from coffee, cocoa and bread are able to scavenge α-dicarbonyl
    compounds. *J Agric Food Chem* (2019).
17. PMID **26059131** — Kinetics of color development, pH decreasing and antioxidative activity
    reduction of Maillard reaction in galactose/glycine model systems. *Food Chemistry* (2007).
18. PMID **30716922** — What kind of coffee do you drink? Effects of eight extraction methods.
    *Food Res Int* (2018). doi:10.1016/j.foodres.2018.10.022

*Literature retrieved via PubMed.*

---

## 9. Data files

- `comparator_matrix.csv` — 840-row tidy matrix: chill × atmosphere × marker × hold time, with
  median and 5–95 % credible retention.
- `kinetic_parameters.csv` — every rate constant, Ea, φ_O₂ and partition coefficient, each with
  its provenance string marking literature-anchored vs engineering estimate.
- `sensitivity_decomposition.csv` — variance shares for all three decision framings.
- `pathway_ranking.csv` — control-regime classification and marginal gains per pathway.
- `colloid_stability.csv` — Stokes velocities, traverse times and Péclet numbers.
