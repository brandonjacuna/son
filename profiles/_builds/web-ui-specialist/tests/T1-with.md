# Pre-ship: reservation deposit step

**Verdict: blocked** (customer-data gate and accessibility gate). No code or render received, so everything except the red-border finding is "not rated: evidence missing." Ship is barred while any R1 gate is unverified.

**First fix:** take the analytics tag and chat widget off the deposit step until counsel and the acquirer answer the scope question.

## Foundational
1. **Card-data scope is not "out of PCI scope."** (C15, A4, R1, R10) A hosted iframe makes this an SAQ A candidate, not out of scope. The script-protection criterion (PCI DSS 6.4.3, 11.6.1) still binds the page around the iframe, and two third-party scripts load on it. "Fields never leave the iframe" is necessary, not sufficient. Not rated: no script inventory. Fix directed: list every script on the page and whether it can touch the iframe or the DOM around it; obtain script protection from Sŏn's own techniques or the processor's written confirmation.
2. **Red border alone fails 3.3.1 (and 1.4.1, color-only meaning).** (C8, R1) Rated from your description. Fix directed: each invalid field says in text what failed and how to fix it, tied to the field programmatically; card errors from inside the iframe surface the same way.
3. **Sticky cookie banner over the focused control: 2.4.11 risk.** (C12) Not rated. Tab the real flow end to end, processor iframe and any 3-D Secure page included, at mobile width and 200% zoom. The pay button and the last field must never sit under the banner.
4. **"Contrast checked in Figma" is not a check of this page.** (C10, A3, R9) Not rated. Measure rendered: error text, focus ring, field borders, disabled pay button, iframe field styling, banner text, and under dark OS mode. 4.5:1 text, 3:1 controls.

## Structural (not rated)
- One focus ring spec across Sŏn inputs and the iframe's styled fields (C9).
- Submit answers in place with block size frozen; no layout jump on error or processing (R8). Feedback motion only (R4).
- Field list: what each field tells the customer about where data goes (R10).

## Flags for Brandon and counsel (one batch)
- Whether the reservation takes a deposit is Brandon's call; confirm it is decided before this ships.
- Card-data scope: analytics tag and chat widget on a payment page (PCI DSS 6.4.3, 11.6.1). The acquirer names the SAQ; ask the processor for its AOC (Attestation of Compliance) for the exact service used. Draft until counsel and acquirer.
- Accessibility: WCAG 2.2 AA 3.3.1, 1.4.1, 2.4.11, 1.4.3, 1.4.11 on this step; URL to attach. Vendor pages unverified.
- Which processor is this? Any design that assumes a vendor goes to Brandon.

## Evidence needed (owner)
- Code and URL of the step (engineering).
- `npm run lint` and `shoot` output, error and processing states, mobile and desktop (session).
- Script inventory on the page with sources (engineering).
- Keyboard pass end to end with the banner open (session or Brandon).
- Processor written confirmation on script protection, plus AOC (Brandon, via vendor).
