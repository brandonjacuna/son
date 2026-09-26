# Book exercises and templates relevant to session 3

Verbatim text from `sources/scaling-people-book.pdf` via PyMuPDF. Page markers `[p.N]` are PDF page numbers (zero offset).

[p.148]
Team Charter
Mission
Example:
Provide best-in-class security to all of our users and their accounts on the
dashboard. This encompasses both authentication and authorization,
including dashboard roles and permissioning.
Vision
Example:
We aim to build strong trust internally and externally in our ability to provide
best-in-class security for all of our users, from enterprises to small users,
while avoiding overhead for our users and support team. Account takeovers
will no longer be an active problem (neither as a terrible user experience
nor as a financial loss). While we won’t ever be able to get them to zero, we
and our customers should have full faith that when they occur (e.g., through
an internal bad actor on the customer side), we did everything within
creative reasonability to prevent them. We will also deliver “table-stakes”
security features such that we fly through user security–related discussions
with new enterprise customers.
Customers
Example:
We’re responsible for the account security of every user and account,
ensuring that their accounts and the sensitive data therein remain theirs
alone.
We protect the interests of all merchant accounts by enabling them to
control who in their business can access what, and by protecting them from
rogue actions.
Metrics

[p.149]
Example:
Number of accounts that have experienced a takeover in a given month
Measuring: User experience, risk of unhappy customer leak, support
burden
Target value: [X]
Account takeover losses
Measuring: Direct financial loss and loss of margin due to account
security issues
Target value: [X]
Percentage of all dashboard users who have adopted two-factor
authentication
Measuring: Protection of entire user base from account takeovers
Target value: [X]
Strategic importance
Example:
Aside from the financial benefits of reducing losses, having better account
security will improve the user experience and build user trust. Strong
foundations here will help prevent attacks, bad user experiences, and
losses, since we will become a target if we are not world-class. A strong
track record will also increase the appeal of our products to enterprise
users, open up new sales conversations, and accelerate existing ones.
Major risks
Example:
Team gets pulled into lower-priority work by audit or compliance
activities
Major security breach
Major new attack vectors

[p.150]
Death by a thousand cuts of one-off enterprise requests
Tech debt
Provided interfaces
Example:
Login code
2FA infrastructure
Session infrastructure
Login/email challenge
Dashboard auditing models
Account recovery/password reset flow
Dependent interfaces
Example:
User registration UI
Verificator (interface for SMS 2FA)
User email system and team
Organizational Foundations
To test whether you have a clear operating system, fill out the table below. How
easily can you complete it for an individual report on your team, for one of your
teams, and for your division? Is this information documented anywhere in your
division, and is it easy to find? If you’re having trouble filling out this template,
imagine how your teams and reports must feel!
This information should be documented and easily accessible on your team’s
and division’s internal homepages. On those same pages or at the top of your

[p.151]
□
□
□
internal dashboard, if separate, be sure to include similar detail about your top
objectives and metrics with targets for the year. (See the next template.)
Individual
Team
Division
Mission
Objectives with owner (DRI)
Key metrics
Accountability mechanisms
Operating cadence
Objectives and Metrics
Checklist
It’s worthwhile to scrutinize any documented objective for clarity and alignment
with the team’s or division’s mission and plan to contribute to company success.
You can use the following template to do so.
Objective
Metric
Baseline
Target
Are your objectives:
Inspirational?
Actionable by your team?
Related to your team’s mission and vision?

[p.152]
□
□
□
□
□
□
□
□
□
□
□
□
Related to the company’s priorities and goals?
Are the objectives SMART?
Specific
Measurable
Achievable
Results-oriented
Targeted
Also check:
Is the metric a leading indicator?
Does it have counterweight metrics? (For example, you could increase the
number of users by giving away the product for free, but you don’t want to
do that! So if you have a user metric, what is your counterweight revenue
metric?)
Is there a framework to evaluate the metric (e.g., a calculation or a query)?
Does the metric have an owner?
Is the metric relative, not absolute? (For example, instead of “Increase the
number of users by 1,000,” explain the relative growth: “Increase the
number of users by 20 percent, from 5,000 to 6,000.”)
Does it take into account your existing user growth? (For example, you
might be able to hit your revenue target just through growth from existing
users, but then you haven’t done anything to earn that growth.)
Writing Good OKRs

