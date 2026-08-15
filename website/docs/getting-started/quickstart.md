---
sidebar_position: 1
title: "Quickstart"
description: "Your first conversation with Nastech Agent — from install to chatting in under 5 minutes"
---

# Quickstart

This guide gets you from zero to a working Nastech setup that survives real use. Install, choose a provider, verify a working chat, and know exactly what to do when something breaks.

## Prefer to watch?

**Onchain AI Garage** put together a Masterclass walkthrough of installation, setup, and basic commands — a good companion to this page if you'd rather follow along on video. For more, see the full [Nastech Agent Tutorials & Use Cases](https://www.youtube.com/playlist?list=PLmpUb_PWAkDxewld5ZYyKifuHxgIbiq2d) playlist.

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
  <iframe
    style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%'}}
    src="https://www.youtube-nocookie.com/embed/R3YOGfTBcQg"
    title="Nastech Agent Masterclass: Installation, Setup, Basic Commands"
    frameBorder="0"
    allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowFullScreen
  ></iframe>
</div>

## Who this is for

- Brand new and want the shortest path to a working setup
- Switching providers and don't want to lose time to config mistakes
- Setting up Nastech for a team, bot, or always-on workflow
- Tired of "it installed, but it still does nothing"

## The fastest path

Pick the row that matches your goal:

| Goal | Do this first | Then do this |
|---|---|---|
| I just want Nastech working on my machine | `nastech setup` | Run a real chat and verify it responds |
| I already know my provider | `nastech model` | Save the config, then start chatting |
| I want a bot or always-on setup | `nastech gateway setup` after CLI works | Connect Telegram, Discord, Slack, or another platform |
| I want a local or self-hosted model | `nastech model` → custom endpoint | Verify the endpoint, model name, and context length |
| I want multi-provider fallback | `nastech model` first | Add routing and fallback only after the base chat works |

**Rule of thumb:** if Nastech cannot complete a normal chat, do not add more features yet. Get one clean conversation working first, then layer on gateway, cron, skills, voice, or routing.

---

