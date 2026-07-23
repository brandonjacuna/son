# Build specification

Status: governing for the build. Decided 2026-07-21, all eighteen batched
decisions ratified by Brandon (fifteen in the main batch, three on the
confirmation state). This document is R3's deliverable: the copy refit and
the design language against the track, merged into one panel-by-panel
specification. The build session inherits execution and the named gates
only. No design decisions remain open below.

Inputs: `docs/structure-motion-decision.md` (governing structure and
motion), `docs/type-decision.md` (governing type), `docs/copy.md` (approved
copy, unchanged here), `docs/reference-spec.md`, the token files, the
superseded-in-part `docs/design-language.md` and
`docs/content-architecture.md` (read for what survives), the Design
Translator profiles (Box: Brand Identity, Editorial and Layout, Web and UI,
Motion and Interaction, Narrative Architect), and the Brand Guidelines
(ClickUp 2ky45bmy-15773: pages 03 and 12, and the Ma baseline). All inputs
were reached.

Copy refit result: every panel is carried by approved copy at the sentence
level. No new copy is needed anywhere, including the arrival state. No
approved sentence fails to fit its panel. One density flag (P9 desktop) is
a build verification, not a copy problem.

## 1. The frame, and two examined non-collisions

The reference vocabulary is the default; canon argues per instance; close
calls go to Brandon; nothing closes silently. The three registers are in
section 8.

Two candidate settled-vs-settled collisions were examined and neither is a
genuine collision; the reasoning is recorded so the doors stay visible.

1. **"Nothing simply appears" vs. "narrative motion never touches the
   ask."** Not a collision: R1's panel map row reads "P10: the ask…
   Feedback register only," which already scopes the entrance rule. The
   ask's every element arrives **by travel**: the panel scrolls in
   complete. Travel satisfies "nothing simply appears" (nothing pops; it
   enters at the panel edge as a ground does). The ask is the one panel
   with zero timed entrances.
2. **The still 선 above dark grounds vs. "absent in daylight" vs. the wipe
   gate.** A mechanism question, not a decision conflict: the layer sits
   above the dark grounds and below content; the daylight panels occlude
   it, and the occlusion IS the wipe. One mechanism serves the absence rule
   and the not-a-watermark gate simultaneously.

## 2. The systems

### 2.1 Panel composition grammar (Decision 3)

Three grammars cover all eleven panels. The 10% Ma margin
(`--son-margin-page`) is the panel frame and is inviolate at every width.

- **The diagonal** — P1 only. Display sentence upper-left on the margin,
  lock-up low-right on the margin, open low-left as the specified void and
  the eye's exit into the moat. The top horizon is the chrome.
- **The column** — P2, P3, P4, P6, and the reading sides of P7 and P9. One
  reading column, left edge on the 10% margin, measure `--son-measure`,
  block optically centered (midpoint ≈ 46vh when seated). Across the moat
  the column's left edge and measure are constant, so P2–P6 read as one
  column traveling through a changing world. This is what holds P3: the
  same column, the world removed around it.
- **The isolate** — P5, the ask's centered stack, the coda's final frame.
  Centered both axes, optical center slightly high (≈ 47vh). P5 and P10
  are deliberate kin: the thesis and the ask face the reader head-on,
  symmetric, complete.

Every panel names its dominant void in section 3 — the Ma baseline's
present/absent discipline at panel scale.

**Panel height rule (Decision 4):** panels are `min-height: 100svh` and may
grow with content where a small viewport demands it (P8 mobile is the known
case; SE-class hero is flagged). Moving edges stay hard regardless of
panel height.

### 2.2 Chapter boundaries (Decision 5)

The hard swap at a moving panel edge, designed:

- **Ground leads, content follows.** Entrances fire at ~85% active, so the
  seam always crosses the viewport before the incoming panel's text rises.
  Color mass announces the chapter; the eyebrow is the first text to land.
- **The seam is clean.** Two grounds abut at a 1px-crisp moving line. No
  hairline rule, no shadow, no dissolve — the color cut is the line. Text
  color and theme resolution swap with the seam; each panel carries its own
  theme and nothing recolors mid-panel.
- **The wipe.** At P6→P7 the rising Bone edge wipes across the held glyph:
  the still layer is clipped by the seam as the daylight panel covers it,
  while visibly not moving. At P9→P10 the mechanism runs in reverse: the
  glyph is re-revealed under the rising Aubergine edge in exactly the
  position it was left, three chapters later, unmoved. The thesis
  performed: everything traveled; the one thing that matters did not.
  Implementation, ratified by Brandon at gate A (2026-07-21): paint-order
  occlusion. The still layer is fixed between the dark grounds and the
  daylight panels' stacking level, so the daylight grounds clip the layer
  at exactly the moving seam in the compositor, zero per-frame script; a
  scripted clip could lag on the single frame that matters most, and this
  cannot. The load-bearing stacking invariant is recorded in
  track/track.css and enforced by adherence/check-track.mjs. The
  not-a-watermark demonstration passed gate A (frames:
  refs/shots/gate-a-wipe, refs/shots/gate-a-rereveal).
- Nothing else moves at a seam. The seam is the loudest event on the page
  and gets the frame to itself.

### 2.3 The arrival state (Decision 6)

