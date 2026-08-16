# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 226 commits affecting 1161 files.
- **Source revision:** `7095e23eb206`.
- **Previous source revision:** `4ef56cef4c6e`.

## Technical coverage

- **AGENTS.md/:** 1 changed files.
- **agent/:** 34 changed files.
- **apps/:** 304 changed files.
- **batch_runner.py/:** 1 changed files.
- **cli-config.yaml.example/:** 1 changed files.
- **cli.py/:** 12 changed files.
- **contributors/:** 20 changed files.
- **cron/:** 6 changed files.
- **docs/:** 1 changed files.
- **evals/:** 24 changed files.
- **gateway/:** 16 changed files.
- **hermes_cli/:** 77 changed files.
- **hermes_state.py/:** 10 changed files.
- **hermes_state_common.py/:** 1 changed files.
- **model_tools.py/:** 1 changed files.
- **plugins/:** 5 changed files.
- **run_agent.py/:** 5 changed files.
- **scripts/:** 3 changed files.
- **skills/:** 6 changed files.
- **tests/:** 152 changed files.
- **tools/:** 24 changed files.
- **tui_gateway/:** 16 changed files.
- **web/:** 6 changed files.
- **website/:** 25 changed files.

## Delivered improvements

### New capabilities

- feat(desktop-sdk): expose focused-session state atoms to plugins
- feat(desktop): running is not busy
- feat(desktop): paste-anything MCP server import
- feat(desktop): expose busy turn flags on plugin SDK
- feat(desktop): make the multi-gateway Connections registry discoverable
- feat(desktop): background MCP health checks with re-auth nudges
- feat(desktop): nastech:// deep link to install MCP servers with explicit confirmation
- feat(desktop): MCP fleet cost/usage overlay with schema token estimates and 30-day usage
- feat(desktop-sdk): host.deleteProfile — teardown-routed profile delete for plugins
- feat(desktop): unify MCP Servers and Catalog into one coherent list
- feat(hooks): pre_tool_call content transformation via `modify` directive
- feat(desktop): drag-resizable panes on the Capabilities Skills tab
- 14 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(agent): attribute background-review usage and add cost controls
- fix(cli): bound the Windows process-scan probes so a slow WMI scan cannot wedge nastech update (#87134)
- fix(acp): make --acp probe tri-state, cached, and mock-safe
- fix(acp): probe CLI for --acp support before spawning subprocess
- fix(cli): address review feedback on chat -c fail-loudly PR
- fix(cli): chat -c fails loudly on stderr and gains --create-if-missing
- fix(gateway): complete /loop ticks after streamed already_sent turns
- fix(auth): only fall back to os.getenv on ImportError in resolve_provider (#86918 review)
- fix(auth): resolve provider auto-detection keys through the profile scope (#86917)
- fix(cron): coerce script_path to str in the NUL guard so it can never crash (#86829, review #86832)
- fix(cron): reject NUL-bearing script paths before any Path call (#76762 class)
- fix(tui): stop queued dispatch after session close
- 139 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(desktop): hydrate transcripts with a small tail page + on-demand older-page backfill
- perf(caching): narrow the widened capability lookup to the LiteLLM grant
- perf(desktop): make session resume incremental

### Documentation

- docs(agents): record multiplex profile-scoped env fail-closed rule (#86905)
- docs: full multi-gateway setup guide for Nastech Desktop
- docs(desktop): document profile scope helpers
- docs(tui): document defer_history vs omit_messages precedence
- docs(evals): real Codex CLI head-to-head arm + results
- docs(evals): ship transcript-building scripts + full eval detail in-repo
- docs(evals): 4-transcript compaction scorecard
- docs: add Connecting Desktop to Many Nastech Instances guide

### Improvements

- test(cli): retarget the wmic-encoding regression test at bounded_probe_run
- chore: map contributor email for @yflmq001
- test(gitlock): pin the git-process guard in sweep tests (deflake slice 8)
- test(auth): cover profile-scoped key resolution in resolve_provider (#86917)
- test(cron): pin the eager NUL rejection contract for _run_job_script (#86829)
- refactor(gateway): share breakaway marker constant
- Merge pull request #87630 from kshitijk4poor/fix/kitty-extended-keys-proper
- chore: map contributor email for focused-session atoms salvage
- test(desktop-sdk): contract-test the focused-session host.state atoms
- fmt(js): `npm run fix` on merge (#87607)
- fmt(js): `npm run fix` on merge (#87599)
- chore(contributors): map emails for P2-sweep salvage wave
- 26 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
