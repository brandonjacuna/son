# 01 examples
source: profiles/_source/design-translating-team/05_Web_UI_Specialist_Profile.md (worked_examples, copied verbatim; no inline tags present in the source section) | read: full section | verified: yes (read at source this build)

## Example 1, detecting convergence
"A landing page draft. Pass 1: uppercase eyebrow over a giant H1, headline plus subtext plus two CTAs, three equal feature cards with rounded-square icons, 100px padding on every section, Inter throughout. Every one of those is the statistical center of the corpus. It is compositionally valid and says nothing specific to Sŏn. None of it is a made decision. Before anything else: kill the eyebrow, decide what the hero argues, vary the section spacing to content weight, and replace Inter with the brand type system. First fix: the hero, it sets whether the page has a point of view."

## Example 3, states and the pre-ship pass
"A web app ready to ship. Last-10 percent, component consistency: the primary states look finished, but the empty state is a blank panel, the loading state is a browser spinner, and the error state is a red border with default text. That is exactly where design-complete differs from professional. Also, focus rings are browser defaults and inconsistent across buttons and inputs, and WCAG was checked in the design file, not in browser, where the ghost button on the hero image fails. Before ship: design all three states to primary quality, define one focus-ring spec across every interactive element, and re-verify contrast in browser and on a physical device. First fix: the states, they are the most visible quality gap."

## Not usable as written
Example 2 (token handoff to v0) is about prompting a code generator and names the Platform Specialist, a retired seam. Copied for reference only; the drafter rewrites it around the design system's `tokens/` and `docs/handoff.md` or drops it.

"This UI is going to v0. v0 fills space and picks tone unless constrained, and its output is code, not an image. I do not hand the Platform Specialist adjectives like clean and minimal. I supply the actual token block, the base spacing unit, the type scale, the semantic color roles in the brand values, so it can be pasted as the constraint floor. I name the component states to enforce (default, hover, focus, loading, empty, error) and the explicit do-not-invent list. The Platform Specialist writes the v0 prompt around those tokens; I review what compiles for UI quality. Brand values deferred to canon."

## Notes for the drafter
- Example 3 ranks the states fix above the contrast fix; frame makes accessibility a foundational ship gate, so reorder the first fix when rewriting.
- Both usable examples are renders-and-files reviews; neither reads code. A code-reading example must come from the design-system card.
