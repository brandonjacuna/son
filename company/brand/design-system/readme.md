# Sŏn — Design System

선 · Future Nostalgia Hospitality Group · 207 E St. Elmo Rd, Austin, Texas 78745

---

## Start here (handoff, 2026-07-23)

You are a developer with no context. This is enough to work:

- **What deploys:** `track/` — a static scroll-driven single page. No
  build step: serve the repo root (`python3 -m http.server 8080`) and
  open `/track/index.html`. `site/` is the frozen v3 fallback (tag
  `v3-fallback`); `track/` is what ships (tag `v4-track`). Why both
  tags exist and why neither gets deleted: `docs/handoff.md`.
- **Your tasks and everything owed by name:** `docs/handoff.md` — the
  ownership record (endpoint, dedup, regeneration, deployment; what is
  still Brandon's).
- **Checks:** `npm install && npm run lint`. Four checks, every one
  blocks: stylelint (CSS/HTML color+font discipline), copy
  (`adherence/check-copy.mjs`), the track stacking invariant
  (`adherence/check-track.mjs` — the one constraint that, broken,
  silently kills the site's central mechanism), and the JSX canon
  (`eslint.config.mjs`). What they do NOT cover: rendered geometry,
  scroll behavior, and visual judgment — those live in the evidence
  workflow (`npm run shoot / scrollframes / timeframes`, output under
  `refs/shots/`) and in rulings. See Adherence below for exact scope
  and the recorded debt register.
- **The rules of the build:** `docs/codified-patterns.md` — the
  graduated pattern rules (why motion is built as an opt-in over a
  complete static page, why states are constructed rather than
  synchronized, the two motion registers, form-surface stability,
  token governance). Read before touching any motion-carrying surface.
- **The decision record:** `docs/build-spec.md` §7 (ratified decisions
  verbatim; supersessions ONLY in its Amendments section) with
  `docs/track-scratch.md` (mechanisms and method notes) and
  `docs/build-state.md` (the build-session record and evidence map).
  The pattern: the record stays verbatim; changes are dated amendments
  with reasons.
- **The tested boundary:** `docs/browser-support.md` — what was tested
  (three engines × four widths, rendered geometry; one real iPhone
  end-to-end), what was not (desktop Safari at all; continuous
  scrolling on any desktop), and what to check first before ship.
- **The standing doors** — named, unspent design decisions that reopen
  only on evidence — are listed at the end of `docs/handoff.md`.

Everything below this line is the design system's own record: brand
foundations, canon, tokens, components, and adherence.

A Korean fine-dining restaurant in Austin. One master brand, four dayparts under
one roof. **Sŏn is the only consumer-facing brand at the building** (canon:
ClickUp 2ky45bmy-15773 §02, Tier 4 / non-negotiable 9, checked 2026-07-23).
**Good Energy** (morning) and **Dosi** (lunch) are **internal daypart codenames
only** — real brand names in the future portfolio, which is how an earlier
version of this paragraph drifted into calling them public daypart expressions;
they are never consumer-facing at this location. The late-night daypart is part
of the Sŏn core; its former name **Luxx is retired entirely** (not
internal-only), and the former membership concept is now the unnamed private
membership layer. The 선 glyph is part of the Sŏn logo and appears where the
logo appears. It is not required on every surface (canon line, 2026-10-07).

Positioning is three equal, unordered values: **Korean restraint · Texas warmth ·
polished but playful.** Texas warmth lives in the service, space, and voice — not
the letterforms.

> This design system encodes the brand's closed visual language as tokens,
> components, specimen cards, sample slides, a deck template, and two product UI
> kits. It is informed by a set of guiding cultural influences (below). They
> shape decisions; they do not hold veto power over them (2026-10-07).

---

## Sources

Everything here is synthesized from two documents supplied at build time
(stored in `uploads/` — do not assume the reader has them):

- `uploads/Son Brand Guidelines v1 (1).md` — the full brand guidelines (v1.0):
  foundation, architecture, visual identity, typography, color, spatial design,
  multi-sensory architecture, service model, verbal identity, photography,
  digital identity.
- `uploads/Design System Guidelines.md` — DESIGN.MD v3.0: the machine-readable
  token/color/type spec plus **Section 14**, the deck governing principles.
- Living document of record (no access assumed): ClickUp doc `2ky45bmy-15773`.

No codebase or Figma file was provided. There were no slide decks to extract;
the deck template here is built fresh from Section 14.

**Font files** supplied: GT Sectra (Book, Regular, Bold, Black, + Display Light/
Medium/Regular and italics) and GT Alpina (Light/Regular/Medium + italics), both
Grilli Type. A stray `Display.ttf` (an unrelated face named "Gems") was ignored.

---

## Guiding influences (inform, do not govern)

Jaeyeonmi, Ma, Mahk, Jeong, and Nunchi are guiding influences. They inform
design, service, and copy decisions. They are not Tier-1 rules and hold no veto
power; a decision is tested against them and weighed alongside cost, aesthetics,
and evidence (2026-10-07).

1. **Jaeyeonmi (자연미) — Beauty of the Natural.** Nothing conceals what it is,
   where it came from, or how long it has been here. *In digital:* no faux
   textures, no simulated foil, no applied grain, no drawn imitations of real
   materials. Gold Foil is named as a physical material, never simulated.
2. **Ma / Yubaek-ui-mi (여백의 미) — Beauty of Meaningful Negative Space.** Empty
   space is active and held — a specification, not a default. A layout that looks
   underbuilt is disciplined, not unfinished.
3. **Mahk (맛) — Taste as Memory.** Specificity is the mechanism of memory. A
   surface that could belong to any restaurant has failed. Name the one thing no
   other sentence could name.
4. **Jeong (정) and Nunchi (눈치): service.** Jeong is accumulated relationship,
   not performed welcome. Nunchi is reading what someone needs before they ask.

---

## Content fundamentals

How Sŏn writes. The voice is **present without performing** — the master register
across all dayparts.

- **Sentence case always.** UPPERCASE is reserved for single-line eyebrow text
  only (category markers, section identifiers). This is near-absolute; the only
  other sanctioned uppercase context is the ADA restroom descriptor.
- **"Customer," never "guest."** Absolute, all contexts, all copy, internal and
  customer-facing. No exceptions.
- **"We" in brand voice; "you" in customer-facing copy.** Warmth is in the
  attention, not the adjectives.
- **No em dashes.** No exclamation points. No emoji. (This system uses hyphens and
  spaced hyphens in running copy; em dashes appear only in this internal readme's
  prose, never in brand-voice output.)
- **No filler.** Copy does not rush to fill silence. The sentence ends at its last
  load-bearing word. Sentences in sequence accumulate; they do not explain each
  other.

**Six binary tests** (a sentence fails at the first it does not pass): (1) Does it
name its own effect? (2) Can the primary noun be swapped for a category sibling
unchanged? (3) Does it continue past its last load-bearing word? (4) Does it answer
a question not yet asked? (5) Could it appear unchanged in a competitor's copy?
(6) Does sentence two explain sentence one?

**Forbidden lexicon (always):** elevated, experiential, innovative, disruptive,
authentic, delicious, mouthwatering, vibrant, seasonal, chef-driven, hand-crafted,
house-made, community-driven, passion, journey, curated, farm-to-table, artisanal,
crafted, must-try, amazing, incredible, thoughtful, intentional, memorable,
unforgettable, beautiful, stunning — and "barbecue" as a genre descriptor.
**Forbidden in context:** "welcome"/"enjoy" in written copy; "inspired by" in menu
and in-space copy; reassurance adjectives (crispy, tender, rich, bold) when they
function as quality signals.

**Korean terms in brand copy** are limited to dish and ingredient names: Galbi,
Dosirak, Banchan, Ganjang, Doenjang, Gochujang, and 선. Philosophy and craft terms
(Jeong, Nunchi, Jaeyeonmi, Ma, Mahk, Buncheong, Baekja, Pyeong-sang) are internal
influences, not brand vocabulary. There is no no-gloss rule: a dish or ingredient
may carry a short description where the customer needs one (2026-10-07). Preparation is stated as decision, factually: scored, aged, braised,
pressed, set, rendered, reduced. Specific over categorical: "thirty days" not
"long-aged"; "white oak" not "hardwood."

> **OPEN DECISION — menu voice (flagged, not rewritten).** The guidance line
> above ("Preparation is stated as decision, factually: scored, aged, braised,
> pressed, set, rendered, reduced") is what generated the clipped menu register
> ("Aged thirty days. Scored before the fire.") that has been removed from every
> slide, specimen, and example as predating the current voice. The rule is kept
> here unedited pending a call on the current menu voice: keep
> preparation-as-decision, or move menu copy to the plainer register of the live
> site. Until that call, dish names carry identity; do not write new imagistic
> menu descriptions.

**Examples (correct):**
- Longer-form: *Most restaurants are pointed at the plate. We are pointed at the
  relationship. The plate is how we earn the right to have one.*
- Statement: *What looks like a people business is a memory business.*
- Statement: *Only two things in a restaurant compound. The organization, and the
  customer. Everything else a good competitor copies in a season.*
- Callout: *One footprint. Coffee, lunch, dinner, late night, against one set of
  fixed costs.*
- Confirmation: *Your table is confirmed for Saturday at 7. Outdoor seating, as
  requested. We'll see you then.*
- In-space: *선 / 207 E St. Elmo Rd*

---

## Visual foundations

**Palette — eight colors, closed.** No tints, no shades, no exceptions. Parchment
`#DBC9B0`, Bone `#EDE7D8`, Plum Ink `#120916`, Aubergine `#2E1F31`, Jade `#8DA982`,
Peacock `#3E5640`, Onggi `#804A33`, plus Pale Jade `#C8D4BE` (a *derived* morning
token, not one of the eight) and Gold Foil (Pantone 871C / Kurz Luxor 220 — a
**physical-only** specification with no flat-fill token, digitally represented as
`#BC9A5C` for reference only). Never introduce a ninth color, a tint, a shade, a
purple gradient, or blue as an accent.

**Daypart themes** switch at the semantic tier via `data-theme`, no JS required:
`morning` (Pale Jade / Peacock), `dosi` (Parchment / Onggi), `dinner` (Plum Ink /
Aubergine), `luxe` (Plum Ink / Aubergine + Jade accent), and the base/editorial
default (Bone / Parchment). These namespaces are **sanctioned internal design
tokens per canon** — `data-theme="dosi"` in markup is correct and stays; the
codename rule above governs consumer-facing *strings*, not token names. Canon
itself flags the `luxe` namespace for review, since it predates the Luxx
retirement — recorded here, not acted on. **Jade is a named failure mode in the dinner register**
— it never appears there as text, accent, glyph, or decoration. Jade enters only
in the morning and as the late-night bar-back accent. Jade paired with Aubergine
or Plum Ink as the two dominant colors is a named failure mode anywhere.

**Type.** Two Latin faces, one Korean companion, and the ceiling is absolute.
*GT Sectra* (Fine Book is the wordmark weight; Display for headlines/section
headers) leads and is felt. *GT Alpina* (Fine Standard) follows and is read.
*Sandoll Myeongjo* is the Korean companion, limited to the 선 glyph and Hangul
dish names. See **Font substitutions** below for the web stand-in. Body copy caps at ~65 characters, never above 75.

**Spacing & structure.** 8pt grid. **1px hairline** borders only — no double
rules, no colored left-border accent boxes. Exactly two 2px exceptions are
sanctioned, both for state legibility and never for decoration: the focus ring
(`outline: 2px`, on every control) and the form-field error border
(`border-width: 2px` at `--son-border-strong` on `[aria-invalid="true"]`, which
distinguishes error from the 1px `:hover` border-strong state). Corners are near-square
(radius 0–2px); rounding reads as decoration and is used sparingly. Restraint over
decoration: silence is more luxurious than noise.

**Backgrounds.** Flat color surfaces from the palette. **No gradients of any kind.**
The editorial register (decks, most digital) lives on Bone/Parchment; the dinner
register lives on Plum Ink/Aubergine. No repeating patterns as ground fill — the
pattern system (reference only, not canon) is edge/accent scale only (see Iconography). No textures applied in
post; texture is a material decision, not a design overlay.

**Shadows.** Effectively none. The system separates surfaces with hairline borders,
not drop shadows. Drop shadows on text or images are prohibited; so are bevels and
embossing. `--son-shadow-hairline` is the only sanctioned "elevation."

**Cards** are held surfaces: a single hairline border, no shadow, generous padding,
near-square corners. The empty margin is part of the composition.

**Motion — two registers.** The **UI register** (`--son-motion-fast/standard/slow`,
100 / 200 / 400ms; easing `cubic-bezier(0.4,0,0.2,1)`) marks state change, never
importance: the reservation flow, forms, product UI. No fade-up-on-scroll, no
pulsing or blinking for emphasis, no bounce/spring. Hover shifts color *within the
palette* (or a low-alpha wash); press reduces opacity slightly. No scale-on-press
theatrics. The **track register** (`tokens/motion-track.css`, replacing the
immersive register retired 2026-07-22: blocks `--son-track-block-duration` 500ms,
lines `--son-track-line-duration` 260ms, `--son-track-stagger` 80ms,
`--son-track-hold` 240ms, ease-out-cubic on transform with linear opacity, fades
500/400ms, `--son-track-pin-distance` 150vh, `--son-track-coda-travel` 80, Lenis
lerp 0.10) carries meaning and sequence, which the UI register forbids by design.
It governs the track build (`track/`): travel scrubbed, text timed, feedback in
the UI register, per-line rises only on locked strophes. Never on UI or the
reservation flow; keeping the registers separate is the point. Under
`prefers-reduced-motion` the UI register collapses to 0ms and the track runs its
designed second path: entrances instant and opacity-only, no pin, the band
complete, the still layer simply present, the coda closed by the placed close.

**Imagery.** Photographs are memories, not documents — people present, found light
only, decentered, closer than comfortable, film grain preserved. **AI-generated
imagery is prohibited on all public-facing surfaces, absolute.** Stock imagery is
prohibited. Color grade is warm: skin to Onggi, shadows to Aubergine (never cool
blue-black), highlights holding in Parchment/Bone, outdoor greens in Jade/Peacock.
One photograph per slide, full bleed or ≥50%. Because real Section-10 photography
is required, this system ships **no images** — surfaces that need a photo use a
drop-in slot or are intentionally type-forward.

**Deck register (Section 14).** The deck is an editorial document, not the
restaurant. Bone/Parchment grounds dominate; Plum Ink is for section dividers (one
per section), Aubergine for major callouts (two or three per deck). The temporal
arc does **not** govern the deck. Left-aligned/asymmetric over centered; ≥10% margin
each side; one idea per slide; max four list items; the 선 glyph renders Plum Ink on
light and Bone on dark, **never Jade.**

---

## Iconography

The brand is **type-forward and icon-sparse by doctrine.** Iconography is
"present, reserved" — it enters only where the wordmark system cannot do the work
(wax seals, bag tags, embossed closures, small-format stamps, merchandise below
wordmark legibility). It is not a UI icon set.

- **No icon library.** Lucide/Heroicons/Material and the like are an explicit
  anti-pattern ("Lucide icons decorating every content block"). This system links
  no icon font and copies none in — there were none in the source to copy.
- **The 선 glyph is part of the logo**, set in the Korean companion face: a drawn
  logotype element, not an iconographic mark. It travels with the logo and is not
  mandated on every surface (2026-10-07). It is rendered with type, never as
  an SVG illustration. Its color resolves from `--son-glyph` per theme.
- **Future marks: reference only, not canon (2026-10-07).** The 원앙 /
  mandarin-duck bird mark is deferred; these notes are kept for reference. Future marks are
  silhouette-first, single closed path, legible at 18mm, built on the wordmark grid,
  always subordinate to the wordmark. None are executed yet — do not invent them.
- **Functional UI affordances** (the select chevron, the checkbox tick, the tab
  rule) are drawn as the simplest possible hairline/unicode marks, never as
  decorative icons.
- **Emoji and decorative unicode are prohibited** in brand voice and on surfaces.
- **The pattern system: reference only, not canon (2026-10-07).** The pattern
  (Joseon-era baekja lineage; geometry derived from the wordmark's own curve radii) is edge/accent scale only: never ground fill, never
  tiled letterforms. It is **deferred** here rather than fabricated, because any
  execution whose wordmark origin is untraceable is a prohibited result.

---

## Font substitutions (FLAGGED — needs your input)

- **Sandoll Myeongjo (산돌명조)** — the mandated Korean companion — was **not
  supplied** and is not web-licensed here. The substitute in this system is
  **Nanum Myeongjo** (Google Fonts), a true Myeongjo serif chosen for construction
  affinity. **Noto Serif KR is brand-prohibited and intentionally not used.** The
  선 glyph and Hangul dish names currently render in the substitute. *Please supply
  Sandoll Myeongjo web files to replace it before any production use.*
- GT Sectra "Fine" subfamily: the supplied files are labeled GT Sectra Book /
  Regular / Display. The wordmark uses **GT Sectra Book** as the "Fine Book"
  weight. If the licensed "Fine" optical cut differs, swap the `@font-face` src.

---

## Adherence

Codified pattern rules live in **`docs/codified-patterns.md`** (G3, ruled
2026-07-23): the enhancement inversion and its required delete-the-gate review
test, construction over synchronization, the motion register rules, the
conversion-surface document-stability rules, paired-encodings token governance,
delivery-name font governance, and the verification appendix. Read it before
building or reviewing any motion-carrying surface.

Four checks hold the canon, all wired into `npm run lint`; a violation blocks,
it does not warn. ESLint (`eslint.config.mjs`) enforces the **JSX** surface;
stylelint (`.stylelintrc.json`) enforces the **CSS and HTML** surfaces;
`adherence/check-copy.mjs` covers **copy** across the specimen cards, the seven
slides, the deck template, and the ui kits; `adherence/check-track.mjs` enforces
the **track's stacking invariant** (the load-bearing constraint of the still
layer — see `docs/codified-patterns.md`).

A correction of record (2026-07-23): this readme previously claimed oxlint
enforced the JSX surface. It never did — stock oxlint cannot parse
`_adherence.oxlintrc.json`'s x-omelette key or run its no-restricted-syntax
rules, so `lint:jsx` was a no-op and the JSX rules never blocked. The first
real run of those rules (as ESLint) found ~130 violations in the system's own
surfaces; see the JSX bullet for how they were resolved.

- **JSX** — `eslint.config.mjs` (authoritative, hand-owned; migrated from the
  compiler's oxlint artifact, which is retained for regeneration compatibility
  but consumed by nothing): raw hex, raw px, and non-design-system font
  families are canon-critical violations; component props are contract-checked
  against the props the components actually implement (the generated `.d.ts`
  files under-declare — they omit the DOM/event passthrough every component
  spreads; flagged for the next regeneration). Two honest scopes: the raw-px
  rule runs as a ratchet (a debt register in the config names the 13 files
  carrying ~91 pre-migration raw-px sites; those files keep every other rule,
  new files get the full set), and `ui_kits/good-energy/ios-frame.jsx` is
  exempt as device-bezel chrome, not a brand surface. Known rule limitation:
  only string literals containing "px" match — numeric style values
  (`fontSize: 14`) pass unflagged.
- **CSS / HTML / copy** — `.stylelintrc.json` (CSS color + font discipline) and
  `adherence/check-copy.mjs` (run `node adherence/check-copy.mjs`): design-system
  tokens only for color, approved font families only, no em dashes in specimen or
  slide copy, no forbidden-lexicon words, no references to removed tokens
  (`--son-color-white`, `--son-color-gold-foil`). Covers the specimen cards, the
  seven slides, the deck template, and the ui-kit surfaces — not only the JSX.
  Exits non-zero on violation. Sanctioned exceptions: the hex primitives in
  `tokens/colors.css`; the gold-foil stripe in `guidelines/colors-special.html`;
  comments (not copy \u2014 but printed `@dsCard`/`@template`/`@startingPoint` labels
  are checked); `guidelines-deck/` (rendered documentation that quotes both
  sides of the voice rules); infra files (`deck-stage.js`, `image-slot.js`,
  `ds-base.js`, `_ds_bundle.js`) and `uploads/`.

---

## Index / manifest

**Global entry** — consumers link one file: **`styles.css`** (imports the token +
base closure). Namespace for components in card HTML: `window.SNDesignSystem_4d795d`.

**This repo is source; compiler artifacts are snapshots (established
2026-07-23).** The authoritative surfaces are the ones you edit here:
`components/**/*.jsx`, the `tokens/*.css` layer, `track/`, `site/`,
`eslint.config.mjs`, and the docs. The compiler-generated files —
`_ds_bundle.js`, `_ds_manifest.json`, `_adherence.oxlintrc.json`, and the
`.d.ts` props files — are point-in-time outputs of an external compiler that
is not in this repo. They still serve the showcase pages, but they are no
longer authoritative: where a generated file disagrees with a source file,
the source file wins, and hand-edits to source do NOT flow into the bundle
until the external regeneration runs (which also drops the retired immersive
components). One manifest path was already hand-patched to fix a 404; treat
the generated set as stale-by-default.

**Runtime dependency — GSAP 3.12.5 (+ ScrollTrigger).** The one runtime
dependency beyond this system's own bundle, and required only by the immersive
components: `Chapter` (and any `[data-surface="immersive"]` scroll-narrative)
reads `window.gsap` / `window.ScrollTrigger` for its pin and scrub. Core, forms,
brand, navigation, the slides, and the deck template need nothing but
`styles.css` and `_ds_bundle.js`. Without GSAP — or under
`prefers-reduced-motion` — the immersive components collapse to static readable
stacks, so GSAP is a progressive enhancement, not a hard requirement for content.

**Immersive components FORMALLY RETIRED, 2026-07-23 (G3, ruled).** The register
they embed was retired at the track build (`tokens/motion-immersive.css` →
`tokens/motion-track.css`); the token layer no longer supports them. Their
prompt docs are marked superseded; the components drop from the bundle at the
next external regeneration (the compiler is not in this repo). With them gone,
the GSAP dependency goes too. Do not build new surfaces on them.

```
styles.css                      @import list only → the full closure
tokens/
  fonts.css                     @font-face (GT Sectra, GT Alpina) + Nanum Myeongjo import
  colors.css                    primitives + 4 daypart theme scopes
  typography.css                families, scale, weights, leading, tracking, measure
  spacing.css                   8pt grid, borders, radius, shadow, motion (UI register)
  motion-track.css              track register (--son-track-*), the scrub-led build's narrative motion
  base.css                      element defaults (.son-eyebrow, .son-kr, .son-glyph)
  components.css                pseudo-class interaction states for primitives
assets/fonts/                   the GT Sectra + GT Alpina .ttf binaries
components/
  brand/Wordmark               vertical lock-up · Latin · 선 (typographic)
  core/Button, Card, Badge, Divider
  forms/Input, Select, Checkbox, Switch
  navigation/Tabs
  immersive/FullBleedSection, Chapter, DaypartTakeover, AmbientField,
    ImageSlot, KineticDisplay, SectionHeader, SeededCTA, Marquee
                                narrative-site components, [data-surface="immersive"] only
guidelines/                     foundation specimen cards (Colors, Type, Spacing)
slides/                         seven sample slide cards (group "Slides", 1280×720)
templates/deck/                 runnable editorial deck template (@template)
ui_kits/
  son-website/                  reservation site, dinner register (home→reserve→confirmed)
  good-energy/                  morning standing-order app, son.theme.morning
SKILL.md                        portable Agent-Skill manifest
```

**Components** (all `window.SNDesignSystem_4d795d`): Wordmark, Button, Card, Badge,
Divider, Input, Select, Checkbox, Switch, Tabs. Each has a `.d.ts` props contract
and a `.prompt.md` usage note; each directory has one `@dsCard` showcase HTML.

**Anti-patterns to never reproduce** (from the brand's named failure modes): Jade
as a structural accent throughout; the dinner register as the dominant deck
surface; Inter/system-sans defaults; purple gradients; blue accents; drop-shadow
card layouts; left-border tinted callout boxes; uniform card padding across
content of unequal weight; AI/stock imagery.
