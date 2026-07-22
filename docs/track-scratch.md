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
10. **The placed close** (settled at gate B review, 2026-07-21; built at
    pass 6, which owns the path). The reduced-motion and no-JS coda cannot
    end on the fixed layer at full opacity: with no scrub to carry the
    footer out, a hard cut anywhere the footer is framed produces content
    over the mark at full opacity, the balance-spec violation, and the
    88vh centered glyph leaves no viewport frame where footer and mark
    coexist clear of each other. Separation must therefore be sequential
    in LAYOUT: the static coda is a two-frame flow composition. Frame one,
    the footer (lock-up, location line). Frame two, the closing glyph at
    full opacity, a panel-local placed instance of the drawn path,
    centered in P11's final viewport height. In this stance P11 occludes
    the resting layer the way daylight panels do, so the page still ends
    on the glyph frame and content can never overlap the mark, by
    document order. Named cost: in this path the closing mark is a placed
    instance, not the layer itself; R1's "the bare glyph is the layer" is
    the scrubbed path's sentence, and the spec's P11 reduced-motion line
    amends when pass 6 builds it. Mechanically: the static stance is the
    CSS default (zero-JS safe) under a dedicated coda class the
    stacking-invariant check will whitelist by exact selector; track.js
    opts into the scrubbed stance only when motion is permitted.
11. **The two unmeasured locked lines** (pass 1 verification). The type
    decision fit-measured only the hero Display and Solo strophes. The
    other two locked single lines were measured at pass 1 on the real
    faces: the hero loop-opener holds one line only at viewports 1109px
    and wider (two lines through the whole tablet range, three below
    ~440px); the P6 blockquote holds one line at 893px and wider. Both are
    single lines at the mandated 1280 and 1440 checks. Whether the locks
    are desktop-band-only (with block rises below) is a pass-3 mechanics
    question sitting on Brandon's composition review of this pass.
12. **Mobile chrome drops the access note** at 640px and below, carried
    verbatim from the settled site component; build-spec §2.4 says three
    elements and does not record the mobile drop. Surfaced for
    ratification or reversal; the string stays in the DOM and "By request
    only." recurs in the coda location line on every viewport.
13. **Coda scrub anchoring, the recorded cost** (gate B verification). The
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
