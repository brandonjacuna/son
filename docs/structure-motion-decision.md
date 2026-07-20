# Structure and motion, restarted

Status: governing. Decided 2026-07-20, all ten batched decisions ratified by
Brandon. This document decides structure and motion as one decision, because on
the reference primary they are one thing: the scroll-scrubbed track is the
structure. The previous run split them, and the split is what allowed the
reference vocabulary to be killed without touching the structure.

Supersedes: `docs/structure-decision.md` and `docs/motion-spec.md` wholly,
`docs/content-architecture.md` and `docs/design-language.md` in part. Each
carries its own superseded header naming what survives and what does not.

Primary input: `docs/reference-spec.md`, the extraction, all eight sections.
Companions: `docs/copy.md` (approved copy; refit scope in section 8),
`refs/notes/lemansclassic-primary-measurements.md`,
`refs/notes/mobile-measurements.md`, the Motion and Interaction Specialist
profile (Box 2355395015610), the Narrative Architect profile (Box
2355388859938), Brand Guidelines (ClickUp 2ky45bmy-15773).

## 1. The frame this was decided under

The reference sites are the point of departure. Their vocabulary is the
default, not the exception. Brand canon describes where Sŏn is today; it is not
a list of what the site is permitted to become. Where canon and the reference
vocabulary collide, canon argues on merits, per instance, and close calls go to
Brandon. Nothing is closed by rule without the door being named. The three
registers at the end of this document are the record of every door.

The funnel constraints that are real: one terminal ask, warm forwarded traffic
only, no cold or paid channel, the reader often on a phone. The exit argument
is admitted only where it is argued against a reader who arrived on a trusted
forward, never assumed.

## 2. The decision

The site is a single continuous scrub-led track: one URL, one scroll, a run of
full-viewport panels grouped into three ground chapters and a coda, where
travel is scrubbed and text is timed, the reference primary's exact two-system
split.

- Grounds swap hard at moving panel edges as the next panel scrolls in, the
  reference's boundary mechanism, and the only transition the closed palette
  permits. Canon and the reference vocabulary agree here.
- One layer holds still while everything travels past it: a persistent,
  low-opacity 선 on the dark grounds, rate zero against the page's rate one.
  The reference's "layers travel at different rates" at its rationed extreme,
  and it argues the thesis: the site about the thing that does not walk out
  the door ends with the page arriving at the one thing that never moved.
- The daypart band is the site's one bounded pin-and-scrub: the reader drags
  the day across the fixed footprint at their own pace. This reinstates the
  Motion profile's own worked example 5 over the rule that overruled it.
- Nothing simply appears: every element enters by rising out of a clip, timed,
  staggered.
- The axis is vertical. Scrub-led-ness is the deep property of the reference;
  the horizontal wheel-remap is only how it expresses that property on a
  mouse. On the phone, where this reader mostly is, the reference itself
  throws the horizontal track away (measured) and its scrub grammar dies with
  the axis. The vertical track is the one axis on which the full scrub
  vocabulary survives touch intact. Horizontality survives in exactly one
  place: the band, where the day moves across a fixed footprint on an axis
  the page otherwise does not use, which makes the rupture stronger, not
  weaker.

This is not v3 with parallax added. V3 is a document whose sections fade in on
arrival; motion is emphasis on a static page. This is a track traveled
through, where traversal is the medium.

## 3. Structure: three chapters and a coda

The belief ladder holds in its locked order: orient and open, moat,
opportunity, team, model, ask, close. The ground arc already in the system is
a day, so the chapters come from it.

