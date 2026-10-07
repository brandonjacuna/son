# Reference spec, primary

A reference document. It describes one external site so our own decisions have
something measured to sit against. It changes nothing in `src/`. The design system is
read-only input to this work, and this file is output, not a proposal.

## Scope of this session

Site: lemansclassic.richardmille.com, `/en` locale only. Secondary sites are out of scope
and belong to a separate session.

Editorial subject of the site: "Below the Line", a first-person photographic account of
Le Mans Classic 2025, credited to Hereme Chronicles. This matters only because the whole
motion and layout system serves a linear, timed narrative, not a product catalogue.

### Route count

Twelve routes were enumerated from the navigation and confirmed by visiting each one.
There is no sitemap.xml (it returns an error) and robots.txt lists none, so the count
comes from the in-page links plus direct visits. All twelve were parsed in this session.
None were left unparsed.

The routing is a Nuxt single-page app. Each chapter is a real route with its own URL and
its own preloader gate, not an anchor inside one long page. `/` redirects to `/en`.

| Number | Route | Displayed title | Slide panels (measured) |
| --- | --- | --- | --- |
| 01 | `/en` | MORNING | ~11 |
| 02 | `/en/curtain` | BACKSTAGE DAY | 10 |
| 03 | `/en/podium` | THE PADDOCKS | 10 |
| 04 | `/en/rituals` | PUBLIC AREA | 10 |
| 05 | `/en/ecosystem` | THE START APPROACH | 7 |
| 06 | `/en/guardians` | 5H THE DAY'S DAWN | 7 |
| 07 | `/en/pixel` | END OF THE DAY | 10 |
| 08 | `/en/colors` | THE SUN SETS TOWARDS THE HORIZON | 10 |
| 09 | `/en/night` | THE NIGHT | 10 |
| 10 | `/en/after` | CHECKERED FLAG | 11 |
| 11 | `/en/backstage` | THE CIRCUIT IS EMPTY | 9 |
| 12 | `/en/witness` | THE EMPTY STANDS | 9 |

Source: route slugs and titles measured from each page's `main` text and slide-wrapper
count. The slugs are thematic and do not match the printed chapter titles.

### How to read the sources

Every number below is tagged. Measured means read directly off the live page, from a
computed style, a JS global, or a DOM count. Computed means derived from a measured value
by arithmetic. Inferred means concluded from indirect evidence, with the evidence stated.

### Toolchain the site runs on (measured)

- GSAP 3.13.0, read from `window.gsapVersions`. `window.gsap` and `window.ScrollTrigger`
  are both undefined, and the core is not reachable from any standard global, so
  `ScrollTrigger.getAll()` returns nothing and no GSAP tween duration can be read from JS.
  This is the constraint the carry-in named, confirmed here.
- Lenis 1.3.8, read from `window.lenisVersion`, instance at `window._lenis`.
- Nuxt app shell, Tailwind utility classes, and a custom design-token layer of CSS
  variables.

---

## 1. Scroll model

Smooth scroll is Lenis 1.3.8. The instance options were read directly off
`window._lenis.options` (all measured):

- lerp 0.10
- duration 0.80
- smoothWheel true
- syncTouch false
- touchMultiplier 1, wheelMultiplier 1
- orientation vertical, gestureOrientation vertical
- infinite false
- easing: `t === 1 ? 1 : 1 - Math.pow(2, -10 * t)`, which is easeOutExpo, the same curve
  the token layer declares as `--ease-out-expo` cubic-bezier(.19, 1, .22, 1)

The prior reference gave the lerp as 0.08. That is corrected: the measured lerp is 0.10.

