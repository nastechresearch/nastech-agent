# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 130 commits affecting 1406 files.
- **Source revision:** `26350357d76e`.
- **Previous source revision:** `360761c8cf50`.

## Technical coverage

- **ANTHROPIC_ISSUES.md/:** 5 changed files.
- **RELATORIO_ANTHROPIC_OAUTH_BUGS.md/:** 6 changed files.
- **agent/:** 36 changed files.
- **apps/:** 46 changed files.
- **cli-config.yaml.example/:** 1 changed files.
- **cli.py/:** 5 changed files.
- **contributors/:** 12 changed files.
- **cron/:** 10 changed files.
- **docker/:** 1 changed files.
- **gateway/:** 9 changed files.
- **nastech_cli/:** 38 changed files.
- **nastech_state.py/:** 1 changed files.
- **optional-skills/:** 4 changed files.
- **plugins/:** 19 changed files.
- **run_agent.py/:** 1 changed files.
- **scripts/:** 3 changed files.
- **skills/:** 10 changed files.
- **tests/:** 128 changed files.
- **tools/:** 27 changed files.
- **tui_gateway/:** 11 changed files.
- **ui-tui/:** 16 changed files.
- **web/:** 2 changed files.
- **website/:** 62 changed files.

## Delivered improvements

### New capabilities

- feat(telegram): inline command picker — search every command and skill, no menu cap
- feat(mcp-oauth): Desktop MCP OAuth now completes against remote backends (client-side callback relay)
- feat(skills-hub): impeccable joins the optional-skills catalog, content pulled live from upstream
- feat(discord): expose /plan in the native slash-command picker
- feat: /plan graduates from bundled skill to built-in command on every surface
- feat(cli): add /plan command (#67264)
- feat(delegation): honor delegation.request_overrides on all three resolution branches with explicit-over-runtime merge precedence
- feat(delegation): forward delegation.request_overrides on direct-endpoint branch
- feat(tui): status rule shows cache-hit %, latency, t/s and honors display.status_bar.fields
- feat(desktop): real-profile browsing toggle in Capabilities → Tools → Browser
- feat: allow configured background review tools
- feat(cli): tui status bar per-field toggle + cache/latency/tps
- 9 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(todo): unversioned tool.start still merges after resume
- fix(browser): real-profile browsing runs headless — no focus-stealing window
- fix(security): widen the exfil substring-suffix fix to the skills-guard sibling patterns
- fix(tools): reduce false positives in exfil_curl/exfil_wget patterns
- fix(skills-hub): reconcile salvaged install fixes with full-directory fetch
- fix(skills): review follow-up — revision pinning, canonicalization, case-fold guards
- fix(skills): fetch explicitly linked same-directory siblings on install (#96310)
- fix(cli): skip unreachable support files instead of aborting URL skill install
- fix(compression): retire completed todo snapshots safely
- fix(compression): strip embedded stale todo snapshot from list message content
- fix(cron): coerce string repeat values on the UPDATE path too
- fix(browser): real-profile snapshot auth files are owner-only (#96729)
- 62 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(cron): bare durations are recurring; one-shot is 'in 30m'
- docs(cron): document natural day/time schedules and named cron fields
- docs: priority list now guarantees skill commands a Telegram menu slot
- docs(computer-use): drop remaining existing-profile grant references
- docs(computer-use): remove the deleted typed browser-page route
- docs(providers): note extra_body survives gateway turns and /model switches; map gitabtion attribution
- docs(cron): note request settings carry into scheduled runs
- docs(auth): record manual A/B validation of OAuth API-key shadowing fix
- docs: delegation.provider alongside base_url carries request overrides (#65035)
- docs: sync stale /background references with the /bg + /btw split

### Improvements

- test: add InlineQueryHandler to every fake telegram.ext module tree
- test: cover InlineQueryHandler in lazy-install rebind and handler-count contracts
- chore: map contributor email for fifeli
- skills hub: don't abort installs on missing referenced support files
- [verified] fix: ignore glob-shaped skill support paths
- test(cli): add install-flow E2E for skipped unreachable URL support file (#66760)
- test(cron): migrate one-shot-intent fixtures to the 'in 30m' form
- test(cron): use explicit one-shot duration syntax
- chore(attribution): map fabiantax@hotmail.com -> fabiantax (PR #90953 salvage)
- chore(release): map adamfortuna1324@gmail.com to 0xAdamFortuna
- test(gateway): reused-agent merge-not-overwrite regression via real _run_agent
- chore(attribution): map bsbofmusic noreply email
- 13 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
