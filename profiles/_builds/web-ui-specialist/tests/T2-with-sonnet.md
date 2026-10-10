# T2: Pinned, scroll-scrubbed hero, word-by-word assembly

**Verdict: not as specified. Do not build the pinned scrub. Direct the admitted alternative.** Evidence is the system's own governing doc; nothing was rendered, so geometry is not rated.

## Findings

1. **"Premium" is an adjective, not a brief (C13, A5).** It names no load the motion carries. Motion is judged by the earn test: does it carry something static cannot (R4, M5)?

2. **Earn test, run (R4).** Remove the motion: the hero line reads in full, and the hero's job (orient, open the argument) is intact. A word-by-word assembly adds ceremony, not information. The argument survives without it, so it is decoration.

3. **The system already decided the hero (`company/brand/design-system/docs/structure-motion-decision.md`, sections 3, 4).**
   - P1 hero: the display sentence rises line by line, timed, clip-rise, 260ms lines, 80ms stagger, fires once. That is the hero's choreography and it teaches the motion vocabulary.
   - Two-system split: travel is scrubbed, text is timed. "Text must finish (a half-scrubbed sentence is unreadable)." A scrubbed word-by-word line puts text on the scrub side. That reverses a ratified rule, and a customer who stops mid-scroll reads a broken sentence.
   - Pins: one bounded pin exists, the daypart band. "No other pin, no other scrubbed set piece"; "A second pin anywhere" is on the excluded register. A pinned hero is a second pin.

4. **Scroll control spent (R5, M7).** A pin takes the first screen of a warm, forwarded reader, mostly on a phone. A customer inside a pin can believe the page ended or is stuck. The decision doc also drops the mobile hard pin. The finding names the control spent: scroll position and pace on the first panel.

5. **Implementation (M17).** Any per-frame script keeping the word reveal and scroll position in sync is rejected. Use sticky geometry and observers.

6. **Reduced path (R6, M15).** Not designed in the ask. Required: no pin, the full line present, opacity only, nothing hidden until scrolled (R7). Every word must be legible and focusable-safe static.

7. **Fonts (decision doc section 3).** Display choreography must not fire on unloaded fonts; the arrival state guarantees it.

## Directed fix (not written here)

- Keep the existing P1 line-by-line timed clip-rise. First fix: build that, check it on a real phone with `timeframes` and `scrollframes`.
- If word-level stagger is wanted inside the line, it is a change to a ratified spec: it needs a per-beat earn argument and Brandon's ruling. It stays timed, not scrubbed, and never pins.
- If the real aim is "feel premium," name the load: restraint, weight, held space, one clean entrance. Those come from type scale, measure, and spacing (C2, C4), not scroll mechanics.

## Flags

- Motion authority conflict (M13): `structure-motion-decision.md` governs, `docs/motion-spec.md` is superseded, and whether `track/` is the public site is unconfirmed. Flagged for Brandon, not ruled.
- A pinned scrub would break a ratified decision: Brandon, before any build.

## Open questions

- Which surface is this hero: the track's P1, the reservation site, or a new page? A new surface with no brief goes to `design-brief-translator`; the point of view goes to `creative-director`.
- Evidence owed: `npm run lint`, `shoot`, `scrollframes`, `timeframes`, and a real-phone frame-rate check (session or Brandon).
