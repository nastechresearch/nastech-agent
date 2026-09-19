# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 809 commits affecting 2246 files.
- **Source revision:** `a51143fbbe6d`.
- **Previous source revision:** `debfc7420b61`.

## Technical coverage

- **.github/:** 2 changed files.
- **acp_adapter/:** 16 changed files.
- **agent/:** 119 changed files.
- **apps/:** 355 changed files.
- **batch_runner.py/:** 1 changed files.
- **cli.py/:** 6 changed files.
- **contributors/:** 63 changed files.
- **cron/:** 24 changed files.
- **gateway/:** 105 changed files.
- **nastech_bootstrap.py/:** 2 changed files.
- **nastech_cli/:** 250 changed files.
- **nastech_constants.py/:** 3 changed files.
- **nastech_state.py/:** 4 changed files.
- **nastech_state_common.py/:** 2 changed files.
- **nastech_state_compression.py/:** 3 changed files.
- **nastech_state_gateway.py/:** 4 changed files.
- **nastech_state_messages.py/:** 4 changed files.
- **nastech_state_readpool.py/:** 1 changed files.
- **nastech_state_repair.py/:** 3 changed files.
- **nastech_state_schema.py/:** 3 changed files.
- **nastech_state_search.py/:** 1 changed files.
- **nastech_state_sessions.py/:** 2 changed files.
- **nastech_state_telegram.py/:** 5 changed files.
- **optional-mcps/:** 3 changed files.
- **optional-skills/:** 4 changed files.
- **plugin-catalog/:** 32 changed files.
- **plugins/:** 47 changed files.
- **scripts/:** 16 changed files.
- **skills/:** 3 changed files.
- **tests/:** 675 changed files.
- **tools/:** 138 changed files.
- **trajectory_compressor.py/:** 1 changed files.
- **tui_gateway/:** 41 changed files.
- **ui-tui/:** 4 changed files.
- **utils.py/:** 1 changed files.
- **web/:** 25 changed files.
- **website/:** 526 changed files.

## Delivered improvements

### New capabilities

- feat(plugin-catalog): add live-time plugin entry
- feat(catalog): add Toolsmith desktop plugin
- feat(catalog): add Session Diff desktop plugin
- feat(plugin-catalog): add Nastech Outpost
- feat(catalog): add ClinePass model provider
- feat(plugin-catalog): add billing community plugin
- feat(catalog): add by2kb video-to-knowledge plugin
- feat(plugin-catalog): add kiro-acp community plugin
- feat(catalog): add Replaid plugin
- feat(plugin-catalog): add nastech-opper (Opper model provider)
- feat(catalog): declare nastech floor and note the placeholder key for zerosignal
- feat(catalog): add zerosignal provider v0.1.0
- 8 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(bedrock): resolve application-inference-profile ARNs before the prompt-cache allowlist match
- fix(bedrock): application inference profile ARNs size from the wrapped model on the real path
- fix(bedrock): size inference-profile ARNs from the wrapped foundation model
- fix(backup): an incomplete archive never prunes the last complete ones
- fix(backup): exit non-zero when a full backup is incomplete
- fix(runtime): drop the dead urlparse import; pin the bare-host-default fail-open
- fix(runtime): share URL path parsing with the host check; pin catalog defaults in tests
- fix(runtime): compare against the catalog default path, keep declared on empty input
- fix(runtime): declared Anthropic transport applies only on the provider's own endpoint
- fix(desktop): every Custom Endpoints completion is dropped once its profile view unmounts
- fix(desktop): drop stale custom endpoint saves
- fix(dashboard): profile-less chat deep links inherit the launcher's preselected profile
- 558 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(desktop): test the pending reply's parts in place instead of joining the transcript per flush

### Documentation

- docs: session-bound Desktop/TUI settings writes and dashboard launch-profile fallback are per profile
- docs(whatsapp): group access section says what the gateway admits; env reference rows; trim bridge tests
- docs(website): re-run the link sweep over pages merged since the rebase
- docs(website): link pages by relative Markdown path so they open on GitHub (#114428)
- docs(website): tell GitHub readers the docs are authored for the rendered site; record the link convention
- docs(memory-provider): state that no bundled provider advertises checkpoint API v2
- docs(desktop): document the Reasoning Blocks toggle; narrow its config type
- docs(gateway): say rejected final sends are retried with a backoff
- docs(update): a multiplexer covers every served profile in the fleet check
- docs(agent): TTFB cap is opt-in — say so where operators read it
- docs(memory-provider): agent_context carries cron/subagent, not always primary
- docs(desktop): the Kanban board switcher sits in the page header, not the window title bar
- 29 additional documentation updates are included in this verified snapshot.

### Improvements

- chore(contributors): map yagnavudathu@gmail.com to @whyyagswhy
- refactor(gateway): one wildcard-host predicate for the HTTP listeners
- test(gateway): trim the TIME_WAIT rebind tests to the two invariants
- chore: map contributor email for @TheBlueHouse75 (#108239 salvage)
- chore: map amitcse, eduardo and jinlingzi-cmd contributor emails
- refactor(state): topic rebuild goes through _rebuild_table; heal also swallows a replaced state.db
- test(state): atomicity probe fails the rebuild's final RENAME, not its first DROP
- refactor(state): one heal-and-retry helper for every topic read; trim tests
- plugin-catalog: bump nastech-newswire pin deccdc4 -> e6b438e
- chore: map contributor email for @NealZhouPanda
- Fix pinned sha to actual v0.1.1 commit
- Add nastech-subscription-meter to plugin catalog
- 165 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
