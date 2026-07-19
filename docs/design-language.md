# Design language

What carries the Sŏn investor site when type, color, and motion are the only
instruments. No photography beyond two founder headshots, no imagery, a closed
eight-color palette, no new values. This document settles the two open hero
decisions, the ground system across the seven slots, the 선 as a graphic
element, and the one graphic rupture. Motion has its own document,
`docs/motion-spec.md`; the two were written together and share the session
registers, which live in full at the end of this file.

Companion inputs: `docs/structure-decision.md` (the funnel, locked),
`docs/content-architecture.md` (the build-ready structure and both canon
registers), `docs/copy.md` (approved, unchanged), the Brand Guidelines
(ClickUp 2ky45bmy-15773), and the rebuilt type system in `tokens/`.

The organizing idea is Ma (여백의 미): empty is a specification, not a default.
It governs space here and, through the motion spec, time. What is not there is
chosen. Type is the argument, color is the day, motion is restraint with a
single rupture.

## The two hero decisions

### The bleed element: none in the hero

The bottom-crop treatment stays in the system, unspent. The hero does not use
it. This re-closes a door content-architecture had reopened for the hero, and
it is closed by proof, not preference.

A bleed is a bottom crop, and the hero's only crop-worthy mass is its identity
element. Cropping it fails both available ways:

- Crop the full Sŏn / 선 lock-up and the crop severs 선, which sits
  centered-below and is therefore what runs off the bottom. That breaks the
  page-04 drawn-balance spec. Forbidden.
- Crop the Latin "Sŏn" alone and 선 is absent from the first viewport. A Korean
  room that does not show its Korean mark in the opening loses the one signal
  the hero exists to plant, and it puts the mark twice.

The signature-word alternative, now testable against copy, fails on three
counts. Sized to presence it would exceed the display ceiling and become the
largest voice, demoting the display sentence that carries the site. A word not
in the approved copy is added copy; a word pulled from the copy reads
ambiguously alone; a giant thesis-word is performed conviction. So the hero's
presence is carried the way the brand asks: the display sentence, a contained
oversized Sŏn / 선 lock-up with 선 intact, and specified Ma. The reopening was
justified on funnel mechanics (a bottom crop pulls toward the fold); mark
integrity and the largest-voice rule outrank that here.

### The hero baseline: diagonal, not horizon; the freed low-left is active Ma

Cutting the location tag did not remove a horizon the hero needs. It removed a
redundant third point and clarified the composition already present: display
sentence upper-left, lock-up lower-right, a diagonal.

- The header chrome already carries a horizon at the top (Sŏn wordmark left,
  the access note and A1 right). A second horizon at the bottom would bracket
  the hero as a closed box, a floor, a mild illusion of completeness at the
  exact place the page must pull downward.
- The freed low-left is specified as active Ma, not left empty. Isolation is
  what gives the lock-up its weight; an open bottom-left is the eye's exit into
  the moat.
- The lock-up sits on the 10% page margin (`--son-margin-page`), its
  concentrated mass counterweighting the dispersed mass of the multi-line
  sentence across the diagonal.

Net: top horizon (chrome), diagonal descent (sentence to mark), specified void
(low-left) that the eye falls through into the scroll. The pre-lease constraint
that forced the tag cut improved the hero's downward pull. Nothing is placed in
the low-left, so the bleed-in-the-convenient-corner path is not taken, and it
is moot in any case now that there is no bleed element.

### Hero typography: orientation at Display, loop-opener at Headline

The hero display block is two sentences and splits into two steps. The split's
shape is orientation larger, loop-opener one step down. Words are unchanged;
only the type step is assigned.

- Orientation, "One Korean room in Austin, Texas, open from first light to last
  call." Type: Display (48 / 96 / 104).
- Loop-opener, "We build for the second visit, not the first." Type: Headline
  (40 / 57 / 60), one step under Display, still GT Sectra Display Regular.

Orientation takes Display. The moat rule is not "belief beats vehicle in size."
It is that the belief takes Display at its install point, where it lands as a
payoff after its vehicle. The moat pull-line is Display because it crystallizes
the belief after the Renata story, last and isolated, so hierarchy and reading
order agree. The hero is not the belief's install point; it is the loop's open.
The memory belief installs at full voice in the moat. Content-architecture
fixes exactly two Display moments on the site, the hero and the moat pull-line,
holding the blockquote to Headline so those two stay the largest. Promoting the
hero loop-opener to Display would create a third Display moment, state the
memory belief at top voice twice (seed and install), and spend the moat's
payoff before the moat. Orientation takes the hero's Display because it is the
hero's own irreplaceable job, locating the reader, and because it makes the two
Display moments complementary, WHAT (identity) and WHY (thesis), instead of
redundant.

