# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 3484 commits affecting 3220 files.
- **Source revision:** `18c525b669b6`.
- **Previous source revision:** `0e427d788d25`.

## Technical coverage

- **.env.example/:** 1 changed files.
- **.github/:** 188 changed files.
- **.npmrc/:** 3 changed files.
- **acp_adapter/:** 106 changed files.
- **agent/:** 456 changed files.
- **apps/:** 2284 changed files.
- **cli-config.yaml.example/:** 14 changed files.
- **cli.py/:** 37 changed files.
- **contributors/:** 59 changed files.
- **cron/:** 139 changed files.
- **docker/:** 1 changed files.
- **docs/:** 8 changed files.
- **evals/:** 55 changed files.
- **gateway/:** 2507 changed files.
- **locales/:** 351 changed files.
- **mcp_serve.py/:** 2 changed files.
- **nastech_cli/:** 1438 changed files.
- **nastech_constants.py/:** 4 changed files.
- **nastech_constants_scratch.py/:** 8 changed files.
- **nastech_dir_acl.py/:** 11 changed files.
- **nastech_logging.py/:** 5 changed files.
- **nastech_platform/:** 1 changed files.
- **nastech_state.py/:** 5 changed files.
- **nastech_state_common.py/:** 22 changed files.
- **nastech_state_compression.py/:** 14 changed files.
- **nastech_state_detached_results.py/:** 1 changed files.
- **nastech_state_gateway.py/:** 15 changed files.
- **nastech_state_keys.py/:** 3 changed files.
- **nastech_state_local.py/:** 16 changed files.
- **nastech_state_local_lineage.py/:** 9 changed files.
- **nastech_state_local_migration.py/:** 8 changed files.
- **nastech_state_maintenance.py/:** 16 changed files.
- **nastech_state_media.py/:** 6 changed files.
- **nastech_state_messages.py/:** 22 changed files.
- **nastech_state_mutation_binding.py/:** 7 changed files.
- **nastech_state_mutation_branch.py/:** 9 changed files.
- **nastech_state_mutation_compress.py/:** 3 changed files.
- **nastech_state_mutation_guards.py/:** 13 changed files.
- **nastech_state_mutation_prepared.py/:** 8 changed files.
- **nastech_state_mutation_reset.py/:** 4 changed files.
- **nastech_state_mutation_retirement.py/:** 22 changed files.
- **nastech_state_mutation_transcript.py/:** 1 changed files.
- **nastech_state_mutations.py/:** 22 changed files.
- **nastech_state_portability.py/:** 2 changed files.
- **nastech_state_profile_repair.py/:** 3 changed files.
- **nastech_state_readpool.py/:** 1 changed files.
- **nastech_state_reconcile.py/:** 15 changed files.
- **nastech_state_repair.py/:** 1 changed files.
- **nastech_state_rewind.py/:** 1 changed files.
- **nastech_state_runtime.py/:** 71 changed files.
- **nastech_state_runtime_workers.py/:** 4 changed files.
- **nastech_state_schema.py/:** 2 changed files.
- **nastech_state_sessions.py/:** 33 changed files.
- **nastech_state_sessions_model_config.py/:** 1 changed files.
- **nastech_state_terminal.py/:** 5 changed files.
- **nastech_state_titles.py/:** 7 changed files.
- **nastech_state_usage.py/:** 8 changed files.
- **nastech_state_wal.py/:** 5 changed files.
- **nastech_state_worker_compression.py/:** 21 changed files.
- **nastech_state_worker_context.py/:** 5 changed files.
- **nastech_state_worker_lifecycle.py/:** 9 changed files.
- **nix/:** 2 changed files.
- **package-lock.json/:** 10 changed files.
- **package.json/:** 4 changed files.
- **plugin-catalog/:** 330 changed files.
- **plugins/:** 317 changed files.
- **pm/:** 8 changed files.
- **providers/:** 8 changed files.
- **pyproject.toml/:** 3 changed files.
- **ruff.strict.toml/:** 1 changed files.
- **run_agent.py/:** 1 changed files.
- **scripts/:** 71 changed files.
- **tests/:** 4174 changed files.
- **tests-js/:** 2 changed files.
- **tools/:** 383 changed files.
- **trajectory_compressor.py/:** 1 changed files.
- **tui_gateway/:** 390 changed files.
- **ui-tui/:** 695 changed files.
- **utils.py/:** 1 changed files.
- **uv.lock/:** 5 changed files.
- **web/:** 32 changed files.
- **website/:** 485 changed files.

