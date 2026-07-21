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
   the pin distance, per build-spec §2.7.
