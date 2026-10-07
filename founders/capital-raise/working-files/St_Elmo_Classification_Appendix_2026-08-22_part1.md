# St. Elmo Dashboard V2, field classification appendix

Part 1 of 2. Companion to `St_Elmo_Classification_Main_2026-08-22.md`.

Base: St. Elmo Dashboard V2 (Airtable). Classified 22 August 2026, read-only.
The base was frozen; nothing was written to it.

Every live field in the base, sorted into exactly one class.

| Code | Meaning |
| --- | --- |
| AS-IS | Goes to the investor workbook unchanged |
| DERIVED | Informs a figure that ships, but not in this form |
| INTERNAL | Never leaves the base |

`F` marks a low-confidence row: a judgment call, a field whose name misstates what it
computes, or something a reader could misread without context. Every flagged row is
written up in section 6 of the main document.

Excluded as retired and not counted: 56 fields prefixed `DELETE`, 24 prefixed `LEGACY`.

Totals across both parts: 773 live fields. AS-IS 145, DERIVED 345, INTERNAL 283.
39 rows are flagged.

Tables in this part: P&L Model, Years 1-5 Projections, Scenario Configurator, Y1 Monthly Projections, Revenue Build Up, Reference: Service Schedule, Reference: Pricing Matrix, Reference: Seating & Capacity, Labor: Positions, Reference: Labor Models, Reference: Staffing Model, Restaurant Configurator, Seasonal Factors, Market Conditions Profile, Scenario Timeline

---

## P&L Model

