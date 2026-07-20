> **Superseded in part, 2026-07-20, by `docs/structure-motion-decision.md`.**
> The flat section layout gives way to the chapter-and-panel structure; the
> moat re-lineates into panel strophes. What remains standing reference: the
> type steps and display fit rule, the location and property constraint, the
> slot content inventory, the three affordances (A1, A2, A3), and both canon
> registers recorded here.

# Content architecture

The build-ready structure for the Sŏn investor site. It expresses the seven
locked slots from `docs/structure-decision.md` as layout: section order, what
each section holds, which type step carries each element, which ground it sits
on, and where the three conversion affordances land. It is structure and
hierarchy, not copy. No sentences here are copy, and none should be read as a
draft of copy. Word budgets from the structure decision appear only as
constraints the layout must accommodate.

Companion inputs: `docs/structure-decision.md` (the funnel and slot map, locked),
`docs/reference-spec.md` (the extraction), and the rebuilt type system in
`tokens/typography.css` and `tokens/fonts.css`.

## Register and grounds

The site runs the dinner register throughout. Grounds alternate by section on the
closed eight-color palette, resolved through the semantic themes in
`tokens/colors.css`: Plum Ink and Aubergine on `[data-theme="dinner"]`, Parchment
on `[data-theme="dosi"]`, and Bone on the base editorial theme. The one place
other daypart colors appear is the model band, where they are a graphic, not a
theme switch for running text.

## Location and property constraint

Standing rule, governs every external surface. Sŏn is pre-lease and unsigned.
Until the lease is executed, no external surface names the address, the
neighborhood, or any property identifier. The site says Austin, Texas, and
nothing more precise. This binds the hero display line, the location tag, the
footer location line, and the footer mark, and any surface added later.

This is not a copy preference, it is a legal and factual constraint. The
property is not secured, so naming it is a claim the venture cannot yet stand
behind. The constraint was set at P3 and the surfaces drifted from it, which is
how St. Elmo and South Austin sat unchecked in the copy until this sweep. When
the lease is signed, this is the first door to reopen, and the neighborhood
returns as orientation. Internal brand records, the guidelines deck and the
design-system readme, may hold the true address. The constraint is external
surfaces only.

## The type steps this architecture references

Defined in `tokens/typography.css`. Sizes are px at 375 / 1280 / cap.

| Step | Token | Face, optical, weight | 375 / 1280 / cap |
| --- | --- | --- | --- |
| Display | `--son-text-display` | GT Sectra Display, Regular 400 | 48 / 96 / 104 |
| Headline | `--son-text-headline` | GT Sectra Display, Regular 400 | 40 / 57 / 60 |
| Section | `--son-text-section` | GT Sectra Display, Medium 500 | 30 / 42 / 44 |
| Subhead | `--son-text-subhead` | GT Sectra (Standard), Regular 400 | 21 / 25 / 26 |
| Lead | `--son-text-lead` | GT Alpina Fine, Light 300 | 18 fixed |
| Body | `--son-text-body` | GT Alpina Fine, Regular 400 | 16 fixed |
| Descriptor | `--son-text-menu` | GT Alpina Fine, Regular 400 | 14 fixed |
| Eyebrow | `--son-text-eyebrow` | GT Sectra (Standard), Regular 400, uppercase | 12 fixed |
| Fine | `--son-text-fine` | GT Alpina (Standard), Light 300 | 12 fixed |
| Wordmark | `--son-font-wordmark` | GT Sectra Fine Book, with 선 delivered as a drawn path (amended; definition in `tokens/typography.css`) | contextual |

On C8, recorded so it is not misread later: the display cap was resolved by
splitting Display from Headline and making the display step reach its size at
real desktop widths. That structural separation is the substance of the fix. The
104px ceiling is the smaller part of it, a reasoned number, not the point.

## Display fit rule

Two parts, and the split carries weight.

- Reading display (the hero sentence, the pull-lines, the headlines) fits and
  wraps on every axis and never overflows. A cropped word loses the argument, so
  the reading voice is always contained.
- Non-reading display (a hero wordmark, or a signature word) may crop on the
  bottom edge only. Never the left or right edge, and never the 선 mark
  silhouette. The reasoning is mechanical before it is anything else: a bottom
  crop runs the form off toward the fold and pulls the eye down, which serves a
  continuous vertical scroll with one terminal ask; a side crop implies content
  off-screen horizontally, fights the downward motion, and on a phone invites a
  horizontal swipe the site cannot honor (measured dead on the reference
  primary). The 선 exclusion is the mark's drawn balance spec (page 04, the eye
  distributes attention between 선 and Sŏn without one pulling harder), which a
  partial glyph breaks by construction. The already-sanctioned oversized 선 behind
  running text is texture at low opacity, not the mark, and is not covered.

