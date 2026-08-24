# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 162 commits affecting 1334 files.
- **Source revision:** `057dcdf236f8`.
- **Previous source revision:** `c584d15cdc31`.

## Technical coverage

- **Dockerfile/:** 1 changed files.
- **agent/:** 26 changed files.
- **apps/:** 182 changed files.
- **batch_runner.py/:** 2 changed files.
- **cli.py/:** 7 changed files.
- **contributors/:** 11 changed files.
- **cron/:** 10 changed files.
- **gateway/:** 22 changed files.
- **nastech_cli/:** 37 changed files.
- **nastech_constants.py/:** 2 changed files.
- **nastech_state.py/:** 7 changed files.
- **nastech_state_portability.py/:** 1 changed files.
- **plugins/:** 6 changed files.
- **run_agent.py/:** 9 changed files.
- **scripts/:** 5 changed files.
- **tests/:** 108 changed files.
- **tools/:** 20 changed files.
- **tui_gateway/:** 33 changed files.
- **ui-tui/:** 3 changed files.
- **web/:** 3 changed files.
- **website/:** 7 changed files.

## Delivered improvements

### New capabilities

- feat(shared): heartbeat and socket-generation invalidation in JsonRpcGatewayClient
- feat(gateway): add gateway.ping heartbeat wire contract
- feat(cron): add explicit one-shot re-arm
- feat(desktop): HUD game-overlay mode

### Reliability and fixes

- fix(desktop): polish HUD movement and resizing on X11
- fix(desktop): add a HUD layout reset control
- fix(desktop): keep the Linux HUD clickable and recoverable
- fix(desktop): debounce and re-verify zoom on Linux Wayland
- fix(desktop): move the Linux HUD with a native compositor drag
- fix(mcp): resolve tool-call timeouts via the unified deadline layer (#85125 2g)
- fix(cron): share liveness helper with CLI and extend it to cronjob list
- fix(cron): surface gateway liveness in cronjob tool results (#87033)
- fix(tui): heartbeat and bounded reconnect for silent WebSocket drops
- fix(desktop-update): use the system default browser for the update shim
- fix(desktop): hold a per-turn socket lease so group-chat member turns survive the runtime-session reaper (#93602)
- fix(desktop): scope branch-opens-primary to the currently selected session
- 91 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(desktop): document Linux and Wayland HUD behavior
- docs(auth): correct the SameSite contract in the cookie source docs

### Improvements

- Merge pull request #93830 from kshitijk4poor/fix/85125-2g-mcp-timeout-resolution
- Merge pull request #93826 from kshitijk4poor/fix/85125-2f-telegram-deadline-migration
- refactor(telegram): migrate _await_with_thread_deadline onto agent.deadline.run_bounded_async (#85125 2f)
- refactor(cron): parameterize liveness warning plurality, drop fragile string replace
- Merge pull request #93793 from Nastechresearch/salv/autospeak-test-93540
- test: drop unused param in group-turn lease mock (lint)
- Merge pull request #93773 from kshitijk4poor/fix/codex-sdk-transform-bypass-93650-v2
- Merge pull request #93784 from Nastechresearch/salv/81234-retry-carrier
- test(desktop): pin auto-speak silence across an Edge TTS fallback id rewrite
- test(terminal): harden watch_patterns lifetime cap — delivered-only counting, Nth-delivery promotion, docstring
- test(bot-relay): match delivery CLI by basename in argv filters
- test(model_metadata): lock in max_tokens last-resort fallback + cache self-heal
- 41 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
