# pm/ — dependencies and Nastech environments

Applies on top of the root `AGENTS.md` (which carries the short form of the pinning rule).

## Dependency pinning policy

All dependencies carry upper bounds (litellm compromise #2796/#2810; Mini Shai-Hulud worm,
May 2026). PyPI: `>=floor,<next_major` (`"httpx>=0.28.1,<1"`); pre-1.0: `<0.(minor+2)`
(`>=0.29,<0.32`). Git URLs: 40-char commit SHA. GitHub Actions: SHA + `# vN` comment. CI-only
Python requirements: `==exact`. A bare `>=X.Y.Z` is rejected by CI and reviewers.
After changing `pyproject.toml`, run `nastech pm lock`, re-source `./activate`, and commit
`pyproject.toml` with `uv.lock`. Reference: #2810 (bounds), #9801 (SHA pinning + audit CI).

PM owns Nastech Python dependency changes. Use `pm.sync_venv(['extra'], explicit=True)`
for declared runtime extras, `nastech pm install` for setup/sync, and `nastech pm repair`
for damaged dependencies. Do not mutate Nastech environments with raw pip or uv.
Use `pm.build_environment` for fresh build outputs and `pm.ensure_environment` for
isolated tool environments. Callers receive an interpreter or tool path, not uv.
Nix's declarative uv2nix builds and unrelated user projects remain independently owned.

The `[tool.uv] exclude-newer = "3 days"` release-age check covers **Nastech's own dependencies
only**, exact pins included, with one per-package exemption class: CA trust stores (`certifi`),
whose revocation releases must reach the lock the day they ship (`exclude-newer-package`; nothing
else goes there). It runs when Nastech LOCKS
(`nastech pm lock`, CI's lock check), never on users' machines: every generated workspace drops the
cutoff (`pm/workspace.py::_without_release_age`), so a mirror without upload times cannot break an
install (#135589). Plugin resolution is unchanged by this: core's exact pins stay put, and a plugin
may move a transitive core package within core's declared ranges
(`tests/pm/test_workspace_build_inputs.py::test_plugin_can_move_compatible_transitive_but_not_exact_requirement`).
Plugin `python_dependencies` follow the plugin's own policy. Teknium's rulings: "plugins dont have to abide by our 14 day rule … Only nastech'
dependencies themselves have to"; dates are checked by us, not users; pinned deps need >3 days.