| Panel | Chapter | Ground | Content |
| --- | --- | --- | --- |
| P1 | I | Plum Ink | Hero: display sentence rises line by line, lock-up low right, A1 chrome |
| P2 | I | Plum Ink | Moat, story one: the Renata world |
| P3 | I | Plum Ink | Moat, the departure: sparse panel, active Ma |
| P4 | I | Plum Ink | Moat, story two: the owners, the room that forgot |
| P5 | I | Plum Ink | Pull-line alone, full viewport, Display |
| P6 | I | Plum Ink | Blockquote, the three compounds, the close |
| — | | | Hard swap at the edge: Plum Ink scrolls off, Bone scrolls on. The tonal hinge, felt as travel |
| P7 | II | Bone | Opportunity: headline, 선 punctuation field |
| P8 | II | Parchment | Team: two founder blocks, headshots fade only |
| P9 | II | Bone | Model: headline, the band pin, release into body and A2 |
| — | | | Hard swap |
| P10 | III | Aubergine | The ask: headline, form on Bone card. Feedback register only |
| — | | | Hard swap |
| P11 | Coda | Plum Ink | Footer: the page arrives at the still 선. Lock-up, location, the bare glyph is the layer itself |

Panelization locked 2026-07-20: five-panel moat as tabled, strophe breaks
approved on the exact approved copy, words unchanged. P3, the departure, is
two sentences alone on the emptiest panel of the site; the reader scrolls
through the space she left. Active Ma doing narrative work: the emptiness is
the event.

Chapter waypoints: cut. Decision 6 reversed on examination, 2026-07-20. The
waypoint was carried from the reference, where the persistent marker orients
across twelve routed chapters whose position is otherwise invisible. Under
our conditions it fails the removal test: three chapters are announced by the
hard ground swaps, the loudest visual events on the page; the section
eyebrows carry fine-grain naming; A1 carries wayfinding. Remove the waypoint
and nothing is lost. It would have been a third naming layer and a fourth
element on the site's quietest surface. The chrome stays at three elements:
wordmark, access note, A1. The door is named: waypoints reopen if the chapter
count ever grows.

Recorded alongside the reversal, per Brandon: this is the reframe working in
the direction that matters. The reframe was never "adopt more from the
reference." It was "let the reference argue, then decide." A carried feature
examined under our own conditions and closed is as much a success as an
admission.

Routes: one URL plus the post-submit confirmation state. The reference's
chapters are self-contained episodes, so its deep links land somewhere whole.
Our beats are dependent rungs; a link into rung four delivers a claim standing
on beliefs rungs one through three never installed. The forwarding unit is the
whole argument.

Arrival: auto-arrival state. Roughly a second of Plum Ink with the wordmark
while fonts and first-chapter assets load, then the hero choreography begins.
No click, no gate. Display choreography must never fire on unloaded fonts;
the arrival state is the guarantee. A click gate was considered and declined:
it adds friction to the most valuable inbound to buy a threshold the grounds
already carry.

Conversion affordances unchanged: A1 header jump for the already-convinced,
A2 the single earned inline pointer at belief completion, A3 the terminal
form. Nothing else.

## 4. Motion model

Three registers, governed separately per the canon amendment in section 5.

### Travel (scrubbed)

- Scroll driver: Lenis, lerp 0.10, easeOutExpo wheel smoothing, syncTouch
  false so touch stays native and is only smoothed. The reference's exact
  configuration. This is the build's one new JS dependency; Dominic inherits
  it, noted in section 9.
- Ground swaps: hard cuts at panel edges, keyed to scroll position. Never a
  dissolve.
- The still 선: fixed, rate zero, present on the dark grounds (Plum Ink,
  Aubergine), absent in daylight, revealed at the coda as the bare closing
  glyph at full opacity. Build gate, per Brandon: it must never read as a
  watermark. Stillness must be established by travel: the layer is revealed by
  content and ground edges moving across it, and at least one panel edge
  visibly wipes across the glyph while the glyph holds. If it sits fully
  inside one panel like a background image, the gesture has failed. This
  specific behavior is shown to Brandon at build before anything else layers
  on it.
- The band pin: bounded, roughly 150vh of scroll distance on desktop. The
  panel holds while the four stripes build left to right keyed to scroll
  progress, labels landing per stripe, then releases into normal travel. The
  pin length is measured against real content so it cannot read as a page
  end. Mobile: no hard pin; the stacked band builds top to bottom, scrub-keyed
  as it passes through the viewport; the column form does the pin's work.
- No other pin, no other scrubbed set piece. The pin's singularity is its
  value, exactly as the band's chromatic singularity is.

### Text (timed)

