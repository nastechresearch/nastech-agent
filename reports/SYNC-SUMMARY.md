# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 81 commits affecting 1259 files.
- **Source revision:** `2eb0b3b2c895`.
- **Previous source revision:** `28803e68b452`.

## Technical coverage

- **agent/:** 29 changed files.
- **apps/:** 48 changed files.
- **cli-config.yaml.example/:** 1 changed files.
- **cli.py/:** 1 changed files.
- **contributors/:** 7 changed files.
- **gateway/:** 1 changed files.
- **nastech_cli/:** 22 changed files.
- **nastech_constants.py/:** 1 changed files.
- **plugins/:** 9 changed files.
- **run_agent.py/:** 4 changed files.
- **scripts/:** 11 changed files.
- **skills/:** 1 changed files.
- **tests/:** 55 changed files.
- **tools/:** 20 changed files.
- **toolsets.py/:** 1 changed files.
- **tui_gateway/:** 2 changed files.
- **ui-tui/:** 2 changed files.
- **website/:** 8 changed files.

## Delivered improvements

### New capabilities

- feat: runtime stall guards — identical-call loop breaker and continue-intent recovery (agent.stall_guards)
- feat: wall-clock run budget — wrap-up injection at 80% and deadline-scaled stale timeouts (agent.run_budget_seconds / --run-budget)
- feat: MCP tool results spill at 50K and carry upstream-elision warnings
- feat: execution-discipline guidance now reaches all tool-capable models (config model.execution_guidance)
- feat(image-gen): route live-catalog models to the Image API; merge picker catalogs; docs
- feat(plugins): add OpenRouter Image API surface to openrouter image_gen backend
- feat(desktop): close preview tabs on preview.close
- feat(tools): close_preview so the agent can dismiss the pane it opened
- feat(desktop): add an Appearance toggle that disables the intro splash
- feat(config): per-provider reasoning_echo opt-in for custom providers
- feat(skill): route nastech-agent's unknown-feature questions to llms.txt
- feat(skills): add --yes/-y flag to nastech skills uninstall

### Reliability and fixes

- fix(desktop): stand the terminal overlay down when its tab loses focus
- fix: read tool_budget config via load_config_readonly (config read guard)
- fix(bot-mode): accept both host.connections() shapes in the Create-on picker normalize
- fix(sdk): preserve primary in registered connections
- fix(sdk): return registered connection list
- fix(tools): honor raw stt.provider: local; finish _reconfigure_provider provider-string migration
- fix(cli): persist one provider string per picker row; mirror strict routing in status
- fix(browser): strict cloud-provider selection; camofox becomes a selection
- fix(voice): route TTS/STT OpenAI audio on the stored selection, not credentials
- fix(web): honor the stored web backend selection; no silent backend swaps
- fix(tools): dispatch image/video FAL strictly on the stored nastech tools selection
- fix: widen reasoning-effort wire translation to sibling sites (#89503 class)
- 21 additional reliability and fixes updates are included in this verified snapshot.

### Improvements

- Merge pull request #90351 from Nastechresearch/bb/terminal-tab-trap
- test(desktop): cover the terminal overlay hiding on an unfocused tab switch
- chore(sdk): remove unrelated session helper from #89893
- test(sdk): cover registry primary connection mapping
- test(sdk): cover connection registry list contract
- test(tools): repin selector/picker tests to the provider-string contract
- test(tools): pin strict provider-string selection per category
- test(codex): cover nested retention entry paths
- refactor(codex): name the dropped shape in the wire-guard warning
- test(codex): pin the retention drop to real endpoints
- chore: map contributor email for #89969 salvage
- chore: map contributor email for Haik-G
- 24 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
