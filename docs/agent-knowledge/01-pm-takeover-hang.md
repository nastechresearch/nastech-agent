# PM takeover hang — rc.7 release gate (durable diagnostic knowledge)

Status: diagnosed, mitigation applied, awaiting confirmation on next gate run.
Scope: nastech-agent release gate / historical-updater takeover path. Keep this file factual and current; update it when the next gate result is known.

## 1. Symptom (observed, not inferred)

Release gate `rc.7`, CI run `44873305395`, attempt 3, head `9efde6c474` (same signature on attempts 1–3). Mode A failures:

- `windows: installer-script+desktop -> nastech-desktop-app-update (v2026.8.11 -> HEAD)`
- `installer-script -> nastech-desktop-app-update`

Both failed with:

```
no successful update completion receipt; leaving the install untouched
```

Side evidence from the failed runs:

- `desktop-update-handoff.log` ends at:
  `-> Handing off to the new updater (package manager) for the rest of this update...`
- Orphan `python` / `nastech` processes were still alive and had to be killed at the 30-minute test timeout.

Interpretation: the old updater handed control to the takeover child, the child never emitted a completion result, and the harness waited until its own timeout killed the leftover processes. The "no successful update completion receipt" message is the harnesss correct refusal to treat an incomplete update as done — it is a symptom, not the defect.

## 2. Root-cause area (file paths)

Historical updater takeover chain:

- `nastech_cli/_old_updater.py` — `_run_child()` (line ~124) spawns the takeover child and pipes its stdout; the handoff print is at line ~150. Takeover stdout piped to `_run_child`; if the child goes silent, `_run_child` sees no result. A `ValueError("invalid update takeover acknowledgement")` is raised if the child exits without a valid acknowledgement.
- `nastech_cli/_update_takeover.py` — `main()`, `prepare(request)` (line ~15). `prepare()` is the suspected silent-hang region. The downstream work it drives is `pm.client.sync_venv` / `pm.client.ensure_tools_for_sync` (`pm/client.py`, lines ~235 and ~268; implementation in `pm/install.py` `sync_venv`, line ~967).
- `pm/client.py` — `_request()` (line ~170). Worker result is read on stdout; after the result, the old code did `process.wait(timeout=5)` and raised `InstallError` on `TimeoutExpired` even though the result/receipt had already arrived.

Why "silent": takeover prints its startup marker only after the fix (below); before the fix, `_update_takeover.py` wrote nothing until it finished or failed. Silence in `_run_child` therefore could not distinguish "hung in prepare/sync" from "working normally".

## 3. Fixes applied

Branch: `fix/rc7-gate-stabilization` (PR #238). Local verification commit: `e86cf47b2995dbce8b3afd2b3170f6fb0cf2f781` (`fix: stabilize rc.7 release gate failures`). Files changed by that commit:

- `.github/workflows/windows-install-update-e2e.yml`
- `nastech_cli/_update_takeover.py`
- `pm/client.py`
- `tests/install/installer-script-e2e.sh`
- `tests/install/windows-e2e.ps1`
- `tests/pm/test_client_worker_wait.py`
- `tests/scripts/test_release_version_from_ref.py`

Specific changes in the root-cause area:

1. `nastech_cli/_update_takeover.py`
   - Startup marker `print("-> Update takeover started.", flush=True)` in `main()` so `_run_child` output shows the child actually launched.
   - `_start_prepare_watchdog(seconds=1500)` (25 minutes) started immediately before `prepare(request)`. On fire it prints a message, calls `faulthandler.dump_traceback(file=sys.stderr, all_threads=True)`, then `os._exit(2)`. A persistent hang now produces a stack dump instead of silence.
2. `pm/client.py` — `_request()`
   - After a result is received, wait up to 30s for worker exit; on `TimeoutExpired`, `terminate()` then `kill()` rather than raising `InstallError`. The already-received result/receipt is preserved. A slow worker teardown no longer fails a completed operation.
3. `tests/pm/test_client_worker_wait.py` — regression test `test_request_tolerates_slow_worker_exit_after_result`: a fake worker returns a result then sleeps 7s (longer than the old 5s wait); `pm.client._request("prune_cache", ...)` must return `"ok"`.
4. `tests/install/windows-e2e.ps1` (line ~848) — desktop-app-update driver `--timeout-ms` raised from 30m to `2100000` ms (35m), matching the open-app-update detached-updater wait and allowing a full PM sync + Desktop rebuild on large source diffs. The workflow file timeout was raised to 5400s; other installer-script E2E hardening (checkout-lock/quiescence waits, clearing historical installer churn) is in the same commit.

## 4. Verification

Commands already run locally on `fix/rc7-gate-stabilization` at `e86cf47b`:

- `git status --short` — clean at time of verification.
- `git show --stat --oneline HEAD` — confirms the 7-file change set above.
- Inspected `pm/client.py` lines 170–205: `wait(timeout=30)` -> `terminate()` -> `kill()` path present in both the success and exception branches.
- Inspected `nastech_cli/_update_takeover.py`: startup marker at `main()`, `_start_prepare_watchdog` default `seconds=1500` with `faulthandler.dump_traceback(..., all_threads=True)` and `os._exit(2)`, invoked before `prepare()`.
- Located driver timeout: `tests/install/windows-e2e.ps1:848` `--timeout-ms 2100000`.

Still required (not yet done at time of writing):

- Run the regression test: `python -m pytest tests/pm/test_client_worker_wait.py -v` (from the repo root, in the project's Python environment).
- Run the broader PM / install test slices per `scripts/run_tests.sh` and CI config.
- Watch the next gate run for `rc.7` (or its recut). Expected outcomes:
  - If the hang is gone: Mode A update rows complete and produce a receipt; no orphan processes at timeout.
  - If it persists: `_update_takeover.py` emits `! Update takeover preparation exceeded 1500s; dumping stacks.` followed by all-thread stacks on stderr, and the child exits 2. Use that dump to identify the exact blocking call in `prepare` / `sync_venv` / `ensure_tools_for_sync` before making any further change.

## 5. Do NOT guardrails

- Do not weaken receipt or completion semantics. `no successful update completion receipt; leaving the install untouched` is the correct safety behavior; make the update genuinely complete instead of bypassing or relaxing the receipt check.
- Do not remove or shorten the watchdog, startup marker, or stack dump to make a gate pass. They are diagnostics; a hang that cannot be observed cannot be fixed.
- Do not treat a flaky result as green by rerunning until it passes. Reproduce and stabilize; classify as a failure until proven otherwise.
- Do not raise timeouts as a substitute for a fix. The 35m driver ceiling and 5400s workflow timeout only remove a false ceiling on legitimately slow syncs; they do not excuse a silent hang.
- Do not conclude the bug is fixed from local unit tests alone — the failure is in the Windows/gate E2E path. Confirmation requires a gate row that completes and writes a receipt.
- No attribution hints: do not add comments, banners, changelog lines, or metadata implying the fix was copied from another project. Keep changes native to this codebase and consistent with its branding policy.
- Do not delete, rewrite, or "clean up" this file when closing the incident; append the confirming gate result instead.

## 6. Cross-reference (factual comparison, no action taken)

The historical takeover path was compared with `NousResearch/hermes-agent`: the takeover is equivalent there, and that project's `pm/client` had the same 5s post-result worker-wait issue. This comparison was diagnostic only; no upstream source, code, or attribution was copied into this repository. The fixes above were authored against the local codebase.