82 live fields. AS-IS 21, DERIVED 44, INTERNAL 17.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Model | INTERNAL | Internal model record name |  |
| Service Schedule | INTERNAL | Relational link, not data |  |
| Notes | INTERNAL | Working commentary |  |
| Food Cost % | AS-IS | Published cost-of-sales rate; investor expects to see it |  |
| Beverage Cost % | AS-IS | Published cost-of-sales rate; investor expects to see it |  |
| CC Processing % | AS-IS | Published cost-of-sales rate; investor expects to see it |  |
| Smallwares % | AS-IS | Published cost-of-sales rate; investor expects to see it |  |
| Marketing % | AS-IS | Published cost-of-sales rate; investor expects to see it |  |
| Rent (Weekly) | DERIVED | Weekly rent allocation; ships annualised |  |
| CAM (Weekly) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Utilities (Weekly) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Insurance (Weekly) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| R&M (Weekly) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Technology (Weekly) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Linen (Weekly) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Total Revenue | AS-IS | Mature weekly revenue, the anchor of the revenue build |  |
| Total FOH Labor | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| BOH Labor % — Legacy Flat Rate | INTERNAL | Superseded flat rate retained beside the live effective rate | * |
| Licenses (Weekly) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Professional (Weekly) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Food Cost | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Beverage Cost | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| BOH Labor | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| CC Processing | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Small Wares  | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Marketing | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Total COGs | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Total Occupancy | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Total OpEx | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Gross Profit | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| COGS % | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Scenario Analysis | INTERNAL | Relational link, not data |  |
| Comps % | AS-IS | Published cost-of-sales rate; investor expects to see it |  |
| Comps | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Voids % | AS-IS | Published cost-of-sales rate; investor expects to see it |  |
| Voids | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Menu Printing % | AS-IS | Published cost-of-sales rate; investor expects to see it |  |
| Menu Printing | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Seasonal Factors | INTERNAL | Relational link, not data |  |
| Labor Summary | INTERNAL | Relational link, not data |  |
| Restaurant Salaried (Weekly) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Lunch Model | INTERNAL | Relational link, not data |  |
| Base Monthly Rent | DERIVED | Ships as annualised occupancy, not as a monthly lease figure |  |
| Revenue Adj per $2.5K | INTERNAL | Undocumented rent-to-revenue sensitivity coefficient | * |
| Location Revenue Multiplier | INTERNAL | Derived from the undocumented rent sensitivity coefficient | * |
| Adjusted Total Revenue | INTERNAL | Applies the undocumented rent sensitivity; diverges from canonical revenue | * |
| Monthly Rent | INTERNAL | Duplicate rent input alongside Base Monthly Rent; ambiguous which governs | * |
| Lunch Strategy | INTERNAL | Internal daypart strategy selector |  |
| Base Operating Model | INTERNAL | Internal model selector |  |
| Scenario Configurator | INTERNAL | Relational link, not data |  |
| BOH Labor — Daypart Rollup | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| BOH Labor % — Effective | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Revenue Weeks / Year | AS-IS | 52-week revenue convention; must be stated to read any annual figure |  |
| Percentage Rent Rate | DERIVED | Lease economics; ships as an occupancy input, not as a lease term |  |
| Natural Breakpoint Yield | DERIVED | Lease economics; ships as an occupancy input, not as a lease term |  |
| Annual Natural Breakpoint | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Annualized Revenue for % Rent | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Percentage Rent (Annual) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Percentage Rent (Weekly) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Legacy Four-Wall EBITDA Before % Rent | INTERNAL | Retired EBITDA terminology; conflicts with locked Restaurant-Level naming | * |
| Labor Weeks / Year | AS-IS | 50-week labor convention; must be stated to read any annual figure |  |
| Hyphen Automation (Weekly) | INTERNAL | Names an unannounced automation vendor |  |
| 3PD Commission (Weekly) | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Packaging (Weekly) | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Burden: FICA % — Input | AS-IS | Payroll burden rate; needed to read the labor line honestly |  |
| Burden: Workers Comp % — Input | AS-IS | Payroll burden rate; needed to read the labor line honestly |  |
| Burden: Per-Hire FUTA+SUTA (Weekly) — Restaurant | DERIVED | Per-hire burden; ships inside the labor line |  |
| Restaurant Wages (Weekly) | AS-IS | Mature weekly wage base, the anchor of the labor build |  |
| Payroll Burden (Weekly) — Rebased | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Restaurant Labor (Weekly) — Rebased | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Corporate Payroll Burden (Weekly) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Restaurant Labor % — Rebased | AS-IS | Labor as a share of revenue, a core operating ratio |  |
| Restaurant Prime Cost % — Rebased | AS-IS | Prime cost, the standard operator benchmark |  |
| Restaurant-Level EBITDA (Weekly) | AS-IS | Weekly restaurant-level result, top of the three-line bridge |  |
| Company EBITDA (Weekly) | AS-IS | Weekly company result, bottom of the three-line bridge |  |
| Burden: Wage-Proportional % | AS-IS | Payroll burden rate; needed to read the labor line honestly |  |
| Burden: Per-Hire Y1 with Calendar Straddle (Annual) | DERIVED | Year 1 straddle; ships as a footnote to Year 1 labor |  |
| Corporate Compensation (Annual) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Corporate Headcount (Allocated) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Corporate Compensation (Weekly) | DERIVED | Weekly operating engine; feeds the annual investor view, not shown raw |  |
| Corporate G&A (Weekly) | AS-IS | Weekly corporate layer, middle of the three-line bridge |  |
| Restaurant-Level EBITDA % (Rebased) | AS-IS | Weekly restaurant-level margin |  |

## Years 1-5 Projections

