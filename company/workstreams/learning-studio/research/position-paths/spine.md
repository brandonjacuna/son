# The spine of Sŏn's training program (working draft, 2026-10-01)

Status: content-first working draft for Brandon. Nothing here is decided until Brandon signs it. It builds every position path at once, so each one is defined partly by the others. Governs: D52 to D61, with D1, D5, D8, D10, D11, D13, D19 to D21, D25, D27, D39 to D41, D44, D46 to D48 and D50 carried. Sources: the six position and research drafts of 2026-10-01 (floor and door, beverage team, managers and systems, kitchen, everyone, and the four track and systems research passes), the discovery inventory (raw material, D59), and the Box canon as those drafts cite it (white paper `2466517057642`, Brand and Experiential Guidelines `2281626080747`). No ClickUp document was read. The Sŏn Operating System is out of scope.

How to read it:
- **R** = readiness: done before working solo, inside the window (D55). **O** = ongoing education. **R/O** = the module has a readiness part and an ongoing part.
- Hours are design estimates (40 paid hours a week, no overtime). Two weeks is 80 hours; three weeks is 120.
- A **supervised service** is counted at shift length (`workflow.shift_length.<position>`, about 6 hours as the design assumption), so pre-shift, opening, closing and side work sit inside it. At least one supervised service is a full night (`workflow.full_night`), and a person is released only for the dayparts they were supervised in (D10). Readiness includes trailing and paired services and the angel shift: Brandon's name for the gate shift where a trainer, the mentor, oversees the person the whole night (term pending his confirmation, `founder.term.angel_shift`). Unsupervised shifts after sign-off, where support is on hand but nobody is watching, come after release and sit outside the window.
- **Prove-first** (D56, stated once in ORI-015): every module that is not safety lets an experienced hire read the material and attempt the module's own proof cold. A pass banks the module; a failed cold attempt routes the person into the instruction with no interval and no recorded miss (D11). Safety elements are demonstrated on every attempt and never test out.
- **Retry room:** a not-yet extends the paid window (D11). Two-week routes are planned to about 72 hours and three-week routes to about 100 hours, leaving one supervised service and one recheck in reserve.
- **Ongoing education is paid and scheduled** at `policy.ongoing_education_hours.<position>` (ADM-104, SYS-134). Nothing is studied at home unpaid (D41).
- Revised 2026-10-01 after the specificity and time-fit red teams and the four module files' "Spine changes needed" lists. Each file's hours table is the detail behind the position windows here.
- Every tool name is a candidate and every tool step is a `tool.*` binding. Every figure is a `fact.*` binding.
- Positions: H host, LH lead host, FR food runner, BW back waiter, FS front server (front waiter is the same role), LFR lead food runner, LS lead server, BB barback, BA barista, BT bartender, LB lead bartender, HB head of beverage, MD Maître d', OM operations manager. Kitchen (draft for the executive chef): P porter, C commis or prep cook, CDP chef de partie or line cook, CT chef de tournant, KO the operations and production chef, KS the service and development chef, CDC chef de cuisine, EC executive chef. Kitchen titles are `people.*` bindings (naming conflict INT C17).
- Groups: **All** = every position. **CF** = customer-facing (H, LH, FR, BW, FS, LFR, LS, BB, BA, BT, LB, HB, MD, OM). **Floor** = H, LH, FR, BW, FS, LFR, LS, MD. **Bar** = BB, BA, BT, LB, HB. **K** = every kitchen position.

---

## 0. What this spine decides (the reconciliations)

