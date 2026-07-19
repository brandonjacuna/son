# Current site inventory

A plain record of the current investor site as it exists in the Claude Design
export at `refs/current-site/Son Investor Website Revision 2/`. Observations
only. No judgment, no comparison to the extraction spec, no recommendations.

## What was captured

The renderable page is `Son Investor Site (Standalone).html`, an 8.2 MB
self-contained bundle. It opens correctly from a local file path: fonts (GT
Sectra, GT Alpina), the 선 glyph, daypart surface colors, and image placeholders
all render without a server. Captures are in `refs/shots/current/` at desktop
(1440px) and mobile (390px) widths, each a full-page image plus viewport-height
slices top to bottom.

The page is one scrolling document, dinner register, with anchor navigation. It
holds eight surfaces in this order.

## Sections in order

1. **Hero** (`#top`, Plum Ink). A top nav with the Sŏn wordmark on the left and,
   on the right, a "By request only" note and a "Request the briefing" button.
   One display headline: "One Korean room in St. Elmo, open from first light to
   last call. Fine dining at dinner. A standing order by morning." A "St. Elmo ·
   South Austin" tag sits low left, with a large Sŏn / 선 lock-up low right. Copy
   is minimal, a single sentence carrying the screen.

2. **01 The concept** (`#concept`, Bone). Eyebrow "01 · The concept", then a
   staggered block of one headline and three short paragraphs that step down and
   across the grid. Theme is "One room. One kitchen. One team," and the business
   pointed at the relationship rather than the plate. Copy is light to moderate,
   roughly ninety words spread across four staggered pieces.

3. **02 Why this** (`#why`, Plum Ink). The longest section. Eyebrow "02 · Why
   this", then a narrative about Renata, a floor manager who carries the room's
   memory and is leaving. It runs three body paragraphs, one display pull-line
   ("Tonight is her last night."), a large centered blockquote ("What looks like
   a people business is a memory business, and the restaurant remembered
   nothing."), and two closing paragraphs about what compounds in a restaurant. A
   large 선 glyph sits behind the text at low opacity. Copy is heavy, roughly two
   hundred and thirty words, the narrative core of the page.

4. **03 The opportunity** (`#opportunity`, Bone, split layout). Eyebrow "03 · The
   opportunity", a headline about Korean cooking reaching top recognition, and
   two short supporting lines about Austin and the customer already being here.
   The right half is a colored field holding a 선 glyph with a caption, "Room
   photography to come. Found light, no stock, no AI." Copy is light to moderate,
   roughly sixty words.

5. **04 The team** (`#team`, Parchment). Eyebrow "04 · The team", then two
   founder cards side by side: Brandon Acuña-Cardona (operations and strategy)
   and Dominic Thomas (capital and systems), each with a portrait placeholder and
   a bio of about fifty words. Below them a full-width room-photo placeholder.
   All three image areas are unfilled slots showing "Portrait to come" and "Room
   photography to come." Copy is moderate, roughly one hundred and ten words plus
   captions.

6. **05 The model** (`#model`, Bone). Eyebrow "05 · The model" and a headline
   about one footprint carrying coffee, lunch, dinner, and late night against one
   set of fixed costs. A four-stripe band spans the width, "First light" to "Last
   call," each stripe a daypart in its own color (Coffee jade, Lunch onggi,
   Dinner plum ink, Late night aubergine) with vertical labels. Two closing
   paragraphs follow, the second linking "in the briefing." Copy is moderate,
   roughly sixty words plus the band labels.

7. **06 The ask** (`#ask`, Aubergine). Eyebrow "06 · The ask" and a centered
   headline, "We share the briefing with a small number of partners." A request
   form on a Bone card takes full name, email, company or affiliation, and a
   short "What interests you about Sŏn?" note, with a Submit button. On submit it
   validates name and email, shows "Sending." briefly, then swaps to a success
   panel ("Your request is in. You will hear from us within a day."). A legal
   line closes it: "By submitting this, you are requesting access to our
   materials. This is not an offer to sell securities." Copy is light, the form
   carries the section.

8. **Footer** (Plum Ink). A Sŏn / 선 lock-up, the line "South Austin. By request
   only.", and a "선 · St. Elmo" mark. A quiet close with no further call to
   action.

## Motion

Motion is minimal. The page uses smooth scrolling for its anchor links, disabled
under `prefers-reduced-motion`. Buttons and form fields carry hover and focus
transitions on border and background, but every motion duration token in the
system resolves to 0ms, so those state changes are effectively instant. There
are no scroll-triggered reveals, no parallax, and no autoplay. The large 선
glyphs are static. The only time-based change on the page is the ask form's
simulated submission, which pauses about nine tenths of a second before showing
the success panel.

## Calls to action

Every path leads to the request form in section 06.

- "Request the briefing" button in the hero nav, anchors to `#ask`.
- "in the briefing" inline link in section 05, anchors to `#ask`.
- The request form itself in section 06 is the terminal conversion.

"By request only," repeated in the hero nav and the footer, frames access rather
than acting as a button.

## How it ends

The footer closes on the wordmark and the two lines "South Austin. By request
only." and "선 · St. Elmo." No newsletter, no social row, no repeated form. The
page ends the way it opens, on the mark and the location.

## What the export contains beyond the page

The export folder holds the page in three forms plus a design-system bundle.

Authored source and durable inputs:

- `Son Investor Site.dc.html` (33 KB). The design-compiler source. It uses
  `<x-dc>` markup and links the `_ds/` token stylesheets and `support.js`. This
  is the editable page of record. It exposes three editor props: an ask-surface
  choice (aubergine or peacock), an opportunity-field choice (peacock or jade),
  and a glyph-opacity range. The standalone applies the defaults (aubergine,
  peacock, 0.07).
- `_ds/.../readme.md`. The design system readme.
- `_ds/.../tokens/*.css` (fonts, colors, typography, spacing, base, components)
  and `styles.css`. The design tokens and system CSS.
- `_ds/.../assets/fonts/*.ttf`. Eighteen GT Sectra and GT Alpina font files.

Compiler generated, would be regenerated on a re-export and should not be edited
by hand:

- `Son Investor Site (Standalone).html` (8.2 MB). The self-contained bundle. It
  inlines the compiled app, CSS, and fonts into one file. This is what renders
  offline; it is a build output, not a source.
- `standalone-src.html` (33 KB). The pre-bundle standalone source. Same page
  markup as the `.dc.html`, but wired to load React from a CDN.
- `support.js` (61 KB). The design-compiler runtime, including the `DCLogic`
  base class and the `<x-dc>` renderer.
- `image-slot.js` (53 KB). The image-placeholder web component used for the
  portrait and room slots.
- `.thumbnail` (4 KB). A generated preview thumbnail.
- `_ds/.../_ds_bundle.js`. The compiled component bundle.
- `_ds/.../_ds_manifest.json`. A manifest of components, tokens, fonts, themes,
  and starting points.
- `_ds/.../_adherence.oxlintrc.json`. A generated adherence lint config.
- The `_ds/` folder name carries a generated namespace hash
  (`s-n-design-system-4d795d13-05e7-4f5b-aea6-31c6c73c84fb`, manifest namespace
  `SNDesignSystem_4d795d`). That identifier would change on a re-export.

No video accompanied this export, and `refs/clips/` holds none, so there was
nothing to decompose into frames this session.
