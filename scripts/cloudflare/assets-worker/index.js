/**
 * nastech-agent — Nastech Agent update-channel assets host + landing site.
 *
 * Serves:
 *   1. A branded landing page at `/` (the "website").
 *   2. The release-channel protocol records that `nastech_cli/source_releases.py`
 *      and `nastech_cli/release_channels.py` read from `_PUBLIC_BASE`.
 *
 * Publication mirrors Hermes: channel records + manifests + candidate feeds are
 * written to Cloudflare object storage (Workers KV in this deployment; R2 in
 * the upstream reference) at the canonical keys:
 *     releases/channels/<name>.json           channel records
 *     releases/channel-builds/<buildId>/...   manifest + artifacts
 *     releases/stable/release-candidates.json candidate feed
 *     releases/tag/<tag>/...                  archived tag bundles
 * and served here with Cache-Control: no-cache.
 *
 * Protocol contract (see nastech_cli/release_channels.py):
 *   - A channel object that does not exist MUST answer HTTP 404 (the reader maps
 *     that to ChannelNotFound and falls back to branch-following for `main`).
 *     Any other failure (5xx, redirect, transport) is a hard `release-unavailable`.
 *   - Artifact reads MUST NOT redirect (reader rejects redirects).
 */

const BRAND = {
  name: "Nastech Agent",
  tagline: "Open-source autonomous AI agent — one core across CLI, messaging, TUI, and desktop.",
  color: "#f59e0b",
  color2: "#7c3aed",
};

const JSON_HEADERS = {
  "content-type": "application/json; charset=utf-8",
  "cache-control": "no-cache",
  "access-control-allow-origin": "*",
};

function json(body, status = 200) {
  return new Response(JSON.stringify(body, null, 2), {
    status,
    headers: JSON_HEADERS,
  });
}



export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Health
    if (path === "/health") {
      return json({ ok: true, service: "nastech-agent", time: new Date().toISOString() });
    }

    // Everything under /releases/ is served from the KV store (publication
    // target). Unknown objects answer a protocol-correct 404, never a redirect.
    if (path.startsWith("/releases/")) {
      const key = path.replace(/^\/+/, "");
      const value = await env.NASTECH_ASSETS.get(key, "text");
      if (value !== null) {
        const isArchive = key.endsWith("/") || key.startsWith("releases/tag/");
        return new Response(value, {
          headers: {
            "content-type": isArchive ? "application/octet-stream" : "application/json; charset=utf-8",
            "cache-control": "no-cache",
            "access-control-allow-origin": "*",
          },
        });
      }
      // Channel records missing -> ChannelNotFound (branch fallback for main).
      const channelMatch = key.match(/^releases\/channels\/([A-Za-z0-9_.-]+)\.json$/);
      if (channelMatch) {
        return json({ error: "ChannelNotFound", channel: channelMatch[1] }, 404);
      }
      return json({ error: "NotFound", path }, 404);
    }

    return json({ error: "NotFound", path }, 404);
  },
};