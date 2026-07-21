# Type, restarted for the panel structure

Status: governing for type. Decided 2026-07-20, all seven batched decisions
ratified by Brandon. This session re-examined the type system under the
reframe (reference vocabulary as default, canon arguing per instance) for the
five conditions the panel structure created — conditions that did not exist
when the prior scale was set from reading conditions and brand guidelines
with zero reference input, for a flat document that no longer exists.

Supersedes: the type-step table and step assignments of
`docs/content-architecture.md` (already superseded in part); the C8 ceiling
resolution recorded in the prior `tokens/typography.css` header; the moat
pull-line's "promotion in isolation, not in type step"
(`docs/structure-motion-decision.md` §8); copy.md's slot note "held to the
same top voice as the hero" (the words are unchanged; the type step is not);
`build-scratch.md`'s footer-seal settlement (mechanism superseded by R1 P11,
structure preserved — see Decision 7); and design-language.md's "never with
Sŏn" register rule, amended per Decision 1. The hero two-step split, the
belief ladder, the panel map and panelization, the palette, the faces, and
copy at the sentence level all hold.

Primary inputs: `docs/structure-motion-decision.md` (governing),
`docs/reference-spec.md` §3 + scratch, both measurement notes under
`refs/notes/`, `docs/copy.md`, the token files, the binaries in
`assets/fonts/`, Brand Guidelines page 04 (ClickUp 2ky45bmy-15773, read
fresh under the reframe), and the Brand Identity, Editorial and Layout, and
Motion and Interaction profiles (Box). All inputs reached.

## 1. Method, and what it caught

Every value was measured, not asserted: Playwright against the real GT
binaries, fit maxima by binary search in the true panel context (100vh
panel, the standing 10% Ma margins, tracking on the sized element), every
proposed value re-verified wrap-free, every current value re-rendered
failing under the same conditions. An adversarial five-lens verification
pass reviewed the first draft and killed it, correctly, three times over:
the harness had silently rendered a fallback face (fonts do not load under
`setContent`; the corrected harness hard-asserts the loaded face), the fit
math assumed 6vw margins against the standing 10% Ma rule, and the hero's
ratified two-step split had been merged into one Display block. It also
proved the clip-pad mechanism collapses in normal flow (the flex-column
requirement in `tokens/typography.css` is verification-caught, not
decorative). Chromium only; non-Chromium engines are untested and priced
into the Solo floor's slack. Evidence and comps live with the session
record; the rendered proposal is the "Sŏn — Type re-examination" artifact.

## 2. The finding under the reframe

**The ceiling was never canon.** Page 04 sets no display ceiling — its
digital table tops at the Headline band (60–96px) and routes clamp
parameters to a later session. The 104 cap and the "~112 = spectacle" line
were a prior session's assertion. The collision was judgment-vs-reference,
and it resolved BOTH ways on measurement:

**The strophe, not the ceiling, is the constraint.** Under the panel
structure display lines are choreography units — locked breaks, one clip
per line — so every display size is a fit equation. Measured at the 10%
margins on the real face:

| Condition | Binding line | max @1440 | @1280 | @375 |
| --- | --- | --- | --- | --- |
| Hero Display sentence, 2-line strophe | "One Korean room in Austin, Texas," | 82.7 | 73.6 | — |
| Hero mobile 6-line strophe | "room in Austin," | — | — | 47.9 |
| Pull-line, 3-line strophe | "a memory business." | 148.4 | 132.1 | — |
| Pull-line mobile 4-line strophe | "is a memory" | — | — | 60.7 |

The current tokens (96@1280 → 104) wrap the hero's Display sentence at
every viewport below ~1810px: clean only on 1920-class desktops, wrapped on
the laptops most readers use. The hero comes down; the isolated pull-line
goes up.

## 3. The scale (ratified)

Values at 375 / 1280 / cap; faces and the seven untouched steps as in
`tokens/typography.css`.