43 live fields. AS-IS 25, DERIVED 15, INTERNAL 3.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Projection ID | INTERNAL | Carries internal scenario record naming |  |
| Scenario Configurator | INTERNAL | Relational link, not data |  |
| Year Number | AS-IS | Canonical five-year P&L line |  |
| Calendar Year | AS-IS | Canonical five-year P&L line |  |
| Growth from Y1 % | AS-IS | Cumulative growth against Year 1 |  |
| Cumulative Multiplier | DERIVED | Intermediate growth factor |  |
| COGS % | AS-IS | Canonical five-year P&L line |  |
| OpEx % | AS-IS | Canonical five-year P&L line |  |
| Y1 Revenue (from Scenario) | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Annual Revenue | AS-IS | Canonical five-year P&L line |  |
| Annual COGS | AS-IS | Canonical five-year P&L line |  |
| Annual OpEx | AS-IS | Canonical five-year P&L line |  |
| Y1 Contribution (from Scenario) | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Notes | INTERNAL | Working commentary |  |
| Annual Base Rent (Normalized) | AS-IS | Canonical five-year P&L line |  |
| Annual NNN / CAM | AS-IS | Canonical five-year P&L line |  |
| Annual Natural Breakpoint | AS-IS | Canonical five-year P&L line |  |
| Annual Percentage Rent | AS-IS | Canonical five-year P&L line |  |
| Total Annual Occupancy | AS-IS | Canonical five-year P&L line |  |
| Mature Weekly Revenue | DERIVED | Lookup of an upstream value; ships through its source |  |
| Six-Day Dinner Weekly Revenue | DERIVED | Year 2 dinner expansion increment; ships inside the growth narrative |  |
| Six-Day Dinner Weekly Labor | DERIVED | Year 2 dinner expansion increment; ships inside the growth narrative |  |
| Price Growth Factor (ex-lunch) | AS-IS | Canonical five-year P&L line |  |
| Wage Escalation Factor | AS-IS | Canonical five-year P&L line |  |
| Revenue Adj % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Labor Adj % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Seasonal Uplift Factor | AS-IS | Canonical five-year P&L line |  |
| Out-Year Price Uplift % | AS-IS | The only lever separating Best Case from Our Plan; must be visible |  |
| Lunch Growth Factor | AS-IS | Canonical five-year P&L line |  |
| Mature Weekly Lunch Revenue (live) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Mature Weekly Wages | DERIVED | Lookup of an upstream value; ships through its source |  |
| Burden: Wage-Proportional % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Burden: Per-Hire (Weekly) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Y1 Labor (from Scenario) — Rebased | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Annual Labor — Rebased | AS-IS | Canonical five-year P&L line |  |
| Restaurant-Level EBITDA | AS-IS | Canonical five-year P&L line |  |
| Corporate G&A | AS-IS | Canonical five-year P&L line |  |
| Company EBITDA | AS-IS | Canonical five-year P&L line |  |
| Corporate Compensation (Annual) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Corporate Headcount (Allocated) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Restaurant-Level EBITDA % | AS-IS | Canonical five-year P&L line |  |
| Corporate G&A % of Revenue | AS-IS | Canonical five-year P&L line |  |
| Company EBITDA % | AS-IS | Canonical five-year P&L line |  |

## Scenario Configurator

37 live fields. AS-IS 4, DERIVED 25, INTERNAL 8.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Scenario Name | AS-IS | Scenario label for the comparison exhibit |  |
| Status | INTERNAL | Internal active/archived state |  |
| Description | DERIVED | Scenario description; ships rewritten |  |
| Operating Model | INTERNAL | Relational link, not data |  |
| Opening Month | DERIVED | Scenario control layer; drives the comparison exhibit |  |
| Market Conditions | INTERNAL | Relational link, not data |  |
| Operating Model Name | DERIVED | Lookup of an upstream value; ships through its source |  |
| Market Profile Name | DERIVED | Lookup of an upstream value; ships through its source |  |
| Base Weekly Revenue | DERIVED | Lookup of an upstream value; ships through its source |  |
| Base Weekly EBITDA (Pre % Rent) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Base COGS % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Revenue Adj % | DERIVED | Lookup of an upstream value; ships through its source |  |
| COGS Adj % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Labor Adj % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Notes | INTERNAL | Working commentary |  |
| Adjusted Weekly Revenue | AS-IS | Mature weekly revenue by scenario |  |
| Adjusted Weekly EBITDA | DERIVED | Scenario control layer; drives the comparison exhibit |  |
| Annual Revenue (52W, mature) | AS-IS | Mature-year revenue at full run rate |  |
| Monthly Projections | INTERNAL | Relational link, not data |  |
| Year 1 Revenue | AS-IS | Year 1 revenue by scenario |  |
| Year 1 Contribution | DERIVED | Contribution after COGS and labor only; label misleads without the caveat | * |
| Year 1 Contribution Margin % (after COGS and labor only) | DERIVED | Partial margin; easily misread as EBITDA | * |
| Manual sort | INTERNAL | Airtable sort control, not data |  |
| Years 1-5 Projections 2 | INTERNAL | Relational link, not data |  |
| Launch Strategy | DERIVED | Ramp-curve selector; ships as a named ramp assumption |  |
| Salaried Weekly | DERIVED | Lookup of an upstream value; ships through its source |  |
| Lunch Daypart | INTERNAL | Relational link, not data |  |
| Mature Weekly Lunch Revenue | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Base Weekly Wages | DERIVED | Lookup of an upstream value; ships through its source |  |
| Burden: Wage-Proportional % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Burden: Per-Hire (Weekly) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Burden: Per-Hire Y1 with Straddle (Annual) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Year 1 Labor — Rebased | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Corporate Compensation (Annual) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Corporate Headcount (Allocated) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Base Labor % (Rebased) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Base Restaurant-Level EBITDA % | DERIVED | Lookup of an upstream value; ships through its source |  |

