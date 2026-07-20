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

## Reconsidered, admitted in a disciplined form

### Pass 1, structure and type

- None. Nothing was reopened against canon this pass.

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

## Open items carried to P7

- Founder headshots: real portraits do not exist yet; the reserved hairline
  frames stand. Brandon owns the portraits.
- Nanum Myeongjo binaries: hand-copy from Box into `assets/fonts` under the
  exact names in `tokens/fonts.css`.
- OFL license text should accompany the self-hosted Nanum files when they
  land (SIL OFL redistribution requirement).
- Korean font weight: the TTFs are 3.7 to 4.4MB each; woff2 conversion or
  Hangul subsetting is a production optimization needing tooling and a
  decision.
- Sandoll Myeongjo web license: the production Korean face is still not
  licensed for web.

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
