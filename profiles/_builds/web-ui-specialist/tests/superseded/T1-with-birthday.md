**Verdict: blocked.** Two R1 gates fail or are unverified: card-data scope (card input in our own form) and accessibility (contrast unmeasured in the render; error state fails 3.3.1). "Ship" is barred until both clear.

**Foundational**
1. Card-number input in a Sŏn form (C15, R10, M16, A4). Card fields live only in the processor's hosted element or behind a redirect. A card input in Sŏn markup puts our page in the payment path, likely wider than SAQ A (L8, L9; inferred). Direct: move card entry to the hosted iframe or a redirect; list every script loading on that page (L13). Not rated until that inventory exists.
2. Contrast "checked in Figma" (C10, A3, R9). The file is not the render. Direct: measure in the browser, light and dark OS mode (4.5:1 text, 3:1 controls), and on a device. Not rated.
3. Error is a red border only (C8, L4). Color-only meaning fails 3.3.1. Direct: each error says in text what failed, at its field; answer in place, block size frozen (R8).
4. Keyboard path untested (C12, L5). Tab the real flow end to end, vendor pages included: 2.4.11, 3.3.7, 3.3.8.

**Structural**
5. Browser-default focus rings (C9). Direct: one ring spec (color, offset, width) on every control.
6. Empty is a blank panel, loading a browser spinner (C8). Direct: both to primary quality from `components/` and `docs/codified-patterns.md` (R2).

**Data collected (R10).** Name, phone, email, birthday, dietary notes. For each: what does the screen tell the customer about where it goes? Nothing stated in what I was given. I do not propose what Sŏn collects. Dietary notes can carry allergy or health information: Brandon's and counsel's call.

**Flags for Brandon (one batch)**
- What the flow collects (five fields) and whether it takes a deposit; the card input implies a deposit no one has ruled on.
- Card-data exposure (L9): for counsel and the acquirer, who picks the SAQ (L14); request the processor's AOC for the exact service (L15). Draft until counsel.
- Accessibility: 3.3.1 (A) on errors; 1.4.3 and 1.4.11 (AA) unverified. URL attached once the flow has one.
- Does the flow assume a vendor? SevenRooms and Toast are candidates, not fact.

**Evidence needed (owner)**
- `npm run lint` output (session).
- `shoot` of every state, light and dark (session).
- Keyboard pass end to end, vendor pages included (session or Brandon).
- Field and script inventory for the payment step (engineering).

**Open question.** Is a hosted payment page already available, or is the in-form input the plan?

First fix: take the card input out of Sŏn markup.
