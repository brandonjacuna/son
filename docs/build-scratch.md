# Build session: registers and scratch list

The two canon registers for the build session, kept live per pass, extending
the registers in `docs/content-architecture.md` and `docs/design-language.md`.
Plus the scratch list: patterns invented during the build that do not enter
the design system until codification at P7 (the G3 gate).

## Excluded by canon

### Pass 1, structure and type

- A meta description and social preview text in the document head. Closed by:
  copy is approved and closed; every external-surface sentence comes from
  `docs/copy.md`, and no meta description exists there. What it would have
  bought: search and link-preview framing. Low cost on a warm, forwarded
  funnel where the forwarding unit is the URL itself. The `<title>` is
  composed strictly from approved strings ("Sŏn" plus "Austin, Texas.").
- A sans-serif for the form controls (inputs, labels, submit). Closed by: the
  two-Latin-plus-one-Korean face limit and the canon body face (GT Alpina
  Fine). What it would have bought: conventional "UI clarity" on the one
  interactive surface. The form reads editorial instead, which suits an ask
  that is a request, not a checkout.
- Sizing the hero lock-up toward Display scale for more counterweight mass.
  Closed by: content-architecture fixes exactly two Display moments (the hero
  sentence, the moat pull-line); a Display-scale lock-up would be a third
  largest voice. Held at Headline scale. What it would have bought: heavier
  low-right mass on the hero diagonal.

### Pass 2, ground and color

- Drop shadow on the ask's Bone card. Closed by: the no-shadow rule
  (`tokens/spacing.css`, hairline separation only). What it would have
  bought: conventional card elevation against the dark commit ground. The
  bone-on-aubergine hard edge carries the separation instead, and reads
  cleaner than a lift would.

### Pass 3, the 선 system and the band

- Full-bleed, edge-to-edge band. Closed by: the settled span (the band runs
  from "First light" on the left to "Last call" on the right, so the labels
  bound it) and the 10% page-margin Ma, which is specified emptiness. What
  it would have bought: a harder, more cinematic rupture. The band stays
  inside the reading column, and its saturation carries the rupture.
- A hairline frame on the peacock accent field. Closed by: the hairline
  system's refusal of decorative dividers, and the accent's own admission
  terms: it earns through as a single semantic instance, and ornament would
  tip it toward 선-as-decoration, which page 03 resists. What it would have
  bought: a crisper edge against Bone. The peacock-on-bone cut needs no
  help.

## Reconsidered, admitted in a disciplined form

### Pass 1, structure and type

- None. Nothing was reopened against canon this pass.

### Pass 2, ground and color

- None. Nothing was reopened against canon this pass.

### Pass 3, the 선 system and the band

- None. Nothing was reopened against canon this pass. One reading recorded
  for transparency, not reopened: the footer carries both the lock-up and
  the bare closing mark, and the rationing rule says at most one 선 event
  per section. The approved copy and the motion spec both specify the two
  footer instances explicitly, so the rule is read as governing designed
  graphic events (nothing added beyond what the copy ships), not as
  overriding the approved copy. No conflict is live.

## Pass 2 gate: the corner on Plum Ink

Run before the arc was built, per direction. Evidence:
`refs/shots/lockup-test/gate-1440-plum.png` and `gate-390-plum.png`.
Verdict: Headline holds on the real ground, at both widths, and holds
better than it did on Bone. Light-on-dark inverts the mass economics: on
Bone the lock-up was an ink spot that wanted weight; on Plum Ink it is the
only luminous object in the hero's lower half, so isolation does the
counterweight work scale would otherwise be asked to do. The open low-left
reads as night atmosphere rather than blank paper, which strengthens the
diagonal exit into the moat. No scale change made or needed.

## Between passes 1 and 2

