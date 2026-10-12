# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 140 commits affecting 2907 files.
- **Source revision:** `835c3dd038d9`.
- **Previous source revision:** `cca83848ec79`.

## Technical coverage

- **.github/:** 27 changed files.
- **.gitignore/:** 1 changed files.
- **agent/:** 3 changed files.
- **apps/:** 164 changed files.
- **contributors/:** 2 changed files.
- **gateway/:** 18 changed files.
- **lefthook.yml/:** 1 changed files.
- **locales/:** 104 changed files.
- **nastech_cli/:** 17 changed files.
- **optional-skills/:** 67 changed files.
- **plugin-catalog/:** 8 changed files.
- **scripts/:** 48 changed files.
- **tests/:** 168 changed files.
- **tests-js/:** 2 changed files.
- **tools/:** 51 changed files.
- **tui_gateway/:** 19 changed files.
- **ui-tui/:** 39 changed files.
- **website/:** 34 changed files.

## Delivered improvements

### New capabilities

- feat(check): run the blob-size guard in scripts/check
- feat(ci): reject PRs that add binaries or new files over 500 KiB
- feat(ci): report files a CI job leaves in the checkout
- feat(release): offer to abandon a blocking attempt from an interactive terminal
- feat(ci): new config keys and slash commands must ship with docs
- feat(desktop): list, name and rename several accounts per connector
- feat(tui,cli): reconnect repairs the chosen account by id, retired accounts fold
- feat(tui): /connectors manages named connector accounts
- feat(cli): nastech connectors lists, connects, renames and removes accounts
- feat(connectors): account rows say when an account is retired, and a repair can name one by id
- feat(cli): the connection card says which name Nastech gave an account
- feat(connectors): gateway contracts for named connector accounts
- 7 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(release): a Store submission failure never blocks publishing
- fix(release): the Store submit reads the CLI's PascalCase submission keys
- fix(check): blob-size exempts untracked copies and reads --head's allowlist (review)
- fix(desktop): the Persistent Shell description says what the toggle does
- fix(terminal): make persistent_shell / TERMINAL_*_PERSISTENT actually work
- fix(release): the Store submit reads the submission with 'get', not 'status'
- fix(tests): keep MagicMock home paths out of the repo checkout
- fix(release): abandon only the approved attempt, and only after the new cut is viable
- fix(install-e2e): chat smoke waits for the app to show the mock model before sending
- fix(gateway): offer an admitted completion again when its turn cannot confirm the owner
- fix(gateway): keep the pre-flight's proof through a completion's turn
- fix(gateway): read a raw api_server completion's notice policy in its served profile
- 51 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(terminal): profile functions and aliases last one command with persistence on
- docs: multiple named connector accounts
- docs(ci): prompt-surface changes need one core approval, not two
- docs: Accent Picker links point at nastech-official-plugins (#136446)

### Improvements

- test(release): a failed Store job leaves the publish phase green; stable-publish still gates it
- fmt(js): `npm run fix` on merge (#136847)
- test(terminal): the local default reaches the environment too; config comment matches the docs
- ci(clean-worktree): run only when every earlier step passed
- Merge pull request #136756 from Nastechresearch/fix/desktop-smoke-wait-for-mock-model
- ci(remote-backends): debian 13 for the test sshd, container setup as a mounted script
- ci(remote-backends): fail on skips from the runner's parsed counts (review)
- ci: run the SSH and Docker terminal backends against a real sshd and daemon
- ci(release): refuse Intel-less retirement targets and define opt-in platforms once
- test(release): an SSH-signed pre-flag claim reads the opt-in platform keys as false
- ci(release): stop building macOS Intel and Termux in stable releases by default
- Code health blocks new wall-clock sleeps in tests (HX013), adds a shared wait_until helper (#136644)
- 42 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
