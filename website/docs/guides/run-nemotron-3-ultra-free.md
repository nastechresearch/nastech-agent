---
sidebar_position: 0
title: "Run Nemotron 3 Ultra free in Nastech Agent"
description: "Try NVIDIA Nemotron 3 Ultra on Nastech Portal — free June 4–18 — with day 0 support in Nastech Agent"
---

# Run Nemotron 3 Ultra free in Nastech Agent

Nastech Research has been inducted into the **Nemotron Coalition** of leading AI labs working with **NVIDIA** to advance open frontier foundation models. In honor of this, we've partnered with **Nebius** to provide **Nemotron 3 Ultra** free on [Nastech Portal](https://portal.nastechresearch.github.io) for two weeks (**June 4th – June 18th**). Follow the instructions below to try the model in your Nastech Agent today.

:::info Limited-time offer
The `nvidia/nemotron-3-ultra:free` tier is available from **June 4th to June 18th**. The `:free` tag is what keeps it on the no-cost plan — pick that exact variant.
:::

Pick whichever install fits you. The **desktop app** is the easiest — no terminal required. If you live in a terminal, the **command-line** install is right below it.

## Option A — Desktop app (recommended)

The simplest path: a one-click installer with a guided, point-and-click setup. No terminal needed.

### 1. Download and install

[Download the Nastech Desktop installer](https://nastechresearch.github.io/nastech-agent/) for macOS or Windows, then open it. On first launch it finishes setting itself up (usually under a minute).

### 2. Connect Nastech Portal

When the app opens, you'll see a "Let's get you set up" screen. Click **Nastech Portal** (marked **Recommended**). Your browser opens — create a [Nastech Portal](https://portal.nastechresearch.github.io) account (or sign in), choose the **Free** plan, and authorize Nastech. The app connects automatically.

### 3. Pick the free Nemotron 3 Ultra model

After connecting, the app shows a **Default model** card. Click **Change**, search for **nemotron 3 ultra**, and select the variant tagged **Free tier**:

```
nvidia/nemotron-3-ultra:free
```

The `:free` tag is what keeps it on the no-cost tier — pick that variant.

### 4. Start chatting

Click **Start chatting**. That's it — you're talking to Nemotron 3 Ultra, free.

## Option B — Command line

Prefer the terminal?

### 1. Install Nastech Agent

On macOS/Linux/WSL2/Android, run

```bash
curl -fsSL https://nastechresearch.github.io/nastech-agent/install.sh | bash
```

On Windows, run

```powershell
iex (irm https://nastechresearch.github.io/nastech-agent/install.ps1)
```

Prefer to review first? Download [`install.sh`](https://nastechresearch.github.io/nastech-agent/install.sh), inspect it, then run it.

After it finishes, reload your shell:

```bash
source ~/.bashrc   # or source ~/.zshrc
```

### 2. Run Quick Setup

```bash
nastech setup
```

Select **Quick Setup**. Nastech opens a browser tab and waits for you to finish the next steps.

### 3. Create a Nastech Portal account

In the browser, create a [Nastech Portal](https://portal.nastechresearch.github.io) account (or sign in) and choose the **Free** plan.

### 4. Connect your account

When prompted to connect your account to Nastech Agent, click **Connect**. You'll see a confirmation once it's linked.

### 5. Select the free Nemotron 3 Ultra model

Return to your terminal. From the model list, select:

```
nvidia/nemotron-3-ultra:free
```

The `:free` tag is what keeps it on the no-cost tier, so make sure you pick that variant.

### 6. Start chatting

Complete the remaining Quick Setup prompts, then run:

```bash
nastech
```

That's it — you're talking to Nemotron 3 Ultra, free.

## Switching to it later

Already set up with another model?

- **Desktop app:** open the model picker, search for **nemotron 3 ultra**, and select the **Free tier** variant.
- **CLI / TUI:** switch any time from inside a session with `/model nvidia/nemotron-3-ultra:free`, or run `/model` to open the picker and choose it from the list.

## Troubleshooting

- **Don't see the model in the list?** Make sure you finished the Nastech Portal connection and that you're on the **Free** plan. In the CLI, `nastech portal info` confirms you're logged in and routing through Nastech.
- **Picked the wrong variant?** Re-select `nvidia/nemotron-3-ultra:free` — the `:free` suffix is required to stay on the no-cost tier.
- **Browser didn't open / you're on a remote host (CLI)?** See [OAuth over SSH / Remote Hosts](/guides/oauth-over-ssh) for port-forwarding workarounds.

## See also

- **[Desktop App](/user-guide/desktop)** — The native one-click app (macOS, Windows, Linux)
- **[Run Nastech Agent with Nastech Portal](/guides/run-nastech-with-nastech-portal)** — Full Portal walkthrough: models, Tool Gateway, and verification
- **[Nastech Portal integration](/integrations/nastech-portal)** — What's in the subscription
- **[Quickstart](/getting-started/quickstart)** — Install-to-chat in under 5 minutes
