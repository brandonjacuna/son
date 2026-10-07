# St. Elmo Dashboard V2, field classification and exhibit design

Prepared 22 August 2026. Read-only pass against the frozen base. Nothing was written.

Companion files: `St_Elmo_Classification_Appendix_2026-08-22_part1.md` and
`St_Elmo_Classification_Appendix_2026-08-22_part2.md` carry the field-by-field table.

This document stands alone. A reader who was not present can work from it without
opening the base.

---

## 1. What this feeds

An Excel workbook for investors: a financial exhibit package plus an interactive
scenario instrument. Fully gated, released only after a live meeting. It shows the
business, not the deal. No returns, no waterfall, no IRR.

Build constraints: Excel-native, no macros, Excel 2016 formula floor, INDEX/MATCH
rather than XLOOKUP. Brand hex carries identity inside the workbook. Typography lives
in the PDF export.

---

## 2. Scope and skip count

The base carries 46 tables and 853 fields. Retired material was excluded before any
classification took place.

### Fields skipped

| Category | Count |
| --- | --- |
| Fields prefixed `DELETE` | 56 |
| Fields prefixed `LEGACY` | 24, across 11 tables |
| **Total fields skipped** | **80** |

The `LEGACY` count matched the brief exactly, 24 across 11 tables: P&L Model 6,
Scenario Configurator 3, Revenue Build Up 3, Reference: Service Schedule 2,
Reference: Labor Models 1, Reference: Staffing Model 1, Restaurant Configurator 2,
Seasonal Factors 1, Scenario Timeline 1, Cash Flow 3, CapEx: FF&E 1.

### Records skipped

| Category | Count |
| --- | --- |
| Y1 Monthly Projections, orphans of the two retired scenarios | 24 |
| Years 1-5 Projections, orphans of the two retired scenarios | 10 |
| Scenario Timeline, `our-plan-no-lunch-m1` through `m12` | 12 |
| Scenario Timeline, `DELETE` prefixed `aggressive-m1` through `m12` | 12 |
| Scenario Configurator, two `DELETE` prefixed retired scenarios | 2 |
| P&L Model, five `DELETE` prefixed retired operating models | 5 |
| Lean Sources and Uses, one `DELETE` prefixed row | 1 |
| **Total records skipped** | **66** |

The 34 projection orphans and the 24 Scenario Timeline rows match the brief exactly.
The remaining 8 fall under the general rule that anything named `DELETE` is skipped.

### One scope correction

The brief said to keep the 12 `conservative-m` Scenario Timeline rows because they are
shared by Our Plan and Best Case. That is correct as far as it goes, but Scenario
Timeline holds **48 rows, not 36**. There are also 12 `downside-m` rows, created
20 August 2026, and they are live. They carry the Downside ramp curve, which runs
52% in month 1 to 100% in month 12 against the conservative curve's 58% to 100%.

The skip count is unaffected and still 24. The keep set is 24, not 12. If the Downside
column is going to appear in the scenario comparison, those rows are load-bearing.

### Live set

**773 live fields** across 46 tables.

---

## 3. Classification counts

| Class | Count | Share |
| --- | --- | --- |
| SHIPS AS-IS | 144 | 18.6% |
| SHIPS DERIVED | 347 | 44.9% |
| INTERNAL ONLY | 282 | 36.5% |

38 rows are flagged low-confidence. Each is written up in section 6.

### What drove the INTERNAL ONLY calls

The non-negotiable categories accounted for most of it.

**Debt, SBA and financing structure.** The `Funding Source` fields in Lean Sources and
Uses and CapEx: Pre-Opening Expenses carry values including "Debt / Vendor / Equity".
The whole Funding Treatment Schedule table maps uses to financing treatment and has a
field named `Equity Funded/SBA7a`. The Lean Sources and Uses `Notes` field carries the
superseded SBA structure in narrative form.

**Daypart code names.** These appear in three places only: the Lunch Model record named
"Dosi QSR", several Model Assumptions records, and one Model Index presentation note.
Worth stating plainly, because it is good news: the Restaurant Configurator daypart
records are already neutral. They read "i. Early Morning", "ii. Lunch", "iii. Brunch",
"iv: Dinner", "v. Late Night". The revenue spine carries no code names at all.

