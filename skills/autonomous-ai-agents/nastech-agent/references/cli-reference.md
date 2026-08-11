# Nastech CLI Reference

Live sources when anything looks stale: `nastech --help`, `nastech <command> --help`,
https://nastechresearch.github.io/nastech-agent/docs/reference/cli-commands

### Global Flags

```
nastech [flags] [command]        (no subcommand = interactive chat)

  --version, -V             Show version
  -z, --oneshot PROMPT      One-shot: print ONLY the final response (for scripts/pipes)
  -m MODEL  --provider P    Model/provider override for this invocation
  -t, --toolsets LIST       Comma-separated toolsets for this invocation
  --resume, -r SESSION      Resume session by ID or title
  --continue, -c [NAME]     Resume by name, or most recent session
  --worktree, -w            Isolated git worktree mode (parallel agents)
  --skills, -s SKILL        Preload skills (comma-separate or repeat)
  --profile, -p NAME        Use a named profile
  --yolo                    Skip dangerous command approval
  --tui / --cli             Force the Ink TUI / classic REPL
  --ignore-rules            Skip AGENTS.md/SOUL.md/memory/skill injection
  --safe-mode               Disable ALL customizations (troubleshooting)
  --pass-session-id         Include session ID in system prompt
```

### Chat

```
nastech chat [flags]
  -q, --query TEXT          Single query, non-interactive
  --image PATH              Attach a local image to a single query
  -Q, --quiet               Suppress banner, spinner, tool previews
  --checkpoints             Enable filesystem checkpoints (/rollback)
  --max-turns N             Cap tool-calling iterations
  --source TAG              Session source tag (default: cli)
```
(plus the global flags above)

### Configuration

```
nastech setup [section]      Wizard (model|tts|terminal|gateway|tools|agent)
nastech model                Interactive model/provider picker
nastech fallback [add|remove|list]  Fallback provider chain
nastech config [show|edit|get|set|unset|path|env-path|check|migrate]
nastech login / logout       OAuth sign-in / clear stored auth
nastech doctor [--fix]       Check dependencies and config
nastech status [--all]       Component status
```

### Tools & Skills

```
nastech tools [list|enable NAME|disable NAME]   Per-platform toolsets (curses UI with no args)

nastech skills list|browse|search QUERY|inspect ID
nastech skills install ID    Hub identifier OR a direct https://…/SKILL.md URL
nastech skills config        Enable/disable skills per platform
nastech skills check|update|uninstall|publish PATH
nastech skills tap add REPO  Add a GitHub repo as a skill source
nastech bundles              Skill bundles (one /<name> alias loads several skills)
```

### MCP Servers

```
nastech mcp add NAME (--url or --command) | remove | list | test NAME
nastech mcp catalog | install NAME     Curated catalog install
nastech mcp configure NAME             Toggle tool selection
nastech mcp serve                      Run Nastech as an MCP server
```
Details (transport, tool discovery, catalog): `references/native-mcp.md`.

### Gateway (Messaging Platforms)

```
nastech gateway run|install|start|stop|restart|status|setup
```

20+ platforms: Telegram, Discord, Slack, WhatsApp (Baileys + Business Cloud API), iMessage (Photon — `nastech photon setup`), Signal, Email, SMS, Matrix, Mattermost, Teams, LINE, SimpleX, ntfy, Google Chat, Home Assistant, DingTalk, Feishu, WeCom, Weixin, API Server, Webhooks. Open WebUI connects via the API Server adapter. Most adapters ship under `plugins/platforms/`.
Docs: https://nastechresearch.github.io/nastech-agent/docs/user-guide/messaging/

### Sessions

```
nastech sessions list|browse|rename ID TITLE|delete ID|export OUT|prune|stats
```

### Cron / Webhooks

```
nastech cron list|create SCHED|edit ID|pause|resume|run ID|remove|status
    Schedules: '30m', 'every 2h', '0 9 * * *', ISO timestamp
nastech webhook subscribe NAME|list|remove NAME|test NAME
```
Webhook payloads/routes: `references/webhooks.md`.

### Profiles

```
nastech profile list|create NAME (--clone|--clone-all|--clone-from)|use|show|delete
nastech profile rename A B | alias NAME | export NAME | import FILE
```

### Credentials & Pools

```
nastech auth                 Interactive credential manager
nastech auth add [PROVIDER]  Add OAuth or API-key credential (nastech, openai-codex, qwen-oauth, …)
nastech auth list|remove P IDX|reset PROVIDER|status
```
Multiple credentials per provider form a pool that rotates automatically and skips exhausted keys.

### Other

```
nastech desktop / gui        Native desktop app
nastech dashboard            Web admin panel + embedded chat (--stop / --status)
nastech proxy                OpenAI-compatible local proxy backed by an OAuth provider
nastech portal               Quick setup / sign in via Nastech Portal
nastech kanban <verb>        Multi-agent work-queue board
nastech project              Named multi-folder workspaces
nastech skin list|use|set    Switch/tweak skins (see references/themes.md)
nastech pets <verb>          Pet mascots (see references/petdex.md)
nastech memory setup|status|off|reset   Memory provider
nastech secrets bitwarden|onepassword   External secret stores
nastech moa                  Mixture-of-Agents slots
nastech hooks / security / backup / import / checkpoints / console
nastech logs [-f] [errors]   View agent/error logs
nastech send                 One-off message through a gateway platform
nastech pairing / plugins / insights / journey / computer-use
nastech acp                  ACP server (IDE integration)
nastech completion bash|zsh|fish
nastech update / uninstall / claw migrate
```

Plugin- and provider-supplied subcommands (e.g. `nastech photon setup`) only appear once their plugin is installed/active.

### Where to Find Things

| Looking for... | Location |
|---|---|
| Config options | `nastech config edit` · [Configuration docs](https://nastechresearch.github.io/nastech-agent/docs/user-guide/configuration) |
| Tools / toolsets | `nastech tools list` · [Tools reference](https://nastechresearch.github.io/nastech-agent/docs/reference/tools-reference) |
| Skills catalog | `nastech skills browse` · [Skills catalog](https://nastechresearch.github.io/nastech-agent/docs/reference/skills-catalog) |
| Provider setup | `nastech model` · [Providers guide](https://nastechresearch.github.io/nastech-agent/docs/integrations/providers) |
| Env variables | `nastech config env-path` · [Env vars reference](https://nastechresearch.github.io/nastech-agent/docs/reference/environment-variables) |
| Gateway logs | `~/.nastech/logs/gateway.log` (or `nastech logs`) |
| Sessions | `nastech sessions browse` (reads state.db) |
