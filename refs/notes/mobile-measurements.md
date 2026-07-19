# Mobile translation, raw measurements

Captured 2026-07-19. Sites: lemansclassic.richardmille.com (/en, /en/night,
/en/podium), hobro.digital, creativeglu.ai, matteprojects.com.

Method. The named DevTools MCP (.mcp.json) was not present in the working
directory. In its place, Playwright (the project's own capture dependency, used
by scripts/shoot.mjs) drove a real device emulation, the "iPhone 13" descriptor,
which carries the touch flag, an iOS Safari user agent, and device pixel ratio,
not a resized desktop viewport. Touch gestures were driven through CDP
Input.dispatchTouchEvent, so swipe behavior is measured, not inferred. Values are
tagged measured (read off the live page), computed (arithmetic on measured
values), or inferred (concluded from indirect evidence, evidence stated). This
note is the evidence log. The write-up lives in docs/reference-spec.md section 8.

refs/clips/ held no phone capture this session (only .gitkeep), so no decomposed
clip fed the touch question. It was answered by gesture driving and code, both
measured.

## Device profile (measured, read on-page)
- userAgent iOS 15 Safari (…Version/26.5 Mobile/15E148 Safari/604.1)
- navigator.maxTouchPoints 1, "ontouchstart" in window true
- matchMedia (pointer: coarse) true, (hover: none) true
- devicePixelRatio 3, innerWidth 390
This confirms a touch device, not a narrow desktop, on every reading below.

## Primary, the horizontal track under touch

The horizontal scrub track does not survive. It collapses to a vertical scroll
column. Measured three ways:

- No track. An exhaustive walk of every element for a row-direction flex wider
  than the viewport returned 0 on all three routes (measured wideRowCount 0).
  document.scrollWidth 401 on /en, 390 on /en/night and /en/podium (measured), so
  there is no horizontal overflow to scrub.
- Gestures. A CDP vertical swipe moved window.scrollY 0 to 774 on /en, 0 to 966
  on /en/night, 0 to 1002 on /en/podium (measured). A horizontal swipe left moved
  scrollX to 11px, a rubber-band bounce, and left scrollY unchanged (measured). So
  touch drives vertical scroll only; a horizontal swipe advances nothing.
- Mechanism. A (max-width: 767px) media rule targets the w-max / flex-row /
  horizontal / a-parallax selectors; a (min-width: 1024px) rule and a
  (pointer: coarse) query also exist (measured, scanned from styleSheets). So the
  collapse is a width-breakpoint branch at 767px and below, reinforced by a
  coarse-pointer query. A narrow desktop viewport would hit the same width branch.
  The .-horizontal parallax modifier class is still in the DOM (measured
  horizParallaxModifier true) but its computed transform is none (measured), so
  the horizontal drift is disabled, not re-eased.

Lenis config is unchanged from desktop (measured window._lenis.options): orientation
vertical, gestureOrientation vertical, syncTouch false, lerp 0.1, duration 0.8. On
desktop the vertical wheel is virtualized into horizontal travel; on mobile Lenis
smooths the now-native vertical scroll.

Lost on collapse: the wheel-remapped horizontal traversal and the horizontal
parallax drift. Kept: the panels and their content, stacked; the timed reveals; the
ground system; the per-route gate. The chapter still reads as a vertical narrative.

## Primary, everything else (measured)

- Gate. Each route still shows its own gate: html carries lenis-stopped before
  entry on all three routes (measured), clearing to is-ready after clicking
  "Start the experience".
- Panels stack. getBoundingClientRect tops increase down the page (933, 1007, 1318,
  1411 … on /en), widths approx viewport (310 to 390). The c-about-panel and slide
  blocks lay top to bottom (measured).
- Ground. The three-value system persists on stacked blocks and swaps block to
  block down the column: white rgb(255,255,255), yellow rgb(255,229,0) = #ffe500,
  soft black rgb(22,22,22) = #161616 (measured backgroundColor on /en/night and
  /en/podium blocks).
- Chapter count unchanged: twelve routes, each gated (measured). Within-chapter
  panel count was not cleanly re-counted at mobile; the panel content is present as
  stacked blocks. Not asserting a per-chapter count change.
- Type ramp (measured font-size, computed ratios):
  - Display Arges-Condensed weight 400, letter-spacing normal, unchanged face.
  - Chapter-takeover letters 584px on /en, line-height 467.2px = 0.8 leading
    (computed 467.2/584), held from desktop's 640px / 0.8.
  - Section-title tier 241px (desktop text-9xl 256px).
  - Running-title tier 180px; a smaller running title 44.3px.
  - Body DieGroteskC 28 / 24 / 20px; .p1-scope body 20px (desktop .p1 21.6px).
  - Per-tier scale factor is uniform, about 0.91 to 0.94 (computed: 584/640=0.91,
    241/256=0.94, 20/21.6=0.93). Display-to-body ratio held: 584/20 ≈ 29 mobile vs
    640/21.6 ≈ 30 desktop (computed). The giant display is kept near full size and
    overflows the 390px viewport rather than scaling to fit.
