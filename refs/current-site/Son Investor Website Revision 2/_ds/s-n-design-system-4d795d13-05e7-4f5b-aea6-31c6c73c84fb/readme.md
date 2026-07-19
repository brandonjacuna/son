# Sŏn — Design System

선 · Future Nostalgia Hospitality Group · 207 E St. Elmo Rd, Austin, Texas 78745

A Korean fine-dining restaurant in Austin. One master brand, four dayparts under
one roof: **Good Energy** (morning), **Dosi** (lunch), **Sŏn** (dinner), and a
late-night register (internal: Luxx, never public-facing). Good Energy and Dosi
are daypart *expressions* of Sŏn at this location, not separate brands. The 선
glyph appears on every daypart surface at a constant scale ratio — it is the sole
mandatory structural constant.

Positioning is three equal, unordered values: **Korean restraint · Texas warmth ·
polished but playful.** Texas warmth lives in the service, space, and voice — not
the letterforms.

> This design system encodes the brand's closed visual language as tokens,
> components, specimen cards, sample slides, a deck template, and two product UI
> kits. It is governed top-down by three Tier-1 cultural frameworks (below) that
> have veto power over every downstream decision.

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

## The three Tier-1 frameworks (always govern)

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

**Preferred terms** stand without translation: Jeong, Nunchi, Jaeyeonmi, Ma, Mahk,
Galbi, Dosirak, Banchan, Buncheong, Baekja, Pyeong-sang, Ganjang, Doenjang,
Gochujang, 선. Preparation is stated as decision, factually: scored, aged, braised,
pressed, set, rendered, reduced. Specific over categorical: "thirty days" not
"long-aged"; "white oak" not "hardwood."

**Examples (correct):**
- Menu, dinner: *Galbi / Aged thirty days. Scored before the fire.*
- Short-form digital: *Scored before the fire. Table available tonight.*
- Longer-form: *Most restaurants are pointed at the plate. We are pointed at the
  relationship. The plate is how we earn the right to have one.*
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
default (Bone / Parchment). **Jade is a named failure mode in the dinner register**
— it never appears there as text, accent, glyph, or decoration. Jade enters only
in the morning and as the late-night bar-back accent. Jade paired with Aubergine
or Plum Ink as the two dominant colors is a named failure mode anywhere.

**Type.** Two Latin faces, one Korean companion, and the ceiling is absolute.
*GT Sectra* (Fine Book is the wordmark weight; Display for headlines/section
headers) leads and is felt. *GT Alpina* (Fine Standard) follows and is read.
*Sandoll Myeongjo* governs all Hangul in production — see **Font substitutions**
below for the web stand-in. Body copy caps at ~65 characters, never above 75.

**Spacing & structure.** 8pt grid. **1px hairline** borders only — no 2px borders,
no double rules, no colored left-border accent boxes. Corners are near-square
(radius 0–2px); rounding reads as decoration and is used sparingly. Restraint over
decoration: silence is more luxurious than noise.

**Backgrounds.** Flat color surfaces from the palette. **No gradients of any kind.**
The editorial register (decks, most digital) lives on Bone/Parchment; the dinner
register lives on Plum Ink/Aubergine. No repeating patterns as ground fill — the
pattern system is edge/accent scale only (see Iconography). No textures applied in
post; texture is a material decision, not a design overlay.

**Shadows.** Effectively none. The system separates surfaces with hairline borders,
not drop shadows. Drop shadows on text or images are prohibited; so are bevels and
embossing. `--son-shadow-hairline` is the only sanctioned "elevation."

**Cards** are held surfaces: a single hairline border, no shadow, generous padding,
near-square corners. The empty margin is part of the composition.

**Motion** marks state change, never importance. Durations 100 / 200 / 400ms;
easing `cubic-bezier(0.4,0,0.2,1)` standard. No fade-up-on-scroll, no pulsing or
blinking for emphasis, no bounce/spring. One `prefers-reduced-motion` override
disables non-essential animation. Hover shifts color *within the palette* (or a
low-alpha wash); press reduces opacity slightly. No scale-on-press theatrics.

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
- **The 선 glyph is the primary mark**, set in the Korean companion face — a drawn
  logotype element, not an iconographic mark. It is rendered with type, never as
  an SVG illustration. Its color resolves from `--son-glyph` per theme.
- **Future marks** (the confirmed 원앙 / mandarin-duck bird mark is deferred) are
  silhouette-first, single closed path, legible at 18mm, built on the wordmark grid,
  always subordinate to the wordmark. None are executed yet — do not invent them.
- **Functional UI affordances** (the select chevron, the checkbox tick, the tab
  rule) are drawn as the simplest possible hairline/unicode marks, never as
  decorative icons.
- **Emoji and decorative unicode are prohibited** in brand voice and on surfaces.
- **The pattern system** (Joseon-era baekja lineage; geometry derived from the
  wordmark's own curve radii) is edge/accent scale only — never ground fill, never
  tiled letterforms. It is **deferred** here rather than fabricated, because any
  execution whose wordmark origin is untraceable is a prohibited result.

---

## Font substitutions (FLAGGED — needs your input)

- **Sandoll Myeongjo (산돌명조)** — the mandated Korean companion — was **not
  supplied** and is not web-licensed here. The substitute in this system is
  **Nanum Myeongjo** (Google Fonts), a true Myeongjo serif chosen for construction
  affinity. **Noto Serif KR is brand-prohibited and intentionally not used.** The
  선 glyph and all Hangul currently render in the substitute. *Please supply
  Sandoll Myeongjo web files to replace it before any production use.*
- GT Sectra "Fine" subfamily: the supplied files are labeled GT Sectra Book /
  Regular / Display. The wordmark uses **GT Sectra Book** as the "Fine Book"
  weight. If the licensed "Fine" optical cut differs, swap the `@font-face` src.

---

## Index / manifest

**Global entry** — consumers link one file: **`styles.css`** (imports the token +
base closure). Namespace for components in card HTML: `window.SNDesignSystem_4d795d`.

```
styles.css                      @import list only → the full closure
tokens/
  fonts.css                     @font-face (GT Sectra, GT Alpina) + Nanum Myeongjo import
  colors.css                    primitives + 4 daypart theme scopes
  typography.css                families, scale, weights, leading, tracking, measure
  spacing.css                   8pt grid, borders, radius, shadow, motion
  base.css                      element defaults (.son-eyebrow, .son-kr, .son-glyph)
  components.css                pseudo-class interaction states for primitives
assets/fonts/                   the GT Sectra + GT Alpina .ttf binaries
components/
  brand/Wordmark               vertical lock-up · Latin · 선 (typographic)
  core/Button, Card, Badge, Divider
  forms/Input, Select, Checkbox, Switch
  navigation/Tabs
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
