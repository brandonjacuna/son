# Track build scratch

Status: scratch, not system. Anything the build invents lands here first.
Codification into the design system is a later gate and it is Brandon's to
open. Started at gate pass A, 2026-07-21.

## Invented, in use

1. **`scripts/scrollframes.mjs`** — scroll-travel evidence tool. Captures a
   seam crossing (or an explicit scroll range) as numbered viewport frames,
   both device widths, frame names carrying the actual settled scroll
   position. Built because a still capture cannot demonstrate a wipe.
   Verification hardened: clears its output directory per run, names frames
   by actual rather than requested position, warns on clamp, drift, partial
   crossings, and duplicate frames.
2. **Paint-order occlusion as the wipe implementation.** The spec's
   "seam-tracked clip on the fixed layer" (build-spec §2.2, a build detail)
   is realized by stacking order rather than a scripted clip-path: still
   layer fixed at z-index 1, daylight panels position relative z-index 2,
   dark panels unpositioned. The daylight ground clips the layer at exactly
   the moving seam in the compositor, zero per-frame script, no lag between
   seam and clip by construction. Spec §1 item 2 already names occlusion as
   the wipe; this is that sentence made literal.

2b. **Sticky-in-wrapper as the pin realization** — RATIFIED by Brandon
    2026-07-23 (pass 4 review), on the same grounds as paint-order
    occlusion: position sticky inside a wrapper one pin-distance taller
    than the panel engages and releases by construction rather than by
    script, so the pin cannot desynchronize from the scroll it tracks.
    Second of the build's remove-the-failure-class mechanisms.

## Enforcement in use, ruled at gate A

3. **The stacking-context invariant as an adherence check** — written at
   Brandon's direction (2026-07-21, gate A review): enforcement of an
   invariant the build already depends on is the same class as the copy
   pass, not a new pattern entering the system. `adherence/check-track.mjs`
   fails lint when body, the track, or a dark panel gains a
   stacking-context-creating property; guarded by selector subject so
   positioning content inside a panel stays legitimate; daylight panels
   exempt. Static CSS only; the same invariant binds track JS by review.

3a. **`scripts/timeframes.mjs`** (pass 3): timed-sequence evidence tool.
    Scroll frames show scrub-keyed travel; this captures TIMED choreography
    (the arrival, panel entrances) as viewport frames on an interval from
    load, actual elapsed ms in each filename. Same conventions as
    scrollframes: fresh output per run, both devices.
3b. **The wordmark subset realized** (pass 3, build-spec §2.3 detail):
    GT Sectra Fine subset to S, n, ŏ with fonttools, 880-byte woff2,
    inlined as a data URI under its own delivery name, "GT Sectra Fine
    Arrival", first in a track-scoped mark stack that contains NO loading
    face. Two probe-verified engine facts forced the shape: same-family
    unicode-range shadowing loses to a loading full face regardless of
    declaration order, and a pending face ANYWHERE in a stack blocks the
    whole run's paint. A token amendment (subset-first in
    --son-font-wordmark) was tried, proven insufficient by the second
    fact, and reverted: the token's letter is unchanged, the mechanism is
    scoped to track.css, and the delivery name is allow-listed in both
    adherence font lists. RULED 2026-07-22: the face limit holds; a
    three-glyph subset of a face already on the page adds no typographic
    voice, the same class as the drawn 선 path. THE WATCHED DOOR, stated
    so it cannot be missed: the violation is not the name "GT Sectra Fine
    Arrival" existing. The violation is that name ever gaining a glyph
    beyond S, o-breve, and n, or being used on any element that is not a
    mark.
3c. **Rise-origin letter vs realization** (pass 3 verification note):
    typography.css describes the origin as "120% of the padded clip";
    CSS translateY percentages resolve against the mover's own line box,
    which is what ships. Pixel probes confirm zero ink above the clip
    pre-rise at every step, but the clearance at display scale is a few
    pixels, not the margin the comment implies. Doc-letter looseness
    inherited from the reference measurement. RULED 2026-07-22: leave the
    behavior; record the comment rewrite as a doc fix for the codification
    gate. Revisit the value itself only if a face or leading retune ever
    eats the clearance. EXECUTED at G3 (2026-07-23): the typography.css
    comment now states the line-box resolution; closed.

3d. **The card holds its height on the live swap** (pass 5 verification; ruled 2026-07-23).
    On viewports where the form pushes P10 past its svh floor, the in-card
    swap shrank the document under the reader: scroll shifted and the
    coda's end anchor staled, stalling the converted close at 0.55. Ruled
    consistent with Decisions 16 and 18: the interior swaps, the geometry
    does not; the card freezes its block size when the swap is an event,
    takes natural height when it is a load condition, the announcement
    focus never nudges scroll, and the scrub anchors re-measure after any
    swap. Probe: document byte-stable, swap-caused scroll shift zero,
    converted coda exactly 1.

