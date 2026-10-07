# What paper is in this work?

## The short answer

**There is one paper here, and it is not the paper the project set out to write.**

The project began as "ultrasonic dispersion is an equal or better substitute for hand
whisking." That framing produces a weak paper — a method comparison in a niche beverage,
with no mechanism and an easy reviewer objection ("so buy a blender").

The paper that the work actually supports is stronger, more general, and has a genuinely
surprising negative result at its centre:

> **Matcha is not an extraction problem. It is a suspension-delivery problem — and the
> particle size that makes matcha matcha is exactly what removes the extraction headroom
> that ultrasound-assisted extraction normally exploits.**

That reframe is the contribution. Everything else in the corpus is either evidence for it,
a bound on it, or an operational appendix.

**Working title:** *Milling has already done the work: why ultrasound-assisted extraction
does not apply to matcha, and what cavitation is actually for*

**Target:** a food-engineering or food-physics venue — *Journal of Food Engineering*,
*Food Hydrocolloids*, *Ultrasonics Sonochemistry*, *Innovative Food Science & Emerging
Technologies*. **Not** a sensory or hospitality venue; the physics is the contribution.

---

## Why this framing and not the alternatives

Three candidate papers exist in the corpus. Only one is a paper.

| Candidate | Verdict |
|---|---|
| "Sonication vs. whisking for matcha" | **Not publishable as a unit.** A two-method comparison with no mechanism. A reviewer asks why not a blender, and the honest answer (a rotor-stator does equally well on dispersion) undermines the framing. |
| "A batching workflow for café matcha service" | **Real, but a trade piece.** Every number rests on assumed CVs and task times. Belongs in a specialty-coffee trade publication or as a separate applications note — not a peer-reviewed paper, and not mixed into one. |
| **"Matcha is a suspension problem, not an extraction problem"** | **The paper.** Generalizable mechanism, a counter-intuitive negative result, a quantitative criterion others can apply to any milled botanical, and a testable consequence for product quality. |

The instinct to keep the workflow material in is the thing to resist. It is the weakest
evidence in the corpus (four claims resting on assumed inputs) attached to the strongest
physics, and reviewers grade a mixed paper at the level of its weakest section.

---

## The figure arc

Six figures exist. Five belong in the paper, in this order, and one does not.

**Fig 1 — The diffusion argument (the hook).**
Equilibration time versus particle diameter, spanning matcha (5–10 µm, ~0.07 s) to whole
leaf (0.5–1 mm, ~25 min), with the UAE literature's operating band marked. One panel, one
log-log line, two annotated points. This is the whole paper in one image: the reader sees
immediately that milling has already collapsed the timescale UAE exists to shorten.

*Currently this content is buried in a supporting panel. It must be promoted to Fig 1 and
given the full width.*

**Fig 2 — Applied stress versus cohesive strength (the mechanism).**
The Rumpf strength distribution with whisk / blender / rotor-stator / cavitation thresholds
overlaid, and survival fractions annotated. This is where the paper stops being negative and
becomes constructive: it identifies deagglomeration as the operative mechanism and shows why
whisking is marginal at it (22 Pa against a 64 Pa median — the tool sits *inside* the
strength distribution).

**Fig 3 — Why survivors matter (the consequence, and the most arresting asset).**
Oversize solids per drink by method, plus settling time in the served vessel (1.4–4.7 min).
The finding that grit does not dilute away but **concentrates in the last third of the
drink** is the most quotable result in the corpus and the one a reader will remember. It
converts an abstract particle-size argument into a sensation every reader has experienced.

*Consider this for Fig 1 instead. The diffusion argument is the more fundamental claim; the
settling result is the more arresting one. If the target venue favours impact over
systematics, lead with settling and make diffusion Fig 2.*

**Fig 4 — The inverted temperature dependence (the useful asymmetry).**
Cavitation driving pressure versus temperature (1.9× stronger at 4 °C) against self-heating
by method (+17 K countertop blender, +0.14 K sonication). This is the practically important
result: sonication is strongest exactly where its alternatives are weakest.

**Fig 5 — What deagglomeration does *not* fix (the honest bound).**
Suspension over an 8 h hold: all methods converge to ~10% suspended, because a fully
dispersed 7 µm particle still clears a 200 mm column in ~11 h. Including this strengthens
the paper. It shows the authors know where their mechanism stops, and it pre-empts the
obvious over-claim.