- **Display Solo — NEW: 58 / 128 / 144, leading 0.98, Regular 400.**
  Admission terms: display text as the only reading content on a full panel
  (today exactly P5); strophe-locked per band (mobile strophe below ~580px
  floor-engage, desktop strophe above); contains, wraps, never crops. The
  fluid slope (10vw) is the fit formula, so the guarantee holds at every
  width by construction.
- **Display — 46 / 73 / 82, leading 1.00** (was 48/96/104 at 1.03). The
  hero's Display sentence, two-line desktop strophe, six-line mobile
  strophe; slope 5.7vw = the fit formula; floor engages ~800px where the
  mobile strophe takes over.
- **Headline — floor 38** (was 40); 57@1280 and the 60 cap unchanged.
  Restores the ≥1.2 adjacency guarantee everywhere, including within the
  shared hero panel (46/38 = 1.21). Consistent hierarchy beats five
  percent (Decision 5).
- **Weight inversion held at every scale** including Solo: canon and the
  reference concur (Regular 400; size does the work).
- Ratios at cap: 144/82 = 1.76, 82/60 = 1.37; at 375: 58/46 = 1.26,
  46/38 = 1.21.

**The consequence, chosen not forced (Decision 2):** the largest reading
voice moves from the door to the thesis. The rule as Brandon settled it:
the belief takes the top voice at its install point, where it lands as
payoff. The hero opens the loop, the moat installs it. The hero being
smaller is the argument working, not a concession.

## 4. The architectural 선 (tokens/seon.css)

- **Still layer 88vh** (Decision 3, whole silhouette at the coda), opacity
  0.06 on dark grounds, 1.0 at the coda reveal. One element: it absorbs the
  v3 per-section moat atmosphere and IS the coda's closing glyph. Rationale
  as ratified: the coda is the payoff, a cropped arrival is a partial
  arrival, and at full opacity the texture carve-out lapses — the layer
  behaves as a mark at exactly that moment, so cropping it breaks the
  drawn-balance spec for the same reason the hero bleed died.
- **Register rule amended (Decision 1):** "never with Sŏn" becomes "never
  with Sŏn in the same register." The still layer sits under the P1/P11
  lock-ups as field-under-mark: lock-up is signature, layer is atmosphere.
  Register duplication is the failure; glyph recurrence is not.
- **Punctuation accent min(36vh, 44vw)**, phone min(30vh, 60vw), derived
  from the reference's planted mid-display tier (256px/720px viewport).
- **Mobile stance:** hold size, crop, never shrink — the sanctioned
  exemption from the horizontal-overflow exclusion (Decision 1), which
  continues to bind all reading type and Latin display.
- **The phone-coda cost, honestly stated** (Brandon asked): at 390px the
  88vh layer is ~676px of glyph width — the phone shows the middle ~58%,
  both side strokes cut, at full opacity as the closing image. A reader who
  knows the glyph from the lock-up reads a zoomed detail of 선; one who
  does not reads abstract strokes. It is somewhat worse than the desktop
  framing implies: the "partial arrival" the coda decision rejected on
  desktop is what the phone gets, softened by the complete lock-up
  signature directly above it. Accepted with the door named: a phone-only
  still-size override exists if this cost grows at build; its price is the
  mobile atmosphere presence through the whole travel.
- **Build gates:** R1's not-a-watermark demonstration, plus Decision 7's
  requirement — the coda reveal must read as a deliberate close, not the
  layer merely becoming visible. Different events; only one ends a page.
- **The Korean face at architectural scale — tested, passes on craft.**
  The drawn path (the only Korean form the site ships) inspected at
  stroke level at 2400px: calligraphic entry flares, head serif, modulated
  bows, clean joins, no faceting, no artifacts. Scoped precisely: this
  verifies rendering craft at scale; Sandoll stroke authority remains the
  drawn-mark production routing's question (page 04) and is not reopened.
  The still layer is not gated. No blocker.