**The culinary seat.** Three fields frame it as open. Labor: Positions carries
`Hiring Phase` and `Hire Week`. The Pre-Opening Six-Month Use Schedule carries
`Sous Chef Salary` as the only pre-opening kitchen hire. Separately, Model Assumptions
books founder compensation as three seats at $100,000 each. Two founders are seated.
Nothing in the base says the third is open, but the arithmetic invites the question.

**Redcar and lease strategy.** Six tables are wholly internal on this basis: Redcar
Property Research, Lease Term Risk Summary, Lease Delivery Matrix, Landlord Direct Work
Requests, Lease Signing Cash Scenarios, and Lease: Rent Basis Sensitivity. Beyond those,
many Model Assumptions `Source` values read "Son tenant proposal to Redcar" and must be
restated before any assumption register ships.

**Unannounced vendors.** The P&L Model has a field naming the automation vendor.
CapEx: Leasehold Improvements has `Contractor / Vendor`. Several CapEx tables carry
`Reference Link` and `Source URL` pointing at suppliers.

**Raw Airtable identifiers.** The entire Hardcoded Input Inventory table, 21 fields, is
an audit register of table IDs, field IDs and record counts.

**One addition beyond the brief.** The service charge pool and points mechanics
(`Service Charge Pool`, `Point Value`, `Total Service Points` on Reference: Service
Schedule, and the point fields on Reference: Staffing Model and Labor: Positions) are
the no-tipping compensation model. That model is designed but not finalised and legal
review is pending counsel. It should not appear on an investor surface in any form
until counsel has cleared it. Classified INTERNAL ONLY.

---

## 4. Exhibit-candidate set

Organised by what an investor has to see. Not everything that could ship.

### 4.1 Revenue build and its drivers

**Status: strong. This is the best-built part of the base.**

The spine reconciles exactly, with no plug, from the individual service to the annual
figure. Confirmed by recomputation:

- 22 day-and-daypart service rows sum to **5,702.5 covers** in a mature week. That is
  the same number the break-even table carries as `Mature Weekly Covers`.
- The same rows sum to **$150,900.50** of mature weekly revenue, which is the
  P&L Model `Total Revenue` to the cent.
- Daypart revenue rolls to the same total: Early Morning $16,515, Lunch $25,000,
  Brunch $22,944.50, Dinner $78,932, Late Night $7,509.

Mature week by daypart:

| Daypart | Covers | Blended PPA | Revenue | Share of revenue |
| --- | --- | --- | --- | --- |
| i. Early Morning | 1,566 | $10.55 | $16,515 | 10.9% |
| ii. Lunch | 1,562.5 | $16.00 | $25,000 | 16.6% |
| iii. Brunch | 675 | $33.99 | $22,944.50 | 15.2% |
| iv: Dinner | 1,500 | $52.62 | $78,932 | 52.3% |
| v. Late Night | 399 | $18.82 | $7,509 | 5.0% |
| **Total** | **5,702.5** | **$26.46** | **$150,900.50** | **100%** |

Operating days: Early Morning 7, Lunch 5 (Monday to Friday), Brunch 2 (Saturday and
Sunday), Dinner 5 (Wednesday to Sunday), Late Night 3 (Friday to Sunday).

Two things to carry forward. Dinner is 26.3% of covers and 52.3% of revenue, which is
the concentration every scenario lever has to respect. And the multi-daypart argument
is visible in this table without being asserted: four dayparts outside dinner produce
47.7% of revenue from one kitchen and one lease.

### 4.2 Unit economics, the three-line bridge

**Status: strong. Foots exactly.**

Our Plan, Year 1, recomputed from the live figures:

| Line | Amount | % of revenue |
| --- | --- | --- |
| Revenue | $6,588,777.97 | 100.00% |
| Cost of sales | ($1,746,026.16) | 26.50% |
| Labor, rebased | ($2,164,338.00) | 32.85% |
| Operating expense | ($1,164,065.76) | 17.67% |
| Occupancy | ($416,221.12) | 6.32% |
| **Restaurant-Level EBITDA** | **$1,098,126.93** | **16.67%** |
| Corporate G&A | ($326,910.00) | 4.96% |
| **Company EBITDA** | **$771,216.93** | **11.71%** |

