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
    adherence font lists (same face, same cut, not a third Latin face).
3c. **Rise-origin letter vs realization** (pass 3 verification note):
    typography.css describes the origin as "120% of the padded clip";
    CSS translateY percentages resolve against the mover's own line box,
    which is what ships. Pixel probes confirm zero ink above the clip
    pre-rise at every step, but the clearance at display scale is a few
    pixels, not the margin the comment implies. Doc-letter looseness
    inherited from the reference measurement; revisit only if a face or
    leading retune ever eats the clearance.

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
   offsets, hard 1px cut); on-device verification remains at gate 7.
6a. **P9 carries provisional entrances** (pass 3): eyebrow and headline
    per the spec; the band (a plain fade) and the two body blocks are
    placeholders that pass 4 replaces with the pin, the scrub-keyed
    stripes, the timed labels, and the release-announcing body.
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
    the static stance is the CSS default (zero-JS safe) under a dedicated
    coda class the stacking-invariant check will whitelist by exact
    selector; track.js opts into the scrubbed stance only when motion is
    permitted.
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
    behavior.
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
