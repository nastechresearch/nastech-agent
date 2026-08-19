# NasTech-Agent Update Summary

> Powered by NousResearch

This verified NasTech-Agent update incorporates the newest confirmed improvements from its open-source foundation. The summary below focuses on delivered functionality, reliability, and operational impact.

## Update scope

- **Changes incorporated:** 120 commits affecting 1255 files.
- **Source revision:** `28803e68b452`.
- **Previous source revision:** `5dd15872a687`.

## Technical coverage

- **.github/:** 6 changed files.
- **agent/:** 3 changed files.
- **apps/:** 475 changed files.
- **contributors/:** 5 changed files.
- **gateway/:** 2 changed files.
- **nastech_cli/:** 12 changed files.
- **package-lock.json/:** 3 changed files.
- **plugins/:** 13 changed files.
- **run_agent.py/:** 1 changed files.
- **tests/:** 21 changed files.
- **tools/:** 7 changed files.
- **toolsets.py/:** 1 changed files.
- **tui_gateway/:** 4 changed files.
- **ui-tui/:** 8 changed files.
- **website/:** 20 changed files.

## Delivered improvements

### New capabilities

- feat(desktop): scope the translucency controls to what each OS can do
- feat(desktop): back window glass with Windows 11 system materials
- feat(image-gen): OpenRouter image picker lists every live image-output model; xAI edits honor dispatched model
- feat(image-gen): add Grok Imagine Image 2.0 to the FAL image catalog
- feat(image-gen): xAI Grok image catalog goes live-driven; grok-imagine-image-2.0 selectable
- feat(desktop): add a dev-only tour demo
- feat(desktop): name the app's shared surfaces for tours
- feat(desktop): give tours a themed spotlight and directional motion
- feat(tools): tour — let the agent walk a user through the UI
- feat(desktop): answer tour.request from the renderer
- feat(desktop): run tours inside the preview pane
- feat(desktop): tour engine — highlight and narrate any DOM
- 11 additional new capabilities updates are included in this verified snapshot.

### Reliability and fixes

- fix(image_gen): Grok Imagine 2.0 no longer upscales by default — opt-in policy restored
- fix(tui): allow the ESC byte in the SGR param matcher
- fix(tui): stop the composer placeholder from sticking Terminal.app into dim
- fix(desktop): send review agent-ship to the composer that opened it
- fix(desktop): isolate composer submit to one visible surface
- fix(desktop): sort translucency named exports for eslint
- fix(desktop): keep the preload bridge alive under the sandbox
- fix(desktop): keep recents when ALL-profiles scope has one profile
- fix(desktop): scope session lookup to the active profile
- fix(desktop): Bot Mode chats no longer paint blank when switching between running bots
- fix(desktop): skill hub installs on non-default profiles no longer 404, and failed installs surface
- fix(xai): forward image_gen.model kwarg to _resolve_model in generate()
- 29 additional reliability and fixes updates are included in this verified snapshot.

### Documentation

- docs(desktop): repoint comments at the modules that now own the code
- docs: cover nastech chat --query-file and the file-based Bot Mode DM transport
- docs(tour): document navigating steps and the handle vocabulary
- docs(desktop): clarify connection settings copy
- docs(desktop): explain multi-source session scoping
- docs: surface Bot Mode in docs landing paths

### Improvements

- Merge pull request #90113 from Nastechresearch/bb/review-submit-isolation
- Merge pull request #89611 from Nastechresearch/bb/desktop-godfiles
- Merge pull request #89837 from Nastechresearch/bb/glass-acrylic
- Merge pull request #89817 from Nastechresearch/bb/sidebar-all-profiles-scope
- Merge pull request #89833 from Nastechresearch/bb/scope-session-lookup
- chore: kick CI
- chore: kick CI
- test(desktop): share the duplicated fixtures
- refactor(desktop): give duplicated helpers one owner
- refactor(desktop): extract IPC clusters from electron/main.ts
- refactor(desktop): split lib/chat-messages.ts into concern modules
- refactor(desktop): split gateway-event.ts into per-family handler modules
- 38 additional improvements updates are included in this verified snapshot.

## Verification evidence

- **Direct source provenance:** Passed
- **Brand and asset integrity:** Passed
- **Dependency, security, and publication-readiness scans:** Passed
- **Full verification and fork-consistency checks:** Passed

This candidate is prepared for review only. No merge, release, or deployment is performed by the verification workflow.