## Y1 Monthly Projections

30 live fields. AS-IS 5, DERIVED 20, INTERNAL 5.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Projection ID | INTERNAL | Carries internal scenario record naming |  |
| Scenario Configurator | INTERNAL | Relational link, not data |  |
| Operating Month | AS-IS | Operating month index |  |
| Scenario Timeline | INTERNAL | Relational link, not data |  |
| Seasonal Factor | INTERNAL | Relational link, not data |  |
| Base Weekly Revenue | DERIVED | Lookup of an upstream value; ships through its source |  |
| Revenue Adj % | DERIVED | Lookup of an upstream value; ships through its source |  |
| COGS Adj % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Labor Adj % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Base COGS % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Lunch Weekly Revenue | DERIVED | Lookup of an upstream value; ships through its source |  |
| Lunch Weekly Labor | DERIVED | Lookup of an upstream value; ships through its source |  |
| Dinner Active | DERIVED | Lookup of an upstream value; ships through its source |  |
| Dinner Days | DERIVED | Lookup of an upstream value; ships through its source |  |
| Scale Factor % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Monthly Revenue | AS-IS | Month-by-month revenue across the opening year |  |
| Monthly COGS | AS-IS | Month-by-month cost of sales |  |
| Monthly Contribution | DERIVED | Contribution after COGS and labor only; label misleads | * |
| Opening Month | DERIVED | Lookup of an upstream value; ships through its source |  |
| Capacity Utilization % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Calendar Month (Calculated) | AS-IS | Calendar mapping of the operating month |  |
| Seasonal Factor Month | DERIVED | Lookup of an upstream value; ships through its source |  |
| Seasonal Factor Check | INTERNAL | Internal reconciliation check |  |
| Active Weekly Revenue | DERIVED | Lookup of an upstream value; ships through its source |  |
| Active Weekly FOH Labor | DERIVED | Lookup of an upstream value; ships through its source |  |
| Active Weekly BOH Labor | DERIVED | Lookup of an upstream value; ships through its source |  |
| Salaried Weekly | DERIVED | Lookup of an upstream value; ships through its source |  |
| Burden: Wage-Proportional % | DERIVED | Lookup of an upstream value; ships through its source |  |
| Burden: Per-Hire Y1 with Straddle (Annual) | DERIVED | Lookup of an upstream value; ships through its source |  |
| Monthly Labor — Rebased | AS-IS | Month-by-month labor |  |

## Revenue Build Up

23 live fields. AS-IS 10, DERIVED 6, INTERNAL 7.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Revenue ID | INTERNAL | Concatenated internal key |  |
| Day of Week | AS-IS | Day-part revenue driver: covers times price |  |
| Day Part | INTERNAL | Relational link, not data |  |
| Revenue Center | INTERNAL | Relational link, not data |  |
| Full Service | DERIVED | Service-type flag behind the labor model |  |
| Covers | INTERNAL | Not the revenue multiplicand; Calculated Covers drives revenue | * |
| Related Pricing Protocols | INTERNAL | Relational link, not data |  |
| Total PPA | AS-IS | Per-person average, the second revenue driver |  |
| Total Daily Revenue | AS-IS | Covers times price by day and daypart |  |
| Total Annual Revenue (52W) | AS-IS | Annualised line revenue |  |
| Service Schedule | INTERNAL | Relational link, not data |  |
| Duration of Service | DERIVED | Lookup of an upstream value; ships through its source |  |
| Turn Time (h) | AS-IS | Turn-time assumption by daypart |  |
| Servers Needed | DERIVED | Staffing derived from peak load |  |
| Peak Covers | AS-IS | Peak-hour load against seats |  |
| Max Seats | DERIVED | Lookup of an upstream value; ships through its source |  |
| Max Covers | AS-IS | Capacity ceiling by service |  |
| Capacity Check | AS-IS | Shows each service sits inside physical capacity |  |
| Total Service Covers | AS-IS | Canonical demand input; 22 rows sum to the 5,702.5 mature week |  |
| Service Seats | DERIVED | Lookup of an upstream value; ships through its source |  |
| Calculated Covers | AS-IS | The actual revenue driver: service covers allocated by seat share |  |
| dow | INTERNAL | Airtable sort control, not data |  |
| Standing Capacity | DERIVED | Lookup of an upstream value; ships through its source |  |