- Motion. Timed reveals kept identical (measured transition strings): .a-mask_inner
  transform 0.5s cubic-bezier(.215,.61,.355,1) opacity 0.5s linear; .a-lines_inner
  transform 0.26s cubic-bezier(.55,.085,.68,.53). Scrub traversal dropped (no
  track). Horizontal parallax drift dropped (transform none).
- Nav. The (About) and (Chapters) menu affordances persist inline (measured button
  text). No hamburger reduction observed. The c-header hides on scroll as on desktop
  (measured header offsetParent null after scroll).

## hobro.digital (measured)
- Reflow, not restructure. Single vertical column preserved: scrollWidth 390,
  scrollHeight 18308 (desktop-session viewport read 15835). Taller as content stacks.
- Motion mostly kept. GSAP 3.12.7, ScrollTrigger.getAll().length 105 (desktop 116),
  so about 90 percent of triggers survive.
- Nav collapses to a mobile menu button: header__btn-mobile visible-mobile present
  in the top 120px band (measured). Full link set stays in the DOM behind it.
- CTA density stays high, repeated down the column. Persistent "GET CAPABILITIES
  DECK" in the chrome and at y 767, 13869, 17619; "Got Project?" at 1251, 11574;
  "GET YOUR COPY" (measured yTop). None fixed.
- Type ramp compresses. Display FreigBigProLigIta 300 italic, biggest 120px (desktop
  193). Weight contrast kept (300 italic vs Kamerik205 400 vs PPNeueMontreal 500).
  Negative tracking kept and scales with size (measured -1.2px at 120px vs desktop
  -1.93px at 193px). Body PPNeueMontreal 22px. Display-to-body ≈ 120/22 ≈ 5.5 mobile
  vs ≈ 193/16 ≈ 12 desktop (computed): display drops far more than body.

## creativeglu.ai (measured)
- Reflow, single column: scrollWidth 390, scrollHeight 8298 (desktop 9902, shorter).
  Multi-column grids collapse: grid-cols-1 lg:grid-cols-2 computes to a single 358px
  track; one 2-up 163px+163px grid retained (measured gridTemplateColumns).
- Fixed WebGL hero dropped. canvas count 0 after 6s settle plus a scroll pass; no
  webgl / sphere / three element anywhere (measured). Desktop carried a fixed
  full-viewport WebGL sphere; mobile does not build it.
- Custom cursor shipped but inert. cursor-magnifier and cursor-dot are in the DOM,
  display block but offsetParent null, not visible (measured). No pointer on touch.
- Motion model unchanged otherwise: no GSAP, no Lenis, timed on-enter reveals only.
- Nav reduces; persistent "PARTNER WITH US" near the top (y310). A burger element was
  not positively identified (header link scrape empty); nav-shape change noted from
  the absent inline link row, not from a named toggle (inferred).
- CTA density high, preserved. "Partner With Us" top; repeated "Start the
  Conversation" and "Explore AI Transformation" / "EXPLORE A PARTNERSHIP"; an FAQ
  accordion (question button at y6700); "Contact Us" at the foot. 10 CTA hits measured.
- Type ramp compresses. Inter weights 700/500/400/300 kept, letter-spacing normal.
  Hero 40px (desktop 72). Body 16px. Ratio 40/16 = 2.5 mobile vs 72/16 = 4.5 desktop
  (computed).

## matteprojects.com (measured)
- Reflow, single column: scrollWidth 390, scrollHeight 10961 (desktop 10063). But the
  named grid does not fully collapse: site-grid computes to 6 tracks of 52.5px at
  mobile (measured gridTemplateColumns), versus a 12-column desktop grid (col-span-6 /
  800:col-span-12 at an 800px breakpoint). Matte halves its grid rather than dropping
  to one column; the editorial grid device survives.
- Motion/hero kept. Lenis 1.1.13 smoothing present (measured window.lenisVersion);
  one hero video present (measured videoCount 1). On-enter fade-plus-rise reveals as
  desktop. No custom cursor.
- Nav collapses to a "Menu" trigger (measured "Menu" button in the top band,
  Syndicat Grotesk 20px).
- CTA density low, matching its portfolio purpose. "View Project" x3 inline (y3557 to
  4515), "Get In Touch" (4935), footer "Projects" and email (measured).
- Type ramp roughly held. Cormorant Garamond 300 display "Let's Get Creative" 75px,
  letter-spacing -0.4px, essentially flat against the desktop 75px read; matte carries
  an explicit mobile display class (display--sans--mobile, measured). RM Mono label
  face preserved as metadata and consent labels (18/14/12/10px). Body Syndicat Grotesk
  16px. Display-to-body ≈ 75/16 ≈ 4.7 (computed): the one secondary that does not
  compress its display much, mirroring the primary.

## Durable stills
refs/shots/mobile/<name>/full.png, one full-page capture each, iPhone 13 emulation
(deviceScaleFactor forced to 1 for file size), primary routes gate-entered:
lemans-en, lemans-night, lemans-podium, hobro, creativeglu, matte. Stock
scripts/shoot.mjs was not used for these: its "mobile" context sets viewport and DPR
but not the touch flag or mobile UA, and it does not click the primary's gate.