State is carried on the `html` element (measured class toggles): `lenis` is always
present, `lenis-smooth` and `lenis-scrolling` appear while scrolling, and `lenis-stopped`
holds during the preloader gate. Every route re-shows that gate, with a button labelled
"Start the experience" (the site's own copy), and Lenis stays stopped until it is clicked.

Scrub versus timed. The site is scrub-led. Vertical wheel input is virtualised into
horizontal travel: a `flex w-max` track of slide panels is translated on the x axis, and
the document's vertical scroll length maps to the track's width. On chapter 01 the document
scrollHeight was ~9513px (measured) and the track scrollWidth was ~10052px (measured), so
they are the same span within a small margin. The moving layers carry no CSS transition
(`transition: all 0s`, measured on the parallax layer and the track), which means their
transform is set every frame from the current scroll position rather than animated over a
fixed time. Confirmation by sampling: the parallax layer's translateX read -216px at
scrollY 0 and -125px at scrollY 1500 (both measured), a straight function of scroll
position. So the horizontal traversal and its parallax are scrub, and the only easing on
them is the Lenis lerp of 0.10.

The timed transitions in the system are the text and block reveals, covered in section 2.
Their durations live in CSS, so they can be read exactly. Any motion whose timing is set
inside a GSAP tween cannot be read, because the core is not exposed. Where a value here is
timed, it came from a CSS transition, not from GSAP.

---

## 2. Motion vocabulary

Six distinct transition types were observed. Durations and eases marked measured come from
computed CSS transitions. Distances marked measured come from computed transforms.

1. Horizontal chapter traversal (scrub). Trigger: wheel or scroll. The `flex w-max` track
   translates on x. Distance: the full track width, ~10052px on chapter 01 (measured).
   Duration: none, it is scrub. Easing: Lenis lerp 0.10, curve easeOutExpo (measured).
   Layers: the track plus a parallax background behind it, so two moving layers minimum.

2. Parallax background (scrub). Class `.a-parallax-bg_inner.-horizontal`. Its translateX
   is set per frame and runs across a background wider than the viewport (measured tx
   -216px on a 1296px-wide layer at rest), so the ground drifts against the foreground.
   Trigger: scroll. Duration: none, scrub (measured `transition: all 0s`). One layer.

3. Masked block reveal, the primary reveal (timed). Class `.a-mask_inner`. Transition
   measured as `transform 0.5s cubic-bezier(.215, .61, .355, 1), opacity 0.5s linear`, so
   500ms on transform with ease-out-cubic and 500ms on opacity with linear. Trigger: the
   panel becoming active. Distance: a short masked translate inside a clip, inner offsets
   read 13 to 35px (measured). Layers: a clip wrapper plus the moving inner, two layers.

4. Line rise reveal (timed). Class `.a-lines_inner`. Transition measured as
   `transform 0.26s cubic-bezier(.55, .085, .68, .53)`, so 260ms with ease-in-quad. The
   line enters from `--appear-y: 120%` (measured), that is translateY 120% up to 0 behind
   a clip. A horizontal variant was also seen, entering from translateX -184px (measured).
   Applied per line, so a multi-line block reveals line by line. Layers: clip plus inner.

5. Chapter takeover. At a chapter boundary the frame fills with the accent yellow and
   presents a large time card (for example "06 30" on chapter 01, measured text) together
   with giant display letters. Trigger: chapter entry. Duration: not cleanly measured. The
   wipe took roughly 2 to 3 seconds to settle, but that reading included asset load, so it
   is left unconfirmed rather than stated as a value.

6. Header hide (timed or scrub, not separated). Class `.c-header.-hidden` carries
   translateY -88px (measured), so the header lifts out of frame as the reader moves into
   the content.

The stagger interval between successive lines in type 4 was not captured as a number. The
elements carry a `--index` variable that would drive it, but no numeric step per index was
read. The prior reference's 80ms stagger is therefore unconfirmed here.

---

## 3. Type behavior

Two families, each at a single weight (measured `font-family` and `font-weight`):

- Display: Arges-Condensed, weight 400, always uppercase, letter-spacing normal.
- Body and UI: DieGroteskC, weight 400.

The ramp is by size, not weight, since only weight 400 was seen on either face.

Display sizes read on chapter 01 (all measured `font-size`):

- 109.5px on an inline running title
- 256px on a section title, which is Tailwind's `text-9xl` as this project extends it
- 640px font-size with 512px line-height on the chapter-takeover letters (`.a-lines_inner`),
  a line-height of 0.8 (computed from 512 / 640)

Body sizes (measured):

- Body paragraph `.p1` at 21.6px with 21.6px line-height, so leading 1.0
- Chapter index, time card, and intro text at ~14.2px

Tracking at display sizes is normal, that is letter-spacing is not tightened as the type
grows (measured letter-spacing normal on the 256px and 640px elements). The tightening the
system does at large sizes is in line-height, not tracking: the 640px letters sit on 0.8
leading (computed).

How large type enters. It rises into a clip. The big display letters are `.a-lines_inner`
elements, which start at translateY 120% and move to 0 behind a mask, on the 260ms
ease-in-quad transition from section 2 (measured). So the largest type in the system does
not fade or scale in, it slides up out of a cropped edge.

The scale itself is a set of chosen points, not a single ratio. From body to display the
measured points are 21.6, then 109.5, 256, 640. The step from body to the first display
size is large and is not a constant multiplier across the set (computed: 109.5 / 21.6 is
about 5.1, 256 / 109.5 is about 2.3, 640 / 256 is 2.5), so this reads as a hand-set ramp
rather than a modular scale.

---

## 4. Color and ground

The token layer declares a small fixed set (measured CSS variables on `:root`):

- `--accent-color` #ffe500, the yellow
- `--bg-color` #fff
- `--text-color` #161616
- `--border-color` rgba(16, 16, 16, .25)

Three grounds are in use across every chapter, read as computed `background-color`
(measured):

- Yellow #ffe500, that is rgb(255, 229, 0)
- Near-black #161616, that is rgb(22, 22, 22). Note the site's `bg-black` utility resolves
  to #161616, not pure #000 (measured). Their black is a soft black.
- White #ffffff

Alongside these, some panels are transparent and carry a full-bleed photo or video, so the
image is the ground on those.

There is no gradient in the ground system. Text color inverts against whichever ground it
sits on (measured): on yellow the text is #161616, on black it is white, on white it is
#161616 or black.

How sections change ground. The ground swaps at panel boundaries, not gradually. Each
slide panel carries its own `bg-*` utility, and because the chapters scroll horizontally,
the ground changes as one panel scrolls off and the next scrolls on, a hard swap at the
panel edge. The mix per chapter was measured. Some examples: chapter 02 ran 6 black and 3
yellow panels, chapter 09 ran 4 black, 4 white, and 3 yellow, chapter 03 ran 3 black, 5
white, and 3 yellow. So the same three-value ground system is reused everywhere, and a
chapter's mood is set by which of the three dominates its panel sequence.

A full Penner easing library is also declared on `:root` (quad, cubic, quart, quint, expo,
and circ, in in, out, and in-out forms). That belongs to motion, not color, and is noted
in section 7 against the prior reference's easing value.

---

## 5. Structure

This section describes their structure. It does not propose one for us. The last part lays
out what each of the two possible models would demand of an implementation, as observation,
not recommendation.

What was measured. Twelve chapters, numbered 01 to 12, each a named route (the table in the
scope section). Each chapter is a single horizontal-scroll track of 7 to 11 slide panels
(measured slide-wrapper counts). Each route independently shows its own preloader gate with
the "Start the experience" button and re-locks Lenis until entered (measured `lenis-stopped`
on each fresh route). The routing is Nuxt client-side routing, so the URL changes per
chapter and each chapter is deep-linkable.

How one panel hands off to the next inside a chapter. Horizontally, by scrub. Panels sit
side by side in the `w-max` track and the reader travels across them on wheel input, with
the parallax ground drifting behind. Text and blocks on each panel reveal on the timed
transitions from section 2 as the panel becomes active.

How one chapter hands off to the next. This is the one structural point that was not fully
resolved. Two readings are consistent with what was measured:

- Routed per chapter. Each chapter is its own page load with its own gate, and moving to
  the next chapter is a route change. This is directly supported: every route re-shows a
  preloader and re-locks Lenis, and `/en/podium` in isolation held only chapter 03 content.
- One continuous scroll. A single Lenis instance and one horizontal timeline span all
  chapters, chapters mount lazily, and the routes are scroll-position deep-links. This is
  hinted at but not confirmed: the live track on `/en` showed panels spanning from the
  (01) marker toward a "(07) CHANGE" marker in one track, which would not happen if `/en`
  held only chapter 01.

The evidence points both ways, so the handoff is left open in section 7. Resolving it needs
a single uninterrupted scroll-through of `/en` from start to end, watching whether the URL
changes on its own and whether the track keeps mounting new chapters.

What each model would demand of us, as observation:

- If the routed-per-chapter model is the real one, an implementation needs each chapter to
  be an independently loadable page: its own gate, its own preloader and asset set, its own
  horizontal track, its own Lenis lifecycle, and a clean state reset on entry and exit. The
  reader re-enters at every chapter. Deep links land on a gate, not mid-motion.
- If the single-continuous-scroll model is the real one, an implementation needs one
  persistent Lenis instance and one horizontal timeline that survives across chapters, lazy
  mounting and unmounting of panels so the DOM stays bounded, and a router that writes the
  URL from scroll position rather than loading a page. The gate is paid once, at the start.

The two models differ most in where the cost sits: repeated gates and per-chapter resets in
the first, persistent shared state and lazy mounting in the second.

---

## 6. Secondaries, what they do that the primary does not

Three sites, landing surface only, one pass each: hobro.digital, creativeglu.ai,
matteprojects.com. Raw evidence in `refs/notes/secondaries-measurements.md`. This section
records only where a secondary is structurally distinct from the primary. It is organized
by behavior, not by site. Sources are tagged as in section 0: measured off the live page,
computed by arithmetic, or inferred with the evidence stated. Absolute type sizes were read
at the in-app browser viewport and, because the sites are responsive, are read as ramp
relationships rather than fixed values.

### Axis and gate

All three drop the primary's two defining structural moves. Each is a single continuous
vertical-scroll page under one URL, with no per-section route and no per-section preloader
gate (measured: document scrollHeight 15835px hobro, 9902px creativeglu, 10063px matte,
one URL each, no "Start the experience" equivalent). None remaps vertical wheel into
horizontal travel. Where the primary pays a gate at every chapter and reads as twelve
routed horizontal tracks, the secondaries are one uninterrupted vertical column each.

### Scrub is the exception, not the rule

The primary is scrub-led: the whole track transforms per frame off scroll position, and
timed CSS is held back for text reveals only. Two of the three secondaries invert that.

- creativeglu.ai has no scrub at all. There is no smooth-scroll library and no scroll
  driver (measured: no GSAP, no ScrollTrigger, no Lenis, no CSS scroll-timeline). Every
  reveal is a timed CSS transition fired on enter, measured at 0.7s and 1s on
  cubic-bezier(0,0,0.2,1) ease-out. Motion is entirely timed, the mirror image of the
  primary.
- matteprojects.com smooths the native vertical scroll with Lenis 1.1.13 (measured) but
  scrubs nothing to scroll position (inferred: no ScrollTrigger, no scroll-timeline, only
  on-enter reveals present). Reveals are a fade plus a short rise, measured as opacity 0 to
  1 with transform translateY 10px to 0 on enter.
- hobro.digital does scrub, but as a per-element eased scrub rather than one raw track.
  Its motion is 116 GSAP ScrollTriggers (measured ScrollTrigger.getAll().length). Of those,
  52 are scrubbed (51 at scrub 0.3, a time-lagged catch-up, measured t.vars.scrub) and 63
  are on-enter timed toggles, with 0 pinned. So even the secondary that scrubs eases each
  trigger on its own 0.3s constant, where the primary's scrub is raw per frame and smoothed
  only by the global Lenis lerp.

Net: the primary reserves timed motion for text and scrubs everything else; the secondaries
lead with timed on-enter reveals and treat scrub as optional and locally eased.

### A persistent hero object behind the scroll

The primary's imagery is bound to the moving panels; there is no layer that stands still.
Two secondaries add one.

- creativeglu.ai fixes a full-viewport WebGL canvas at top:0 left:0 (measured: canvas
  1280x720, position fixed) carrying an iridescent sphere that animates on its own time
  base, behind all scrolling content. THREE is not global, so the renderer is bundled
  (inferred from the presence of a WebGL canvas with no global three.js).
- matteprojects.com anchors a hero video (measured: one autoplay <video>), time-based
  rather than scrubbed.

In both, a time-driven media object sits still while content scrolls over it. The primary
has no such layer.

### A custom cursor

creativeglu.ai runs a custom magnifier cursor (measured elements: cursor-magnifier,
cursor-dot, magnifier-lens, magnifier-ring). The primary has no custom cursor. Neither
other secondary does either.

### Type ramps by weight and style, and tightens as it grows

The primary's type is two faces at a single weight each (400), ramped by size only, with
letter-spacing left normal at every size. All three secondaries break at least two of those
rules.

- Weight as a ramp axis. hobro pairs Kamerik205 700 against FreigBigProLigIta 300 and adds
  PPNeueMontreal 400 and 500 (measured font-weight). creativeglu ramps Inter 400, 500, 700
  (measured). matte runs RM Mono 700 for labels under a light display. The primary never
  changes weight; the secondaries carry three to four.
- A light serif or italic for display. hobro sets its largest heading in a 300-weight
  italic serif ("title--cursive", FreigBigProLigIta, measured "What" at 193px). matte sets
  display in Cormorant Garamond 300 uppercase (measured "Let's Get Creative" 75px). The
  primary's display is a condensed grotesque at 400; a light serif or italic display face
  is a secondary-only move.
- Negative tracking that grows with size. hobro's display tightens as it scales (measured
  letter-spacing -1.6px at 160px, -1.93px at 193px). matte's display sits at -0.4px. The
  primary holds letter-spacing normal at 256px and 640px; tightening large type by tracking
  rather than only by leading is a secondary move.