This does not invert the moat rule, it completes it. Reserving the belief's
single Display moment for the moat is the rule applied across the page. Reading
order agrees: orientation is the known the antithesis requires, so it must be
first and largest; a Display antithesis above a subordinate orientation would
land before the reader knows the room or the city. Orientation is also not a
spent vehicle the way the Renata story is; it is standing context every later
section leans on, a foundation laid first and firm.

The loop-opener sits at Headline, not Subhead. Subhead is three steps down and
leaves the Display optical into GT Sectra Standard, the structural face, which
drops the site's one antithesis into a supporting register. Headline keeps it
in the felt Display face, one step down, 40 against 48 on mobile, a 1.2x
adjacency, and it matches the moat's blockquote (also Headline), so both dark
narrative sections run the same two-tier logic, a Display crystallization over
a Headline second voice.

## The ground arc across the four color states

Four grounds run across the seven slots. Read down, they make a day, and the
day is the argument's structure.

| Slot | Ground | State | Role |
| --- | --- | --- | --- |
| Hero | Plum Ink | dark, cold | the dinner register, the anchor, the frame opens |
| Moat | Plum Ink | dark, cold | sustained; the felt interior deepens without a ground change |
| Opportunity | Bone | light | step into daylight, the market argued |
| Team | Parchment | light, warm | the human proof, warmed one notch |
| Model | Bone | light | back to cool for the economic proof |
| Ask | Aubergine | dark, warm | the commit, a different dark |
| Footer | Plum Ink | dark, cold | home, the frame closes |

Dark bookends carry feeling, the moat at the front and the ask and close at the
back. The daylight center carries proof: market, people, model. Two deliberate
moves inside it:

- The moat holds Plum Ink from the hero. The two darkest, most-felt beats share
  a ground so the moat reads as the hero deepening, not a new place. This is
  Jeong made literal, the accumulated thing that does not reset.
- The two darks are not the same dark. The ask is Aubergine, the warm
  late-night register, not Plum Ink, so the return to dark for the commit is a
  new dark, not a loop to the start. The footer then returns to true Plum Ink,
  home. Cold-dark open, daylight, warm-dark commit, cold-dark close.

Chroma is rationed to daylight. On the dark grounds the palette is monochrome,
cream on near-black, no accent (dinner's explicit "no chroma," Jade a named
failure mode). Chroma appears only on the light grounds and only as the
secondary voice: Peacock on Bone, Onggi on Parchment. Even the accents tell the
daypart story quietly, peacock the morning green, onggi the lunch clay.

Transitions are hard cuts, never dissolves. A cross-fade between two palette
colors renders a transient blend that is not in the closed palette, so it is
out on "no tints, no shades." The one boundary that matters, moat to
opportunity, Plum Ink to Bone, dark to daylight, is the site's tonal hinge and
it is a cut on purpose: a dissolve would soften a moment that should feel like
stepping outside. Motion never morphs a ground; the new section's content
settling in is what registers the arrival.

## The 선 as a graphic element: one system, three depths

The three recorded uses cohere under one variable, depth, and one rule.

- Signature, foreground, mark scale, full opacity, always with Sŏn: the
  lock-up. This is the mark, protected by the balance spec, never cropped.
- Atmosphere, background, architectural scale, low opacity, never with Sŏn: the
  oversized 선 behind the moat text. This is the site's only texture, the
  brand's own glyph enlarged and dimmed, which is the only Jaeyeonmi-honest way
  to get tonal depth on a photo-less dark ground. Not grain, not noise, not
  pattern.
- Punctuation, midground, architectural scale, full opacity in a color field,
  never with Sŏn: the accent split on the opportunity.

The rule that makes them one system and protects the mark: 선 appears with Sŏn
only in the lock-up; everywhere else it stands alone. Solo-선 is the glyph as
material, lock-up-선 is the mark as signature, and the reader learns the
distinction, so mark integrity is never at risk from the large solo instances.
Rationing rule: at most one 선 event per section.

The accent split sits close to "선 as decoration," which page 03 resists (선
prohibited as a pattern element). It earns through because it is a single
semantic instance carrying the opportunity's claim, the Korean mark planted at
the intersection the headline names, not a tiled or ornamental fill. If it were
merely a green panel with a glyph, it would fail. It passes on meaning, and its
reveal is choreographed to enact the meaning (see the motion spec).

## The daypart band: the one strong rupture

The band is the only saturated, hard-edged, full-palette moment on the site,
and the only place Jade appears at all (Jade is otherwise a dinner failure
mode; here it is legitimately Coffee, morning). Everywhere else color is
rationed; the band spends the whole palette at once. Its singularity is the
value, so the governing rule is absolute: the band appears exactly once, and
nothing else on the site uses saturated color blocking.

Four stripes, descriptive labels only, never the internal code names: Coffee on
jade, Lunch on onggi, Dinner on plum ink, Late night on aubergine, spanning
from "First light" on the left to "Last call" on the right.

What it costs the sections around it, named so the cost is chosen:

