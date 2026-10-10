# Legal rows: accessibility exposure and card-data scope

**Status: draft until counsel.** Every row below is a draft until counsel signs (and, for card data, until the acquirer confirms). The seat uses these rows to frame a flag for Brandon and counsel, never to clear or rule. When a row is confirmed, it moves to a `kb/domains/` page with `last_verified`.

Terms, one sentence each:
- Title III: the part of the Americans with Disabilities Act covering private businesses open to the public, restaurants included.
- WCAG: the W3C's Web Content Accessibility Guidelines; levels A, AA, AAA, AA being the level cited in practice.
- PCI DSS: the card industry's security standard any business taking card payments must meet.
- SAQ: Self-Assessment Questionnaire, the PCI form a smaller merchant completes; SAQ A is the narrowest, SAQ A-EP covers sites that shape the payment page.
- Acquirer: the bank that processes Sŏn's card payments and decides which SAQ applies.
- AOC: Attestation of Compliance, a processor's signed statement that a named service meets PCI DSS.

## Accessibility (draft until counsel)
| id | row |
|---|---|
| L1 | Test to WCAG 2.2 AA. It contains 2.1 AA, the only level a federal rule names (the Title II rule for governments). Draft until counsel. |
| L2 | A restaurant sits under Title III general duties. DOJ treats WCAG as a reference, not a mandated method, and names no level for businesses. Draft until counsel. |
| L3 | The Title II compliance-date extension (26 April 2027 / 2028) is for state and local governments. Never cite it as relief for Sŏn. Draft until counsel. |
| L4 | DOJ's named barriers are low contrast, color-only meaning, missing alt text, unlabeled form fields, and mouse-only controls. Check these first; each blocks ship. Draft until counsel. |
| L5 | Conformance spans every page of a process, so a hosted reservation or payment page inside Sŏn's flow is in scope. Test end to end; flag vendor pages as unverified. The third-party reading is inferred. Draft until counsel. |
| L6 | Reduced motion on interaction (2.3.3) is AAA. The gate on it is Sŏn's own design-system spec, not a legal reference. Draft until counsel. |
| L7 | Routed to counsel, never decided by the seat: claim exposure, Texas law, vendor terms, and any "WCAG compliant" statement on the site. The seat sends level, criterion, and URL. Draft until counsel. |

## Card-data scope (draft until counsel and acquirer)
| id | row |
|---|---|
| L8 | A hosted iframe served by the processor is an SAQ A candidate; card inputs rendered in Sŏn's own markup make Sŏn's page part of the payment path (A-EP). Draft until counsel and acquirer. |
| L9 | A card or CVV input in a Sŏn component means Sŏn's site affects the payment page even though Sŏn never receives the data; likely not SAQ A (inferred). Flag Brandon and counsel. Draft until counsel and acquirer. |
| L10 | If the page embeds a processor iframe, the script-protection criterion binds Sŏn's surrounding page. Draft until counsel and acquirer. |
| L11 | If checkout redirects to the processor (30x, meta refresh, or JS), the script criterion does not apply; this is the lowest scope. Draft until counsel and acquirer. |
| L12 | Script protection comes from Sŏn's own techniques (PCI DSS 6.4.3, 11.6.1) or the processor's written confirmation. Never assume it; get it in writing. Draft until counsel and acquirer. |
| L13 | List every analytics, chat, or tag script that loads on a payment page and ask whether it can touch card data. Draft until counsel and acquirer. |
| L14 | The acquirer says which SAQ applies and whether Sŏn submits one; the seat never picks. Draft until counsel and acquirer. |
| L15 | Ask the processor for its AOC covering the exact service Sŏn uses. Draft until counsel and acquirer. |
| L16 | "Fields never leave the hosted element" is necessary, not sufficient: the script criterion still binds the page around it. Draft until counsel and acquirer. |

## Team-member screens (draft until counsel)
| id | row |
|---|---|
| L17 | A screen team members operate is an accommodation matter for Brandon and counsel, not Title III. Draft until counsel. |

## Not covered
Texas accessibility law, claim volume and case outcomes, third-party widget terms, the current SAQ A wording (not read at source), PCI DSS 4.0.1 changes (A-EP read at v4.0), whether a reservation takes a deposit (Brandon's call), and employee-used screens.
