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

function html(body, status = 200) {
  return new Response(body, {
    status,
    headers: {
      "content-type": "text/html; charset=utf-8",
      "cache-control": "no-store",
    },
  });
}

const LANDING = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${BRAND.name}</title>
<style>
  :root { color-scheme: dark; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    min-height: 100vh;
    background: radial-gradient(1200px 600px at 70% -10%, #1e1b2e 0%, #0b0b0f 55%);
    color: #e5e7eb;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    padding: 2rem; text-align: center;
  }
  .logo {
    font-size: 3.2rem; font-weight: 800; letter-spacing: -0.02em;
    background: linear-gradient(90deg, ${BRAND.color}, ${BRAND.color2});
    -webkit-background-clip: text; background-clip: text; color: transparent;
  }
  .tagline { max-width: 34rem; margin: 1.2rem auto 0; font-size: 1.05rem; color: #9ca3af; line-height: 1.6; }
  .badge {
    display: inline-block; margin-top: 1.4rem; padding: 0.35rem 0.9rem;
    border: 1px solid #374151; border-radius: 999px; font-size: 0.78rem;
    color: #d1d5db; background: rgba(17,17,24,0.6);
  }
  .routes { margin-top: 2.4rem; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.8rem; color: #6b7280; }
  .routes div { padding: 0.25rem 0; }
  footer { position: absolute; bottom: 1.2rem; font-size: 0.72rem; color: #4b5563; }
  a { color: ${BRAND.color}; text-decoration: none; }
</style>
</head>
<body>
  <div class="logo">${BRAND.name}</div>
  <p class="tagline">${BRAND.tagline}</p>
  <span class="badge">update-channel assets host &bullet; workers.dev &bullet; KV-backed</span>
  <div class="routes">
    <div>GET /releases/channels/main.json</div>
    <div>GET /releases/channels/stable.json</div>
    <div>GET /releases/stable/release-candidates.json</div>
    <div>GET /health</div>
  </div>
  <footer>Deployed via Cloudflare Workers &bullet; <a href="/health">health</a></footer>
</body>
</html>`;

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Landing site
    if (path === "/" || path === "/index.html") {
      return html(LANDING);
    }

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