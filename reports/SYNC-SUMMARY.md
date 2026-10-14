# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 301 commits affecting 2944 files.
- **Source revision:** `6e84ce66fb57`.
- **Previous source revision:** `6e7b83a2f1c0`.

## Technical coverage

- **.github/:** 55 changed files.
- **.npmrc/:** 1 changed files.
- **Dockerfile/:** 1 changed files.
- **agent/:** 102 changed files.
- **apps/:** 735 changed files.
- **contributors/:** 106 changed files.
- **evals/:** 2 changed files.
- **gateway/:** 7 changed files.
- **locales/:** 43 changed files.
- **model_tools.py/:** 1 changed files.
- **nastech_cli/:** 116 changed files.
- **nastech_constants.py/:** 1 changed files.
- **nastech_platform/:** 14 changed files.
- **nastech_state.py/:** 1 changed files.
- **nastech_state_compression.py/:** 2 changed files.
- **nastech_state_sessions.py/:** 3 changed files.
- **nastech_state_tool_retries.py/:** 1 changed files.
- **optional-skills/:** 5 changed files.
- **package-lock.json/:** 2 changed files.
- **package.json/:** 1 changed files.
- **plugins/:** 1 changed files.
- **pm/:** 10 changed files.
- **pyproject.toml/:** 1 changed files.
- **run_agent.py/:** 5 changed files.
- **scripts/:** 13 changed files.
- **tests/:** 272 changed files.
- **tests-js/:** 4 changed files.
- **tools/:** 41 changed files.
- **toolsets.py/:** 5 changed files.
- **tui_gateway/:** 96 changed files.
- **ui-tui/:** 1 changed files.
- **uv.lock/:** 1 changed files.
- **web/:** 1 changed files.
- **website/:** 22 changed files.

## Delivered improvements

### New capabilities

- feat(release): dispatch Stable Release from the default branch
- feat(metrics): count connector file-input refusals by error class
- feat(connectors): connector tools send and save local files
- feat(gateway): connector downloads are a trusted media delivery root
- feat(connectors): client calls to stage file inputs and fetch file outputs
- feat(gemini): Gemini 4 Argon support with long decode
- feat(onboarding): the first desktop boot records that onboarding is due and the trial reserved
- feat(free-tier): the free model is a desktop first-install trial, claimed once per machine
- feat(onboarding): one machine-level answer to "has Nastech been used here"
- feat: release the agentic setup profiles once, at serve boot
- feat(desktop): picking Elite opens its terminal and file tree
- feat(desktop): the first-run intro types in the app's language
- 40 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(install-e2e): the Windows packaged-app feed serves byte ranges
- fix(pm): re-merge the uv cache seed on volumes marked by a seedless image
- fix(release): publish replaces the stable head instead of create-only
- fix(release): keep a stable run on main from using the controller commit or cancelling pushes
- fix(pm): stage a version for version-less buildable plugin members too
- fix(pm): don't stamp project.version on members declaring it dynamic
- fix(pm): give generated virtual workspace members a project.version
- fix(pm): retry sync without bytecode compile when that step fails
- fix(deps): bump httpx2/httpcore2 2.7.0 -> 2.12.0 for the audit advisories
- fix(doctor): stop mislabeling the root npm audit row as agent-browser
- fix(doctor): say recreating the same Docker image does not fix npm findings
- fix(doctor): describe full workspace npm audit scope
- 152 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(onboarding): the due answer is worked out at serve boot and served from a cache
- perf(onboarding): one provider walk per due answer, one AWS chain walk, no IMDS on the desktop backend

### Documentation

- docs: Local Models is on by default on macOS, Windows and Linux
- docs(free-tier): the trial is once per OS user, not once per machine
- docs(desktop): drop the start_chat clause from the onboarding chat comment
- docs: remove the initiate-setup and first-task skills and the setup docs
- docs(onboarding): document onboarding.run; salvaged reads say first-run onboarding
- docs(platform): record the N1X markers measured on hardware

### Improvements

- test(relay): the OpenAI-stream e2e no longer self-deadlocks when the stream is buffered
- Merge pull request #138028 , fixes for bundles
- Merge pull request #138159 from Nastechresearch/ci/stable-release-dispatch-from-main
- Merge pull request #138163 from Nastechresearch/fix/docker-seed-uv-cache
- Merge pull request #138179 from Nastechresearch/fix/stable-head-cas
- chore(contributors): map ieqzya@gmail.com to Ieqzya
- test(pm): one streamed-sync test covers the bytecode-compile retry
- chore(contributors): map Darthvader88@gmail.com to guthixboss1
- test(deps): fail the build if an httpx2 pin or lock entry drops below 2.12.0
- test(doctor): point the root-row label test at the staged-npm seam
- ci(release): pass the commit under test through every stable lane
- Merge pull request #138107 from Nastechresearch/fix/docker-release-version-tag
- 65 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