**Fig 6 — Operational translation. → Cut, or move to a separate applications note.**
Batching, dosing, labor, CV. Every input is an estimate. It is the right content for a trade
audience and the wrong content for this paper.

---

## The three things a reviewer will attack, and what to do about them

**1. "None of this is measured."** Correct, and currently fatal. Of 25 substantive claims in
the corpus, 14 are pure calculation, 5 are literature-grounded calculation, 2 are
literature-only, 4 rest on assumed inputs, and **0 are measured.** No amount of framing fixes this — see the experimental
programme below.

**2. "Your cohesive strength model assumes van der Waals bonding only."** Matcha contains
lipids and proteins that may form stronger bridges. Note that this objection cuts *for* the
paper: stronger bonds widen sonication's margin and make whisking look worse. Say so
explicitly rather than waiting to be asked.

**3. "A rotor-stator does this too."** True, and the paper is stronger for saying it first.
The claim is about the *mechanism* (stress must exceed cohesive strength), not about
ultrasound's supremacy. Two methods clear the bar; ultrasound's distinguishing advantages are
thermal (near-zero energy input) and inverted temperature dependence, and those are Fig 4.
A paper that concedes this reads as rigorous; one that hides it reads as advocacy.

---

## The minimum experimental programme

Four experiments convert this from a modelling exercise into a paper. Ordered by necessity.

1. **Laser-diffraction PSD by preparation method** — chasen, immersion blender, rotor-stator,
   sonication, same powder, n ≥ 3. Report the full distribution and D90. **This is the
   paper's keystone.** Without it Fig 2 is a prediction and Fig 3 is a corollary of a
   prediction; with it, both become results. Nothing else on this list matters as much.
2. **Settling in the served vessel** — photograph three preparations in identical glasses at
   0/5/15 min, with top-versus-bottom TDS at each point. Grounds Fig 3's most arresting claim,
   and costs essentially nothing.
3. **TDS at equal powder, all methods, ≥3 matcha grades** — confirms the paper's central
   negative result. A null result here *is* the finding, so it must be adequately powered; an
   underpowered null proves nothing.
4. **Blind sensory panel, n = 30 triangle test, grit and astringency only** — in the actual
   serving matrix, not neat. Tests whether the measured particle-size difference is
   perceptible, which is what makes it matter.

Secondary, strengthens but not gating: hydrophone mapping of the acoustic field (grounds Fig 2's
applied-stress axis); headspace GC-MS for the volatile claim, which **must** include the
hot-then-ice-bath arm or it overstates the effect; thermocouple logging (trivial, closes Fig 4).

**Required regardless: probe tip erosion.** Mass loss plus ICP-MS for Ti/Al/V over realistic
duty cycles in an abrasive suspension. This is unmodelled throughout the corpus and a
reviewer of any food-contact ultrasound paper will ask. It is also the one open question with
a consumer-safety dimension, so it belongs in the paper as measurement, not as a caveat.

---

## Structure

- **Introduction.** UAE's success on leaf tea and botanicals; the natural inference that it
  should help matcha; the r² scaling that breaks the inference.
- **Theory.** Diffusion timescale (Fig 1); Rumpf strength versus applied stress (Fig 2);
  cavitation temperature dependence (Fig 4).
- **Methods.** PSD, TDS, settling, sensory, erosion.
- **Results.** Figs 1–5 in arc order, negative result stated plainly and early.
- **Discussion.** Matcha as suspension delivery; generalization to other milled botanicals
  (the criterion is particle size versus diffusion length, which any reader can apply);
  where the mechanism stops (Fig 5); the astringency/casein interaction.
- **Limitations.** Named explicitly: α unmeasured; van der Waals-only bonding; far-field
  acoustic estimate; single-vessel geometry.

---

## Honest assessment

**With experiments 1–4 done:** a solid, publishable paper in a good food-engineering journal.
The negative result is genuinely counter-intuitive to anyone who knows the UAE literature,
the mechanism is clean, and the generalization criterion is useful beyond matcha.

**Without them:** a well-argued modelling note at best, and reviewers will say the same
thing in different words. The corpus contains zero measurements. That is the gap, and it is
the only gap that matters right now.

**The single most valuable next action** is laser-diffraction PSD across the four
preparation methods. It is one afternoon on a borrowed instrument, and it converts the two
central figures from predictions into results.