- Nothing simply appears. Every element enters by rising out of a clip.
- Blocks: 500ms, ease-out-cubic on transform, linear on opacity.
- Lines: 260ms rise from 120% behind the clip, 80ms sibling stagger.
- Fires once as the panel becomes active (roughly 85% viewport), never
  re-fires. Headshots fade only, no rise, no scale.
- These are the reference's measured values adopted as starting points, tuned
  at build with fresh eyes, not imported as law.

### Feedback

Unchanged, governed by Brand Guidelines page 12: duration tokens 100/200/400ms
and the standard eases. Header hide on scroll (~300ms). Focus ring, the single
2px exception. Confirmation cross-fade 200ms, functional, not congratulatory.

### Boundaries, confirmed by Brandon

- Narrative motion never touches the ask. Conversion surfaces are feedback
  register only.
- Reduced motion is a designed second path: the pin never engages and the band
  renders complete, the still 선 is simply present, clip-rises become
  opacity-only, hard cuts remain because a cut is not motion. Every claim is
  fully legible static.

### Performance floor

Transform and opacity only. will-change scoped to the animation window and
cleared. Frame rate verified on a real phone, not the build machine. Fonts
loaded before choreography, guaranteed by the arrival state.

## 5. Canon amendment: two motion registers

Confirmed by Brandon 2026-07-20 as a canon amendment, not a build decision.
The following is written to be lifted into the Brand Guidelines verbatim;
Brandon carries it there.

> **Amendment — Motion registers** (2026-07-20, confirmed by Brandon
> Acuña-Cardona).
>
> Digital motion at Sŏn runs in two registers, governed separately.
>
> The feedback register marks state change: hover, focus, active, loading,
> confirmation, error, and chrome behavior. It is governed by Section 12's
> interaction principles: motion marks state change, not importance; duration
> tokens motion.duration.fast 100ms, motion.duration.standard 200ms,
> motion.duration.slow 400ms; motion as emphasis is prohibited in this
> register.
>
> The narrative register carries an argument over time: scroll choreography,
> reveal and travel, sequencing and stagger. It is governed by the Motion and
> Interaction Specialist profile's earn test, applied per beat: the motion
> must carry load that nothing static carries, or it does not ship. Narrative
> motion is permitted where it passes that test, including scrub, bounded
> pin, and layered travel. It is never applied to conversion surfaces, which
> remain in the feedback register.
>
> Section 12's sentence "motion marks state change, not importance" governs
> the feedback register and the component library. It is not a prohibition on
> the narrative register. Reading it as a blanket ban is incorrect: the
> narrative register has its own governing test, and the team's commissioning
> of a narrative motion discipline is incoherent under the blanket reading.
>
> Both registers honor prefers-reduced-motion as a designed path, not a kill
> switch: the feedback register per Section 12's token override; the
> narrative register with a designed second choreography in which nothing
> pins, travel-coupled motion is removed, and every claim remains legible
> static.

## 6. What carries from the reference and what does not

Every item argued on mechanics. Canon appears only where it was the deciding
argument, and those cases are in section 7.

Carries:

1. **Scrub-led travel.** Reader-paced, reversible, physical. A belief ladder
   benefits from reader pacing: a reader who wants rung two again scrubs back
   and the world runs backwards with them. Translated to the vertical axis,
   where it survives touch.
2. **The two-system split, scrub for travel and timed for text.** Verbatim.
   Text must finish (a half-scrubbed sentence is unreadable); travel must not
   (reader pacing is the point).
3. **Layers at different rates.** As rate zero against rate one: the still 선
   against the traveling page. One depth contrast, rationed.
4. **Nothing simply appears.** Global entrance rule, clip-rises throughout.
5. **Hard ground swaps at moving panel edges.** The closed palette and the
   reference converge on the same mechanism.
6. **Chapter structure.** Three plus a coda, from the ground arc. Chapter
   count follows the argument, not the reference's twelve.
7. **Display sized to content, not the frame.** For the non-reading 선
   layers: architectural scale, allowed to exceed the viewport, held near
   full size on mobile and cropped rather than shrunk (the reference's
   measured mobile stance). Reading type stays contained; a cropped word
   loses the argument, which is comprehension, not canon.
