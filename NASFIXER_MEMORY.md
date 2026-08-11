# Nasfixer Working Memory

Shared working memory for the Nasfixer collaboration. Read this every session.
This is our living record — update it as the project moves.

## Working Agreement

- **Everything lands on the `Nasfixer` branch.** All our fixes and changes
  are committed there and flow to `main` only through PRs, so nothing is ever
  merged blind.
- **PRs are the safety rail.** Each change gets its own PR, CI runs on it, and
  we review together before merging. No direct pushes to `main` for our work.
- **The project is delicate.** It is the nastech-agent codebase — the core
  agent (`run_agent.py`, `model_tools.py`, `cli.py`) is a narrow waist and
  every core tool ships on every API call. Read the Contribution Rubric in
  `AGENTS.md` before touching core. When in doubt, ask each other.
- **Fix the whole bug class, not one site.** Reproduce the symptom on `main`,
  point to the exact line, and cover sibling call paths too.
- **Cache-safe.** Never mutate past context, swap toolsets, or rebuild the
  system prompt mid-conversation (prompt caching is sacred).
- **Profile-safe.** Use `get_nastech_home()` / `display_nastech_home()`, never
  hardcode `~/.nastech`.
- **We stick together always.** If I am unsure, I ask rather than guess.

## Current Task Context

### install-e2e / pick-release-tags (in progress)

**Goal:** make the install/update E2E matrix honest. It must sample the real
set of releases a nastech user can actually be on, so updates are exercised
against real upgrade paths.

**The rebrand problem:** the repo lived as `hermes-agent` (upstream remote
`NousResearch/hermes-agent`) and rebranded to nastech around **v2026.8.11**
(the hermes→nastech rebrand). Releases before that installed an app called
`hermes` into `~/.hermes/...` — no nastech user is in that state, so updating
FROM them is meaningless (and the E2E harness is nastech-shaped). This is the
"match hermes / must be perfect" point: the floor is the first nastech-branded
release and must not drift backward into the hermes era.

**What we changed in `scripts/sandbox/pick-release-tags.sh`:**

1. **nastech-era floor filter** — `NASTECH_FLOOR="v2026.8.11"`, only tags
   `>=` floor survive (version-sorted comparison). Future releases are newer,
   so this never needs bumping.
2. **Current-release exclusion** — drop the tag whose commit equals the
   checkout being tested (`base == target` is a no-op the harness rejects).
3. **Fixed `had_tags` ordering bug** — it was captured *after* the filters, so
   "tags exist but none qualify" was misreported as "no tags at all" (a
   shallow-clone error). Now captured right after the tag list is read, and the
   empty-qualified case prints a `note:` and emits `[]` (exit 0) instead of
   erroring.

**Verified behavior:**
- Real checkout today: emits `[]` (only nastech tag is v2026.8.11 == current
  `main`, so nothing to update FROM yet). Workflow jobs are skipped, not
  failed — that is correct until the next release ships.
- Temp repo with mixed hermes/nastech tags: correctly drops hermes-era
  (`v2026.7.7`, `v2026.8.3`) and picks only nastech-era; with `HEAD` moved past
  the newest tag, samples `["v2026.8.11","v2026.8.18","v2026.9.2"]`.
- `--count 1` emits newest only; spread dedupes on rounding collisions.

**Status (current):**
- Branch `Nasfixer` created, change committed (`f4a9ccb86`), pushed.
- **PR #10 open** → https://github.com/nastechresearch/nastech-agent/pull/10
  (base `main`, head `Nasfixer`). CI running on it.
- The pick-releases job runs on `workflow_dispatch`, so the empty matrix is the
  expected honest output until the next release. Once CI is green, we review
  together and merge. After merge, we can `workflow_dispatch` the
  `install-e2e.yml` manually to watch it skip gracefully.
- Current checkout has no qualifying update-FROM tag (v2026.8.11 == main), so
  no E2E legs run today. After the NEXT release ships, the matrix will sample
  real nastech→nastech upgrade paths.

## Project Map (quick orientation)

- `run_agent.py` — `AIAgent` core loop; `run_conversation()` is the heart.
- `model_tools.py` — tool orchestration; `discover_builtin_tools()`,
  `handle_function_call()`; plugin discovery side effect lives here.
- `toolsets.py` — `TOOLSETS` dict + `_NASTECH_CORE_TOOLS` default bundle.
- `cli.py` — `NastechCLI`; `process_command()` dispatches slash commands.
- `gateway/` — messaging gateway; `run.py` + `session.py` + `platforms/`.
- `tools/` — tool implementations; auto-discovered via `tools/registry.py`.
- `scripts/run_tests.sh` — ALWAYS use this, never bare `pytest`.
- Tests: `tests/` (~17k). Use `scripts/run_tests.sh tests/path -k name`.

## Commands We Use

- `scripts/run_tests.sh [path] [-k name]` — CI-parity test runner.
- `bash scripts/sandbox/pick-release-tags.sh --count N [--repo DIR]` — tag
  picker (source of truth for the E2E matrix).
- `git -C <repo> tag --list 'v*'` — see what release tags exist.
- Workflow: `.github/workflows/install-e2e.yml` — matrix built from
  `pick-releases` output via `fromJSON`.
