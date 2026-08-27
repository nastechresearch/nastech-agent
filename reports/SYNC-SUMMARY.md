# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 50 commits affecting 1375 files.
- **Source revision:** `5fc308a70719`.
- **Previous source revision:** `ef46ec03e114`.

## Technical coverage

- **agent/:** 7 changed files.
- **apps/:** 43 changed files.
- **contributors/:** 7 changed files.
- **cron/:** 1 changed files.
- **evals/:** 2 changed files.
- **gateway/:** 4 changed files.
- **nastech_cli/:** 20 changed files.
- **nastech_state.py/:** 1 changed files.
- **pyproject.toml/:** 1 changed files.
- **tests/:** 33 changed files.
- **tools/:** 9 changed files.
- **tui_gateway/:** 2 changed files.
- **uv.lock/:** 1 changed files.
- **website/:** 6 changed files.

## Delivered improvements

### New capabilities

- feat(models): add GLM-5.3-Flash to z.ai and OpenCode Go pickers
- feat(desktop): Stop button for a running group-chat round (#94570)
- feat(models): add Inkling free models to OpenRouter catalog
- feat(models): add minimax/minimax-m3:free to OpenRouter picker (#96234)
- feat(desktop): read-only stored-transcript resume + legacy owner-backfill trigger (#94724)
- feat(sessions): one-shot single-match owner backfill for legacy NULL-profile rows (#94724)
- feat(desktop): browser_exec rows use the leading # comment as their title, matching CLI/TUI (#96093)

### Reliability and fixes

- fix(deadline): remove the dead second SuspectableBackend class shadowing the Phase 3a Protocol
- fix(gateway): preserve exception type when error string is empty (#78183)
- fix(serve): review follow-ups — never-raise sentinel fallback, DEVNULL stderr in split-stream test
- fix(serve): widen fd-1 sentinel write to BACKEND_PORT_IN_USE sibling site
- fix(serve): announce READY sentinel on fd 1, not the redirected sys.stdout
- fix(agent): honor explicit free OpenRouter models
- fix(models): delist openrouter/elephant-alpha (no longer served by OpenRouter)
- fix(desktop,bots): render "(empty)" sentinel as a friendly message in group chat
- fix(desktop/bots): keep a substantive group reply after a synthetic (pass)
- fix(desktop): real stop primitive for group-chat rounds (#91868, #94569)
- fix(nastech_cli): scope hook timeouts and fail closed on pre_tool_call
- fix(browser): inline windows-footgun annotation for os.kill(pid, 0) (#85125 CI)
- 17 additional reliability and fixes updates are included in this verified snapshot.

### Improvements

- chore: release v0.20.6 (2026.8.27)
- chore(contributors): map me@kitsonkelly.com -> kitsonk
- refactor(browser_exec): schema diet 803->663 tok/call, A/B-gated; eval harness runs on Windows + Nastech auth (#96300)
- chore(contributors): map aydinhrrs@gmail.com -> RibatTRW
- test(desktop/bots): drop unused prompt params in empty-sentinel harness (lint)
- test(desktop/bots): pin harvestStrandedGroupReply's rescued-delivery path
- test(desktop): lock the Stop button to room.running and the stop primitive
- test(cron): pin lock-first liveness + harden lock-probe failure
- chore: contributor email mapping for ekzhang
- fmt(js): `npm run fix` on merge (#96263)
- desktop: fix two managed-SSH-spawn bugs that break every fresh remote backend
- Merge pull request #86412 from kshitijk4poor/salvage/83225-overflow-clamp
- 2 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