- A monospace as an editorial label face. matte uses RM Mono heavily for metadata and
  bracket labels (measured RM Mono on roughly 250 elements, e.g. "[ WHO WE ARE ]");
  creativeglu carries Geist Mono. The primary has no mono face.

How large type enters is one place they converge with the primary rather than diverge:
hobro also splits headings into lines and rises them in (measured ".line" split), which is
the primary's own line-rise reveal. That is noted as shared, not distinct.

### Ground

The primary runs a three-value ground (yellow accent, soft black #161616, white) and swaps
it hard at panel edges, letting the dominant value set each chapter's mood. The secondaries
each depart from that.

- Monochrome, no accent. matteprojects.com is a greyscale system with no chromatic accent
  at all (measured grounds rgb(241,241,241) light grey dominant, rgb(129,129,129) mid grey,
  rgb(29,29,29) near-black). It is also the only light-grounded secondary.
- One continuous ground, variation carried elsewhere. creativeglu.ai does not swap ground.
  It is one continuous dark field (measured oklab(0 0 0 / 0.95)) and lets the fixed WebGL
  object, not the ground, carry the variation.
- Pure black and modern color spaces. hobro's dominant ground is pure rgb(0,0,0), not the
  primary's soft #161616 (measured), with a single green spot accent #00FB96 used off the
  ground rather than as one. creativeglu declares grounds in oklab and lab (measured), where
  the primary's tokens are hex and rgb.

### Where calls to action sit

The primary carries no conversion call to action. Its only button is the per-route "Start
the experience" gate; it is an editorial narrative and sells nothing. All three secondaries
are agency or product sites and place calls to action throughout (measured anchor and button
text): a persistent one in the chrome (hobro "GET CAPABILITIES DECK", creativeglu "Partner
With Us", matte "Contact") and repeated inline conversion prompts between content blocks
(creativeglu "Start the Conversation", "Explore AI Transformation"; hobro a terminal "Got
Project?" block). creativeglu also closes with an FAQ accordion (measured question buttons),
a disclosure pattern the primary has no equivalent for. This is the clearest behavioral split
and it follows from purpose: the primary tells a story, the secondaries convert.

### Structure dividing

Beyond the vertical-versus-horizontal split already covered, one secondary divides its page
with a device the primary does not use: matteprojects.com lays content on a named column
grid (measured classes "site-grid", "col-span-6" with an 800px breakpoint) and marks sections
with monospace bracket labels ("[ WHO WE ARE ]"), an editorial index device. hobro and
creativeglu divide by stacked feature and content blocks and are not structurally distinct
from the primary on this axis beyond the axis itself.

---

## 7. Open questions and unmeasured items

Parsing coverage. All twelve routes were parsed. None were left unparsed.

Prior reference values, checked one by one:

- lerp 0.08. Corrected. The measured Lenis lerp is 0.10.
- Easing cubic-bezier(0.22, 1, 0.36, 1). This is close to the declared token
  `--ease-out-quint` cubic-bezier(.23, 1, .32, 1), which the site does define. But it is
  not the ease applied to the two reveals that were actually measured. Those use
  ease-out-cubic (500ms block reveal) and ease-in-quad (260ms line reveal). The scroll
  smoothing uses ease-out-expo. So the prior value names a token that exists but was not
  seen applied to the measured motion.
- 450ms title land. Close, corrected to 500ms. The measured primary reveal (`.a-mask_inner`)
  is 500ms on ease-out-cubic.
- 80ms stagger. Unconfirmed. Per-line reveal is driven by a `--index` variable, but no
  numeric step per index was read.
- 850ms panel reveal. Unconfirmed. No 850ms value was found in any measured transition.
- 1400ms takeover. Unconfirmed. The chapter wipe was not cleanly timed. It settled in
  roughly 2 to 3 seconds, but that included asset load, so no firm value is given.
- About 89 transformed elements. Measured 66 to 68 at rest on chapter 01, growing during
  motion as more elements mount. The order of magnitude holds, the exact count depends on
  mount state and is not fixed.

Could not measure:

- Chapter-to-chapter handoff, routed versus one continuous scroll (section 5). Needs a full
  uninterrupted scroll-through of `/en`.
- Any GSAP tween whose duration or ease is set in JavaScript. The GSAP core is not reachable
  from a global, so only CSS-driven timings could be read. Timed values in this spec are all
  from CSS transitions.
- The stagger step between reveal lines, as above.
- The chapter-takeover duration, as above.

Secondaries, could not measure (section 6):

- hobro.digital reveal durations. Its 63 on-enter toggles run as GSAP timelines, and the
  GSAP core, though reachable here, exposes ScrollTrigger vars but not the tween durations
  those toggles fire. Only the scrub values (0.3 on 51 of them) were read. Contrast the
  primary, where reveal timing came from CSS; here it lives in JS and was not captured.
- hobro.digital behind the preloader. The "LOADING..." gate did not clear in the in-app
  browser during the pass, so all hobro readings are from the DOM and computed styles behind
  the overlay, not from watching the motion run. Content was fully present and measurable,
  but the reveals and scrub were not observed in motion. This is the client-rendered,
  markup-invisible motion the brief flagged; it is noted, not fought.
- matteprojects.com and creativeglu.ai smooth-scroll and scrub state. Neither exposes a
  scroll instance on window (matte's Lenis 1.1.13 is module-scoped, creativeglu has no
  library), so the "not scrub-led" reading for each is inferred from the absence of any
  scroll driver and the presence of only on-enter reveals, not from a positive measurement.
- Absolute display type sizes on all three. Read at the in-app browser viewport against
  responsive layouts, so they stand as ramp relationships (weight contrast, tracking sign,
  face pairing), not fixed pixel values. The relationships are robust; the exact px are not.
- Whether the fixed hero objects (creativeglu WebGL sphere, matte video) respond to scroll
  at all. Both were read as time-based and fixed, but a full scroll-through watching for any
  scroll coupling was not run.

Bearing on the routed-versus-continuous question. The secondaries do not resolve it. All
three are continuous single-page vertical scroll under one URL with no routing and no
per-section gate, which is the continuous model in the abstract, but none uses the primary's
per-chapter Nuxt routing or its horizontal-track-per-chapter construction. They are a
contrast to the primary, not evidence about how it chains its own routed chapters. The
primary question, routed per chapter versus one continuous horizontal scroll, stays open and
still needs the full uninterrupted scroll-through of `/en` named above.

Housekeeping:

- Screenshots were viewed live during the session but could not be written into
  `refs/shots/` as image files from this browser tool, which returns inline images only.
  The measurements they would have supported are recorded here and in
  `refs/notes/lemansclassic-primary-measurements.md` instead, which is the durable record.

---

## 8. Mobile translation

How each site renders itself on a touch device. Sections 1 through 7 describe desktop and
do not change. This section is observation only.

Raw evidence is in `refs/notes/mobile-measurements.md`. Sources are tagged as before:
measured off the live page, computed by arithmetic, or inferred with the evidence stated.

### How this was rendered

A real device was emulated, not a resized viewport. The profile was the Playwright
"iPhone 13" descriptor, which brings the touch flag, an iOS Safari user agent, and device
pixel ratio 3, so a site that branches on touch support reads as touch, not as a narrow
desktop. Confirmed on-page (measured): user agent iOS 15 Safari, `navigator.maxTouchPoints`
1, `"ontouchstart" in window` true, `(pointer: coarse)` true, `(hover: none)` true, device
pixel ratio 3, innerWidth 390. Every reading below sat behind that profile.

Tooling note. The named DevTools MCP (`.mcp.json`) was not present in the working directory.
Playwright, the project's own capture dependency behind `scripts/shoot.mjs`, was used in its
place. It emulates the device and, through CDP touch events, drives real swipe gestures, so
the primary question below was answered by measurement, not inference. `refs/clips/` held no
phone capture this session, so no decomposed clip fed the question.

### The primary's horizontal track on touch

The horizontal scrub track does not survive as a swipe. It collapses to a vertical scroll
column. This was measured three ways, on `/en`, `/en/night`, and `/en/podium`.

- No track. An exhaustive walk of every element for a row-direction flex wider than the
  viewport returned zero on all three routes (measured). `document.scrollWidth` was 401 on
  `/en` and 390 on the other two (measured), so there is no horizontal overflow to travel
  across.
- Gestures. A driven vertical swipe moved `scrollY` from 0 to 774 on `/en`, 0 to 966 on
  `/en/night`, 0 to 1002 on `/en/podium` (measured). A driven horizontal swipe moved
  `scrollX` to 11px, a rubber-band bounce, and left `scrollY` unchanged (measured). Touch
  drives vertical scroll only; a horizontal swipe advances nothing.
- Mechanism. A `(max-width: 767px)` media rule targets the `w-max`, `flex-row`,
  `horizontal`, and `a-parallax` selectors, alongside a `(min-width: 1024px)` rule and a
  `(pointer: coarse)` query (measured, scanned from the stylesheets). So the collapse is a
  width breakpoint at 767px and below, reinforced by a coarse-pointer query. The
  `.-horizontal` parallax modifier class is still in the DOM (measured) but its computed
  transform is `none` (measured), so the horizontal drift is switched off, not re-eased.

The Lenis instance is configured exactly as on desktop (measured `window._lenis.options`):
orientation vertical, gestureOrientation vertical, syncTouch false, lerp 0.1, duration 0.8.
On desktop that vertical wheel is virtualised into horizontal travel by the `w-max` track; on
mobile there is no track, so Lenis simply smooths the native vertical scroll.

What is lost: the wheel-remapped horizontal traversal and the horizontal parallax drift.
What is kept: the panels and their content, the timed reveals, the three-value ground, and
the per-route gate. The chapter still reads. Its content lays out top to bottom as a vertical
narrative and reveals on the same timed transitions. This finding is measured, from gesture
driving plus DOM and CSS reads, not inferred.

### The primary, everything else

- Structure changes, it is not only a reflow. The defining desktop move, a horizontal
  wheel-remapped track, is removed and the panels are re-laid as a vertical stack (measured
  bounding-rect tops increasing down the page, widths at viewport). This is the only site in
  the set whose structure changes on mobile.
- Chapter count is unchanged: twelve routes, each still showing its own gate (measured
  `lenis-stopped` before entry on every route tested). Within-chapter panel count was not
  cleanly re-counted at mobile; the panel content is present as stacked blocks, so no count
  change is asserted.
- The ground system carries over intact: white, yellow `#ffe500`, and soft black `#161616`
  still appear on stacked blocks and swap block to block down the column (measured
  background-color), where on desktop they swapped panel to panel across the track.
- Type ramp. The display face is unchanged, Arges-Condensed weight 400, letter-spacing
  normal (measured). The tiers scale down together by a near-constant factor of about 0.91
  to 0.94 (computed): chapter-takeover letters 584px against desktop 640px, section title
  241px against 256px, body 20px against 21.6px. Line-height on the takeover letters holds
  at 0.8 leading (computed 467.2 / 584). So the display-to-body ratio is preserved across
  widths, about 29 on mobile against about 30 on desktop (computed). The giant display is
  kept near full size and overflows the 390px viewport rather than being scaled to fit.
- Motion. The timed reveals are kept identical (measured transition strings unchanged from
  section 2: masked block reveal 500ms ease-out-cubic, line rise 260ms ease-in-quad). The
  two scrub behaviours are dropped, because their axis is gone: the horizontal traversal has
  no track, and the horizontal parallax computes to `none`. The timed system survives whole;
  the scrub system is removed.
- Navigation keeps its shape. The `(About)` and `(Chapters)` affordances stay inline
  (measured button text); no hamburger reduction was seen. The header hides on scroll as on
  desktop (measured header not visible after scrolling).

### The secondaries, one pass each

All three keep a single vertical-scroll column under one URL (measured `document.scrollWidth`
390 on each), so on the vertical axis they reflow rather than restructure. Where each departs
is below.

hobro.digital.

- Reflow only, taller as content stacks (measured scrollHeight 18308 mobile against 15835 at
  the desktop-session viewport).
- Motion is mostly kept: GSAP 3.12.7 with 105 ScrollTriggers against 116 on desktop
  (measured), about nine in ten surviving.
- Navigation collapses to a mobile menu button (measured `header__btn-mobile visible-mobile`
  in the header band); the full link set stays in the DOM behind it.
- Calls to action stay dense and repeat down the column: the persistent "GET CAPABILITIES
  DECK" in the chrome and again at three points down the page, plus "Got Project?" twice and
  "GET YOUR COPY" (measured vertical positions). None are fixed.
- The type ramp compresses. The 300-weight italic display drops to 120px from desktop 193px,
  while the body holds near 22px, so the display-to-body ratio falls to about 5.5 from about
  12 (computed). Weight contrast and size-growing negative tracking are kept (measured
  -1.2px at 120px against -1.93px at 193px).

creativeglu.ai.

- Reflow, and shorter than desktop (measured scrollHeight 8298 against 9902). Multi-column
  grids collapse: `grid-cols-1 lg:grid-cols-2` computes to a single 358px track, with one
  2-up 163px grid retained (measured grid-template-columns).
- The fixed WebGL hero is dropped. Zero canvas elements after a six-second settle and a
  scroll pass, and no sphere or three.js element anywhere (measured). The desktop's still,
  time-based centre is not built on mobile.
- The custom magnifier cursor is shipped but inert: its `cursor-magnifier` and `cursor-dot`
  elements are in the DOM, display block, but not visible (measured offsetParent null). Touch
  has no pointer to magnify.
- Navigation reduces to a persistent "PARTNER WITH US" near the top (measured position); a
  named toggle was not positively identified, so the reduction is read from the absent inline
  link row (inferred).
- Calls to action stay dense: "Partner With Us" at top, repeated "Start the Conversation" and
  "Explore AI Transformation" through the body, an FAQ accordion, and "Contact Us" at the
  foot (measured, ten hits). The timed on-enter reveal model is unchanged, no scroll library
  either width (measured).
- The type ramp compresses: Inter hero 40px against desktop 72px, body 16px, ratio about 2.5
  against about 4.5 (computed). The 400 to 700 weight ramp is kept.

matteprojects.com.

- Reflow, similar height (measured scrollHeight 10961 against 10063). The named column grid
  does not fully collapse: `site-grid` computes to six 52.5px tracks at mobile against a
  twelve-column desktop grid at its 800px breakpoint (measured grid-template-columns). Matte
  halves its grid rather than dropping to one column, so the editorial grid device survives.
- Motion is kept: Lenis 1.1.13 still smooths the scroll and the one hero video is still
  present (measured). The on-enter fade-plus-rise reveals are unchanged. No custom cursor.
- Navigation collapses to a "Menu" trigger (measured "Menu" button in the header band).
- Calls to action are low density, matching a portfolio: three inline "View Project", one
  "Get In Touch", and a footer "Projects" and email (measured positions).
- The type ramp roughly holds. The 300-weight serif display sits at 75px, flat against the
  desktop 75px read, carried by an explicit mobile display class (measured
  `display--sans--mobile`); the monospace label face is preserved for metadata and consent
  labels (measured). Display-to-body is about 4.7 (computed). This is the one secondary that
  does not compress its display, mirroring the primary.

### Where structure changes and where it only reflows

Only the primary changes structure on mobile, from a horizontal wheel-remapped track to a
vertical stack. The three secondaries reflow their single vertical column and no more. This
follows from the axis: a horizontal wheel remap has no touch equivalent, so it has to be
rebuilt, while a vertical column only has to narrow. Touch also removes the pointer-dependent
flourishes, creativeglu's WebGL hero and its custom cursor both go, one removed and one left
inert, while matte's video, which needs no pointer, stays.

---

## Scratch

Patterns worth keeping in mind. These are notes, not part of the design system, and they do
not carry any recommendation for our own build.

- A three-value ground (one accent, one soft black, one white) reused across every chapter,
  with a chapter's character set by which value dominates its panel run, is a cheap way to
  give a long linear piece both variety and unity.
- Vertical wheel mapped to horizontal travel, with the whole thing scrub-led and smoothed
  only by a single lerp, keeps the motion model small. The timed CSS transitions are
  reserved for text reveals, so the two systems, scrub for travel and timed for reveal, stay
  cleanly separated.
- The largest type entering by rising out of a clip, rather than fading or scaling, is what
  makes the display sizes feel physical rather than decorative.
- Soft black (#161616) instead of pure black across the ground and text is a small choice
  that reads throughout.

From the secondaries:

- The scrub-led primary and the timed-led secondaries are two ends of one axis, not two
  unrelated systems. A page can lead with either. What the primary shows is that once you
  commit to scrub for travel, you gain the freedom to reserve timed motion for text alone;
  what creativeglu shows is that dropping the scroll library entirely and firing every reveal
  on enter is a smaller, calmer build that still reads as considered.
- A fixed time-based hero object with content scrolling over it (creativeglu's WebGL sphere,
  matte's video) is a cheap way to give a still page a living center without scrubbing
  anything to scroll.
- Weight and a second face carry a type system when the copy is short and declarative;
  size-only, single-weight ramps like the primary's suit long editorial runs where a single
  voice should hold. Negative tracking that grows with size is what makes large weight-heavy
  display feel set rather than default.
- A monospace used only for metadata and bracket labels (matte) is a low-cost way to mark
  structure and signal craft without adding a display face.

From the mobile pass:

- A type ramp can either scale down as a whole into mobile, keeping the display-to-body ratio
  fixed across widths (the primary and matte), or flatten the display toward the body on small
  screens (hobro and creativeglu). These are two distinct stances on responsive type: hold the
  ratio, or compress the top of the ramp. The choice is separate from the face and weight
  choices, and it is measurable per breakpoint.
- The primary keeps its display type near full size and lets it overflow a 390px viewport
  rather than fitting the letters to the screen. Sizing display type to the content and
  clipping, instead of sizing it to the viewport, is a way to keep the same physical presence
  on a small screen that the large type has on a large one.
- A horizontal wheel-remapped track has no touch equivalent, so it cannot reflow, it has to be
  rebuilt as a vertical column. A model that leads with a horizontal scrub axis is buying a
  second layout for touch, where a vertical column only narrows. The cost of the horizontal
  idea is paid twice.
- Pointer-dependent flourishes do not carry to touch. A custom cursor becomes inert and a
  fixed WebGL centre can be dropped rather than ported. Anything that reads as the signature of
  the desktop page may simply be absent on the device most readers arrive on, so it is worth
  knowing which parts of a page are pointer-only before leaning on them.
- Navigation tends to converge on mobile even when desktop navigation diverges: all three
  secondaries collapse to a single menu trigger, while only the primary keeps its two labelled
  affordances inline. A menu trigger is the safe default; keeping affordances inline is the
  exception that has to be chosen.