The bottom-crop treatment sits outside the nine-step scale: its element is sized
to presence and allowed to exceed viewport height, cropping only at the bottom,
not clamped to fit. Which element bleeds is undecided; see the hero slot.

## Persistent chrome

Header, minimal, hides on scroll.

- Left: the Sŏn wordmark. Type: Wordmark, at Subhead scale.
- Right: an access note, Eyebrow, and affordance A1 (below).
- Ground: inherits the hero (Plum Ink), then transparent over what follows.

## The seven slots

### 1. Hero, orient and open

- Ground: Plum Ink. Theme: dinner.
- The display sentence, one line that says what and where and opens the loop the
  moat will close. Type: Display. This is the single largest voice on the site,
  and the one element that earns the resolved ceiling.
- Location tag, low left: cut. It carried a locator at a finer gradient than the
  display line (neighborhood beneath the line's place). The fold moved the
  location into the display line, and the location and property constraint
  forbids any gradient finer than Austin, Texas, so the tag had only Austin,
  Texas left to carry, one scale below an identical string. Nothing
  non-redundant and non-second-ask remained, so it is cut rather than filled
  with an invented line. Structural consequence, recorded not absorbed: the
  hero's bottom baseline loses its low-left anchor and the two-point horizon that
  counterweighted the low-right lock-up. Rebalancing the bottom row is a layout
  call for the structure session; the freed low-left is a candidate anchor for
  the still-open bottom-crop bleed element below.
- The Sŏn / 선 lock-up, low right. Type: Wordmark, with 선 in the Korean face at
  the optical up-scale.
- Bottom-crop bleed: available here, element undecided. The bleed treatment (per
  the display fit rule, bottom edge only) is admitted for the hero, but the
  element that bleeds is not chosen. The hero already places a Sŏn / 선 lock-up;
  an oversized cropped Latin wordmark alongside it would put the same mark in the
  first viewport twice, in two registers, which may be redundancy rather than a
  system. The signature-word alternative needs copy that does not exist yet. So
  this resolves at P5 or P6, with copy in hand, not before. Dependency, recorded
  so it is not decided by default: whoever builds the hero must not ship a cropped
  wordmark simply because the slot permits a bleed. The element is an open
  decision, not a builder's discretion.
- Carries affordance A1.
- Budget: 15 to 30 words across the display line and the nav.

### 2. Why this, the moat

- Ground: Plum Ink. Theme: dinner. The dark emotional core, the one section
  allowed to run long.
- Section eyebrow. Type: Eyebrow. See the renumbering flag below.
- The narrative body. Type: Body, set to the `--son-measure` measure.
- The pull-line, the felt load-bearer ("memory business"). Type: Display. Held to
  the same top voice as the hero because it carries equivalent weight in the
  argument.
- The centered blockquote. Type: Headline, one step below the pull-line so the
  hero and the pull-line remain the two largest moments.
- The oversized 선 behind the text. Type: the Korean glyph as a low-opacity
  ground element, color resolved by theme.
- Budget: 180 to 230 words, the longest section on the site.

### 3. The opportunity, why now

- Ground: Bone, base editorial theme, with the 선 accent split.
- Section eyebrow. Type: Eyebrow.
- The timing statement ("same curve" or "intersection"). Type: Headline.
- The key supporting line. Type: Lead. Remaining support. Type: Body.
- The right field carrying the 선 accent and its caption. Type: the Korean glyph,
  caption in Descriptor.
- Budget: 50 to 70 words.

### 4. The team, who executes

- Ground: Parchment. Theme: dosi.
- Section eyebrow. Type: Eyebrow.
- Two founder names. Type: Subhead.
- Two role labels. Type: Eyebrow.
- Two bios. Type: Body.
- Founder headshots, the only photography the site is allowed. Portrait slots.
  Captions. Type: Descriptor.
- Position: before the model, per the structure decision.
- Budget: about 110 words across two bios, plus captions.

### 5. The model, the return

- Ground: Bone, base editorial theme, carrying the daypart band.
- Section eyebrow. Type: Eyebrow.
- The economic statement ("one footprint, one set of fixed costs"). Type:
  Headline.
- The body. Type: Body. This body carries affordance A2 inline, at the
  belief-completion point.
- The daypart band, the site's one strong graphic rupture: four stripes on the
  daypart colors (Coffee on jade, Lunch on onggi, Dinner on plum ink, Late night
  on aubergine), spanning the width. Band labels, vertical. Type: Eyebrow. The
  labels are descriptive (Coffee, Lunch, Dinner, Late night). Internal code names
  never appear here, or on any external surface.
- Budget: 50 to 70 words, plus band labels.

### 6. The ask

- Ground: Aubergine. Theme: dinner.
- Section eyebrow. Type: Eyebrow.
- The centered ask headline. Type: Headline.
- Affordance A3, the terminal form, on a Bone card: full name, email, company or
  affiliation, and the free-text qualifying field. Field labels: Eyebrow. Input
  text: Body. Submit control: Descriptor.
- The securities disclaimer, inline. Type: Fine, held at 12px for the
  accessibility target, not smaller.
- The confirmation state after submit is the one separate surface, a legitimate
  exit because conversion has happened. Register is functional, not
  congratulatory (page 12). Confirmation text: Body or Lead.
- Budget: 25 to 40 words of surrounding copy; the form carries the rest.

### 7. Footer, close

- Ground: Plum Ink. Theme: dinner.
- The Sŏn / 선 lock-up. Type: Wordmark.
- The location line. Type: Descriptor.
- The closing mark. Type: Fine.
- Quiet close, no further ask.
- Budget: under 15 words.

## The three conversion affordances

- A1, the header shortcut. A persistent wayfinding jump to the ask, for the
  reader who arrives already convinced. Type: Descriptor. It is not a second ask.
  Lives in the header chrome.
- A2, the model inline soft link. A single earned inline pointer to the briefing,
  set inside the model body at the belief-completion point. Type: Body, styled as
  a link, anchored to the ask.
- A3, the terminal form. The only place the site asks. In slot 6.

Nothing else. No repeated inline prompts, no floating call-to-action bar, no FAQ,
no exit-intent. The type system is the same under all three: the affordances are
placement and behavior, not new type steps.

## Eyebrow renumbering, flagged not resolved

Folding the concept into the hero removes the standalone "01 · The concept"
eyebrow, which breaks the numbered sequence. The remaining sections either
renumber (Why this to 01, and so on) or move to semantic eyebrows with no
numbers. This is a copy-layer decision, resolved when copy is written at P4, not
here. The type step is Eyebrow under either outcome, so the type system is
agnostic to the resolution and no build value turns on it.

## Scratch, patterns discovered and deferred

Discovered during this work, not built, because this session rebuilds type only.
They belong to later sessions (structure, motion, components), not to the type
system.

- Header hide-on-scroll behavior.
- Restrained reveal motion on the load-bearing beats.
- The daypart band as a reusable graphic component.
- The oversized 선 watermark device behind running text.
- The post-submit confirmation surface as its own state.

## Reconsidered, admitted in a disciplined form

One item first logged under "excluded by canon" was reopened and reargued on
mechanics, with canon applied last, not first. It is admitted, in a disciplined
form. Kept here so the reasoning travels with the decision.

**Deliberate viewport overflow on display type.** The device is an intentional
crop: type sized to its own presence rather than to the frame, so a form runs
past an edge and the reader infers the whole from the fragment. It is orthogonal
to loudness; a crop can be quiet. The original closure ("display that shouts is a
brand failure") conflated crop with volume and is withdrawn.

The substance is the axis, and it holds on mechanics before any brand rule. A
crop on the bottom edge runs the form off toward the fold and pulls the eye down,
which serves a continuous vertical scroll with one terminal ask. A crop on the
left or right edge implies content off-screen horizontally, fights the downward
motion, and on a phone invites a horizontal swipe the site cannot honor.

Admitted: a bottom-edge crop of a non-reading display element (a hero wordmark or
a signature word), sized to presence and outside the nine-step scale, as a way to
give a photo-less hero physical presence on the device most readers arrive on.
The treatment is available; the element that bleeds is an open decision deferred
to P5 or P6 with copy in hand. See the display fit rule and the hero slot.

Still excluded, each argued not asserted:

- Overflow of the reading sentence, or any reading display. A cropped word loses
  the argument and the hero's job is to orient. Comprehension closes this, not
  canon.
- Overflow of the 선 mark silhouette. The mark carries a drawn balance spec (page
  04): the eye must distribute attention between 선 and Sŏn without one pulling
  harder, and a partial 선 pulls harder by construction. Mark integrity closes
  this. The low-opacity oversized 선 behind running text is texture, not the mark,
  and is not covered.
- Horizontal, left or right edge, overflow of any element. It fights the vertical
  funnel and invites a swipe the site cannot honor. Funnel mechanics close this.

**The one dollar figure, Dominic's assets under management.** The site keeps
every number off the surface: the raise amount, structure, and returns live in
the briefing, and the page proves everything else in words. Dominic's bio
carries the lone exception, more than three billion dollars in assets. Reopened
against that norm and admitted, because the figure is a professional credential,
not deal financials, and it is the irreducible proof of the capital partner's
credibility. For a reader weighing whether the capital side is sound, the scale
of assets his team is trusted with is the proof, and no adjective substitutes
for it. Admitted in disciplined form: attributed to the team, not to him alone,
since he sits on the team responsible for it; stated flat with no intensifier;
and standing as the single deliberate numeric exception on the page, never a
precedent for putting other numbers on the surface. The raise financials stay in
the briefing without exception.

## Excluded by canon

A standing record. For every element, device, or approach considered this session
and not pursued because a canon rule closed it: what it was, which rule closed it,
and what it would have bought. Canon still governs the output. This section does
not reopen it. It names the doors so a specific rule can be reopened deliberately
later, when it is worth it.

### Display and type devices

- Uppercase or all-caps display and headlines. Closed by: "Sentence case always.
  UPPERCASE reserved for single-line eyebrow only" (canon and page 04). What it
  would have bought: the reference primary's monumental uppercase masthead voice,
  a more overtly designed display register.

- Heavy display weights (GT Sectra Bold 700, Black 900) for impact. We own them
  and considered them for a photo-less hero. Closed by: the quiet authority
  register and canon's deliberate weight inversion, where the largest type is the
  lightest (Display Regular). What it would have bought: heavier presence on the
  hero. Closed because heavy display reads as force, which is performed conviction
  by another name.

- A monumental display step above the ceiling (a chapter-takeover moment in the
  hundreds of px, as the primary uses). Closed by: the resolved display ceiling,
  with roughly 112px treated as the line where quiet authority becomes spectacle.
  What it would have bought: a hero that dominates the way the reference primary's
  takeover letters do.

### Faces and language

- A third Latin face, or a monospace label face for metadata and section markers
  (as matte uses a mono for its bracket labels). Closed by: the two-Latin-plus-one-
  Korean limit ("the ceiling is absolute", page 04). What it would have bought: a
  low-cost craft signal and a structural marking device without adding a display
  face, matte's editorial index effect.

- Noto Serif KR as the Korean face. It is the obvious, fully hinted, freely
  available web Korean serif with a complete weight range. Closed by: canon, which
  prohibits Noto Serif KR in any public-facing context. What it would have bought:
  a robust Korean webfont today. What closing it costs: our Korean runs on the
  Nanum Myeongjo substitute with fewer optical niceties, pending the licensed
  Sandoll Myeongjo.

- Standard (non-Fine) GT Alpina for all body sizes, or a sans for form and UI
  labels. Closed by: canon body face is GT Alpina Fine, and the two-face limit
  bars a UI sans. What it would have bought: steadier small-size legibility from
  the standard optical, and clearer form controls from a sans. What closing it
  costs: the Fine optical is higher contrast, so the smallest reading sizes are a
  legibility watch item. We answer it narrowly by setting the 12px fine step in
  the standard optical, not Fine.

### Graphic and textural devices for a page carrying itself on type alone

- Gradients and tonal washes in the grounds. Closed by: the closed eight-color
  palette, "no tints, no shades, no exceptions" (`tokens/colors.css`). What it
  would have bought: depth and atmosphere on photo-less grounds without adding
  imagery.

- A living hero object: a WebGL field, a generative center, or a hero video, as
  two of the reference secondaries use to give a still page a moving center.
  Closed by: no AI or stock imagery, no photography beyond founder headshots, and
  the rule that type, color, and restrained motion carry the site. What it would
  have bought: a living center for a still page.

- Texture, grain, noise, pattern fills, or ornament. Closed by: the hairline
  system with no decorative dividers, colored border accents, or double rules
  (page 12), and the closed palette. What it would have bought: warmth and a sense
  of material on empty grounds, a digital echo of the brand's physical
  materiality.

- A chromatic spot accent used as a graphic device (as one secondary uses a bright
  green off its ground), including bringing Jade into the dark sections. Closed by:
  the closed eight-color palette, and the dinner theme's explicit "no chroma
  accent", where Jade is a named failure mode (`tokens/colors.css`). What it would
  have bought: a punch of energy and a wayfinding accent in the Plum Ink and
  Aubergine sections.

- Illustration, line art, diagram, or iconography as an imagery substitute (for
  example a floor-plan diagram for the one-footprint model). Closed by: no stock or
  AI imagery, no photography beyond headshots, and construction-governed
  iconography (page 12). What it would have bought: visual relief and explanatory
  support where the argument currently carries alone.

### Motion and conversion

- Motion as emphasis: scrub, parallax, or scroll-jacking, the reference primary's
  signature. Closed by: "motion marks state change, not importance" (page 12), and
  the structure decision's restrained-reveal posture. What it would have bought:
  the primary's immersive, physical narrative. (Motion is out of scope for this
  session; the canon closure is recorded because it shaped the type and layout
  thinking, for instance the reference device of the largest type rising out of a
  clip.)

- Conversion density: persistent or repeated calls to action, a floating call-to-
  action bar, an FAQ accordion, exit-intent, as the reference secondaries carry.
  Closed by: the low-density conversion decision (structure decision), reinforced
  by canon, which bars performed conviction, social proof widgets, and components
  that route customers through prescribed sequences (page 12). What it would have
  bought: a conversion safety net for a reader who leaves mid-argument. We take the
  belief ladder and the header shortcut instead.

- Internal daypart code names on the model band, considered as authentic internal
  language. Closed by: canon, no internal daypart code names on any external
  surface, ever. What it would have bought: nothing external worth having; the band
  uses the descriptive names and the closure is correct.

### Location and orientation

- The neighborhood as hero orientation ("in St. Elmo," "South Austin," the
  footer mark "선 · St. Elmo"). Closed by: the location and property constraint
  above, pre-lease and unsigned, no property identifier on any external surface.
  What it would have bought, stated so the cost is chosen and not absorbed
  quietly: real specificity in a hero whose one job is to orient. A neighborhood
  places the room on a mental map, sets a price band and a crowd, and tells a
  local reader something true before a word of argument. "Austin, Texas" cannot
  do that work. The hero now orients to a city of nearly a million people
  instead of a block in South Austin, and the copy carries that looseness on its
  single most orientation-dependent surface until the lease is signed. The bet
  is that a warm, forwarded investor reads for the model and the moat, not the
  cross streets, so the cost is real but survivable. It stops being survivable
  the day a location-curious reader arrives cold; that is the same door the
  no-photography cost names, and it reopens with the lease.

- The opportunity field's photo-promise caption ("Room photography to come.
  Found light, no stock, no AI"). Closed by: the location and property constraint
  (property-agnostic, pre-lease) and the no-photography rule. It reads worse than
  a canon brush, it is a property claim: it promises a specific room the venture
  cannot yet show or even name, on a pre-lease site, which is the same drift the
  neighborhood sweep just cleaned. What it would have bought: a hint of
  forthcoming warmth and a credit asserting the photography ethic (found light,
  no stock, no AI). Cut with nothing in its place. The field carries the 선 accent
  glyph alone, which needs no caption. The same photo-promise recurs on the team
  section's room slot and is closed the same way when that section is set. The
  photography-ethic credit, if it is worth stating at all, belongs on a surface
  that is not also making a room claim.

### Voice and conviction

- The photography-ethic credit as a caption ("Real portrait, found light, no
  stock, no AI") under the founder headshots, and the identical credit on the
  opportunity field. Closed by: no performed conviction, declarative over
  aspirational. It announces integrity instead of demonstrating it, performed
  conviction wearing a photo credit, and it spends words a low-word page cannot
  afford. What it would have bought: an explicit signal of the no-stock, no-AI
  ethic at the one place the site shows real people. Cut. The ethic is
  demonstrated by the photograph being real, not asserted beside it. This closes
  the thread left open when the credit was first cut from the opportunity field:
  there is no surface on this page where announcing it reads as anything but
  performed.

### The standing cost of no photography

Stated plainly, not assumed. The site cannot show the room, the food, or the
people, except two founder headshots, so it cannot use the most persuasive lever a
restaurant raise has: desire. Every belief is installed by type, color, and
argument alone. The consequences run through the whole architecture. The moat has
to carry feeling in words the reader must read, not in an image absorbed at a
glance, which is why it is the one long section. The opportunity cannot show its
market and the model cannot show its space, only the abstract daypart band. The
architecture compensates structurally: the protected long moat section, the
daypart band as the single graphic rupture, the oversized 선 as texture, and the
founder headshots as the one photographic anchor of credibility. The honest cost
is that a photo-carried version of this page could be shorter and land faster,
because desire is fast and argument is slow, and on a phone, where images convert,
we are asking a warm reader to read rather than to look. The bet is that the warm,
forwarded funnel makes that acceptable, since the reader arrived motivated. If a
cold, paid, or search channel is ever added, this constraint becomes a conversion
liability and is the first door to reopen.
