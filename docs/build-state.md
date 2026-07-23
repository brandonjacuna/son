# Build state — the track

Written 2026-07-23 at the close of the build session (commits 31074de
through 5015dc0, tagged v4-track). Assume no context beyond this repo.
Governing documents: `docs/build-spec.md` (panel-by-panel specification,
decisions record with its amendments section), `docs/track-scratch.md`
(every mechanism, ruling, door, and method note from the build),
`docs/structure-motion-decision.md` and `docs/type-decision.md` (the
ratified structure, motion, and type systems), `docs/copy.md` (approved
copy, closed at the sentence level).

## What exists

The scrub-led track lives in `track/`: `index.html` (eleven panels, the
drawn 선 path, the still layer, the chrome, the inlined 880-byte wordmark
subset under the delivery name "GT Sectra Fine Arrival"), `track.css`
(type steps, three composition grammars, the wipe stacking, entrances,
the pin, the ask, both coda stances, the revealed header), `track.js`
(Lenis driver, coda scrub, entrance armer and arrival gate, band
controller, ask module, header controller), `vendor/lenis-1.3.8.min.js`
(pinned, byte-identical to the npm dist, MIT). The v3 fallback in `site/`
is frozen at tag v3-fallback and received only the retirement migration
(the carried ease value and reduced-motion delay kill in site.css).

Tokens: `tokens/motion-track.css` replaced the retired
motion-immersive.css (pass 2). Enforcement: `adherence/check-track.mjs`
(the stacking-context invariant, wired into `npm run lint` as lint:track)
plus the track/ scope added to check-copy.mjs and the delivery-name
entries in both font allow-lists. Evidence tooling:
`scripts/scrollframes.mjs` (scroll-keyed frames), `scripts/timeframes.mjs`
(timed-choreography frames), both under npm run. Node and npm live at
`~/.local/node/bin` (off PATH; prefix it or lint and shoot fail).
Playwright has chromium, webkit, and firefox installed.

## What each pass built

- **Gate A** (31074de, 71c1d87): the not-a-watermark wipe and re-reveal.
  Paint-order occlusion ratified as the mechanism. Evidence:
  refs/shots/gate-a-wipe, gate-a-rereveal.
- **Gate B** (2a8d7a3): the coda deliberate close, end-anchored scrub
  ratified. Evidence: refs/shots/gate-b-close.
- **Pass 1** (bfbe358): eleven panels, all copy at its steps, the three
  grammars, static chrome. Evidence: refs/shots/pass-1.
- **Pass 2** (0a1ef06): Lenis pinned and vendored, motion-immersive
  retired for motion-track.css, the reduced-motion delay-kill catch
  migrated into site.css, mobile chrome holds three elements.
- **Pass 3** (589e3a3): entrances and the arrival state; the wordmark
  subset and its two probe-verified engine facts (track-scratch 3b); the
  reduced-motion delay kill built into the track. Evidence:
  refs/shots/pass-3-arrival, pass-3-p7, pass-3-coda.
- **Pass 4** (8e97c4d, 0259770): the band; sticky-in-wrapper pin
  ratified; the label floor (no scrub state hides approved copy).
  Evidence: refs/shots/pass-4-pin, pass-4-band, pass-4-release,
  pass-4-scrubback.
- **Pass 5** (cf9c0c1): form, confirmation, persistence; the
  document-shrink catch (card holds its height on the live swap).
  Evidence: refs/shots/pass-5-ask, pass-5-frozen-card.
- **Pass 6** (b21804e, fe2c26a, 7714b1a): the placed close built as the
  default stance with html.track-motion as the opt-in (the enhancement
  inversion, scratch 3f); keyboard path walked; contrast from rendered
  pixels; the confirmation placement ruling executed; the amendments
  section added to the decisions record. Evidence:
  refs/shots/pass-6-placed-close, pass-6-confirmation-placed.
- **Pass 7** (31f2603, 5015dc0): the eight gates (below); the revealed
  header, found unimplemented at final review and built (scratch 3i
  carries the process lesson and the carried semantics). Evidence:
  refs/shots/pass-7-*, refs/notes/pass-7-gate5-cross-engine.txt.