**The arrival is the first frame of the hero, not a screen before it.**
Plum Ink, the Sŏn wordmark already at its chrome position top-left, the
still 선 already present at 0.06. Nothing else. When fonts and chapter-I
assets are ready (floor ~800ms so the arrival reads as a beat, not a
flash), the hero choreography begins from this exact frame. The wordmark
never moves; there is no handoff seam and no splash surface.

- The wordmark renders instantly via an inlined subset of GT Sectra Fine
  covering exactly S, ŏ, n (~2KB; build detail). The still layer is the
  drawn path and has no load dependency.
- The still layer never enters. It is the ground condition, present from
  frame one. "Nothing simply appears" governs things that enter; this
  layer's meaning is that it was already there.
- **No arrival copy.** Any line here is a loading message: either performed
  conviction or a progress indicator, both closed (page 12; copy is closed
  at the sentence level). R1's ruling stands: the wordmark is the arrival.
- Degradation: if fonts hang past ~5s, render the reduced path complete
  rather than firing choreography on fallback faces. Display never fires
  on unloaded fonts.

### 2.4 The chrome (Decision 7)

Three elements, unchanged: wordmark left (Wordmark face at Subhead scale),
access note "By request only" (Eyebrow) and A1 "Request the briefing"
(Descriptor) right.

- At the top, over P1: transparent, part of the hero frame.
- Hides on scroll down (~300ms, feedback register). Returns on scroll up
  as a **solid bar in the active chapter's ground and theme**: Plum Ink
  over chapter I, Bone or Parchment over chapter II's panels, Aubergine
  over the ask, Plum Ink over the coda. This amends the build-scratch
  pass-5 settlement (solid Plum Ink) to the track: "a summoned object
  should be solid" holds, but on a page whose ground is a traveling
  variable, a fixed Plum Ink bar over daylight would be a foreign dark
  band. The summoned object is solid in the world it is summoned into.
- A1 is an instant native jump to the ask. The track does not animate the
  travel; replaying the traversal at the reader would be a forced
  sequence, and no smooth-scroll-to-anchor exists (carried exclusion).
- Header reveal is **not** suppressed during the band pin. It is
  wayfinding for the already-convinced reader; the feedback register
  governs it everywhere the same.

### 2.5 The band as rupture (Decision 8; panel detail in §3 P9)

The band is the site's one bounded pin-and-scrub, its one saturated
moment, and the page's only horizontal move — that combination is the
rupture. Desktop sequence:

1. P8→P9 hard swap (Parchment→Bone); eyebrow and headline rise while the
   panel travels in.
2. **The pin engages only when the panel is fully seated** — the
   composition is complete and stable before it locks. Held frame:
   headline at top (the anchor), the empty footprint spanning the column
   below it, "First light" and "Last call" already bounding the span. The
   band sits inside the reading column, bounded by its labels, inside the
   margins — never full-bleed (carried).
3. Over ~150vh of scroll the four stripes build left to right,
   scrub-keyed, reversible: jade, onggi, plum ink, aubergine. The day
   sweeps the fixed footprint at the reader's own pace. Each label
   (Coffee · Lunch · Dinner · Late night, Eyebrow, vertical on desktop)
   lands **timed** as its stripe completes: travel scrubbed, text timed,
   the two-system split honored inside the set piece. Jade's only
   appearance on the site.
4. At full build the pin releases and the body and A2 rise (timed, block
   register). The body's entrance announces the release — motion says
   "you may continue" without an affordance. Fires once; scrubbing back
   re-runs stripes but text never un-enters.

Either side of the pin: normal travel. The pin must not read as a page
end; release is visibly followed by content the reader has not seen, and
pin length is verified against real build distance at build (gate 7).

Mobile: no pin. The stacked band builds top to bottom, scrub-keyed through
the viewport; the column form does the pin's work (carried). Reduced
motion: band renders complete, no pin, no build.

### 2.6 The still 선 (mechanics consolidated; Decision 13 of R3, Decisions 1/3/7 of R2)

- One fixed element, rate zero, centered in the viewport, 88vh
  (`tokens/seon.css`), opacity 0.06 on the dark grounds, 1.0 at the coda.
- Z-order: above the dark grounds, below content. Daylight panels (P7–P9)
  occlude it; the occlusion at the two dark–light seams is the wipe
  (§2.2), implemented by paint order, ratified at gate A.
- Present P1–P6 and P10–P11; absent through chapter II by occlusion, not
  by fade.
- It never enters, never moves, and must never sit fully inside one panel
  like a background image (gate 1). Its coda behavior is §3 P11.

### 2.7 Motion registry (Decision 13)

- **Per-line clip-rises only where breaks are locked**: the hero Display
  strophe, the loop-opener line, P5's Solo strophe, P6's blockquote line.
  Everything else enters in the **block register** (500ms, one clip per
  block, 80ms sibling stagger). Line-splitting stays out of body and
  Headline text; strophes remain the only per-line choreography units.
- Values carried from R1 as starting points, tuned at build with fresh
  eyes: blocks 500ms, ease-out-cubic on transform, linear on opacity;
  lines 260ms from 120% behind the padded clip, 80ms sibling stagger;
  fires once at ~85% active, never re-fires. Named tuning knob: the
  reference's measured line ease is ease-in-quad, which the Motion
  profile flags as register-inverted for entrances; both are prototyped
  at the tuning pass rather than asserted here.
