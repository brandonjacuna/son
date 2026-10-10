# Pre-ship check: reservation deposit step (from description, no code seen)

Verdict: not ready to ship. Four claims in the brief need correcting or verifying first.

## 1. "Out of PCI scope" is not accurate
A hosted iframe reduces scope; it does not remove it. Sŏn still validates (likely SAQ A, the shortest self-assessment questionnaire for merchants who fully outsource card entry). SAQ A eligibility now requires confirming the page hosting the iframe is protected against malicious scripts. This page loads an analytics tag and a chat widget, both third-party scripts that could overlay or alter the payment frame.
- Remove the analytics tag and chat widget from the deposit step, or document why each must stay.
- Add a Content Security Policy limiting scripts and frames to known sources.
- Confirm with the processor which SAQ applies and what they require of the host page.

## 2. "Contrast checked in Figma" does not cover the shipped page
Figma checks the static design, not the rendered states. Test in the browser:
- Focus rings, error text, placeholder text, disabled button, hover states.
- The processor iframe's own field styling (often configured separately).
- Text over any photo, and the cookie banner text.
Target WCAG 2.2 AA: 4.5:1 for text, 3:1 for field borders and focus indicators.

## 3. Red border alone is an accessibility failure
Color cannot be the only error signal (WCAG 1.4.1). Each invalid field needs:
- A text message next to it stating what to fix.
- `aria-invalid="true"` and `aria-describedby` linking the message.
- On submit, focus moves to the first error (or an error summary).
- Card errors from the iframe surfaced the same way, not only inside the frame.

## 4. Sticky cookie banner can hide the form
WCAG 2.2 criterion 2.4.11 fails if a focused field or the pay button sits under the banner. Check keyboard tabbing and mobile at 320px width and 200% zoom. Also confirm the analytics tag waits for or respects the consent choice; if it is an advertising pixel, the Texas Data Privacy and Security Act requires an opt-out for targeted advertising.

## Also check
- Deposit amount, cancellation window, and no-show forfeiture stated before the pay button, with a link to the full policy.
- Iframe has a `title`; full keyboard path works; 3-D Secure challenge renders on mobile.
- Any hold timer can be extended or warns before expiring.
- Pay button disables on submit; server uses an idempotency key so a double tap does not double charge.
- Chat widget cannot capture card details typed into it; consider hiding it on this step.
- Clear confirmation screen and email showing amount charged and refund terms.

## Needed to finish the review
The code, the processor name and integration type, the analytics vendor, and the cookie banner configuration.
