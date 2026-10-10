# Makers, routing, and the constraint floor

Read when routing, when two seats share a piece, when the maker is Claude Code, or when the artifact is a mark or a print piece.

## Route map
- M1. Route by what the artifact is and does.

| medium | seat | typical maker |
|---|---|---|
| print, menus, documents, long-form, non-investor decks | `editorial-layout-specialist` | coding session reading the design system, or a printer |
| screens, web, interface, token handoff | `web-ui-specialist` | coding session reading the design system |
| hero images, photo direction, campaign imagery | `image-campaign-specialist` | a real photographer |
| signs and physical surfaces in the space | `environmental-signage-specialist` (brief covers function and register only; placement and material are theirs) | a fabricator |
| a claude.ai artifact for a Sŏn surface | `artifact-design` owns the page contract; this seat decides whether an artifact is the right medium and writes its brief | a claude.ai artifact |
| a learning-studio module page | `materials-author-editor` owns the prose; this seat writes the layout brief once Brandon starts that work | |
| investor decks, exhibits, investor site | founder seats; no brief | |

- M2. A new mark or identity piece has no owning craft seat since the brand identity seat retired. Say so and ask Brandon through `interview` who makes it; do not assign it.
- M3. A seam is the handoff neither maker owns alone; the failure is each assuming the other has it. Name it in the route line with what each side must hold.
- M4. Sequence by dependency. A page that needs a campaign hero: the hero's owner goes first, so the page is built around a real asset rather than a placeholder swapped late. The page looks like the bigger job; it still waits.

## What a coding session already has, and what the brief still decides
- M5. The design system answers rules and vocabulary: tokens, type scale, color, spacing, motion timings, component props. It never answers one page's body. The brief decides:
  - function, audience, content, and hierarchy;
  - the register and therefore the theme;
  - the one primary action (component docs give props, not purpose);
  - the states the surface needs (error, confirmation, empty, reduced motion) and where a response renders (it never moves the document under the reader);
  - motion register per surface: UI motion for state change, track motion for narrative, kept separate;
  - photo-led from a named real source, or type-only (the system ships no images);
  - acceptance criteria a lint pass cannot check: rendered geometry, scroll behavior, visual judgment.

## Claude Code prompt grammar (the only tool prompt this seat writes)
- M6. Claude Code reads structure, not taste: Markdown, file paths, directory conventions. Map each visual decision to color, typography, spacing, shape, or structure, each by semantic role and token name from `tokens/`, never by value.
- M7. Every quality becomes a constraint the maker can honor or a file it can read. Interpretation is where defaults enter: each unspecified decision is filled from the training average.
- M8. House default watch: Claude's own style (warm cream ground, serif display, italic accents, terracotta) reads right for hospitality, so it can pass as on-brand. The prompt points at `styles.css` and adds the acceptance check: no color outside the eight tokens, no face outside `tokens/fonts.css`. Override any default with the system's named alternative, never a bare negation.

## Marks and print: designed is not delivered
- M9. Right in presentation, wrong in production is where identity and print work fail. Every mark or print brief requires:
  - a minimum-size variant: test the mark small; a simplified variant if it fails;
  - print color parity: Pantone coated and uncoated taken from the bridge, not algorithmic conversion; if the design system does not carry them, that is a named gap for Brandon;
  - prohibited-use notes, since guidelines that show only correct uses get reverse-engineered by production.
  A piece missing any of the three is not ready to ship; a missing Pantone is not a minor gap.

## Other makers
- M10. Any other generation tool is named with the maker and the constraint floor, never prompted here; its grammar lives in `kb/tools/`. No AI-generated imagery anywhere in the pipeline. Name each element that will not translate reliably to the named maker, with the workaround or a different maker.

## After the piece is made
- M11. Each craft seat critiques its own piece; this seat checks only that upstream content arrived unchanged, gaps were flagged rather than filled, and the seams held. A finding names its owner and whether it blocks.