- Headshots fade only (500ms, linear). Grounds and the ask enter by
  travel. The still layer never enters. The coda glyph's opacity is
  scrub-keyed. Chrome elements fade (400ms).
- Clip geometry per `tokens/typography.css`: pads 0.12em/0.26em with equal
  negative margins, rise origin 120% of the padded clip, flex-column
  strophe stacks mandatory.
- Scroll driver: Lenis, lerp 0.10, easeOutExpo, syncTouch false, pinned
  version at build (R1).
- Reduced motion, the designed second path: entrances opacity-only and
  instant; the pin never engages and the band renders complete; the still
  layer is simply present; the coda is the placed close (amended
  2026-07-23 at pass 6, per the design answer accepted 2026-07-22: a
  two-frame flow composition whose closing mark is a panel-local placed
  instance of the drawn path, P11 occluding the resting layer by document
  order; the hard-cut phrasing is superseded); Lenis smoothing off,
  native scroll. Every claim fully legible static.
- `tokens/motion-immersive.css` is retired at build (it predates R1 and
  carries corrected-away values and killed devices). A new
  `tokens/motion-track.css` carries the track values above plus the pin
  distance and reduced-motion rules. Feedback tokens in
  `tokens/spacing.css` are unchanged and govern the feedback register.
- Performance floor (carried): transform and opacity only; will-change
  scoped to the animation window and cleared; frame rate verified on a
  real phone.

## 3. Panel-by-panel specification

Type steps are `tokens/typography.css` (R2, ratified): Solo 58/128/144 at
0.98; Display 46/73/82 at 1.00; Headline 38/57/60; Section, Subhead, Lead,
Body, Menu/Descriptor, Eyebrow, Fine as tokenized. Strophe bands switch
where the floors engage: hero ~800px, Solo ~580px.

### P1 — Hero. Plum Ink, dinner.

- **Copy:** orientation "One Korean room in Austin, Texas, open from first
  light to last call." at **Display**. Desktop two-line strophe: "One
  Korean room in Austin, Texas," / "open from first light to last call."
  Mobile six-line strophe (locked 2026-07-20): "One Korean / room in
  Austin, / Texas, / open from / first light / to last call." Loop-opener
  "We build for the second visit, not the first." at **Headline**. Chrome
  strings as approved.
- **Composition:** the diagonal. Sentence upper-left on the margin;
  lock-up low-right on the margin at Headline scale, sitting over the
  still layer (field-under-mark, the amended register rule). Named void:
  the open low-left, the eye's exit into the moat.
- **Enters:** from the arrival frame. Display lines rise per line (260ms,
  80ms stagger); a 240ms hold; the loop-opener rises; the lock-up
  block-rises low-right; access note and A1 fade last (400ms). Initiator:
  display line one. Holds: wordmark, still 선. The site's first gesture
  teaches the whole vocabulary: rise from clips, two voices, one thing
  still.

### P2 — Moat, the Renata world. Plum Ink.

