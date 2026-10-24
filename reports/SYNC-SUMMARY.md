# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 677 commits affecting 3344 files.
- **Source revision:** `5894e750c3db`.
- **Previous source revision:** `ebc9960b9d42`.

## Technical coverage

- **.env.example/:** 2 changed files.
- **.envrc/:** 2 changed files.
- **.github/:** 11 changed files.
- **.npmrc/:** 3 changed files.
- **CONTRIBUTING.md/:** 2 changed files.
- **Dockerfile/:** 3 changed files.
- **README.es.md/:** 1 changed files.
- **README.md/:** 2 changed files.
- **README.ur-pk.md/:** 1 changed files.
- **README.zh-CN.md/:** 1 changed files.
- **acp_adapter/:** 3 changed files.
- **agent/:** 108 changed files.
- **apps/:** 592 changed files.
- **batch_runner.py/:** 1 changed files.
- **cli-config.yaml.example/:** 8 changed files.
- **cli.py/:** 3 changed files.
- **contributors/:** 25 changed files.
- **cron/:** 3 changed files.
- **docker/:** 3 changed files.
- **evals/:** 8 changed files.
- **flake.lock/:** 2 changed files.
- **gateway/:** 94 changed files.
- **locales/:** 202 changed files.
- **model_tools.py/:** 1 changed files.
- **nastech_cli/:** 276 changed files.
- **nastech_constants.py/:** 1 changed files.
- **nastech_state_local.py/:** 1 changed files.
- **nastech_state_worker_context.py/:** 1 changed files.
- **nix/:** 24 changed files.
- **optional-skills/:** 28 changed files.
- **package-lock.json/:** 4 changed files.
- **package.json/:** 3 changed files.
- **plugin-catalog/:** 204 changed files.
- **plugins/:** 24 changed files.
- **pm/:** 33 changed files.
- **providers/:** 1 changed files.
- **pyproject.toml/:** 53 changed files.
- **requirements-payload.txt/:** 2 changed files.
- **run_agent.py/:** 1 changed files.
- **scripts/:** 29 changed files.
- **skills/:** 67 changed files.
- **tests/:** 648 changed files.
- **tests-js/:** 4 changed files.
- **tools/:** 275 changed files.
- **toolsets.py/:** 1 changed files.
- **tui_gateway/:** 68 changed files.
- **ui-tui/:** 44 changed files.
- **uv.lock/:** 59 changed files.
- **web/:** 9 changed files.
- **website/:** 210 changed files.

## Delivered improvements

### New capabilities

- feat(desktop): name the owning chat in transcript directive props
- feat(desktop): folder-scoped plugin file access (ctx.files)
- feat(plugins): desktop surface lint refuses reaching the preview webview
- feat(desktop): gate preview scripts behind a declared capability and per-origin consent
- feat(desktop): preview.executeJavaScript SDK door for plugins
- feat(tools): terminal backends can declare that file tools go through the sandbox
- feat(desktop): app-owned composer context-menu slot + host.spellcheck
- feat(desktop): pass the board's tenant list to Kanban badge decorators
- feat(desktop): app-owned Kanban card badge slot in the plugin SDK
- feat(desktop): allow explicit canonical Bot Chat tab opens
- feat(plugin-catalog): add the timestamp-ref catalog card
- feat(plugin-catalog): add timestamp-ref
- 50 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(mcp): accept SSE responses over 1 MiB on Streamable HTTP
- fix: address review — Feishu plain .ogg stays a file, Ogg duration walks pages
- fix(cron): forward the voice flag when cron delivery calls send_voice
- fix(gateway): keep plain audio MEDIA out of WhatsApp/BlueBubbles voice notes
- fix(discord): send plain audio as an attachment, voice messages only as Ogg/Opus
- fix(mcp): mask every secret-shaped argument and show arguments on the text approval
- fix(mcp): keep trust-gate arguments redacted and legible on every approval surface
- fix(mcp): show redacted, size-capped arguments on untrusted MCP write approvals
- fix(mcp): YOLO and approvals.mode off skip the untrusted-server trust prompt
- fix(mcp): trust-gate Session/Always answers now stick per (server, tool)
- fix(image_gen): keep palette transparency and EXIF orientation when shrinking FAL sources
- fix(image_gen): inline local source paths for FAL edits on the local backend
- 233 additional reliability and fixes updates are included in this verified snapshot.

### Performance

- perf(mcp): bound the work behind a large trust-gate argument preview

### Documentation

- docs: name each YOLO source's reach; sampling never prompts the user
- docs: YOLO / approvals.mode off skip the MCP trust prompt, not the spend limit
- docs(mcp): deleting an Always entry leaves the granting chat's copy until it ends
- docs(mcp): what the trust-gate and one-shot consent prompts offer
- docs(image_gen): fit the style-reference catalog line under the 80-char cap
- docs(tools): lead every tool description with its key capability
- docs(desktop): document ctx.preview capability and per-origin consent
- docs(catalog): argue nastech-windows-ports on latency and process surface
- docs(catalog): disclose credential-bearing saved presets
- docs(plugins): portable packages lack requires_nastech, not a version field
- docs(config): the v52 browser notices reach startup migrations too and name what they removed or pinned
- docs(browser): browser_cdp and browser_dialog still need a configured CDP endpoint
- 11 additional documentation updates are included in this verified snapshot.

### Improvements

- test(mcp): let the reconnect tests' fake streamable_http_client take SDK kwargs
- refactor(mcp): trim the 1 MiB SSE fix to the transport argument
- test(cron): move the voice-flag delivery tests into their own file
- test(mcp): trust-gate approval scopes match what each prompt offers
- chore: map Schildkrote contributor email
- test(tools): pin the confined-backend tests to POSIX with the fast path at its default
- refactor(nix): stdenv.is* -> stdenv.hostPlatform.is*
- chore(nix): nix flake update
- chore(plugin-catalog): re-pin bubblewrap to da8d324 (1.2.1)
- chore(plugin-catalog): re-pin bubblewrap to 35d24e4 (1.2.0)
- refactor(tui): keep server.py from growing by moving the scoped provider lookup to agent_factory
- chore(release): map @DearGlory's commit email
- 334 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** fresh-direct-clone at 5894e750c3db, fetched 2026-10-24T02:10:51+00:00
- **Publication gate:** PASS - cleared for human review only
- **Tree parity:** 20902/20902 files verified byte-faithful after branding; no outstanding differences
- **Branding:** 20902 files branded, 20717 rewritten, 0 errors
- **Fork consistency:** 0 inconsistency violations, 49 fork-owned files carried forward
- **Upstream change evidence:** added 286, deleted 75, modified 1152, renamed 0

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