1. **The shared core is 34.25 hours.** The drafts put the everyone layer at 33 to 38 hours before position work. Every hour there comes out of every position, so it was trimmed: ORI-001 to 2 h, ORI-003 to 2 h, ORI-015 to 1.5 h, ORI-016 taught inside the first drill (0.5 h), SAF-006 to the first-week walk-through (full event drills recur on the drill cadence), CMP-106 to 0.5 h, the day-one systems trimmed, and MNU-004 split into a 1-hour readiness part and an ongoing part. The red team then counted the watched service in ORI-021 at shift length (+2 h), cut SAF-011 to the house behaviors (0.5 h), reduced CMP-105 to the HR rules (0.5 h) and added CMP-113 (0.5 h), so the core is 34.25 h, not 32.5.
2. **One numbering.** The drafts collided (four different SYS-101s, three CMP-101s, three BEV-101 to BEV-110 runs, two MNU-101s). This spine assigns one ID to each module. Section 8 maps every discovery ID and every draft ID.
3. **Shared modules carry position parts, not copies.** MNU-001, BEV-102, SAF-001, SAF-009, SVC-002, SVC-008, SVC-071, BEV-002, KIT-002 and SYS-130 are each one module with a part per position. Nobody relearns a part they hold when they move.
4. **Wine is split in two.** What a position must pour and say on its first solo shift lives in BEV-102 (the current drink list at that position's depth, by-the-glass wines included). The wine track itself (BEV-110 to BEV-114) is ongoing education and carries the promotion gates (D54, D55).
5. **The certificate lever.** If the food handler certificate (CMP-101) and the alcohol seller-server certificate (CMP-102) must be held before solo (the proposed Sŏn rule), floor and bar entry windows run two to six hours over two weeks. If they are completed inside their legal windows (Texas: food handler within 60 days, TABC Safe Harbor within 30 days; verified-secondary), the entry windows fit two weeks. One decision for Brandon: `founder.compliance_timing`.
6. **Hiring routes the window rules out, or nearly.** A green external bartender does not fit (about 150 hours): bartenders come from barback or arrive experienced. A green external back waiter fits three weeks only; entering as a runner is recommended. An external front server fits three weeks only with technique test-outs and current certificates. A green barista does not fit two weeks by any route except from barback.
7. **Managers split readiness from pre-opening.** The MD and OM readiness windows (about 119 and 113 to 119 hours) hold only if configuration (SYS-119, SYS-120), assessor training (LEA-002, LEA-014, LEA-101, LEA-102) and recruiting sit outside them: configuration in a pre-opening window Brandon sets, assessor training before the first booked check slot. Even so, counted honestly (section 2.2) both windows run past three weeks, so whether D55 applies to the manager pair is Brandon's call.
8. **SevenRooms is one stacked track** (D60): basics for All (SYS-110 to SYS-112), host (SYS-113, SYS-114), lead host as master (SYS-115 to SYS-118), managers (SYS-119 to SYS-121), and the regulars and feedback module for every position that keeps customers (SYS-122). Its screens are named by function and customer is the only word used.
9. **Product feedback is one module** (MNU-101) used by every knowledge track, so D54's business advocacy has one method across food, wine, coffee, tea, spirits and beer.
10. **Compliance stays named** (D57). House safety (SAF-) is Sŏn's own content; compliance (CMP-) is provider content or HR-written rules, linked and tracked in Trainual with certificates uploaded (D17, D27). The red team applied this both ways: the illness exclusion list left SAF-011 for CMP-113, the chef's own food-safety controls left CMP-110 for KIT-013, the legal basis for paid learning left ORI-001 for CMP-105, and the supplier certification for cryogenic equipment became CMP-112 with the house procedure kept as its SAF-003 part.
11. **Mechanisms, policies and open questions are not modules.** CUL-023 (the recheck cadence), CUL-024 (the recommitment step), LIB-012 (the study-placement policy), BEV-034 (whether Sŏn runs two bars), MNU-007 (an interest, routed through ORI-015), SVC-080 and SVC-041 (folded into SVC-019 and SVC-018), BEV-031 (folded into BEV-030) and LEA-047 (merged into LEA-007) leave the module count. Section 5.10 lists them.
12. **Every window is counted the same way.** Supervised and observed services at shift length, with at least one full night; the supervisor version of CMP-103 and SYS-142 in every lead, manager, head of beverage and kitchen-leader window; retry room planned, not hoped for.

---

## 1. Positions and how they connect

**The ladders**
- Service: FR → BW → FS → LS (lead, designation). FR → LFR (lead, designation).
- Beverage: BB → BT → LB (lead, designation). BA and BT are one team; each cross-trains into the other through the specialist sets. HB is hired with expertise and holds a dotted line over the bar.
- Door: H → LH (lead, designation; holds the door by delegation from the MD, D20).
- Host moves into either team: into service at FR, into beverage at BB.
- Management: MD and OM are the parallel pair; usually external hires who prove floor or office fluency by test-out. A lead becoming MD is not a ladder rung.
- Kitchen (draft): P → C → CDP → CT; CDP → KO or KS; CDC and EC above. Production (prep) is also a full career a person can stay in (WP p.11, as the kitchen draft cites it). P can also move to the floor (FR) or C.

**What each step adds, and what the mover already holds**

| Move | Already proven | What the step adds | Window |
|---|---|---|---|
| H → FR | Core, CF, floor block (KIT-003 excluded for the host), the walk, scanning, the book, MNU-001 and BEV-102 at host depth | KIT-003 (1.5), carry, glass, seats, modified-plate delivery, the pass, set-down line, runner menu and drink depth, runner POS, two supervised services at shift length | about 30 h; plus 4.5 if CMP-101 and CMP-102 were not completed in the host's first month |
| P → FR | Core, kitchen block (porter version), ORI-021, the kitchen's calls | Blocks B and C, the runner set, three supervised services | about 50 h |
| FR → BB | Core, CF, SVC-071 handling | Block D less what is held, the barback set, two supervised services | about 40 h |
| FR → BW | Everything a runner holds; BEV-110 (wine level 1) as the gate | Pitcher and bottle pour, clear and reset, body at the table, reading table state, the pair, setting a place, service bar, menu and by-the-glass at BW depth | about 39 h |
| BW → FS | Everything through BW; BEV-111, BEV-015, BEV-112, BEV-113 held as the gate | Opening the table, the order, helping a customer choose, pairing presentation, pacing and firing, holding a section, full recovery range, saying no, the check and departure, the end-to-end sequence, full menu depth, full POS | about 58 h |
| BW covering FR shifts | Everything | Menu re-proof if changed (MNU-002), station card (CUL-011), one supervised pass run | about 5 h |
| FS → LS | Everything through FS | Reading the whole room and the team's load, stepping in without taking over, teaching, the lead's admin, the supervisor version of CMP-103, SYS-142 | about 33 h (37 if a closing lead) |
| FR → LFR | Everything through FR | Directing runs, coaching a drill, teaching, the lead's admin, the supervisor version of CMP-103, SYS-142 | about 35 h |
| H → LH | Host release; SYS-115 to SYS-117 held as the gate | Holding the door by delegation, off-plan pacing calls, teaching, pre-shift updates, the lead's admin, the supervisor version of CMP-103, SYS-142 | about 32 h (34 if `people.close_roles` includes the lead host) |
| H or BW → BB | Core, CF, floor block | Bar team core, barback drink depth, reading the bar ahead, bar logging | about 41 h |
| BB → BT | Bar team core; BEV-105, BEV-012, BEV-005, BEV-008, BEV-001, FLV-002 held as the gate | Barista-shared set, full drink list, wine and sparkling at the bar, beer and Korean drinks if listed, counter hosting, two queues, the full alcohol-service part, bar POS | about 66 h (60 if neither beer nor Korean drinks is listed) |
| BB → BA | Bar team core | Barista set (milk, coffee program, tea and matcha, morning window, counter POS); BEV-120 if the barista pulls the batch espresso | about 48 h |
| BA ↔ BT | Bar team core and the shared set | The other specialist set | BA → BT about 35 h (gate items done as ongoing); BT → BA about 10 h |
| BT → LB | Everything through BT; BEV-035 part one and BEV-111 full (proposed gate) | Coaching drills, team palate calibration, the lead's admin, bar ordering and counts, the supervisor version of CMP-103, SYS-142 | about 39 h |
| P → C | Core, kitchen block (porter version), receiving | Knife drills, the cook's food safety and allergen chain, recipes, paired prep | about 40 to 60 h |
| C → CDP | Prep set | A first station, the pass, cooking to the call; released solo on a named non-peak service, peak nights under KIT-030 after | about 55 h per first station (chef to reset) |
| CDP → CT | One station | Entering a running station, briefing and coaching at the station (LEA-105), each further station | about 41 h on the first move, then about 38 h per added station |

**Internal moves never repeat a signed-off module.** They re-prove only currency: the current menu or list (MNU-002, BEV-102 recheck) and the station card (CUL-011).

---

## 2. Readiness by position

### 2.1 The shared blocks (taken once, counted in every position below)

**Block A: everyone, kitchen included. 34.25 h (17 remote, 17.25 on site).**
- The house (16.5 h): ORI-001 (2), ORI-015 (1.5), ORI-008 (1), ORI-003 (2), CUL-002 (2), ORI-021 (7, on site, one full service watched at shift length, after SAF-007 and the SAF-006 walk that same day), CUL-001 (0.5), ORI-016 (0.5).
- House safety (4.5 h): SAF-001 part 1 (1.5), SAF-006 (1.5), SAF-007 (1), SAF-011 (0.5, then observed on the first supervised services).
- Compliance (6.25 h): CMP-101 (2), CMP-103 (1), CMP-104 (1.25), CMP-105 (0.5), CMP-106 (0.5), CMP-113 (0.5).
- Systems (6.5 h): SYS-002 (1), SYS-101 (0.5), SYS-103 (0.75), SYS-104 (0.75), SYS-105 (0.5), SYS-110 (2), SYS-111 base (1).
- Food and menu (1 h): MNU-004 readiness part.

**Block B: customer-facing add. 9.75 h (4.25 remote, 5.5 on site).** ORI-006 (1.5), ORI-009 (1), ORI-020 first daypart (1), SAF-001 part 2 (1.5), SAF-009 part 1 (1), SVC-009 (0.75), CMP-102 (2.5), SYS-111 customer-facing add (0.5).

**Block C: floor add. 3.5 h (1 remote, 2.5 on site); 2 h for the host.** SVC-013 (1), SVC-015 (0.5), SVC-079 (0.5), KIT-003 (1.5; not the host, whose slice of it sits inside SVC-011). SVC-013 carries a 0.5 h service-well part for food runners only if runners carry drinks (`workflow.runners_carry_drinks`).

**Block D: bar team core (BB, BA, BT). 22.5 h for BB; 24 h for a green external BA; 22 h for BT (2.5 remote).** BEV-017 (2), BEV-002 (4), BEV-003 (2.5), BEV-016 (2), SVC-071 bar part (2), BEV-014 (1), BEV-024 (1), BEV-033 (6 for BB; 3 for BA and BT, the house portion), BEV-105 recognition part (2, BB and BA). BEV-001 (2.5) and FLV-002 (2) are barback ongoing education and part of the gate to bartender; a green external barista takes them prove-first (4.5). BEV-101 (opening, closing, side work) runs inside supervised services, which are counted at shift length.

**Block K: kitchen add.** Cooks 17 h: KIT-102 (2), KIT-101 (2), CMP-110 (3, the code items only; its hours are rechecked once the chef's own controls sit in KIT-013), CMP-111 (2), SAF-013 (3), KIT-016 (2), SYS-139 (2), SYS-140 (1). Porter version 11.5 h (KIT-101 1, CMP-110 1.5, SAF-013 1, SYS-139 1).

**Remote time.** Block A alone carries about 17 remote hours; customer-facing positions carry 22 to 31. Brandon floated about 8 remote hours at intake (`workflow.remote_onboarding_hours`). Either the larger remote share is accepted (it is paid, and it is screen knowledge), or modules move on site, which costs the same hours. Remote work is capped at about 3 h a day and drills start on day two (section 2.6), so a green or second-language hire is never left alone with a screen for a week.

**Before the first supervised service** only the safety items and the calls are required: SAF-001 both parts, SAF-006 walk, SAF-007, SAF-011's demonstration, CMP-113, SVC-013, SVC-079, and SVC-009 (a new person can meet a customer crossing a line on the first night). ORI-003, ORI-009, ORI-006, SVC-015 and the CUL-002 role-play follow it, inside the first week and before the angel shift.

### 2.2 Front of house

**Food runner (green).** A 34.25 + B 9.75 + C 3.5 + position 22.5 + supervised services 18 (three at shift length, one a full night) + checks 2.5 = **about 90.5 h (26 remote, 64.5 on site); 91 if runners carry drinks.** About 2.3 weeks. **About 86 h with the certificate lever (2.15 weeks).** It no longer fits two weeks on paper; the honest options are to report 2.2 weeks, or to cut about 9 h from readiness. Brandon's call (section 7, item 1).
- Position set: SVC-003 (4), SVC-071 floor part (1.5), SVC-004 runner part (1.5), SVC-019 (1), SAF-004 (1.5), KIT-002 floor side (2), SVC-008 set-down part (0.5), SVC-018 (1), SVC-006 runner part (0.5), SVC-002 runner part (0.5), MNU-001 runner depth (5), BEV-102 runner depth (1.5), SYS-130 runner part (1.5), SYS-112 passing half (0.5).
- Experienced hire: prove-first on every non-safety module; banked run-throughs on SVC-003, SVC-071, SVC-004, SVC-018, and SYS-130 if the same POS; ORI-033 runner part added. About 84 h; about 80 with current certificates uploaded. Always proven on every attempt: SAF-001, SAF-004, SAF-006, SAF-007, hot-plate handling in SVC-003, MNU-001's spoken check (instruction skipped only if passed cold).
- Internal mover: from host, about 30 h (section 1). From porter, about 50 h. A back waiter covering runner shifts, about 5 h.

**Back waiter.**
- From food runner (main route): **about 39 h (3 remote, 36 on site), one week.** Adds BEV-002 floor part (2), SVC-025 (2), SVC-028 (1), SVC-006 back-waiter part (2), SVC-027 (2), SVC-072 (1.5), SVC-013 service-bar part with the BEV-016 service-well part (1), MNU-001 to back-waiter depth (+3), BEV-102 to back-waiter depth including the by-the-glass list at depth (+3), SVC-008 second-question part (0.5), SYS-130 add (0.5), SVC-002 part (0.5), plus supervised services 18 and checks 2.
- Green external: **route proposed closed.** It would skip the BEV-110 gate an internal runner must hold, which is unfair to internal people, and at about 110 h it fits three weeks only. Everyone enters service as a runner. Brandon's call.
- Experienced external: prove-first on the FR and BW sets; banked technique on SVC-003, SVC-071, SVC-004, BEV-002, SVC-025, SVC-028, SVC-072; a cold BEV-110 check (about 2 h) so the outside hire holds the gate an internal runner holds; about 96 h (92 with current certificates). Always proven: SAF-001, SAF-004, the BEV-110 check.

**Front server.** The wine gate (BEV-111, BEV-015, BEV-112, BEV-113) is held before the window opens, never taught inside it (D55).
- From back waiter (main route): **about 58 h (5.5 remote, 52.5 on site), a week and a half.** Adds SVC-029 (1), SVC-032 (2), SVC-033 table part (3), SVC-008 full part (1), BEV-042 current pairings (2), SVC-035 (3), SVC-036 with the section handover (2), SVC-002 full range (2), SVC-037 (1), SVC-038 (1), SVC-078 end-to-end practical (4, its own staged block), SAF-009 part 2 (2), MNU-001 full depth (+4), BEV-102 front-server depth (+2), BEV-025 floor part (1), SYS-130 front-server part (+4), SYS-112 full writer (1), plus supervised services 18 and checks 4 (the full-menu spoken check, D40). SVC-101 (follow-up emails, D61, about 2 h) follows in the first month after release.
- External, arriving with wine at Sommelier 1 level or above: FR, BW and FS sets together, about 150 h untested. With prove-first across the three sets (the FS set components proven cold in one mock service of about 4 h and banked per component; technique banked on SVC-003, SVC-071, SVC-004, BEV-002, SVC-025, SVC-028, SVC-072, SYS-130 on the same POS), current certificates uploaded, ORI-033, the wine gate proven by credential plus Sŏn's own proofs (BEV-111 proof about 4 h, BEV-112 integrated spoken check and tasting about 6 h, BEV-113 role-play about 2 h, BEV-015 live demonstration about 1 h), **about 120 h, three weeks, with no retry room; about 130 h if the FS set does not bank.** SVC-078 stays its own staged block, never on the angel shift and never banked. The technique proofs may run at the paid practical interview (LEA-033) before day one. A candidate who fails two or more technique proofs enters as back waiter. Always proven: SAF-001, SAF-004, SAF-009, MNU-001, BEV-042, the translation and Sŏn-list elements of BEV-112, BEV-113's role-play. This is the tightest route in the program; D55 already accepts that front servers are likely not hired externally.

**Host (green).** A 34.25 + B 9.75 + C 2 + position 25.5 + supervised services 18 + checks 2.5 = **about 92 h (29 remote, 63 on site).** **About 86.5 h (2.2 weeks) by taking CMP-101 and CMP-102 in the first month (a host neither handles food nor serves alcohol, so both are recommended, not required) and moving the MNU-004 readiness part to the first month.**
- Position set: SVC-010 (1.5), SVC-004 host part (1), SVC-018 host part (0.5), SVC-011 (1.5, carrying the host's slice of KIT-003), SVC-059 (1), SVC-062 (1.5), SVC-037 door part (0.5), SVC-017 door part (0.5), SVC-012 (1), SVC-072 walk before doors (0.5), SVC-038 departure part (0.5), MNU-001 host depth (3), BEV-102 host depth (1), SYS-112 (1.5), SYS-113 (6), SYS-114 (3), SYS-130 host part (1). SVC-103 (opening and closing the door) is learned inside the supervised shifts.
- Gating policy: no host is released before `founder.mistreatment_policy` exists (SVC-009), and nothing about reading the door's demographics is taught before `founder.door_data_policy`.
- Experienced hire: prove-first on every non-safety module; SVC-062 by role-play, SVC-004 by run-through, SYS-113 and SYS-114 for a SevenRooms-experienced host; about 85 h. Always proven: SAF-001, SAF-006, SVC-010 and SVC-011 (the arrival canon is house-specific, so the spoken check runs even when the instruction is skipped), the honest-quote standard in SYS-113, the card-number item in SYS-114 (if Brandon confirms).
- Internal mover: a back waiter moving to host holds A, B, C and the menu; about 34 h.

**Lead host.** Host release plus designation (D5). Gate held before: SYS-115, SYS-116, SYS-117 (ongoing for a host, about 20 h). SYS-118 (signing off a new hire's basics with ratings that match a second rater's) is the lead host's mastery proof for the SevenRooms track.
- Window: **about 32 h, on site (34 if `people.close_roles` includes the lead host, with ADM-113's lead version).** SVC-068 (3), SVC-057 (2), LEA-001 (3), LEA-018 (1.5), LEA-005 host-updates part (1), ADM-117 (2.5), ADM-109 (3), CMP-103 supervisor version (+1), SYS-142 (1), a shift as lead under the MD's observation (12, at shift length), checks (2). SYS-118 is completed before signing off basics alone.
- External lead host: host set with prove-first, the SevenRooms master modules (test-out on building the book only), and the window: about 126 h, over three weeks with no retry room. Recommended: lead host is reached from host. No test-out on the delegation layer or flags.

**Lead food runner.** **About 35 h, on site.** SVC-066 (3), SVC-067 (2), LEA-011 (3), LEA-001 (3), LEA-018 (1.5), KIT-002 expo part (1), ADM-117 (2.5), ADM-109 (3), CMP-103 supervisor version (+1), SYS-142 (1), observed peak shifts (12), checks (2). Prove-first on the teaching modules for a lead who has led elsewhere; the observed shifts always run.

**Lead server.** **About 33 h (37 if a closing lead), on site.** SVC-063 (2), LEA-024 (2), SVC-067 (2), LEA-001 (3), LEA-018 (1.5), SVC-002 lead part (1), ADM-117 (2.5), ADM-109 (3), CMP-103 supervisor version (+1), SYS-142 (1), ADM-113 lead version (2) and SYS-131 (2) only if `people.close_roles` includes the lead server (cash and the deposit stay with managers), an observed full shift (12), checks (2).

**Maître d'.** Usually an external management hire (ORI-033 management part). Brandon owns people and training (D1); the MD teaches and runs the floor but does not own the program.
- Window, counted honestly: **about 139 h with current certificates uploaded; about 120 h if MNU-001 and BEV-102 pass prove-first.** A, B, C (47.5); ORI-033 (2); floor and door fluency by banked run-through on SVC-010, SVC-011, SVC-057, SVC-015, SVC-004, SVC-078, with SVC-063, SVC-067, SVC-012 and SVC-072's MD part proven inside it (10); MNU-001 front-server depth (12, prove-first); BEV-102 front-server depth (6.5, prove-first); BEV-042 (2); LEA-028 (2), LEA-029 (3), LEA-005 (2), LEA-027 (1.5), LEA-010 (1), LEA-024 (2; the MD reads who is going under from the first solo night), LEA-016 (1.5), LEA-103 (2); SVC-069 (1.5); SVC-002 widest range (1.5); SAF-009 part 2 (2); SVC-009 manager part (1); ADM-101 (12, one shadowed and one led office day); ADM-109 (3); ADM-110 (4); ADM-113 (3); SYS-112 (1.5); SYS-113 by test-out run (2); SYS-130 by test-out run (1); SYS-131 (2); CMP-103 supervisor version (+1); SYS-142 (1); observed full services in the role with Brandon (12, two at shift length), under a management gate spec Brandon sets.
- First month, outside the window (about 17.5 h, before the first booked check slot): LEA-101, LEA-002, LEA-014, LEA-102, LEA-001. D19 has managers assessing the first cohorts.
- Hiring requirements, not training (Brandon to confirm): wine level 3 (BEV-112) proven at the paid practical interview or in the first week; CMP-108 held at hire, or a dated post-hire deadline with `workflow.cfpm_coverage`.
- Pre-opening only (the opening MD), or first quarter (a later MD): SYS-115, SYS-116, SYS-119, SYS-120, SYS-121.
- Always proven: SAF-001, SAF-009, the house management layer.
- **Either way the MD runs past three weeks with retry room.** Brandon decides whether D55 applies to the manager pair, or sets a four-week manager onboarding standard (section 7, item 4).

**Operations manager.**
- Window, counted honestly: **about 124 h (about 119.5 with current certificates); about 127 if the OM owns the schedule (ADM-104 6 plus SYS-134 1, one shared practical owned by ADM-104).** A and B (44); ORI-033 (2); LEA-028 (2), LEA-010 (1), LEA-027 (1.5); ADM-101 (12), ADM-102 (4), ADM-103 (5), ADM-105 (6), ADM-106 (4), ADM-108 (3), ADM-109 (3), ADM-110 (4), ADM-112 (2), ADM-113 (3), ADM-115 (3); CMP-109 (2.5); SYS-131 (2), SYS-133 (3), SYS-136 (3), SYS-139 alarm part (1); SAF-009 part 2 (2); SVC-009 manager part (1); CMP-103 supervisor version (+1); SYS-142 (1); observed office days with Brandon (8).
- First month, outside the window (about 20 h): LEA-101, LEA-002, LEA-014, LEA-102, LEA-005, LEA-016, LEA-103.
- CMP-108 (certified food protection manager) is provider-set hours (`fact.cert_hours`): a hiring requirement, or a dated post-hire deadline (`policy.cfpm_deadline`) with `workflow.cfpm_coverage` keeping a certified person present during all hours of operation (25 TAC 228.31, verified-secondary), which is also a scheduling input.
- Prove-first for experienced managers: ADM-102, ADM-103, ADM-105, ADM-113 practicals (saves about 8 h). Always proven: ADM-106's never-do list, ADM-108's legal steps, ADM-110, the house split.
- Same decision as the MD: D55 for the pair, or a four-week standard.

### 2.3 Beverage

**Barback (green).** A 34.25 + B 9.75 + D 22.5 + position 6 + supervised services 18 + checks 2 = **about 92.5 h (24.5 remote, 68 on site).** **About 87 h (2.2 weeks) with the certificate lever and the MNU-004 readiness part moved; about 84 h if SYS-110 and SYS-111 also move to the first month for barbacks (Brandon's call, D60 names every position but not before solo).** BEV-027 (reading the bar ahead) stays in readiness: it is the barback's job, and it is what breaks first on a busy night.
- Position set: BEV-102 barback depth (2), BEV-027 (2), SYS-130 bar read-only part (1), SYS-139 bar refrigeration part (1).
- Experienced: prove-first on every non-safety module; banked technique on BEV-002, BEV-003, SVC-071 bar part, BEV-033 technique; ORI-033 bar part added; about 85 h, about 80 with current certificates. Always proven: BEV-014, the knife-safety element of BEV-033, CMP-112 (if the barback preps with the equipment), safety, compliance.
- Internal mover (a host or back waiter picking up barback shifts): Block D plus position set plus two supervised services at shift length; **about 40 h.**

**Barista.**
- Green external: A 34.25 + B 9.75 + D 24 + barista set 33 + supervised services 18 + checks 3 = **about 122 h (30.5 remote, 91.5 on site); about 117.5 with the lever; plus 2.5 if the barista pulls the batch espresso (BEV-120).** Over three weeks with no retry room. **Barback-first is the default route; a green external barista is accepted only with prove-first on BEV-001 and FLV-002.**
- Barista set: BEV-004 (3.5, conditional on milk-texturing equipment on the bar, `tool.bar.equipment`), BEV-103 full (3), BEV-104 (3.5), BEV-006 (2), BEV-025 (2), FLV-005 (1), BEV-102 barista depth (2), BEV-026 (3), BEV-020 (1.5), SVC-033 drink part (1.5), SVC-008 bar part (1), MNU-001 counter depth (3, only if the window sells food: `workflow.bar.counter_food`), SYS-130 counter part (4), SYS-112 (1), SYS-139 (1).
- Experienced: prove-first; banked technique on BEV-002, BEV-003, BEV-004, SVC-071, FLV-002, BEV-001, BEV-104 brewing technique, BEV-033 technique; about 109 h, about 104 with current certificates. Fits three weeks.
- **From barback: about 48 h (50.5 with BEV-120). This is the only route that fits two weeks.** From bartender: about 10 h.
- Always proven: BEV-006, BEV-014, BEV-026, the matcha method, the steam-wand safety element of BEV-004, allergens.
- Open: is the barista a separate hire or the bartender on the morning register? Do baristas serve alcohol (then SAF-009 part 2 applies, `workflow.bar.morning_alcohol`)? Who pulls the batch espresso (`people.espresso_puller`)?

**Bartender.** Gate items are held before the move as barback ongoing education: BEV-105 full, BEV-012, BEV-005, BEV-008, BEV-001, FLV-002 (about 26.5 h; about 7 weeks at 4 paid hours a week).
- From barback (main route): **about 66 h (65 until late night runs; 60 if neither beer nor Korean drinks is listed), a week and a half.** Barista-shared set (BEV-004 3.5, BEV-103 short 1.5, BEV-104 3.5, BEV-006 2, BEV-025 2, FLV-005 1, BEV-020 1.5, SVC-033 drink part 1.5, SVC-008 bar part 1); bartender set (BEV-102 bartender depth +4 over the barback's 2, BEV-015 bar part 2, BEV-116 serving part 3 if beer is listed, BEV-028 short part 2 if listed, BEV-023 2.5, BEV-021 2, SAF-009 part 2 2, SYS-130 bar part +5, SYS-112 1, MNU-001 counter depth 3, ORI-020 late-night part 1 only once late night runs, D24); supervised services 18; checks 3.
- Experienced external: about 158 h untested. With prove-first across the bar core, the shared set and the bartender set (BEV-016, BEV-020, BEV-021, BEV-023, BEV-024 included, about 9 h back), banked technique on BEV-002, BEV-003, SVC-071, FLV-002, BEV-001, BEV-012, BEV-005, BEV-105 category knowledge, BEV-008, BEV-004, BEV-104 technique, BEV-033 technique and SYS-130 on the same POS, plus current certificates, **about 110 h, three weeks with no retry room.** BEV-105's full part is readiness only on this route.
- **Green external: about 158 h. Does not fit.** Enters as barback. Brandon to confirm.
- From barista: about 35 h once BEV-105, BEV-012 and BEV-005 are done as barista ongoing education (section 3).
- Always proven: BEV-102's Sŏn list (prove-first allowed), SAF-009, BEV-014, the ice-well burn, allergens.
- Food at the bar: if counter customers order food, the bartender adds SVC-032 counter part and MNU-001 counter depth (already counted), and the workflow decision `workflow.bar.counter_food` is needed.

**Lead bartender.** Designation on a signed-off bartender (D5). **About 39 h, on site, spread across weeks.** LEA-011 (3), LEA-001 (3), LEA-018 (1.5), BEV-019 running a session (3), ADM-117 (2.5), ADM-109 (3), ADM-105 bar part (4), SYS-136 (2), LEA-005 bar-update part (1), CMP-103 supervisor version (+1), SYS-142 (1), an observed shift as lead (12), checks (2). Before signing practicals alone: LEA-002, LEA-014, LEA-003, LEA-016 after calibration and audit (D5; HR's ruling on hourly leads rating is open). CMP-108 manager alcohol credential if delegated. BEV-119 (cellar and stock condition) follows as ongoing education.

**Head of beverage.** House onboarding, not a craft window. **About 94 h, plus `fact.cert_hours.saf003`; under three weeks.** A, B (44); ORI-033 (2); BEV-017 (2); a bar familiarity walk on BEV-016, BEV-014, BEV-024 (4); BEV-102 at bartender depth (6, normally proven first); CMP-112 (supplier hours, `fact.cert_hours.saf003`, plus the SAF-003 house part 0.5); SAF-009 part 2 (2); SYS-112 (1.5); LEA-002 (6) and LEA-014 (2.5), kept in the window and not the first month because at opening the HB signs every bar practical and spoken check, so calibration cannot wait; ADM-105 (6); SYS-136 (3); ADM-115 (2); CMP-103 supervisor version (+1); SYS-142 (1); observed shifts (12). **Hiring requirements, not training (Brandon to confirm): wine knowledge above Sommelier 1 level at hire,** because the HB teaches front servers to that level (D47); CMP-108 held at hire.

### 2.4 Kitchen (draft for the executive chef; every hour is the chef's to reset)

- **Cook release is defined** as solo on the station on a named non-peak service (`workflow.kitchen.nonpeak_service`); peak nights are signed off after the window under KIT-030 over a window of shifts (D10). The 16 h per station and the paired-service unit (4 h in the earlier draft; about 6 h at shift length) look optimistic for a kitchen held to this standard; the chef resets both.
- **Porter:** A 34.25 + K porter 11.5 + KIT-010 (6) + KIT-015 (3) + SYS-136 receiving entries (1) + paired shifts including one full night (22) + practicals (4) = **about 82 h, two weeks (about 79 if SYS-110 and SYS-111 move to the first month).**
- **Commis or prep cook:** A 34.25 + K 17 + KIT-012 (10) + KIT-013 (4.5, now carrying the chef's own food-safety controls from CMP-110) + KIT-015 (2) + KIT-020 (3) + KIT-021 (3) + KIT-022 (2) + SYS-141 (2) + SYS-136 count part (1) + paired prep (20) + practicals (4) = **about 103 h green (2.6 weeks); about 88 h experienced** (prove-first: knife by a practical with cuts chosen on the day, with the knife-safety element demonstrated every attempt; recipes by spoken check; mise observed on the first paired shift). With the lever (food handler inside 60 days), 2 h less.
- **Chef de partie or line cook:** experienced external **about 122 h, three weeks** (A, K, commis set by prove-first, ORI-033 kitchen part, KIT-002, KIT-023.x first station 16, KIT-024, SYS-132, paired service 28, practicals 6; KIT-103 parked until two dayparts run). Internal from commis **about 55 h.** A green line cook enters as commis.
- **Chef de tournant:** usually experienced or an internal CDP. About 125 h for an experienced hire (adds LEA-105 3 and CMP-103 supervisor version +1), second-station practicals at the edge; internal about 41 h on the first move (KIT-031 2, LEA-105 3, a station 16, paired service, practicals), then about 38 h per added station.
- **KO, KS, CDC:** onboarding **about 102 h (two and a half weeks)**: A, K, ORI-033, every station walked and cooked under the EC (16), LEA-027, LEA-104, LEA-105 (3), LEA-103 (2, before the first cook's start date), CMP-103 supervisor version (+1), SYS-142 (1), SYS-133 (KO in full, 3; KS and CDC the 1 h timecard-approval part only if named in `people.timecard_approvers`), SYS-134, SYS-136, SYS-141 maintain part, observed services (12). KO adds KIT-041; KS adds KIT-040 and KIT-042 as ongoing (identified, chef to define). CMP-108 at provider hours: hire holding it.
- **Executive chef:** onboarding about 66 h, not a readiness window: LEA-106 (the people and training system, D1, about 6 h with Brandon), the non-negotiables, the brand frameworks and the BG 17 held sessions, the floor's service model, person-in-charge compliance, systems at owner level, LEA-002 kitchen part as an assessor.
- Always proven in the kitchen: CMP-110 behavior, SAF-013, CMP-111, emergencies, the knife-safety element of KIT-012. A valid certificate counts only as the certificate.

### 2.5 Summary

Hours are counted with supervised and observed services at shift length, the supervisor version of CMP-103 and SYS-142 in every lead and manager window, and every listed module counted. "Retry room" is the gap to 72 h (two-week routes) or 100 h (three-week routes), the planning targets that leave one supervised service and one recheck in reserve.

| Position and route | Hours | Remote / on site | Weeks | Retry room | Fit |
|---|---|---|---|---|---|
| FR green | 90.5 (86 with lever) | 26 / 64.5 | 2.3 (2.15) | none to 72 | Just over two weeks; Brandon reports 2.2 weeks or cuts about 9 h |
| FR experienced | 80 to 84 | | 2 to 2.1 | none to 72 | At the edge |
| BW from FR | 39 | 3 / 36 | 1 | yes | Fits |
| BW green external | about 110 | | 2.75 | none | Route proposed closed; runner entry |
| BW experienced external | 92 to 96 | | 2.4 | 4 to 8 h to 100 | Three weeks |
| FS from BW | 58 | 5.5 / 52.5 | 1.5 | yes | Fits |
| FS external | 120 (130 if the FS set does not bank) | | 3 | none | Tightest route; likely not hired externally (D55) |
| H green | 92 (86.5 with moves) | 29 / 63 | 2.3 (2.2) | none to 72 | Just over two weeks with moves |
| LH from H | 32 (34 closing) | on site | under 1 | yes | Fits |
| LFR, LS | 35, 33 (37 closing) | on site | under 1 | yes | Fits |
| BB green | 92.5 (87 with moves; 84 with SYS-110 and SYS-111 moved) | 24.5 / 68 | 2.3 (2.2) | none to 72 | Just over two weeks |
| BA green external | 117.5 to 122 | 30.5 / 91.5 | 3 | none | Barback-first is the default |
| BA from BB | 48 (50.5 with BEV-120) | | 1.2 | yes | Fits; the only two-week barista route |
| BT from BB | 66 (60 to 65 by what is listed) | | 1.7 | 6 h to 72 | Fits |
| BT experienced external | 110 | | 2.75 | none | Three weeks with prove-first |
| BT green external | 158 | | 4 | | Does not fit |
| LB | 39 | on site | spread | yes | Fits |
| HB | 94 plus supplier hours | | 2.4 | 6 h to 100 | Fits three weeks |
| MD | 139 (120 with prove-first on MNU-001 and BEV-102) | | 3 to 3.5 | none | Over three weeks; D55 for managers is Brandon's call |
| OM | 119.5 to 127 | | 3 to 3.2 | none | Over three weeks; same call |
| P, C, CDP, CT, pair | 82, 88 to 103, 122, 125, 102 | | 2 to 3 | P yes; others thin | Chef to reset |

### 2.6 The reference sequence for each entry route

The order below is the design reference; the day-by-day plan for a person is built by LEA-103. Rules: remote work is capped at about 3 h a day; drills start on day two; the safety items and the calls come before the first supervised service; ORI-003, ORI-009, ORI-006, SVC-015 and the CUL-002 role-play follow the first supervised service and precede the angel shift; at least one supervised service is a full night; the angel shift is the last supervised service, and the gate record is written at its close (D8); a not-yet extends the window by the interval the practice plan sets.

- **Green food runner, back waiter from runner, green host (two weeks, 10 working days).** Days 1 to 2: ORI-001, ORI-015, ORI-008, SYS-002, SYS-101, SYS-103, SYS-104, SYS-105 (remote, paid, capped); on site, SAF-007, the SAF-006 walk, ORI-021 (the watched full service), the first drill (ORI-016 inside SVC-003 or SVC-004). Days 3 to 4: SAF-001 both parts, SAF-011, CMP-113, SVC-013, SVC-079, SVC-009, the position's drills (SVC-003, SVC-071, SVC-004, SVC-018), SYS-110, SYS-111, SVC-103 walked; the first supervised service on day 4. Days 5 to 7: ORI-003, CUL-002, ORI-009, ORI-006, SVC-015, CUL-001, KIT-002 floor side, KIT-003, SAF-004, MNU-001 and BEV-102 at depth (remote study inside the cap, tastings on site), SYS-130, SYS-112; the second supervised service (a full night). Days 8 to 9: the spoken checks (MNU-001, BEV-102), the remaining practicals, the compliance courses (CMP-101, CMP-102, CMP-103, CMP-104, CMP-105, CMP-106) where `founder.compliance_timing` places them, the third supervised service. Day 10: the angel shift and the gate record, with retry room held in reserve.
- **Green barback.** As above, with Block D's drills from day 2 (BEV-002, BEV-003, BEV-033, SVC-071 bar part), BEV-014 and BEV-016 before the first supervised service, BEV-017 and BEV-102 in the study hours, BEV-027 before the angel shift.
- **Bartender from barback, barista from barback, front server from back waiter (one to two weeks).** No shared blocks. Days 1 to 2: the new set's study (BEV-102 or MNU-001 at the new depth) and drills; the gate items are already held. The first supervised service in the new position on day 2 or 3; the capstone (SVC-078, or the bar's full-shift practical) as its own staged block before the angel shift, never on it.
- **Experienced hire (any position).** Day 1: ORI-001, ORI-015, ORI-033, the safety items; the technique proofs and the mock service booked as check slots on days 2 and 3 (or at the paid practical interview, LEA-033); the prove-first attempts for the knowledge modules in the study hours; then the same supervised-service sequence as the green route, with the instruction only for what did not bank.
- **Internal mover.** CUL-011 (the station card) and the currency re-proof (MNU-002, BEV-102 recheck) on day 1; the new set's drills and study; two supervised services in the new position; no signed-off module repeated.
- **Managers and the head of beverage.** Configuration (SYS-119, SYS-120) and recruiting sit in the pre-opening window; assessor training (LEA-002, LEA-014, LEA-101, LEA-102) is first-month for the MD and OM and in-window for the HB. The pre-opening calendar (`workflow.preopening_calendar`) starts managers at least four weeks before line staff and the HB at least two weeks before bar staff, because every opening front server is external and runs the tightest route at once. Assessor hours per cohort are counted against `workflow.live_gate_limit` (LEA-101).
- **Kitchen.** The chef sets the sequence; the reference is Block A and Block K in the first three days, knife and mise drills from day 2, paired prep or paired service from day 3, release on a named non-peak service.

---

## 3. Ongoing education and promotion gates, by position

Gate types: **hard** (must be held before the next window opens), **soft** (listed for promotion; a lead may promote with a dated plan to finish inside `policy.soft_gate_window`, unblocked in the standing conversation, D13). Promotion also requires the designation or opening (`people.*`).

**Paid hours for ongoing education.** Each position has a weekly allowance (`policy.ongoing_education_hours.<position>`), placed in the schedule by ADM-104 and SYS-134 and tracked by LEA-102. No overtime means these hours displace shift hours, so the allowance decides how long a promotion takes. At an assumed 4 paid hours a week: food runner to back waiter about 3 weeks (BEV-110, 10 h); barback to bartender about 7 weeks (26.5 h of gate items); back waiter to front server about 27 weeks for the hard gates (106 h) and about 33 with the soft gates. At 2 hours a week the wine gates alone take about a year. Without the allowance, wine study drifts home and unpaid, which breaks D6, D41 and 29 CFR 785.27 to 785.29 (verified-primary).

**Everyone after release:** the standing recheck (`workflow.recheck_cadence`, run through LEA-101 and LEA-102; what a recheck is sits in ORI-015), MNU-002 on every menu change, BEV-102 recheck on every list change, MNU-004 ongoing part, MNU-101 product feedback, CUL-003, CUL-004, CUL-010, the annual recommitment (`workflow.recommitment`, a people step under LEA-006), ORI-023 (once the open-books scope exists), SVC-044 (once `founder.staff_experience_meal` exists), SAF-006 event drills on cadence, ORI-020 for each new daypart, CMP-103 renewal, any track by interest.

| Position | Ongoing education | Required for promotion |
|---|---|---|
| FR | BEV-110, FLV-002 beyond the core, MNU-001 to back-waiter depth, SVC-006 back-waiter part as reinforcement, MNU-101 (reading returned plates), SVC-023 once D48 sets it | To BW: **BEV-110 (hard)**. To LFR: release plus designation |
| BW | BEV-111, BEV-015, BEV-112 (in dated sections), BEV-113, BEV-008 at wine level, SVC-017 section handover, SVC-018's senses part (draft, glare, a sound spike, smell, seat temperature), SVC-007, BEV-037 floor level, BEV-035 part one, BEV-028 floor level, MNU-003 started | To FS: **BEV-111, BEV-015, BEV-112, BEV-113 (hard)**; BEV-035 part one, BEV-037 floor level, BEV-028 floor level, MNU-003 started (soft) |
| FS | SVC-101 (first month, D61), BEV-114 (elective), MNU-003, MNU-004 ongoing part, BEV-028 full, BEV-035 full, SVC-073, SVC-047, SVC-056, SVC-019's names-and-seats part, CUL-013, SVC-007, SYS-122, MNU-101 | To LS: MNU-003 and MNU-101 as a collector (soft); release plus designation |
| LS | LEA-002, LEA-014 after calibration (D5), LEA-015, LEA-022, LEA-046, SVC-074 (the drafted bar, for Brandon to confirm), SYS-122 | (none above; MD is a hire) |
| LFR | LEA-003, LEA-002 after calibration, LEA-022, LEA-025, SVC-075 (elective, parked on the chef's expo decision) | |
| H | MNU-001 back-waiter depth, SVC-063, SVC-057, SVC-060 (elective with a mentor), SVC-019's names-and-seats part, SYS-115 to SYS-117 | To LH: **SYS-115, SYS-116, SYS-117 (hard)** |
| LH | SYS-118, SVC-060, SVC-063, LEA-003, LEA-002 after calibration, LEA-022, LEA-046, LEA-037, ADM-114 by delegation, ADM-118 host part when unparked, SVC-070 (parked) | |
| BB | BEV-105 full, BEV-012, BEV-005, BEV-008, BEV-001, FLV-002, BEV-110 (open), BEV-027 at volume, MNU-101 | To BT: **BEV-105, BEV-012, BEV-005, BEV-008, BEV-001, FLV-002 (hard)** |
| BA | BEV-036 (in the first months), BEV-037 (first months), BEV-008, BEV-019, SVC-007, BEV-040, BEV-105, BEV-012, BEV-005 (the route to BT), the rest of the bartender set by interest | To coffee program owner: BEV-036 then BEV-117 (soft). To BT: BEV-105, BEV-012, BEV-005, BEV-008 (hard) |
| BT | BEV-111 full, BEV-035, BEV-036, BEV-037, BEV-116 style part, BEV-028 full, BEV-019, BEV-022, BEV-030 (with its bench-to-proposal part), BEV-040, BEV-032 (elective), SYS-122 | To LB: **BEV-035 part one (proposed hard)**, BEV-111 full (soft), BEV-036 (soft) |
| LB | BEV-035 full, LEA-015, BEV-030, BEV-018, BEV-119 | |
| HB | LEA set, BEV-032, BEV-117 or delegation, BEV-118 (parked until `people.tea_program_owner` exists), BEV-119, BEV-114 as teacher, ADM-102, ADM-103 beverage share | |
| MD | LEA-101, LEA-002, LEA-014, LEA-102, LEA-001 (first month), LEA-046, LEA-045, LEA-037, LEA-032, LEA-033, LEA-041, LEA-023, LEA-007, LEA-017, LEA-021, ADM-103, ADM-104 cover, ADM-111, ADM-114, ADM-115, ADM-118 office part when unparked, SYS-119 to SYS-121, SYS-135, SYS-143, CMP-109 cover; LEA-036 when the panel exists | |
| OM | LEA-101, LEA-002, LEA-014, LEA-102, LEA-005, LEA-016, LEA-103 (first month), ADM-103 further, ADM-111, LEA-032, LEA-033, LEA-021, ADM-118 office part when unparked, SYS-119 to SYS-121, SYS-135, SYS-137, SYS-138, SYS-143 | |
| K | KIT-030, KIT-033, KIT-034, further KIT-023.x stations, KIT-061, LEA-105 (CDP), KIT-045 (KS, CDC), KIT-040, KIT-042, KIT-043 (identified, chef to define), KIT-103 (parked until two dayparts run), MNU-003 culinary form | Chef sets; C to CDP: a first KIT-023.x station |

---

## 4. The knowledge tracks, by level and position

Every track teaches both kinds of advocacy (D54): customer advocacy (finding what this customer wants and would enjoy; SVC-033, BEV-113) and business advocacy (structured product feedback the maker can trust; MNU-101). Every level of every track names its customer element and the MNU-101 note it must produce; the "Advocacy and feedback" column below carries them. Outside courses count only if delivered and tracked inside Trainual (D27); none of the providers below was found to do so (unverified; ask each). Until then each serves as a content benchmark and as prior-learning evidence for test-outs, never as the gate.

**Wine (gates hardest).**

| Level | Module | Hours | Scope benchmark | Who | Advocacy and feedback |
|---|---|---|---|---|---|
| By the glass, at position depth | BEV-102 | in readiness | Sŏn's list | R: FR (one line), BW (at depth), BT (at back-waiter depth), FS, MD at FS depth; H light | Who the glass suits, one sentence; a note on a list change |
| 1 | BEV-110 | about 10 | the first part of WSET Level 2 | O: FR; hard gate to BW. Open to H, BB, BA | Who on our floor would order each by-the-glass wine; one note after a staff tasting |
| 2 | BEV-111 + BEV-015 | about 30 + 6 | WSET Level 2 (verified-primary) | O: BW; hard gate to FS. BT full level 2 (soft gate to LB) | Why each pairing works for the customer in front of you; a note on a pairing |
| 3 | BEV-112 + BEV-113 + BEV-042 | about 60 (in dated sections, `bev.wine_list.sections`) + 10 + 2 per change | CMS Introductory curriculum (verified-primary) plus a hospitality practical in the style of CMS Certified | Hard gate and condition of FS; LS holds it; proposed hiring requirement for the MD | Leading a table from "I don't know wine" to a choice they are glad of; a list-level note (a gap, or a wine customers avoid, and why) |
| 4 | BEV-114 | open | CMS Certified or WSET Level 3 | Elective; the path to a wine seat. HB holds above level 3 at hire | Program-level feedback on submissions and list notes |

Design rules: knowledge at full depth; translation for the customer and reading the customer are separate required elements that are always proven (prove-first allowed); expert vocabulary is a team tool and is graded absent at the table; selling and recommending practice sits inside the track (Orlowski 2022 found certification raised knowledge but not sales, and trainees named missing selling practice; verified-primary). A CMS or WSET certificate counts toward theory test-outs only. Whether Sŏn pays for an outside exam is `policy.wine_cert_sponsorship`.

**Coffee.**

| Level | Module | Hours | Benchmark | Who | Advocacy and feedback |
|---|---|---|---|---|---|
| Floor | BEV-102 | in readiness | | All CF describe the current coffee service | Who would want it after which course |
| 1 | BEV-103, with BEV-120 for whoever pulls the batch | 3 (BT 1.5); BEV-120 2.5 | Sŏn's program | R: BA full, BT short; BEV-120 for `people.espresso_puller` | Which coffee suits which customer and course; a drift log entry that HB can act on |
| 2 | BEV-036 | about 40 | SCA Barista Skills and Brewing intermediate; Barista Hustle Barista One, Percolation, Immersion (verified-primary) | O: BA within the first months (soft); BT, LB on the way to lead | Describing coffee by what the customer likes; a level-2 note to HB on a coffee |
| 3 | BEV-117 | 80 to 120 | SCA Barista Skills professional plus Sensory Skills intermediate, or BH Advanced Coffee Making, Coffee Quality Control and The Water Course | The coffee program owner (`people.coffee_program_owner`), soft gate. The Q Grader is not needed unless Sŏn buys green coffee | Roaster feedback; the coffee menu built from what customers choose |

Constraint to confirm in Box: espresso is batch-pulled in the back and there is no espresso machine on the front bar (WP pp.4 to 5, as the discovery cites it). The readiness need is therefore the back pull (BEV-120, owner set by the chef and HB); hand espresso craft is an elective inside BEV-036, conditional on equipment (`tool.bar.equipment`). BEV-004 (milk texturing) is likewise conditional on texturing equipment on the bar.

**Spirits.** Level 1: BEV-105 (6 h full for BT, a hard gate BB to BT; a 2 h recognition part in readiness for BB and BA). Level 2: BEV-035 part one (about 20 h; WSET Spirits Level 2 scope, verified-primary; soft gate BW to FS for after-dinner spirits; proposed hard gate BT to LB). Level 3: BEV-035 full (about 70 h; WSET Spirits Level 3 scope; LB, HB). Advocacy and feedback: who would enjoy a back-bar bottle neat or in which drink, and one MNU-101 note on a back-bar bottle at levels 1 and 2.

**Beer (only if beer is listed, `menu.beer.*`).** Level 1: BEV-116 serving part (3 h; R for BT and BB). Level 2: style part (6 to 8 h; Cicerone Certified Beer Server syllabus, verified-primary; open). Level 3: owner step (about 60 h; Certified Cicerone scope) only if beer becomes a program. Advocacy and feedback: recommending from what the customer drinks now; one note at the style level.

**Tea.** Floor: BEV-102. Level 1: BEV-104 (R for BA, BT; which tea suits which customer and course). Level 2: BEV-037 (about 30 h; BA and BT in the first months; front-server floor level about 6 h, soft gate BW to FS; WTA Certified Tea Specialist and UKTA Tea Sommelier Award, Service and Innovation as benchmarks, verified-primary; a level-2 note to HB on a tea). Level 3: BEV-118 (the tea owner; parked until `people.tea_program_owner` exists).

**Korean drinks.** BEV-028 short part (2 h; R for BT if listed; floor level for BW and FS, soft gate to FS); full part (about 15 h, open). Advocacy and feedback: recommending from what the customer drinks now; one note. Sources are unverified; founder-sourced and verified before drafting.

**Non-alcoholic.** BEV-025 (R for BA, BT; FS floor part); BEV-040 (O); writing specs through BEV-030.

**Cellar and stock.** BEV-119 (HB, LB ongoing; a receiving part for `people.receiving_roles`): a note on stock condition by supplier or lot.

**Food and menu (gates less hard).** MNU-001 at position depth (R; H 3, FR 5, BW 8, FS 12, BA and BT counter depth 3, MD 12 with prove-first); MNU-002 on every change; MNU-004 readiness part for All, ongoing part open; MNU-003 producers (soft gate FS to LS). Advocacy and feedback: MNU-001 names who each dish suits; MNU-004's ongoing part and MNU-003 each add helping a customer choose (SVC-033) and one MNU-101 note on a dish or producer; MNU-101 itself teaches how to ask a customer for a reaction without fishing, and the line between a customer's taste and a product fault. No recognized certificate exists; it is house knowledge proven in conversation. MNU-007 is no longer a module; interest in going further is raised through ORI-015 and met by KIT-060 and MNU-003.

**By position, at a glance**

| Position | Wine | Coffee | Tea | Spirits | Beer | Korean drinks | Non-alcoholic | Food and menu |
|---|---|---|---|---|---|---|---|---|
| H | floor light; L1 open | floor | floor | floor | floor | floor | floor | MNU-001 host; MNU-004 |
| FR | floor one line; L1 gate | floor | floor | floor | floor | floor | floor | MNU-001 runner |
| BW | at depth; L2 and L3 gate | floor | L2 floor, soft | L2 part one, soft | floor | floor level, soft | floor | MNU-001 BW; MNU-003 started, soft |
| FS, LS | L3 held | floor | floor level | part one | floor | floor level | floor part | MNU-001 full; MNU-003 soft to LS |
| MD | L3 as a proposed hiring requirement | floor | floor level | part one | floor | floor level | floor part | MNU-001 full (prove-first) |
| BB | L1 open | open | open | L1 recognition R; L1 full gate to BT | L1 if listed | | | |
| BA | L1 open | L1 R, L2 soft, L3 owner; BEV-120 if the puller | L1 R, L2 first months | recognition R; L1 full on the route to BT | | | R | counter depth |
| BT | BW depth R; L2 soft to LB | L1 short R; L2 soft to LB | L1 R; L2 O | L1 R; L2 gate to LB | L1 R if listed | short R if listed | R | counter depth |
| LB | L2 | L2 | | L2 to L3 | | | | cellar (BEV-119) |
| HB | above L3 at hire | L3 or delegate | L3 (owner parked) | L3 | L3 if a program | full | specs | cellar (BEV-119) |
| K | | BEV-120 if the kitchen pulls | | | | | | MNU-004; tasting with the chef |

---

## 5. The full module list, by area

Each module appears once. Position parts live inside the one module. Hours are the module's total or per part.

### 5.1 The house (writer 1)

| ID | Title | What it teaches | Positions | R/O | Hours |
|---|---|---|---|---|---|
| ORI-001 | Why Sŏn exists and the standard it holds | The why in Brandon's words (`founder.why_story`); "best in the country" as consistency every night (public criteria cited, never adopted); the standard in the smallest task; learning is work and is paid (the legal rule is cited in CMP-105) | All | R | 2 |
| ORI-015 | How learning, proof and promotion work here | Readiness and ongoing; spoken check, practical, the angel shift (glossed), unsupervised shifts after sign-off, what a recheck is; "not yet" extends the paid window; prove-first for every non-safety module (a failed cold attempt is not a miss); release per daypart after a full night; ongoing education paid at `policy.ongoing_education_hours.<position>`; entry routes; paths and track gates; asking for a direction | All | R | 1.5 |
| ORI-008 | How we talk here | Customer, never the other word; the lexicon (BG 11, cited); first-shift Korean terms (`founder.glossary`) | All | R | 1 |
| ORI-003 | How decisions get made here, and your range | Intent over script; the house's decision order (`founder.decision_order`); your range (`people.*`, `fact.*`); judge the call, not the result; ask and unblock; casebook cases | All | R | 2 |
| CUL-002 | Giving and taking a note at every level | One line in service (always on an allergy); the after-service note; taking a note; the one-line shift review; open critique versus private incident review | All | R | 2 |
| ORI-021 | How one night works, and every name in the building | One full service watched as extra, at shift length, after SAF-007 and the SAF-006 walk that day; tabletop walk door to bar to kitchen to floor; how an order becomes a plate; how one delay travels; the room's intent; every name | All | R | 7 |
| CUL-001 | Pre-shift and the warm-up | Pre-shift as teaching; the warm-up drill at every rank (D44); how to take part | All | R | 0.5 |
| ORI-016 | How we drill: movement apart from decisions | Isolate, change tempo, vary, return to the whole; self-review; a reset routine for composure | All with physical work | R | 0.5 |
| ORI-009 | Talking about the house honestly | Answers to the questions customers ask: what Sŏn is, a Korean term, the chef (`brand.*`), "can I tip?" (`founder.tipping_response`); "let me find out" | CF | R | 1 |
| ORI-033 | Coming in with experience: what to keep, what to drop | Contrast and unlearn against house conventions, by part: runner, server, bar, door, kitchen, management | Experienced hires | R | 1.5 to 2 |
| CUL-011 | Stepping into a station you do not own | The station card for internal movers: what differs, who owns it, the currency check | Internal movers | R | 0.5 |
| SAF-001 | Allergies and dietary needs: knowing, taking and routing | Part 1: allergy, intolerance, preference, religious or ethical need; never judge, never promise; major allergens (confirm at FDA, lead-only); hidden sources including drinks; reaction signs; the route (`workflow.allergy_route`, `chef.allergen_matrix`). Part 2: the words at the table, the door and the counter; confirming back; never promising | All (part 1); CF (part 2) | R | 1.5 + 1.5 |
| SAF-004 | Delivering a modified plate | Marking (`chef.allergen_marking`), the right seat every time, what the runner confirms before lifting | FR, BW, FS, LFR | R | 1.5 |
| SAF-006 | Emergencies: noticing and the first minute | Name one person aloud; first-minute roles for choking, reaction, fall, fire, evacuation, severe intoxication, harassment (`workflow.emergency_plan`); locations as placeholders (D58) | All | R/O | 1.5, then drills on cadence |
| SAF-007 | Moving safely in a shared space | House calls and callback (`chef.call_language`); carrying through traffic; wet floors, breakage, lifting | All | R | 1 |
| SAF-009 | Noticing intoxication, and slowing or stopping service | Part 1: signs, never in public, the quiet handoff (`workflow.intoxication_handoff`). Part 2: the private approach, keeping the customer's face, the stop rule, who to call (`founder.responsible_service_policy`) | CF (part 1); BT, FS, LS, LB, HB, MD, OM (part 2) | R | 1 + 2 |
| SAF-010 | The allergen and food-safety steward on a shift | What the designated steward checks before and during service; parked until Brandon decides the role exists | `people.allergen_steward` | parked | 1 |
| SAF-011 | Handling service ware and food when nobody is watching | The house behaviors beyond the law: stem and handle handling, hands and ware when rushed, speaking up at any rank; proven by observation on the first supervised services. The exclusion list and reporting duty are CMP-113 | All | R | 0.5 |
| CUL-003 | Care as craft, and its cost | The signs before it shows (shortened answers, skipped callbacks, missed small checks, avoiding the pass) in yourself and a teammate; the named routes (`founder.wellbeing_routes`; TBRI review) | All | O | 1 |
| CUL-004 | Receiving someone new onto your floor | Helping a trainee: extra to staffing, give the cue and the check, never take over | All | O | 0.5 |
| CUL-010 | Writing down what went wrong | The blameless note (`founder.incident_policy`) | All | O | 0.5 |
| CUL-013 | Present without performing | Four moments (presenting a dish to an expert, a celebrating table, a complaint, a silent table), each with its cue, the over-performing move and the house move; the held pause | CF | O | 1.5 |
| ORI-023 | How a restaurant makes and loses money, and how the house knows it is working | Principles only; leading indicators (WP Part II) with employee NPS, the cultural labor score and the customer recognition rate each defined in one plain sentence (working wording, to confirm in Box); waits on `founder.open_book_scope` | All | O | 2 |

### 5.2 Service (writer 2)

| ID | Title | What it teaches | Positions | R/O | Hours |
|---|---|---|---|---|---|
| ORI-006 | Two layers: the fixed standard and reading the customer | Which moments are exact and which call for reading; persona cases (BG 05); exactness as care (BG 02, BG 03) | CF (kitchen knowledge-only) | R | 1.5 |
| ORI-020 | The register for each daypart you work | Plain descriptors only; the moment the room changes; late-night part (what loosens, what stays fixed) counted only once late night runs (D24, `workflow.daypart_schedule`); a walk-through never releases a daypart | CF | R per daypart | 1 each |
| SVC-009 | When a customer crosses a line | Step back, get the person holding the room, the mistreated person first, the report; manager part | CF; MD, OM part | R | 0.75 |
| SVC-013 | Calls and callbacks on the floor and at the service bar | Floor calls (`workflow.floor_calls`); closed loop; service-bar pickup and check; service-well part shared with BEV-016 | Floor | R | 1 (+1 BW; +0.5 FR only if `workflow.runners_carry_drinks`) |
| SVC-015 | Acting on a protocol flag | What a flag means and the move it requires, without improvising (`tool.reservations.flags`) | Floor | R | 0.5 |
| SVC-079 | Calling your own load early | What never drops (allergy call, callback, seat check); asking before the point of no return | Floor | R | 0.5 |
| SVC-003 | Carrying plates, trays and glass racks (drills) | Two and three plates, hot plates, stemware tray, at three tempos while talking; quiet set-down in seat order | FR (BW, FS inherit) | R | 4 |
| SVC-071 | Glass, silver and linen: handling, polishing, inspection | Stem and handle only; polishing to the standards book (D46); inspection under light; bar part: every house glass and its drink, chilling, rack loading, breakage | FR, BW (floor part); BB, BA, BT (bar part) | R | 1.5; 2 |
| SVC-004 | Moving through the room and walking a customer in | Runner part: routes, never blocking a path or sightline, never pointing. Host part: lead distance, scanning while walking, the reveal; access route (`facility.*`) | FR, H | R | 1.5; 1 |
| SVC-018 | Scanning on every trip | What to look for and report; habit drill; BW ongoing part: the room's senses (draft, glare, a sound spike, smell, seat temperature) and the fix for each | FR; H, BW part; BW O | R/O | 1; 0.5; 1 |
| SVC-019 | Seeing the table as positions | Seat numbering (`workflow.position_numbering`); counter seats; ongoing part: methods for holding names and seats, never screened on memory | FR, BW, FS, BT; O open | R/O | 1; 1 |
| SVC-008 | Describing honestly, at the right length | Set-down line (FR); the second question (BW); full, without instructing (FS); bar part (BA, BT); ongoing: storytelling and voice | FR, BW, FS, BA, BT | R/O | 0.5 to 1 per part |
| SVC-006 | Reading a table | Runner part: when to enter and when to hold a beat. BW part: table state and acting before asked; where the customer's attention is. FS part: check back by what changed, never the clock | FR, BW, FS | R/O | 0.5; 2; matures in O |
| SVC-002 | Recovering a miss within your range | Repair between pass and table (FR); matching the make-good to the loss; ranges (`fact.recovery_range.*`); lead and widest parts | FR, BW, FS, LS, MD | R | 0.5 to 2 per part |
| SVC-025 | Clearing and resetting (drill) | Quiet clearing, no reaching across; when to clear (`workflow.clearing_rule`, D48) | BW, FS | R | 2 |
| SVC-028 | The body at the table | Approach, stillness at eye level, leaving without hovering | BW, FS | R | 1 |
| SVC-027 | Working the pair | Signals (`workflow.pair_signals`); no duplication or collision; the handoff at the table | BW, FS | R | 2 |
| SVC-072 | Setting a place exactly, and the walk before doors | The standards book (D46); seeing a set room's faults | BW, FS; H, MD part | R | 1.5; 0.5 |
| SVC-017 | Handing over so the receiver can act | Door part (the read to the server); section part at break or close | H door part R 0.5; BW ongoing; FS inside SVC-036 | R/O | 0.5 |
| SVC-029 | Opening the table | The coverage position (BG 15) | FS | R | 1 |
| SVC-032 | Taking the order and reading it back | Accuracy, allergies on the closed loop, method (`workflow.order_capture`, D48) | FS; BT counter part | R | 2 |
| SVC-033 | Helping a customer choose | Opening with what they love; the second and third question; offering from what was said, never the favorite or the price; food and drink together; drink part for the bar | FS; BA, BT part | R | 3; 1.5 |
| SVC-035 | Pacing a table's meal and firing the next course | By the table, never the clock (`workflow.fire`, `chef.*`) | FS | R | 3 |
| SVC-036 | Holding a section under load | Not losing one table to serve another; the section handover | FS | R | 2 |
| SVC-037 | Saying no well | An 86, a policy no, an item gone; door part (walk-in no) | FS, BT; H part | R | 1; 0.5 |
| SVC-038 | The check, payment and departure | The check when the table is done, discreet payment (`tool.pos.payment`), the departure (BG 13) | FS, BT; H part | R | 1; 0.5 |
| SVC-078 | The standard sequence of a visit, end to end | The whole visit in each daypart's register; the capstone practical, its own staged block, never on the angel shift and never banked | FS | R | 4 |
| SVC-103 | Opening, closing and side work on the floor and at the door (placeholder) | Why the order matters; stations to par, the walk before doors, the door's opening; running side work; the close; the checklist and its sign-off (`workflow.floor.*`, `workflow.door.*`, D58) | H, FR, BW, FS; leads sign off | R | inside supervised shifts |
| SVC-010 | Receiving the customer at the threshold | Arrival canon (BG 15, D20); recognition by a check, never a memory gamble | H, LH, MD | R | 1.5 |
| SVC-011 | Why the door sets the kitchen's tempo | Seating by what is open breaks the pass; pacing rules (`workflow.pacing.*`) | H, LH, MD | R | 1.5 |
| SVC-059 | Holding a wait with an honest quote | The quote, updating it, bridging to the bar | H, LH; BT part | R | 1 |
| SVC-062 | First contact by phone and in writing | The house register (BG 11); a no that keeps the relationship (craft; tool in SYS-114) | H, LH | R | 1.5 |
| SVC-012 | Access for customers with mobility or sensory needs | Arrival, route, seating; service-animal law linked | H, LH, MD | R | 1 |
| SVC-068 | Holding the door by delegation | Handback triggers named before service (BG 15, D20) | LH | R (lead seat) | 3 |
| SVC-057 | Pacing calls inside the rules | Yes, wait or no into a jammed room | LH; H O | R (lead seat) | 2 |
| SVC-063 | Reading the whole room | The room's load and mood; listening to the room | LS, MD; H, LH O | R/O | 2 |
| SVC-066 | Directing the runs | Two runners never to one table; plates never stack; under the expo's call | LFR | R (lead seat) | 3 |
| SVC-067 | Stepping in without taking over | Moving help without taking the table relationship (WP p.8) | LFR, LS, MD | R | 2 |
| SVC-069 | Holding the room's sound and light | What the MD may and may not change, in plain words (a proposed reading of BG 14, bound `brand.sound_light_authority`); five drift signals and the correction for each | MD | R | 1.5 |
| SVC-060 | Composing the room | Who sits near whom, section load, occasions | LH; H elective | O | 4 |
| SVC-070 | Calling the late-night turn, and the pyeong-sang escort | Parked until the daypart runs and the layout exists (`people.late_night_trigger`, D58) | LH, MD | parked | |
| SVC-047 | Making one moment specific | The occasion, the gesture, generosity as a decision inside range (WP p.26); the thank-you note | FS | O | 3 |
| SVC-073 | Reading and lifting a table's mood | The cues for four starting states (tense, tired, rushed, disappointed) and the lift move for each; handing the read forward | FS | O | 2 |
| SVC-101 | Follow-up emails to the customers you served | When an email is sent and when not; consent (`compliance.messaging`); the register (BG 11); one true specific detail; what is never in it; writing fast; finding the history first (SYS-111, SYS-122); what to do with a reply (D61; `tool.email.*`, `workflow.follow_up_email`) | FS | O (first month) | 2 |
| SVC-056 | Noticing and noting | What is worth noting (craft; the tool is SYS-112); proven by the lead host's audit of the person's real notes over the first month | FS, BT, H | O | 2 |
| SVC-007 | Comparing your calls with the house panel | Measurement only, service and bar cases; the house panel is a set of judgment cases answered by Brandon and calibrated leads | BW, FS, BA, BT | O | standing |
| SVC-023 | Team set-down | Waits on the D48 convention | FR, BW, FS | O | 1 |
| SVC-074 | The path to master server | The drafted bar for Brandon to confirm or change: the widest table range (expert, split, conflict, press) at the LS recovery range; the panel's calls matched on SVC-007; wine to BEV-114; teaching by LEA-001; MNU-101 notes the chef and HB act on | LS | O | open |
| SVC-075 | Working the service with the expo | One caller, one moment; parked on the chef's expo decision | LFR elective | parked | |
| SVC-044 | Dining at Sŏn as a customer | A meal as a customer (`founder.staff_experience_meal`) | All | O | 3 |

### 5.3 Food and menu (writer 2)

| ID | Title | What it teaches | Positions | R/O | Hours |
|---|---|---|---|---|---|
| MNU-001 | Every dish on the current menu, at your position's depth | Per dish, on a printed card: name and pronunciation, components, technique, origin and intent, vessel and maker, allergens, taste and who it suits (`chef.menu.*`, `chef.tableware.*`); host shape and allergen hand-off; runner set-down depth; BW second question; FS full; counter depth | H 3, FR 5, BW +3, FS +4, BA/BT 3, MD 12 (prove-first) | R | as listed |
| MNU-002 | When the menu changes | The change, allergen change first, tasting at pre-shift, spoken check before first service | All who serve or describe | O standing | 0.5 to 1 per change |
| MNU-004 | Korean food culture behind the menu | R part: the references on the current menu. O part: seasonality, fermentation and the jang, rice, soup and banchan, eating together; helping a customer choose from it; one MNU-101 note | All | R/O | 1; about 10 |
| KIT-003 | What the kitchen needs from the floor, and why | Honest times, early 86s, what a modification costs mid-fire (`chef.modification_policy`), fire when the table is ready, kitchen visits set before service; taught by the chef | FR, BW, FS, leads, MD (the host's slice is inside SVC-011) | R | 1.5 |
| ORI-005 | How flavor works: what we say changes what they taste | Three effects, each with a team tasting: description changes perceived taste; vessel and sound change taste; the honesty line. Parked until its sources are verified | CF | parked | 2 |
| MNU-003 | Producers and where the food comes from | Who grows and makes it, why the chef chose them; which customer a producer story serves; visits on the clock; one MNU-101 note | FS soft gate to LS; open | O | 10 to 20 a year |
| MNU-101 | Product feedback: from the customer to the maker | The note: what was served, what the customer said or left, what you tasted, who it suits, keep or change; taste versus fault versus fit at the table; asking a customer for a reaction without fishing; trusted after the tasting check; how it reaches the chef and HB and how they answer (`workflow.product_feedback`) | All after release; leads collect | O | 1, then standing |

### 5.4 Beverage (writer 3)

| ID | Title | What it teaches | Positions | R/O | Hours |
|---|---|---|---|---|---|
| BEV-017 | How the beverage program is built, and how to hold it | What is batched, pulled in the back, finished at the bar, and why (WP p.4 cited); habits to drop; who owns a spec | BB, BA, BT, LB, HB | R | 2 |
| BEV-001 | The four variables | Temperature, dilution, texture, extraction, each taught over a flawed drink | BB ongoing (gate to BT); BA, BT R (green external BA prove-first) | O/R | 2.5 |
| BEV-002 | Pour control (drills) | Brandon's water-pitcher sequence, measured flow, jigger, bottle, milk stream; floor part: pitcher, bottle, still and sparkling water, pour levels | Bar; BW, FS (floor part) | R | 4; 2 |
| BEV-003 | Station and body (drill) | The set station, order of reach, reset after each drink (`workflow.bar.station_layout`) | BB, BA, BT | R | 2.5 |
| BEV-016 | Moving together behind the bar | House calls with callback, passing lanes, who yields, handoff at the well | BB, BA, BT; FR, BW part via SVC-013 | R | 2 |
| BEV-014 | Glass and ice: the contamination call | Glass near ice burns the well, always; how to burn it safely | BB, BA, BT | R | 1 |
| BEV-024 | Working in the sightline | What reads as mess; onstage and backstage; uniform (BG 13, BG 15) | BB, BA, BT | R | 1 |
| BEV-033 | Bar prep to spec | Prep list, citrus and hold, syrups, garnish, ice, labeling and rotation, batching within limits; drift by look, smell and taste | BB (full); BA, BT (house portion) | R | 6; 3 |
| BEV-101 | Opening, closing and side work at the bar (placeholder) | Why each task exists, what done looks like, the handoff note; sequence bound (`workflow.bar.*`, D58) | BB, BA, BT | R | inside supervised services, counted at shift length |
| FLV-002 | The smell library | Core aromas from reference kits, near-miss pairs, house words | BB ongoing (gate to BT); BA, BT core R; open O | R/O | 2 |
| BEV-102 | The current drink list, at your position's depth | Every drink and wine on the list: H names and hands off; FR one line and the glass; BW by-the-glass at depth (grape, place, style, temperature, why listed, its dish); FS describes and recommends every list; BB name, glass, garnish, ice; BA coffee, tea and non-alcoholic in full; BT every drink in full spec; category primers (tea categories, spirit bases, beer, Korean drinks); re-proven on every list change | All CF | R | H 1, FR 1.5, BW +3, FS +2, BB 2, BA 2, BT 6 (+4 from BB), MD 6.5 (prove-first), HB 6 |
| BEV-103 | The house coffee program | What Sŏn pours, where it is pulled, hold times, origin and process, which coffee suits which customer and course, honest answers to the coffee-literate customer | BA (full), BT (short) | R | 3; 1.5 |
| BEV-120 | Pulling and holding the batch espresso | The spec and only the spec (`bev.spec.espresso.*`); the method (`chef.batch_espresso_method`); tasting against the reference; the drift log; cleaning; hot-equipment safety every attempt | `people.espresso_puller` (BA, a kitchen position, or both; chef and HB decide) | R | 2.5 |
| BEV-104 | Tea and matcha to the house standard | Every tea on the list; dose, water, time; the founder matcha method (`founder.matcha_method`); describing each in two lines; which tea suits which customer and course | BA, BT | R | 3.5 |
| BEV-004 | Finishing on house-textured milk (drill) | Water first; placing and cutting; the house finish; alternative milks; the steam-wand safety element every attempt. Conditional on `tool.bar.equipment`: with no texturing on the bar it moves to wherever milk is textured, or drops | BA, BT | R (conditional) | 3.5 |
| BEV-006 | Reading the dispensed product | In-spec versus drifted pairs; pull and flag, never fix at the counter | BA, BT; LB owns the call | R | 2 |
| BEV-025 | The customer not drinking alcohol | Equal ceremony, never asking why, every non-alcoholic drink, a build | BA, BT; FS floor part | R | 2; 1 |
| FLV-005 | Checking your palate before you judge | A fixed reference before any quality call; deferring to a second taster | BA, BT; anyone tasting for quality | R | 1 |
| BEV-008 | The house tasting grid | One grid for every drink, and the plain words used with customers | BB (gate to BT), BA O; BW, FS inside the wine levels | O (gate) | 2 |
| BEV-026 | The morning window | The morning register, standing orders, regulars, queue triage at the window | BA | R | 3 |
| BEV-020 | Holding the spec or moving it | What may move, within what range, who to tell | BA, BT | R | 1.5 |
| BEV-023 | Hosting the counter | The counter as a table; reading a solo customer; pacing a counter meal | BT | R | 2.5 |
| BEV-021 | Two queues: the counter and the service well | Ticket age against the counter; triage; calling for help | BT | R | 2 |
| BEV-012 | The build (drills) | Two-handed measuring; shake, stir, strain to dilution and temperature targets; tempo ladder | BB (gate), BT | O/R | 8 |
| BEV-005 | Classic drinks and their families | Templates, balance, a reasoned variation | BB (gate), BT | O/R | 6 |
| BEV-105 | Spirits on the back bar | Every bottle: category, base, production, taste, alternative, allergens, who would enjoy it; neat pours; one MNU-101 note on a back-bar bottle. Full part held before the BT window; readiness only for an experienced external BT. Recognition part in readiness for BB and BA | BT; BB, BA recognition | O/R; R | 6; 2 |
| BEV-015 | Opening and pouring wine and sparkling (drill) | Presenting, opening still and sparkling safely, pour order, decanting, a refused bottle; sparkling safety never tests out | BW (gate to FS); BT bar part | O/R | 6; 2 |
| BEV-116 | Beer: serving, styles and freshness | Serving part: glass, pour, head, lines, bad pours. Style part. Owner step | BT, BB (if listed); open | R/O | 3; 6 to 8; 60 |
| BEV-028 | Korean drinks: soju, makgeolli, yakju and cheongju | Short part: what each is and how it is poured. Full part: fermentation, producers, honest history, pairing | BT (if listed); BW, FS floor level | R/O | 2; 15 |
| BEV-027 | Reading the bar ahead | Cues: a party seated, late night, a run on a component; stays in barback readiness (it is the barback's job); at volume ongoing | BB | R/O | 2 |
| BEV-110 | Wine 1: what is in the glass and how to say it | How wine is made; structure in customer words; the principal grapes; the by-the-glass list and who on our floor would order each; handling and off glasses; "let me bring someone"; one MNU-101 note after a staff tasting | FR (gate to BW); open; a cold check of about 2 h for an experienced external BW | O | 10 |
| BEV-111 | Wine 2: the whole list by style, the pour, the pairing reason | Level 2 depth through Sŏn's list; why each pairing works; top-ups and glass changes; faults | BW (gate to FS); BT | O | 30 |
| BEV-112 | Wine 3: Sommelier 1-level knowledge on Sŏn's list | The CMS Introductory scope; deductive tasting inside the team; the list in depth; translation to customer language; a list-level MNU-101 note; paced in dated sections (`bev.wine_list.sections`) with banked section checks and an unbanked integrated spoken check and tasting | BW; condition of FS; proposed hiring requirement for the MD | O | 60 |
| BEV-113 | Recommending wine | Opening questions, reading the table, budget without numbers (`policy.price_conversation`), two or three honest options; role-play against set customer profiles; always proven, prove-first allowed (the same role-play cold, about 2 h, floor observation after release) | FS gate; BW light; BT where the bar sells wine | O | 10 |
| BEV-042 | Presenting the pairing | What meets what; the one-breath version and the longer one; adjusting for a customer who dislikes it or is not drinking | FS, BT where the bar pours it | R per change | 2 |
| BEV-114 | Wine beyond the front server | Toward Certified or Level 3 depth; running a staff tasting | Elective | O | open |
| BEV-035 | Spirits in depth | Part one: production stages, categories, cocktail families (WSET Level 2 scope), who would enjoy a bottle, one MNU-101 note on a back-bar bottle. Full: production choices, labelling, blind assessment, plain description | BW soft, BT to LB; LB, HB | O | 20; 70 |
| BEV-036 | Coffee craft | Extraction and strength, grind, ratio, water, the back pull (BEV-120), brewing, describing coffee by what the customer likes, a level-2 note to HB on a coffee; hand espresso as an elective conditional on equipment | BA (first months); BT, LB | O | 40 |
| BEV-117 | Owning the coffee program | Cupping and calibration, quality control on shift, roaster feedback, water spec, the coffee menu | Coffee owner | O | 80 to 120 |
| BEV-037 | Tea craft and tea service | Processing and the categories, brewing styles, water, Korean tea, tea with food, a level-2 note to HB on a tea | BA, BT; FS floor level | O | 30; 6 |
| BEV-118 | Owning the tea program | Sourcing criteria, the calibration protocol, the list structure, supplier feedback, pairing with the chef; parked until `people.tea_program_owner` exists | Tea owner | parked | 40 to 60 |
| BEV-040 | Non-alcoholic craft in depth | What replaces ethanol's body and length; building the list | BA, BT | O | 10 |
| BEV-019 | Calibrating palates as a team, and tasting the bar on a shift | Triangle tests as practice; agreeing on in-spec; on-shift tasting rhythm | LB runs, HB owns; bar | O | standing |
| BEV-119 | Cellar, storage and stock condition | Receiving against the order and catching a damaged bottle; storage conditions (`bev.spec.cellar`); the cellar map and rotation (D58); vintage changes told to the floor before service; open-bottle life; one MNU-101 note on stock condition | HB, LB; `people.receiving_roles` (receiving part) | O | 3 |
| BEV-018 | Back-of-house beverage prep and its quality check | Batch prep, liquid nitrogen and pressure holding within CMP-112 and its SAF-003 house part | HB, LB | O | 6 |
| BEV-022 | Blind-testing a method before it changes | Blind tests before a method changes | BT, LB, HB | O | 4 |
| BEV-030 | Writing a spec someone else can execute | Spec format, ranges, reasons; from bench to proposal (where and when development happens, from BEV-031) | LB, HB | O | 4 |

### 5.5 Culinary (writer 4; draft for the executive chef)

| ID | Title | What it teaches | Positions | R/O | Hours |
|---|---|---|---|---|---|
| KIT-102 | Starting in Sŏn's kitchen | Who decides; BG 01 and BG 07 in a kitchen; asking before acting; how the kitchen learns; kitchen languages (`founder.kitchen_languages`) | K | R | 2 |
| KIT-101 | What the kitchen must know about the floor | Step-back service (BG 15), personas (BG 05), recovery range, how the door's pacing becomes the line's surges, what tonight's book says | K (porter 1) | R | 2 |
| KIT-002 | The pass: call, callback, handoff | The closed loop; the call list (`workflow.pass.call_lexicon`); threshold volume (BG 13); what the runner confirms before lifting; checking a plate at the pass; wrong, late, missing | Cooks, the pass; FR, BW, FS floor side; LFR expo part | R | 2 |
| KIT-010 | The porter's craft | Flow drills: scrape, sort, rack, load, run, unload, return; priority when calls collide (`chef.porter_priority`) | P | R | 6 |
| KIT-012 | Knife and body (drills) | One movement at a time, slow to fast, short spaced sessions; the knife-safety element (grip, guard hand, board stability, carrying and passing) every attempt, never tests out | C, CDP, CT | R | 10 |
| KIT-013 | Mise en place, the line check and clean as you go | Setup, the spoken line check (`chef.line_check`), the organized withdrawal, the chef's own food-safety controls (`chef.food_safety_rules`, moved from CMP-110) | C, CDP | R | 4.5 |
| KIT-015 | Receiving, storing, labeling, rotating | First in first out, storage map (`chef.storage_map`), labels | P, C | R | 2 to 3 |
| KIT-016 | Moving and calling in the kitchen | The kitchen's calls, built on SAF-007 | K | R | 2 |
| KIT-020 | Prep production: list, par, sequence | Prep follows service need, lead times, holding | C | R | 3 |
| KIT-021 | Recipes as specs and as reasons | Each assigned recipe and why it is built that way (`chef.recipe.*`) | C, CDP | R | 3 |
| KIT-022 | Tasting and seasoning to the house | Taste references (`chef.taste_reference.*`); state the adjustment before applying it | C, CDP | R | 2 |
| KIT-023.x | Station modules, one per station | Items, holds, plates, layout (`chef.station.<name>.*`); release is solo on a named non-peak service | CDP, CT | R | 16 per station (chef to reset) |
| KIT-024 | Cooking to the call | Fire, hold, finish, plate so a table's plates land together | CDP | R | 4 |
| KIT-031 | Entering a station without disrupting it | Read the board, ask the owner, repeat back, take a named task, hand back | CT | R | 2 |
| KIT-103 | Daypart transitions in one kitchen | What changes between dayparts (D24; which dayparts run at opening is `workflow.daypart_schedule`); parked until two dayparts run | CDP, CT | parked | 1 |
| KIT-104 | Opening and closing the kitchen (placeholder) | Durable part only; sequences bound (D58) | K | R | inside paired shifts |
| SAF-013 | Allergens and cross-contact in production | The chain from reservation to plate; controls in storage, prep, cooking, plating; when to refuse a modification | Cooks, the pass (porter 1) | R | 3 |
| KIT-030 | Owning a station through a full night | Peak nights after release on a non-peak service; signed off over a window of shifts (D10); the full nights are the evidence, no test-out | CDP | O | window |
| KIT-033 | Yield and total utilization | Yield, trim, waste data | C, CDP | O | 4 |
| KIT-034 | Recovery from the kitchen side | Refire rules (`chef.refire_rules`) and what the floor does with them | CDP | O | 2 |
| KIT-040 | Running the pass | Identified, chef to define; who expos is a chef call | KS, CDC | O | chef to set |
| KIT-042 | Developing a dish inside the brand | Identified, chef to define; away from service; codified | KS | O | chef to set |
| KIT-043 | Codifying the kitchen | Identified, chef to define; knowledge in the system, not in a person (WP p.37); the library mechanics sit in LEA-037's kitchen part | Pair, CDC, EC | O | chef to set |
| KIT-045 | The kitchen's part in pre-shift | Tasting with the floor, menu teaching with MNU-001 and MNU-002 | KS, CDC | O | standing |
| KIT-060 | A rotation through the kitchen | Floor elective | Floor | O | 8 |
| KIT-061 | A shift on the floor | Kitchen elective | K | O | 8 |

### 5.6 Leadership and teaching (writer 4)

| ID | Title | What it teaches | Positions | R/O | Hours |
|---|---|---|---|---|---|
| LEA-001 | Teaching on the floor | The job breakdown, modelling, fading support; when to step in, teach or let it run | All leads (lead seat), mentors; MD first month | R (lead seat); MD O | 3 |
| LEA-011 | Coaching a movement drill | Isolate the pattern, vary tempo, fade feedback | LFR, LB, kitchen leads | R (lead seat) | 3 |
| LEA-018 | Holding the standard as a peer | The standard walk; saying it without policing | All leads | R (lead seat) | 1.5 |
| LEA-005 | Running pre-shift as teaching | Teaching not announcements; the warm-up; leads' update parts (host, bar) | MD, LH R; OM first month; leads' parts | R/O | 2; 1 |
| LEA-019 | Teaching one thing at pre-shift | For anyone who takes the rotating slot (D43) | Volunteers | O | 1 |
| LEA-015 | Mentoring a new hire through the path | The mentor's role (D21), trailing log, check-ins | Designated mentors | R before first mentee | 2 |
| LEA-003 | Running the angel shift | Supervising without taking over; what is recorded | Mentors, leads, managers | O | 1 |
| LEA-002 | Assessing a practical | Frame-of-reference calibration, process and product rated apart, safety passes every attempt, co-rated audits; kitchen part | MD, OM (before first assessment, D19); leads, HB, kitchen leads before signing alone | O | 6 |
| LEA-014 | Holding a spoken check | Set cases, neutral questions, score the content, sample the unit | Same as LEA-002 | O | 2.5 |
| LEA-016 | Delivering a not-yet and the changed practice plan | The conversation and the plan (D11); a not-yet extends the paid window | MD R; OM first month; assessors O | R/O | 1.5 |
| LEA-006 | The unblock conversation | The four recorded outcomes (D13): learning opened, a move opened, reserve, not now with a reason and a reopen trigger (Brandon to confirm); carries the annual recommitment step (`workflow.recommitment`) | MD, OM, leads | O | 1 |
| LEA-101 | Running booked check slots | Protected slots (`workflow.check_slots`), preparing from the record, writing the gate record at close (D8); the recheck cadence; assessor hours per cohort against `workflow.live_gate_limit`; the pre-opening calendar | MD, OM; calibrated leads | O (first month) | 3 |
| LEA-102 | The manager's side of the learning system | Assigning paths and variants, running prove-first attempts, recording release per daypart, placing ongoing-education hours, routing overrides to Brandon | MD, OM | O (first month) | 3 |
| LEA-103 | Building a new hire's readiness plan | Choosing the variant, laying out the window day by day (section 2.6) with retry room, the mentor, the ninety-day plan | MD R; OM first month; kitchen pair before the first cook's start | R/O | 2 |
| LEA-024 | Reading the team's load | Who is going under, the signs before it shows | LS, MD; LB O | R | 2 |
| LEA-027 | Giving intent, not instructions | Stating intent so the team can act when the script breaks | MD, OM, kitchen pair | R | 1.5 |
| LEA-028 | The parallel pair in service | What the MD holds and the OM holds on the night | MD, OM | R | 2 |
| LEA-029 | Owning the room, delegating the door | Not a super-server or a host; stepping into the door on named cues | MD | R | 3 |
| LEA-010 | Calling a live failure across domains | The agreed rule between the pair | MD, OM | R | 1 |
| LEA-021 | Running a private incident review | Process first, no blame (WP p.17) | MD, OM, kitchen leaders | O | 3 |
| LEA-022 | Stewarding everyday critique | Keeping open critique open and safe | Leads | O | 1.5 |
| LEA-023 | Noticing drift | The watchlist signals, named: healthy, complacency and drift (a step skipped on an ordinary night, a recheck miss pattern, silence in critique rounds) | MD, OM, leads | O | 1.5 |
| LEA-025 | Leading one improvement at a time | Picking one, measuring it, closing it | Leads | O | 2 |
| LEA-046 | The nightly review of the service | What went right, wrong, one change; the decision note | MD runs; LH, LS | O | standing |
| LEA-036 | Explaining the call: the reference panel | Anchoring panel cases; parked until the D14 panel exists (explaining a call sits in LEA-037) | MD, EC | parked | open |
| LEA-037 | Capturing a decision for the house library | The decision interview method; explaining a call; the library, with a kitchen part | MD; kitchen leaders (kitchen part) | O | 2 |
| LEA-045 | Inspecting the house as a customer would | Outside eyes; the inspection walk with nine named stops (arrival and wait, threshold, restroom, set table, sound and light, bar sightline, departure and more) and what is checked at each | MD | O | 3 |
| LEA-007 | Taking critique and repairing a lapse in front of the team | The leader's side: closing the loop on a note from below, never paying a note back, the repair after a lost temper, routing to the HR route under CMP-103; two role-plays (merges LEA-047) | MD, OM, leads | O | 1.5 |
| LEA-017 | The fit conversation after repeated misses | Honest, private, with a path | MD, OM | O | 1.5 |
| LEA-041 | Governing the house's customer relationships | So books do not drift or leave with a person (tool side in SYS-120) | MD | O | 2 |
| LEA-004 | Writing and reviewing a module | Parked with SYS-144 until Brandon opens authoring (D1) | Authors | parked | open |
| LEA-104 | Leading a kitchen without harm | Intensity and precision kept, degradation not; correction in private | Kitchen pair, CDC, EC | R | 4 |
| LEA-105 | Briefing, coaching and teaching at the station | The station brief, coaching a cook | CDP O; CT, KO, KS, CDC R (counted in their windows) | R/O | 3 |
| LEA-106 | The executive chef's onboarding to the people and training system | Who owns what (D1, D30); the readiness window in the kitchen; how proof works; booked check slots and the live-gate cap; what the EC signs; correction and critique in a kitchen; kitchen paths and ongoing education | EC, inside onboarding | O | about 6 |

### 5.7 Administration (writer 4)

| ID | Title | What it teaches | Positions | R/O | Hours |
|---|---|---|---|---|---|
| ADM-101 | The office day | The day's rhythm (`workflow.office_day`); the pair's split (WP Part I); one manager doing the other's work, or doing by hand what a system should do; no admin during service; the weekly cadence | MD, OM | R | 12 |
| ADM-102 | Reading labor | Load and coverage first; learning hours never cut; the signal that the team has no capacity left (fix the design, not the hours); leading indicators with employee NPS and the cultural labor score defined as in ORI-023; targets as `fact.*` | OM R; MD, HB O | R/O | 4 |
| ADM-103 | Reading cost, sales and the business | Cost terms, theoretical versus actual, comps and voids, waste; what moves each number; the AI read as a prompt | OM R; MD, HB, LB O | R/O | 5 |
| ADM-104 | Building and running the schedule | Scheduling against demand; coverage only by released people (D10); what the schedule protects, ongoing-education hours and a certified food protection manager on every hour included; records kept two years (29 CFR 516.6); owns the one shared practical with SYS-134 (7 h in total) | `people.schedule_owner` R; other manager O | R/O | 6 |
| ADM-105 | Ordering, receiving, inventory and variance | Par and reorder, receiving against the order, credits, counts, telling variance causes apart | OM, HB R; LB R (lead seat); KO kitchen part; `people.ordering_roles` | R | 6; LB 4 |
| ADM-106 | Payroll handoffs and time records | Approvals before cutoff, missed punches with the employee's confirmation, the never-do list, records three years (29 CFR 516.5) | OM R; MD cover | R | 4 |
| ADM-108 | Hiring paperwork and onboarding before the first shift | I-9 Section 2 within three business days; certificates; the mentor and uniform ready before day one | OM R; MD O | R | 3 |
| ADM-109 | The documentation standard | One home per record type; facts before judgment; written at close | MD, OM, all leads | R | 3 |
| ADM-110 | Incident records and the duty to report | First moves by incident type; care first; notification order; OSHA reporting duty (windows bound); harassment to the HR seat | MD, OM; leads' first-response part in ADM-117 | R | 4 |
| ADM-111 | Vendor relations | Specs in writing, same-day quality issues, credits, producer stories for the floor, gifts policy | OM, HB, MD | O | 1.5 |
| ADM-112 | Facility, maintenance and repair | Triage, preventive calendar, pest and waste records | OM | R | 2 |
| ADM-113 | Closing the day | Open checks, voids and comps reviewed, payments reconciled, cash with two people, unexplained differences escalated; a lead's close version (cash and the deposit stay with managers) | MD, OM; closing leads (`people.close_roles`) | R | 3; lead version 2 |
| ADM-114 | After the visit: correspondence, reviews and the loop | Written replies in the house register; what goes back into the record; one teaching point | MD; LH by delegation | O | 2 |
| ADM-115 | Reading the system's outputs and acting on exceptions | Act, watch, ignore; system fault versus operational fault; the fallback drill | OM R; MD, HB O | R/O | 3 |
| ADM-117 | The lead's administrative duties | The lead's close note, sign-offs, reporting repairs, helping with counts, first response on an incident, swaps by the rules, where a lead's authority stops (D5) | All leads | R (lead seat) | 2.5 |
| ADM-118 | Events and private bookings | Office part: inquiry to event sheet (`founder.events_policy`, `fact.*` terms, `chef.event_menus`, staffing inside ADM-104's protections, the follow-up). Host part: routing and booking, never quoting terms. Floor part: the event briefing, allergies confirmed at the door, a fixed menu in sequence, who may change the plan. Identified, parked on Brandon's events answer | MD, OM; LH and hosts; the floor and bar | parked | about 3; 1; 1.5 |
| LEA-032 | Interviewing together | The white paper hiring system; structured interviews with a shared scale (Sackett 2022); independent ratings; the transparency sheet | MD, OM before the first interview | O | 6 |
| LEA-033 | Running the paid practical interview | Paid, tasks told in advance, fixed procedure, two raters; kitchen variant | MD, OM, HB; KO, EC for cooks | O | 2 + first run |
| BEV-032 | Program economics | Pour cost and waste as decision inputs (`fact.*`), with ADM-103's method | HB; LB elective | O | 4 |
| KIT-041 | Kitchen production and operations | Forecast to prep list, ordering, labor inside policy, maintenance (WP p.13) | KO; CDC, EC O | R | 4 |

### 5.8 Systems and technology (writer 1)

Every tool name is a candidate from Sŏn's archived SaaS catalog (lead-only), except where the white paper names SevenRooms as the customer identity spine. Every step is a `tool.*` binding.

| ID | Title | What it teaches | Positions | R/O | Hours |
|---|---|---|---|---|---|
| SYS-002 | The learning system: finding, doing and logging your training | Signing in, your path, a module, booking a check (D13), flagging content, uploading a certificate, logging remote paid time (Trainual) | All | R | 1 |
| SYS-101 | Using systems well | The system is the house's memory; your login is yours; devices only where allowed (D8); data you may see and share; the fallback; reporting a tool problem | All | R | 0.5 |
| SYS-103 | Payroll and HR: your pay and your records | Setup, direct deposit and tax forms, reading a pay stub from a sample (owned here), policies, reporting a pay error (Rippling, candidate) | All | R | 0.75 |
| SYS-104 | Scheduling and the time clock | Your schedule, availability, time off, swaps only to someone released on that position, clocking in and out, the missed punch (owned here), remote training clocked (tool open) | All | R | 0.75 |
| SYS-105 | Team communication | Which channel for what; never customer data or incident details in chat; off-hours rule (tool open) | All | R | 0.5 |
| SYS-110 | SevenRooms 1: booking, finding, changing, cancelling | Why everyone books; search before you create; the fields in order; the read-back; cancel versus no-show versus delete; allergy in the allergy field; the practice rule | All, kitchen included | R | 2 |
| SYS-111 | SevenRooms 2: reading the customer record before you approach | Visit notes versus profile notes; the pre-service view; reading for the one or two items that change your service; using it without reciting it; spend never changes warmth; door, table, counter and kitchen versions | All (CF +0.5) | R | 1 to 1.5 |
| SYS-112 | SevenRooms 3: writing to the record after service | What to write and never write; profile or visit note; the tag list; at close, never at the table; FR and BW pass observations; kitchen notes through the chef | Writers; FR, BW passing half | R | 1.5; 0.5 |
| SYS-113 | SevenRooms for the host: arrivals, seating and the waitlist | Service screens by function; arrival statuses; seating; statuses through the meal; walk-ins to profiles; honest waitlist quotes; downtime on paper | H, LH, MD | R | 6 |
| SYS-114 | SevenRooms for the host: the phone, messages and payments in the book | Booking at pace by phone; two-way messages in the house register; payment links, never a card number; refunds within permission; consent | H, LH | R | 3 |
| SYS-115 | SevenRooms for the lead host: how the book is built | Shifts, access rules, pacing (the shift sets the ceiling, an access rule can only lower it), durations, combinations, blocks; why the screen says no; day-of changes versus configuration; sections; rebuilding the night | LH (gate for H); MD | O/R | 10 |
| SYS-116 | SevenRooms for the lead host: setting the book before service | The pre-service walk; flags and tags; confirmations; the pre-service view and the door's part of pre-shift; allergies and occasions to the kitchen; a premortem | LH | O/R | 6 |
| SYS-117 | SevenRooms for the lead host: keeping the record accurate | Merging duplicates, tag discipline, auditing and coaching notes, closing out the night, data requests to the MD | LH | O/R | 4 |
| SYS-118 | SevenRooms for the lead host: teaching and signing off the basics | Running the SYS-110 practical and SYS-113 drills; anchors; agreeing with a second rater; the lead host's mastery proof for the track | LH | O | 3 |
| SYS-119 | SevenRooms for managers: configuring the book | Floor plan, availability, policies, messages, channels, user accounts and offboarding, integrations, change control, who owns which setting | MD, OM | pre-opening R; else O | 8 |
| SYS-120 | SevenRooms for managers: customer data, tags and permissions | The tag list, auto-tags, the permission matrix, exports, consent and opt-out, data requests, the founder data policies in the system | MD, OM | pre-opening R; else O | 4 |
| SYS-121 | SevenRooms for managers: reading the book as the business | Reports read for one decision; recognition (the customer recognition rate defined as in ORI-023), returning customers, no-shows; figures pulled, never typed; the book as forecast | MD, OM; LH joins | O weekly | 5 |
| SYS-122 | Building your regulars and your product feedback from the book | Finding your returning customers; preparing for them; feeding the house record (`founder.regulars_policy`); what customers choose as evidence for feedback (D54, D60); feeds SVC-101 | FS, BT, BA, LS, LB, HB, LFR | O | 4 |
| SYS-130 | Point of sale for your position | Seat and course entry, modifiers the kitchen can make, the allergy flag every time, firing, transfers, splits, payments, voids and comps within authority; counter tabs and close-out (Toast, candidate) | H 1, FR 1.5, BW +0.5, FS +4, BB 1, BA 4, BT 6 | R | as listed |
| SYS-131 | Point of sale: manager functions and the day's reports | Approving voids and comps in range, 86 and menu updates, permissions, end-of-day reports, tip reports to payroll | MD, OM; closing leads | R | 2 |
| SYS-132 | Kitchen order display and ticket flow | Course, seat, modifications, allergy flags; bump, recall, refire; screen down | Cooks, the pass | R | 2 |
| SYS-133 | Payroll and HR: managers' approvals, onboarding and offboarding | Timecards with reasons, onboarding records, changes on Brandon's approval, offboarding access the same day | MD, OM, KO; KS and CDC the timecard-approval part only if named in `people.timecard_approvers` | R | 3; 1 |
| SYS-134 | Scheduling: building and approving the schedule | The tool steps only: a week from the book's forecast, training and ongoing-education hours placed, swaps without overtime, posting rules; the practical is ADM-104's | Schedule owner R; others O | R/O | 1 |
| SYS-135 | Recruiting system | Posting, self-scheduling, scorecards, every decision sent including the no (Greenhouse, candidate) | MD, OM; leads as interviewers | O | 3 |
| SYS-136 | Inventory, purchasing and ordering in the tool | Counts, transfers, waste and receiving entries; orders and invoices; variance reports (Restaurant365, candidate) | OM, HB, LB, KO, CDC, `people.ordering_roles` (2); cooks' count part | R | 3; 2; 1 |
| SYS-137 | Accounting: invoices, coding and the period close | Coding, the close checklist, reconciling POS, payroll and bank (Restaurant365, QuickBooks, candidates) | OM, office | O | 4 |
| SYS-138 | Sales tax filing | Tax collected is held in trust; reconciling the set-aside to the POS tax report (Davo, candidate) | OM | O | 1.5 |
| SYS-139 | Food safety logging and temperature monitoring | Taking and logging a reading, corrective action, sensor alarms and who responds (FoodDocs, ConnectedFresh, candidates); no test-out | K, managers (alarms), bar (refrigeration) | R | 1 to 2 |
| SYS-140 | Food waste tracking | Every discard by weight and category; chefs read the report (Winnow, candidate) | K | R | 1 |
| SYS-141 | Prep and recipe management | Working from the generated prep list and the recipe as written; chefs maintain (PrepWizard, candidate) | C, CDP, CT; KO, CDC, EC maintain | R | 2 |
| SYS-142 | Maintenance and repair requests | A request someone can act on; urgency; after-hours contacts (ResQ, candidate) | Leads, MD, OM; everyone reports through SYS-101 | R | 1 |
| SYS-143 | Tasks and projects | One owner and a date; decisions in the task; sources stay in Box (ClickUp) | MD, OM, HB, CDC, project-owning leads | O | 1.5 |
| SYS-144 | Training video production | Script from the module source, scene direction through the Design Translating Team, re-render on change (Synthesia); parked with LEA-004 until Brandon opens authoring | Authors | parked | 3 |
| SYS-145 | The loyalty layer | Identified, parked on the tool choice (the white paper names a loyalty layer beside SevenRooms; lead-only as a choice): recognizing a member on the floor, reading it as a manager | Floor; managers | parked | |

### 5.9 Compliance (writer 1)

Provider content or HR-written rules, linked and tracked in Trainual with certificates uploaded; never rewritten (D17, D27, D57).

| ID | Title | What it covers | Positions | R/O | Hours |
|---|---|---|---|---|---|
| CMP-101 | Food handler certificate (Texas) | The accredited provider's course; legal window 60 days, valid two years (verified-secondary); test-out by a current certificate | All food employees (`people.food_handler_scope`); recommended for All | R per `founder.compliance_timing` | 2 |
| CMP-102 | Alcohol seller-server certification (TABC) and the house policy | The approved provider's course; Safe Harbor within 30 days and a written house policy (verified-secondary; confirm at TABC); policy acknowledgement always required | Anyone who sells, serves or delivers alcohol and their managers; recommended for all CF | R per `founder.compliance_timing` | 2.5 |
| CMP-103 | Harassment prevention | Provider course plus the house policy and a reporting route that bypasses the scheduler; supervisor version; renewal | All; supervisor version for leads, managers, HB, kitchen leaders | R | 1; 2 |
| CMP-104 | Workplace safety and hazard communication | Provider course; safety data sheets; injury reporting (`workflow.injury_report`) | All | R | 1.25 |
| CMP-105 | Wage and hour basics | The HR-written rules and the acknowledgement: all time recorded, no work off the clock (training included; 29 CFR 785.27 to 785.29 cited here), no overtime, breaks, final pay. The pay stub is SYS-103 and the missed punch is SYS-104 | All | R | 0.5 |
| CMP-106 | Handbook and policy acknowledgements | E-signatures on each policy as it exists (D50) | All | R | 0.5 |
| CMP-107 | First aid and CPR | Provider course with the hands-on session; once `founder.first_aid_coverage` names the designees, `fact.cert_hours.cmp107` is added to their windows | `people.first_aid_designees`; open to others | R/O | `fact.cert_hours.cmp107` |
| CMP-108 | Manager certifications | Certified food protection manager; manager-level alcohol credentials. A hiring requirement, or a dated post-hire deadline (`policy.cfpm_deadline`) with `workflow.cfpm_coverage` keeping a certified person on every hour | MD, OM, HB, KO, KS, CDC, EC; LB if delegated | hiring requirement | `fact.cert_hours` |
| CMP-109 | The compliance calendar and inspections | Permits, renewals, certificates per person, postings, walking an inspector through the records | OM R; MD O | R/O | 2.5 |
| CMP-110 | Food safety on the line: the code requirements | The code items only: hand washing, gloves, time and temperature, cooling, reheating, date marks (`fact.food_code.*`). The chef's own controls are KIT-013 | K (porter version) | R | 3; 1.5 (to recheck) |
| CMP-111 | Chemicals, equipment and body safety in the kitchen | Chemical use and mixing, protective equipment, equipment hazards | K | R | 2 |
| CMP-112 | Cryogenic and pressure equipment (supplier certification) | The supplier's certification, linked and tracked; the house procedure kept as its SAF-003 part (where it is stored and filled, who may handle it, what never happens near a customer); passes every attempt | HB and any preparer | R | `fact.cert_hours.saf003` plus 0.5 |
| CMP-113 | Reporting illness and exclusion | HR-written from the adopted food code: the symptoms and diagnoses that exclude or restrict, when a person may return, the duty to report before a shift (`workflow.illness_report`), pay under `people.sick_policy` | All | R | 0.5 |

### 5.10 Parked, dropped, and not modules, with reason

**Parked (written or identified, waiting on a named decision):**
- SYS-003 (practicing with an AI partner) and LEA-043 (coaching with a co-pilot): until the AI practice policy exists.
- LEA-048 (choreographing the house's movement): until the space exists (D58).
- SVC-070: until late night runs and the layout exists. SVC-075: on the chef's expo decision. KIT-103: until two dayparts run.
- SAF-010: until Brandon decides the allergen steward role exists. BEV-118: until `people.tea_program_owner` exists. ORI-005: until its sources are verified.
- LEA-004 and SYS-144: until Brandon opens authoring (D1). LEA-036: until the D14 panel exists.
- ADM-118 (events and private bookings, the single events ID with office, host and floor parts): on Brandon's events answer. SYS-145 (the loyalty layer): on the tool choice.
- SVC-023 (team set-down): on the D48 convention.

**Not modules (mechanisms, policies, people steps and open questions; they leave the module count):**
- CUL-023 (the standing recheck): a mechanism. What a recheck is sits in ORI-015; the cadence is `workflow.recheck_cadence`, run through LEA-101 and LEA-102.
- CUL-024 (the annual recommitment): a people step, `workflow.recommitment`, run by the MD under LEA-006.
- LIB-012 (study placement): a policy, `policy.study_placement`, referenced from ORI-015; the never-reconstruct rule and the presentation format become a short LEA part if Brandon adopts placements. LIB-008 and LIB-009 go with it.
- BEV-034 (one program, two bars): an open question (section 7), specified only if Sŏn runs two bars.
- MNU-007 (going further with the cuisine): an interest, raised through ORI-015 and met by KIT-060 and MNU-003.
- SVC-080 (memory as a craft): folded into SVC-019's ongoing part. SVC-041 (the room's senses): folded into SVC-018's BW ongoing part. BEV-031 (R&D apart from service): folded into BEV-030. LEA-047: merged into LEA-007. SVC-102: folded into ADM-118.

**Dropped:**
- The reading tracks LIB-001 to LIB-007, LIB-010, LIB-011 are dropped as modules; their sources become reading lists attached to the module they serve (section 8). LIB-008 and LIB-009 go with the study-placement policy that replaced LIB-012 (5.10).
- ORI-026 dropped as a module; its method sits in ORI-016's self-review. CUL-021 dropped: a format, not content. CUL-016 and CUL-026 fold into CUL-001 and LEA-005 (D44).

---

## 6. Which writer covers which area

| Writer | Areas | Modules | Shared parts they write for others, or take from others |
|---|---|---|---|
| 1 | The house, compliance, systems and technology | 5.1, 5.8, 5.9 | Writes SAF-001 (with host, table and bar parts drafted from writers 2 and 3's input), SAF-009 part 1 (part 2's bar cases from writer 3), SYS-130 (position parts from writers 2 and 3), SYS-139 and SYS-140 with the chef. Takes the kitchen versions of SYS-111 and SYS-112 from writer 4 |
| 2 | Service, food and menu | 5.2, 5.3 | Owns SVC-071 (writer 3 writes the bar part), SVC-033 (writer 3 writes the drink part and keeps it consistent with BEV-113), SVC-008 (bar part from writer 3), the floor side of KIT-002 (with writer 4), MNU-001 (counter depth with writer 3), MNU-101 (track examples from writer 3) |
| 3 | Beverage, all tracks | 5.4 | Owns BEV-002 (writer 2 writes the floor part), BEV-016 (service-well part for writer 2's SVC-013), BEV-102 (floor depths checked by writer 2), the wine track's language rules shared with SVC-008 |
| 4 | Leadership and teaching, administration, culinary (draft) | 5.5, 5.6, 5.7 | Owns KIT-002 and KIT-003's chef content, LEA-002's kitchen part, LEA-033's kitchen variant; writes ADM-105's bar part with writer 3 |

Rules for all four: one module, one owner; a shared part is written by the writer who knows the work and reviewed by the owner; no writer duplicates a part another module holds. Every module is written in the module format in the task brief and in the library voice.

---

## 7. Open for Brandon (consolidated, in the order they unblock the most)

1. **Service length and the two-week claim.** Counting supervised services at shift length (`workflow.shift_length.<position>`, about 6 h) moves the green runner, host and barback windows to about 2.2 weeks even with the certificate lever. Report them as 2.2 weeks, or cut about 9 h from readiness; the honest options are in 2.2 and 2.3.
2. **Certificate timing** (`founder.compliance_timing`): before solo, or inside the legal windows? This one decision moves FR, H and BB by 4.5 h each.
3. **Ongoing education hours** (`policy.ongoing_education_hours.<position>`): how many paid hours a week per position. Without it the wine gates cannot be met with no overtime; at 4 hours a week a back waiter reaches front server in about 27 weeks (section 3).
4. **Managers:** does D55 apply to the MD and OM? Counted honestly they run about 120 to 140 h. If it does, make wine level 3 (MD) and CMP-108 (every named role) hiring requirements and set a pre-opening window for configuration and recruiting; if not, set a four-week manager onboarding standard. Also: who owns the schedule, approves swaps and closes the day (`people.*`).
5. **Prove-first rule:** adopt it program-wide in ORI-015. Safety elements still never test out.
6. **Hiring routes:** everyone enters service as a runner (close the green external back waiter route); no green external bartenders; external front servers only with prove-first, or not at all (D55 accepts this); barback-first as the default barista route; the barista as a separate hire or the bartender on the morning register; whether baristas serve alcohol.
7. **Opening:** the pre-opening calendar (`workflow.preopening_calendar`: managers at least four weeks before line staff, the HB at least two weeks before bar staff) and the assessor capacity per cohort (`workflow.live_gate_limit`), since every opening front server is external.
8. **Remote hours:** accept about 17 remote hours for everyone and 22 to 31 for customer-facing positions, against the 8 floated at intake, with the 3-hour daily cap?
9. **Head of beverage:** wine above Sommelier 1 level and CMP-108 as hiring requirements.
10. **Gates:** confirm the hard gates (BEV-110; BEV-111 with BEV-015; BEV-112; BEV-113; SYS-115 to SYS-117; BEV-105, BEV-012, BEV-005, BEV-008, BEV-001, FLV-002; BEV-035 part one for LB) and set `policy.soft_gate_window`.
11. **Outside courses (D27):** may the studio ask CMS, WSET, SCA providers, Barista Hustle, Cicerone, WTA and UKTA about delivery and tracking inside Trainual? Does Sŏn fund outside exams (`policy.outside_certification_funding`, `policy.wine_cert_sponsorship`)? Does vendor onboarding for SevenRooms count as an outside course?
12. **Policies that gate modules (D50):** mistreatment, responsible service, customer data and door data, protocol criteria and holds, regulars, harassment and reporting, emergency plan, incident note, after-hours contact, comp and gifted-pour ranges, vendor gifts, public replies, events, study placement, the recommitment format, tasting on paid time and the non-drinking route.
13. **SevenRooms:** which bookings any position may make alone; who owns configuration; spend visibility; whether the card-number item never tests out; which messages and channels Sŏn uses; whether follow-up emails (D61) send through its messaging; at onboarding, a training environment, permission level names and whether every employee needs a paid seat (`fact.*`).
14. **The bar and the coffee:** is beer on the list, and are Korean drinks; who pulls the batch espresso (`people.espresso_puller`) and is there milk-texturing equipment on the front bar (BEV-004); does a coffee owner role exist, and a separate tea owner; does Sŏn run two bars; do food runners carry drinks from the service well (`workflow.runners_carry_drinks`); should SYS-110 and SYS-111 move to the first month for kitchen and barback positions (saves about 3 h).
15. **Program questions:** HR's ruling on hourly leads rating practicals (D5); whether unsupervised shifts after sign-off sit outside the window (assumed here); whether the allergen steward role exists; the term "angel shift" (`founder.term.angel_shift`); the four unblock outcomes as drafted in LEA-006; the master server bar as drafted in SVC-074; the working definitions of employee NPS, the cultural labor score and the customer recognition rate.
16. **Interviews (D45) the spine waits on:** the why story; the decision order; the allergy route; first-minute emergency roles; the tipping answer; the glossary; how he reads a table, times a check-back, chooses a recovery and makes a pacing call; composing the room; the MD's step-in cues; how he reads a team's load; what performing looks like at a table; what "Sommelier 1 level" means to him in practice; how Sŏn recommends; the coffee method and the water-pitcher drill story; what the pair must never hand to software; which numbers the pair act on without asking; teaching a new cook, a correction that worked and one that did not, what he will not carry; the EC split.
17. **For the chef (draft kitchen):** titles (INT C17); prep and line as two strands or one path; who expos; stations and their hours, the paired-shift length and the named non-peak service for cook release; the call lexicon; refire rules; tasting calibration; allergen controls; the kitchen's own food-safety controls (KIT-013); the kitchen's part in pre-shift; kitchen visits; batch espresso in the back and who pulls it (with the HB); event menus; KIT-040, KIT-042 and KIT-043 to define; every kitchen hour in 2.4.

---

## 8. Crosswalk: where every discovery and draft ID went

**Kept as the same ID:** ORI-001, ORI-003, ORI-005, ORI-006, ORI-008, ORI-009, ORI-015, ORI-016, ORI-020, ORI-021, ORI-023, ORI-033; CUL-001, CUL-002, CUL-003, CUL-004, CUL-010, CUL-011, CUL-013; SAF-001, SAF-004, SAF-006, SAF-007, SAF-009, SAF-010, SAF-011, SAF-013; every SVC listed in 5.2; MNU-001 to MNU-004; BEV-001 to BEV-006, BEV-008, BEV-012, BEV-014 to BEV-028, BEV-030, BEV-032, BEV-033, BEV-035 to BEV-037, BEV-040, BEV-042; FLV-002, FLV-005; KIT and LEA IDs listed in 5.5 to 5.7; SYS-002.

**Changed after the 2026-10-01 red teams:** SAF-003 → CMP-112 (the house procedure kept as its SAF-003 part). SAF-011's illness content → CMP-113. CUL-023 → `workflow.recheck_cadence` (what a recheck is → ORI-015; CUL-019, CUL-020 → ORI-015). CUL-024 → `workflow.recommitment` under LEA-006. LIB-012 → `policy.study_placement` (LIB-008, LIB-009 with it). MNU-007 → ORI-015, KIT-060, MNU-003. SVC-080 → SVC-019. SVC-041 → SVC-018. BEV-031 → BEV-030. BEV-034 → an open question. LEA-047 → LEA-007. SVC-102 → ADM-118. New: SVC-101 (D61), SVC-103, BEV-119, BEV-120, LEA-106, ADM-118, CMP-112, CMP-113, SYS-145 (parked).

**Folded into another module:**
- ORI-002 → SYS-002 (tool) and ORI-015 (progression). ORI-004, ORI-011, ORI-012, ORI-014, CUL-005 → ORI-003. ORI-007 → ORI-008 and MNU-004. ORI-010 → ORI-021. ORI-013 → LEA-045. ORI-017, ORI-034, SVC-001 → ORI-015. ORI-019 → ORI-006. ORI-022 → ORI-001 and ORI-023. ORI-028, ORI-032 → ORI-016. ORI-029, ORI-030, ORI-025 → ORI-001. ORI-031 → LEA-023. ORI-035 → SVC-007.
- CUL-006, CUL-007, CUL-008, CUL-009, CUL-012 → CUL-002. CUL-014 → LEA-024. CUL-015 → CUL-013. CUL-016, CUL-026, LEA-019's pre-shift frame → CUL-001 and LEA-005. CUL-017 → KIT-060, KIT-061. CUL-018 → CUL-002 and LEA-021. CUL-019, CUL-020 → ORI-015 (what a recheck is). CUL-022 → SVC-047. CUL-025, KIT-001 → ORI-021. CUL-027 → LEA-045.
- SAF-002 → CMP-101 to CMP-108 and ADM-108. SAF-005 → SAF-006 and ADM-110. SAF-008 → SAF-001. SAF-012 → CMP-111.
- SVC-005 → SVC-027 and SVC-006. SVC-014, SVC-022 → KIT-002 and SVC-013. SVC-016 → SYS-111 and SVC-010. SVC-021, SVC-076, SVC-077 → SVC-008. SVC-024, SVC-082 → SVC-006. SVC-026 → BEV-002. SVC-039 → SVC-047. SVC-040 → SYS-122 (and SYS-117 for the record). SVC-042 → SVC-070. SVC-043 → ORI-020. SVC-048 → SVC-002. SVC-050 → MNU-101. SVC-051 → SVC-072. SVC-053 → SVC-004. SVC-054 → SYS-113. SVC-058, SVC-061 → SYS-116. SVC-081 → SVC-063. SVC-084 → SVC-003, SVC-004. SVC-085 → SVC-028. SVC-062 tool side → SYS-114; written replies → ADM-114. SVC-059, SVC-011 tool sides → SYS-113. SVC-057, SVC-068 tool sides → SYS-115. LEA-031 → SVC-009.
- MNU-005 → MNU-004. MNU-006 → MNU-001.
- BEV-009 → SVC-007. BEV-010 → BEV-110 to BEV-114. BEV-013 → BEV-012. BEV-029 → BEV-019. BEV-038, BEV-039 → BEV-116. BEV-035 beer part → BEV-116; sool part → BEV-028; readiness part → BEV-105. FLV-001 → BEV-008. FLV-003, LIB-004 → ORI-005. FLV-004 → BEV-022. FLV-006 → BEV-019 (bar), KIT-045 (kitchen), MNU-101 (reporting).
- KIT-004 → MNU-001 and KIT-045. KIT-011, KIT-014 → KIT-013. KIT-025 → KIT-102. KIT-032, KIT-050 → LEA-105. KIT-044 → LEA-104. KIT-051 → LEA-002. KIT-052 → LEA-033. KIT-015 floor and bar half → ADM-105; tool half → SYS-136. KIT-020 tool side → SYS-141. KIT-041 tool half → SYS-136, SYS-141.
- LEA-008, LEA-049 → LEA-037. LEA-009 → ADM-117. LEA-012, LEA-020 → LEA-001. LEA-013 → LEA-002. LEA-028 office half → ADM-101. LEA-030 → LEA-029. LEA-038, LEA-042 → LEA-004. LEA-040 manager part → LEA-102; owner part held by Brandon (D1). LEA-041 tool side → SYS-120.
- LIB-001 → CUL-003. LIB-002 → LEA-029. LIB-003 → LEA-015. LIB-005 → SVC-078. LIB-006 → BEV-001. LIB-007 → SVC-012. LIB-010 → SVC-059. LIB-011 → SVC-010. LIB-008, LIB-009 → `policy.study_placement` (with LIB-012).
- SYS-001 → SYS-101.

**Draft IDs renumbered in this spine (2026-10-01 drafts):**
- Everyone draft: SYS-101 (Trainual) → SYS-002; SYS-102 → SYS-103; SYS-103 → SYS-104; SYS-104 → SYS-105; SYS-105 → SYS-110 to SYS-112; SYS-106 → SYS-130; CMP-101 → CMP-101; CMP-103 → CMP-102; CMP-104 → CMP-103; CMP-105 → CMP-104; CMP-106 → CMP-105; CMP-107 → CMP-106; CMP-108 → CMP-107; "SAF-001 (table practice)" → SAF-001 part 2; "SAF-009 (floor version)" → SAF-009 part 1.
- Managers draft: SYS-101 → SYS-101; ORI-002 → SYS-002; SYS-130 → SYS-103; SYS-131 → SYS-104; SYS-150 → SYS-105; SYS-110 to SYS-114 → SYS-110 to SYS-120 (SevenRooms draft numbering used); SYS-120 → SYS-130; SYS-121 → SYS-131; SYS-160 → SYS-135; SYS-170 → SYS-136, SYS-137, SYS-138; SYS-180 → SYS-139 to SYS-141; SYS-190 → SYS-143, SYS-144; CMP-101 → CMP-109; CMP-102 → CMP-108.
- SevenRooms and systems draft: SYS-101 to SYS-103 → SYS-110 to SYS-112; SYS-104, SYS-105 → SYS-113, SYS-114; SYS-106 to SYS-109 → SYS-115 to SYS-118; SYS-110 to SYS-112 → SYS-119 to SYS-121; SYS-113 → SYS-122; SYS-120, SYS-121 → SYS-130, SYS-131; SYS-122 → SYS-103; SYS-123 → SYS-133; SYS-124 → SYS-104; SYS-125 → SYS-134; SYS-126 → SYS-105; SYS-127 → SYS-135; SYS-128 to SYS-130 → SYS-136 (variance content to ADM-105); SYS-131 → SYS-137; SYS-132 → SYS-139; SYS-133 → SYS-140; SYS-134 → SYS-141; SYS-135 → SYS-142; SYS-136 → SYS-138; SYS-137 → SYS-143; SYS-138 → SYS-144.
- Kitchen draft: SYS-171 → SYS-132; SYS-172 → SYS-136; SYS-173 → SYS-139; SYS-174 → SYS-110 to SYS-112 kitchen versions; SYS-175 → SYS-104 and SYS-134; SYS-176 → SYS-141; CMP-171 → CMP-111; CMP-172 → CMP-110; LEA-171 → LEA-104; LEA-172 → LEA-105; LEA-173 → LEA-002 kitchen part; LEA-174 → LEA-033 kitchen variant.
- Beverage team draft: BEV-101 (current drink list) → BEV-102; BEV-102 (opening and closing) → BEV-101; BEV-104 (glass) → SVC-071 bar part; BEV-105 (tea and matcha) → BEV-104; BEV-106 (beer) → BEV-116; BEV-107 (spirits) → BEV-105; BEV-108 (wine at the bar) → BEV-102 bartender depth and BEV-015 bar part; BEV-109 (coffee program) → BEV-103; BEV-110 (product feedback) → MNU-101; SYS-101, SYS-102 → SYS-130; CMP-101 → CMP-102; CMP-102 → CMP-108.
- Wine research: BEV-101 → BEV-110; BEV-102 → BEV-111; BEV-103 → BEV-112; BEV-104 → BEV-113; BEV-105 → MNU-101; BEV-106 → BEV-114.
- Other-tracks research: BEV-101 → BEV-102; BEV-104 → BEV-103, BEV-104, BEV-006; BEV-105 → BEV-117; BEV-106 → BEV-118; BEV-107 → BEV-105; BEV-108 → BEV-116; MNU-101 → SVC-033; MNU-102 → MNU-101.

---

## 9. Outside sources and their marks

| Claim | Source | Mark |
|---|---|---|
| Generic job floors for waiters, attendants and barbacks, hosts, supervisors, food service managers, bartenders, baristas | O*NET 35-3031.00, 35-9011.00, 35-9031.00, 35-1012.00, 11-9051.00, 35-3011.00, 35-3023.01 | verified-primary (35-3023.01 read through a summary) |
| CMS Introductory: two days in person or online up to 180 days; curriculum; 70 multiple-choice questions, theory only; no renewal | mastersommeliers.org | verified-primary; pass mark and fees are `fact.*` |
| CMS Certified examines tasting, theory and a hospitality and service practical | mastersommeliers.org | verified-primary |
| WSET Level 2 and Level 3 Wines: hours and exam formats | wsetglobal.com | verified-primary |
| Certification raised knowledge, not wine sales; trainees named missing selling practice | Orlowski 2022, International Hospitality Review | verified-primary |
| CMS members rate belonging lowest | CMS Americas 2022 survey summary | verified-primary (self-report) |
| Expert and novice wine language differ | Croijmans and Majid 2016; Food Quality and Preference 2021 | verified-secondary |
| SCA Coffee Skills structure, hours and exam types | SCA catalog and course pages | verified-primary (points detail verified-secondary) |
| Barista Hustle tiers; no SCORM route found | baristahustle.com, `research/phase2-working/10-barista-hustle.md` | verified-primary; Trainual fit unverified |
| WSET Spirits levels and exams | wsetglobal.com, Level 3 specification | verified-primary |
| Cicerone Certified Beer Server format and syllabus | cicerone.org | verified-primary |
| WTA Certified Tea Specialist; UKTA Tea Sommelier Award | providers' pages | verified-primary |
| USBG Spirits Professional and Advanced Bartender | usbg.org | verified-primary |
| Texas food handler: within 60 days, valid two years | provider and guide sites citing TFER and HSC | verified-secondary; confirm at DSHS |
| TABC Safe Harbor: certification within 30 days, immediate managers, written policy | TABC FAQs; secondary sources | verified-secondary; confirm at tabc.texas.gov |
| Certified food protection manager present during all hours | 25 TAC 228.31 | verified-secondary |
| Payroll records three years, time cards and schedules two years | 29 CFR 516.5, 516.6 | verified-secondary |
| I-9 Section 2 within three business days | USCIS | verified-secondary |
| OSHA severe-injury reporting; partial exemption from logs | 29 CFR 1904 | verified-secondary; windows lead-only and bound |
| Learning time is paid working time | 29 CFR 785.27 to 785.29 | verified-primary |
| Structured interviews predict best | Sackett 2022 | verified-secondary |
| SevenRooms: vendor training tracks, unique logins, settings, consent on the client, pre-service view, waitlist and payment-link features | sevenrooms.com public pages and terms | verified-primary (help guide dated 2020) |
| Shift pacing ceiling; access rules can only lower it | Peoplevine help article | verified-secondary |
| Toast to SevenRooms integration is one-way | Toast Support | verified-secondary; reopen before drafting |
| A SevenRooms training environment; permission level names | not found | unverified; ask at onboarding |
| SevenRooms is common at top restaurants | search results | lead-only; not used as a claim |
| Every tool candidate in 5.8 | archived SaaS catalog via D60 | lead-only |
| Major allergen list including sesame | FASTER Act | lead-only; confirm at FDA |
| Korean drink and Korean tea sources | none verified | unverified; founder-sourced |