## 1. Install Nastech Agent
### With the Nastech Desktop installer on macOS or Windows (recommended)
To easily install the command-line and desktop applications, [download the Nastech Desktop installer](https://nastechresearch.github.io/nastech-agent/) from our website and run it.

### Without Nastech Desktop:
For a command-line only install without Nastech Desktop, run:

#### Linux / macOS / WSL2 / Android (Termux)
```bash
curl -fsSL https://nastechresearch.github.io/nastech-agent/install.sh | bash
```

#### Windows (native)

Run in powershell:
```powershell
iex (irm https://nastechresearch.github.io/nastech-agent/install.ps1) 
```

:::tip Android / Termux
If you're installing on a phone, see the dedicated [Termux guide](./termux.md) for the tested manual path, supported extras, and current Android-specific limitations.
:::

After it finishes, reload your shell:

```bash
source ~/.bashrc   # or source ~/.zshrc
```

For detailed installation options, prerequisites, and troubleshooting, see the [Installation guide](./installation.md).

## 2. Choose a Provider

The single most important setup step. Use `nastech model` to walk through the choice interactively:

```bash
nastech model
```

:::tip Easiest path: Nastech Portal
One subscription covers 300+ models plus the [Tool Gateway](../user-guide/features/tool-gateway.md) (web search, image generation, TTS, cloud browser). On a fresh install:

```bash
nastech setup --portal
```

That logs you in, sets Nastech as your provider, and turns on the Tool Gateway in one command.
:::

:::info Setup modes
On a fresh install, `nastech setup` offers three modes:

- **Quick Setup (Nastech Portal)** — free OAuth login, no API keys; sets up a model plus the Tool Gateway tools. The recommended fast path.
- **Full Setup** — walk through every provider, tool, and option yourself (bring your own keys).
- **Blank Slate** — everything starts **off** except the bare minimum needed to run an agent: **provider & model, the File Operations toolset, and the Terminal toolset**. No web, browser, code execution, vision, memory, delegation, cron, skills, plugins, or MCP servers — and compression, checkpoints, smart routing, and memory capture are all disabled. After the minimal baseline is applied, you choose one of two paths: **start with everything disabled** (finish now with the minimal agent), or **walk through all configurations** (opt in to tools, skills, plugins, MCP, and messaging). Pick this when you want a minimal, fully-controlled agent and intend to enable only exactly what you need.

Blank Slate writes an explicit `platform_toolsets.cli` list plus `agent.disabled_toolsets`, so nothing you didn't choose ever loads — not even after `nastech update`. Re-enable anything later with `nastech tools`, seed skills with `nastech skills opt-in --sync`, or tune settings with `nastech setup agent`.
:::

Good defaults:

| Provider | What it is | How to set up |
|----------|-----------|---------------|
| **Nastech Portal** | Subscription-based, zero-config | OAuth login via `nastech model` |
| **OpenAI Codex** | ChatGPT or Codex subscription, uses Codex models | Device code auth via `nastech model` → **ChatGPT or Codex Subscription** |
| **Anthropic** | Claude models directly — Max plan + extra usage credits (OAuth), or API key for pay-per-token | `nastech model` → OAuth login (requires Max + extra credits), or an Anthropic API key |
| **OpenRouter** | Multi-provider routing across many models | Enter your API key |
| **Fireworks AI** | Direct OpenAI-compatible model API | Set `FIREWORKS_API_KEY` |
| **Z.AI** | GLM / Zhipu-hosted models | Set `GLM_API_KEY` / `ZAI_API_KEY` (also accepts `Z_AI_API_KEY`) |
| **Kimi / Moonshot** | Moonshot-hosted coding and chat models | Set `KIMI_API_KEY` (or the Kimi-Coding-specific `KIMI_CODING_API_KEY`) |
| **Kimi / Moonshot China** | China-region Moonshot endpoint | Set `KIMI_CN_API_KEY` |
| **Arcee AI** | Trinity models | Set `ARCEEAI_API_KEY` |
| **GMI Cloud** | Multi-model direct API | Set `GMI_API_KEY` |
| **Actual Computer** | Your own hardware as a private inference cluster — hosted relay or local daemon | Set `ACTUAL_API_KEY` (relay) or `ACTUAL_BASE_URL=http://127.0.0.1:8080` (local, no key) |
| **MiniMax (OAuth)** | MiniMax frontier model via browser OAuth — no API key needed (model name in `nastech_cli/models.py` may change between releases) | `nastech model` → MiniMax (OAuth) |
| **MiniMax** | International MiniMax endpoint | Set `MINIMAX_API_KEY` |
| **MiniMax China** | China-region MiniMax endpoint | Set `MINIMAX_CN_API_KEY` |
| **Alibaba Cloud** | Qwen models via DashScope | Set `DASHSCOPE_API_KEY` (Qwen Coding Plan also accepts `ALIBABA_CODING_PLAN_API_KEY`) |
| **Hugging Face** | 20+ open models via unified router (Qwen, DeepSeek, Kimi, etc.) | Set `HF_TOKEN` |
| **AWS Bedrock** | Claude, Nova, Llama, DeepSeek via native Converse API | IAM role or `aws configure` ([guide](../guides/aws-bedrock.md)) |
| **Azure Foundry** | Azure AI Foundry-hosted models | Set `AZURE_FOUNDRY_API_KEY` + `AZURE_FOUNDRY_BASE_URL` |
| **Google AI Studio** | Gemini models via direct API | Set `GOOGLE_API_KEY` / `GEMINI_API_KEY` |
| **xAI** | Grok models via direct API | Set `XAI_API_KEY` |
| **xAI Grok OAuth** | SuperGrok / Premium+ subscription, no API key needed | `nastech model` → xAI Grok OAuth |
| **NovitaAI** | Multi-model API gateway | Set `NOVITA_API_KEY` |
| **StepFun** | Step Plan models | Set `STEPFUN_API_KEY` |
| **Xiaomi MiMo** | Xiaomi-hosted models | Set `XIAOMI_API_KEY` |
| **Tencent TokenHub** | Tencent-hosted models | Set `TOKENHUB_API_KEY` |
| **Ollama Cloud** | Managed Ollama-hosted models | Set `OLLAMA_API_KEY` |
| **LM Studio** | Local desktop app exposing an OpenAI-compatible API | Set `LM_API_KEY` (and `LM_BASE_URL` if non-default) |
| **Qwen OAuth** | Qwen Portal browser OAuth — no API key needed | `nastech model` → Qwen OAuth |
| **Kilo Code** | KiloCode-hosted models | Set `KILOCODE_API_KEY` |
| **OpenCode Zen** | Pay-as-you-go access to curated models | Set `OPENCODE_ZEN_API_KEY` |
| **OpenCode Go** | $10/month subscription for open models | Set `OPENCODE_GO_API_KEY` |
| **DeepSeek** | Direct DeepSeek API access | Set `DEEPSEEK_API_KEY` |
| **NVIDIA NIM** | Nemotron models via build.nvidia.com or local NIM | Set `NVIDIA_API_KEY` (optional: `NVIDIA_BASE_URL`) |
| **GitHub Copilot** | GitHub Copilot subscription (GPT-5.x, Claude, Gemini, etc.) | OAuth via `nastech model`, or `COPILOT_GITHUB_TOKEN` / `GH_TOKEN` |
| **GitHub Copilot ACP** | Copilot ACP agent backend (spawns local `copilot` CLI) | `nastech model` (requires `copilot` CLI + `copilot login`) |
| **Vercel AI Gateway** | Vercel AI Gateway routing | Set `AI_GATEWAY_API_KEY` |
| **Custom Endpoint** | VLLM, SGLang, Ollama, or any OpenAI-compatible API | Set base URL + API key |

For most first-time users: choose a provider, accept the defaults unless you know why you're changing them. The full provider catalog with env vars and setup steps lives on the [Providers](../integrations/providers.md) page.

:::caution Minimum context: 64K tokens
Nastech Agent requires a model with at least **64,000 tokens** of context. Models with smaller windows cannot maintain enough working memory for multi-step tool-calling workflows and will be rejected at startup. Most hosted models (Claude, GPT, Gemini, Qwen, DeepSeek) meet this easily. If you're running a local model, set its context size to at least 64K (e.g. `--ctx-size 65536` for llama.cpp or `-c 65536` for Ollama).
:::

:::tip
You can switch providers at any time with `nastech model` — no lock-in. For a full list of all supported providers and setup details, see [AI Providers](../integrations/providers.md).
:::

### How settings are stored

Nastech separates secrets from normal config:

- **Secrets and tokens** → `~/.nastech/.env`
- **Non-secret settings** → `~/.nastech/config.yaml`

The easiest way to set values correctly is through the CLI:

```bash
nastech config set model anthropic/claude-opus-4.6
nastech config set terminal.backend docker
nastech config set OPENROUTER_API_KEY sk-or-...
```

The right value goes to the right file automatically.

## 3. Run Your First Chat

```bash
nastech            # classic CLI
nastech --tui      # modern TUI (recommended)
```

You'll see a welcome banner with your model, available tools, and skills. Use a prompt that's specific and easy to verify:

:::tip Pick your interface
Nastech ships with two terminal interfaces: the classic `prompt_toolkit` CLI and a newer [TUI](../user-guide/tui.md) with modal overlays, mouse selection, and non-blocking input. Both share the same sessions, slash commands, and config — try each with `nastech` vs `nastech --tui`.
:::

```
Summarize this repo in 5 bullets and tell me what the main entrypoint is.
```

```
Check my current directory and tell me what looks like the main project file.
```

```
Help me set up a clean GitHub PR workflow for this codebase.
```

**What success looks like:**

- The banner shows your chosen model/provider
- Nastech replies without error
- It can use a tool if needed (terminal, file read, web search)
- The conversation continues normally for more than one turn

If that works, you're past the hardest part.

## 4. Verify Sessions Work

Before moving on, make sure resume works:

```bash
nastech --continue    # Resume the most recent session
nastech -c            # Short form
```

That should bring you back to the session you just had. If it doesn't, check whether you're in the same profile and whether the session actually saved. This matters later when you're juggling multiple setups or machines.

## 5. Try Key Features

### Use the terminal

```
❯ What's my disk usage? Show the top 5 largest directories.
```

The agent runs terminal commands on your behalf and shows results.

### Slash commands

Type `/` to see an autocomplete dropdown of all commands:

| Command | What it does |
|---------|-------------|
| `/help` | Show all available commands |
| `/tools` | List available tools |
| `/model` | Switch models interactively |
| `/personality pirate` | Try a fun personality |
| `/save` | Save the conversation |

### Multi-line input

Press `Alt+Enter`, `Ctrl+J`, or `Shift+Enter` to add a new line. `Shift+Enter` requires a terminal that sends it as a distinct sequence (Kitty / foot / WezTerm / Ghostty by default; iTerm2 / Alacritty / VS Code terminal once the Kitty keyboard protocol is enabled). `Alt+Enter` and `Ctrl+J` work in every terminal.

### Interrupt the agent

If the agent is taking too long, type a new message and press Enter — it interrupts the current task and switches to your new instructions. `Ctrl+C` also works.

## 6. Add the Next Layer

Only after the base chat works. Pick what you need:

### Bot or shared assistant

```bash
nastech gateway setup    # Interactive platform configuration
```

Connect [Telegram](/user-guide/messaging/telegram), [Discord](/user-guide/messaging/discord), [Slack](/user-guide/messaging/slack), [WhatsApp](/user-guide/messaging/whatsapp), [Signal](/user-guide/messaging/signal), [Email](/user-guide/messaging/email), or [Home Assistant](/user-guide/messaging/homeassistant), or [Microsoft Teams](/user-guide/messaging/teams).

### Automation and tools

- `nastech tools` — tune tool access per platform
- `nastech skills` — browse and install reusable workflows
- Cron — only after your bot or CLI setup is stable

### Sandboxed terminal

For safety, run the agent in a Docker container or on a remote server:

```bash
nastech config set terminal.backend docker    # Docker isolation
nastech config set terminal.backend ssh       # Remote server
```

For Docker sandboxes, you can also enable the **egress credential-injection proxy** so the sandbox never sees your real API keys — only opaque proxy tokens that work exclusively from behind a local TLS-intercepting daemon. See [Egress proxy](../user-guide/egress/iron-proxy.md). Setup is `nastech egress setup && nastech egress start`; `nastech setup terminal` also points Docker users at it. Modal, SSH, Daytona, and Singularity are not wired yet.

### Voice mode

```bash
# From the Nastech install directory (the curl installer placed it at
# ~/.nastech/nastech-agent on Linux/macOS or %LOCALAPPDATA%\nastech\nastech-agent on Windows):
cd ~/.nastech/nastech-agent
uv pip install --python ./venv/bin/python -e ".[voice]"
# Includes faster-whisper for free local speech-to-text
```

Then in the CLI: `/voice on`. Press `Ctrl+B` to record. See [Voice Mode](../user-guide/features/voice-mode.md).

### Skills

Skills are on-demand instruction documents that teach Nastech how to do a specific task — deploy to Kubernetes, open a GitHub PR, fine-tune a model, search for GIFs. Each is a `SKILL.md` file with a name, a description, and a step-by-step procedure. The agent reads the short descriptions for free and only loads a skill's full content when a task actually calls for it, so adding skills doesn't bloat every request.

Nastech ships with a catalog of bundled skills already installed in `~/.nastech/skills/`. You can add more from the Skills Hub, or write your own.

**Browse and install from the hub:**

```bash
nastech skills browse                      # list everything available
nastech skills search kubernetes           # find skills by keyword
nastech skills install openai/skills/k8s   # install one (runs a security scan first)
```

The install argument is a `source/path` slug from the hub — `openai/skills/k8s` means the `k8s` skill from OpenAI's catalog. `nastech skills browse` shows the exact slugs to use.

**Use a skill** — every installed skill becomes a slash command automatically:

```bash
/k8s deploy the staging manifest          # run the skill with a request
/k8s                                       # load it and let Nastech ask what you need
```

This works in the CLI and in any connected messaging platform. You don't have to install everything up front — the agent picks the right bundled skill on its own during normal conversation when a task matches one.

See [Skills System](../user-guide/features/skills.md) for writing your own, external skill directories, and the full hub source list.

### MCP servers

```yaml
# Add to ~/.nastech/config.yaml
mcp_servers:
  github:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_xxx"
```

### Editor integration (ACP)

ACP support ships with the standard `[all]` extras, so the curl installer already includes it. Just run:

```bash
nastech acp
```

(If you installed without `[all]`, run `cd ~/.nastech/nastech-agent && uv pip install -e ".[acp]"` first.)

See [ACP Editor Integration](../user-guide/features/acp.md).

---

## Common Failure Modes

These are the problems that waste the most time:

| Symptom | Likely cause | Fix |
|---|---|---|
| Nastech opens but gives empty or broken replies | Provider auth or model selection is wrong | Run `nastech model` again and confirm provider, model, and auth |
| Custom endpoint "works" but returns garbage | Wrong base URL, model name, or not actually OpenAI-compatible | Verify the endpoint in a separate client first |
| Gateway starts but nobody can message it | Bot token, allowlist, or platform setup is incomplete | Re-run `nastech gateway setup` and check `nastech gateway status` |
| `nastech --continue` can't find old session | Switched profiles or session never saved | Check `nastech sessions list` and confirm you're in the right profile |
| Model unavailable or odd fallback behavior | Provider routing or fallback settings are too aggressive | Keep routing off until the base provider is stable |
| `nastech doctor` flags config problems | Config values are missing or stale | Fix the config, retest a plain chat before adding features |

## Recovery Toolkit

When something feels off, use this order:

1. `nastech doctor`
2. `nastech model`
3. `nastech setup`
4. `nastech sessions list`
5. `nastech --continue`
6. `nastech gateway status`

That sequence gets you from "broken vibes" back to a known state fast.

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `nastech` | Start chatting |
| `nastech model` | Choose your LLM provider and model |
| `nastech tools` | Configure which tools are enabled per platform |
| `nastech setup` | Full setup wizard (configures everything at once) |
| `nastech doctor` | Diagnose issues |
| `nastech update` | Update to latest version |
| `nastech gateway` | Start the messaging gateway |
| `nastech --continue` | Resume last session |

## Next Steps

- **[CLI Guide](../user-guide/cli.md)** — Master the terminal interface
- **[Configuration](../user-guide/configuration.md)** — Customize your setup
- **[Messaging Gateway](../user-guide/messaging/index.md)** — Connect Telegram, Discord, Slack, WhatsApp, Signal, Email, Home Assistant, Teams, and more
- **[Tools & Toolsets](../user-guide/features/tools.md)** — Explore available capabilities
- **[AI Providers](../integrations/providers.md)** — Full provider list and setup details
- **[Skills System](../user-guide/features/skills.md)** — Reusable workflows and knowledge
- **[Tips & Best Practices](../guides/tips.md)** — Power user tips
- **[Moving to another machine](/reference/faq#exporting-nastech-to-another-machine)** — `nastech backup` migrates your whole setup (or [a single profile](/reference/faq#moving-a-single-profile-to-another-machine)); no need to rebuild from scratch