The mature weekly view sits alongside it: Restaurant-Level EBITDA $31,696.53 (21.00%),
Corporate G&A $6,521.10, Company EBITDA $25,175.43. Restaurant labor 29.57% and prime
cost 56.07% on the mature week.

Terminology is clean and consistent across P&L Model, Years 1-5 Projections and
Scenario Configurator. The retired Four-Wall and Fully Loaded language survives only on
`DELETE` and `LEGACY` fields, which are out of scope.

The two views are not interchangeable, and the workbook must say so. Year 1 is a
twelve-month ramp. The weekly row is a stabilised build. The 16.67% and the 21.00% are
both true and they are not the same measurement.

### 4.3 Five-year projection

**Status: strong for Our Plan and Downside.**

Our Plan:

| Year | Revenue | Restaurant-Level EBITDA | % | Corporate G&A | Company EBITDA | % |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | $6,588,778 | $1,098,127 | 16.67% | $326,910 | $771,217 | 11.71% |
| 2 | $8,493,849 | $1,943,770 | 22.88% | $326,055 | $1,617,715 | 19.05% |
| 3 | $9,380,163 | $2,276,175 | 24.27% | $326,055 | $1,950,120 | 20.79% |
| 4 | $9,900,794 | $2,478,579 | 25.03% | $326,055 | $2,152,524 | 21.74% |
| 5 | $10,366,872 | $2,647,247 | 25.54% | $326,055 | $2,321,192 | 22.39% |

Downside:

| Year | Revenue | Restaurant-Level EBITDA | % | Company EBITDA | % |
| --- | --- | --- | --- | --- | --- |
| 1 | $5,427,845 | $471,911 | 8.69% | $145,001 | 2.67% |
| 2 | $7,385,402 | $1,307,632 | 17.71% | $981,577 | 13.29% |
| 3 | $8,156,052 | $1,566,222 | 19.20% | $1,240,167 | 15.21% |
| 4 | $8,608,741 | $1,724,593 | 20.03% | $1,398,538 | 16.25% |
| 5 | $9,013,995 | $1,854,909 | 20.58% | $1,528,854 | 16.96% |

Best Case:

| Year | Revenue | Restaurant-Level EBITDA | % | Company EBITDA | % |
| --- | --- | --- | --- | --- | --- |
| 1 | $6,588,778 | $1,098,127 | 16.67% | $771,217 | 11.71% |
| 2 | $9,003,480 | $2,229,849 | 24.77% | $1,903,794 | 21.15% |
| 3 | $9,942,973 | $2,592,100 | 26.07% | $2,266,045 | 22.79% |
| 4 | $10,494,842 | $2,812,048 | 26.79% | $2,485,993 | 23.69% |
| 5 | $10,988,884 | $2,996,412 | 27.27% | $2,670,357 | 24.30% |

Growth is price-led. Covers are flat from Year 2, which is stated in the assumption
register. The Year 2 step comes from the six-day dinner expansion, entering as a half
increment in Year 2 and a full increment from Year 3. Base rent escalates 2% annually
off $225,000. Fixed operating expense is held flat across all five years by decision.

### 4.4 Scenario comparison

**Status: thin, and the thinness is structural rather than an error.**

Best Case Year 1 is identical to Our Plan Year 1 to the cent. Both carry a revenue
adjustment of 0.00%, a COGS adjustment of 0.00% and a labor adjustment of 0.00%. Best
Case differs from Our Plan through exactly one input, the out-year price uplift of 6%,
which touches Year 2 onward and moves no cost line.

A three-column Year 1 comparison will therefore render two distinct lines and a
duplicate. That is defensible if the workbook says what it is doing, which is claiming
the same opening and a faster path to pricing power rather than a better opening. It is
indefensible if presented as three independent cases.

The Downside is the more interesting column and is genuinely differentiated: revenue
adjustment -13.05%, COGS adjustment +3.00%, labor adjustment -8.70%, and its own
12-month ramp curve.

Recommendation, for decision rather than execution: either give Best Case a Year 1
distinction, or relabel the axis so the three columns read as one opening case and two
out-year trajectories plus one stress case.

### 4.5 Break-even

