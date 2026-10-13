# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 498 commits affecting 2932 files.
- **Source revision:** `6e7b83a2f1c0`.
- **Previous source revision:** `835c3dd038d9`.

## Technical coverage

- **.github/:** 5 changed files.
- **agent/:** 40 changed files.
- **apps/:** 219 changed files.
- **contributors/:** 38 changed files.
- **evals/:** 4 changed files.
- **gateway/:** 1 changed files.
- **locales/:** 22 changed files.
- **model_tools.py/:** 4 changed files.
- **nastech_cli/:** 94 changed files.
- **plugin-catalog/:** 255 changed files.
- **plugins/:** 79 changed files.
- **pm/:** 8 changed files.
- **pyproject.toml/:** 2 changed files.
- **scripts/:** 25 changed files.
- **tests/:** 206 changed files.
- **tools/:** 104 changed files.
- **toolsets.py/:** 1 changed files.
- **tui_gateway/:** 23 changed files.
- **uv.lock/:** 2 changed files.
- **web/:** 4 changed files.
- **website/:** 38 changed files.

## Delivered improvements

### New capabilities

- feat(plugin-catalog): add auto-pin plugin
- feat(catalog): add wicked-memory tools plugin
- feat(catalog): add TTS Buddy native speech provider
- feat(plugin-catalog): bump approval-ledger to 1.2.0
- feat(plugin-catalog): bump error-ledger to 1.3.0
- feat(plugin-catalog): add channel3 shopping plugin
- feat(plugin-catalog): pin heartbeat2 to v0.1.1 (catalog review conditions)
- feat(plugin-catalog): add heartbeat2 plugin
- feat(plugin-catalog): re-pin Index 0.48.5 to 1214c61
- feat(plugin-catalog): pin Index to 0.48.5 (7f4c3ed)
- feat(plugin-catalog): pin Index to 0.48.4 (87e714d)
- feat(plugin-catalog): add nastech-mobile platform adapter entry
- 56 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(desktop): a catalog link that launches Desktop opens the install dialog
- fix(desktop): the catalog lookup falls back only for a backend without the method
- fix(desktop): a malformed catalog lookup reply reads as unavailable; the gateway validates names with the CLI's own rule
- fix(desktop): catalog deep links ask the backend for the entry
- fix(update): --version, the dashboard and a remote backend name a stable rollback too (#137714)
- fix(desktop): the rollback dialog names its button and claims no changes (#137714)
- fix(desktop): a stable release older than the checkout is offered as a rollback (#137714)
- fix(desktop): preserve stable update channel context
- fix(update): a stable release older than the checkout reads as a rollback (#137714)
- fix(install): a rerun keeps an install on the update channel it chose (#137714)
- fix(plugin-catalog): only plain UTF-8 data may ship compressed
- fix(plugin-catalog): rule 17 gate reads a single gzipped file instead of failing it
- 138 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(prompt): fixed prefix back under the post-diet size (-2.1k tokens per request)

### Documentation

- docs(plugin-catalog): inline disclosure line in the nastech-mobile description
- docs(tools): the refresh docstring and publish guard say when schema bytes count
- docs(plugins): catalog rule 9 notes validate warns on private core imports
- docs(plugins): place lifecycle Routing after the example; list the routed delegation keys
- docs(shared-metrics): connector naming, error classes and the three new rows
- docs(pm): 3-day release age checked at lock time; plugins trust core's lock
- docs(auth): spell out the unknown sk-ant-* default in _is_oauth_token
- docs: pin released provider with API-key onboarding
- docs: use AceDataCloudModelProviderNastech repository name

### Improvements

- fmt(js): `npm run fix` on merge (#137796)
- catalog: add agent-ledger v0.4.4 (e9eba11)
- chore(catalog): reviewed disclosure for holographic
- plugin-catalog: bump holographic to 0.13.0
- plugin-catalog: bump holographic to 0.12.0
- plugin-catalog: bump holographic to 0.11.0
- plugin-catalog: bump holographic to 0.10.0
- plugin-catalog: bump holographic to 0.9.0
- plugin-catalog: bump holographic to 0.8.0
- plugin-catalog: bump holographic to 0.7.0
- plugin-catalog: bump holographic to 0.6.2
- refactor: keep the rollback wiring inside the code-health caps (#137714)
- 258 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