3e. **The focusin armer** (pass 6, 2026-07-23): focus arriving inside an un-entered
    [data-enter] element arms it immediately, so a keyboard reader can
    never focus invisible content (A2 inside the unreleased model body is
    the live case; probe-verified at both widths). Accessibility outranks
    choreography; fire-once semantics hold.
3f. **THE ENHANCEMENT INVERSION** — a pattern, not an implementation
    detail (named at Brandon's direction, 2026-07-23; CODIFICATION
    CANDIDATE). The designed second path is the default and the full
    experience is the opt-in: the scrubbed track exists only under
    html.track-motion, set when JS runs and motion is permitted, so the
    reduced path can never be broken by a failure to enhance. Fourth
    mechanism in this build that removes a failure class by construction
    rather than managing it (paint-order occlusion, sticky-in-wrapper,
    the label floor, this).
3g. **Method notes: the false-reading probe traps** (recorded at
    Brandon's direction, 2026-07-23; the class that produced the previous build's
    phantom failures). One: unfocused outline-color computes to
    currentColor, so ring contrast must be measured WHILE focused. Two: a
    ground probe that walks ancestor backgrounds reads through a
    transparent list item to the panel behind it; measure the pseudo fill
    that actually paints. Three, same family: differential occlusion
    probing by hiding a layer false-positives on compositing-collapse
    re-anti-aliasing; measure by paint-boost (force the layer loud),
    never by removing it.

3h. **The confirmation renders where the act happened** — RULED by
    Brandon 2026-07-23: on the live swap the line lands where the submit
    control stood, so the reader who just acted sees the response in
    their standing view; the empty card around it is the isolate, taught
    three panels earlier, and nothing fills it. The load-rendered state
    keeps natural placement: a returning reader arrives at a state, not a
    change. Evidence: refs/shots/pass-6-confirmation-placed, both widths.
    AMENDED 2026-07-23 (build-spec §7 amendment 10), with the reason, not
    replaced: the ruling was right for the case it was made from — the
    mobile reader's standing view — and wrong in scope, because a line in
    the card's lower third with empty field above is a composition the
    site never established (the isolate is content CENTERED in a field),
    and at desktop the whole card is already in view, so the reason for
    low placement is absent and only the odd composition remains. The
    placement now measures its reason per swap: centered at the isolate's
    optical seat when the centered line lands in the visual viewport, the
    act's position otherwise, degrading to the act when the visual
    viewport is unavailable — the safe case, not the elegant one.
3i. **The revealed header, built at final review** (2026-07-23). Ratified
    Decision 7 was deferred at pass 1 as "a motion pass" and never
    assigned to one; the final review caught it unimplemented. Built
    carrying the settled header (fixed, 2px direction hysteresis, hidden
    by transform at the ~300ms chrome-hide token, focus always reveals)
    with the track's ratified amendment: past the hero the bar is solid
    in the ACTIVE panel's ground and theme, swapped as a hard cut like
    the seams; never suppressed during the pin. Process lesson, recorded:
    a settled behavior with no pass assignment is a silent omission
    class; the final review is the net, but the pass plan should name an
    owner for every settled behavior up front. The build's own first cut
    then violated the inversion (an ungated fixed stance broke the no-JS
    header); caught by the header verification and re-gated under
    html.js, no-JS default restored to the hero-frame absolute chrome.
    Two carried semantics recorded: scrolling down with focus inside the
    bar re-hides it with focus still inside (verbatim v3 behavior; Enter
    still fires; focusin re-reveals), and a hash jump clicked mid-glide
    is retargeted so the driver cannot yank the page back (the settled
    instant-jump ruling held against the driver).
3j. **The skip-link door** (pass 6 register, written down 2026-07-23): a
    skip link was excluded by judgment at seven keyboard stops with
    scroll keys free; the door reopens if the stop count ever grows.
3k. **Probe traps, continued** (pass 8, the register probe; the 3g
    class): a FontFaceSet check is load-level, not render-level — a
    stale ch basis can hold fallback geometry in layout after the face
    reports loaded, so gate the RENDERED basis with a ch ruler (the
    real face measures 9.12px/ch at 16 on GT Alpina Fine; the fallback
    ~9.82). Firefox may never re-resolve ch-based max-width after font
    load: flush styles before measuring, and DETECT the stale state as
    a logged note rather than archiving its geometry (the build's own
    first evidence file carried fallback rows under a passing verdict).
    getComputedStyle fontFamily reports the cascade, never the rendered
    face. A reported metric with no assertion attached is not evidence.