## Reference: Service Schedule

31 live fields. AS-IS 4, DERIVED 15, INTERNAL 12.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Schedule ID | INTERNAL | Concatenated internal key |  |
| Day Part | INTERNAL | Relational link, not data |  |
| Day of Week | DERIVED | Operating-hours and daypart cost build behind the revenue spine |  |
| Available | INTERNAL | Day-active flag; unset on all five lunch rows that carry revenue | * |
| Start Time | AS-IS | Operating hours by daypart |  |
| End Time | AS-IS | Operating hours by daypart |  |
| Total Hours | AS-IS | Service hours by daypart |  |
| Display Order | INTERNAL | Airtable sort control, not data |  |
| Revenue Projections 2 | INTERNAL | Relational link, not data |  |
| Odd Duck | INTERNAL | Column named after a local competitor | * |
| Sŏn | DERIVED | Comparison column against a competitor benchmark | * |
| Staffing | INTERNAL | Relational link, not data |  |
| Total Service Revenue | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Total Labor Cost | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Service Labor % | DERIVED | Operating-hours and daypart cost build behind the revenue spine |  |
| Service Charge Pool | INTERNAL | No-tipping compensation model, not yet legally reviewed | * |
| Total Service Points | INTERNAL | No-tipping point-pool mechanic, not yet legally reviewed | * |
| Point Value | INTERNAL | No-tipping point-pool mechanic, not yet legally reviewed | * |
| Weekly Totals | INTERNAL | Relational link, not data |  |
| Service Peak Covers | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Total Service Covers | AS-IS | Canonical demand input; 22 rows sum to the 5,702.5 mature week |  |
| Service Seats | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Annual Service Revenue (52W) | DERIVED | Operating-hours and daypart cost build behind the revenue spine |  |
| BOH Rate Basis | INTERNAL | Internal derivation commentary |  |
| BOH Labor % — Input | DERIVED | Kitchen labor rate by daypart; ships inside the labor line |  |
| BOH Labor — Daypart Base | DERIVED | Operating-hours and daypart cost build behind the revenue spine |  |
| 3PD Commission % — Input | DERIVED | Delivery commission; ships inside the lunch margin |  |
| 3PD Mix % — Input | DERIVED | Delivery mix; ships inside the lunch margin |  |
| Packaging Cost Per Order — Input | DERIVED | Packaging cost; conflicts with the Lunch Model figure | * |
| 3PD Commission Cost | DERIVED | Operating-hours and daypart cost build behind the revenue spine |  |
| Packaging Cost | DERIVED | Operating-hours and daypart cost build behind the revenue spine |  |

## Reference: Pricing Matrix

9 live fields. AS-IS 4, DERIVED 0, INTERNAL 5.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Price Point | AS-IS | Per-person average by daypart and revenue center |  |
| Day of Week | AS-IS | Per-person average by daypart and revenue center |  |
| Day Part | INTERNAL | Relational link, not data |  |
| Menu | INTERNAL | Relational link, not data |  |
| Revenue Center | INTERNAL | Relational link, not data |  |
| PPA | AS-IS | Per-person average by daypart and revenue center |  |
| Active | AS-IS | Per-person average by daypart and revenue center |  |
| Notes | INTERNAL | Working commentary |  |
| Revenue Projections | INTERNAL | Relational link, not data |  |

## Reference: Seating & Capacity

