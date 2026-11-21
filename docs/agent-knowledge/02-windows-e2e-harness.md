# Windows install/update E2E harness — Durable Knowledge

Scope: permanent operating knowledge for `nastech-agent` contributors and agents
triaging the Windows install/update E2E lane. This captures two hard-won failure
classes (installer churn on the GUI update route, and OS-specific file timeouts on
`crash_cells` / `pause_durable`) plus the two update routes the harness drives.
Source of truth is the checkout itself — re-read the cited files before acting;
this note records WHY the code looks the way it does, not a substitute for it.

> **Skill-first gate (mandatory).** Before diagnosing a Windows E2E failure, scan and
> load `systematic-debugging` and `100wayskills` (`skill` tool). The `100wayskills`
> safety contract binds the work: evidence first, no weakening a test/gate to get green,
> no retry merely to obtain green CI, no merge/tag/release/deploy. See
> `07-100ways-ci-triage.md` for the CI/release triage contract this note builds on.

## 1. Where the lane lives

| Thing | Path |
|---|---|
| Driver script | `tests/install/windows-e2e.ps1` |
| Workflow | `.github/workflows/windows-install-update-e2e.yml` |
| Launch-capture / Playwright driver | `tests/install/e2e-assets/launch-from-spec.mjs` |
| Source-update observer | `tests/install/e2e-assets/source-update-observer.mjs` |
| OS-specific E2E | `tests/e2e/core/windows_update/` (`test_crash_cells.py`, `test_pause_durable.py`, ...) |
| Companion note (PM takeover hang) | `01-pm-takeover-hang.md` |

