# 4.6 Team-building complexities: what the book says

Claire Hughes Johnson, *Scaling People*, Chapter 4, pp. 331 to 353. Full text: `extraction/build/s11/book.md`. This file is a quick reference; nothing here is about Sŏn.

## Managing distributed and remote teams

Being distributed is now the nature of a modern company: global ambitions, offices in multiple countries, and remote work accelerated by Covid-19. Stripe has had remote employees since its early years. Managing distributed teams poses three main challenges (p. 332):

- **Coordination.** People must be more diligent about what gets documented, how decisions are made, and where discussions happen, because colleagues sit in different places and time zones. It is tempting to assign remote employees isolated, independent work, but that only isolates the team further and weakens its coordination muscle (pp. 332 to 333).
- **Cohesion.** Out of sight becomes out of mind. Without deliberate work, teams default to siloed pockets, or co-located members dominate decisions and the best assignments. The fix is consistent communication and operating practices that put everyone on a level playing field, plus a cultural norm that any informal conversation that turns into a work discussion moves to a channel everyone can see, such as Slack (pp. 334 to 335).
- **Participation.** Some barriers are obvious (hard to chime in on a call, meetings at midnight in your time zone) and easier to design around: an active moderator, rotating meeting times. Less obvious barriers, like missing the dynamic in a room or missing casual meals, do more damage. A culture of documenting what happens in every meeting helps close the gap (pp. 335 to 336).

A sidebar (pp. 333 to 334) gives a real example from a Stripe engineer in Dublin who lost three days waiting on US-hours approvals for the wrong access group, twice. The lesson: build self-service access to most systems, and build mechanisms that unblock people across time zones without breaking security.

Table 9 (pp. 336 to 337) maps which challenge dominates by team shape: a few remote people on an otherwise centralized team face a participation problem; a whole team that is remote but reports to one manager without being a real team faces a cohesion problem; a team split across offices and remote locations faces a coordination problem; a fully remote company faces coordination and cohesion but less participation pressure, since everyone is in the same boat.

Mitigations that apply across all three challenges, weighted by which one bites hardest (p. 337):

- Set structures and norms for inclusive meetings: video links, attention to acoustics, active facilitation, and notes.
- Level the playing field: shared Slack channels instead of hallway conversations, and strong internal documentation.
- Make room for in-person time, budgeted at the right frequency.

On leveling the playing field, her worked example (pp. 338 to 339) walks through a remote employee's disadvantaged experience in a single meeting: missing videoconferencing links, missing hallway context from an office lunch, unable to hear a debate over a bad connection. Automattic's answer is that everyone dials into calls from a separate location, even when some people happen to be in the same building, so no one experiences being the lone remote voice; it also gathers everyone in person at least once a year.

On in-person time (pp. 339 to 340), she argues she has not found a substitute for quality in-person time on a regular cadence, valuable for two things: spontaneous social connection beyond the professional, and getting people out of day-to-day operating rhythms so they can reach a level of alignment a 45-minute meeting cannot produce. Her own example is a distributed revenue leadership group that met quarterly in San Francisco for two-day working offsites plus a team social event.

Cadence guidance (pp. 340 to 341): meet at least quarterly when a remote team is first forming; space out toward biannual once the team has banked a couple of solid in-person interactions, though growing teams should keep the quarterly cadence longer. Aim for in person even through disruptions like a pandemic; half-day virtual offsites are the fallback, not the plan.

## Going global

A global company is not the same work done in different countries (pp. 341 to 342). Leading over 2,000 people in 16 offices at Google taught her that cultural differences and local strategic needs are real, even when user needs turn out to be similar across countries; she points to Geert Hofstede's work on the dimensions of national culture as a useful map. There are also ecosystem and landscape differences: developer community size, local competitors, consumer expectations. She recommends a team exercise that reviews the cultural dimensions of the business and discusses the implications for day-to-day work, including for local teams balancing local norms against company norms (pp. 341 to 342). Her Stripe example: a cultural-comparison exercise with country leads showed Stripe is not a mirror of American culture, since its founders are Irish, which she read as an opportunity to build a shared global identity while still leaving room for local variation in practices like after-hours socializing (p. 342).