## Gate status

Gates 1 and 2 passed at the gate passes (marked in build-spec §5). Gate
5 (cross-engine: three engines, four widths, zero wraps) and gate 8
(font-hang: complete render at the 5s ceiling, wordmark immune via the
subset) passed with evidence on disk. Gate 7 assessed: no pin frame
reads as a page end; the release is announced by the body with P10
rising in frame. Gate 6: P9 desktop density passed (pass 1); the
SE-class hero cost MATERIALIZED and awaits Brandon (below). Gates 3 and
4 PASSED at the device session (2026-07-23, real phone, Safari): the
phone coda reads as an ending, cropped and all (the still-size override
door stays closed, unspent); 0.06 held with no tune. The same session
produced two chapter-one findings, examined and ruled the same day:
the moat body register and the departure's tail (build-spec §7,
amendments 2–7). Both were built (passes 8 and 9) and ruled at the
device pass the same day: story size 20, tail approved at 40svh
(the closed section below).

## The device session (gates 3 and 4, plus seam crispness) — Brandon

Serve the repo from its root and open the track on the phone:

    cd ~/son/design-system && python3 -m http.server 8080
    # then on the phone: http://<the Mac's LAN IP>:8080/track/index.html

- **Gate 3, phone coda**: judge the side-cropped full-opacity glyph in
  the hand, in BOTH stances (normal scroll for the scrubbed close;
  Settings > Accessibility > Motion > Reduce Motion for the placed
  close). Emulated reference: refs/shots/pass-7-phone-coda (WebKit,
  iPhone geometry, both stances at 57.7% of the silhouette, matching the
  ruled middle ~58% crop). Known residuals that only the device shows:
  real Safari toolbar dynamics (the end-anchored scrub can begin
  slightly before the seat; recorded cost, scratch item on coda
  anchoring), OLED rendering of 0.06, true touch feel. The named door if
  the cost is too high: the phone-only still-size override
  (type-decision, judgment register 10).