## 5. Clip-rise geometry (Decision 6)

Leading is a motion variable. Measured on the real face: glyphs span
0.956em against a 1.24em font box; unpadded per-line clips cut descenders
at any leading below ~1.22 — including the old 1.03, where the y in
"memory" amputates mid-stroke. Sentence case floors at 0.942 (cap 0.700 +
descender 0.242); the reference's 0.8 is an uppercase-only face's trick.
Tokens: pads 0.12em / 0.26em with equal negative margins; rise origin 120%
of the padded clip; mover unpadded; **flex-column strophe stack mandatory**
(negative margins collapse in normal flow and inflate leading 0.12em per
line — verification-proven). Reduced motion: clip-rises become
opacity-only; the rest state is identical on both paths.

## 6. Mobile stance, amended

Compress by strophe, hold by crop — one system, two stances, each earned
by its job. Reading display re-breaks its strophe per band to recover every
pixel the no-crop rule allows (Solo 58 against a measured 60.7 max at 375 —
the slack covers untested text engines; Display 46 against 47.9). The
non-reading 선 holds size and crops, the reference's stance, where the
ratio is genuinely held. Mobile strophes are new choreography units,
amending R1's strophe lock (Decision 4): the six-line hero strophe
("One Korean / room in Austin, / Texas, / open from / first light / to
last call.") is accepted in principle and locks only after Brandon reviews
the rendered panel — the natural break ("in Austin, Texas," whole) caps at
41.6px and flattens the panel's own hierarchy, which is why it lost.

## 7. Collisions, and who won

1. Display ceiling vs viewport-isolated display: the reframe won both ways
   — Solo up to 144, hero down to 82. The ceiling was an assertion; the
   strophe is a measurement.
2. Weight inversion vs architectural scale: canon holds, reference concurs.
3. Sentence case vs monumental uppercase: canon wins at the Solo step;
   cost recorded in the register.
4. "No horizontal overflow of any element" vs R1's crop-not-shrink 선: the
   session's one settled-vs-settled collision; resolved by the brief's own
   restatement and ratified as Decision 1 — the exclusion re-scoped to the
   reading ramp and Latin display.
5. Mark-balance spec vs the coda crop: resolved by Decision 3 — at full
   opacity the layer behaves as a mark, so the whole silhouette closes the
   page (88vh), the crop option declined.
6. "Adjacent steps ≥ 1.2×" vs the measured mobile floors: resolved by
   Decision 5 (Headline floor 38); the guarantee holds globally again.

## 8. Session registers

### Excluded by canon

1. Uppercase at the Solo step. Rule: sentence case always (page 04). Would
   have bought: the reference's monumental masthead voice at the one place
   it would land hardest. Carried instead by scale and isolation.
2. Weight above Regular at Solo scale. Rule: canon's weight inversion
   (page 04 table: largest = Display Regular). Would have bought: sturdier
   stems at 144px on low-DPI screens. The reference concurs with canon
   (its whole ramp is 400), so the door costs little.
3. Korean display TEXT at architectural scale (setting 선 or any Hangul as
   live type). Rule: page 04 Rule 3 (the 선 glyph is a drawn logotype
   element) and tokens/fonts.css (Korean text on external surfaces reopens
   font delivery). Would have bought: nothing the drawn path does not
   already deliver, at added font-load risk. Cost ≈ 0, measured.
4. Noto Serif KR (standing door, recorded unchanged): no Korean text at
   scale exists to need it.

### Excluded by judgment

1. The reference's 0.8 display leading. Geometry: an uppercase-only trick;
   sentence case on this face floors at 0.942 (measured). Chosen: 0.98 and
   1.00, with the clip-pad geometry that makes either renderable.
2. The natural mobile hero strophe ("in Austin, Texas," kept whole). It
   caps the floor at 41.6px and flattens the hero panel's own two-step
   hierarchy against the loop-opener. The six-line strophe at 46 keeps the
   step; its "Texas," beat is deliberate cadence under per-line rises.
3. Solo at hero parity (82) — the canon-clean alternative preserving "same
   top voice." Would have bought: copy.md's parity note intact and no
   voice inversion. Refused because the isolated panel reads as absence at
   that scale (the comp is the evidence), and ratified so by Decision 2.
4. An intermediate Solo (the two-line strophe near 128 at cap) without a
   new step. Would have bought: a modest lift with no ramp change. Refused:
   it neither fills the panel nor preserves parity — the worst of both.
5. Ratio-held mobile READING display. The no-crop rule caps the phone at
   strophe-fit; re-breaking recovers 58 of the 60.7 theoretical; full
   ratio-hold (~100px+) is impossible without cropping words. Cost named:
   the phone never gets the desktop's 9:1 reading drama — that drama lives
   in the still-선, which does hold its ratio.
6. JS fit-to-width sizing (the takeover-letters approach). Tokens whose
   slopes are the fit formulas are deterministic and testable; runtime
   measurement is neither.
7. A separate per-panel atmosphere 선 (v3's device). Duplicates the still
   layer on the same grounds. Cost: per-panel compositional control of the
   glyph's position; the still layer's position is global by definition.
8. Keeping the mobile hero floor at 48 by shaving the Ma margin (a ~5vw
   margin would fit it). The margin is the Ma system's specified emptiness,
   not a type variable.
9. The still layer at 110vh (rendered and argued as the architecture-first
   option; also its 130vh sibling, rendered twice). Would have bought: the
   moat text sitting deeper inside the glyph, a stronger wipe interaction
   at panel edges. Refused at ratification (Decision 3): the coda closes on
   the whole glyph, and at full opacity the layer is behaving as a mark.
10. A phone-only still-size override (shrink-to-fit at the coda). Would
    have bought: a whole-silhouette phone coda. Refused for now: it trades
    away the layer's mobile presence through the entire travel; named as
    the door if the accepted phone-coda cost grows at build.

### Reconsidered, admitted

1. A reading step above the retired ceiling: Display Solo 58/128/144,
   admission-termed (isolation only, strophe-locked, exactly the panels
   that qualify — today one). The "~112 = spectacle" line is retired as a
   rule; the comp at 144 in isolation, with the still layer co-present,
   does not read as spectacle because nothing competes. Replaced by
   mechanical caps: strophe-fit × panel height, per instance.
2. Two-register tight display leading (1.00 / 0.98) plus the clip-pad
   geometry that makes tight leading renderable at all.
3. The still-선 as one consolidated element — atmosphere, texture, and
   closing glyph — under the lock-ups on P1/P11, admitted via the
   register-rule amendment ("never with Sŏn in the same register").
4. Per-breakpoint strophe re-breaking as a designed choreography variable
   (same words, breaks chosen per band, each set approved by Brandon;
   the hero's six-line set accepted in principle, locks on render review).
5. Viewport-relative 선 sizing with deliberate mobile crop — the
   reference's hold-by-crop stance, admitted for the non-reading layers
   only (Decision 1's scoping).

## 9. Open items

1. The six-line mobile hero strophe locks only after Brandon reviews the
   rendered panel (shown post-commit; Decision 4's condition).
2. Cross-engine fit verification (WebKit/Firefox) at build; only Chromium
   was testable this session. The Solo floor's 4.4% slack prices this.
3. Still-layer opacity (0.06) tunes on a real device at build.
4. Short-viewport phones (SE-class, ~667px): the mobile hero block plus
   chrome runs tight; verify at build.
5. `tokens/motion-immersive.css` predates the R1 restart and carries
   corrected-away values (450/850/1400ms, lerp 0.08) and killed devices
   (takeover, drift, marquee); flagged for the motion/build session.
6. The coda deliberate-close gate (Decision 7) and the not-a-watermark
   gate are the build session's first demonstrations, shown to Brandon
   before anything layers on them.
