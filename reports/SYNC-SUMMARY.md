# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 66 commits affecting 1377 files.
- **Source revision:** `0dfba37b11ff`.
- **Previous source revision:** `5fc308a70719`.

## Technical coverage

- **agent/:** 1 changed files.
- **apps/:** 7 changed files.
- **cli-config.yaml.example/:** 3 changed files.
- **contributors/:** 6 changed files.
- **cron/:** 6 changed files.
- **gateway/:** 28 changed files.
- **model_tools.py/:** 1 changed files.
- **nastech_cli/:** 24 changed files.
- **nastech_state.py/:** 7 changed files.
- **nastech_state_common.py/:** 1 changed files.
- **optional-skills/:** 1 changed files.
- **plugins/:** 25 changed files.
- **pyproject.toml/:** 1 changed files.
- **skills/:** 3 changed files.
- **tests/:** 68 changed files.
- **tools/:** 5 changed files.
- **tui_gateway/:** 5 changed files.
- **uv.lock/:** 1 changed files.
- **website/:** 14 changed files.

## Delivered improvements

### New capabilities

- feat(plugins): wire plugin platform handlers into a2a, buzz, and qqbot adapters
- feat(plugins): generalize native platform handler registration to every gateway platform
- feat(plugins): let plugins register Telegram PTB handlers via ctx.register_telegram_handler
- feat(wecom): native reply streaming (per-turn isolation, dedup-safe delivery, interaction boundaries)
- feat(gateway): per-platform streaming config default for WeCom
- feat(skills): publish-site — versioned website publishing to GitHub/Cloudflare/Netlify Pages

### Reliability and fixes

- fix(dashboard): trust configured reverse proxies (#94126)
- fix(tui-gateway): spare durable rows while a sibling backend holds them
- fix(cli): keep Desktop liveness leases when the session cap is off
- fix(gateway): disarm the heartbeat writer in _stop_loop_liveness_guards
- fix(gateway): a single tick-socket miss must not authorize the wedge kill
- fix(gateway): interlock the stale-heartbeat wedge verdict with a loop-scheduling witness
- fix(gateway): the loop watchdog's own heartbeat can freeze the loop it watches
- fix(state.db): cross-backend heartbeat gates orphan sweep
- fix(model): coerce YAML integer provider names before picker/CRUD
- fix(desktop): unwrap Mistral Voxtral JSON in client-direct STT
- fix(desktop): retain remote owner after session resume
- fix(desktop): recover cloud auth through portal (#96170)
- 23 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(cron): comment accuracy — booking is fail-open on probe errors; cross-ref status vocabulary
- docs(cron): pin the manual_run_at comparison as intentionally string-exact
- docs: document the database section (journal_mode, synchronastech, WAL sizing)
- docs(state): call the macOS synchronastech rule a floor, not a pin
- docs(sessions): name the reachable ordinal-0 rewind path in the #95868 guards

### Improvements

- chore: suppress posix-gated os.kill probe in footgun scan; map rodrigogs in AUTHOR_MAP
- test(gateway): adapt witness-composition harness to the SIGUSR1 in-place drain path
- docs+test(gateway): pin Windows witness-absent behavior and the probe-budget math
- refactor(gateway): simplify witness-probe ambiguity arms; sweep stale tick-socket nodes; clean test tempdirs
- test: short tmp_path for loop-tick witness sockets (macOS AF_UNIX limit)
- test(model): cover numeric YAML provider keys in picker and CRUD
- fmt(js): `npm run fix` on merge (#96506)
- test(desktop): cover Voxtral JSON unwrap on client-direct STT
- review: tighten pre-call gate comment; drop redundant _ReadyAdapter test stub
- chore: map contributor email for deadczarvc
- test(cron): stale hand-edit without manual marker still re-anchors
- test(gateway): end-to-end rendered-unit coverage for the cron drain floor
- 8 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
