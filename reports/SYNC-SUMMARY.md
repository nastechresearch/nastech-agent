# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 429 commits affecting 1435 files.
- **Source revision:** `5a8e8a6b8748`.
- **Previous source revision:** `a9c783f21995`.

## Technical coverage

- **.dockerignore/:** 2 changed files.
- **.env.example/:** 1 changed files.
- **.github/:** 8 changed files.
- **.gitignore/:** 2 changed files.
- **agent/:** 77 changed files.
- **apps/:** 296 changed files.
- **cli-config.yaml.example/:** 5 changed files.
- **cli.py/:** 5 changed files.
- **contributors/:** 82 changed files.
- **cron/:** 16 changed files.
- **docs/:** 3 changed files.
- **evals/:** 1 changed files.
- **gateway/:** 72 changed files.
- **locales/:** 17 changed files.
- **nastech_cli/:** 137 changed files.
- **nastech_constants.py/:** 2 changed files.
- **nastech_logging.py/:** 1 changed files.
- **nastech_startup_watchdog.py/:** 2 changed files.
- **nastech_state.py/:** 30 changed files.
- **nastech_state_common.py/:** 3 changed files.
- **nastech_state_schema.py/:** 5 changed files.
- **nastech_state_search.py/:** 2 changed files.
- **nastech_time.py/:** 2 changed files.
- **plugins/:** 73 changed files.
- **pyproject.toml/:** 4 changed files.
- **run_agent.py/:** 12 changed files.
- **scratch/:** 2 changed files.
- **scripts/:** 21 changed files.
- **skills/:** 1 changed files.
- **tests/:** 442 changed files.
- **tools/:** 43 changed files.
- **toolsets.py/:** 1 changed files.
- **trajectory_compressor.py/:** 1 changed files.
- **tui_gateway/:** 35 changed files.
- **ui-tui/:** 13 changed files.
- **utils.py/:** 2 changed files.
- **uv.lock/:** 2 changed files.
- **web/:** 3 changed files.
- **website/:** 43 changed files.

## Delivered improvements

### New capabilities

- feat(desktop): built-in optional-skills catalog in Capabilities → Skills with one-click install
- feat(desktop): first-open consent prompt for real-profile browsing
- feat(desktop): add comment mode to the in-app browser
- feat(tools): withdraw tip and tour when the user switches them off
- feat(desktop): collapse Yesterday / Last week groups in the sessions sidebar
- feat(agent): escalate repeated transcript-sanitiser heals with a one-time user notice (#96870)
- feat(cron): doctor flags overdue next_run_at as silent non-firing
- feat: add cron doctor health check
- feat(browser): honor browser.engine=lightpanda in Browser Use mode
- feat(buzz): compose thread-topology cluster — reply_in_thread opt-out, NIP-10 root anchoring on all send paths, _PLATFORM_DEFAULTS tier
- feat(buzz): implement edit_message and delete_message so replies can stream
- feat(worktree): pushed open-PR lanes reclaim their disk; cron tick prunes worktrees
- 2 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(terminal): strict Linux-only gating for background-executor systemd scopes (#70716 follow-up)
- fix(desktop): pass --disable-setuid-sandbox on the userns launch path
- fix(cli): use Chromium's namespace sandbox when userns is available on Linux
- fix(gemini): strip call ids on insert, name the realignments in the log
- fix(gemini): echo bridged tool_call name on the OpenAI-compatible path
- fix(cache,tests): durable generation docstring + studio-bridge order (PR #98811, refs #96811)
- fix(cache): repair settlement, and make the generation unprunable
- fix(cache): source-qualify the peer identity and gate the declared bind
- fix(cache): make the conversation generation survive a backwards clock
- fix(api): resolve the declared conversation instead of minting a session per request
- fix(cache): qualify the declared key with the conversation generation
- fix: initialize affinity_token before the turn-lease early returns
- 296 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(openviking): clarify remember extraction semantics
- docs(desktop): document the in-app browser comment mode
- docs(agent): explain intentional preflight vs in-loop message divergence
- docs(browser): document Lightpanda in Browser Use mode and the engine precedence rules
- docs(buzz): clarify reaction-only user precedence
- docs(cron): explain why the secret-scope reset must stay function-level

### Improvements

- chore: map contributor emails
- chore: map yongliabc888@gmail.com to yongli-abc for PR #87629 salvage
- test(cache): fix stale Studio construction-order paragraph in the bridge witness docstring
- test(cache): pin the affinity contract on Studio's real bridge construction
- chore(cache): take the pre-merge cleanups on the declared conversation scope
- test(api): cover the declared-conversation precedence through the real handlers
- refactor(compression): extract preflight seed predicate onto ContextCompressor
- chore: add contributor mapping for vjpixel (PR #93439 salvage)
- fmt(js): `npm run fix` on merge (#100128)
- fmt(js): `npm run fix` on merge (#100096)
- test(desktop): isolate the consent dialog in preview-pane tests
- fmt(js): `npm run fix` on merge (#99917)
- 89 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
