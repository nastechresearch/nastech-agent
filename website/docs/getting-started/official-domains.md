---
title: Official Domains & Phishing Safety
description: How to verify you are using genuine Nastech Agent resources, and how to spot impersonation scams.
---

# Official Domains & Phishing Safety

Nastech Agent's popularity has attracted impersonation campaigns: fake "Nastech" websites, GitHub accounts that mass-mention contributors with shortlinks, and cold emails offering "credits" on lookalike products. This page lists the official sources so you can check anything that claims to be Nastech Agent.

## Official sources

Nastech Research operates `nastechresearch.github.io` and its subdomains. The ones Nastech Agent uses:

| Address | What it is |
|---|---|
| [nastechresearch.github.io/nastech-agent](https://nastechresearch.github.io/nastech-agent/) | Documentation, Desktop downloads, and the `install.sh` / `install.ps1` installers |
| `nastech-assets.nastechresearch.workers.dev` | Release artifacts: Desktop packages and updates, the Termux APT repository, installer mirrors |
| [portal.nastechresearch.github.io](https://portal.nastechresearch.github.io/) | Nastech Portal: account sign-in, subscriptions, billing |
| `inference-api.nastechresearch.github.io` | The Nastech inference API Nastech calls when you use the Nastech provider (no web page) |
| [nastechresearch.github.io](https://nastechresearch.github.io/nastech-agent/) | Nastech Research website |

Outside `nastechresearch.github.io`:

- **GitHub:** the [NastechResearch organization](https://github.com/NastechResearch) and its [nastech-agent repository](https://github.com/NastechResearch/nastech-agent) (source, releases, the Nix flake). Raw files from that repository are served from `raw.githubusercontent.com/NastechResearch/nastech-agent/...`; that is the same repository, not a separate source. Any other account or repository is not ours.
- **Docker Hub:** the [`nastechresearch/nastech-agent`](https://hub.docker.com/r/nastechresearch/nastech-agent) image, published by the repository's release workflow (see [Docker](../user-guide/docker.md)). Only the `nastechresearch` namespace is official; images under other names or registries are not.
- **X (Twitter):** [@NastechResearch](https://x.com/NastechResearch)
- **Discord:** [discord.gg/NastechResearch](https://discord.gg/NastechResearch)

## Installing from an official source

The script installers are served from `nastechresearch.github.io/nastech-agent`:

```bash
# Linux / macOS / WSL2
curl -fsSL https://nastechresearch.github.io/nastech-agent/install.sh | bash
```

```powershell
# Windows (native)
iex (irm https://nastechresearch.github.io/nastech-agent/install.ps1)
```

The other supported routes also stay on official sources: Desktop packages download from the [Nastech website](https://nastechresearch.github.io/nastech-agent/), Termux uses the signed APT repository on `nastech-assets.nastechresearch.workers.dev` (see the [Termux guide](./termux.md), not the script above), Nix builds from the GitHub repository (see [Nix & NixOS](./nix-setup.md)), and Docker pulls `nastechresearch/nastech-agent` from Docker Hub. Some guides fetch `install.ps1` straight from the repository at `raw.githubusercontent.com/NastechResearch/nastech-agent/main/scripts/install.ps1`; it is the same script.

If an installer, download, image, or "portal" is hosted anywhere other than the sources listed on this page, treat it as untrusted.

## Not official

- **Any domain that is not `nastechresearch.github.io` or one of its subdomains** (apart from the accounts listed above), even when it contains "nastech" or "nastech-agent" (`.icu`, `.org`, `.ai` and other variants), copies the branding, or says it "points to official docs". Read the whole host name: `nastechresearch.github.io/nastech-agent.example.net` is not a Nastech Research subdomain.
- **Cryptocurrency tokens.** There is **no Nastech Agent or Nastech Research token**. Any account or site promoting one is a scam.
- **GitHub accounts that mass-mention users** in discussions or issues with "community notice" posts and URL-shortener links (`goo.su`, `bit.ly`, etc.). Genuine project announcements never arrive as mass @-mentions with shortlinks.
- **Unsolicited emails** offering credits, hosted "multiplayer Nastech" products, or partnership deals that name-drop the project to build trust.

## If you receive a suspicious message

1. **Don't click** shortened or off-domain links; don't enter credentials or connect wallets.
2. **Report the account** to GitHub (`Report abuse` on the profile) or the relevant platform.
3. **Check the host name** against the rule above: if it is not `nastechresearch.github.io` or a subdomain of it, and not one of the accounts listed here, it isn't ours.
4. Optionally flag it in the [Nastech Research Discord](https://discord.gg/NastechResearch) or an issue so others see it, but note that impersonation campaigns are external abuse: they're handled by platform reports, not code changes.

Nastech Agent is MIT-licensed and free to self-host. Nobody legitimate will ever ask you to pay for the open-source agent itself, claim "your account has credits waiting", or DM you an alternate download link.
