# Le Mans Classic, raw measurements (primary session)

Source site: lemansclassic.richardmille.com, /en scope only. Captured 2026-07-19.
Method: in-app DevTools browser, JS evaluation against the live page after library
registration (~3.5s waits), plus real wheel input to trigger motion. Viewport 1280x720.

This note is the evidence log. The reasoned write-up lives in docs/reference-spec.md.

## Libraries (measured, from window globals)
- GSAP 3.13.0 (window.gsapVersions = ["3.13.0"]). window.gsap and window.ScrollTrigger
  are undefined. The core is not reachable from any standard global, so
  ScrollTrigger.getAll() returns nothing and tween durations cannot be read from JS.
- Lenis 1.3.8 (window.lenisVersion).
- Framework: Nuxt (#__nuxt, #__NUXT_DATA__), Tailwind utility layer, custom token layer.

## Lenis config (measured, window._lenis.options)
lerp 0.1 | duration 0.8 | smoothWheel true | syncTouch false | touchMultiplier 1 |
wheelMultiplier 1 | orientation vertical | gestureOrientation vertical | infinite false
easing: function (t) => t===1 ? 1 : 1 - Math.pow(2, -10*t)   // easeOutExpo
html classes: "lenis" always; "lenis-smooth"/"lenis-scrolling" active; "lenis-stopped"
during preloader gates.

## Easing token library (measured, CSS custom properties on :root)
Full Penner set declared as --ease-in/out/in-out-{quad,cubic,quart,quint,expo,circ}.
Relevant values:
- --ease-out-expo   cubic-bezier(.19,1,.22,1)   (matches the Lenis wheel easing)
- --ease-out-quint  cubic-bezier(.23,1,.32,1)   (this is what the prior reference wrote as 0.22,1,0.36,1)
- --ease-out-cubic  cubic-bezier(.215,.61,.355,1)
- --ease-in-quad    cubic-bezier(.55,.085,.68,.53)

## Grounds and color tokens (measured)
- --accent-color #ffe500 (yellow), --bg-color #fff, --text-color #161616,
  --border-color rgba(16,16,16,.25)
- Three grounds in use, read as computed backgroundColor:
  yellow rgb(255,229,0) = #ffe500
  near-black rgb(22,22,22) = #161616   (the "bg-black" utility resolves to #161616, not #000)
  white rgb(255,255,255) = #ffffff
  plus transparent panels that carry full-bleed photo/video.

## Type (measured, computed style)
- Display face: Arges-Condensed, weight 400, uppercase, letter-spacing normal.
  Sizes seen: 109.5px, 256px (Tailwind text-9xl), 640px font-size / 512px line-height
  (0.8 leading) for chapter-takeover letters (.a-lines_inner).
- Body/UI face: DieGroteskC, weight 400. Body paragraph .p1 = 21.6px / 21.6px line-height
  (leading 1.0). Chapter index, time card, intro text ~14.2px.
- Single weight per face. The ramp is by size, not weight.

## Grid tokens (measured)
--layout-columns-count 12 | --layout-columns-gap calc(1vw*1.38889) |
--layout-margin calc(1vw*2.77778) | --vh 7.2px (= 720px viewport).

## Motion primitives (measured, computed transition)
- .a-mask_inner : transition "transform 0.5s cubic-bezier(.215,.61,.355,1), opacity 0.5s linear"
  (ease-out-cubic, 500ms). Primary block/text reveal. willChange transform.
- .a-lines_inner : transition "transform 0.26s cubic-bezier(.55,.085,.68,.53)"
  (ease-in-quad, 260ms). Enters from --appear-y 120% (translateY 120% to 0, clipped).
  Horizontal variant seen at translateX(-184). willChange transform.
- .a-parallax-bg_inner.-horizontal : transition "all 0s" (none). translateX set per frame
  from scroll position (measured tx -216 at scrollY 0, -125 at scrollY 1500). Scrub.
- .c-header.-hidden : translateY(-88px), header hides on scroll.
- Horizontal track: .h-full.flex.w-max, children = slide panels, scrollWidth ~10052px on
  chapter 01, transition none on the moving layer. Vertical wheel maps to horizontal
  translate (document scrollHeight ~9513px on ch.01).

## Chapter map (measured: route, displayed number, displayed title, slide count, grounds)
01 /en         MORNING                          ~11 slides   yellow/black/white
02 curtain     BACKSTAGE DAY                     10 wrappers  black x6, yellow x3
03 podium      THE PADDOCKS                      10 wrappers  black x3, white x5, yellow x3
04 rituals     PUBLIC AREA                       10 wrappers  black x6, yellow x4, white x1
05 ecosystem   THE START APPROACH                7  wrappers  black x4, yellow x1, white x1
06 guardians   5H THE DAY'S DAWN                 7  wrappers  black x4, yellow x3
07 pixel       END OF THE DAY                    10 wrappers  black x3, white x5, yellow x3
08 colors      THE SUN SETS TOWARDS THE HORIZON  10 wrappers  black x5, white x1, yellow x3
09 night       THE NIGHT                         10 wrappers  black x4, white x4, yellow x3
10 after       CHECKERED FLAG                    11 wrappers  black x5, yellow x3, white x2
11 backstage   THE CIRCUIT IS EMPTY              9  wrappers  black x3, white x4, yellow x2
12 witness     THE EMPTY STANDS                  9  wrappers  black x3, yellow x2, white x1

Route slugs are thematic and do not match the displayed chapter titles.
Each route re-shows a preloader gate ("Start the experience") and re-locks Lenis.

## Prior reference verdicts
- lerp 0.08         CORRECTED to 0.10 (measured).
- ease 0.22,1,0.36,1  present as a declared token (--ease-out-quint 0.23,1,0.32,1) but NOT
  the ease applied to the two measured reveals; those use ease-out-cubic and ease-in-quad.
- 450ms title land  measured primary reveal is 500ms (a-mask). Prior close, correct to 500.
- 80ms stagger      UNCONFIRMED (per-line reveal uses --index, numeric step not captured).
- 850ms panel reveal UNCONFIRMED (no 850ms value found).
- 1400ms takeover   UNCONFIRMED (chapter wipe not cleanly timed; ~2-3s including load).
- ~89 transformed   measured 66 to 68 at rest on ch.01, count grows during motion.

## Not captured
- Whether a chapter continuously scrolls into the next, or the next chapter is a route
  change. /en's live track showed panels spanning (01) toward a "(07) CHANGE" marker,
  which hints at chaining, but this was not confirmed with a full scroll-through.
- Any GSAP tween whose duration/ease is set in JS (core not exposed).
- Screenshots were viewed live but could not be written to refs/shots/ as PNG files from
  this browser tool (it returns inline images only).