13 live fields. AS-IS 9, DERIVED 2, INTERNAL 2.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Capacity Config | DERIVED | Concatenated label; ships restated |  |
| Total Seats | AS-IS | Physical capacity constraint |  |
| Indoor Seats | AS-IS | Physical capacity constraint |  |
| Outdoor Seats | AS-IS | Physical capacity constraint |  |
| Indoor:Outdoor Ratio | AS-IS | Physical capacity constraint |  |
| Patio Weather Factor % | DERIVED | Weather derate exists but is not visible in the revenue build | * |
| Notes | INTERNAL | Working commentary |  |
| Revenue Center | INTERNAL | Relational link, not data |  |
| 2-Top Ratio | AS-IS | Physical capacity constraint |  |
| Total Tables | AS-IS | Physical capacity constraint |  |
| 2-Top Count | AS-IS | Physical capacity constraint |  |
| 4-Top Count | AS-IS | Physical capacity constraint |  |
| Actual Seats | AS-IS | Physical capacity constraint |  |

## Labor: Positions

27 live fields. AS-IS 4, DERIVED 14, INTERNAL 9.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Task ID | INTERNAL | Internal record key |  |
| Position | DERIVED | Role names; ship as an org summary, not a roster |  |
| Hiring Phase | INTERNAL | Hiring sequence; exposes which seats are unfilled | * |
| Department | DERIVED | Position-level wage build; ships as summarised labor lines |  |
| Day Part | DERIVED | Position-level wage build; ships as summarised labor lines |  |
| Role Level (drop down) | DERIVED | Position-level wage build; ships as summarised labor lines |  |
| 👥Headcount | DERIVED | Headcount by role; ships as a total |  |
| Labor Models | INTERNAL | Relational link, not data |  |
| Training Wage | DERIVED | Position-level wage build; ships as summarised labor lines |  |
| Training Days | DERIVED | Position-level wage build; ships as summarised labor lines |  |
| Pre Opening Wages | DERIVED | Position-level wage build; ships as summarised labor lines |  |
| 💰 Hourly Wage | DERIVED | Wage by role; ships as blended labor cost |  |
| Compensation Type | DERIVED | Position-level wage build; ships as summarised labor lines |  |
| Annual Position Wages (50W) | DERIVED | Position-level wage build; ships as summarised labor lines |  |
| Points | INTERNAL | No-tipping point-pool mechanic, not yet legally reviewed | * |
| Staffing Model | INTERNAL | Relational link, not data |  |
| Covers per Staff | DERIVED | Position-level wage build; ships as summarised labor lines |  |
| Operating Salaried Weekly | DERIVED | Position-level wage build; ships as summarised labor lines |  |
| Full Cost Salaried Weekly | DERIVED | Position-level wage build; ships as summarised labor lines |  |
| Hire Week | INTERNAL | Hiring sequence; exposes which seats are unfilled | * |
| Pre-Opening Notes | INTERNAL | Working commentary on hiring |  |
| Manual sort | INTERNAL | Airtable sort control, not data |  |
| Labor: BOH Shift Build | INTERNAL | Relational link, not data |  |
| Cost Classification | AS-IS | Four-wall versus corporate split, the basis of the G&A layer |  |
| Corporate Allocation % | AS-IS | Share of a seat charged to corporate |  |
| Corporate Compensation (Annual) | AS-IS | Corporate compensation feeding Corporate G&A |  |
| Corporate Headcount (Allocated) | AS-IS | Allocated corporate headcount |  |

## Reference: Labor Models

7 live fields. AS-IS 0, DERIVED 5, INTERNAL 2.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Summary Name | DERIVED | Salaried rollup feeding the labor line |  |
| Positions | INTERNAL | Relational link, not data |  |
| P&L Model | INTERNAL | Relational link, not data |  |
| Total Operating Salary | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Total Full Cost Salaried | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Corporate Compensation (Annual) | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Corporate Headcount (Allocated) | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |

## Reference: Staffing Model

