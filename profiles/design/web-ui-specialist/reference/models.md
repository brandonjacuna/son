# Models and distinctions

Read when explaining a verdict or ranking many valid findings.

- M1. Web is judged as built. The surface is the discipline closest to code, so the verdict is on what renders, not on the drawing.
- M2. Made decision or statistical default. Every tell gets one of the two labels, in formal vocabulary (measure, proximity, register, hierarchy), never aesthetic adjectives like clean or minimal. Competent and generic is a failure, and the seat says so.
- M3. Sections are a scripted argument. At each scroll position the customer understands something and something is withheld to create forward motion; emphasis pauses where the argument needs weight.
- M4. Proximity carries meaning. Tighter grouping signals relationship, isolation signals emphasis, deliberate emptiness creates weight. Uniform spacing answers to none of these.
- M5. The earn test. The question is not whether motion helps but whether it carries load nothing else carries. A good narrative surface still makes sense static; removing the scroll should collapse the story if the motion was load-bearing.
- M6. Motion is a cost the customer pays in performance, attention, and time. The gate is whether removing it loses information or context.
- M7. Scroll is borrowed control. Pinning, snapping, damping, and parallax spend it; a customer stuck in a pin believes they reached the end of the page.
- M8. Two registers. Feedback motion reports a state change; narrative motion must carry load static cannot. Narrative motion never touches the ask.
- M9. Reduced means reduced, not none. If you cannot name what is lost without the motion, it was decoration and the earn test already failed.
- M10. Checks and evidence are different instruments. `npm run lint` blocks on stylesheet, copy, track stacking, and JSX rules; it does not see rendered geometry, scroll behavior, or visual judgment. Those need `npm run shoot`, `scrollframes`, `timeframes`, and a physical device.
- M11. Unverified is not broken. A browser and OS cell the design system has not tested is reported as unverified.
- M12. Severity ladder. Foundational: an accessibility or data gate, an earn-test failure, no system, convergence on the average. Structural: hero formula, default grid, metronomic spacing, uncapped measure, missing states. Surface: component tells, decoration. A finding that needs investigation is documented, not dismissed.
- M13. Motion authority. The frame calls inertia damping scrolljacking; the design system ships Lenis smoothing, a bounded pin, and scrub. `docs/structure-motion-decision.md` governs (ratified by Brandon) and covers the `track/` build, which the readme says is what ships. `docs/motion-spec.md` carries a "Superseded 2026-07-20" header and was written for the investor site, retired 2026-10-07; whether `track/` is the public site is unconfirmed and open for Brandon (`memory/state.md`). The seat cites both, flags a conflict, and does not rule.
- M14. Stacking contexts (R3). Dark panels, `html`, `body`, and `main` gain no stacking-context property in a design-system change; a `var()` there counts.
- M15. Reduced-motion details (R6). Narrative sequences pause on a static end frame with a play control. Self-starting motion (2.2.2) and interaction-triggered motion (2.3.3) are separate checks.
- M16. Payment fields (R10). They live only in the processor's hosted element or behind a redirect; anything else is flagged unverified to Brandon and counsel.
- M17. Scroll implementation (R5). Reject any per-frame script keeping two things in sync; use stacking, sticky geometry, and observers. Discrete steps get discrete controls, not a scrub (R4).
- M18. Gated content (R7). The fix makes the failing state the stylesheet default. An untested browser cell is "unverified", not broken; desktop Safari is untested (R9).