**Status: strong, and the most carefully documented table in the base.** Recomputed
22 August 2026 with the derivation of every input written into the record.

| Case | Fixed cost block | COGS % | Contribution margin | Break-even revenue | Break-even week | Covers per day |
| --- | --- | --- | --- | --- | --- | --- |
| Our Plan, Year 1 | $3,077,301.88 | 26.50% | 60.13% | $5,214,886 | $100,286 | 541.4 |
| Downside, Year 1 | $2,889,004.48 | 29.50% | 57.13% | $5,154,941 | $99,133 | 615.5 |
| Our Plan, Year 2 steady | $3,303,182.92 | 26.50% | 60.13% | $5,611,941 | $107,922 | 582.6 |
| Downside, Year 2 steady | $3,095,550.98 | 29.50% | 57.13% | $5,538,026 | $106,500 | 661.2 |

Best Case duplicates Our Plan on both rows, for the reason in 4.4, and the record says
so in terms.

Variable operating expense is 13.366425% and percentage rent enters at 4% above the
natural breakpoint, which is $3,750,000 in Year 1 and $3,825,000 in Year 2. Every case
solves above the breakpoint, so percentage rent behaves as a fourth variable cost. No
active scenario stays under the breakpoint, including the Downside, which clears it by
$1,677,845 in Year 1.

The headline is that Our Plan Year 1 clears break-even by $1,373,892 of revenue, and
the Downside clears it by $272,904. The Downside is thin but positive, and the workbook
should show that rather than smooth it.

### 4.6 Sources and uses

**Status: uses are strong, sources are thin.**

| Line | Lean Opening | Full Vision |
| --- | --- | --- |
| Confirmed LHI and permanent improvements | $195,000 | $195,000 |
| TI-eligible hard-cost scope | $1,055,000 | $1,055,000 |
| FF&E | $315,000 | $443,089 |
| OS&E | $300,000 | $399,581 |
| Pre-opening expenses | $252,000 | $415,000 |
| Reserves and deposits | $467,000 | $467,000 |
| **Adjusted project cost** | **$2,584,000** | **$2,974,670** |
| Less landlord allowance | ($1,100,000) | ($1,100,000) |
| **Outside capital after allowance** | **$1,484,000** | **$1,874,670** |
| Working capital and opening cash cushion | $1,016,000 | $625,330 |
| **Total raise** | **$2,500,000** | **$2,500,000** |

Both plan views balance to the same raise. Gross project funding is $3,600,000 with the
allowance included. Roughly $250,000 of landlord-delivered scope is carried at zero and
is explicitly not added.

The sources side is one line. That is honest for a full equity raise, but the exhibit
should show the allowance as a separate non-cash source rather than only as a deduction,
or an investor will read $2.5M against a $2.58M to $2.97M project and ask where the
gap went.

### 4.7 Capacity and physical constraints

**Status: strong.**

5,178 rentable square feet. 126 seats: 52 in the main dining room, 74 on the patio.
Patio standing capacity of 24, confirmed against the floor plan. Table mix: 28 tables
on the patio at a 70% two-top ratio, 17 in the dining room at 50%.

Turn times by daypart: dinner 1.67 hours, brunch 1.25, lunch 1.00, late night 1.75.
Early morning is window service with no seat constraint.

Every service row carries a capacity check with the headroom stated, ranging from
23 seats of buffer on peak late night to 148 on a Wednesday dinner. The two peak late
night services are the only ones that rely on standing capacity, using 10.58 of the
24 places.

One exposure the exhibit has to state rather than bury: 74 of 126 seats, 58.7%, are
outdoors. See section 6 on the weather factor.

### 4.8 The assumption register

**Status: strong in substance, needs screening before it ships.**

63 records in Model Assumptions, most carrying an explicit source and a decision date.
This is unusually good material and it is the fastest way to answer a diligence question
without opening the model.

Roughly a quarter of the records are INTERNAL ONLY and must be filtered at record level
rather than field level: everything sourced to the Redcar tenant proposal, the SBA
record, the strategic capital record, and the records naming the automation vendor or a
daypart code name.

The register also contains its own supersession trail, with records marked CLOSED,
RESOLVED and REPORT ONLY. Those should not ship as-is. They are working state, and an
investor reading "REPORT ONLY: documented mature week is stale" will draw a conclusion
about the model rather than about the documentation.

