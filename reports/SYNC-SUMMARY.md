# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 10866 commits affecting 2755 files.
- **Source revision:** `af8839df1038`.
- **Previous source revision:** `8df0a0379378`.

## Technical coverage

- **%SystemDrive%/:** 8 changed files.
- **.dockerignore/:** 5 changed files.
- **.env.example/:** 5 changed files.
- **.gitattributes/:** 1 changed files.
- **.github/:** 607 changed files.
- **.gitignore/:** 22 changed files.
- **.python-version/:** 1 changed files.
- **AGENTS.md/:** 27 changed files.
- **COMPAT_MANIFEST.md/:** 5 changed files.
- **CONTRIBUTING.es.md/:** 7 changed files.
- **CONTRIBUTING.md/:** 25 changed files.
- **Dockerfile/:** 27 changed files.
- **README.es.md/:** 4 changed files.
- **README.md/:** 6 changed files.
- **README.ur-pk.md/:** 4 changed files.
- **README.zh-CN.md/:** 4 changed files.
- **acp_adapter/:** 63 changed files.
- **activate/:** 15 changed files.
- **activate.fish/:** 1 changed files.
- **activate.ps1/:** 11 changed files.
- **agent/:** 2171 changed files.
- **apps/:** 11978 changed files.
- **assets/:** 24 changed files.
- **batch_runner.py/:** 2 changed files.
- **cli-config.yaml.example/:** 31 changed files.
- **cli.py/:** 49 changed files.
- **compat_manifest.json/:** 5 changed files.
- **constraints-termux.txt/:** 2 changed files.
- **contributors/:** 624 changed files.
- **cron/:** 328 changed files.
- **datagen-config-examples/:** 1 changed files.
- **docker/:** 12 changed files.
- **docs/:** 42 changed files.
- **eslint.config.shared.mjs/:** 1 changed files.
- **evals/:** 89 changed files.
- **gateway/:** 1330 changed files.
- **hicortex.yaml/:** 2 changed files.
- **locales/:** 368 changed files.
- **mini_swe_runner.py/:** 2 changed files.
- **model_tools.py/:** 6 changed files.
- **nastech/:** 2 changed files.
- **nastech_bootstrap.py/:** 21 changed files.
- **nastech_cli/:** 4786 changed files.
- **nastech_constants.py/:** 56 changed files.
- **nastech_constants_scratch.py/:** 2 changed files.
- **nastech_logging.py/:** 17 changed files.
- **nastech_platform/:** 28 changed files.
- **nastech_startup_watchdog.py/:** 3 changed files.
- **nastech_state.py/:** 44 changed files.
- **nastech_state_common.py/:** 21 changed files.
- **nastech_state_compression.py/:** 13 changed files.
- **nastech_state_coverage.py/:** 2 changed files.
- **nastech_state_dbfile.py/:** 2 changed files.
- **nastech_state_errors.py/:** 6 changed files.
- **nastech_state_fts.py/:** 3 changed files.
- **nastech_state_gateway.py/:** 10 changed files.
- **nastech_state_health.py/:** 1 changed files.
- **nastech_state_holders.py/:** 8 changed files.
- **nastech_state_identity.py/:** 6 changed files.
- **nastech_state_ids.py/:** 3 changed files.
- **nastech_state_lockguard.py/:** 2 changed files.
- **nastech_state_lockowners.py/:** 2 changed files.
- **nastech_state_maintenance.py/:** 17 changed files.
- **nastech_state_messages.py/:** 64 changed files.
- **nastech_state_pidns.py/:** 5 changed files.
- **nastech_state_portability.py/:** 16 changed files.
- **nastech_state_profile_repair.py/:** 2 changed files.
- **nastech_state_registry.py/:** 3 changed files.
- **nastech_state_rewind.py/:** 4 changed files.
- **nastech_state_schema.py/:** 10 changed files.
- **nastech_state_search.py/:** 3 changed files.
- **nastech_state_sessions.py/:** 35 changed files.
- **nastech_state_telegram.py/:** 2 changed files.
- **nastech_state_timeline.py/:** 1 changed files.
- **nastech_state_titles.py/:** 5 changed files.
- **nastech_state_usage.py/:** 2 changed files.
- **nastech_state_user_copy.py/:** 2 changed files.
- **nastech_state_wal.py/:** 2 changed files.
- **nastech_time.py/:** 7 changed files.
- **nastech_wisdom/:** 1 changed files.
- **nastech_yaml.py/:** 3 changed files.
- **native/:** 1 changed files.
- **nix/:** 71 changed files.
- **optional-mcps/:** 27 changed files.
- **optional-skills/:** 83 changed files.
- **package-lock.json/:** 39 changed files.
- **package.json/:** 2 changed files.
- **plugin-catalog/:** 1204 changed files.
- **plugins/:** 888 changed files.
- **pm/:** 599 changed files.
- **providers/:** 31 changed files.
- **pyproject.toml/:** 106 changed files.
- **run_agent.py/:** 37 changed files.
- **scripts/:** 1215 changed files.
- **setup-nastech.ps1/:** 11 changed files.
- **setup-nastech.sh/:** 17 changed files.
- **setup.py/:** 1 changed files.
- **skills/:** 58 changed files.
- **test.txt/:** 2 changed files.
- **tests/:** 15282 changed files.
- **tests-js/:** 187 changed files.
- **tools/:** 1857 changed files.
- **toolsets.py/:** 9 changed files.
- **trajectory_compressor.py/:** 3 changed files.
- **tui_gateway/:** 778 changed files.
- **ui-tui/:** 486 changed files.
- **utils.py/:** 18 changed files.
- **uv.lock/:** 70 changed files.
- **venv_check/:** 2088 changed files.
- **web/:** 196 changed files.
- **website/:** 2481 changed files.

