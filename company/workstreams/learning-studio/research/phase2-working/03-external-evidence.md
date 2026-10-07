<!-- Phase 2 working output, run wf_c7d3565a-a0f, 2026-09-28. Raw agent return, not reviewed line by line. The synthesis is research/starting-structure-2026-09.md. -->

## Box sources found (user request)

- **White paper:** Box folder `00. Pitch Materials` (`388972799337`), then `White Paper` (`382453064958`), then file **`2466517057642`**, "Sŏn Investor White Paper Sept 2026.pdf", modified 2026-09-14. The sections relevant here are cited by label below. Nothing from the paper is restated. **Lineage flag for Brandon:** the paper's opening narrative (pp. 1-2) names Gracious, Coqodaq and Cote. This research uses none of it.
- **Brand Guidelines:** Box has more than one version, and none is marked canonical:
  - `2281626080747`, "Brand and Experiential Guidelines PDF", in `Sŏn / 10. AI Projects / Design`, dated 2026-06-12.
  - `2356731001214`, "Son Brand Guidelines v1 (1).md", in `Design / v2.1-2026-07-19-defect-fix / uploads`. This is the latest.
  - Older copies: `2356714319901` (v2) and `2281555280952` (v1.0).
  - The folder `05. Brand and Creative / Identity and Design Assets` (`420132746170`) is empty.
  - **Flag:** CLAUDE.md names a ClickUp doc as canon, but this task allows Box only. Which Box file is canonical needs Brandon's confirmation.
  - Sections relevant to training, cited from `2356731001214`: §01 Brand Foundation (Service Philosophy, Company Non-Negotiables), §08 Service Model (Step-Back Architecture, Arrival Choreography, Key Protocols), §09 Verbal Identity.

**Status key:**
- **VP**: verified-primary. I read the original's abstract at the source, through the publisher, Europe PMC or Crossref. "VP-full" means I read the full-text opening.
- **VS**: verified-secondary.
- **LO**: lead-only.
- **UV**: unverified.

---

## 1. Module length and microlearning

**Verdict:** No evidence shows that short is better in itself. The gains credited to "microlearning" come from spacing, retrieval, a single objective per unit, and learner-paced segmenting. Size each unit to one objective and one learning job. Where the benefit comes from is spreading units out and making people retrieve.
**Strength:** Weak and poorly defined for microlearning as a category. Strong for the mechanisms underneath it.

- De Gagne et al. 2019, *JMIR Med Educ*, scoping review. [VP]
  - Microlearning is "difficult to define."
  - Studies mostly measured reactions and knowledge. Few measured behavior, and none measured results.
  - https://mededu.jmir.org/2019/2/e13997/
- Monib, Qazi & Apong 2024, *Heliyon*, systematic review. [VP]
  - Reports positive outcomes, but states that "a largely agreed definition does not yet exist."
  - Only covered 2020 to 2024. Outcomes are mostly short-window.
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11774797/
- Rey et al. 2019, *Educ Psychol Rev*, meta-analysis of the segmenting effect. [VP]
  - Learner-paced, meaningful segments beat continuous presentation for retention and transfer. Effect is small to medium, and segmenting lowers cognitive load.
  - Learners with more prior knowledge benefited more.
  - This is about segmenting within a lesson. It is not evidence that short standalone modules are better.
  - https://eric.ed.gov/?id=EJ1217373