### 4.9 The corporate G&A scaling view

**Status: strong, with two caveats that must travel with it.**

| Units | Annual revenue | Founder comp | Burden | Corporate hire | Total G&A | % of revenue |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | $8,493,849 | $300,000 | $26,055 | $0 | $326,055 | 3.84% |
| 2 | $16,987,698 | $300,000 | $26,055 | $0 | $326,055 | 1.92% |
| 3 | $25,481,547 | $300,000 | $26,055 | $103,275 | $429,330 | 1.68% |

The leverage argument holds even with the third-unit Director of Operations booked at
$103,275, which is the honest way to present it.

Caveat one: recruiting and the ACA health plan are held at zero at two and three units
by decision, not by omission. The mechanism for both is documented in the base and
neither cost has been sized from a source. Corporate G&A at two and three units is
understated by both lines. The workbook must say this on the same page as the table.

Caveat two: the revenue basis is Year 2 steady state, $8,493,849, not Year 1. The
column header has to say so or the 3.84% will be read against the Year 1 revenue of
$6,588,778, where the same $326,055 is 4.95%.

### 4.10 What is missing

**Monthly cash flow and runway. This is the single largest gap.**

The Cash Flow table holds five manual rows covering July to November 2025, with no
cumulative balance. The base's own Model Index says it must not be used for runway and
that runway remains unverified pending a rebuild for the August 2027 opening.

An investor in a pre-opening restaurant will ask, early and in the room, how many months
of cash sit between close and the break-even month, and what the trough looks like. The
Pre-Opening Six-Month Use Schedule answers part of it and the $1,016,000 cushion in the
Lean plan answers part of it, but there is no month-by-month path. Nothing else in this
package can substitute for it.

Also missing, in descending order of importance:

- **A sensitivity view.** No table computes elasticity. The scenario instrument will be
  the first place this exists, so the underlying ranges have to be defensible on their
  own rather than inherited.
- **Per-cover contribution across all dayparts.** It exists for lunch and late night
  only. Given that the multi-daypart argument is the thesis, contribution per cover by
  daypart is the number that proves it.
- **A Year 1 monthly revenue and EBITDA curve for the exhibit.** The data exists in
  Y1 Monthly Projections but stops at contribution after COGS and labor. It does not
  carry down to Restaurant-Level EBITDA by month.
- **Working capital beyond the pre-opening six months.**

---

## 5. Lever set for the scenario instrument

Operating levers only. No capital levers. Selection is by sensitivity, measured against
the mature annual revenue of $7,846,826 and a contribution margin of 60.13%.

The ranking is worth stating plainly, because it is not intuitive: the revenue levers
move the outcome three to six times harder than the cost levers. An instrument that
gives equal visual weight to a food cost slider and a dinner covers slider will
misrepresent the business.

### The eight

**L1. Dinner covers per service.** Source: Reference: Service Schedule,
`Total Service Covers`, five dinner rows.
Current: Wednesday 200, Thursday 270, Friday 350, Saturday 350, Sunday 330. 1,500 per
week. Defensible range 80% to 115% of current.
Moves: 52.3% of revenue. A 10% move is $410,446 of annual revenue and $246,816 of
EBITDA. Capacity headroom supports the top of the range, since the tightest dinner
service still carries 42 seats of buffer.
**Highest sensitivity input in the model.**

**L2. Dinner per-person average.** Source: Reference: Pricing Matrix, dinner rows.
Current: $46 to $54 by day, $52.62 blended. Defensible range $46 to $62.
Moves: 52.3% of revenue with only the COGS offset. A $5 move is $390,000 of annual
revenue and roughly $287,000 of EBITDA. Slightly harder than L1 per dollar because it
carries no incremental labor.

**L3. Blended cost of sales.** Source: P&L Model, `Food Cost %` 28% and
`Beverage Cost %` 22%, resolving to 26.50% blended.
Current 26.50%. Defensible range 25.0% to 31.0%, where the top is the Downside case
already modelled at 29.50%.
Moves: $78,468 of EBITDA per 100 basis points. The register notes COGS is held flat
across all five years with no supplier-negotiation improvement modelled, so the
downward half of this range is unclaimed upside.

