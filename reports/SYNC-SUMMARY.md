# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 167 commits affecting 1294 files.
- **Source revision:** `261a4efb90d7`.
- **Previous source revision:** `fcbd1076a938`.

## Technical coverage

- **.github/:** 13 changed files.
- **AGENTS.md/:** 3 changed files.
- **agent/:** 27 changed files.
- **apps/:** 217 changed files.
- **cli-config.yaml.example/:** 1 changed files.
- **contributors/:** 12 changed files.
- **cron/:** 2 changed files.
- **gateway/:** 39 changed files.
- **nastech_cli/:** 49 changed files.
- **nastech_state.py/:** 15 changed files.
- **nastech_state_common.py/:** 1 changed files.
- **nastech_state_portability.py/:** 1 changed files.
- **nastech_state_schema.py/:** 1 changed files.
- **nix/:** 8 changed files.
- **plugins/:** 13 changed files.
- **run_agent.py/:** 1 changed files.
- **scripts/:** 4 changed files.
- **tests/:** 127 changed files.
- **tools/:** 14 changed files.
- **tui_gateway/:** 22 changed files.
- **ui-tui/:** 2 changed files.
- **web/:** 1 changed files.
- **website/:** 25 changed files.

## Delivered improvements

### New capabilities

- feat(desktop): Send Diagnostics — one-click redacted debug-bundle upload from the error card
- feat(bot-mode): @mention middleware identifies, never delivers — the agent owns messaging
- feat(desktop): error card offers Nastech support link on Portal-auth sessions
- feat(desktop): failed turns name the failing layer with recovery actions
- feat(bot-mode): message_agent tool — structured, Bot-Chat-only agent-to-agent DMs
- feat(update): updates.parked_branch_strategy gates the in-place merge; switch stays the default
- feat(update): --switch-branch opts an unmerged branch out of the in-place merge
- feat(update): update branches carrying unmerged commits in place instead of skipping
- feat(bedrock): add OpenAI GPT-5.6 family (Sol/Terra/Luna) to Mantle Responses routing
- feat(bedrock): support OpenAI Responses models
- feat(models): free models show star + -100% in the model picker discount column
- feat(models): glm-5.3 replaces glm-5.1 in the OpenRouter and Nastech Portal catalogs
- 9 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(gateway): claim ledger rows and clear resume_pending inline before the abandonable boot-send task
- fix(compression): restore the prune runway when a would-grow refusal keeps the transcript
- fix(gateway): retain failed replacement evidence
- fix(gateway): distinguish failed systemd replacements
- fix(gateway): make handoff recovery idempotent
- fix(gateway): preserve systemd handoff recovery
- fix(gateway): make systemd the sole restart owner
- fix(gateway): isolate kanban dispatcher to_thread context
- fix(gateway): isolate supervised watcher contexts
- fix(gateway): give supervision exhaustion an owner for queued platforms
- fix(gateway): heal a dead reconnect watcher when the platform is already queued
- fix(tui): log the refused shared-handle transfer and pin _get_db caching
- 76 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(ci): set python test workers to one for each core, from measurement
- perf(api): classify compaction rows once per message in run.completed transcript
- perf(browser): read the feature flags via load_config_readonly

### Documentation

- docs(agents-md): Bot Mode canonical-chat invariant is name-identity — corrections folded in
- docs: record the Bot Mode canonical-chat invariant in AGENTS.md
- docs(agents-md): update pipeline architecture, process-identity pitfall, gateway lifecycle contract, wine2e lane
- docs(credits): document naming-convention trust in aux free-SKU detector
- docs: Add Nix/NixOS to installation link description

### Improvements

- Merge pull request #92214 from kshitijk4poor/discord-picker-constants-followup
- Merge pull request #92216 from kshitijk4poor/fix/p1-gateway-simplify-followups
- refactor(gateway): promote parse_systemd_duration_to_us to public
- refactor(telegram): share the flood-wait cap between send and edit paths
- refactor(gateway): route kanban notifier writer offloads through _to_thread_process_service
- refactor(discord): use _DISCORD_SELECT_MAX_OPTIONS in ChoicePickerView
- refactor(discord): derive model-select capacity from the row/option constants
- review follow-up: trim overreaching comment sentence, pin durable-copy assertion
- refactor(terminal): extract _current_session_key() helper for session-key lookups
- test(terminal): cover gateway ContextVar session-key path
- refactor(discord): derive model-select counts, name the 25-option cap
- chore: map contributor email epicstorage0@gmail.com
- 38 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
