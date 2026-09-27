# Adapter: Synthesia

Researched 2026-09-26 from Synthesia's knowledge base and docs. Re-verify with `/refresh-capabilities synthesia` before a real render.

## What Synthesia is good for here

Scripted video with an AI presenter or AI-voiced scenes, fast to revise when a binding changes, translatable. It is a strong fit for framing a scenario, voicing the customer side of a branching scenario, and explaining a concept. It is a weaker fit for modeling warmth, the physical craft of service, or anything a learner should imitate, where behavior-modeling research favors a credible, real model. Default: the expert behavior is modeled by real Sŏn footage; Synthesia sets up and voices the situation.

## Capabilities that shape design

| Capability | Plan | Verified |
|---|---|---|
| Interactive buttons (open a link, jump to a scene) and branching menus | Creator and Enterprise | 2026-09-26 |
| In-video quizzes with pass or fail results | Enterprise only | 2026-09-26 |
| SCORM export (completion when the learner reaches the end scene or the results scene) | Enterprise only | 2026-09-26 |
| Interactivity works only in Synthesia's player: share link, iframe embed, or SCORM. Downloaded MP4s lose it. | All | 2026-09-26 |
| Replacing a video updates the SCORM package without re-export | Enterprise | 2026-09-26 |
| APIs: Video API (scripted avatar video, templates, dubbing), Interactive Avatars API (real-time), Upload API | Check plan | 2026-09-26 |

## Render paths

1. **Linear explainer:** render video, embed the share link in a Trainual page. Tracking comes from a Trainual test after it.
2. **Branching video on Creator:** embed via iframe in Trainual. Learners branch; nothing is recorded. Pair with a native test or written response for the record.
3. **Branching video with quiz on Enterprise:** export SCORM, upload to Trainual. Completion and pass or fail tracked.
4. **Alternative for tracked branching without Enterprise:** render short linear clips per scene in Synthesia, then assemble them in the repo's SCORM scenario player (`adapters/scorm.md`) with the video URLs as scene media. Tracked, no Enterprise plan needed.

Path 4 keeps the branching logic in the repo, which also keeps it portable to any other video tool.

## From video-script.md to Synthesia

- Each row in `video-script.md` becomes one scene.
- Narration becomes the script for that scene. Keep lines short; one idea per scene.
- On-screen text only where it adds something narration does not (Mayer's redundancy principle, per the Instructional Designer).
- Visual direction is a brief. **It goes through the Design Translating Team before it becomes a Synthesia prompt or scene setting.** Start with 01 Design Brief Translator and 02 Platform Prompt Specialist; add 03 Brand Identity Specialist when brand elements appear.
- Interaction points become buttons or branches per the scenario map.

## Open decision

AI presenters are AI-generated imagery. The standing rule bars AI-generated imagery on public surfaces; training is internal. Whether AI presenters are acceptable for internal training, and whether they may portray team members or customers, is **founder-gated**. Record it as `founder.ai_presenter_policy` in any module that uses Synthesia until Brandon decides.
