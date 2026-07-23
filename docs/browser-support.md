# Browser support — what was tested, on what, and where the boundary is

Written 2026-07-23 at handoff. The track (`track/`) is a scroll-driven
build with a vendored scroll driver (Lenis 1.3.8, pinned, byte-identical
to the npm dist). Whoever deploys it inherits a scroll dependency; this
document states the tested edges so they are known rather than
discovered.

## What was tested

**Rendered geometry (gate 5).** Playwright Chromium, WebKit, and Firefox
— three engines, four widths each: 1440×900, 1280×800, 390×844,
375×812. Checked per cell: real font binaries loaded, zero unplanned
line wraps, column geometry constant, no horizontal scroll. All twelve
cells clean (refs/notes/pass-7-gate5-cross-engine.txt). This is
**settled-state geometry**: each cell is a rendered page measured at
rest, not a scroll session.

**Scroll-position sampling.** The scrub events (the wipe, the re-reveal,
the pin, the coda close) were verified as scroll-keyed frame sequences
(`npm run scrollframes` / `timeframes`): the page is placed at a series
of scroll positions and each is captured settled. This proves the state
at every sampled position; it does not exercise continuous scrolling.

**One real device.** iPhone (Safari, iOS), the device pass 2026-07-23:
real touch scrolling through the full page, the coda in both stances
(scrubbed close and, under Reduce Motion, the placed close), the
still-layer opacity on OLED, seam crispness at dpr 1, the departure tail,
the story size in the hand. This is the only continuous-scroll,
real-input verification the build has.

**Firefox font-timing.** The stale-ch race is fixed and verified 12 of
12 Firefox desktop loads with no harness intervention
(refs/notes/g3-stale-ch-fix.txt).

**Degradation paths.** Font-hang (gate 8): complete render at the 5s
ceiling, wordmark immune via the inlined subset. No-JS and
reduced-motion paths render the placed close by construction (the
enhancement inversion, docs/codified-patterns.md). SE-class geometry
(375×667) verified emulated, including the 2026-07-23 seen-frame hero
fix.

## What was NOT tested

- **Scrolling behavior over time on any desktop engine.** No desktop
  browser has run the track under continuous real input — wheel
  momentum, trackpad glides, interrupted flicks, scroll during the pin.
  The Lenis driver, the pin hand-off, and the wipe seam under motion are
  verified by position sampling and by one phone, nothing else.
- **Desktop Safari, at all.** Playwright WebKit is not desktop Safari:
  different scroll path, toolbar dynamics, and compositor behavior. The
  still-layer wipe depends on compositor paint order, which makes
  desktop Safari the highest-risk untested surface in the build. Test it
  before ship.
- **Intermediate widths as a sweep.** Between the tested widths only
  specific thresholds were measured (the loop-opener holds one line at
  ≥1109px, the blockquote at ≥893px, the mobile wrap-free floor at
  ~360px, the 800px strophe switch, the ≤720px-height hero compression).
  No continuous width sweep was run.
- **Landscape phones and tablets.** The device pass was portrait; no
  tablet was tested in any form.
- **Engine versions.** One pinned Playwright version per engine plus one
  real iPhone. No version matrix, no older engines.

## The boundary, stated plainly

Supported means: the twelve gate-5 cells at rest, the sampled scrub
positions in three engines, and one real iPhone end to end. Everything
outside that — above all desktop Safari, and continuous scrolling on any
desktop — is **unverified**, not broken and not designed-for-failure.
The degradation paths (no-JS, reduced-motion, font-hang) are the safety
net and are verified by construction; an engine that mishandles the
scrub still has a complete, readable, canon-clean page underneath it.

First checks for whoever ships: desktop Safari through the wipe (P6→P7)
and the re-reveal (P9→P10), the pin under real trackpad momentum, and
the coda's end-anchored scrub against toolbar dynamics.