## Delivered improvements

### New capabilities

- feat(plugin-catalog): add omh community plugin
- feat(plugin-catalog): bump prompt-studio to 1.9.0
- feat(plugin-catalog): add talaria-webui
- feat(catalog): add Usage Ledger 0.4.3 Windows beta
- feat(plugin-catalog): add parcel-deliveries
- feat(plugin-catalog): add model-drift-watch
- feat(plugin-catalog): add parlor
- feat(catalog): add Ando platform beta plugin
- feat(plugin-catalog): add mistral-vibe plugin
- feat(plugin-catalog): pin pushover-nastech-plugin to bbfea17
- feat(plugin-catalog): add pushover-nastech-plugin
- feat(pii): add nastech-pii plugin configuration
- 728 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(google-workspace): emit [] for empty Python-backend Gmail searches
- fix(desktop): let the zone menu grow so spelled-out shortcuts stay visible
- fix(plugins): --install-deps probe imports from the synced environment
- fix(tui_gateway): reopen the finalized row in the compute-host child, not _run_prompt_submit
- fix(tui_gateway): reopen a finalized row before the isolated compute-host dispatch too (#85303 review)
- fix(state): retire never-drained queue rows on the read-only mount paths too (#128508, #125577)
- fix(tui_gateway): mounting a finalized session no longer reopens its row — the first real turn does (#85303)
- fix(kanban): use unknown fallback for worker failure_reason and add test
- fix(kanban): stop goal loop on worker/judge failures (#91264)
- fix(install): let NASTECH_RUNTIME_DIR decide where the guarded store lands
- fix(install): decode launcher path captures as UTF-8 and refuse a NastechHome inside InstallDir
- fix(install): preserve Unicode Python paths in developer setup
- 5400 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(pm): attempt the libatomic install once per process
- perf(skills): skill_view's disabled check loads config once
- perf(skills): memoize the shadow identity decision, not only the warning
- perf(inventory): resolve fast capability once per model
- perf(tui_gateway): run session.save on the RPC pool
- perf(tui): bound the share_nastech client-text scrub to a 2x-cap window
- perf(debug): redact support egress once
- perf(logging): check a routed profile's liveness at most every 2 s
- perf(state): session-list subqueries stay on idx_messages_session under stale planner stats (#119403)
- perf(fallback): stamp the early-reopen throttle before loading the pool
- perf(desktop): defer mermaid admission one paint so the source fallback renders first
- perf(desktop): bound messages-below scroll measurements
- 77 additional performance updates are included in this verified snapshot.

### Documentation

- docs(tui_gateway): drop a stray comment marker inside the resume docstring
- docs(install): document the libatomic host package step
- docs(plugin-catalog): README and docs pages describe the same delisting, removal and entry fields
- docs(email): say an absent authserv_id pin fails closed for every sender
- docs(email): authserv_id is required for authenticated-sender mode
- docs: left-core migration table in plugins/AGENTS.md; HA tools sit behind Tool Search like every plugin tool
- docs: Home Assistant moves to the plugin catalog
- docs(desktop): note the local-secondary exception on the owner stamp helper
- docs(discord): include thread creation permission
- docs(state): trim derived-id recognizer comments to the contract
- docs(compression): drop stale split-turn clause from task-snapshot comment
- docs(skills): regenerate skill pages for the braced role-tag placeholders
- 289 additional documentation updates are included in this verified snapshot.

### Improvements

- test(google-workspace): type and shrink empty Gmail search regression test
- chore(contributors): map youcefcherid for attribution
- chore(plugin-catalog): omh disclosure at merge
- chore(plugin-catalog): repin omh to 021e5c63 and drop the host upper bound
- ci(plugin-catalog): full blobless checkout so Nastech resolves its version
- plugin-catalog: bump evalroute to v0.6.0
- chore(plugin-catalog): evalroute disclosure at merge
- plugin-catalog: bump evalroute to v0.5.1
- test(desktop): require the zone menu to fit a spelled-out shortcut
- test(tui_gateway): the resume guard fail-open proof is the history read, not the reopen (#85303)
- test(kanban): add tests for judge transport failure and worker failed stops (#91264)
- test(install): cover Unicode paths in Desktop hidden PowerShell hosts
- 4312 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