- The model, which holds it. The band is strong enough to dominate, so the
  model is the one section where type is not the primary instrument. The
  headline "One footprint. Four dayparts. One set of fixed costs." reads first,
  at the top; the band is the proof below it; the band is the site's only
  image. Type yields, once, on purpose.
- The team before it. Headshots into a saturated band would stack the two
  highest-texture beats. The team sits before the model for this reason, and
  the model opening on quiet Bone with the headline gives a cushion, so the
  band never lands directly off the founders' faces.
- The ask after it. The band's rightmost stripe is Late night, Aubergine, and
  two beats later the ask ground is Aubergine. The "Last call" label points
  where the reader is going. The rupture foreshadows the commit rather than
  fighting it.

## Session registers

Kept live from the start of the session, not reconstructed at the end. These
extend, and do not repeat, the registers already recorded in
`docs/content-architecture.md`. Motion entries are marked; they are also
referenced in `docs/motion-spec.md`.

### Excluded by canon

- Cropped Latin wordmark as the hero bleed. Closed by: 선-integrity (cropping
  the lock-up severs 선; the Latin-alone form drops 선 from the opening) and
  mark redundancy. Would have bought: a monumental cropped hero mark in the
  reference primary's register. Cost: no cropped-type spectacle in the hero.
- Cropped signature word as the hero bleed. Closed by: the largest-voice rule
  (it would demote the display sentence), copy discipline (a new word is added
  copy; a copy word reads ambiguously alone), and "no performed conviction."
  Would have bought: a bold one-word hero enacting the spine, memory and
  return. Cost: none beyond forgoing the boldness; the spine is carried by the
  loop-opener.
- Splitting the lock-up across the hero's bottom row, Latin left and 선 right,
  to rebuild the horizon from the mark's halves. Closed by: the mark spec,
  "centered-below," "not right-adjacent," the drawn balance. Would have bought:
  a mark-native horizon embodying "one Korean room." Cost: the horizon is
  rebuilt as top-chrome plus diagonal.
- Ground cross-fade on section transitions. Closed by: the closed palette, "no
  tints, no shades." Would have bought: cinematic tonal dissolves, especially
  at the dark-to-light hinge. Cost: hard cuts.
- Ambient drift on the oversized 선 (motion). Closed by: "motion marks state
  change, not importance," the earn test (no argument carried), and vestibular
  caution over large-area movement. Would have bought: a whisper of life on the
  photo-less dark moat, the sanctioned echo of the excluded living-hero-object.
  Cost: nil, arguably a gain, since a still 선 is the memory that stays.
- Scrubbing the daypart band to scroll (motion), the Motion profile's own
  stated ideal for a change-over-time sequence. Closed by: the no-pin, no-scrub
  frame; a scrubbed band pins the section and reads as a page end. Would have
  bought: reader-paced control of the one transformation. Cost: the band is a
  triggered wipe, no pin.
- Smooth-scroll, inertia, snap (motion). Closed by: scroll is the reader's
  control surface, and we have no scrub to smooth. Would have bought: the
  reference's eased scroll feel. Cost: none for us; native scroll is more
  responsive on a phone and cannot lag.
- Parallax on the 선 or the lock-up (motion). Closed by: vestibular trigger
  plus not being scrub-led. Would have bought: depth on a flat page. Cost:
  depth comes from type scale and the 선 depth system instead.
- Chapter takeover or masthead wipe (motion), the reference's accent-color
  boundary spectacle. Closed by: no takeover (it reads as a page end), no
  monumental display, and the closed palette (no accent flood). Would have
  bought: an immersive chapter-boundary moment. Cost: our boundaries are quiet
  cuts plus content settle.

### Reconsidered, admitted in a disciplined form

- The daypart band as a roughly one-second choreographed wipe, the site's one
  noticeable motion (motion). Reopened against site-wide near-stillness and
  "motion marks state, not importance." Admitted because the band is the single
  graphic rupture and the one beat where motion equals argument, four returns
  across one footprint read as the day sweeping a fixed space. Disciplined:
  triggered once on enter, not scrubbed, not pinned, transform and opacity
  only, reduced-motion falling back to the complete static band, which loses
  nothing since the static band already states the claim. It is the only motion
  allowed to exceed roughly 700ms or to be noticed. Its singularity protects
  it.
- The 선 accent split as a large solo glyph, despite page 03's "선 not as
  pattern element." Admitted because it is a single semantic instance carrying
  the opportunity's claim, not a tiled or decorative fill. Argument: it earns
  on meaning, not on filling space.
- Any narrative motion at all. Reopened against the Motion profile's strict
  earn test, which classes emphasis-only reveals as decoration. Admitted in the
  disciplined form the settled frame already named, restrained reveal on
  load-bearing beats, because the reveals serve the funnel and reduced-motion
  loses nothing. Stated honestly: no beat requires motion; motion is rationed
  emphasis.
