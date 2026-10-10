# T3: Landing section review

**Summary:** The draft is a generic SaaS template. Nothing in it says Sŏn, a Korean restaurant. The mechanics are fine; the identity and system discipline are missing.

## Findings

**1. Layout is the default startup pattern.**
Uppercase eyebrow over giant headline, subtext, two buttons, three equal cards with rounded icons is the most common landing structure on the web. It carries no point of view. Decide what the section must do (invite a reservation, show the menu, introduce the place) and let that set the layout. Break the symmetry: one lead item larger than the others, or lead with an image of the food or room.

**2. Two buttons.**
Two competing actions dilute the one that matters. One primary action (reserve), and a quieter text link for the secondary.

**3. Three equal cards with rounded icons.**
Stock icons do the work photography or specific copy should do. Replace icons with real images or specific facts. If cards stay, vary their weight and keep radius consistent with the system.

**4. 100px padding on every section.**
Uniform spacing flattens rhythm. Use spacing tokens on a scale, with tighter spacing inside related groups and larger breaks between ideas. Make it responsive; 100px on mobile wastes the screen.

**5. Inter throughout.**
Inter is neutral and ubiquitous. Use the Sŏn design-system typefaces, with a hierarchy (display, text, label), and check that Hangul text has a paired face with matching weights and line height.

**6. Hex literals.**
Colors must come from design-system tokens (CSS variables). Literals drift and break theming and contrast audits. List every literal and map it to an existing token; flag the ones with no token for design decision.

**7. Uppercase eyebrow.**
Fine in small doses, but uppercase with letter spacing and a giant headline together is formula. Use it only if it carries information; with Korean text, uppercase does not apply, so check the pattern works in both scripts.

## Missing from the review (need the code)
Contrast, focus states, responsive behavior, image alt text, heading order (one h1), copy rules ("customer" not "guest," no em dashes, declarative voice).

## Priority
Tokens (6) and the single primary action (2) first; structure and typography (1, 3, 5) next; spacing (4) alongside.
