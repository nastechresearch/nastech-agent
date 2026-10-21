# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 271 commits affecting 3315 files.
- **Source revision:** `369cc6b07f26`.
- **Previous source revision:** `edeefe514f49`.

## Technical coverage

- **.github/:** 29 changed files.
- **agent/:** 5 changed files.
- **apps/:** 33 changed files.
- **contributors/:** 23 changed files.
- **gateway/:** 3 changed files.
- **locales/:** 1 changed files.
- **nastech_cli/:** 26 changed files.
- **nastech_platform/:** 1 changed files.
- **nastech_state_messages.py/:** 3 changed files.
- **optional-mcps/:** 1 changed files.
- **plugin-catalog/:** 181 changed files.
- **plugins/:** 5 changed files.
- **pm/:** 1 changed files.
- **scripts/:** 16 changed files.
- **tests/:** 53 changed files.
- **tests-js/:** 3 changed files.
- **tools/:** 23 changed files.
- **tui_gateway/:** 2 changed files.
- **web/:** 3 changed files.
- **website/:** 23 changed files.

## Delivered improvements

### New capabilities

- feat(mcp-catalog): add RentAHuman hosted MCP
- feat(shared-metrics): offer two consent answers, drop collect-only
- feat(ci): pin docker buildx version to v0.31.8
- feat(catalog): pin mcp-plugin-creator to 0.2.1 (review fixes)
- feat(catalog): add mcp-plugin-creator
- feat(plugin-catalog): bump xmemo to 1.2.1 (499a383)
- feat(plugin-catalog): add aave-mcp
- feat(plugin-catalog): add llmslim plugin
- feat(plugin-catalog): add day-panel plugin
- feat(plugin-catalog): add draft-cards plugin
- feat(plugin-catalog): add hermetic
- feat(plugin-catalog): add sunshine-moonlight entry
- 39 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(gateway): make the ownership-refusal stamp durable before the hard exit
- fix(gateway): let the startup_failed stamp clear the way instead of parking the unit
- fix(gateway): park a unit on unprovable --replace ownership instead of restart-looping
- fix(gateway): a detached root gateway no longer boots the sticky active profile
- fix(gateway): --detach keeps --force, covers --all, and older runtimes still restart
- fix(desktop): a stale-gateway restart no longer turns the app's restart call into the gateway
- fix: judge a skill_manage rollback failure by its error text only
- fix: a skill_manage batch whose rollback failed stays a visible failure
- fix: a refused skill_manage write reads neutral, not as a red failure
- fix(install-e2e): desktop smoke accepts the canonical gateway Desktop attaches to
- fix(terminal): no poll() fallback for a macOS PTY
- fix(terminal): never report a selector setup failure as EOF
- 26 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(desktop): reuse Developer ID signatures for loose macOS payload binaries
- perf(release): stage candidates from metadata; verify package bytes at publish
- perf(release): blobless history for release checkouts
- perf(release): give Windows bundle assembly caches that actually restore
- perf(release): submit the Store package beside verify-published
- perf(ci): stop transporting node_modules in the desktop dependency snapshot

### Documentation

- docs(user-stories): add fourteen more community stories
- docs(quickstart): link User Stories from Next Steps
- docs(user-stories): add eleven community stories, swap one author's tile for a stronger post
- docs(zh-Hans): move skills that left the bundled set out of the zh-Hans bundled catalog
- docs: fix two dead anchors and list three orphaned guides in the sidebar
- docs(release): stable-store comment says who releases the held submission

### Improvements

- test: Termux assembly test skips when the Docker daemon hangs instead of failing main
- ci: install/update leg runner defaults to ubuntu-latest again
- ci: run install/update E2E on GitHub-hosted runners again
- Merge pull request #142350 from Nastechresearch/feat/shared-metrics-two-choice-consent
- ci: run registry-side imagetools jobs on current buildx
- Merge pull request #142306 from Nastechresearch/fix/desktop-smoke-canonical-gateway
- ci: re-enable smoke windows and macos on non-gh runners
- chore: map contributor email for aholten
- Update base_output.py
- chore: map contributor email for yunze7373
- chore: map contributor email for mbgulden
- chore(catalog): review disclosure for kanban-stream
- 158 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