24 live fields. AS-IS 0, DERIVED 14, INTERNAL 10.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Assignment ID | INTERNAL | Internal record key |  |
| Headcount | DERIVED | Shift assignment build behind labor cost |  |
| Hours Worked | DERIVED | Shift assignment build behind labor cost |  |
| Positions (Synced) | INTERNAL | Relational link, not data |  |
| Service Schedule | INTERNAL | Relational link, not data |  |
| Hourly Wage | DERIVED | Lookup of an upstream value; ships through its source |  |
| Day Cost | DERIVED | Shift assignment build behind labor cost |  |
| Service Revenue | DERIVED | Lookup of an upstream value; ships through its source |  |
| Position Labor % | DERIVED | Shift assignment build behind labor cost |  |
| Points | INTERNAL | No-tipping point-pool mechanic, not yet legally reviewed | * |
| Total Points | DERIVED | Shift assignment build behind labor cost |  |
| Point Value | INTERNAL | No-tipping point-pool mechanic, not yet legally reviewed | * |
| Position Pool Share | INTERNAL | No-tipping point-pool mechanic, not yet legally reviewed | * |
| Bonus Per Person | INTERNAL | No-tipping point-pool mechanic, not yet legally reviewed | * |
| Effective Hourly | INTERNAL | Effective pay under the unreviewed no-tipping model | * |
| Points Override | INTERNAL | No-tipping point-pool mechanic, not yet legally reviewed | * |
| Effective Points | INTERNAL | No-tipping point-pool mechanic, not yet legally reviewed | * |
| Service Peak Covers | DERIVED | Lookup of an upstream value; ships through its source |  |
| Covers per Staff | DERIVED | Lookup of an upstream value; ships through its source |  |
| Target Headcount | DERIVED | Shift assignment build behind labor cost |  |
| Headcount Override | DERIVED | Shift assignment build behind labor cost |  |
| Effective Headcount | DERIVED | Shift assignment build behind labor cost |  |
| Cost Classification | DERIVED | Lookup of an upstream value; ships through its source |  |
| Corporate Allocation % | DERIVED | Lookup of an upstream value; ships through its source |  |

## Restaurant Configurator

29 live fields. AS-IS 6, DERIVED 7, INTERNAL 16.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Name | AS-IS | Daypart and revenue-center names; already neutral, no code names present |  |
| Type | INTERNAL | Internal record taxonomy |  |
| Active | INTERNAL | Internal on/off state |  |
| Display Order | INTERNAL | Airtable sort control, not data |  |
| Notes | INTERNAL | Working commentary |  |
| Service Schedule | INTERNAL | Relational link, not data |  |
| Pricing Matrix | INTERNAL | Relational link, not data |  |
| Pricing Matrix 2 | INTERNAL | Relational link, not data |  |
| Pricing Matrix 3 | INTERNAL | Relational link, not data |  |
| Revenue Projections | INTERNAL | Relational link, not data |  |
| Revenue Projections 2 | INTERNAL | Relational link, not data |  |
| Strategic Context | DERIVED | Positioning commentary; ships rewritten in House voice |  |
| Comparison | INTERNAL | Names local operators as revenue comparables | * |
| Comp Annual Revenue | INTERNAL | Unsourced revenue attributed to named local businesses | * |
| Quality | DERIVED | Positioning commentary; ships rewritten in House voice |  |
| Hospitality | DERIVED | Positioning commentary; ships rewritten in House voice |  |
| Value | DERIVED | Positioning commentary; ships rewritten in House voice |  |
| Seating & Capacity | INTERNAL | Relational link, not data |  |
| Total Seats (from Seating & Capacity) | AS-IS | Seats by revenue center |  |
| Standing Capacity | AS-IS | Patio standing places, part of the capacity picture |  |
| Daypart Weekly Revenue | AS-IS | Revenue by daypart, the multi-daypart proof |  |
| Daypart Weekly FOH Labor | AS-IS | Front-of-house labor by daypart |  |
| Daypart Weekly BOH Labor | AS-IS | Kitchen labor by daypart, the shared-crew proof |  |
| Scenario Timeline | INTERNAL | Relational link, not data |  |
| Labor: BOH Shift Build | INTERNAL | Relational link, not data |  |
| Scenario Configurator | INTERNAL | Relational link, not data |  |
| BOH Rate Derivation Revenue (Weekly) | DERIVED | Intermediate used to derive the BOH rate |  |
| BOH Rate Derivation Cost (Weekly) | DERIVED | Intermediate used to derive the BOH rate |  |
| BOH Rate Basis Check | DERIVED | Internal reconciliation check |  |

## Seasonal Factors