## Delivered improvements

### New capabilities

- feat(plugin-catalog): add nastech-gensyn-ree
- feat: add Nextcloud Talk plugin catalog entry
- feat(plugin-catalog): add nastech-jina plugin
- feat(plugin-catalog): add DeadBolt reviewed artifact writer
- feat(plugin-catalog/vector): bump Vector Platform plugin to v0.5.3
- feat(plugin-catalog): add field-academy plugin
- feat(catalog): add Unraid plugin
- feat(plugin-catalog): add the voice-ledger catalog card
- feat(plugin-catalog): add voice-ledger
- feat(plugin-catalog): add the stop-ledger catalog card
- feat(plugin-catalog): add stop-ledger
- feat(plugin-catalog): add nastech-wslc-sandbox
- 202 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(browser): raise the redaction walk cap so real DOM trees survive
- fix(browser): cap redaction walks so nested page data cannot crash
- fix(home): mkdir_under_nastech_home always takes the elevated-grant path; no ImportError fallback
- fix(windows): repairing a left-behind dir also repairs what is inside it; the icacls tree fallback walks once
- fix(gateway): an unusable token-lock dir keeps the adapter retryable, so a token-only gateway stays up
- fix(windows): a refusal names only a gateway proved by its process identity
- fix(update): an operator-linked NASTECH_HOME is repaired, and an empty repair stays owed
- fix(windows): a recreated dir gets the elevated grant again
- fix(windows): the icacls fallback refuses every link in the subtree
- fix(windows): media capture grants keep the home provenance of the store
- fix(windows): an existing dir an elevated run left is repaired, not an error
- fix(windows): elevated ACL grants never follow a junction or link out of the home
- 1957 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(gateway): resolve the route paths only on a frozen-secret mismatch
- perf(desktop): track a pending submission without scanning the journal
- perf(gateway): A2A forward and hosted-room member creation commit off the owner loop
- perf(gateway): the Bot Chat a first delivery mints commits off the owner loop
- perf(gateway): native admission derives its route without re-hashing captured media
- perf(gateway): publish_execution fences on the executing generation, not the ledger
- perf(gateway): the session listener serves local clients without importing the dashboard app
- perf(gateway): config load imports only the platform adapters a profile configures
- perf(gateway): overlap the cold-start toolchain probe and notice READY sooner
- perf(cli): a chat client no longer spawns the MCP servers its gateway owns
- perf(state): index worker_executions(session_id,status) and probe a lineage in one query
- perf(state): bound the retired-media owner check to one messages pass
- 2 additional performance updates are included in this verified snapshot.

### Documentation

- docs(cli): Ctrl+D during a gateway turn leaves the turn running
- docs(gateway): name the commit that added each later policy field
- docs(plugin-catalog/vector): new vector plugin image. Same version, same code.
- docs: pin nastech-muse v0.1.9 proactive guidance
- docs: pin nastech-muse v0.1.8 verified direct delivery
- docs: pin nastech-muse v0.1.7 direct patrol delivery
- docs: pin nastech-muse v0.1.6 signal source fix
- docs: repin nastech-muse v0.1.5 with weekly and monthly reviews
- docs(catalog): pin nastech-muse 0.1.2 feature coverage
- docs(catalog): pin nastech-muse 0.1.1 with its project background
- docs(catalog): X Chat card says Nastech runs as the account you connect
- docs(platforms): adding-a-platform guides point at the plugin declarations
- 87 additional documentation updates are included in this verified snapshot.

### Improvements

- chore: map contributor email for TurgayAcar49
- Merge pull request #140490 from Nastechresearch/fix/pkg9-windows
- Merge pull request #140487 from Nastechresearch/fix/pkg9-schema-drift
- test(tools): inject the delegation schema failure on the cursor replay
- Merge pull request #140489 from Nastechresearch/fix/pkg9-detach
- Merge pull request #140472 from Nastechresearch/fix/pkg9-tui-skills
- Merge pull request #140488 from Nastechresearch/fix/pkg9-config-scope
- test(windows): run the real windows_home_acl update step against a stranded home on Windows CI
- refactor(update): the windows_home_acl step lives in nastech_cli/update_windows_acl.py
- refactor(windows): one TokenElevation probe for grants, refusal naming and the service installer
- refactor(media): grant the unresolved store path directly; drop the _grant_path seam
- refactor(gateway): no re-export shims for the split status/base helpers; the lock split is one-way
- 1176 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
