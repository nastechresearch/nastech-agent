# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 367 commits affecting 1323 files.
- **Source revision:** `c584d15cdc31`.
- **Previous source revision:** `261a4efb90d7`.

## Technical coverage

- **.dockerignore/:** 1 changed files.
- **.gitignore/:** 4 changed files.
- **acp_adapter/:** 1 changed files.
- **agent/:** 60 changed files.
- **apps/:** 533 changed files.
- **cli-config.yaml.example/:** 2 changed files.
- **cli.py/:** 5 changed files.
- **contributors/:** 35 changed files.
- **cron/:** 21 changed files.
- **default.tar.gz/:** 1 changed files.
- **gateway/:** 31 changed files.
- **log.txt/:** 1 changed files.
- **nastech_cli/:** 104 changed files.
- **nastech_state.py/:** 10 changed files.
- **nastech_state_common.py/:** 5 changed files.
- **nastech_state_portability.py/:** 2 changed files.
- **nastech_state_schema.py/:** 3 changed files.
- **nastech_state_search.py/:** 2 changed files.
- **package-lock.json/:** 1 changed files.
- **plugins/:** 2 changed files.
- **run_agent.py/:** 5 changed files.
- **scripts/:** 7 changed files.
- **sqlite_leak_fix.png/:** 1 changed files.
- **tests/:** 267 changed files.
- **tools/:** 50 changed files.
- **tui_gateway/:** 33 changed files.
- **ui-tui/:** 3 changed files.
- **web/:** 1 changed files.
- **website/:** 27 changed files.

## Delivered improvements

### New capabilities

- feat(bots): typed failure reasons reach the sending agent on A2A calls (#93091)
- feat(bots): retry session policy — resume transient turns, compress-and-resume on context overflow (#93091 item 5)
- feat: every subagent's prompt embeds the workspace's project context files
- feat: /review briefing embeds the workspace's project context files
- feat: /review briefing carries the parent's loaded skills
- feat: review slot appears in every aux-model picker (desktop, dashboard, CLI)
- feat(desktop): OAuth sign-in for registry connections; keep profile picks on the browsed source (#92194)
- feat: /review command — independent reviewer subagent on every surface
- feat(desktop): bring the old Nastech palette back as Nastech Alt
- feat(bot-mode): per-profile turn lock — concurrent deliveries queue instead of racing (#93091)
- feat(bot-mode): push-notified relay drain with poll backstop (#93091)
- feat(bot-mode): envelope TTL + offline fast-fail for bot relay (#93091 item 2)
- 16 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(classifier): 429 quota walls route to billing across providers; reset signals stay rate-limited
- fix(state): reap only proven database holders
- fix(state): recover FTS after orphan holder deferrals
- fix(auth): rotate credentials for named custom providers after 401/429
- fix(auth): canonicalize configured provider display names
- fix(auth): preserve configured provider compatibility
- fix(auth): normalize configured provider pool keys
- fix(gateway): stop multiplex allowlist leak and bot-relay python -c injection
- fix(dashboard): name the exact gate trigger in fail-closed refusals
- fix(dashboard): secure loopback public URL proxy mode
- fix(state): stop rebuilding the whole FTS index on every open when the trigram tokenizer is missing
- fix(telegram): watchdog silent long-poll death via last getUpdates progress (#92991)
- 220 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(bluebubbles): move attachment reads off the event loop

### Documentation

- docs: dashboard ws keepalive + orphan-reap grace config keys
- docs: make the mutate-then-persist marker contract explicit (#92231 review)
- docs: record why the reap grace window exists in the reaper docstring

### Improvements

- test(bots): turn-lock fake Proc gains stdout/stderr attrs
- chore: map e-macgregor contributor email
- chore: map contributor email for cxxCoolStar
- chore: add contributor email mapping for jackijianxa
- chore: map contributor emails for ring-2 salvage (A2chitect, c-pompa)
- harden(adoption): review findings — exact-id donors only, divergence guard, honest donor_retired
- fmt(js): `npm run fix` on merge (#93429)
- chore: map wingkwong contributor email
- test(cua): pin PATH-preservation contract, not byte equality
- chore: map UniversePeak contributor email
- test(cron): e2e regression — scrubbed child env resolves bare nastech under minimal parent PATH
- test(agent): drain truncation warnings before and after each prompt-builder test
- 91 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