3l. **The zero-band seat observer** (pass 9, the amendment 6
    realization): an IntersectionObserver with rootMargin
    "0px 0px -100% 0px" collapses the root box onto the viewport's top
    edge, so a panel first intersects exactly when its top edge seats —
    seat-firing by geometry, no scroll math, engine-verified on all
    three (unarmed 6px before seat, armed at seat). Same
    remove-the-failure-class family as paint-order occlusion and
    sticky-in-wrapper: the firing point cannot desynchronize from the
    scroll it tracks. Fire-once; disconnected with the main observer on
    the font-hang path.
3m. **The invisible-edge lesson** (pass 9, caught at frame review):
    between same-ground panels the panel edge does not render, so
    anti-page-end analysis must run on VISIBLE content — the window
    from one text's exit to the next text's entry — never on box
    geometry. The pass's first probe asserted "P4's edge enters before
    the couplet exits," true of boxes and vacuous of frames; corrected
    to the glyph-alone window (17-25svh phone, ~31svh desktop at the
    40svh tail), with the rest-opacity hold as the ending-grammar
    assertion.

## Notes for later passes

4. **Pass 1, body ground.** With no theme on body, the document ground
   behind the panel stack resolves to Bone (base editorial). Invisible in
   travel, but macOS rubber-band overscroll above P1 would flash light over
   a dinner opening. Theme the body ground with the hero's chapter when the
   hero lands.
5. **Pass 2 on, deterministic capture.** scrollframes settles 140ms per
   frame, below every timed register (blocks 500ms, lines 260ms, chrome
   400ms), and fire-once entrances make a frame depend on scroll history.
   When Lenis and entrances exist, capture under reduced-motion emulation
   (the designed second path: entrances instant, native scroll) or an
   adaptive settle. Deferred now: the scaffold ships zero JS.
6. **Capture dpr.** shoot and scrollframes capture at deviceScaleFactor 2.
   Seam crispness at dpr 1 was probe-verified this pass (integer seam
   offsets, hard 1px cut); on-device verification belongs to the same
   device session as gates 3 and 4 (repointed 2026-07-23; the earlier
   "gate 7" reference was dangling).
6a. **P9's entrances resolved at pass 4**: eyebrow and headline enter with
    the panel; the stripes are scrub-keyed to the pin (or the viewport
    passage on mobile); labels and body are data-enter-manual, fired by
    the band controller. Capture caveat, same class as the fixed-layer
    note in item 6: shoot's full-page render evaluates scrub state at
    scroll 0, so its P9 slice shows entered labels over an unbuilt band, a
    composite no reader sees. The scrollframes sequences (pass-4-pin,
    pass-4-band, pass-4-release) are authoritative for the band.
6b. **No pin without JavaScript** (pass 4 verification): the pin exists
    only under html.js. A no-JS reader has no build to hold for; the
    default is the complete band in normal travel, mirroring the reduced
    path. The pin wrapper is guarded by the invariant check (a stacking
    context on it would capture P9 below the still layer).
6c. **The label floor** (ruled 2026-07-23): the deep scrub-back state
    where Bone labels sat invisible over emptied stripes was a contrast
    failure produced by scrubbing, not the spec's "text never un-enters"
    cost. Fix: once a label has entered, its stripe's build floors at the
    label's own rendered extent, so the field never withdraws beneath
    entered text. No mixed-contrast crossing state exists at any scrub
    position; the empty footprint before first fire is untouched; the
    entered day keeps its name on its field. Evidence:
    refs/shots/pass-4-scrubback at both widths.
7. **`range=` mode is device-blind.** An explicit scroll range applies
   verbatim to both devices though document geometry differs per width; use
   `seam=` or `seat=` (per-device resolution) for anything that must hold
   on both.
8. **`seat=` capture mode** (gate B): frames from an element seated (top
   edge at viewport top) to the end of the document travel; built for the
   coda close, reusable for any seated-to-end sequence.
9. **Coda travel distance.** `CODA_TRAVEL_VH = 80` lives in track/track.js
   for the gate; it moves into tokens/motion-track.css at pass 2 alongside
   the pin distance, per build-spec §2.7. The 180svh panel height in
   track.css encodes the same 80 (180 minus the 100svh seat frame); the
   pass-2 tokenization closes both so they cannot drift apart.
