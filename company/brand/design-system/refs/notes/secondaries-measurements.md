# Secondary sites, raw measurements

Sites: hobro.digital, creativeglu.ai, matteprojects.com. Landing surface only, one
pass each. Captured 2026-07-19. Method: in-app DevTools browser, JS evaluation against
the live page, computed styles and DOM counts. In-app browser default viewport (pane
reported innerHeight 450 to 720, width ~800 to 1280). Display font sizes are responsive,
so absolute px below are measured at that viewport and read as ramp relationships, not
fixed values. This note is the evidence log. The write-up lives in docs/reference-spec.md.

## Shared structural fact (measured)
All three are a single continuous vertical-scroll page under one URL. No per-section
route, no per-section preloader gate, no wheel-to-horizontal remap.
- hobro.digital: document scrollHeight 15835px.
- creativeglu.ai: document scrollHeight 9902px.
- matteprojects.com: document scrollHeight 10063px.
Contrast: the primary is twelve named Nuxt routes, each a horizontal track of 7 to 11
panels, each re-showing a "Start the experience" gate.

## hobro.digital (measured, from window globals and computed style)
- GSAP 3.12.7 (window.gsap.version, window.gsapVersions). ScrollTrigger present and
  reachable. ScrollSmoother loaded but ScrollSmoother.get() returns none (not active).
  Lenis constructor present (window.Lenis, proto has setScroll/on/off/destroy) but the
  instance is module-scoped, not on window. So smoothing is Lenis, effects are GSAP
  ScrollTrigger, and unlike the primary the GSAP core is reachable.
- ScrollTrigger.getAll() = 116 triggers. Breakdown (measured t.vars):
  - scrub true: 1
  - scrub numeric: 52 (51 at scrub 0.3, 1 at scrub 1) = time-lagged / eased scrub
  - scrub false: 63 = on-enter toggles (timed timelines, durations set in GSAP, not CSS)
  - pinned: 0
  Triggers seen: cta__lottie, lazy-lottie, feature__frame feature-content-js.
- Grounds (computed backgroundColor, most common first): rgb(0,0,0) pure black x189,
  rgb(255,255,255) white x28, rgb(221,221,221) x4, rgb(0,251,150) green #00FB96 x1.
  Pure black, not the primary's soft #161616. Green is a spot accent, not a ground.
- Type (computed, largest first, measured at pane viewport):
  - Kamerik205 700 uppercase: "We" 160px / lh 140.8px (0.88), ls -1.6px
  - FreigBigProLigIta 300 uppercase italic ("title--cursive"): "What" 193.3px / lh
    170.1px (0.88), ls -1.93px; "Fresh" 66.7px
  - PPNeueMontreal 400/500: footer numbers 80px, cta__text "Got Project?" 53.3px 500,
    body/labels 16px
  Three display faces, weight contrast 700 vs 300, a light italic serif for emphasis,
  and negative tracking that grows with size (-1.6 to -1.93px). Line-height ~0.88
  (computed from lh/fs).
- Reveal: large type split into ".line" elements (line-based reveal).
- CTAs: persistent "GET CAPABILITIES DECK" in the header chrome; terminal "Got Project?"
  block near the footer.
- Preloader: black gate with a "LOADING..." progress bar. Did not clear in the in-app
  browser during the pass (body class stayed "loading first-load"); DOM content was fully
  present and measurable behind it. Motion runs client-side and is invisible to a static
  markup read, as the brief anticipated.

## creativeglu.ai (measured)
- No GSAP, no ScrollTrigger, no Lenis, no ScrollSmoother, no CSS scroll-timeline
  (animationTimeline auto everywhere, 0 scroll-driven). Next.js / React (body class
  carries next/font module names). Native browser scroll, no smoothing library.
- Fonts: Inter (sans) + Geist Mono (mono), via next/font.
- Hero: a canvas fixed at top:0 left:0, full viewport (1280x720), iridescent sphere.
  WebGL (document canvas present; THREE not global). Persists behind content, animates on
  its own time base (not scroll-linked).
- Custom cursor: cursor-magnifier, cursor-dot, magnifier-lens, magnifier-ring elements.
- Reveal: opacity 0 elements carry timed CSS transitions, measured transitionDuration
  0.7s and 1s with cubic-bezier(0,0,0.2,1) (ease-out). On-enter timed, nothing scrubbed.
- Ground: one continuous dark field. Computed grounds oklab(0 0 0 / 0.95) and
  rgba(0,0,0,0.09). Modern color space (oklab/lab), near-black. No three-value swap; the
  WebGL object carries the variation.
- Type (computed, measured at pane viewport): Inter 700 hero "The future is yours to
  create" 72px; Inter 500 subheads 48px, 36px "STRATEGY", 32px; Inter 400 body. Weight
  ramp 400/500/700, single family plus mono accent, letter-spacing normal.
- CTAs: persistent "Partner With Us" in nav; repeated inline "Start the Conversation",
  "Accelerate Your Path To Mastery", "Explore AI Transformation" between content blocks;
  an FAQ accordion of question buttons near the end.

## matteprojects.com (measured)
- Lenis 1.1.13 (window.lenisVersion), older than the primary's 1.3.8. No GSAP, no
  ScrollTrigger, no canvas. One hero <video> (autoplay, time-based). Instance not on
  window (module-scoped), config not readable.
- No CSS scroll-timeline (0 scroll-driven), no ScrollTrigger. Reveal: opacity 0 elements
  carry transform matrix(1,0,0,1,0,10) = translateY 10px, revealing to opacity 1 and 0
  offset on enter (fade plus short rise). Transition applied at reveal time (measured
  transitionDuration 0s at rest). Inferred not scrub-led: no scroll-driver instrumentation
  found, only Lenis smoothing the native vertical scroll.
- Grounds (computed backgroundColor): rgb(241,241,241) light grey (dominant), rgb(129,129,129)
  mid grey, rgb(29,29,29) near-black, rgb(244,244,244), plus white and black. A greyscale
  system, no chromatic accent. The only light-grounded secondary.
- Fonts in use (count of elements): Syndicat Grotesk x216, RM Mono x250, Cormorant
  Garamond x11. A grotesque for structure, a monospace used heavily for labels and
  metadata (e.g. bracket labels "[ WHO WE ARE ]"), a light serif for display.
  Display measured: Cormorant Garamond 300 uppercase "Let's Get Creative" 75px / lh 90px
  (1.2), ls -0.4px. Body/label p: RM Mono 700 16px.
- Structure: named column grid ("site-grid", "col-span-6 800:col-..." with an 800px
  breakpoint), mono bracket labels as section markers.
- CTAs: nav Menu with Projects/Community/About/Careers/Contact; inline "View All Work",
  "About Us", "Matte Films".
- Cookie banner rejected (Reject All) per privacy default. Google-analytics-style consent.

## Bearing on the routed-versus-continuous question (primary section 5/7)
All three secondaries are continuous single-page scroll under one URL with no routing and
no per-section gate. That is the continuous model, but none uses the primary's per-chapter
Nuxt routing or its horizontal-track-per-chapter construction, so none is evidence for how
the primary chains its routed horizontal chapters. They are a contrast, not a resolution.
The primary question stays open and is left open in the spec.
