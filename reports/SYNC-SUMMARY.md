# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 228 commits affecting 2888 files.
- **Source revision:** `0240fa4a8412`.
- **Previous source revision:** `cc75e8f4021f`.

## Technical coverage

- **.github/:** 6 changed files.
- **agent/:** 93 changed files.
- **apps/:** 849 changed files.
- **contributors/:** 2 changed files.
- **gateway/:** 23 changed files.
- **locales/:** 99 changed files.
- **model_tools.py/:** 4 changed files.
- **nastech_cli/:** 102 changed files.
- **nastech_platform/:** 6 changed files.
- **nastech_state.py/:** 4 changed files.
- **nastech_state_tool_retries.py/:** 3 changed files.
- **optional-skills/:** 129 changed files.
- **plugin-catalog/:** 3 changed files.
- **plugins/:** 6 changed files.
- **pm/:** 31 changed files.
- **run_agent.py/:** 4 changed files.
- **scripts/:** 16 changed files.
- **skills/:** 2 changed files.
- **tests/:** 88 changed files.
- **tools/:** 44 changed files.
- **toolsets.py/:** 7 changed files.
- **tui_gateway/:** 124 changed files.
- **ui-tui/:** 20 changed files.
- **website/:** 114 changed files.

## Delivered improvements

### New capabilities

- feat(release): add a changelog subcommand and point oversized drafts at it
- feat(desktop): the dimmed composer comes back after 5s without scrolling
- feat(desktop): show the free-tier sign-in offer when the backend says it is due
- feat(free-tier): offer sign-in after finished tasks, backing off
- feat(desktop): Terms and Privacy butterbar for free-tier users
- feat: the setup handoff carries what setup learned, and the task chat talks first (#129419)
- feat(setup): the setup chat can connect an app the user asks for now (#129203)
- feat(start_chat): a handoff from the setup profile marks onboarding complete
- feat(desktop): setup_choose question cards and the start_chat handoff card
- feat(onboarding): /initiate-setup built-in on every surface; the first message offers it
- feat(skills): initiate-setup reads a pre-read user scan at skill load
- feat(setup): the setup profile runs inline shell at skill load
- 6 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(release): read the Nastech version line in the Nix check and accept rc.N attempt refs
- fix(desktop): never idle-reap a local profile backend (#134942)
- fix(update): a whole-second marker creation time in our own second is still us
- fix(release): the stable MSIX smoke accepts the release-time package quad
- fix(termux): upgrade libc++ in the wheelhouse builder so cmake starts
- fix(release): build the default flake package for the Nix identity check
- fix(tui_gateway): a bare mid-turn model pick gets its confirm before it is queued
- fix(desktop): tag every line of a multi-line waiter script error
- fix(desktop): make the relaunch waiter's script log per-attempt, UTF-8 and bounded
- fix(desktop): log why the MSIX relaunch waiter failed to start
- fix(release): abandon clears every outstanding attempt of the version
- fix(release): read attempt claims from the remote, not local tags
- 99 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(state): pre-filter the per-turn tool-retry scan with LIKE

### Documentation

- docs(plugins): list the built-in author tools at the top of the plugin guide
- docs(security): /yolo survives a TUI/Desktop resume too
- docs(desktop): say which app checks setup runs
- docs: regenerate the initiate-setup skill page
- docs: escape <machine> so the docs site builds
- docs(first-task): reach a first result faster with hard limits and per-ask first moves (#130247)
- docs(catalog): target_scope no longer names the setup profile
- docs(delegation): list start_chat among the tools subagents cannot call

### Improvements

- refactor(approval): one session /yolo contract for CLI, TUI/Desktop and the messaging gateway
- test(install-e2e): the windows source update check reads staged main, not GitHub main
- Update .github/workflows/nix.yml
- ci(release): also build the desktop package from the stamped source
- Merge pull request #134916 from Nastechresearch/fix/relaunch-waiter-log-review
- Merge pull request #134884 from Nastechresearch/fix/release-abandon-all-of-version
- Merge pull request #134911 from Nastechresearch/fix/relaunch-waiter-diagnostics
- Merge pull request #134905 from Nastechresearch/fix/release-seed-0215
- refactor(tui-gateway): restore session /yolo once in session.resume, test in its own file
- chore(contributors): map jonh-dev's commit email
- test(tui_gateway): pin the large-context boundary and the no-agent pick
- revert: dashboard-auth token exchange breaks on gzip IdP responses (partial revert of #133938)
- 78 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
