# SaaS Map — Duplicates & Vendor-Name Mismatches (Open Items List)

Local analysis only. Nothing here has been merged, renamed, or resolved — this is a punch list for the Dominic tech review pass. Source: `exports/2026-09-16-baseline/tasks/saas-map.json` (241 tasks), `exports/2026-09-16-baseline/tasks/saas-catalog.json` (46 tasks), `exports/2026-09-16-baseline/lists/901323733488-fields.json` (Solution dropdown, 57 options), and `audit/technology.md`.

## (a) Duplicate / near-duplicate task pairs in the Function → SaaS Map

27 pairs found (the audit estimated "~10+ pairs" / "~15-20 rows" — this is the fuller list, including several 3-way clusters that show up as more than one pair below).

| Task A (id, name) | Task B (id, name) | Why they look like duplicates |
|---|---|---|
| 86ae8p19z, Reservation Management | 86ae4mj0g, Reservation Management | Identical name, both mapped to SevenRooms |
| 86ae8p4bu, Inventory Management | 86ae4mhhx, Inventory Management | Identical name, both mapped to Restaurant 365 |
| 86ae8p6h3, Performance Management | 86ae4mhy4, Performance Management | Identical name, both mapped to Rippling |
| 86ae4n17u, Tip Management | 86ae4mj2f, Tip Management | Identical name but assigned to two different vendors (TipHaus vs. Deputy) — conflicting, not just duplicated |
| 86ae4mhu4, Payroll | 86ae8p57a, Payroll Processing | Same function, same vendor (Rippling), different naming pass |
| 86ae4mhja, POS | 86ae8p3ve, Point of Sale (POS) | Same abbreviation/function, same vendor (Toast) |
| 86ae4mht1, HRIS | 86ae8p5db, HR Information System (HRIS) | Same acronym spelled out, same vendor (Rippling) |
| 86ae8p6az, Learning Management (LMS) | 86ae4mhz8, Learning Management System | Same acronym expanded, same vendor (Trainual) |
| 86ae4mhzb, S.O.P Creation | 86ae4mhyh, S.O.P Storage | Two halves of one SOP function, same vendor (Trainual) — audit's original near-dup pair |
| 86ae4mhyh, S.O.P Storage | 86ae4mwyb, Digital SOP's (Clips) | Third SOP-adjacent row; different vendor (ClickUp Clips vs. Trainual) but same "digital SOP" concept |
| 86aj16qp0, Vendor & Supplier Management | 86ae4mj6n, Vendor Management | Same function, same vendor (Restaurant 365) |
| 86aj16qkh, Sales Tax Filing | 86ae4mj23, Sales Tax Collection | Same function, same vendor (Davo) |
| 86aj16qrx, Allergen Management | 86ae4mhyx, Allergy Management | Likely typo variant of the same function, same vendor (Trainual) |
| 86ae8p4gt, Gift Card Program | 86ae4mhjh, Gift Cards | Same function, same vendor (Toast) |
| 86ae4mkn6, Customer Loyalty | 86ae8p2f3, Loyalty Program Management | Same function, same vendor (Hang) |
| 86ae4mkn6, Customer Loyalty | 86ae8qqx0, Loyalty Platform & CDP (Hang) | Third loyalty row forming a cluster with the pair above; same vendor (Hang) |
| 86ae8pj08, Onboarding Sequences | 86ae4mhwe, Onboarding | Overlapping onboarding function, different vendor (Trainual vs. Rippling) |
| 86ae4mhwe, Onboarding | 86ae8p5u3, Employee Onboarding | Same function, same vendor (Rippling) |
| 86ae8p6yw, Employee Scheduling | 86ae4mhxw, Scheduling | Same function, conflicting vendor assignment (Rippling vs. Deputy) |
| 86ae4mjak, Employee Recognition | 86ae8pee3, Peer Recognition | Overlapping recognition function, same vendor (Nectar) |
| 86ae4mj1p, CRM | 86ae8p1m9, Guest CRM | Same function, same vendor (SevenRooms) |
| 86ae8p3mf, Cross-Concept Guest Profiles | 86ae8qv6n, Cross-Concept Guest Recognition | Near-identical name, same vendor (SevenRooms), both tagged `architecture` |
| 86ae4muyv, Data Dashboards | 86ae4muy0, Data Analytics | Overlapping reporting function, same vendor (AirTable), both tagged `architecture` |
| 86ae4mkn1, Video Analytics | 86ae8qmz1, Vision AI Analytics (Footfall & Demographics) | Overlapping vision-analytics function, same vendor (EveryAngle) |
| 86ae4mj7g, Building Access | 86ae8p9yp, Access Control | Overlapping physical-access function, same vendor (Kisi) |
| 86aj3xb9m, Employee Feedback & Suggestions | 86ae8pexa, Pulse Surveys | Lower confidence — both staff-sentiment capture, same vendor (Canny) |
| 86ae4mj6x, Work Orders | 86ae8phqd, Equipment Repair Requests | Lower confidence — overlapping maintenance-request function, same vendor (ResQ) |

## (b) Vendor-name mismatches: Solution dropdown vs. SaaS Catalog

### Same vendor, different spelling (breaks cross-reference/filtering)

| Solution option | Catalog task | Issue |
|---|---|---|
| ElevenLabs | Eleven Labs (86aj11evh) | Dropdown has no space, catalog task name has a space |
| Restaurant 365 | Restaurant365 (86aj11bbp) | Dropdown has a space, catalog task name doesn't |
| APG Solutions - Smart Till (hyphen) | APG Solutions — Smart Till (86aj11d0h, em dash) | Different dash character |
| SuperHuman | Superhuman (86aj11eka) | Capitalization differs (mid-word capital H vs. none) |
| AirTable | Airtable (86aj11dmh) | Capitalization differs (mid-word capital T vs. none) |
| EveryAngle | Every Angle (86aj11e5y) | Dropdown has no space, catalog task name has a space |

### Catalog task with no matching Solution option at all

| Solution option | Catalog task | Issue |
|---|---|---|
| (none) | Google Business (86aj11erv) | No Solution dropdown option corresponds to this catalog vendor |
| (none) | Synthesia (86aj11dbb) | Missing from the Solution dropdown entirely |
| (none) | Claude (Anthropic) (86aj11d76) | Missing from the Solution dropdown entirely (not previously flagged in the audit) |

### Solution option actively used in the map with no Catalog task at all (reverse gap)

| Solution option | Catalog task | Issue |
|---|---|---|
| Deputy | (none) | Used as the confirmed Solution on 3 map tasks (e.g. Frontline Communication, Scheduling, Tip Management) but has no SaaS Catalog row |
| Okta | (none) | Used on 1 map task (Password Management) but has no SaaS Catalog row |
| Ramp | (none) | Used on 5 map tasks (Corporate Cards, Expense Management, Spend Controls, Spend Management, Price Intelligence) but has no SaaS Catalog row |
| Fireflies | (none) | Used on 2 map tasks (Meeting Analytics, Meeting Recording & Storage) but has no SaaS Catalog row |
| TipHaus | (none) | Used on 2 map tasks (Tip Pool Calculation & Distribution, Tip Management) but has no SaaS Catalog row |

### Note: unused dropdown options

8 additional Solution dropdown options are not referenced by any of the 241 map tasks and also have no Catalog entry: Dropbox, Fellow.AI, Gmail, Google Fiber, HubSpot, OLO, Shogo, Zoom. These aren't "mismatches" in the strict sense (nothing to cross-reference against), but they're dead weight in the dropdown worth a look during cleanup.