## Adding remote workers

Four things to weigh before adding remote team members (pp. 342 to 344):

- **Maturity of your operating system.** A strong operating system and cadence, good asynchronous norms (recorded meetings, strong notes), make a team more ready to absorb remote members.
- **Role.** Roles with heavy coordination needs, like engineering, product, and design, are more sensitive to how a remote or hybrid team is structured than roles that can run more independently, like legal or finance. A team split evenly across locations can coordinate more easily than one where most, but not all, members are co-located.
- **Manager support.** Remote management is its own skill. Stripe once required remote employees to have remote managers, on the theory that a remote manager has more empathy for the remote experience; it now trains any manager to do this well, while keeping that intention. Concrete practices: a team Slack channel, a norm that side conversations get documented, availability outside in-person channels, and structured touchpoints like 1:1s and snippets docs.
- **Experience level.** People who have already worked remotely adjust faster; new graduates need more support to learn both the job and how to work remotely at the same time.

Her closing counsel (pp. 344 to 345): build documentation, norms, and practices for distributed work in from day one, understand the national cultures on your team, try being remote yourself for a stretch, and use engagement survey feedback to check how connected and productive remote employees actually feel.

## Underperforming teams

Sometimes a team that looks well built still falters on its goals and metrics for weeks running, with explanations that never quite satisfy (pp. 345 to 346). Her course-correction sequence:

1. **Investigate the root cause with probing questions.** Test a hypothesis in 1:1s, aimed at the work rather than at a person, for example whether a dependency is the real bottleneck.
2. **Have an open, curious conversation in the team meeting**, not an accusatory one. Ask: why do you think we're behind (without going easy if the goal itself was wrong); do these reasons feel in or out of our control (usually more in the team's control than people think); what can we do now, with clear ownership; and how much impact do the truly external reasons have, and what could reduce them (pp. 345 to 346).

If the goal itself was wrong: agree as a team to adjust it, document the original goal, what changed, and why, and be transparent with stakeholders about the reset and what you learned (p. 346).

If the issue is skills or collaboration: keep building the hypothesis with data. An individual performance issue goes to the Chapter 5 feedback guidance. A collaboration issue between two or more people calls for separate conversations, then a joint one, with each person sharing nonjudgmental feedback on work style, staying neutral, and, if nothing improves, considering moving one or both people to another team (pp. 346 to 347).

If the friction is systemic across the group: don't ignore it. Have a neutral party, such as HR, interview team members the way a 360 review would, write up a summary, and hold a session on what everyone will do differently. Most friction traces back to a lack of mutual self-awareness (Operating Principle 1), so return to personality and work style assessments (p. 347).

Missing a goal often traces to a dependency on another team, more so as scope and company size grow. The manager's job is to anticipate dependencies, negotiate, resolve issues as they occur, and escalate to the relevant leaders when needed; she describes her own job as clearing the path her team needs to travel (pp. 347 to 348).

### Working with other teams

A short guide to de-risking cross-team dependencies (pp. 348 to 349):

- Identify dependencies during planning: for every goal, name what you need from whom by when, and align with the other team before they finalize their plan. Escalate disagreements to the shared decision-maker.
- Set up a semi-regular check-in, starting with an email and escalating to a meeting if things drift.
- Embed a representative from the dependent team in your meetings, and send one to theirs.
- Form a temporary working group with its own shared goals, metrics, and a DRI, when the dependency is substantial (see her Table 6, p. 265, on working groups versus teams).

