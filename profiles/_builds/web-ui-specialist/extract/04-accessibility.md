# 04 accessibility
source: W3C WCAG 2.2; DOJ Web Guidance 2022 (ada.gov); DOJ IFR 91 FR 20902, 20 Apr 2026 | read: criteria and 5.2 (partial), DOJ page, IFR | verified: yes; federalregister.gov blocked, read govinfo copy of 2026-07663

## Rows
| id | kind | row | quote | locator |
|---|---|---|---|---|
| 04.1 | rule | Draft until counsel. Test to WCAG 2.2 AA; it contains 2.1 AA, the Title II level. Inferred. | "backwards compatible with WCAG 2.1" | WCAG abstract |
| 04.2 | model | Draft until counsel. A restaurant sits under Title III general duties; WCAG is a reference, not a mandated method. | "have flexibility in how they comply" | DOJ |
| 04.3 | model | Draft until counsel. The Title II date extension (26 Apr 2027 / 2028) is for governments; never cite it as Sŏn relief. | "only pertains to the Department's regulations implementing title II" | 91 FR 20902 |
| 04.4 | anti | Reject "the scanner passed"; test by keyboard in a browser. | "A “clean” report does not necessarily mean everything is accessible." | DOJ |
| 04.5 | cue | Low contrast, color-only meaning, missing alt, unlabeled forms, mouse-only -> DOJ's named barriers -> check first -> block ship | | DOJ |
| 04.6 | cue | Red border as only error signal -> fails text identification -> add message text | "described to the user in text" | 3.3.1 (A) |
| 04.7 | rule | If a slot, stepper, or close control is under 24 by 24 CSS px, fail it; new in 2.2. | "at least 24 by 24 CSS pixels" | 2.5.8 (AA) |
| 04.8 | rule | If a sticky header or cookie banner covers the focused control, fail; tab the real page. | "not entirely hidden due to author-created content" | 2.4.11 (AA) |
| 04.9 | rule | If the flow re-asks given details or sets a login puzzle, fail. | "Information previously entered by or provided to the user" | 3.3.7 (A), 3.3.8 |
| 04.10 | rule | Contrast on the rendered background: 4.5:1 text, 3:1 controls. | "a contrast ratio of at least 4.5:1" | 1.4.3, 1.4.11 |
| 04.11 | decision | Draft until counsel. Conformance spans every page of a process, so a hosted processor page is in scope. Test end to end; flag vendor pages unverified. Third-party scope inferred. | "all web pages in the process conform at the specified level or better" | 5.2.3 |
| 04.12 | decision | Reduced motion is AAA (2.3.3), so the gate is Sŏn's own spec, not the legal reference. | "Motion animation triggered by interaction can be disabled" | 2.3.3 |
| 04.13 | decision | Draft until counsel. To counsel: claim exposure, Texas law, vendor terms, any "WCAG compliant" site claim. Seat sends level, criterion, URL; never clears. | | inferred |

## Tensions
- DOJ names no level for businesses; the only named level (2.1 AA) is in the Title II rule, while W3C's current version is 2.2.

## Not usable
- Texas law, claim volume, case outcomes: not in these sources. AAA criteria, Section 508, HHS and K-12 notes. DOJ page silent on third-party widgets.
