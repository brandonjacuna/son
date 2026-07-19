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