8. **Lenis smoothing, lerp 0.10, easeOutExpo, syncTouch false.** Earned now:
   there is scrub to smooth, which flips v3's own native-scroll argument.
9. **Header hide on scroll.** Feedback register.
10. **Ratio-held mobile type ramp; single-weight size-only ramp.** Already
    ours; the reference validates both stances.
11. **A persistent chapter marker.** Initially adopted as the current-chapter
    eyebrow in the header (decision 6), then reversed on examination: on
    three chapters it fails the removal test. See section 3.

Does not carry:

1. **The horizontal axis and wheel remap.** The reference pays for
   horizontality twice: a second vertical layout below 768px, on which the
   scrub system dies entirely (measured). Our majority surface is that
   screen. Shipping the fallback to most readers while maintaining two
   layouts is the wrong trade for this page. Ratified as decision 1.
2. **Per-chapter gates.** A gate between self-contained episodes is a
   threshold; between dependent rungs it interrupts a dependency chain. Even
   a reader who never leaves is served worse.
3. **Twelve routes, per-chapter preloaders, deep links.** Fragment-forwarding
   strips the ladder. One route.
4. **The chapter takeover.** The closed palette has no accent to flood on
   dark grounds, and a full-frame takeover is the one move whose measured
   failure, reading as the end of the page, attacks a terminal-ask page
   directly. The scrubbed hard swap carries the boundary.
5. **Custom cursor** (secondary). Measured inert on touch; no pointer task.
6. **Autonomous time-based hero object** (secondaries). Its own author drops
   it on mobile (measured, zero canvases). Transposed into canon material as
   the still 선, which needs no time base because its meaning is that it does
   not run.
7. **Conversion density** (secondaries). Solves a cold-traffic problem this
   funnel does not have. Reopens if a cold, paid, or search channel is ever
   added.
8. **Mono label face, weight ramps** (secondaries). Face-limit canon; and the
   primary, the site nearest our register, takes our side of the axis anyway.

## 7. Canon collisions, and who won each

1. **Page 12 motion rule vs. the scrub-led model.** Resolved by scoping: two
   registers, the amendment in section 5. Confirmed as canon.
2. **Closed palette vs. takeover flood.** Canon wins; mechanics agree. Cost:
   no boundary spectacle.
3. **Sentence case vs. monumental uppercase display.** Canon wins. Cost: the
   reference's masthead voice; presence carried by 선 scale and choreography.
4. **Display ceiling vs. content-sized type.** Split: reading type capped
   (comprehension closes it before canon does); non-reading 선 exceeds the
   frame (sanctioned texture).
5. **Two-Latin-face limit vs. mono waypoints.** Canon wins. Eyebrow carries
   waypoints.
6. **"No forced sequences" vs. an entry gate.** Avoided: the auto-arrival
   state routes nobody through anything. The click gate was declined.
7. **선 depth system vs. the persistent still layer.** Extension admitted:
   solo-선-as-material was established; persistence across the dark grounds
   is new, adopted with the not-a-watermark build gate.

## 8. What this costs the copy

No belief moves. No sentence-level rewrite is forced. The costs:

- **The moat re-lineates.** The approved words break into panel strophes;
  breaks are choreography units and are shown to Brandon before build
  (approved in principle, decision 9).
- **The pull-line gains a panel of its own.** Promotion in isolation, not in
  type step. No word changes.
- **New copy: none.** Chapter labels were cut with the waypoints (decision 6
  reversed). No arrival-state line; the arrival is the wordmark.
- **The traversal is never named in copy.** A line explaining the day would
  be performed conviction; the grounds already say it.
- The hero's two-step split (Display + Headline) survives as-is and becomes
  the choreography's first gesture.

Wording delta under five percent. Belief delta zero.

## 9. Build notes and inherited dependencies

- **Lenis** (smooth scroll, scrub driver) is the build's one new JS
  dependency. Dominic inherits it. Version pinned at build; the reference
  runs 1.3.8.
- **The still 선 build gate:** the not-a-watermark demonstration (section 4)
  is shown to Brandon before further layering.
