# Hermes → Nastech Port Schedule

Source: `NousResearch/hermes-agent` (10511 files) → `NastechResearch/nastech-agent` (8736 files)
Gap: 2989 raw tracked files (1523 filesystem-only). Each batch rebranded via `hundredways/rules.py:128` and committed.

## Batches (saved for schedule)
- [x] **Batch1 agent:16** — `fix/port-hermes-batch1-agent` @ 80285ba — 2026-08-27 — no npm, `py_compile` 0 failed
- [ ] **Batch2 tools:21** — `tools/annotate_preview_tool.py:1` etc. — no npm, `py_compile` check
- [ ] **Batch3 gateway:8** + `tui_gateway:7`
- [ ] **Batch4 apps/desktop electron:200+** — `npm --workspace apps/desktop install` after
- [ ] **Batch5 apps/bootstrap-installer:4** + `ui-tui:18` + `web:16` — `npm install --workspaces=false` per workspace
- [ ] **Batch6 optional-mcps:60** + `website:32` + `skills/devops:1`
- [ ] **Batch7 tests:430** — final, `scripts/run_tests.sh:1` per-file isolation

## Each batch steps
1. `python3 -c "from hundredways.rules import BrandingRules; rules.transform_text(...)"`
2. `py_compile` + `npm install` (if JS) + `scripts/run_tests.sh tests/<area>/ -q`
3. `git add && git commit -m "port(<area>): batch<N>"` && `git push origin <branch>`

## Schedule
Run `python3 scripts/port_hermes_batch.py --batch <N>` daily via `nastech cron add --schedule "0 2 * * *" --command "python3 scripts/port_hermes_batch.py --next"`