- **Hype markers:**
  - The "human attention span is shorter than a goldfish" claim has no traceable research source. [LO: secondary debunks, e.g. https://thewell.northwell.edu/brain-nerve-health/attention-span-goldfish-myth. I did not read the original BBC trace.]
  - Efficiency and engagement percentages credited to the *Journal of Applied Psychology* circulate on vendor pages (e.g. https://www.shiftelearning.com/blog/numbers-dont-lie-why-bite-sized-learning-is-better-for-your-learners-and-you-too) with no citable article. [LO, treat as UV]
  - Rule: never cite a microlearning percentage.
- **For Sŏn:** Brandon's rule fits the evidence: lean on the critical path, long-form allowed off it. Masterclass audio can run long as optional material. Critical-path units need one objective plus retrieval, with review scheduled later.

## 2. Spacing, retrieval and interleaving across shifts

**Verdict:** Spaced retrieval is the most reliable lever available to Sŏn.
- The right gap between reviews grows with how long the knowledge must last.
- Retrieval beats re-reading.
- Interleaving helps people tell similar categories apart, especially visual ones. It is unproven for tastes and for text.

**Strength:** Strong and replicated for spacing and retrieval. Moderate and conditional for interleaving.

- Cepeda et al. 2006, *Psych Bull*, meta-analysis of distributed practice. [VP] https://digitalcommons.usf.edu/psy_facpub/1771/
  - The gap between study sessions and the retention interval work together. The best gap gets longer as the retention interval gets longer.
- Cepeda et al. 2008, *Psych Sci*, "temporal ridgeline." [VS, search abstract] https://laplab.ucsd.edu/articles/Cepeda%20et%20al%202008_psychsci.pdf
  - The best gap is a shrinking share of the retention interval as that interval grows.
  - Gaps that are too short or too long both cost retention.
- Adesope, Trevisan & Sundararajan 2017, *Rev Educ Res*, meta-analysis. [VP] https://eric.ed.gov/?id=EJ1141817
  - Practice tests beat restudy and every other comparison condition.
- Rawson & Dunlosky 2022, successive relearning. [VS] https://journals.sagepub.com/doi/full/10.1177/09637214221100484
  - Retrieve to criterion, then repeat across spaced sessions. This gives durable retention, and returns diminish after the first few relearning sessions.
- Kerfoot et al. 2007, *J Urol*, RCT with working residents. [VP] https://pubmed.ncbi.nlm.nih.gov/17382760/
  - A daily push of one or two spaced questions beat the same material delivered all at once, for both acquisition and retention.
  - This is the closest analog to shift workers. A follow-up reports the benefit persisting long-term. [VS] https://www.auajournals.org/doi/10.1016/j.juro.2009.02.024
- Brunmair & Richter 2019, *Psych Bull*, meta-analysis of interleaving. [VP] https://pubmed.ncbi.nlm.nih.gov/31556629/
  - Moderate overall benefit, strongest for visual materials.
  - Ambiguous for expository text and **tastes**. Blocking beat interleaving for words.
  - Interleaving helps most when categories look alike to each other and items within a category vary.
- **For an hourly workforce:**
  - Anchor spacing to shifts, not the calendar. The learner's next shift is the review trigger: retrieval in pre-shift call-and-response, or a short retrieval set at clock-in.
  - Variable schedules mean gaps vary. The ridgeline shows performance is forgiving near the optimum and falls off at extremes, so cap the longest gap rather than chase an exact interval. (The cap is a bound workflow value.)
  - No study found tests spacing on irregular hourly shift patterns. That is inference.
  - Interleave near-miss visual discriminations (setup faults, plate readiness, glassware). Do not assume interleaving helps tasting until tested.

## 3. On-shift versus off-floor learning

**Verdict:**
- Off-floor time is for concepts and first practice.
- Structured on-floor practice with feedback is where transfer happens.
- The work environment decides whether training transfers, most of all for open, judgment-heavy skills, which is most of hospitality.

**Strength:** Strong for transfer climate. Moderate for structured OJT over unstructured. Principle-level for cognitive apprenticeship.

- Blume, Ford, Baldwin & Huang 2010, *J Management*, transfer meta-analysis. [VP-full] https://journals.sagepub.com/doi/10.1177/0149206309352880
  - A supportive work environment and motivation predict transfer.
  - Most predictors mattered more for **open** skills (latitude in how to act) than for closed skills (one right procedure).
  - When the same source rates both support and transfer at the same time, the relationship is consistently inflated. Do not measure transfer only by self-report.
- Salas et al. 2012, *PSPI*, "Science of training." [VS, ScienceDaily summary] https://www.sciencedaily.com/releases/2012/06/120613133148.htm
  - After training, people need ample chances to use the skill with real feedback.
  - Leaders must be aligned beforehand.
  - Errors during training and behavior modeling narrow the gap between training and the job.
- Structured OJT (Jacobs). [VS for direction, via Ahadi & Jacobs 2017 review: https://journals.sagepub.com/doi/10.1177/1534484317725945, abstract not reachable. LO for any magnitude.]
  - Planned OJT led by a trained trainer beat unstructured shadowing in efficiency. Turnover influenced the size of the benefit more than task difficulty did.
- Collins, Brown & Newman, cognitive apprenticeship. [VS] https://www.isls.org/research-topics/cognitive-apprenticeship/
  - Sequence: modeling, coaching, scaffolding and fading, then articulation, reflection and exploration.
  - A design framework, not an effect size.
- **For Sŏn:**
  - The white paper already rejects unstructured shadowing: `2466517057642`, Part II, "Training infrastructure", p.18.
  - Design on-floor learning as structured OJT: a named trainer, a written task breakdown, planned fading.
  - For open skills (reading a table, recovery), invest in the floor climate, meaning lead and peer support and a chance to use the skill in the next shift. More screen content will not substitute.

## 4. Separating physical movement from decisions

**Verdict:** Brandon's model is well supported, with conditions:
- Drill the recurrent, consistent motor parts (pour control, tray carry, stemware handling) separately until automatic.
- Then put them back into whole-task practice under realistic decision load.
- Practice across tempos, which is variable practice.
- Do not rely on random-versus-blocked scheduling for applied skills.

**Strength:** Moderate to strong for part-task training of recurrent components inside a whole-task design, and for distributed motor practice. Weak or null for scheduling tricks in applied settings. Contested for attentional focus. Small for mental practice.

- van Merriënboer's 4C/ID model. [VS] https://edutechwiki.unige.ch/en/4C-ID
  - Whole-task learning is the spine.
  - Part-task practice is reserved for **recurrent** constituent skills where automaticity is wanted.
  - This is Brandon's split in instructional-design terms.
- Wightman & Lintern 1985, *Human Factors*. [VS] https://journals.sagepub.com/doi/10.1177/001872088502700304
  - Part-task methods (segmentation, fractionation, simplification) need an explicit plan for putting the parts back into the whole.
- Wulf & Shea 2002, *Psychon Bull Rev*. [VP] https://pubmed.ncbi.nlm.nih.gov/12120783/
  - Findings from simple lab skills do not generalize to complex skills.
  - When demands are low, add challenge. When load is extreme, reduce it.
  - This supports isolating movements for novices, before load is added back.
- Czyż et al. 2024, *Sci Rep*, contextual interference meta-analysis. [VP] https://www.nature.com/articles/s41598-024-65753-3
  - Random practice helps retention in the lab. **In applied settings the benefit was almost negligible.**
  - Barreiros et al. 2007 reach the same direction. [VS]
- Moulton et al. 2006, *Ann Surg*, RCT. [VS] https://journals.lww.com/annalsofsurgery/abstract/2006/09000/teaching_surgical_skills__what_kind_of_practice.8.aspx
  - With equal total practice time, weekly sessions beat a single day for retention and transfer of a fine motor skill. This supports Brandon's short, repeated drills.
- Home practice:
  - Joosten et al. 2022, *Surg Endosc*, RCT. [VP, via PMC] https://pmc.ncbi.nlm.nih.gov/articles/PMC9125971
    - Skills decayed within months without practice. Continuous unsupervised home practice gave better retention.
  - Thinggaard et al. 2017, *Surg Endosc*, mixed methods. [VP] https://pubmed.ncbi.nlm.nih.gov/27515838/
    - Home practice was irregular and bunched at the start and end.
    - Required elements and tests set when people practiced. Self-rating guided practice where no feedback was available.
  - Brandon's water-pour kit therefore needs:
    - a self-check standard (a video exemplar and a self-rating),
    - a scheduled check-in,
    - a paid-time answer (HR-gated, because Brandon requires paid learning).
- Mental practice:
  - Driskell, Copper & Moran 1994, *JAP*. [VS] https://www.semanticscholar.org/paper/Does-mental-practice-enhance-performance-Driskell-Copper/a5011fa801a9fd7e446af1131c27b5aa0bffdbdc
    - Positive effect, moderated by task type and retention interval.
  - Toth et al. 2020 follow-up. [VS] https://pure.ul.ie/en/publications/does-mental-practice-still-enhance-performance-a-24-year-follow-u/
    - A small positive effect again.
  - That it helps more for tasks with more cognitive content is my recollection. [UV]
  - Use it as a supplement (for example, rehearsing the sequence before a shift), never as a replacement for physical reps.
- Deliberate practice:
  - Macnamara, Hambrick & Oswald 2014, *Psych Sci*. [VS] https://journals.sagepub.com/doi/abs/10.1177/0956797614535810
    - Practice matters, but it explains much less of performance in professions than in games and music.
    - Keep the method (a specific goal, immediate feedback, repetition at the edge of ability). Drop any "enough hours makes an expert" framing.
- Attentional focus (cue the effect, e.g. "keep the stream steady", rather than the body part):
  - Chua et al. 2021, *Psych Bull*, reports a benefit. [VS]
  - McKay et al. 2023, bias-corrected, finds effects small to nil. [VS, preprint] https://sportrxiv.org/index.php/server/preprint/view/304
  - Verdict: contested. External-focus cueing is harmless to use, but do not claim it as evidence-backed.

## 5. Conversational assessment

**Verdict:** Brandon's verbal knowledge gate and live practical can be valid and fair if they are **structured**:
- set cases,
- anchored rubrics,
- trained examiners,
- two raters, or enough separate cases, for any gate.

Unstructured conversation is where bias enters. The format matters less than how many cases are sampled and whether raters are calibrated.

**Strength:** Strong for the reliability conditions. Moderate for peer validity. Evidence on oral-exam bias exists and is serious.

- Wass et al. 2003, *Med Educ*, structured orals (RCGP). [VP] https://pubmed.ncbi.nlm.nih.gov/12694283/
  - Structured orals can reach reliability fit for a high-stakes exam "if sufficient resources are available."
  - The topic sampled and the examiner each drove a large share of score variance. More cases and examiner pairs raise reliability.
- Brannick, Erol-Korkmaz & Prewett 2011, *Med Educ*, OSCE reliability meta-analysis. [VP] https://pubmed.ncbi.nlm.nih.gov/21988659/
  - Overall OSCE scores "are often not very reliable."
  - More stations and two examiners per station help.
  - Communication skills are harder to assess reliably across situations than technical skills.
- Kogan, Holmboe & Hauer 2009, *JAMA*, direct-observation tools. [VP] https://pubmed.ncbi.nlm.nih.gov/19773567/
  - Many tools exist but validity evidence is scarce. The Mini-CEX has the strongest evidence.
  - Implication: adapt an evidenced format rather than invent one.
- Fairness:
  - Roberts et al. 2000, *BMJ*. [VS, abstract not in the index] https://pubmed.ncbi.nlm.nih.gov/10657339/
    - Candidates from minority ethnic backgrounds can be disadvantaged by the mix of personal, professional and institutional talk that orals demand.
    - Examiners must be selected, trained and monitored.
  - Memon, Joughin & Memon 2010, *Adv Health Sci Educ*. [VP] https://pubmed.ncbi.nlm.nih.gov/19466570/
    - Sets out conditions for validity, reliability and fairness in oral assessment, with special concern for candidates whose first language differs.
  - This bears on Erica Catubig's third post (intake group 8) and on the white paper's dignity commitment in interviews (`2466517057642`, Part II, hiring, p.17).
- Rater training: frame-of-reference training (a shared picture of what good looks like) improves rating accuracy.
  - Woehr & Huffcutt 1994. [VS] https://bpspsychub.onlinelibrary.wiley.com/doi/abs/10.1111/j.2044-8325.1994.tb00562.x
  - Roch et al. 2012. [VS]
- Peer assessment:
  - Falchikov & Goldfinch 2000, *Rev Educ Res*. [VP] https://eric.ed.gov/?id=EJ630369
    - Peer and teacher marks agree best on global judgments made against well-understood criteria.
    - Agreement is weaker when rating professional practice than when rating academic products. [VS for that moderator]
  - Double, McGrane & Hopfenbeck 2020, *Educ Psychol Rev*. [VP] https://doi.org/10.1007/s10648-019-09510-3
    - As a **formative** practice, peer assessment improves performance, robustly across contexts.
  - Speyer et al. 2011, *Med Teach*. [VP] https://pubmed.ncbi.nlm.nih.gov/22022910/
    - Many peer instruments lack psychometric data.
  - Friendship and reciprocity bias. [LO/VS, multiple secondary] https://www.researchgate.net/publication/247354417_Reciprocity_as_a_Source_of_Bias_in_Multiple_Peer_Assessment_of_Group_Work
- **When a manager co-rater is needed.** The evidence supports Brandon's instinct. Add one when:
  - the decision gates access to the customer,
  - the peer is not yet calibrated through frame-of-reference training on the rubric,
  - the peer has a close relationship with the candidate,
  - the skill is professional practice in an open situation rather than a product,
  - a rating falls near the cut line.
  - Peer-only sign-off is defensible once the lead is calibrated, uses anchored global ratings, and co-rated audits keep agreement high. (Audit cadence is a workflow binding.)
- **Compliance flag:** whether hourly positional leads acting as raters counts as managerial work is an HR-seat question, as already noted in the intake.

## 6. Staged autonomy and whole-team feedback

**Verdict:**
- The angel shift followed by an eyes-off shift maps directly onto the EPA supervision levels: direct supervision, then indirect supervision with help available, then unsupervised, then supervising others.
- The framework is well developed conceptually. Outcome evidence is thin.
- Whole-team feedback during a trial shift is useful as **formative** input. It is unreliable and risky as a **gate** unless structured and kept task-focused.

**Strength:** EPAs: principle-level and implementation evidence only. Multi-source feedback: reliable only with many raters, and improvement after it is small. Feedback can backfire: strong, replicated.

- ten Cate et al. 2015, AMEE Guide 99. [VP] https://pubmed.ncbi.nlm.nih.gov/25897707/
  - Assessment becomes an entrustment decision for designated levels of permitted autonomy, "ranging from acting under full supervision to providing supervision to a junior learner."
- Hauer, ten Cate et al. 2014, *Adv Health Sci Educ*. [VP] https://pubmed.ncbi.nlm.nih.gov/23892689/
  - Trust depends on five things: supervisor, trainee, their relationship, task and context.
  - So write the eyes-off criteria per task, not per person.
- Suthiram & Naidoo 2026, systematic review of EPAs in family medicine. [VP]
  - Reported benefits are clearer expectations, transparency and better formative feedback.
  - Barriers are integration and faculty development.
  - No hard outcome data.
- Donnon et al. 2014, *Acad Med*, multi-source feedback. [VP] https://pubmed.ncbi.nlm.nih.gov/24448053/
  - Reliable **only with many raters across several rater groups**.
  - A single shift's team gives too few raters per dimension to support a pass or fail.
- Smither, London & Reilly 2005, *Personnel Psych*. [VP-full] https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1744-6570.2005.514_1.x
  - Improvement after multi-source feedback "is generally small."
  - It is likelier when the recipient sees a need, reacts positively, believes change is feasible and sets goals.
- Kluger & DeNisi 1996, *Psych Bull*. [VS, institutional abstract] https://cris.huji.ac.il/en/publications/the-effects-of-feedback-interventions-on-performance-a-historical/
  - Feedback helps on average, but a substantial share of feedback interventions **reduced** performance.
  - Effectiveness drops as feedback moves away from the task toward the self.
- Edmondson 1999, *ASQ*. [VP, via Crossref] https://doi.org/10.2307/2666999
  - Team psychological safety predicts learning behavior, which mediates team performance.
  - Brandon's "anyone critiques anyone" norm needs this as a precondition.
- **Risks of "prove it to the team" night:**
  - Evaluation pressure shifts attention to the self (Kluger and DeNisi).
  - Social and hierarchy bias. A food runner may feel unable to rate a bartender honestly in public.
  - Too few raters to be reliable.
- **Design response:**
  - Task-focused prompts, for example one thing observed and one thing to try next.
  - Collect privately and have a lead synthesize.
  - Feeds the conversation; it is not a vote.
  - The final release decision stays with the calibrated raters in section 5.
  - The TBRI seat must review.

## 7. Self-directed progression and motivation

**Verdict:**
- Autonomy support strongly predicts autonomous motivation.
- Learner **control** over sequencing adds almost nothing to achievement.
- So give choice over **which branch and when**, and keep structure **within** a skill.
- Completion-contingent tangible rewards undermine intrinsic motivation.
- Badges and leaderboards can backfire.

**Strength:** Strong on reward undermining and on incentives tracking quantity rather than quality. Strong correlational evidence for autonomy support. Near-null for learner control. Small and unstable for gamification's motivational effects.

- Slemp et al. 2018, *Motiv Emot*, meta-analysis of leader autonomy support. [VP] https://link.springer.com/article/10.1007/s11031-018-9698-y
  - Strongly and positively related to autonomous motivation, well-being and positive work behavior. Correlational.
- Karich, Burns & Maki 2014, *Rev Educ Res*. [VP] https://doi.org/10.3102/0034654314526064
  - The overall effect of learner control was "almost zero." Effects were somewhat larger for behavioral outcomes, but still small.
- Deci, Koestner & Ryan 1999, *Psych Bull*. [VP] https://pubmed.ncbi.nlm.nih.gov/10589297/
  - Rewards contingent on engagement, completion and performance all undermined free-choice intrinsic motivation, as did tangible and expected rewards.
  - Positive feedback **enhanced** intrinsic motivation.
- Cerasoli, Nicklin & Ford 2014, *Psych Bull*. [VP] https://pubmed.ncbi.nlm.nih.gov/24491020/
  - Intrinsic motivation predicts **quality** of performance. Incentives predict **quantity**.
  - When incentives are tied directly to performance, intrinsic motivation matters less, a crowding-out effect.
- Sailer & Homner 2020, *Educ Psychol Rev*. [VP] https://eric.ed.gov/?id=EJ1245270
  - Small positive effects of gamification.
  - Motivational and behavioral effects are unstable in rigorous studies.
  - Game fiction and social interaction (collaboration alongside competition) helped.
- Hanus & Fox 2015, *Computers & Education*, semester-long study. [VS] https://www.semanticscholar.org/paper/Assessing-the-effects-of-gamification-in-the-A-on-Hanus-Fox/dff76a9862467d426113ec530f83942016ae3a97
  - A badge-and-leaderboard course lowered intrinsic motivation and satisfaction over time. Exam scores were lower, mediated by motivation.
- **Founder-gated flags (tensions with the white paper `2466517057642`):**
  - (a) Part II, "Training infrastructure", p.18 ties earnings to the number of modules completed. This is a completion-contingent tangible reward. The evidence predicts it will raise completion counts and erode the intrinsic, quality-driven engagement Brandon wants: the "mere participation" he distrusts (intake group 7).
    - Evidence-aligned alternatives: tie pay to demonstrated competence (a passed practical, a new role) and to teaching; keep completion unpaid but recognized with informational feedback.
  - (b) Part II, "Cultural impact measurement", p.22 lists participation in development as a measure. See section 9.
  - (c) Part II, "Performance management", p.19, peer recognition platform: keep it informational and specific, not point-scored.
- **Skill-tree presentation** (Brandon's Horizon image, and the white paper's "inverted web", Part I, p.11): showing competencies and open paths is autonomy- and competence-supportive in principle. Avoid rank comparison (leaderboards).

## 8. Training decisions to match an expert's

**Verdict:** The best-supported route to "decide the way Brandon would" is:
1. Elicit his reasoning with incident-based cognitive task analysis (the Critical Decision Method).
2. Build scenarios with decision points from it.
3. Train by comparing the learner's reasoning to his (ShadowBox style).
4. Check with situational judgment items keyed to an expert panel.

**Strength:**
- CTA-based training: large effects, but few studies.
- ShadowBox: positive, mostly developer-run.
- SJTs: moderate, replicated criterion validity for job performance.
- RPD: strong descriptive model of expert decisions, not itself a training effect.

- Klein, Calderwood & MacGregor 1989, *IEEE SMC*, Critical Decision Method. [VS] https://ieeexplore.ieee.org/document/31053/
  - An incident-based interview with probes for cues, perceptual and conceptual discriminations, and typicality judgments.
  - This is the method for Brandon's agreed interviews (intake group 8, item 5). Probe each incident for cues noticed, options rejected, and what a novice would miss.
- Tofel-Grehl & Feldon 2013, *JCEDM*, meta-analysis of CTA-based training. [VS] https://journals.sagepub.com/doi/abs/10.1177/1555343412474821
  - Large effect over training designed without CTA. The authors flag the small number of studies.
- Edwards et al. 2021, *BJS Open*, CTA in surgery. [VP] https://pmc.ncbi.nlm.nih.gov/articles/PMC8669793/
  - Improved procedural knowledge and performance in novices.
- ShadowBox:
  - Klein & Borders 2016, *JCEDM*. [VS, abstract behind a 403 wall; the evaluators are the method's developers] https://journals.sagepub.com/doi/abs/10.1177/1555343416636515
    - Trainees rank options at decision points, then see an expert panel's rankings and rationale.
    - Evaluations with Marines and soldiers improved against controls.
  - Tallentire et al. 2026, *Adv Simul*. [VP]
    - National-scale feasibility in healthcare. Outcomes are learner-reported.
- McDaniel et al. 2007, *Personnel Psych*, SJT meta-analysis. [VS] https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1744-6570.2007.00065.x
  - SJTs predict job performance.
  - "What should one do" (knowledge) instructions measure more cognitive ability. "What would you do" (behavioral tendency) instructions pick up more personality.
  - Choose the instruction for the construct you want.
- **Design caution:**
  - A key built on one expert encodes that person's idiosyncrasies.
  - ShadowBox uses a panel. For Sŏn: use Brandon's CDM-derived rationale as the anchor, then build the panel from calibrated leads as they emerge. Items where the panel disagrees become discussion cases, not scored items.
  - Lineage rule: any incident Brandon draws from Coqodaq, Alinea or Gracious is flagged for him and never written as fact.

## 9. Signals that behavior changed versus mere completion

**Verdict:**
- Completion and satisfaction do not show behavior change.
- Use behavior-level evidence: observed performance on the floor, and success-case interviews.
- Watch for compliance-without-commitment, which is well documented in checklist research.
- Direct evidence on detecting complacency is thin. Proxies come from the safety-participation and learning-behavior research.

**Strength:** Strong that affective reactions poorly predict transfer. Moderate that behavior-level evaluation goes with transfer. Strong natural-experiment evidence that mandated tools without cultural uptake do nothing. Weak, by analogy only, on complacency detection.

- Alliger et al. 1997, *Personnel Psych*. [VP, via Crossref] https://doi.org/10.1111/j.1744-6570.1997.tb00911.x
  - Liking-type reactions relate weakly to transfer.
  - "Was this useful to my job" reactions relate more strongly, even more strongly than immediate learning scores.
  - If Sŏn asks one question after a module, ask about usefulness, not satisfaction.
- Saks & Burke 2012, *IJTD*. [VS] https://eric.ed.gov/?id=EJ964490
  - Only behavior- and results-level evaluation was associated with higher transfer.
  - Weak design: a survey of training professionals.
- Brinkerhoff 2005, Success Case Method. [VP, via Crossref] https://doi.org/10.1177/1523422304272172
  - Survey to find the extremes, then interview the most and least successful cases to learn what in the performance environment made the difference.
  - Fits Brandon's weekly 90-day review.
- Box-checking evidence:
  - Urbach et al. 2014, *NEJM*. [VP] https://pubmed.ncbi.nlm.nih.gov/24620866/
    - Mandated province-wide surgical checklists brought no significant change in mortality or complications.
  - Mayer et al. 2016, *Ann Surg*. [VP]
    - Partial checklist completion was common. Benefit showed up mainly when the checklist was completed in full.
  - Dixon-Woods et al. 2011, *Milbank Q*. [VP] https://pubmed.ncbi.nlm.nih.gov/21676020/
    - The Michigan program worked through peer networks, normative pressure, professional identity, and data used as discipline, not through the tool itself.
- Neal & Griffin 2006, *JAP*. [VP] https://pubmed.ncbi.nlm.nih.gov/16834517/
  - Group climate predicted later individual motivation, which predicted later behavior. Better group behavior was followed by fewer accidents.
  - The wider framework separates **compliance** (doing what is required) from **participation** (voluntary contribution). [VS] That distinction is the one Brandon is reaching for.
- Edmondson 1999 (section 6): observable learning behaviors are the positive signal opposite complacency: asking for help, seeking feedback, raising errors, experimenting.
- **Candidate signals for Sŏn** (reasoned from the evidence above; untested in restaurants):
  - Positive:
    - voluntary practical requests and cross-training unlocks,
    - errors raised in pre-shift,
    - learner flags on modules,
    - peer feedback given across roles,
    - agreement between learner and expert on scenario decisions rising over time,
    - positive success cases.
  - Complacency:
    - completion without later requests,
    - practicals passed at the first attempt with no rationale given,
    - uniform ratings with no spread (a leniency signal),
    - pre-shift retrieval answered by the same few people,
    - no errors reported at all.
  - Treat these as leading indicators to investigate, never as targets. Once a measure becomes a target it stops working as a measure (Campbell and Goodhart, a principle, not tested here).

---

## Evidence-backed design rules for Sŏn

1. Size a unit to one objective and one learning job, never to a target length; critical-path units stay lean, optional long-form is fine. (§1)
2. Every critical-path unit schedules spaced retrieval, triggered by the learner's next shifts. (§2)
3. Retrieve, don't re-read: every "know it" component ends in recall, not review. (§2)
4. Interleave near-miss visual discriminations; do not assume interleaving helps tasting or text. (§2)
5. On-floor learning is structured OJT: a named trainer, a task breakdown, planned fading. Never ad hoc shadowing. (§3)
6. For open skills, design the next shift's chance to use the skill and the lead's support as part of the module. (§3)
7. Drill only recurrent, consistent movements in isolation, practice them across tempos, and always put them back into whole-task practice under decision load. (§4)
8. Spread physical drills over several short sessions rather than one long one. (§4)
9. Take-home kits need a self-check standard, a scheduled check-in, and an HR-settled pay answer. (§4)
10. Mental rehearsal supplements physical reps and never replaces them. (§4)
11. Every conversational gate uses set cases, an anchored rubric, and either two calibrated raters or enough cases. (§5)
12. Train every rater with frame-of-reference calibration before they sign anything off. (§5)
13. Examiners are chosen, trained and monitored for discourse and language bias; content, not fluency of talk, is scored. (§5)
14. Peers sign off alone only after calibration and with regular co-rated audits; a manager co-rates gates to the customer, near-cut ratings, and close relationships. (§5)
15. Autonomy is released per task in explicit supervision levels, with written criteria for each step. (§6)
16. Team feedback in a trial shift is task-focused and private, synthesized by a lead, and never a vote or a gate. (§6)
17. Give choice over which path and when; keep sequence and structure inside a skill. (§7)
18. Do not pay or point-score per module completed; reward demonstrated competence and teaching, and recognize completion with specific feedback. (§7, founder-gated)
19. No leaderboards; if progress is gamified, use a narrative map and collaboration, not rank. (§7)
20. Build decision training from Brandon's Critical Decision Method incidents, train by comparing reasoning to the expert panel, and check with SJTs whose instructions match the construct. (§8)
21. A module is "measured" only on behavior-level evidence (observation or success case); after a module, ask about usefulness, not satisfaction. (§9)
22. Track participation signals as prompts to investigate, never as targets. (§9)

## Evidence gaps (Sŏn will reason by analogy)

- **Hospitality-specific studies:** almost none found for any of the above. Nearly all evidence comes from medicine, the military, aviation, education or manufacturing.
- **Spacing on irregular hourly shifts:** no direct test. Gaps are extrapolated from lab and resident studies.
- **Microlearning:** no behavior-level or long-term evidence, and no agreed definition.
- **Separating movement from decisions for service skills** (tray, pour, pace): extrapolated from surgical, sport and part-task research. Tempo-variation drills in particular are untested.
- **Take-home practice for hourly workers:** evidence is from motivated surgical trainees. Adherence in a paid hourly setting is unknown.
- **Oral assessment in a workplace with no exam board:** reliability evidence assumes resourced, high-stakes settings. The feasible number of cases and raters at Sŏn is unknown.
- **Peers of different roles rating each other** (a food runner rating a bartender): no direct evidence. Status and hierarchy effects are likely but unmeasured.
- **Whole-team feedback during one trial shift:** no study found. The inference comes from multi-source feedback (many raters, long windows) and feedback-intervention research.
- **EPAs outside medicine:** conceptual transfer only. Outcome evidence for staged autonomy is thin even in medicine.
- **Matching a single founder's decisions:** CTA and ShadowBox evidence uses expert panels. Training toward one person's judgment has no direct evidence and carries a single-source risk.
- **Complacency and box-checking detection:** no validated instrument for training culture. Proxies come from safety-participation, psychological-safety and checklist studies.
- **Tasting and flavor discrimination training** (psychotaste): interleaving evidence for tastes is ambiguous. No perceptual-learning evidence specific to service staff was reviewed.
- **Not re-verified this pass:**
  - full texts of most papers (abstracts only unless marked VP-full),
  - Jacobs's structured-OJT magnitudes,
  - the ShadowBox original abstract,
  - the task-type moderator in the mental-practice papers,
  - the original goldfish trace.