[p.153]
This guide was written by Stripes on our finance and tech enablement teams in
collaboration with our CTO, David Singleton.
The basics
Write: Note the top-level 3–5 objectives, with 1–5 key results per objective, that
you’re committed to accomplishing in the quarter. Identify which are must-hit
goals. (See the next section for guidance.)
Collaborate: If you partner closely with other functions or teams, get feedback
and make sure you agree on the OKRs you’ve set.
Publish: When you’re done, change “Draft” to “On track” in the document title to
signal that your OKRs are published (on the company intranet or other
document-sharing method) and in progress.
Guidance on ambition
Most goals should be ambitious yet attainable. This means we expect to
achieve the vast majority of them over time, while also recognizing that some
will be a stretch. Overall, we should expect to score in the 70–80 percent range
over the quarter.
A small number of our goals (20–30 percent for any given team in a quarter)
might be hard commitments. These should be marked as “must-hit,” and we
expect to reach 95 percent attainment or more. If these goals are trending
behind, we expect to sacrifice other goals in service of hitting them.
Good OKRs start with good objectives
Best practices for good objectives
Objectives are clearly defined goals that answer the question “Where do I
want to go?”
Objectives should be an outcome—a description of the state of the world at
the end of the quarter. They should focus on the user problem you’re
solving.
Objectives should be focused on the most important work. There should be
no more than 3–5 of them.

[p.154]
Objectives chart intent and direction—they chart outcomes.
Objectives are long-term and often span several quarters, even years.
Objectives nest up and down to some degree in an organization.
Objectives should be ambitious and can be open to (some) interpretation
and debate.
Objectives can be aspirational (70 percent) or committed (100 percent).
Identify which are which!
All objectives should matter. The best objectives are inspirational.
Objectives can be shared across teams.
Define key results
Best practices for good key results
Key results are concrete definitions of success. Each one determines
whether the objective has been achieved or not and answers the question
“How will I pace myself to see if I’m on track?”
Key results should list outcomes, not activities. There should be 1–5 key
results per objective.
Key results are measurable and binary: Either they did or didn’t happen.
They’re not open to interpretation.
Key results flow from a theory of a plausible causal mechanism that
connects the key result with the objective and with your own work.
Key results build a shared model of reality across teams and organizations.
Key results should compound over time, if possible.
Common pitfalls when formulating OKRs
Using an activity or action as an outcome.
Having a key result that can’t be measured in some way.

[p.155]
Turning a roadmap directly into objectives and key results.
Writing more than 3–5 objectives, or 1–5 key results per objective.
Iterating and Scoring
Mid-quarter scoring
At some point in the quarter, the team should get together to discuss progress
to date and give it an approximate score. The easiest way to do this is a simple
green, yellow, and red rubric accompanied by an assessment of on track, off
track, or at risk. (If your team prefers to use percentage-based scoring, do
what works best.) Items that are off track or at risk should be discussed further
so that the team can find ways to redirect their energy and build in time to
recover.
How to handle changes in information and
priorities
If new information arises that changes an objective or key result, there should
be some common practices to track and handle the changes. This could mean
scoring an OKR lower or swapping it out. Do whatever makes sense for the
team, but be consistent and clear. Most importantly, communicate changes to
any impacted teams, and clearly document what’s changed and why.
Here’s some general guidance:
If you add or drop a key result, document the decision and notify impacted
teams.
If you add an objective (e.g., due to an urgent shift in the world), document
whether it resulted in deprioritizing existing work and, if so, what work was
deprioritized.
Dropping an objective should be rare. This may happen due to a change in
constraints or because it truly isn’t providing value to users. In these cases,
