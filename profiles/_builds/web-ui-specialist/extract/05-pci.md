# 05 PCI SSC card scope
source: PCI SSC FAQ 1588 (Feb 2025); SAQ A-EP v4.0 (Apr 2022) | read: FAQ full; A-EP pp. i-v; SAQ A r1 not reached (404), via PCI blog, Adyen | verified: yes (FAQ, A-EP); no (SAQ A wording)

## Rows
Every row is draft until counsel and the acquirer confirm.
| id | kind | row | quote | locator |
|---|---|---|---|---|
| 05.1 | model | Hosted iframe = page from processor (SAQ A candidate); card inputs in Sŏn markup = merchant elements (A-EP). [draft: counsel, acquirer] | "originates from either the merchant's website or a PCI DSS compliant TPSP" | A-EP p. iii |
| 05.2 | cue | Card or CVV input in Sŏn's own component -> site affects the page though Sŏn never receives data -> not SAQ A (inferred) -> flag Brandon, counsel. [draft: counsel, acquirer] | "does not itself receive account data but which does affect the security" | A-EP p. iii |
| 05.3 | rule | If the page embeds a processor iframe, the script criterion binds Sŏn's surrounding page. [draft: counsel, acquirer] | "not susceptible to attacks from scripts" | FAQ 1588 |
| 05.4 | rule | If checkout redirects (30x, meta refresh, JS), the script criterion does not apply; lowest scope. [draft: counsel, acquirer] | "does not apply to e-commerce merchants with a webpage that redirects customers" | FAQ 1588 |
| 05.5 | decision | Script protection: own techniques (6.4.3, 11.6.1) or processor confirmation; novice assumes it. Get it in writing. [draft: counsel, acquirer] | "Obtaining confirmation from the merchant's PCI DSS compliant TPSP/payment processor" | FAQ 1588 |
| 05.6 | rule | If analytics, chat, or tag scripts load on the payment page, list each; ask if it can touch card data. [draft: counsel, acquirer] | | FAQ 1588, paraphrase |
| 05.7 | rule | Ask the acquirer which SAQ applies and whether Sŏn submits; the seat never picks. [draft: counsel, acquirer] | "continue to consult with their compliance-accepting entity" | FAQ 1588 |
| 05.8 | rule | Ask the processor for its AOC covering the exact service used. [draft: counsel, acquirer] | "PCI DSS compliant for the services used by the merchant" | A-EP p. iii |
| 05.9 | anti | Rejects "we never see the card, so SAQ A": A-EP covers sites that affect, not receive, data. [draft: counsel, acquirer] | "directly impacts how account data is transmitted" | A-EP p. iii |

## Tensions
- "Fields never outside the hosted element" is necessary, not sufficient: the script criterion still binds Sŏn's page.

## Not usable
- SAQ A r1 wording; "6.4.3/11.6.1 removed from SAQ A": secondary, re-read at PCI SSC.
- A-EP read is v4.0, not 4.0.1.
- 7-day change-detection figure: vendor blogs only.
- Whether a reservation needs a deposit: Brandon's call.
