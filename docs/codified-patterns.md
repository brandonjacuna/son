# Codified patterns (G3)

Status: governing for the rules below. Ruled by Brandon 2026-07-23 at the
G3 codification gate, from the track build's candidate list
(`docs/track-scratch.md` remains the archaeological record; this document
is what graduated). Scope, ruled: the system carries rules and
vocabulary, never one page's body. The track's implementations — the
still-layer architecture, the wipe and pin realizations, the seat
observer, the capture tooling, every measured threshold — stay
build-local, enforced where they are. Anything that supersedes a rule
here is recorded dated, with the reason, in the pattern of the build
spec's amendments ledger.

## 1. The enhancement inversion — the governing rule of the motion system

The designed second path is the DEFAULT; the full experience is the
opt-in. Reduced motion, no-JS, and failure paths (a hung font, a dead
script) are not fallbacks written as overrides of the rich path: they are
the stylesheet's base state, and the choreography exists only under
explicit gate classes applied when capability and permission are
confirmed (the track's idiom: `html.js` set pre-paint by script
presence; `html.track-motion` set only when motion is permitted). Under
this inversion the second path can never be broken by a failure to
enhance, because nothing needs to succeed for it to render. The track
removed four failure classes this way: the placed close, the complete
no-JS band, the no-JS header, the pin that cannot freeze.

This is stricter than progressive enhancement. PE says build the
baseline first; the inversion additionally makes the enhanced state an
explicitly gated class, so the baseline is not a fallback that rots
behind a media query — it is the shipping default that every ungated
reader gets.

**THE DELETE-THE-GATE TEST — required review question on every surface
that carries an enhancement gate.** The reviewer performs it; it is not
a principle to nod at.

Procedure: open the surface and remove its gate classes from the root
element (for the track: delete `js` and `track-motion` from `<html>` in
the inspector; equivalently, load with JavaScript disabled). Then read
the entire surface top to bottom and operate every control.

Expected result: every claim is legible, every control operates, layout
is complete and correct, and the page reads as a designed composition,
not a degraded one. Nothing is hidden mid-entrance, no state is frozen
or empty, no content waits on anything.

Failure: any content that vanishes, any control that dies, any frozen
frame. The fix direction is always inversion — make the failing state
the stylesheet default and gate the enhancement — never a patch to the
fallback.

## 2. Construction over synchronization — the mechanism principle

Where a visual relationship must hold under scroll or time — a clip
tracking a seam, a pin engaging and releasing at a seat, an entrance
keyed to a position, a field under entered text — realize the
relationship as CONSTRUCTION: stacking order, layout geometry, static
height, observer geometry. Never realize it as a per-frame script that
keeps two things in agreement. Whatever script synchronizes, jank, load,
or a missed frame can desynchronize; what structure guarantees cannot
disagree with itself.

The test for any proposed mechanism: name the failure state in which the
two coupled things disagree. If the mechanism makes that state
representable and then manages it, choose instead the construction that
makes it unrepresentable.

Corollary, derived rather than memorized: scroll is never hijacked. A
pin that repositions content from a scroll handler is synchronization
with the reader's own control surface, and it inherits every desync and
every jank of that surface; the structural pin — sticky inside a wrapper
measured to the pin distance — engages and releases by construction and
cannot fall out of agreement with the scroll it tracks. The reader's
scroll keeps moving the document; only the panel's position holds. The
same derivation refuses smooth-scroll position faking, scroll-keyed
clip-paths, and any mechanism whose correctness depends on a handler
running every frame.

The build's five instances, recorded as evidence (details in
`docs/track-scratch.md` and `track/`):

1. **Paint-order occlusion** — the wipe as stacking order: the opaque
   ground clips the fixed layer at exactly the moving seam, in the
   compositor, zero per-frame script.
2. **Sticky-in-wrapper** — the pin above, carrying the corollary.
3. **The label floor** — the field cannot withdraw beneath entered text
   because the floor is computed geometry, not a managed state.