- Korean face conflict resolved toward self-hosting. The Google Fonts import
  in `tokens/fonts.css` conflicted with the settled self-hosted-fonts
  requirement. Box 388972713490 holds no Sandoll Myeongjo web files; it holds
  NanumMyeongjo Regular, Bold, and ExtraBold, the already-documented
  substitute, uploaded 2026-06-10. The import is removed and replaced with
  three self-hosted @font-face declarations pointing at
  `assets/fonts/NanumMyeongjo-*.ttf`. The binaries are pending a hand-copy
  from Box (the text-only MCP cannot deliver binaries, and the download path
  is closed to the build agent); file ids and sha1s are recorded in
  `tokens/fonts.css`. Until they land, 선 renders on a local Myeongjo
  (Apple Myungjo or Batang), never a sans. The face identity is unchanged;
  only the delivery moved. Sandoll Myeongjo web licensing remains the open
  production question.
- Lock-up scale tested against its counterweight job at both widths, evidence
  in `refs/shots/lockup-test/`. Headline holds. At 390 the glyph (45px)
  already sits within 8% of the display sentence (48.8px), so there is no
  upward headroom without inverting the largest-voice rule on the width most
  readers arrive at. At 1440x900 the 1.25x variant grows the hero past the
  fold and the viewport bottom cuts through 선 in the first-viewport
  presentation, the partial-glyph condition the mark spec forbids. The
  counterweight job is carried by isolation, the empty right column and the
  open low-left Ma, more than by point size. Re-verify the corner's perceived
  weight at pass 2 when the ground inverts to Plum Ink.

## Korean subset, resolved before pass 2

The site's Korean glyph inventory is exactly one glyph: 선 (U+C120), weight
400, across every surface that will ever render it (hero lock-up, moat
atmosphere, opportunity accent, footer lock-up and closing mark). All other
Korean in the corpus (여백의 미) is internal-doc language, never on a site
surface. Shipped as `assets/fonts/SeonMyeongjo-Regular.woff2`, 1,924 bytes, a
subset of the OFL Nanum Myeongjo build (google/fonts v2.032), renamed because
"Nanum" and "NanumMyeongjo" are OFL Reserved Font Names and a subset is a
Modified Version; copyright and license name records retained; license text
at `assets/fonts/SeonMyeongjo-OFL.txt`; scoped by `unicode-range: U+C120`.
Provenance disclosed: the subset derives from the google/fonts build, not the
Box artifact (different build, sha1s differ; Box copy is likely Naver's
original distribution). Regenerating from the Box artifact is a five-minute
job if preferred. Adding Korean copy to any external surface requires
regenerating the subset; the unicode-range scoping makes the failure mode
visible (new glyphs fall to a local Myeongjo, never a sans).

## Between passes 2 and 3: the 선 delivery test

Directed test, no path built. Question: all site uses of 선 may be graphic,
not text, making a font the wrong delivery mechanism. Findings, evidence at
`refs/shots/seon-svg-test/`:

- Every 선 instance on the site is graphic: the two lock-ups (canon already
  treats the lock-up as a drawn mark under the balance spec), the moat
  atmosphere (texture), the opportunity accent (a glyph in a field, no
  caption), and the footer closing mark (a seal). None participates in a
  sentence. Nothing functional breaks if all become drawn; find-in-page and
  selection of a one-glyph mark are nil costs.
- The SVG path extracted from the shipped subset's own outline (1,363 bytes
  of path data, upm 1024, advance 973, tight-crop file 1,484 bytes) renders
  identically to the font at 12, 45, 67, 240, and 640px, both polarities,
  including the 7%-opacity atmosphere treatment. Identity is by
  construction; rasterization parity verified at 2x DPR. Caveat recorded:
  at 12px on low-DPI displays font grid-fitting could differ marginally.
- A drawn path makes the mark invariant. As a font, the mark can flash a
  system Myeongjo (Batang on Windows) under font-display swap or any load
  failure, which puts the drawn-balance spec at the mercy of delivery. SVG
  removes that failure class.