16 live fields. AS-IS 3, DERIVED 8, INTERNAL 5.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Month Summary | DERIVED | Concatenated label |  |
| Month | AS-IS | Calendar month |  |
| Days in Month | AS-IS | Days per month |  |
| Scale Factor % | AS-IS | Monthly seasonality index |  |
| Display Order | INTERNAL | Airtable sort control, not data |  |
| Pro Forma Model | INTERNAL | Relational link, not data |  |
| Linked Weekly Revenue | DERIVED | Lookup of an upstream value; ships through its source |  |
| Baseline Mth Rev | DERIVED | Monthly seasonality layer applied to the revenue spine |  |
| Adjusted Wk Rev | DERIVED | Monthly seasonality layer applied to the revenue spine |  |
| Wk Rev Adjust | DERIVED | Monthly seasonality layer applied to the revenue spine |  |
| Adjusted Mth Rev | DERIVED | Monthly seasonality layer applied to the revenue spine |  |
| Mth Rev Adjustment | DERIVED | Monthly seasonality layer applied to the revenue spine |  |
| Notes | INTERNAL | Working commentary |  |
| Key Events | DERIVED | Austin demand calendar; ships restated |  |
| Revenue Strategy & Context | INTERNAL | Internal strategy commentary |  |
| Monthly Projections | INTERNAL | Relational link, not data |  |

## Market Conditions Profile

14 live fields. AS-IS 4, DERIVED 7, INTERNAL 3.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Scenario | AS-IS | Scenario profile label |  |
| Description | DERIVED | Scenario description; ships rewritten |  |
| Revenue Adjustment % | AS-IS | Scenario revenue adjustment, a headline scenario input |  |
| COGS Adjustment % | AS-IS | Scenario COGS adjustment, a headline scenario input |  |
| Labor Adjustment % | AS-IS | Scenario labor adjustment, a headline scenario input |  |
| Adjusted Revenue | DERIVED | Scenario adjustment set behind Downside and Best Case |  |
| Adjusted COGS | DERIVED | Scenario adjustment set behind Downside and Best Case |  |
| Weekly Totals | INTERNAL | Relational link, not data |  |
| Base Revenue | DERIVED | Lookup of an upstream value; ships through its source |  |
| Base COGs | DERIVED | Lookup of an upstream value; ships through its source |  |
| Base Occupancy | DERIVED | Lookup of an upstream value; ships through its source |  |
| Base OpEx | DERIVED | Lookup of an upstream value; ships through its source |  |
| Profile Type | INTERNAL | Internal record taxonomy |  |
| Scenario Configurator | INTERNAL | Relational link, not data |  |

## Scenario Timeline

25 live fields. AS-IS 8, DERIVED 10, INTERNAL 7.

| Field | Class | Reason | F |
| --- | --- | --- | --- |
| Timeline ID | INTERNAL | Internal record key |  |
| Notes | INTERNAL | Working commentary |  |
| Month Number | AS-IS | Operating month |  |
| Calendar Month | AS-IS | Calendar month |  |
| Early Morning Active | AS-IS | Daypart phase-in flag |  |
| Brunch Active | AS-IS | Daypart phase-in flag |  |
| Lunch Model legacy. don't use | INTERNAL | Field name declares itself retired but carries no DELETE prefix | * |
| Dinner Active | AS-IS | Daypart phase-in flag |  |
| Dinner Days | AS-IS | Dinner days per week by month |  |
| Late Night Active | AS-IS | Daypart phase-in flag |  |
| Scenario | INTERNAL | Internal scenario label, inconsistent with Scenario Configurator naming | * |
| Lunch Model | INTERNAL | Relational link, not data |  |
| Lunch Weekly Revenue | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Lunch Weekly Labor | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Lunch Weekly Contribution | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Lunch Weekly Covers | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Lunch Contribution % | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Lunch Days Per Week | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Lunch Labor % | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Monthly Projections | INTERNAL | Relational link, not data |  |
| Capacity Utilization % | AS-IS | Monthly ramp curve, the opening-year story |  |
| Active Dayparts | INTERNAL | Relational link, not data |  |
| Active Weekly Revenue | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Active Weekly FOH Labor | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
| Active Weekly BOH Labor | DERIVED | Rollup of upstream values; ships as the aggregated figure |  |