4. **The zero-band seat observer** — seat-firing as observer geometry
   (root box collapsed onto the viewport's top edge), no scroll math.
5. **The enhancement inversion itself** — the default-state construction:
   rule 1 is this principle applied to failure paths.

## 3. Motion register rules

- **Entered text never loses its ground** (the label-floor rule). No
  scrub state may render entered copy unreadable: "text never un-enters"
  extends to the field the text stands on. If a scrub-keyed field can
  withdraw beneath text that has entered, floor the field at the text's
  rendered extent. The failure this removes is silent — a contrast
  failure that only a scrub-back review finds.
- **Instant means duration AND delay.** A reduced-motion path that
  zeroes durations but preserves delays ships staggered invisibility:
  content that appears instantly, later. Every reduced path zeroes both.
  (The v3 fallback regressed exactly here; the global kill in
  `tokens/spacing.css` zeroes durations only — its scope is a separate
  swept change, and this rule binds regardless of that outcome.)
- **Nothing focusable is ever invisible.** Focus arriving inside
  un-entered content arms that content immediately; fire-once semantics
  hold. Accessibility outranks choreography, always.

## 4. Conversion-surface rules — document stability

Ratified at the track's ask card; they bind any future conversion
surface.

- **An interior swap never moves the document under the reader.** When a
  swap is an event (a submit, a live state change), the container
  freezes its block size for the swap; the interior changes, the
  geometry does not. A shrinking document shifts scroll and stales every
  position-keyed anchor below it.
- **The response renders where the act happened.** The reader who just
  acted sees the answer in their standing view, without the page moving.
- **A load-rendered state is a condition, not an event.** No fade, no
  focus steal, natural placement: a returning reader arrives at a state,
  not a change.
- **Anchors re-measure after any interior swap.** Anything keyed to
  document geometry (scrub windows, pin distances) follows the document
  it measures.

## 5. Token governance — paired encodings

Values that must move together are tokenized adjacently, with the
pairing named in the comment, and swap together or not at all. If two
encodings of one design fact live apart, they will drift apart; the
token file is where the pairing is made structural. The build's
instances: the coda travel (one token consumed in svh by layout and
against innerHeight by the scrub), the departure tail (tokenized beside
the pin distance), the story size and its compensated measure (the pair
renders one constant width; 992 font-units in every pairing).

## 6. Font governance — delivery names

A delivery name is a face served under a scoped name for delivery
mechanics only (the standing instance: "GT Sectra Fine Arrival", the
880-byte S/ŏ/n wordmark subset, inlined so the mark never waits on the
network). A delivery name adds no typographic voice and does not count
against the face limit. THE WATCHED DOOR, enforced by both adherence
font allow-lists (`.stylelintrc.json`, `adherence/check-copy.mjs`): the
violation is never the name existing; it is the name ever gaining one
glyph beyond its subset, or appearing on any element that is not a mark.

## 7. Verification appendix — method knowledge

Each entry below cost a session to isolate; together they are the
vaccine against the phantom-failure class (probes that read false and
send a build chasing defects that do not exist, or passing states that
do).

1. **Measure ring contrast while focused.** Unfocused `outline-color`
   computes to currentColor; the unfocused measurement is of nothing.
2. **Measure the fill that paints.** A ground probe that walks ancestor
   backgrounds reads through a transparent element to the panel behind
   it; measure the pseudo-element fill that actually renders.
3. **Prove occlusion by paint-boost, never layer-removal.** Hiding a
   layer collapses compositing and re-anti-aliases everything above it,
   producing pixel diffs that read as occlusion where none exists. Force
   the layer loud instead.
4. **Font gates are load-level unless made render-level.** A FontFaceSet
   check reports load state; layout can still hold fallback-derived
   values (see 5). Gate the rendered basis: a ch ruler on the asserted
   face (GT Alpina Fine measures 9.12px/ch at 16; the serif fallback
   ~9.82). `getComputedStyle().fontFamily` reports the cascade, never
   the rendered face.
5. **Flush before measuring ch.** Firefox can resolve ch-based
   `max-width` against the fallback at first layout and never
   re-resolve it after the font lands (`fonts.ready` reflows glyphs,
   not the stale unit). Style-flush the measured elements first; when
   the stale state fires, DETECT it and log it — never archive its
   geometry under a passing verdict.
6. **A reported metric with no assertion is not evidence.** Every line a
   probe prints carries a gate or it is decoration.
7. **The invisible edge.** Same-ground panels render no edge between
   them; any frame-reading analysis (anti-page-end above all) runs on
   VISIBLE content — one text's exit to the next text's entry — never on
   box geometry.
8. **Capture determinism.** Rest states capture under reduced-motion
   emulation (the designed second path renders them instantly and
   identically — verified, not assumed: assert motion-path parity once).
   Scroll-keyed sequences are authoritative over full-page composites,
   which evaluate scrub state at scroll 0. Explicit scroll ranges are
   device-blind; resolve ranges per device.
9. **Tracking is set on the element that carries the font-size.** An em
   tracking inherited from a smaller ancestor computes near zero.
10. **Every settled behavior gets a named pass owner up front.** A
    settled behavior with no pass assignment is a silent omission class;
    the final review is the net, not the plan.

## Pointers

- Enforcement: `adherence/check-copy.mjs` (copy canon, fonts),
  `.stylelintrc.json` (color and font discipline),
  `adherence/check-track.mjs` (the track's stacking invariant,
  build-local beside the architecture it guards).
- The archaeological record: `docs/track-scratch.md` (mechanisms,
  rulings, doors, method notes as they were found).
- Standing doors stay recorded where they live (track-scratch,
  build-state, type-decision) and are not rules: the phone still-size
  override, waypoints at chapter growth, the skip link at stop growth,
  Body floor 16 → 17, the couplet door, the wordmark watched door
  (enforced), the chrome focus re-hide nuance, the reduced-motion
  load-time gating limitation.
