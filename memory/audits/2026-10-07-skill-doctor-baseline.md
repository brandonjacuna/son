# Skill library baseline (2026-10-07, phase 2)

## /skill-doctor (headless, cloud container)
```
Skills loaded this session

  skill                                              source                    context  7d tokens   uses  last used
  session-start-hook                                 userSettings                  ~90          -     0×  never
  book-ingest                                        projectSettings               ~90          -     0×  never
  chat-handoff                                       projectSettings              ~140          -     0×  never
  consolidate                                        projectSettings               ~50          -     0×  never
  equipment-record                                   projectSettings               ~60          -     0×  never
  intake                                             projectSettings               ~70          -     0×  never
  interview                                          projectSettings               ~60          -     0×  never
  profile-forge                                      projectSettings               ~70          -     0×  never
  session-close                                      projectSettings              ~160          -     0×  never
  skill-scanner                                      projectSettings              ~120          -     0×  never
  thread                                             projectSettings              ~100          -     0×  never
  capture                                            projectSettings               ~30          -     0×  never
  deep                                               projectSettings                 -          -     0×  never
  gate                                               projectSettings                 -          -     0×  never
  lease-signed                                       projectSettings                 -          -     0×  never
  promote                                            projectSettings               ~30          -     0×  never
  sandbox                                            projectSettings               ~30          -     0×  never
  cowork-plugin-management:cowork-plugin-customizer  cowork-plugin-management     ~110          -     0×  never
  cowork-plugin-management:create-cowork-plugin      cowork-plugin-management     ~130          -     0×  never
  anthropic-skills:built-in-browser                  claude.ai sync               ~290          -     0×  never
  anthropic-skills:chrome-browser                    claude.ai sync               ~260          -     0×  never
  anthropic-skills:computer-use                      claude.ai sync               ~320          -     0×  never
  anthropic-skills:deep-research                     claude.ai sync               ~200          -     0×  never
  anthropic-skills:docs                              claude.ai sync               ~340          -     0×  never
  anthropic-skills:docx                              claude.ai sync               ~320          -     0×  never
  anthropic-skills:google-workspace                  claude.ai sync               ~330          -     0×  never
  anthropic-skills:import-memory                     claude.ai sync                ~60          -     0×  never
  anthropic-skills:mcp-builder                       claude.ai sync               ~100          -     0×  never
  anthropic-skills:morning                           claude.ai sync               ~120          -     0×  never
  anthropic-skills:pdf                               claude.ai sync               ~150          -     0×  never
  anthropic-skills:pptx                              claude.ai sync               ~330          -     0×  never
  anthropic-skills:skill-creator                     claude.ai sync               ~120          -     0×  never
  anthropic-skills:xlsx                              claude.ai sync               ~320          -     0×  never

  context = this skill's one-line listing in the system prompt, included every turn
  (dash = not in the current listing, costs nothing; full SKILL.md loads only when it runs)
  7d tokens = tokens attributed to the skill over the last 7 days of sessions on this machine
```

Usage columns are per machine; a fresh cloud container always reports 0 uses. Listing cost of the account-synced skills (about 3,300 tokens a turn) is the main lever; turning unused ones off happens on claude.ai, not in the repo.

## skill-scanner, every project skill
| Skill | Findings | Note |
|---|---|---|
| book-ingest | 0 | Was 1 (unparseable frontmatter: colon in the description); description quoted |
| chat-handoff | 0 | |
| consolidate | 0 | |
| equipment-record | 0 | |
| intake | 0 | |
| interview | 0 | |
| profile-forge | 0 | |
| session-close | 0 | |
| skill-scanner | 35 | Pattern tables and examples only; see its SOURCE.md |
| thread | 0 | |
