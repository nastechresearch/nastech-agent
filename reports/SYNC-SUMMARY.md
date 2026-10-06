# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 890 commits affecting 2807 files.
- **Source revision:** `e97923c38acb`.
- **Previous source revision:** `af8839df1038`.

## Technical coverage

- **.coderabbit.yaml/:** 1 changed files.
- **.github/:** 11 changed files.
- **.gitignore/:** 1 changed files.
- **AGENTS.md/:** 7 changed files.
- **CONTRIBUTING.md/:** 8 changed files.
- **agent/:** 137 changed files.
- **apps/:** 476 changed files.
- **cli-config.yaml.example/:** 3 changed files.
- **cli.py/:** 3 changed files.
- **contributors/:** 37 changed files.
- **cron/:** 4 changed files.
- **gateway/:** 47 changed files.
- **locales/:** 11 changed files.
- **nastech_cli/:** 406 changed files.
- **nastech_platform/:** 3 changed files.
- **plugin-catalog/:** 191 changed files.
- **plugins/:** 62 changed files.
- **pm/:** 14 changed files.
- **providers/:** 6 changed files.
- **scripts/:** 115 changed files.
- **skills/:** 1 changed files.
- **tests/:** 669 changed files.
- **tests-js/:** 12 changed files.
- **tools/:** 77 changed files.
- **tui_gateway/:** 45 changed files.
- **ui-tui/:** 1 changed files.
- **utils.py/:** 1 changed files.
- **web/:** 39 changed files.
- **website/:** 78 changed files.

## Delivered improvements

### New capabilities

- feat(tts): let PCM-streaming plugin TTS providers join the streaming path
- feat(catalog): add limbic entry
- feat(plugin-catalog): add nastech-tenuo
- feat(plugin-catalog): add session-lens
- feat(catalog): add nastech-gemini-live
- feat(plugin-catalog): add banner image for openclawcash-agentwallet
- feat(plugin-catalog): add openclawcash-agentwallet
- feat(telemetry): ask once more where a "No thanks" may never have been seen
- feat(plugin-catalog): add cursor-provider v0.3.5
- feat(plugin-catalog): bump pushover-nastech-plugin to 1.2.0
- feat(plugin-catalog): show a card image for stt-vocab
- feat(plugin-catalog): add stt-vocab
- 65 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix: an unopenable checkout lock reads held to every Python reader, as the scripts and Desktop read it
- fix: the F2 replacement-claim regressions run under a psutil-less live-system guard
- fix: the update's Windows child runner and the probe runner share one kill-and-drain
- fix: every Python identity reader judges our own pid by one incarnation rule
- fix: a Ctrl-C'd build runner can no longer kill the custodian of its detached writers
- fix: Desktop SSH marker readers judge the v2 marker with update_lock's one parser and identity rule
- fix: a historical takeover reaches its child on a cp1252 Windows pipe
- fix: a group kill of the build's caller no longer kills the custodian of its detached writers
- fix: a background git hook never keeps a completed update's checkout locked
- fix: Desktop SSH readers clear a dead v2 update claim instead of stranding it
- fix: a reader reports the live claim that replaced its stale marker snapshot
- fix(update): the watched fetch's timeout drains its pipes for a bounded time
- 421 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(providers): memoize the bare-name custom check on the config signature
- perf(compaction): cap the typed-boundary bisect at budget*4 chars

### Documentation

- docs(update): nastech_cli/AGENTS.md keeps the post-commit rule within the size cap
- docs(update): nastech_cli/AGENTS.md states the post-commit exit rule and points at its table
- docs(update): post-commit contract in the compacted update-pipeline docs
- docs(update): maintenance docstring says profile sync is best-effort per profile (review F1-profile-sync, declined)
- docs(update): profile sync is owed only when the step escapes; one post-commit Windows resume (m6, M4)
- docs(update): receipt-store and gateway-marker rules after the commit point
- docs(update): dependency follow-up, Ctrl-C after commit, root-home readers, fleet exit 0
- docs(models): the answer_in_reasoning opt-in is re-read on the active route
- docs(models): document the answer_in_reasoning custom-provider opt-in
- docs(user-stories): add 45 business and professional stories (#133708)
- docs(ssl): note SSL_CERT_FILE sits on top of the platform store
- docs(discord): state what the slash role flag means
- 15 additional documentation updates are included in this verified snapshot.

### Improvements

- test(update): the L3 lease test's fake --prepared child writes its result
- refactor(cli): container exec routing moves out of main.py into main_container.py
- test: browser tree-kill unit tests no longer SIGKILL real processes under PID 999
- test: v2-marker delegate fixtures record the delegate's real creation time
- test: R2's custody test stalls git with a clean filter, not a hook the updater no longer runs
- test(update): the F54 control job sets its breakaway flag through the extended limits
- test(update): fake win32 for update_custody only, not the whole process
- test(update): the borrowed-home tail fixture patches the custody spawn
- chore(update): waive the deliberate catch-alls and unbounded update children for the health ratchet
- test(update): new lock tests write/read bytes (Windows footgun gate)
- test(update): gc custody is asserted through run_git; drop the dead spawn_kwargs (review N-coverage)
- refactor(update): drop the gc-fold custody exception (#132927 removed the fold)
- 339 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