- **Copy:** eyebrow "Why this" (**Eyebrow**); paragraph one ("Every good
  restaurant has a Renata…") at **Body**.
- **Composition:** the column. Named void: the right two-thirds, where the
  still glyph sits.
- **Enters:** eyebrow, then the paragraph, block register.

### P3 — The departure. Plum Ink.

- **Copy:** "One day she leaves. There's always a better offer across
  town." at **Body** (Decision 1: not promoted).
- **Composition:** the same column as P2 — same left edge, same measure —
  with the world removed around it. Promotion in type would spend the
  event on the words; the emptiness is the event. Emptiest panel on the
  site. Named void: everything but two lines.
- **Enters:** one block rise. Holds: everything else.

### P4 — Moat, the owners. Plum Ink.

- **Copy:** paragraph three ("The owners tell each other they'll be
  fine…") at **Body**.
- **Composition:** the column. **Enters:** block.

### P5 — Pull-line. Plum Ink.

- **Copy:** "A restaurant is a memory business. Most forget." at **Display
  Solo**. Desktop three-line strophe: "A restaurant is" / "a memory
  business." / "Most forget." Mobile four-line strophe: "A restaurant" /
  "is a memory" / "business." / "Most forget." (R2 fit table; band switch
  ~580px.)
- **Composition:** the isolate. No eyebrow, no other content; the belief
  takes the top voice at its install point. The still glyph co-present at
  0.06 is what keeps 144px from reading as spectacle (R2's comp finding).
- **Enters:** per-line rises, 80ms stagger; nothing else exists to move.

### P6 — Blockquote and the close. Plum Ink.

- **Copy:** blockquote "The restaurant remembered nothing." at
  **Headline**; then the compounds paragraph and "We're building the
  restaurant…" at **Body**.
- **Composition:** the column returns, same edge as P2–P4.
- **Enters:** blockquote as a single line-rise, then the two body blocks.

### — Hard swap: the tonal hinge. Bone wipes the glyph (§2.2).

### P7 — Opportunity. Bone, base editorial theme.

- **Copy:** eyebrow "The opportunity"; headline "Korean food and the city
  of Austin are climbing the same curve. Sŏn opens where they meet." at
  **Headline**; lead "In a city where dining is judged harder than most,
  Korean cooking holds the highest honors." at **Lead**; body "The
  customer this room is built for already lives in Austin, and already
  eats this way." at **Body**. Verify-pending flag carried from copy.md
  (the accolade stays qualitative; source-verified before ship).
- **Composition:** column left; the peacock field right — full panel
  height, bleeding to the top, right, and bottom panel edges, ≈38vw, a
  vertical hard seam (static; the band remains the page's only horizontal
  move). The 선 accent (`min(36vh, 44vw)`; mobile `min(30vh, 60vw)`)
  planted in the field, **Bone on Peacock** (carried from v3), no frame,
  no caption. Named void: the seam gap between column and field.
- **Enters:** eyebrow → headline block → glyph rises in the field (500ms)
  with the lead → body. Reduced motion: glyph fades.
- **Mobile:** column, then field below.

### P8 — Team. Parchment, dosi.

- **Copy:** eyebrow "The team"; names at **Subhead**; roles at **Eyebrow**
  (interpunct grammar: "Brandon Acuña-Cardona · Operations and strategy",
  "Dominic Thomas · Capital and systems"); bios at **Body**.
  Verify-pending flags carried (credentials and years against source; the
  dollar figure is the page's one deliberate numeric exception).
- **Composition:** two founder columns, portrait-led: hairline-framed 3:4
  slot, then name · role, then bio. Slots stay reserved; Brandon owns the
  portraits.
- **Enters:** eyebrow, then left column blocks, right column +160ms;
  headshots **fade only**, never rise.
- **Mobile:** stacked; the panel grows past 100svh — the sanctioned case.

### P9 — Model. Bone, base editorial theme.

- **Copy:** eyebrow "The model"; headline "One footprint. Four dayparts.
  One set of fixed costs." at **Headline**; band bounds "First light" /
  "Last call" and stripe labels Coffee · Lunch · Dinner · Late night at
  **Eyebrow**; both body paragraphs at **Body**, with A2 inline on "in
  the briefing."
- **Composition and motion:** §2.5 in full. The headline is the anchor
  throughout the pin. Named void: the unbuilt footprint at pin engage.
- **Density flag:** eyebrow, headline, band, and two paragraphs inside
  100vh desktop is the tightest fit on the site. Verify at build; if it
  fails, the body sits below the seated fold and the panel grows. No copy
  change.

### — Hard swap. Aubergine rises; the glyph is re-revealed where it was left.

### P10 — The ask. Aubergine, dinner.

- **Copy:** eyebrow "The ask"; headline "We share the briefing with a
  small number of partners." at **Headline**; form strings as approved
  2026-07-20 (labels **Eyebrow**, "Company or affiliation · optional"
  interpunct treatment; inputs **Body**; submit "Request the briefing"
  **Descriptor**; the five functional strings; errors per
  `tokens/components.css`: 2px border plus message, never color alone);
  disclaimer verbatim at **Fine** (12px held); confirmation "Your request
  is in. You will hear from us within two business days." at **Body**.
  Verify-pending carried: counsel confirms the disclaimer; the
  two-business-day promise stands only if it can be kept.
- **Composition:** the isolate — centered stack, headline over the Bone
  card (`.ask-card` token re-resolution carried; hairline edges; no
  shadow). Deliberate kinship with P5.
- **Enters: by travel, complete** (Decision 11). Zero timed entrances;
  feedback register only — focus, hover, validation, and the confirmation
  state (§4).

### — Hard swap. Plum Ink; the frame closes.

### P11 — Coda. Plum Ink, dinner.

- **Copy:** the Sŏn / 선 lock-up (**Wordmark**); "Austin, Texas. By
  request only." at **Descriptor**. No further ask, no new words. The
  closing mark is the still layer itself (R1 P11; the 12px footer seal is
  superseded).
- **Composition and motion — the deliberate close (Decision 12):** P11
  runs ≈180vh, the only extended panel besides the pin distance. The
  lock-up and location line rise (timed) as the panel seats: signature,
  then information. Then the final ~80vh of travel: the footer text exits
  upward at rate one past the held glyph while the still layer's opacity
  scrubs 0.06 → 1.0, whole silhouette, 88vh, centered. The scroll ends
  with the glyph alone at full opacity — the last frame is the one thing
  that never moved, holding the page. Signature, information, seal, as a
  traveled sequence rather than a stacked frame. Nothing sits over the
  glyph at full opacity: at that moment the layer behaves as a mark (R2
  Decision 3) and content over it would break the balance spec, so the
  close empties rather than stacks. Scrubbing back reverses it; the close
  is the reader's own act.
- **Reduced motion:** the placed close (amended 2026-07-23, design answer
  accepted 2026-07-22): footer frame, then a placed closing-glyph frame at
  full opacity in flow, the panel occluding the resting layer by document
  order; content can never overlap the mark, and the page still ends on
  the glyph frame. In this path the closing mark is a placed instance of
  the drawn path, not the layer itself; that sentence remains the
  scrubbed path's.
- **Phone:** the ruled side-crop stands (middle ~58% of the silhouette at
  full opacity, the complete lock-up above); revisited only at the build
  gate on a real device. The named door remains the phone-only still-size
  override.

## 4. The confirmation state (Decisions 16–18)

- **Post-submit, the track does nothing** (Decision 16). No auto-travel,
  no lock, no pointer toward the coda. Auto-traveling the reader is a
  forced sequence and narrative motion on a conversion surface at the
  moment of conversion; locking the track is control theft with no
  argument. The confirmation copy closes every loop the page opened,
  which makes it the one exit the structure permits unguarded. Cost
  accepted and recorded: most converted readers leave at the confirmation
  and never see the full-opacity close. The coda's audience is mostly the
  unconverted and the thorough, and nothing downstream of the ask depends
  on being seen.
- **The coda stands unchanged for both readers** (Decision 17). It
  survives conversion because it was never funnel machinery: it installs
  nothing and asks nothing — signature, information, seal. To the
  unconverted reader it is the dignity of no chase; to the converted
  reader the same travel inverts into the stronger form: they have just
  asked to be part of the thing, then watch everything exit the frame
  while the one still thing holds and comes to full presence. The
  P9→P10 re-reveal performs the thesis mid-argument; the coda performs it
  post-commitment. Canon forbids celebrating a conversion; gravity is not
  congratulation, and this is the only ending canon would permit after
  one.
- **"The one separate surface" framing is retired** (Decision 18). The
  framing was a document-era answer: in a scrolling column, separateness
  was the means of making the state change unambiguous and the exit
  legitimate. On the track the panel is already the surface: P10 is a
  full-viewport isolate, the card is the only object in front of the
  reader, and a state swap of its interior is a total state change of
  everything in view. R1's routes line already speaks this language
  ("one URL plus the post-submit confirmation state"). Mechanism: the
  card interior swaps — fields, submit control, and disclaimer give way
  to the confirmation line — 200ms cross-fade, feedback register. The
  eyebrow and headline remain; post-submit the headline reads as context
  for what was requested, not a repeated ask. Announced via `aria-live`.
- **Persistence boundary:** across reloads on the same browser, via one
  stored flag. In-memory covers scroll-away and A1 re-entry but dies on
  reload, and a reload would hand a fresh form to a reader whose request
  already landed. Mechanism (build detail): one localStorage key
  (`son-ask-confirmed`, value = submit timestamp), written **only after
  the endpoint returns success** — a failed submit can never fake a
  confirmation. On load, if present, P10 renders in the confirmation
  state. The flag carries a 30-day window, after which the form returns:
  the two-business-day promise cannot be honestly displayed months
  later, and a reader returning that late is plausibly making a new
  request. Private mode or blocked storage degrades to in-memory only —
  accepted residual risk; the client flag is a courtesy, not the
  guarantee.

## 5. Build gates

Named, in order of demonstration:

1. **Not-a-watermark**: the seam-tracked wipe at P6→P7 and the re-reveal
   at P9→P10, shown to Brandon before anything layers on the still 선
   (carried, R1). PASSED 2026-07-21; paint-order occlusion ratified as
   the mechanism (§2.2).
2. **Coda deliberate-close**: the emptying-out sequence must read as a
   close, not the layer merely becoming visible (carried, R2 Decision 7;
   §3 P11 is the proposal it tests).
3. **Phone coda on device**: the side-cropped full-opacity glyph in the
   hand (carried; door named: the phone-only still-size override).
   PASSED 2026-07-23 on device: the coda glyph reads as an ending,
   cropped and all. The phone-only still-size override door stays
   closed, unspent.
4. Still-layer opacity 0.06 on-device tune (carried). PASSED 2026-07-23
   on device at 0.06; no tune needed.
5. Cross-engine fit (WebKit/Firefox) on the strophe maxima (carried; the
   Solo floor's 4.4% slack prices it).
6. SE-class hero height (carried) and **P9 desktop density** (§3 P9).
7. Pin distance vs. illusion-of-completeness on real content (Motion
   profile check).
8. Font-hang degradation path (~5s ceiling → reduced-path render, §2.3).

Verification stance carried from R1/R2: real phone, reduced playback,
fresh eyes on a later day; WCAG in browser, not the design file.

## 6. Inherited and provisioned items

- **Lenis** remains the build's one new JS dependency; Dominic inherits
  it; version pinned at build (carried, R1).
- **Dominic provisions**, alongside the existing `data-endpoint` POST URL:
  **server-side deduplication by email** on the submit endpoint, so a
  duplicate from any path (second device, private window, cleared
  storage) collapses in his inbox rather than reading as two leads. The
  client flag prevents reader-facing confusion; the server prevents the
  data-facing one. Nothing else.
- Founder portraits: Brandon owns; reserved frames stand (carried).
- Canon amendment (motion registers, R1 §5): Brandon carries it into the
  Brand Guidelines (standing open item).

## 7. Decisions record

Ratified by Brandon 2026-07-21, verbatim from the session batch:

1. P3 at Body, column-continuous, not promoted.
2. Eyebrows once per section (P2, P7, P8, P9, P10); none on P3–P6, P11.
3. Composition grammar: diagonal / column / isolate; moat column
   continuity; Ma margin inviolate; per-panel named void.
4. Panel height rule: 100svh floor, growth allowed, edges hard.
5. Chapter boundary design: ground leads, content follows; clean seam;
   theme swaps at seam; the wipe and re-reveal at the two dark–light
   seams.
6. Arrival: first-frame-of-hero, inlined wordmark subset, still layer
   present from frame one, ~800ms floor, fonts-gated; no arrival copy.
7. Chrome: revealed header solid in the active chapter's ground and
   theme; transparent at top; A1 instant jump; no reveal suppression in
   the pin.
8. Band choreography as specified; fires once.
9. Accent field: full-height right field ≈38vw, three-edge bleed, Bone
   glyph on Peacock, glyph block-rises.
10. Team composition: portrait-led two columns; fade-only; reserved
    frames stand.
11. The ask arrives complete: feedback register only, zero timed
    entrances; centered stack, kinship with P5.
12. Coda: ~180vh; signature → information → exit → glyph alone; opacity
    scrubbed to 1.0; ends on the glyph frame; reduced path by hard cut.
13. Motion registry: per-line rises only on locked strophes; block
    register elsewhere; motion-immersive.css retired at build, replaced
    by motion-track.css.
14. Axis addendum recorded in the governing doc.
15. New copy: none. Copy misfits: none. P9 density is a build-verify.
16. Post-submit, the track does nothing; the reader decides; the cost
    (most converted readers never see the close) is accepted and
    recorded.
17. The coda stands unchanged for both readers: argument-close for the
    unconverted, commitment-seal for the converted; it carries no ask and
    no belief, so conversion cannot orphan it.
18. The confirmation is a state of P10, not a separate surface; in-card
    cross-fade; eyebrow and headline remain; state persists per §4;
    aria-live announced; the content-architecture framing is superseded.

### Amendments to ratified decisions

The record above stays verbatim; what supersedes a ratified decision is
recorded here, dated, with the reason. This is the pattern for anything
that supersedes a ratified decision from here on.

1. Decision 12, the reduced-path clause ("reduced path by hard cut"):
   superseded 2026-07-23 by the placed close (§2.7, §3 P11; the design
   answer accepted 2026-07-22, built at pass 6). Reason: a path with no
   scrub cannot carry the footer out past an 88vh centered mark, so a
   hard cut with the footer framed puts content over the mark at full
   opacity, the balance-spec violation. The close became a two-frame flow
   composition whose closing mark is a placed instance of the drawn path,
   the panel occluding the resting layer by document order.
2. **The moat body register** (amends Decision 3's one-voice implication
   and §3's P2/P4 step labels): ratified 2026-07-23, from the device
   session findings. The moat column is not one voice; it is a story
   followed by a verdict. Story register: P2, P3, P4. Case register:
   P6, at Body 16, matching chapter II's argumentation — P6's letter
   needs no amendment ("the column returns, same edge as P2–P4"; the
   ratified word is edge). P4 ruled story on content grounds: it opens
   and closes in scene, and the room that forgot is the payoff the
   pull-line then abstracts; ruling it case would put the verdict voice
   before the verdict and give chapter one two hinges where the reading
   names one. The silent device evidence (P4 at 16 did not bother) cuts
   less than it looks: five panels were read at one size, against no
   register boundary. The story-body size is 18 or 20 (GT Alpina Fine
   Regular 400 at the body leading — never Lead's face), decided on
   device strips at both values; the recommendation enters at 20
   (namespace: 18 duplicates Lead's size and distinguishes two named
   steps by weight alone, a system smell independent of appearance; 20
   is a clean namespace at the top of canon's Lead band). The register
   is an editorial reading ratified per instance, not a mechanical
   rule: copy.md's own label for the post-blockquote slot is "Body,
   continued", so the document asserts slot continuity and the split is
   a judgment. copy.md is not edited; this entry is the supersession
   note over §2's first Body slot (the words are unchanged; the type
   size is not — R2's precedent class). Realization at build: a
   panel-register attribute, never a theme override (typography.css:
   sizes are invariant across dayparts; the register axis is orthogonal
   to theme). Token names and the typography.css admission terms land
   at build with the chosen value.
3. **Decision 1's letter ("P3 at Body") and §8 judgment register 1**:
   amended 2026-07-23. P3 takes the story size, level with its column
   siblings; "promotion" is read as above the column, which the ruling
   preserves. The rationale is confirmed by measurement rather than
   assertion: the seat frame is >=88% void at every candidate size from
   16 through Subhead 21, so no size holds that frame by mass — the
   void argues, exactly as ratified. The device defect at P3 was break
   shape, not size: at 16 the sentence pair breaks 43/18 characters
   with the second line dangling at ~39% of measure, an accidental
   wrap; at the story size the pair re-breaks composed (measured: two
   lines at both 18 and 20, both widths, real binaries). Treatment
   changes were argued against Decision 1 and refused: Subhead changes
   face and makes the sentence a heading; Lead Light is an elegy plus
   300-weight hairlines on Plum Ink OLED; a designed gap performs the
   departure the copy refuses to perform. THE COUPLET DOOR, named and
   unspent: if the composed couplet still under-holds in the hand and
   the reaction is occupancy, the staged argument is the two sentences
   locked as a one-panel couplet strophe (a dated amendment to Decision
   13's line-splitting rule) — never Subhead, never Lead Light.
4. **Decision 3's constancy sentence** ("the column's left edge and
   measure are constant"): amended 2026-07-23. Constancy narrows from
   {left edge, --son-measure} to {left edge, rendered width}, scoped to
   the moat column, where co-visibility makes it a guarantee.
   Per-register measures render equal width, measured on the real face:
   62ch@16 = 565.44px; 55.1ch@18 and 49.6ch@20 render the same width
   exactly (ch scales linearly on this face). On the phone the 10%
   margins cap every candidate, so the registers render at identical
   width there by container. Recorded finding: .t-lead and .t-body
   already consume the same 62ch token at different sizes in P7/P9, so
   rendered-width constancy was never global; it was only ever
   meaningful under co-visibility, which is why the scope is the moat.
5. **Decision 12's uniqueness clause** ("P11 runs ≈180vh, the only
   extended panel besides the pin distance"; also §3 P11, §8
   Reconsidered 2; the track.css comment moves at build): superseded
   2026-07-23. P3 becomes the page's second designed extension: the
   100svh seat frame, then a ~40svh empty tail before P4's edge —
   ratified as the fix for the device finding that chapter one has no
   felt movement (the glyph registered on device, so the parallax was
   firing and the five frames were too alike). The tail is the first
   moment the rate-zero relationship becomes legible rather than merely
   present: the text exits and the glyph holds the frame alone.
   Extension stays rationed by proportion (pin 150 > coda travel 80 >
   departure tail 40), and the tail carries no scrub, no pin, and no
   full-opacity event, so the coda's close remains the page's only
   ending. Magnitude judged in the hand at the device pass; the failure
   criteria are recorded in build-state so the judgment is recognizable
   rather than talked into.
6. **Decision 4's growth clause**: extended 2026-07-23 with a third
   height class, the designed extension — emptiness-driven, all
   viewports, distinct from content growth (P8 mobile) and from travel
   distance (pin, coda). Sanctioned today for exactly P3. With it: P3's
   entrance arms at full seat rather than 85% (the second seat-fired
   panel after P11; the registry letter gains the exemption at build),
   and the anti-page-end verification (gate 7's class) attaches to the
   tail. The tail distance is tokenized at build in motion-track.css
   beside the pin distance so the two encodings cannot drift (scratch
   item 9's pattern).
7. **R2's letter ("the seven untouched steps") and the typography.css
   header sentence ("body holds 16px at every width")**: amended
   2026-07-23 by the story register. Body's own sentence survives per
   step — the Body step still holds 16 at every width, and P6, chapters
   II–III, and the ask all consume it unchanged — but the scale gains
   an admission-termed story-register reading size, the same shape as
   Solo's admission: the panel structure created a condition the scale
   never priced (story paragraphs as the sole reading content of full
   dark viewports; 16px in a large empty field reads small in a way it
   would not in a document). Canon's page 04 Body band (14–16) argues
   and loses per instance: the story size sits inside canon's own Lead
   band (16–20), so no new band is minted; the delta is Lead's size
   territory at Body's face and weight, taken on dark-ground rendering
   grounds. Ratio guarantees are untouched (the >=1.2 adjacency
   guarantee is display-ramp-scoped). Fit evidence, measured this
   session on the real binaries: P2 at 20/390 is 13 lines, 390px, 46%
   of frame; SE-class worst case 14 lines, 420px, fits with headroom;
   the copy-refit fit sentence re-verifies at the chosen size at build
   (P2/P3/P4, both widths, three engines).
8. **Amendment 2's size clause ("18 or 20")**: closed 2026-07-23 at the
   device pass. The story size is 20, ruled in the hand: 18 lost
   clearly, and 22 — directed as a third candidate from the pass,
   extending the clause's letter — was measured on the real binaries
   before being built and REFUSED unbuilt on the couplet gate: at 22
   the P3 couplet breaks to three lines on all three engines at both
   phone widths, reintroducing the exact break-shape defect the story
   size exists to repair, and it fails on desktop too, where 18 and 20
   never did (a dangling fragment at 10 to 21% of measure). Secondary
   finding, recorded: below ~595px a body paragraph at 22 renders
   larger than the Subhead step itself — a worse system smell than
   18's size duplication, and outside canon's Lead band where 20 sits
   inside it. Evidence: refs/notes/pass-10-story-22.txt,
   refs/shots/pass-10-couplet-22. The strip apparatus (the 18 token
   pair, the ?story query switch, the pre-paint head-script selector)
   is removed with this ruling; the track ships at 20 with no
   candidate mechanism, and a stray ?story parameter is inert.
9. **Decision 3's diagonal seat ("lock-up low-right on the margin") and
   Decision 4's SE-class flag**: amended 2026-07-23, ruled against the
   built state. "Low-right" is the low of the SEEN frame, not of the
   overgrown panel's foot: the foot-anchor was never the grammar's
   point, and it is what handed the mark to the fold — an SE reader's
   first frame was a severed 선, and the site cannot forbid a design
   that crops the mark (the hero-bleed kill, the drawn-path-over-font
   decision) and then open with a fold-cropped mark; the reader cannot
   tell the fold from a designer. The no-partial-mark rule outranks
   the foot-anchor. Realization: at short frames (phone widths,
   height ≤ 720px) the entry air compresses 14svh → 9svh and the
   strophe→loop gap 40px → 32px; type untouched, reading order
   untouched, both voices stay in the arrival frame; the sanctioned
   growth remains and moves below the completed lock-up as ground —
   breathing room, not displacement. Boundary measured on the built
   page at 375px: the natural stack completes with its 4svh floor at
   ≥ ~716px, the compressed one down to ~665px; no portrait device
   ≥ 360px wide (the wrap-free floor) sits below that. Rejected: type
   shrink (forbidden; the mark is drawn precisely so it cannot be
   re-set), exiling the loop-opener below the fold (breaks the reading
   order and the arrival gesture's second voice), absolute positioning
   (fights the stacking invariant). Evidence:
   refs/shots/se-hero-fix.
10. **The confirmation placement ruling (scratch 3h)**: amended
   2026-07-23 with its reason, not replaced. The prior ruling — the
   line renders where the submit control stood, the empty card as the
   isolate — was right for the case it was made from and wrong in
   scope. Two corrections. One: the empty card with a line in its
   lower third is NOT the isolate; the isolate the site taught (P5,
   the ask's stack, the coda) is content centered in a field. Two: the
   act-position's reason is the standing view — the reader who just
   acted must see the answer — and no width proxies that boundary,
   because the card never exceeds the layout viewport at any tested
   width (590px at 1440×900, 644px at 390×844); what shrinks a phone's
   standing view is the keyboard, i.e. the visual viewport. Scoped
   realization, measured per swap at the moment the reason applies: if
   the card-centered line would land inside the visual viewport (24px
   breathing), the confirmation centers in the held card at the
   isolate's optical seat (center slightly high, 47%); otherwise it
   renders at the act. A phone with the keyboard dismissed and the
   whole card in view centers too — the condition working, not
   leaking. Degradation rule, ruled: if the visual viewport is
   unavailable or reports nothing usable, the swap renders at the
   act's position — toward the safe case, never the elegant one. The
   load path is untouched: a returning reader arrives at a state, not
   a change. Evidence: refs/shots/g4-confirmation-covisibility.

## 8. Session registers

### Excluded by canon

1. An arrival line or progress indicator. Rule: page 12 (progress
   indicators not reflecting progress; performed conviction) and closed
   copy. Cost: none; the wordmark carries it.
2. Clip-rise entrances on the ask's card and fields. Rule: the ratified
   boundary — narrative motion never touches conversion surfaces. Cost:
   the ask never teaches the entrance vocabulary; bought: a complete,
   calm surface at the commit.
3. A hairline rule at chapter seams. Rule: no decorative dividers. Cost:
   nil; the color cut is the line.
4. Footer text held over the full-opacity coda glyph. Rule: the
   drawn-balance spec via R2 Decision 3 (at full opacity the layer
   behaves as a mark). It forced the emptying-out close, which is a gain.
5. Auto-traveling the reader to the coda after submit. Rule: forced
   sequences (page 12) and the conversion-surface motion boundary,
   crossed at once. Cost: none a warm reader would pay; the close remains
   the reader's own act.

### Excluded by judgment

Each argued against the warm, forwarded reader; none closed silently.

1. Promoting P3 above Body. Promotion spends the event on type; the void
   argues. Cost: no typographic monument at the departure.
2. A centered-splash arrival. A second surface and a teleporting mark;
   the first-frame arrival has no seam. Cost: quieter than a title card.
3. Animated A1 travel. Replaying the traversal at the reader is a forced
   sequence; the instant jump is the reader's own teleport.
4. Suppressing header reveal during the pin. Wayfinding for the
   convinced outranks frame purity. Cost: a fourth element can enter the
   band frame on scroll-up.
5. Eyebrows on every moat panel. Chrome-ification; naming is carried
   once per section.
6. The accent glyph straddling the Bone/Peacock seam (the intersection
   literalized). A bisected glyph reads as error; the field placement
   carries the claim. Cost: the literal metaphor.
7. Per-line rises on Headline and Body text. Unlocked breaks make lines
   viewport-dependent choreography; blocks carry them. Cost: less
   line-cascade texture outside the display moments.
8. Locking or ending the track after submit. Control theft with no
   argument; scroll was the reader's surface through the whole argument
   and remains so after it.
9. A post-submit pointer toward the coda ("see the close"). The page
   directing at the moment its interest in directing ends. Cost, named:
   most converted readers never see the full-opacity close.

### Reconsidered, admitted

1. The revealed header re-grounded to the active chapter — amends the
   build-scratch pass-5 settlement's letter, keeps its intent.
2. P11 extended to ~180vh, the only extended panel besides the pin, for
   the emptying-out close.
3. Panel growth past 100svh where small viewports demand it.
4. "Enter by travel" as the sanctioned entrance class for conversion
   surfaces (the P10 reading of R1's own row).
5. The wipe as a seam-tracked clip on the fixed layer — mechanism
   admission feeding gate 1. (Outcome at gate A, 2026-07-21: the clip is
   realized by paint order rather than script; ratified, §2.2.)
6. The confirmation as a state of P10 with client-side persistence (one
   flag, success-gated, 30-day window) — the separate-surface framing
   retired in favor of the isolate the track already provides.
