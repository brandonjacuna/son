# Scenarios

Format: see `framework/module-spec.md`. Build and test with `python scripts/build_scorm.py <module folder>`.

## Scenario S1: Title

**Setup.** What the learner sees and hears.

**Cues present.** What an expert would notice.

### Decision 1
Prompt: What do you do?
- A. First choice. -> go to 1A
- B. Second choice. -> go to 1B

### 1A
Consequence: What happens, shown not told.
Feedback: Why, tied to the cue.
Expert rationale: What the expert noticed and chose.
Next: End (recoverable)

### 1B
Consequence: What happens.
Feedback: Why.
Expert rationale: What the expert noticed and chose.
Next: End (strong)
