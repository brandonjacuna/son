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

## 6. Placeholder

Reserved. To be filled next session.

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

Housekeeping:

- Screenshots were viewed live during the session but could not be written into
  `refs/shots/` as image files from this browser tool, which returns inline images only.
  The measurements they would have supported are recorded here and in
  `refs/notes/lemansclassic-primary-measurements.md` instead, which is the durable record.

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