- If SVG ships: the wordmark step's definition ("with 선 in the Korean
  face") needs a one-sentence canon amendment, which is Brandon's, not the
  builder's. Accessibility pattern: lock-up container role="img"
  aria-label="Sŏn 선"; footer mark role="img" aria-label="선"; atmosphere
  and accent aria-hidden.
- Sandoll reframe: with no font software served, there is no webfont or
  file-provision license in play at all; the remaining question is purely
  whether to redraw the mark on Sandoll's letterform, a one-time logotype
  conversation.

**Resolution: SVG, confirmed by Brandon.** The invariance argument settled
it: a font leaves the mark exposed to a system Myeongjo during swap or on
load failure, so the balance spec only holds when delivery cooperates. A
drawn mark should be drawn. Disposition executed: the subset woff2, its
@font-face, the unicode-range rule, the OFL.txt, and the "Seon Myeongjo"
lint allow-list entries are removed; the drawn path (1,363 bytes) lives as
`#seon-path` in `site/index.html` with provenance in the adjacent comment;
the wordmark definition is amended in `tokens/typography.css` with Brandon's
verbatim wording; the Korean font stack stays for internal text surfaces.
Accessibility: each lock-up is one named object (`role="img"`,
`aria-label="Sŏn 선"`), the closing mark is named (`aria-label="선"`), the
atmosphere and accent are `aria-hidden`. Door recorded: Korean text on any
external surface reopens font delivery.

## Open items carried to P7

- Founder headshots: real portraits do not exist yet; the reserved hairline
  frames stand. Brandon owns the portraits.
- Full Nanum Myeongjo binaries on disk: OPTIONAL now the subset ships and no
  external surface needs any other Hangul. Brandon decides whether to
  hand-copy any of the three weights from Box; the pending declarations in
  `tokens/fonts.css` fail silently (one 404 per declared weight per cold
  load) until then, and can be deleted instead.

## Parked, not open

- Sandoll Myeongjo. With 선 delivered as a drawn path, no font software is
  served and no webfont or file-provision license is in play. The remaining
  question is purely aesthetic, whether Sandoll's drawing of 선 is better
  than the current Nanum-derived form, and the current mark is legally
  settled without them (glyph-as-artwork is unrestricted OFL use). That is a
  brand-level question for after the raise, not a website decision. Parked
  by Brandon, off the build's open items.

## Scratch list (new patterns, not in the system until P7)

- Type-step utility classes (`.t-display` … `.t-fine`) mapping the nine-step
  scale 1:1 onto classes; candidate for the design system at codification.
- The lock-up as a reusable component (`.lockup`: Latin over centered 선 at
  the Korean optical up-scale).
- Reserved headshot slot pattern (`figure.headshot[data-slot]`, hairline
  frame, 3:4).
- Font preload hints for the four critical faces (deferred; consider at
  pass 6 polish).
- `site/` added to the copy-adherence scope in `adherence/check-copy.mjs`
  (enforcement scope, not a design pattern; recorded so it is reviewed).
- The `.ask-card` pattern: a light card inside a dark themed section that
  re-resolves the semantic tokens (text, borders, focus ring, accent) to the
  base editorial register. Candidate for a system-level surface-card
  primitive at P7.
- Chrome stacking: `.site-header` carries `z-index: 2` so painted section
  grounds cannot occlude the absolutely positioned header.
- "Seon Myeongjo" added to the two lint font allow-lists (enforcement scope,
  recorded so it is reviewed). Superseded: the allow-list entries were
  removed with the subset when 선 moved to the drawn path.
- The drawn-mark pattern: one `#seon-path` definition, per-instance `<svg>`
  plus `<use>`, sized in em against the type it accompanies, colored via
  currentColor so the theme tokens resolve it. P7 candidate.
- The daypart band component: label-bounded grid, four equal stripes,
  vertical eyebrow labels on desktop, stacks top-to-bottom on mobile. P7
  candidate.
- The atmosphere placement pattern: absolutely positioned background glyph
  with sibling z-index lift (`.slot-moat > :not(.moat-atmo)`). P7 candidate.
