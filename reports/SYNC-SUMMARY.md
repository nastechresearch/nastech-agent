# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 731 commits affecting 3287 files.
- **Source revision:** `9cb34e9e285d`.
- **Previous source revision:** `b3c28838095b`.

## Technical coverage

- **.github/:** 1 changed files.
- **README.md/:** 1 changed files.
- **acp_adapter/:** 29 changed files.
- **agent/:** 57 changed files.
- **apps/:** 462 changed files.
- **cli.py/:** 2 changed files.
- **contributors/:** 17 changed files.
- **gateway/:** 344 changed files.
- **locales/:** 316 changed files.
- **nastech_cli/:** 325 changed files.
- **nastech_constants_scratch.py/:** 3 changed files.
- **nastech_constants_scratch_stuck.py/:** 2 changed files.
- **nastech_logging.py/:** 3 changed files.
- **nastech_state.py/:** 1 changed files.
- **nastech_state_api_content.py/:** 1 changed files.
- **nastech_state_common.py/:** 4 changed files.
- **nastech_state_errors.py/:** 1 changed files.
- **nastech_state_maintenance.py/:** 4 changed files.
- **nastech_state_messages.py/:** 8 changed files.
- **nastech_state_mutation_branch.py/:** 1 changed files.
- **nastech_state_mutation_guards.py/:** 1 changed files.
- **nastech_state_mutation_prepared.py/:** 3 changed files.
- **nastech_state_mutations.py/:** 8 changed files.
- **nastech_state_portability.py/:** 1 changed files.
- **nastech_state_profile_repair.py/:** 2 changed files.
- **nastech_state_prune_rewrite.py/:** 1 changed files.
- **nastech_state_runtime.py/:** 5 changed files.
- **nastech_state_sessions.py/:** 4 changed files.
- **nastech_state_todo.py/:** 1 changed files.
- **nastech_state_worker_compression.py/:** 2 changed files.
- **plugin-catalog/:** 97 changed files.
- **plugins/:** 15 changed files.
- **run_agent.py/:** 8 changed files.
- **scripts/:** 5 changed files.
- **tests/:** 532 changed files.
- **tools/:** 51 changed files.
- **tui_gateway/:** 69 changed files.
- **ui-tui/:** 71 changed files.
- **website/:** 82 changed files.

## Delivered improvements

### New capabilities

- feat(plugins): portable plugins get the Settings > Plugins form, live
- feat(cli): glyph transcript, status line under the composer, two-line header
- feat(plugins): a re-pin that moves an OAuth entry's authorize host asks first
- feat(plugins): OAuth clients a plugin declares, signed in and refreshed by Nastech
- feat(plugins): nastech plugins update with no name offers every plugin update
- feat(catalog): add rea-captcha
- feat(plugin-catalog): pin agent-station to v3.0.3
- feat(plugin-catalog): add agent-station plugin
- feat(catalog): add git-tasks plugin entry
- feat(plugin-catalog): add runbox (offline per-chat Python run/check/test box)
- feat(plugin-catalog): add post-cortex memory provider
- feat(plugin-catalog): add nastech-wsl-terminal
- 15 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(desktop): read the final reply aloud after tool calls (#140623)
- fix(desktop): an unhinted project-tree lookup reads the live gateway's profile
- fix(desktop): unread lookups stay within the owning profile and see project-tree rows
- fix(gateway): the stored picker lists plugin-platform conversations the cold mount opens
- fix(cli,tui): a refused delete releases its read with a plain detach under the resolved id
- fix(gateway,desktop): the live session poll names each session's source, so a messaging settle never lights unread before its row loads
- fix(desktop): reading any segment of a messaging or cron conversation marks the whole conversation read
- fix(desktop): a held completion the user already read stays read; the marker goes to its own profile
- fix(desktop): note Desktop's turns at the canonical client, by profile, in either order
- fix(desktop): a turn Desktop sends into a messaging session lights the unread dot
- fix(gateway): an old messaging conversation can be deleted from the picker
- fix(tui): hold picker input from the moment a delete starts
- 405 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(cli): filter the gateway subagent tail once per fetch, not per frame
- perf(cli): release a retired agent off the command path
- perf(state): a display read hashes only rows a removed copy could match
- perf(cli): keep a turn's streamed-delta buffers linear
- perf(gateway): parse a policy's follow flag once, not on every read

### Documentation

- docs(cli): /queue's shared gateway queue, move refusal, lost-answer note
- docs(tui): say why not_found stays a pre-commit refusal
- docs(plugins): give only the Google client as an example of a plugin OAuth client
- docs(gateway): name the real root-DM transfer hook in run_turn_prepare
- docs(gateway): the parity note for /save names Desktop's client-side write
- docs(gateway): regenerate the command parity table for the Desktop actions
- docs(slash): document /discard and regenerate the Desktop slash registry
- docs(pause): nastech pause holds interactive CLI, TUI and Desktop turns too
- docs(desktop): document the Subagents page in the delegation guide
- docs(hooks): note on_session_delete delivery is process-local, not cross-process (#124988)
- docs(plugins): name locate_skill's real second parameter; decode SKILL.md like skill_view

### Improvements

- test(desktop): another profile's same-id messaging tree row does not silence a local completion
- style(desktop): the project-tree fixture is a complete tree, no cast; blank line before the source key
- test(desktop): the live source cache and the read family stay within their own profile (currently failing)
- test(desktop): a messaging completion known only from the project tree does not light unread (currently failing)
- test(gateway): a bundled plugin platform conversation is listed in the stored picker (currently failing)
- test(cli,tui): a refused delete detaches by the resolved id and keeps a view the client holds (currently failing)
- test(gateway): releasing a refused delete's read leaves a live messaging chat unfenced
- test(gateway): a refused delete's read is released by a plain detach under the resolved id
- style(tui): the delete hook takes the possibly-missing row, keeping the picker's key handler under its complexity cap
- style(desktop): import order in the unread poll and its message-stream tests
- refactor(tui): the picker's delete lifecycle lives in a useSessionDelete hook
- test(gateway,desktop): a messaging turn that settles before its row loads does not light unread (currently failing)
- 259 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
