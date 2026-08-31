# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 68 commits affecting 1410 files.
- **Source revision:** `a9c783f21995`.
- **Previous source revision:** `26350357d76e`.

## Technical coverage

- **.gitignore/:** 1 changed files.
- **SOUL.md/:** 1 changed files.
- **agent/:** 47 changed files.
- **apps/:** 6 changed files.
- **cli-config.yaml.example/:** 1 changed files.
- **cli.py/:** 2 changed files.
- **contributors/:** 4 changed files.
- **evals/:** 2 changed files.
- **gateway/:** 20 changed files.
- **nastech_cli/:** 11 changed files.
- **nastech_state.py/:** 1 changed files.
- **optional-skills/:** 153 changed files.
- **plugins/:** 10 changed files.
- **run_agent.py/:** 4 changed files.
- **skills/:** 38 changed files.
- **tests/:** 92 changed files.
- **tools/:** 14 changed files.
- **tui_gateway/:** 15 changed files.
- **ui-tui/:** 1 changed files.
- **website/:** 208 changed files.

## Delivered improvements

### New capabilities

- feat(bot-mode): run same-gateway Group Chats without Desktop
- feat(delegation): surface config-level model_not_found notice in delegation batch reports
- feat(bot-mode): Group Chats survive the authority gateway dying — log replication and fenced takeover
- feat(bot-mode): replay pages carry authority lineage; pin byte-bounded replay
- feat(bot-mode): add durable Group Chat authority and replay
- feat(photon): read-receipt toggle, receipt-type alias, docs
- feat(photon): support iMessage read receipts
- feat(compaction): system prompt always rebuilds at the commit boundary — updates finally reach long-lived sessions (#98426)

### Reliability and fixes

- fix(desktop): surface persistent group holds
- fix(bot-mode): avoid inherited stdin on Windows
- fix(tools): surface config-level model_not_found notices in delegation batch reports
- fix(delegation): report failed children as failed, not completed
- fix(bot-mode): cancel re-routes on worker races instead of failing disband
- fix(delegation): pin failure-status edge cases and document exit_reason enum
- fix(delegation): report provider-failed subagents as failed, not completed/max_iterations
- fix(compression): keep estimate seam positional-compatible for monkeypatched estimators
- fix(compression): route-aware stale-thinking charge parity between compaction trigger and tail walks (#84371)
- fix: failed subagents now surface a clean error to the user (CLI + gateway)
- fix(gateway): compact the live codex thread instead of no-op mirror rewrites (#73503)
- fix(compression): scope worker-teardown grace to the total-ceiling path
- 30 additional reliability and fixes updates are included in this verified snapshot.

### Improvements

- chore: map contributor email for @sambai-dev
- chore: map contributor email for itskaism
- test: adapt #97667 rejection-notice tests to the config-reading implementation on main
- test: drop duplicate failed-flag regression test superseded by TestDelegateFailedChildStatus
- test(compression): drop moot digest-loop tests; match stamped backoff errors
- test(compression): pin attempt-lifecycle contracts (#97488 #96775)
- test(compression): cover stall-interrupt vs early /stop backoff (#96775)
- test(compression): isolate deadline timing assertions
- test(compression): isolate commit overrun scheduling
- refactor(skills): clarify _find_skill docstring, narrow _local_root except
- refactor(skills): short-circuit bare-name match before resolve machinery
- test: cron ContextVar-masking test now uses a chat platform
- 6 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