The workflow runs `scripts/run_tests.sh tests/e2e/core/windows_update/ -- -m "platforms and
integration" -v --tb=short -rA` on a **free 4-core `windows-latest`** runner with
`NASTECH_TEST_WORKERS: '4'`, `NASTECH_TEST_FILE_TIMEOUT: '5400'`,
`NASTECH_TEST_FILE_RETRIES: '0'`, and a job `timeout-minutes: 120`. It fakes user profiles
under `C:\Users` (real-install layout, avoids checkout's 159-char-path MAX_PATH issues) and
keeps machine work dirs under `runner.temp`.

## 2. Failure A — open-app-update churn (rc.7)

### Symptom / evidence

- rc.7 **attempt 1, job `136761049283`** and **attempt 3, job `136825552752`**: the
  `installer-script+desktop -> open-app-update` leg never completed. The post-update
  read-only assertion failed with the message:
  `post-update -- read-only install verification (no repair)`
  (`windows-e2e.ps1` `Assert-True ($LASTEXITCODE -eq 0)` at the `Test-NastechRuns
  "post-update"` step, ~line 516).

### Root cause (verified in the driver comments)

The GUI driver refuses a dirty source tree, so the production updater autostashes before
it pulls. A historical installer leaves installer-generated state in the disposable clone:

- `npm install` on Windows rewrites `package-lock.json` as CRLF (later installers use `npm
  ci`); `diff --ignore-cr-at-eol` shows the path "modified" with identical index/HEAD blobs.
- v2026.6.19-era installers write an unignored `.install_method`.
- Installers through v2026.9.24 clone under Git-for-Windows `core.autocrlf=true` and pin
  `false` only afterwards, leaving CRLF copies of every text file not pinned to LF by
  `.gitattributes` (`*.mdx`, `LICENSE`, ...). The stat cache hides most, except the few
  written in the index's racy-timestamp window.
- Pre-launcher-layout installers copied `bin/nastech.exe` and `bin/nastech-acp.exe` into
  the checkout (untracked, unignored on the OLD install only).

On a large diff the updater's autostash **restore conflicts**, so the update never finishes
and the read-only post-update verifier rejects the conflicted tree. This is not a product
bug — it is stale installer state feeding the updater.

### Fix (already in the tree)

`Clear-HistoricalInstallerChurn` is called at the **start of `Invoke-GuiUpdateDesktopRoute`**
(`windows-e2e.ps1` ~line 1270; also in `Invoke-NastechDesktopAppUpdate` ~line 832). Its
safe contract (function ~line 719):

- Enumerate dirty paths with `git status --porcelain=v2 --untracked-files=all`
  (porcelain v2 because `Invoke-Git` trims v1's leading `" M"`).
- Treat as churn ONLY: `package-lock.json` rewrites whose content differs from the index
  solely by CRs (`git diff --numstat --ignore-cr-at-eol`, which honours the flag where
  `--name-only` does not), `.install_method`, and the two legacy launcher paths — the
  latter only when the OLD checkout predates the launcher-layout commit
  `dbee5b4665ba4012b8bb3c89423327d66e182e0d` (this fork's rebrand commit; the upstream
  SHA would be a no-such-object here and `merge-base --is-ancestor` would exit 128, which
  is asserted against, never silently treated as "not an ancestor").
- Revert tracked churn via a NUL-separated `--pathspec-from-file` (from a file because a
  v2026.7.1 clone churns hundreds of paths that would overflow the Windows command line),
  and add `.install_method` / legacy launcher paths to `.git/info/exclude`.
- **Hard-fail on any other local change:**
  `Assert-True ($other.Count -eq 0) "installed source has only installer-generated changes
  (other: ...)"` and a final clean-tree assertion. Genuine local modifications are never
  silently swept away.

Do NOT weaken `post-update -- read-only install verification (no repair)` to hide a skipped
rebuild; fix the upstream state, not the verifier.

## 3. Failure B — crash_cells / pause_durable timeouts

### Symptom / evidence

- **attempt 1, job `136756350045`** (also recorded in the workflow comment as run
  `44873305395` attempt 1): `test_crash_cells.py` hit
  `NASTECH_TEST_FILE_TIMEOUT=3600s` and was SIGKILLed at **3603 s**. Because the whole
  journey (install → gateway phase → six crash cells) runs inside one module-scoped
  fixture, the kill skipped teardown and leaked a gateway process, the fake profile, and
  `serve.git` — leaving leftover PowerShell/teardown state.
- `pause_durable` additionally observed its PM worker raising `TimeoutExpired` after a
  **5 s post-result wait** (see `01-pm-takeover-hang.md`).

### Fixes (already in the tree)

- Workflow `NASTECH_TEST_FILE_TIMEOUT` bumped `3600` → **`5400`** in
  `.github/workflows/windows-install-update-e2e.yml` (~line 102), with
  `NASTECH_TEST_FILE_RETRIES: '0'` (a file killed by signal or file timeout is never
  retried — relaunching a runaway doubles the damage). A "Every crash cell ran" step
  (`crash-cells-ran.txt` manifest) prevents a lost marker/opt-in from passing green with
  zero cells.
- PM client wait hardened — cross-reference `01-pm-takeover-hang.md`.
- Root-cause framing: on the 4-core free runner under 4-way load `test_crash_cells.py`
  exceeds 3600 s (~2,100 s on a normal runner); the job allows 120 min, so give the file
  room to finish instead of killing it mid-journey. Do not "fix" this by retrying or by
  raising a test's tolerance to hide a hang.

## 4. The two update routes (Mode A vs Mode B)

Both start from a clean checkout and drive the same production updater; they differ in how
they trigger it and how they detect completion.

| | `nastech-desktop-app-update` (Mode A) | `open-app-update` (Mode B) |
|---|---|---|
| Driver function | `Invoke-NastechDesktopAppUpdate` (`windows-e2e.ps1` ~line 795) | `Invoke-GuiUpdateDesktopRoute` (~line 1254) |
| Trigger | `nastech desktop` under launch capture (`launch-capture/sitecustomize.py` + optional `pm-launch.py` for the PM `-I` launcher), then `launch-from-spec.mjs` re-executes the captured spawn under Playwright and clicks **Update now** | Installed `Nastech.exe` launched directly; `drive-update.cjs` clicks Settings → About → **Update now**; exit 0 = app quit for hand-off |
| Cleanup | `Clear-HistoricalInstallerChurn` (~line 832) | `Clear-HistoricalInstallerChurn` at route start (~line 1270) |
| Completion wait | `launch-from-spec.mjs` polling for a **successful source-update receipt** + expected checkout + marker removal; `--timeout-ms 2100000` = **35 min** (was 30 min — large diffs + full Electron rebuild pushed PM sync past the old 30 min ceiling, per ~lines 841–848) | Detached-updater wait up to **35 min** (~line 1335), tailing `logs/update.log`. COMPLETION = result JSON **OR** (checkout reached target SHA AND marker gone). Result JSON asserted only on the script path; staged-binary path relies on sha/marker/relaunch asserts (~lines 1320–1360) |
| Post steps | close the verified relaunched window; checkpoint | marker-grace handling (2 min + 10 min under active checkout lock), relaunch wait, `Test-NastechRuns "post-update"` |

`0`/`42` driver exit codes: `0` = update completed; `42` = manual-update card path
(`Invoke-ManualCardUpdate` on `manual-update.json`). A launch-capture exit 0 **without** a
captured launch is a failure (`Assert-True (Test-Path "$spec.captured")`), never a pass.

`launch-from-spec.mjs` details: `SELF_DEADLINE_MS = --timeout-ms + 20 * 60 * 1000`
(the extra 20 min is for launch/OLD-chat after the update wait, not the wait itself);
default `--timeout-ms` is `900000`, but the driver overrides it to `2100000`. On timeout it
 throws `no successful update completion receipt; leaving the install untouched`.

## 5. Evidence commands

Fetch a job's **full** log via the bare API path (`gh run view --log` can return empty for
some slices):

```bash
# Job logs (bare API path returns the complete log)
gh api "repos/nastechresearch/nastech-agent/actions/jobs/<job-id>/logs"

# Enumerate jobs for an attempt, paged
gh api "repos/nastechresearch/nastech-agent/actions/runs/<run>/attempts/<n>/jobs?per_page=100&page=<p>"

# Human-readable overview
gh run view <run> -R nastechresearch/nastech-agent
```

Download run artifacts (transcripts, `nastech-agent-update`, proof trees) and inspect them
locally:

```bash
gh run download <run> -R nastechresearch/nastech-agent -D /tmp/opencode/win-e2e-artifacts  # no-tmp: ok — example artifact download target
```

Mine logs/artifacts for the decisive lines (run from the artifact dir):

```bash
grep -rniE 'ASSERTION FAILED|read-only install verification|update result|receipt|handoff|SIGKILL|TimeoutExpired|timeout' .
```

For churn failures look for the `source status before GUI update:` block and the
`installed source has only installer-generated changes (other: ...)` assertion. For
detached-updater failures look for `waiting for the detached updater to finish`, the
`updater result:` line, and the `update marker still present after 2 min grace` block.
For timeout failures look for the SIGKILL timestamp vs `NASTECH_TEST_FILE_TIMEOUT` and any
leftover process/PowerShell teardown. A 502 from the jobs API is transient — retry; do not
read it as a product failure.

## 6. No attribution hints — absolute rule

Never introduce source/fork attribution, provenance, or "branded from" wording — in code,
comments, docstrings, commit messages, PR titles/bodies, release notes, generated reports,
summaries, or skill/knowledge files. The `windows-e2e.ps1` comments about historical
installer versions and the launcher-layout commit are **version/behavior facts**, not brand
attribution, and are fine. Do not add upstream-brand narrative. A single hint is a brand
audit violation.

## 7. Status template for this lane

```text
Lane: windows-install-update-e2e (run <id>, attempt <n>, job <id>)
Route: open-app-update | nastech-desktop-app-update | crash_cells | pause_durable
Classification: installer churn | file timeout/teardown leak | product regression | flaky
Decisive log line: <exact assertion / receipt / SIGKILL / TimeoutExpired>
Fix: <file:line + function>, clean-tree / timeout / wait contract preserved
Validation: local targeted test → workflow rerun on exact head → crash-cells manifest present
Safety boundary: no weakened gate, no retry-to-green, no merge/tag/release/deploy
```