10. **The placed close** — ACCEPTED by Brandon 2026-07-22 as a design
    answer, not a fallback: the reduced-motion and no-JS coda is its own
    composition, designed for its own conditions. A path with no scrub
    cannot carry the footer out past the mark, and the 88vh centered glyph
    leaves no viewport frame where footer and mark coexist clear of each
    other, so the separation is sequential in layout: a two-frame flow
    composition. Frame one, the footer (lock-up, location line). Frame
    two, the closing glyph at full opacity, a panel-local placed instance
    of the drawn path, centered in P11's final viewport height. P11 in
    this stance occludes the resting layer by document order, the way
    daylight panels do, so the page still ends on the glyph frame and
    content can never overlap the mark. Named cost, recorded: the closing
    mark here is a placed instance, not the layer itself; R1's "the bare
    glyph is the layer" is the scrubbed path's sentence, and the spec's
    P11 reduced-motion line amends when pass 6 builds it. Mechanically:
    the static stance is the CSS default (zero-JS safe) under the
    dedicated class .panel--placed-close (applied as
    .panel--coda.panel--placed-close), exempted in the stacking-invariant
    check by class subject, the same latitude as the daylight exemption
    (letter amended 2026-07-23 to match the probe-verified realization;
    bare .panel--coda stays guarded per the gate B hole-closure); track.js
    opts into the scrubbed stance only when motion is permitted. BUILT at
    pass 6.
11. **The two unmeasured locked lines** (pass 1 verification). The type
    decision fit-measured only the hero Display and Solo strophes. The
    other two locked single lines were measured at pass 1 on the real
    faces: the hero loop-opener holds one line only at viewports 1109px
    and wider (two lines through the whole tablet range, three below
    ~440px); the P6 blockquote holds one line at 893px and wider. Both are
    single lines at the mandated 1280 and 1440 checks. RULED by Brandon
    2026-07-22: desktop band only, block rises below threshold — recorded
    as the existing R3 rule applying, not a new ruling. Per-line rises
    were admitted only on locked strophes, and below 1109px (loop-opener)
    and 893px (blockquote) those breaks are not locked, so the block
    register governs. Pass 3 implements the band switch.
12. **Mobile chrome holds three elements** (Brandon, 2026-07-22: do not
    carry the v3 drop on inheritance; the access note is what makes the
    shortcut read as privilege rather than a sales button, and mobile is
    the majority surface, so the reduced case is the main case). Built at
    pass 2: below 640px the chrome's right block stacks, access note over
    A1, right-aligned — the note frames the shortcut at exactly the point
    the reader might use it. Shown at 390 for review; if it costs more
    than it buys, the drop reopens on evidence.
13. **Reduced motion does not zero delays globally** (pass 2 verification,
    the retirement's sharpest catch). The retired immersive register's
    kill rule zeroed transition-delay in its scope; the global kill in
    tokens/spacing.css zeroes durations only. The v3 site's carried block
    now restores its scoped delay kill. NAMED REQUIREMENT for the track:
    when pass 3 lands staggered entrances, the track's reduced-motion path
    must zero its delays explicitly (entrances instant means duration AND
    delay); pass 6 owns the designed path, pass 3 must not ship staggers
    that survive reduced motion even for a pass.
14. **Generated artifacts, standing regeneration item** (pass 2). The
    retirement leaves _ds_bundle.js and _ds_manifest.json embedding the
    retired register (immersive components referencing dead tokens and
    keyframes; the manifest's token table still lists --son-imm-*), and
    _adherence.oxlintrc.json still allowlists --son-imm-*. No regeneration
    path exists in the repo (the compiler is external, per the readme).
    The one 404-causing edge, the manifest's globalCssPaths pointing at
    the deleted stylesheet, was hand-patched to motion-track.css; the rest
    waits for regeneration. The immersive components themselves degrade
    gracefully on their own fallbacks (verified per component: drift and
    marquee static, takeover hard-cuts, kinetic and section-header arrive
    instant, the AmbientField glyph module unreachable without
    --son-glyph-motion); their retirement or rework is Brandon's
    codification call, and their prompt docs still describe pre-retirement
    behavior. RULED at G3 (2026-07-23): formal retirement. The nine
    prompt docs carry superseded banners, the components drop from the
    bundle at the next external regeneration, and the readme records it.
    G3's graduated rules live in docs/codified-patterns.md; this file
    stays the archaeological record.
15. **Coda scrub anchoring, the recorded cost** (gate B verification). The
    scrub is end-anchored: the close is the last ~80vh of document travel,
    measured in innerHeight units, while panel geometry is svh. On
    dynamic-toolbar phones (innerHeight grows past 1svh once chrome
    collapses) the scrub therefore begins up to ~1.8x the toolbar delta
    BEFORE the seat point. End-anchoring is correct and necessary: a
    seat-anchored window mathematically never reaches full opacity on a
    collapsed-chrome phone, and the final-frame guarantee is the gate.
    Felt effect reviews at build gate 3 (phone coda on device); the pass-2
    tokenization decides which unit the 80 is 80 of. Exact at both capture
    viewports (seat and scrub start coincide to the pixel).