**L4. Dinner kitchen labor rate.** Source: Reference: Service Schedule, the BOH labor
percentage input on dinner rows.
Current 12.0%. Defensible range 10.0% to 15.0%. For reference the other dayparts run
at lunch 6.83%, brunch 9.55%, late night 15.34% and early morning 17.23%.
Moves: $41,045 per 100 basis points. This is the lever that tests the shared-crew
thesis, since all five dayparts derive from one kitchen shift build.

**L5. Front-of-house schedule density.** Source: Reference: Service Schedule,
`Total Labor Cost`, all 22 rows.
Current $15,402 per week against $17,368 of kitchen labor and $7,880 salaried.
Defensible range 90% to 115%.
Moves: $80,090 per 10%. This is the lever an operator actually pulls week to week, and
it is the one most likely to be tested in the room.

**L6. Year 1 capacity utilisation ramp.** Source: Scenario Timeline,
`Capacity Utilization %`, 12 rows per curve.
Current: conservative curve 58% in month 1 rising to 100% by month 10 and holding.
The Downside curve runs 52% to 100%. The register documents a B2 curve of 65% to 100%
over six months and a C2 curve of 75% to 110%.
Moves: Year 1 only, but it moves it hard. Our Plan Year 1 revenue is 84% of the mature
annual run rate, so the ramp is worth roughly $1.26M of Year 1 revenue.
Defensible range: the three documented curves.

**L7. Out-year price uplift.** Source: Years 1-5 Projections,
`Out-Year Price Uplift %`.
Current 0% in Our Plan, 6% in Best Case. Defensible range 0% to 8%.
Moves: $622,012 of Year 5 revenue between the two current settings. This is the only
input that separates Best Case from Our Plan and it should be exposed as such rather
than hidden behind a scenario name.

**L8. Wage escalation.** Source: Years 1-5 Projections, `Wage Escalation Factor`.
Current 3.5% annually, Years 2 to 5. Defensible range 2.5% to 5.0%.
Moves: roughly $88,000 of Year 5 EBITDA per 100 basis points, compounding.
The register records this as an above-market premium rather than a market rate, which
is a deliberate position and a good one to be able to defend live. Exposing it invites
the question, which is the point.

### Levers considered and not proposed

- **Seat count.** Physically fixed at 126 until a buildout decision reopens it. The
  capacity cases exist for stress testing, not for operating.
- **Percentage rent rate and natural breakpoint yield.** These are lease terms under
  live negotiation, not operating levers, and they sit inside the internal set.
- **Days per week by daypart.** A real lever, but it changes the labor build
  structurally rather than proportionally, so a slider would misrepresent it. Better
  handled as a discrete scenario.
- **Corporate G&A.** Not an operating lever at one unit. It is founder compensation
  and its burden, and it is a decision, not a dial.
- **3PD commission and mix.** Real, but confined to lunch, which is 16.6% of revenue,
  and the two source tables disagree on packaging cost. See section 6.

---

## 6. Judgment calls

Reported rather than decided alone, as instructed. Grouped by what kind of problem
each one is.

### 6.1 The documentation layer is one revision behind the calculation layer

**This is the highest-priority item in this document.**

The Model Index presentation note for the operating engine, dated 20 August 2026,
states Our Plan Year 1 as Restaurant-Level EBITDA $1,249,649 (18.97%) and Company
EBITDA $922,739 (14.00%).

The live figures in Years 1-5 Projections are Restaurant-Level EBITDA $1,098,126.93
(16.67%) and Company EBITDA $771,216.93 (11.71%).

Both lines are overstated in the note by **$151,522.07**. The same note's mature weekly
row says Restaurant-Level EBITDA $34,457 (22.83%) against a live $31,696.53 (21.00%),
overstated by $2,760.47 per week.

The calculation layer was refrozen 22 August 2026 and is internally consistent. The
Model Index note was not refreshed with it. This matters because the Model Index is
precisely the artefact someone would trust when writing investor copy, and it is the
most quotable text in the base. Anything already drafted from it carries the error.

Not a modelling defect. A documentation defect, and a dangerous one.

### 6.2 Fields whose names misstate what they compute

