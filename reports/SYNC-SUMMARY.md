# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 703 commits affecting 1534 files.
- **Source revision:** `3ea71a47b3f8`.
- **Previous source revision:** `7cd91114b462`.

## Technical coverage

- **.github/:** 8 changed files.
- **.gitignore/:** 1 changed files.
- **agent/:** 165 changed files.
- **apps/:** 470 changed files.
- **cli-config.yaml.example/:** 15 changed files.
- **cli.py/:** 12 changed files.
- **contributors/:** 45 changed files.
- **cron/:** 37 changed files.
- **docs/:** 24 changed files.
- **evals/:** 11 changed files.
- **gateway/:** 119 changed files.
- **locales/:** 17 changed files.
- **model_tools.py/:** 2 changed files.
- **nastech_cli/:** 293 changed files.
- **nastech_constants.py/:** 1 changed files.
- **nastech_state.py/:** 28 changed files.
- **nastech_state_common.py/:** 8 changed files.
- **nastech_state_holders.py/:** 2 changed files.
- **nastech_state_portability.py/:** 1 changed files.
- **nastech_state_registry.py/:** 2 changed files.
- **nastech_state_schema.py/:** 8 changed files.
- **nastech_state_search.py/:** 6 changed files.
- **plugins/:** 71 changed files.
- **providers/:** 3 changed files.
- **pyproject.toml/:** 6 changed files.
- **run_agent.py/:** 14 changed files.
- **scripts/:** 16 changed files.
- **setup-nastech.sh/:** 2 changed files.
- **tests/:** 674 changed files.
- **tools/:** 136 changed files.
- **toolsets.py/:** 2 changed files.
- **tui_gateway/:** 37 changed files.
- **ui-tui/:** 32 changed files.
- **uv.lock/:** 5 changed files.
- **web/:** 6 changed files.
- **website/:** 96 changed files.

## Delivered improvements

### New capabilities

- feat(models): add Meta Muse Spark 1.3 family to picker
- feat(models): add Muse Spark contributor to OpenRouter
- feat(opencode): send x-opencode-session on every OpenCode request for backend affinity
- feat(meta-ai): live-first model catalog + generic contributor warning
- feat(search): add fast discovery file ordering
- feat(browser): give Lightpanda an on-disk HTTP cache
- feat(cli): filter MCP server spawning by -t/--toolsets flag + fix orphan subprocess leak
- feat(config): context_file_read_timeout key + narrow reader catch
- feat(desktop): group a comment batch by page region so it lands as a few tasks
- feat(desktop): browser comments carry the element's selector, markup, and styles
- feat: delegation batch tags read "set N" instead of a hex id slice
- feat(providers): let an external-process provider ship out of tree
- 32 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(desktop): refresh Bot Chat transcript when a roster click fronts an already-open tab
- fix(desktop): toast action is a real button, not a hairline text link
- fix(prompt): Muse Spark gets tool-use enforcement + execution guidance on defaults (#96550)
- fix(models_dev): alias opencode-free to the Zen "opencode" catalog; pin Muse Spark 1M invariant
- fix(context): resolve commandcode models via live /models
- fix(context): add muse-spark 1M fallback (zen/GO SG showed 256k)
- fix(models): correct contributor guard, 1M context, docs for muse-spark-1.3
- fix(meta-ai): declare supports_vision_tool_messages=False — Muse Spark 400s on image tool results
- fix(vision): honor supports_vision_tool_messages=False in tool-result media gates
- fix(inventory): reword pending-entitlement warning to avoid Windows footgun false positive
- fix(inventory): explain the locked Nastech list while entitlement is pending
- fix(gateway): keep first model picker open responsive on cold pricing cache
- 416 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(state): exclude cron sessions from trigram FTS
- perf(agent): stop rebuilding the streamed reply text on every delta
- perf(mcp): skip npx's resident parent when the package is already cached
- perf(usage): prefer bundled pricing before metadata fetch
- perf(cron): 1 MiB walk budget; document the independent pre-scan budget
- perf(cron): bound the lifecycle guard's whole-walk scan work
- perf(mcp): apply the -t spawn filter before the mcp SDK import
- perf(file-ops): count the native read's tail with memchr; reuse the local-env gate
- perf(file-ops): native read_file fast path on local POSIX environments
- perf(file-ops): merge write_file's pre-write probes into one shell call
- perf(file-ops): collapse read_file's shell probes into one compound command
- perf(mcp): one parent-death supervisor per process, not one per stdio server
- 12 additional performance updates are included in this verified snapshot.

### Documentation

- docs(meta-ai): trim live catalog comments
- docs(meta-ai): point contributor pricing to live page
- docs: document context_file_read_timeout in configuration.md
- docs(curator): carry over the #91449 growth rationale for the .git exclusion
- docs(multiplex): list teams among port-binding platforms
- docs(google-chat): document per-profile scoping and ADC fail-closed under multiplex
- docs(profiles): cron delivery for routed profiles rides the shared bot only for exact routed targets (#101113)
- docs: ${VAR} config refs resolve per-profile under a multiplexed gateway
- docs(design): note loader-boundary dotenv guard, scoped ${VAR} expansion and scoped .env publish in multiplexing design doc
- docs(design): add the multiplexing-gateway design doc referenced by secret_scope
- docs(sessions): explain why the canonical Bot Chat guard is provenance-blind (#99517)
- docs: terminal settings resolve per profile under multiplexing
- 9 additional documentation updates are included in this verified snapshot.

### Improvements

- chore(contributors): map sosxradar@gmail.com -> GTHell
- chore(contributors): map csreyes92@gmail.com -> csreyes (salvage #93073)
- test(desktop): trim Bot Chat pane-focus regression to the two invariant cases
- fmt(js): `npm run fix` on merge (#101952)
- [verified] fix(cron): close restart handoff races
- [verified] fix(cron): harden gateway restart handoff
- [verified] fix(cron): preserve active runs across gateway restart
- refactor(config): close empty-list root gap in strict check; assert tolerant returns
- chore: add EmanueleCornaggia to contributor map (#101778 salvage)
- Merge pull request #101936 from kshitijk4poor/test/101922-rearm-reset-public-boundary
- test(compression): pin rearm-reset wiring through a public boundary
- test(agent): cover streamed argument materialization
- 174 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
