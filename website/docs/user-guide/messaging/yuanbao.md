---
sidebar_position: 16
title: "Yuanbao"
description: "Yuanbao moved out of Nastech core into the yuanbao Nastech Labs plugin"
---

# Yuanbao

:::warning Nastech Labs plugin
Yuanbao is now a Nastech Labs plugin: built by Nastech Research, not supported, and likely not maintained going forward. Fixes from the community are welcome.
:::

The [Yuanbao](https://yuanbao.tencent.com/) gateway platform and its `yb_*` tools (`yb_query_group_info`, `yb_query_group_members`, `yb_send_dm`, `yb_search_sticker`, `yb_send_sticker`) are no longer part of Nastech core. They ship as the `yuanbao` plugin in [NastechResearch/nastech-labs-plugins](https://github.com/NastechResearch/nastech-labs-plugins/tree/main/yuanbao), which carries the full setup guide.

## Install

```bash
nastech plugins install yuanbao
```

Plugins are installed per profile; use `nastech -p <profile> plugins install yuanbao` for another profile. Restart the gateway afterwards so it serves the platform.

Every name stays the same: the `YUANBAO_*` environment variables (`YUANBAO_APP_ID` or the legacy `YUANBAO_APP_KEY`, `YUANBAO_APP_SECRET`, `YUANBAO_HOME_CHANNEL`, ...), the `platforms.yuanbao` block (and the legacy `gateway.yuanbao` block) in `config.yaml`, the `yuanbao` toolset and the tool names.

:::info Upgrading from a release that bundled Yuanbao
Nothing to do. Every profile that was already using Yuanbao (`YUANBAO_APP_ID` or `YUANBAO_APP_KEY` plus `YUANBAO_APP_SECRET` in its `.env`, `platforms.yuanbao` enabled in `config.yaml`, or the `yuanbao` / `nastech-yuanbao` toolset listed for another platform) gets the plugin installed automatically from the catalog by `nastech update`, or the first time the profile starts (agent or gateway start; this honours `security.allow_lazy_installs`). A failed attempt is retried with a backoff; `nastech update` always retries. This happens once per profile: if you later remove the plugin (`nastech plugins remove yuanbao`), it stays removed.
:::