- **Arrival state** doubles as the font/asset preloader; choreography never
  fires on unloaded fonts.
- **Verification:** real phone, reduced playback, fresh eyes on a later day,
  per the Motion profile. WCAG checks in browser, not the design file.

## 10. The hero bleed door, re-examined and closed

Recorded per decision 8: the cropped-wordmark bleed was re-examined under the
new frame, because the hero's job changed (it now also teaches the motion
vocabulary), and it was closed again on merits, not by inheritance. The
mark-integrity argument is mechanical and survives the new structure: cropping
the lock-up severs 선, and the Latin-alone form drops 선 from the opening
while doubling the mark. The door remains named and reopens only if the mark
spec itself is ever amended.

## 11. Session registers

### Excluded by canon

- Monumental uppercase display. Rule: sentence case. Would have bought: the
  reference's masthead voice.
- Accent-flood chapter takeover. Rule: closed palette, no chroma on dark
  grounds (mechanics concurring). Would have bought: the boundary spectacle.
- Ground dissolves at chapter edges. Rule: no tints, no shades. Would have
  bought: cinematic hinges. Cost near nil; the reference hard-cuts anyway.
- Mono waypoint face. Rule: two-Latin-face limit. Would have bought: matte's
  editorial index device.
- Cropped hero wordmark bleed. Rule: the mark's drawn-balance spec. Would
  have bought: a monumental cropped hero mark. Re-examined this session,
  closed on merits (section 10).

### Excluded by judgment

Each argued against a warm, forwarded reader; none closed silently.

- Horizontal axis and wheel remap. Reason: the fallback would ship to the
  majority surface at the cost of a second layout. Ratified by Brandon.
- Per-chapter gates and routes. Reason: dependency-chain mechanics, not leak
  fear.
- Twelve-chapter granularity. Reason: chapter count follows the argument.
- Click-gated arrival. Reason: friction on the most valuable inbound for a
  threshold the grounds already carry. Ratified by Brandon.
- Custom cursor. Reason: measured dead on the majority surface.
- Autonomous time-based hero object. Reason: dropped on mobile by its own
  author; transposed to the still 선.
- Conversion density. Reason: cold-traffic solution without cold traffic.
  Reopens with any cold channel.
- Naming the day-traversal in copy. Reason: performed conviction.
- A second pin anywhere (including the moat pull-line). Reason: the pin's
  singularity is its value.
- Chapter waypoints in the header (decision 6, reversed on examination).
  Reason: on three chapters the marker fails the removal test; the ground
  swaps, eyebrows, and A1 already carry orientation, naming, and wayfinding.
  Door named: reopens if the chapter count grows.

### Reconsidered, admitted

- Scrub as the leading motion model. Form: travel scrubbed, text timed,
  feedback untouched. The central admission.
- Smooth scroll. Form: Lenis, lerp 0.10, syncTouch false. Earned because
  there is now scrub to smooth.
- Pin and scrub on the daypart band. Form: bounded ~150vh, reader-paced,
  reduced-motion static. Reinstates the Motion profile's example 5 over the
  spec that overruled it.
- Parallax and layered travel. Form: one still layer at rate zero against
  the traveling page.
- Chapter structure. Form: three ground chapters plus coda, no gates.
- Content-sized viewport-exceeding type. Form: non-reading 선 only.
- Clip-rise entrances everywhere. Form: nothing simply appears.
- An arrival moment. Form: auto-arrival state, no click.
- The persistent still 선. Form: dark grounds only, revealed at the coda as
  the bare glyph, with the not-a-watermark build gate.

## 12. Open items

1. Canon amendment: Brandon carries section 5 into the Brand Guidelines.
2. Type re-examination session precedes build: the prior scale was set with
   no reference input, and the new structure creates type conditions that
   did not exist when it was set (viewport-isolated display panels,
   clip-rise entrances, the architectural 선).
3. Build sessions follow. First deliverable of the first build session: the
   still-선 not-a-watermark demonstration (section 4), shown to Brandon
   before anything else layers on it. The v3 site at tag `v3-fallback`
   remains the working fallback and is not extended.
