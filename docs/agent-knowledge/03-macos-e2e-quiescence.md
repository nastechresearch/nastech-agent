# macOS installer-script E2E: HEAD→NEXT lock/quiescence contention flake

Durable knowledge for `nastech-agent`. This is an observed CI failure class with a
concrete root cause and a ported fix — not a "retry until green" item. Read this
before touching the installer-script E2E harness or re-triaging a red macOS E2E.

## Symptom / incident record

- Gate: rc.7 macOS installer-script E2E, HEAD→NEXT update legs.
- Attempt 1 jobs **136761052874** and **136761054598** failed on the macOS
  installer-script leg; both **passed on attempt 2** after an unmodified re-run.
- The pass-on-retry signature is the tell: same head, same inputs, different
  result. Per the repo flake policy (`tests/AGENTS.md`), pass-on-retry is green
  but printed under `⚠ FLAKY` and is "a bug to fix, not noise."

## Root cause

A stale checkout lock / sidecar marker, or an update still in flight, remained
present after the harness's prior quiescence check. The product refuses a second
updater/build while that lock is held, so a deferred completion could still be
running (or a Desktop build it spawned still held the shared checkout lock) when
the harness:

1. advanced the served `main` ref,
2. invoked the update method, and
3. captured the desktop launch.

Those three mutations raced with the live update/lock, so the outcome depended
on timing. The same guard already existed in `tests/install/macos-desktop-e2e.sh`
from the rc.4/rc.6 gate hardening; the script-install harness
(`tests/install/installer-script-e2e.sh`) had **not** been ported, which is why
only that leg flaked.

Relevant state that must be clear before mutating the checkout:

- Update-in-progress marker: `$NASTECH_HOME/.nastech-update-in-progress`.
- Checkout lock: `<git-common-dir>/nastech-update.lock` (fallback
  `$INSTALL_DIR/.nastech-update.lock`). A held `DesktopBuildLock` also holds the
  checkout lock beneath it for the whole build, so probing the checkout lock
  covers both.

## Fix (already applied on `fix/rc7-gate-stabilization`)

File: `tests/install/installer-script-e2e.sh`

Ported two helpers from `tests/install/macos-desktop-e2e.sh`:

- `checkout_lock_held()` (line ~404) — probes the lock with a non-blocking
  `fcntl.flock(LOCK_EX | LOCK_NB)` via an inline `python3` heredoc. Exit 0 =
  lock held (busy), exit 1 = free; permission/OSError is treated as held.
- `wait_for_update_quiescence()` (line ~435) — default timeout 600s, polls every
  10s until BOTH the marker is absent and `checkout_lock_held` reports free.
  On timeout it prints a diagnostic (`marker`/`lock`/`path`) and returns 1.

Key correctness detail — **git-common-dir anchoring**: the lock path is derived
with `git -C "$INSTALL_DIR" rev-parse --git-common-dir`. That value is relative
to the `-C` directory (normally `.git`), so the script anchors a relative result
to `$INSTALL_DIR` exactly as `update_lock.checkout_lock_path` does; otherwise a
held *real* lock looks free because the probe checks the wrong path.

Three call sites, each `wait_for_update_quiescence 600 || fail ...`:

1. Before served-ref advance — `git -C "$SERVE_REPO" update-ref refs/heads/main "$TARGET_SHA"` (line ~468/470).
2. Before invoking the update method (inside the `nastech-update` branch, just before `source_build_env "${update_cmd[@]}"`) (line ~507).
3. Before the desktop launch capture / build preflight that takes `DesktopBuildLock` (`nastech-desktop-app-update` branch) (line ~541).

Validation performed: `bash -n tests/install/installer-script-e2e.sh` (syntax OK).

## Guardrails

- **Do not classify this as "just flaky" without evidence.** A retry-only
  resolution hides a real lock race. Require the pass-on-retry receipt plus a
  root-cause hypothesis before moving on.
- **Harden quiescence, don't widen the wait blindly.** The fix is a correct lock
  probe (git-common-dir anchored) at every mutation boundary, not just a longer
  sleep. Any new site that advances the served ref, runs an update, or launches a
  desktop build must add its own `wait_for_update_quiescence` call.
- Keep all three call sites in lockstep with `tests/install/macos-desktop-e2e.sh`;
  that file is the reference implementation for this guard.
- Preserve the `⚠ FLAKY` flake policy: a failing file retried once in a fresh
  subprocess is green but flagged, and pass-on-retry is a bug to fix.

## How to confirm / detect recurrence

- Syntax check: `bash -n tests/install/installer-script-e2e.sh`.
- Confirm the guard is present at all three boundaries:
  `grep -n 'wait_for_update_quiescence\|checkout_lock_held\|--git-common-dir' tests/install/installer-script-e2e.sh`
  — expect the two helper definitions plus three `wait_for_update_quiescence 600`
  call sites and the `--git-common-dir` anchoring line.
- Confirm the git-common-dir anchor is present (relative path prefixed with
  `$INSTALL_DIR/`); if removed, a held real lock can read as free and the race
  returns.
- Recurrence signature: same head passes on unmodified re-run on the macOS
  installer-script E2E leg (HEAD→NEXT), typically with an update/desktop build
  concurrently active. If seen, check whether a new mutation boundary was added
  without a quiescence call, or whether the lock path lost its git-common-dir
  anchor, before re-running.
- Run the leg with the repo runner (never bare tools for Python tests):
  `scripts/run_tests.sh` is the canonical runner for `tests/`; installer shell
  scripts are validated with `bash -n` here and exercised via their dedicated
  E2E lane.
