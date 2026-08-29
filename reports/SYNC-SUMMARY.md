# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 283 commits affecting 1403 files.
- **Source revision:** `1d8946b40b93`.
- **Previous source revision:** `0dfba37b11ff`.

## Technical coverage

- **.github/:** 3 changed files.
- **.superpowers/:** 2 changed files.
- **agent/:** 87 changed files.
- **apps/:** 567 changed files.
- **cli-config.yaml.example/:** 2 changed files.
- **cli.py/:** 3 changed files.
- **contributors/:** 21 changed files.
- **cron/:** 18 changed files.
- **eslint.config.shared.mjs/:** 2 changed files.
- **gateway/:** 7 changed files.
- **nastech_cli/:** 38 changed files.
- **nastech_constants.py/:** 4 changed files.
- **nastech_logging.py/:** 1 changed files.
- **nastech_state.py/:** 9 changed files.
- **optional-skills/:** 6 changed files.
- **package-lock.json/:** 2 changed files.
- **package.json/:** 2 changed files.
- **plugins/:** 11 changed files.
- **pyproject.toml/:** 2 changed files.
- **run_agent.py/:** 7 changed files.
- **scripts/:** 18 changed files.
- **setup-nastech.sh/:** 1 changed files.
- **skills/:** 1 changed files.
- **tests/:** 182 changed files.
- **tests-js/:** 6 changed files.
- **tools/:** 72 changed files.
- **toolsets.py/:** 2 changed files.
- **tui_gateway/:** 12 changed files.
- **ui-tui/:** 9 changed files.
- **uv.lock/:** 1 changed files.
- **website/:** 15 changed files.

## Delivered improvements

### New capabilities

- feat(cli): render Ghostty-level pets in the interactive pane
- feat(pet): gate Unicode placeholders to kitty and Ghostty
- feat(desktop): export, import, rename and delete a board from the switcher
- feat(desktop): PluginOs gains native save/open file pickers
- feat(kanban): board export/import REST endpoints
- feat(kanban): export and import a whole board as a portable archive
- feat(a2a): client tools config-gated — disabled unless enabled (−561 tok/call on unconfigured installs) (#97421)
- feat(skill_manage): operations[] is the call — each op names its skill; atomic with cross-skill rollback (#97295)
- feat(agent): context size anchors on provider-reported usage — estimation shrinks to the last turn
- feat: session temp root moves off tmpfs /tmp to ~/.nastech/cache/terminal by default; auto-pruned after 72h
- feat: expose terminal.temp_dir to redirect session temp root off tmpfs
- feat(cli/tui): -q now seeds a live interactive session; prompts submit literally
- 18 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(prompt-caching): tool-using sessions no longer 400 behind LiteLLM Anthropic proxies (#89886)
- fix(skills): drop redundant identical-strings guard and its vacuous tests
- fix(skills): make skill_manage patch failures recoverable instead of a dead end
- fix(desktop): preserve streamed assistant text and unify atomic persistence (#95514)
- fix(desktop): make gateway file saves failure-atomic so a failed download never destroys an existing file
- fix(bedrock): recover from server-side cachePoint rejections per placement
- fix(cache): over-length caller prompt_cache_key no longer 400s Chat Completions requests
- fix(caching): prevent whitespace-only text blocks in prompt cache prefix splits
- fix(desktop): open HUD links in the system browser
- fix(desktop): let HUD prompts take clicks on solid X11
- fix(agent): count only substantive auxiliary progress
- fix(teams): allowlist-gate BF attachment auth, stream downloads under media cap, lock token refresh
- 138 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(state): route 39 pure-read SessionDB methods off the writer lock + gate
- perf: skip dict copy for non-compression auxiliary calls
- perf(compression): add guarded fast summary lane

### Documentation

- docs(update): --yes help states the fork-upstream prompt is skipped, not accepted
- docs(bots): name the room budget as the seam the limits PRs hook
- docs: reconcile positional pairing with shared _classify_tool_call_orphans (#97167) — classifier docstring reflects its remaining consumer; empty-id filter note updated
- docs(skills): document programmatic-write scope cut in skills_guard module docstring
- docs(desktop): record why the Bots-home new-chat refusal is gone
- docs: relay-fronted cron delivery + manual-run gateway forward (troubleshooting)
- docs(skills): keep optional-skills catalog scoped to the agentmail row
- docs(skills): regen agentmail optional page + catalog row

### Improvements

- test(skills): cover the patch recovery loop end to end
- refactor(desktop-tools): consolidate preview + project, diet the desktop_ui suite (3,861 → 2,293 tok/call, −41%) (#97659)
- fmt(js): `npm run fix` on merge (#97713)
- test(cache): pin the prompt-cache scope isolation invariant for per-response session ids
- chore: map eric.maddox@outlook.com -> ericmaddox (attribution for #97618)
- fmt(js): `npm run fix` on merge (#97706)
- refactor: fold simplify-code review findings into #96667 salvage
- test: pin fence/TTFP semantics for substantive-progress gating (#96667 salvage)
- Merge pull request #97676 from kshitijk4poor/fix/pattern-c-reader-offload
- fmt(js): `npm run fix` on merge (#97642)
- fmt(js): `npm run fix` on merge (#97638)
- test(desktop): follow the model and path menu labels to sentence case
- 80 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
