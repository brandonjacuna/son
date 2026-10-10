# T1: Pre-ship, reservation deposit step

**Verdict: blocked by two gates (card-data scope, error state), plus not rated on contrast, focus, and keyboard path (evidence missing).** "Ship" is barred while any R1 gate is unverified. The code was not attached; this is read from your description only, so no file or line is cited.

## Foundational (gates, ahead of every craft finding)

1. **Card-data scope is wider than the iframe (C15, R10, L10, L13, L16, A4).** "Hosted iframe, so out of PCI scope" is necessary, not sufficient. The script criterion still binds the page around the iframe. The analytics tag and the chat widget both load on a payment page. Each is a script that could, in principle, touch the page the iframe sits in.
   - Fix directed: list every script on this step and what it can read. Strip the chat widget and analytics from this step, or get the processor's written confirmation of script protection (PCI DSS 6.4.3, 11.6.1). Ask for the processor's AOC covering this exact service. Confirm the iframe, not a Sŏn component, is the only place a card or CVV field exists (M16). A redirect to the processor is the lowest scope (L11).
   - Evidence: not rated. Needs the network and script inventory from engineering.
   - Draft until counsel and acquirer. The seat does not pick the SAQ (L14).

2. **Red border alone fails 3.3.1 (C8, L4).** Color-only meaning is a DOJ-named barrier. Each invalid field needs text saying what failed, tied to the field, announced to assistive tech, with a non-color cue.
   - Fix directed: designed error state at primary quality; focus goes to the first error. Evidence: `shoot` of every error state.

3. **Contrast "checked in Figma" is not evidence (C10, A3, R9).** Measure the rendered page, under dark OS mode too: 4.5:1 text, 3:1 controls, including the red border against its background and the placeholder and helper text. Evidence: not rated.

4. **Sticky cookie banner (C12, 2.4.11).** It can cover the focused control, especially the iframe and submit button at 200% zoom and on a phone. Tab the real flow end to end, vendor iframe included, with the banner open. Evidence: not rated; needs a keyboard pass and a device.

## Structural and surface (not rated, no evidence)

- Focus ring spec on every control, and the iframe's own focus (C9, C16: re-measure what paints focused).
- Targets at least 24 by 24 CSS px, 44 house practice; text at 3x length (C11).
- Submit and processing states: freeze block size, answer in place (R8). Empty, loading, declined-card, and timeout states each need design (C8).
- Deposit step is a conversion surface: feedback motion only (R4).
- The iframe is a vendor page inside Sŏn's flow: its accessibility is unverified (L5).

## Flags for Brandon and counsel (one batch)

- Whether the reservation takes a deposit and what the step collects is Brandon's call. Confirm it is decided, not assumed.
- Card-data exposure from the tag and chat scripts: Brandon and counsel, finding attached (L9, L13). Counsel on the third-party reading of L5 and any vendor terms (L7).
- The step assumes a processor. Processor, and any of SevenRooms, Toast, Restaurant365, are candidates, not fact.

## Open questions and evidence owed

- Output of `npm run lint` (session or Brandon).
- `shoot` of the step in default, error, loading, and declined states, light and dark (session).
- Script inventory and processor written confirmation (engineering, vendor).
- Keyboard and device pass with the banner open (Brandon or session).
- Does the page contain a photo? If so: images unreviewed; `image-campaign-specialist` verdict required.