- **Gate 4, still-layer opacity tune**: comparison strips at
  0.04/0.06/0.09 are in refs/shots/pass-7-opacity-tune. THE TRAP,
  probe-proven: overriding the CSS variable in devtools does NOT repaint
  under motion, because track.js caches the token at measure() and
  rewrites an inline opacity; a var-only override silently compares 0.06
  to 0.06 (the build's own first strips were three identical images).
  Tune by editing `--son-seon-still-opacity` in tokens/seon.css and
  reloading, or trigger a resize after the override.
- **Seam crispness at dpr 1** was probe-verified headlessly; eyeball a
  seam on the device in the same session (scratch item 6).

## The register session, the amendment build, and the device pass (2026-07-23) — CLOSED

The device session's two chapter-one findings were examined and ruled
the same day (the register session; every ruling is recorded as
build-spec §7 amendments 2–7). The moat is a story followed by a
verdict: story register P2/P3/P4, case register P6 at Body 16 matching
chapter II; P3 level with its siblings, the couplet door named and
unspent; the departure gains a ~40svh empty tail as the page's second
designed extension. Finding 2 rests entirely on the tail and the moat's
density arc — the glyph registered on device at 0.06, so witness
presence was never the problem; the frames were too alike.

The amendments were built the same day (passes 8 and 9; pass 10
measured and refused a third size candidate), and the DEVICE PASS
CLOSED 2026-07-23 with every item ruled:

1. **The story size is 20** (build-spec §7 amendment 8). 18 lost in
   the hand. 22, directed from the pass, was measured before building
   and refused unbuilt: the couplet breaks to three lines on all three
   engines at both phone widths — the break-shape defect the story
   size exists to repair — and dangles on desktop where 18 and 20
   never did. Secondary finding, recorded: a body paragraph at 22
   renders larger than the Subhead step below ~595px, a worse system
   smell than 18's duplication. Evidence:
   refs/notes/pass-10-story-22.txt, refs/shots/pass-10-couplet-22.
   THE STRIP APPARATUS IS REMOVED (the removal condition met): the 18
   token pair, the ?story query switch, and the pre-paint head-script
   selector are gone; the track ships at 20 and a stray ?story
   parameter is inert, verified post-removal on the rendered page.
2. **The tail is approved at 40svh: it reads as aftermath.** The
   criteria under which the judgment was made are preserved below
   (amendment 5's letter points here; they govern again only if the
   magnitude ever reopens):
   - TOO SHORT: the silence ends before it begins. P4's edge arrives
     while the eye is still releasing P3's lines, and the gap reads as
     paragraph spacing — layout air, not a place. The after-test:
     asked where the departure happened, you point at the two
     sentences. The space never became the event.
   - RIGHT: the emptiness reads as aftermath — the room after she
     left, crossed at your own pace, the glyph the only thing not
     moving. Asked where the departure happened, you point at the
     space. And chapter one afterwards has geography you could sketch:
     the dense room, the departure and its space, the hollow room, the
     monument, the verdict. If the sketch is "five screens of text,"
     travel did not read.
   - TOO LONG: you doubt the page — a scrollbar check, a flick to see
     if it is still alive, or the void with the glyph starting to read
     as an ending, the coda's grammar arriving early. The boundary is
     one full frame of nothing but ground: the tail fails when it
     stops being P3's aftermath and becomes the site's absence.
   - THE FURNITURE TELL, at any magnitude: if the emptiness reads as
     anticipation — a drumroll for P4, a transition any site might
     insert — it is decorating scroll. It must read as consequence,
     belonging to the two sentences above it, not to the panel below.
3. **The seam is clean** (the dpr-1 eyeball, re-queued from the gate
   session, scratch item 6: done on device).
4. **The Body-floor watch item did not fire**: the pass raised no
   finding that the case panels read small against story 20. The door
   (global Body 16 → 17) stays named and unopened; it reopens only on
   evidence, not by default.

Session registers (the register session, 2026-07-23). Excluded by
canon: ground events inside chapter one (no tints, no shades; the day
arc reserves Aubergine for the ask) — cost: the reference's per-slide
ground vocabulary, carried instead by the tail, the density arc, and
the register split. Excluded by judgment: the graded per-panel body
ramp (sub-perceptual; type acting at the departure), the mechanical
copy.md register rule (smuggled the judgment it claimed to remove),
the register seam as a felt progression event (withdrawn; zero
finding-2 credit claimed), measure narrowing, column vertical descent,
stepped still-layer opacity, entrance/leading/weight walks, site-wide
16 → 17 (the watch-item door above), and the P3 treatments — Subhead,
Lead Light, the designed gap (the couplet door named, unspent).
Reconsidered, admitted: two body registers inside one chapter as an
editorial reading; rendered-width constancy scoped to co-visibility;
the departure as the page's second designed extension; seat-firing as
a per-panel entrance term.

## Outstanding, by owner

**Brandon**
1. **SE-class hero ruling**: at 375x667 the hero grows 77px past the
   viewport and the lock-up completes below the fold at arrival; the
   strophe and loop carry, the diagonal's third point does not complete
   in the first frame. Frame: refs/shots/pass-7-se-hero. This is the
   sanctioned-growth flag from Decision 4, shown as built.
2. **Frozen-card desktop composition check, still owed**: the
   confirmation now renders where the submit control stood (ruled
   2026-07-23, BUILT on the live path, load path keeps natural
   placement; scratch 3h). Brandon asked to see both widths and rule
   whether desktop still reads as an isolate rather than bottom-heavy;
   the captures exist (refs/shots/pass-6-confirmation-placed, both
   widths) but the desktop composition ruling was not yet given.
3. The codification gate: CLOSED at G3 (2026-07-23, ruled). The
   graduated rules live in docs/codified-patterns.md (the enhancement
   inversion with the required delete-the-gate review test,
   construction over synchronization with the pin corollary folded in
   as ruled, the motion register rules, the conversion-surface
   document-stability rules, paired-encodings token governance, the
   delivery-name sentence, the verification appendix); the immersive
   components are formally retired (banners on all nine prompt docs;
   drop at next external regeneration); the 3c comment rewrite is
   executed. The sticky-in-wrapper ban did not graduate as its own
   sentence, by reversal: the principle carries it as a corollary. The
   standing doors stay recorded where they live. Companion changes,
   own commits: the delay-kill sweep (spacing.css global kill) and the
   Firefox stale-ch fix.
4. Carry the motion-registers canon amendment into the Brand Guidelines
   (standing open item from R1).
5. Founder portraits for the reserved P8 frames.
6. Verify-pending facts before ship (copy.md): the accolade source,
   Dominic's credentials and years, counsel on the disclaimer, the
   two-business-day promise.

**Dominic**
1. The POST endpoint: set `data-endpoint` on the form in
   track/index.html (the marked INTEGRATION POINT; today a valid submit
   shows the confirmation and logs a warning instead of sending, and the
   persistence flag is success-gated so it is never written).
2. Server-side deduplication by email on that endpoint (build-spec §6).
3. The Firefox stale-ch race — PRE-EXISTING, site-wide, surfaced by the
   pass 8 probe (evidence: refs/notes/pass-8-register-fit.txt, engine
   finding 1): on roughly two in ten desktop Firefox loads, ch-based
   max-width resolves against the fallback face at first layout and is
   never re-resolved when GT Alpina Fine arrives, so the reading column
   renders ~43px wide of ruled until any style invalidation — a broken
   page for those readers. Not patched at the register pass (predates
   it; scope is every ch measure on the site, not the moat). CANDIDATE
   FIX, named: a one-time style invalidation of ch-measured elements
   after document.fonts.ready (track.js already re-measures there;
   reading geometry alone does not re-resolve the unit). WebKit and
   Chromium are unaffected; phone widths are container-capped. Brandon
   rules at handoff.

**Nobody yet / next session**
1. Chrome behavior nuance: scrolling down with focus inside the revealed
   bar re-hides it with focus inside (carried v3 semantics, recorded in
   scratch 3i); fine today, revisit only if it bothers a real keyboard
   session.
2. The reduced-motion mid-session toggle keeps its load-time gating
   (recorded limitation).
3. Generated artifacts (_ds_bundle.js, _ds_manifest.json, oxlint
   allowlist) still embed the retired immersive register; regeneration
   is external (the compiler is not in this repo); the one 404-causing
   manifest path was hand-patched.

## Knowledge not otherwise obvious from the files

- Every pass ran a multi-agent adversarial verification; the method
  notes in scratch 3g are the distilled probe traps (measure rings while
  focused, measure pseudo fills not ancestor backgrounds, prove
  occlusion by paint-boost not layer-removal). The single most valuable
  sequence this build produced, per Brandon: isolate engine facts by
  probe, try the obvious fix, let the probe disprove it, revert, scope
  the mechanism, and record all of it (the wordmark subset story,
  scratch 3b).
- The full-page shoot tool composites the fixed layer only at the top
  viewport and evaluates scrub state at scroll 0: its slices of the
  still layer and the band are artifacts; scrollframes/timeframes
  sequences are authoritative (scratch items 6 and 6a).
- The stacking invariant is the load-bearing constraint of the whole
  still-layer concept: body, main.track, .pin-track, and dark panels
  must never gain a stacking-context-creating property. It is enforced
  by lint; the two sanctioned positioned panels are the daylight class
  and .panel--coda.panel--placed-close.
- Fit thresholds measured on the real faces: the loop-opener holds one
  line at >=1109px, the blockquote at >=893px; below those the block
  register governs by rule (R3 applying, scratch item 11). The
  wrap-free floor for the mobile strophes is ~360px; below it lines
  re-wrap by designed degradation.
- Brandon's working pattern for this build, held across seven passes:
  gated passes with a commit, captures, a report with the three
  registers (excluded by canon, excluded by judgment, reconsidered and
  admitted), then a full stop for his review. Supersessions of ratified
  decisions go in the amendments section of the decisions record; the
  record itself stays verbatim.