If an impasse remains despite de-risking, escalate constructively. Asking for help is not a failure; escalation paths exist precisely for this. The failure modes run both ways: a hair-trigger escalator looks ineffective and becomes unpopular, but so does someone who lets their team stay stuck rather than escalate (p. 349). Stripe's own unblocking process is reproduced in the chapter's exercises (p. 343 in her text, appended below). It is also worth stepping back to ask whether a different strategy, architecture, org structure, or set of priorities could remove the dependency altogether (pp. 349 to 350).

## Managing through uncertainty

When something is not working, the team feels it. She leans on Rebecca Solnit: authentic hope requires clarity and imagination, meaning management (clarity) and leadership (imagination) both have work to do (p. 350). Her approach to supporting a team through uncertainty:

- **Be transparent, to a point.** The more common failure is a manager who does not acknowledge the challenge or pretends to have it all figured out, which erodes trust exactly when the team needs the manager most. Openness does not mean pessimism; it means an honest, objective read, such as naming that the deadlines are unrealistic or that a plan is not yet in place (pp. 350 to 351).
- **Reiterate the vision.** Uncertainty does not mean the vision is wrong. Retell the story of why the work matters and how the future improves because of it (p. 351).
- **Move forward.** Bias toward action rather than a perfect plan; small decisions and small actions, communicated openly, beat overanalysis (p. 351).

Her Covid-19 example (pp. 351 to 352): with incomplete data and no detailed plan, Stripe still acted, moving part of the leadership team and some critical teams remote in February 2020, and then communicated every subsequent decision methodically, guided by two stated priorities: serving customers and protecting employee health and safety.

A sidebar (pp. 352 to 354) carries a Reid Hoffman account of steering LinkedIn through the 2007 launch of the Facebook Platform, treated as a case study in managing a perceived existential threat: building a fast, cheap test (three teams, eight weeks, three apps) to learn whether the threat was real before reacting further, then a follow-up test (one team, one unrelated app) to separate the platform's actual potential from any dependency on LinkedIn-specific knowledge. In hindsight the crisis wasn't much of one, but getting to that confidence required admitting what wasn't yet known and building a plan to find out.

## Exercises and templates

See `extraction/build/s11/exercises.md` for full text.

**Career conversations (pp. 364 to 367).** A 60-minute 1:1 (30 to 45 minutes for a recent graduate) that walks a report's life and career history: childhood and schooling, choices right after school, favorite and least favorite jobs and why, and a forward-looking projection of the kind of work and life they want in five years, without pinning it to a title. Comes with a pre-conversation script for introducing the exercise, a reminder script sent the day before, guidance to actively listen and keep asking why, and a wrap-up that recaps and sets two or three development goals.

**Planning and running your offsite (pp. 367 to 370).** A checklist by time horizon (1+ month, 1 month, 1 week, 1 day, day of, after) covering goals, scheduling, agenda-building with a DRI per section, logistics, and post-offsite notes and feedback. A day-of structure (welcome, check-in, icebreaker, sessions, check-out) and a sample welcome email and agenda table are included.

**Leadership team snippets and updates (pp. 370 to 372).** A weekly template due the Sunday night before the meeting: actions, discussion topics with time allocations, standing questions (QBR reflections, what to pass down, any objections to passing something down, decisions made), customer issues and wins, and a snippets section per executive covering action updates, whereabouts, topics for discussion, and notable customer or talent information.

**Stripe's unblocking process (pp. 372 to 377).** A process for when two parties cannot agree on a reversible-enough-to-matter, hard-to-reverse decision after trying to solve it locally. Steps: write a short joint document (the problem in the user's voice, the options, the unresolved trade-offs); if that doesn't resolve it, send it to both managers, who either decide or escalate up the management chain; the process can be triggered unilaterally if one party refuses to participate, with the other party copied; and managers are expected to refuse to hear a unilateral complaint until the complaining party has tried negotiation and the joint document first. A worked fictional example (storage encryption at rest between two teams) shows the document and the escalation to a shared manager.