**`Covers` in Revenue Build Up is not the revenue multiplicand.** The field that drives
revenue is `Calculated Covers`, which allocates the Service Schedule `Total Service
Covers` across revenue centers by seat share. Saturday dinner reads `Covers` 166 in
both the dining room and on the patio, while the revenue implies 145 and 206
respectively, allocating 350 service covers across 52 and 74 seats. Anyone building the
workbook from the field named `Covers` will produce a number that does not tie.

**`Available` is unset on all five lunch rows** in Reference: Service Schedule, each of
which carries $5,000 of daily revenue. Every other operating row has it checked. Either
the flag is stale or lunch is flagged off while contributing 16.6% of revenue.

**`Lunch Model legacy. don't use`** is a live Scenario Timeline field. It declares
itself retired in its own name but carries no `DELETE` prefix, so it survived the skip
rules. It should be prefixed.

**`Adjusted Total Revenue`, `Location Revenue Multiplier` and `Revenue Adj per $2.5K`**
in P&L Model implement an undocumented rent-to-revenue coefficient and produce a
revenue figure that diverges from the canonical $150,900.50. No source record explains
the coefficient. Classified INTERNAL ONLY on that basis.

**`Monthly Rent` sits alongside `Base Monthly Rent`** in P&L Model with no indication
which governs.

**`Odd Duck`** is a Reference: Service Schedule field name. It is a competitor's name
used as a column header, with a companion `Sŏn` column.

### 6.3 Reconciliation gaps

**The Lunch Model table does not tie to canonical lunch revenue.** Three figures exist:
$25,000 per week canonical, flowing through Revenue Build Up to Service Schedule to
Restaurant Configurator and into the mature week; $17,040 on the "Dosi QSR" record; and
$3,600 on the "FSR Lunch" record, which is the only one with `Active` checked. The
active flag points at a record that does not drive the model. The Model Index confirms
lunch now flows through the revenue spine, so the Lunch Model table appears to be a
superseded parallel structure that was never retired. Its 42 live fields were
classified, but the exhibit should not draw from it.

**Packaging cost per order is $1.60** in Reference: Service Schedule and **$2.50** in
Lunch Model. Same input, two values.

**A second live P&L Model record, "Lean Fixed Costs",** carries no `DELETE` prefix and
is referenced by no active scenario. It runs different rates: 24% food against 28%,
20% beverage against 22%, 1% marketing against 1.5%. It reads as a live alternative
and is not one.

**Revenue Build Up `Covers` disagrees with Service Schedule `Total Service Covers`**,
for example 190 against 200 on Wednesday dinner. The latter is canonical, since the
22 rows sum to exactly the 5,702.5 the break-even table uses.

### 6.4 Working assumptions that are directionally right but unsourced

**Competitor revenue attributed to named local businesses.** Restaurant Configurator
carries `Comparison` and `Comp Annual Revenue`: two named coffee operators at $800,000,
and three named restaurants at $3,000,000, $1,600,000 and $4,800,000. There is no
source field on the table. These are private companies and the figures are estimates.
Classified INTERNAL ONLY. If a comparable set is wanted in the exhibit, it needs
published or licensed data, and probably needs the names anonymised to "comparable
Austin operators".

**The patio weather factor.** Reference: Seating & Capacity carries
`Patio Weather Factor %` at 75 on the patio record. It does not appear to reach the
revenue build: the capacity checks compute against the full 74 patio seats, and the
cover counts are entered demand rather than derived from usable seats. With 58.7% of
seats outdoors in Austin, a diligence-minded reader will look for a weather derate and
will find a field that exists and a model that does not visibly apply it. Either it is
applied somewhere not visible through the schema, or it is a real unmodelled exposure.
Worth resolving before the exhibit ships rather than in the room.

**Recruiting and the ACA health plan at zero.** Documented as a decision at two and
three units, with the mechanism written up and the cost unsized. The base states
plainly that corporate G&A is understated by both. Ships only with that statement
attached.

**Founder tax treatment modelled as W-2, pending CPA confirmation.**

**FF&E and OS&E quotes are unvalidated**, per the Model Index. They carry $315,000 and
$300,000 in the Lean plan.

