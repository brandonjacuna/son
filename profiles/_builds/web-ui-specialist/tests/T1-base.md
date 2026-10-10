# T1: Reservation flow, ready to ship?

**Verdict: No. Do not ship yet.** Five issues, two of them blocking for legal and security reasons.

## Blocking
1. **Card-number input rendered by our own form.** Raw card data touching our page puts the site in far broader PCI DSS scope (the payment card security standard). Use the payment provider's hosted fields or hosted checkout (iframe or redirect) so the number never passes through our code. If a card is not needed to hold a reservation, remove the field entirely. Confirm which: a card hold or deposit policy is a business decision.
2. **Data collection.** The form asks name, phone, email, birthday, dietary notes. A reservation needs name, party size, date/time, and one contact method. Birthday has no stated purpose; remove it or make it optional with a stated reason. Dietary notes are health-adjacent; make them optional, say how they are used, and keep them out of logs and analytics. Add a short privacy notice and consent wording near the submit button. Texas privacy law and the Texas Data Privacy and Security Act may apply; have counsel confirm.

## Must fix before release
3. **Contrast "checked in Figma".** Not sufficient. Figma does not test the shipped result (states, overlays on photo, disabled text). Run automated checks plus manual verification on the built page: body text 4.5:1, large text and UI components 3:1, including hover, focus, error, and disabled states.
4. **Browser-default focus rings.** They often fail against custom backgrounds. Provide a designed `:focus-visible` indicator with at least 3:1 contrast against adjacent colors, not removed, not clipped. Test full keyboard flow: tab order, no traps, date and time pickers operable by keyboard.
5. **Empty, loading, error states.**
   - Empty (no times available): explain why and give alternatives (other dates, waitlist, phone number).
   - Loading: spinner alone is not enough. Add text such as "Checking availability" in a live region (`aria-live="polite"`) and preserve layout to avoid shift.
   - Error: a red border alone fails color-independence. Add an icon and text message tied to the field (`aria-describedby`, `aria-invalid`), move focus to the first error or an error summary, and state how to fix it. Include a failed-network and a "slot just taken" state.

## Also check
- Mobile layout and touch targets of at least 44 px.
- Confirmation page and email: date, time, address, cancel/change route.
- Reduced motion, zoom to 200 percent, screen reader pass.
- Double-submit prevention.

## Next
Fix 1 and 2, rerun with built-page evidence for 3 to 5, then re-review.