**Roughly $250,000 of landlord-delivered scope** traces to an internal task rather than
the tenant proposal. Correctly carried at zero. Should stay at zero in the exhibit.

### 6.5 Things a reader could misread without surrounding context

**`Year 1 Contribution` and `Monthly Contribution` are after cost of sales and labor
only.** No occupancy, no operating expense, no corporate G&A. The Scenario Configurator
field name spells this out; the Y1 Monthly Projections one does not. Our Plan Year 1
contribution is $2,678,414 against a Company EBITDA of $771,217. A reader who takes
contribution for EBITDA overstates the business by 3.5 times. If either ships, the
label has to carry the qualifier.

**Covers are held constant at 5,702.5 across all three scenarios.** The Downside
achieves its -13.05% through check average, not through traffic. The break-even record
states this explicitly and notes the reading could run the other way. The exhibit should
make the choice visible, because "fewer customers" and "customers spending less" are
different risks and an investor will have a view on which is more likely.

**Scenario naming is inconsistent across tables.** Scenario Configurator says
"Downside". Years 1-5 Projections and Y1 Monthly Projections say "Investor Downside".
Scenario Timeline says "Downside". Launch Strategy values read "Conservative" and
"Aggressive", which are a third vocabulary. Pick one set of names for the workbook.

**Year 1 corporate G&A is $326,910 against $326,055 in every other year.** The $855 is
the calendar straddle charging the per-hire payroll component twice. It looks like an
error and is not. Footnote it or it will be queried.

**Best Case Year 1 equals Our Plan Year 1 exactly.** Covered in 4.4. Flagged again here
because in a side-by-side table it reads as a copy-paste failure.

---

## 7. Method notes

**Access.** Read-only throughout. The base was frozen at the time of the pass and
nothing was written to it, including no corrections to the items in section 6.

**How fields were classified.** The schema was pulled once and the 80 retired fields
removed before any classification. The remaining 773 were classified by an ordered rule
set: explicit field-level decisions first, then name-pattern rules for the
non-negotiable INTERNAL ONLY categories, then field-type defaults for relational
plumbing, then a table-level default. Where a table was wholly internal, no field within
it was promoted out of that class.

**Verification.** Field IDs, not field names, were used to read values, because the base
carries many similarly named fields across tables. Every ID appearing in this document
was mapped back to its name against the schema before the value was used. Figures were
recomputed from the base rather than carried from any document: the mature week was
rebuilt from the 22 service rows, the Year 1 bridge was rebuilt from its five component
lines, and both tied to the cent. The staleness in section 6.1 was found by that
recomputation, not by reading two documents against each other.

**What was not verified.** Formula bodies are not exposed through the API, so
dependency direction was inferred from `referencedFieldIds` and confirmed by arithmetic
against live values rather than by reading formula text. Where arithmetic could not
confirm a relationship, the field was flagged rather than asserted. The patio weather
factor in 6.4 is the main case: its absence from the revenue build is an inference from
the capacity checks, not a proven fact.

**Confidence.** The revenue spine, the three-line bridge, the five-year projection, the
break-even table and the sources and uses are high confidence and reconciled. The labor
build is high confidence at the daypart level and medium at the position level, which
was not fully traced. The Lunch Model, Late Night Model and Multi-Daypart Summary are
medium to low confidence as investor-facing sources, for the reasons in 6.3.

**Figure provenance.** Every number in this document came from a live read of
St. Elmo Dashboard V2 on 22 August 2026. None was carried from memory, a deck or a
prior document.

---

## 8. Recommended sequence from here

1. Refresh the Model Index presentation notes against the live figures, or mark them
   superseded. Nothing investor-facing should be drafted from them until then.
2. Resolve the patio weather factor. It is the one open item that could move the
   revenue build rather than the documentation around it.
3. Decide the Best Case question in 4.4, since it determines whether the scenario
   comparison has three columns or two plus a trajectory.
4. Rebuild the cash flow for the August 2027 opening. It is the largest gap and the
   most likely question in a live meeting.
5. Prefix the stragglers: `Lunch Model legacy. don't use`, the "Lean Fixed Costs"
   P&L record, and the Lunch Model table if it is confirmed superseded.
6. Screen the assumption register at record level and restate the Redcar-sourced
   citations before it ships.
