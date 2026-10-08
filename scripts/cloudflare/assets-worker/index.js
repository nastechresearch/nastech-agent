/**
 * nastech-agent — Nastech Agent update-channel assets host + landing site.
 *
 * Serves:
 *   1. A branded landing page at `/` (the "website").
 *   2. The release-channel protocol records that `nastech_cli/source_releases.py`
 *      and `nastech_cli/release_channels.py` read from `_PUBLIC_BASE`.
 *
 * Publication mirrors the upstream reference layout: channel records +
 * manifests + candidate feeds are written to Cloudflare object storage
 * (Workers KV in this deployment; R2 in the upstream reference) at the
 * canonical keys:
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
  name: 'Nastech Agent',
  tagline: 'Open-source autonomous AI agent — one core across CLI, messaging, TUI, and desktop.',
  color: '#f59e0b',
  color2: '#7c3aed'
}

const JSON_HEADERS = {
  'content-type': 'application/json; charset=utf-8',
  'cache-control': 'no-cache',
  'access-control-allow-origin': '*'
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body, null, 2), {
    status,
    headers: JSON_HEADERS
  })
}

function html(body, status = 200) {
  return new Response(body, {
    status,
    headers: {
      'content-type': 'text/html; charset=utf-8',
      'cache-control': 'no-store'
    }
  })
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
</html>`

// ---- Bucket front (R2) ----------------------------------------------------

function contentTypeFor(key, stored) {
  if (stored) return stored
  if (key.endsWith('.json')) return 'application/json; charset=utf-8'
  if (key.endsWith('.html')) return 'text/html; charset=utf-8'
  if (key.endsWith('.txt') || key.endsWith('.asc')) return 'text/plain; charset=utf-8'
  return 'application/octet-stream'
}

function r2Headers(key, obj) {
  const meta = obj.httpMetadata || {}
  const headers = {
    'content-type': contentTypeFor(key, meta.contentType),
    'cache-control': meta.cacheControl || 'no-cache',
    etag: obj.httpEtag || obj.etag,
    'accept-ranges': 'bytes',
    'access-control-allow-origin': '*'
  }
  if (meta.contentEncoding) headers['content-encoding'] = meta.contentEncoding
  if (meta.contentDisposition) headers['content-disposition'] = meta.contentDisposition
  return headers
}

// Serve an object straight from the R2 bucket: real 200/206/304 responses,
// stored metadata, byte ranges, never a redirect (protocol contract above).
// Returns null when the key is absent or unbound so callers can fall through.
async function serveFromBucket(env, key, request) {
  if (!env.R2 || !key) return null
  // Pass the request's own conditional/range headers to R2 (the documented
  // pattern): R2 evaluates If-None-Match / If-Modified-Since / Range and
  // returns metadata only when the condition fails.
  const options = {}
  const conditional = request.headers.get('if-none-match') || request.headers.get('if-modified-since')
  if (conditional) options.onlyIf = request.headers
  const rangeHeader = request.headers.get('range')
  if (rangeHeader) options.range = request.headers
  let obj
  try {
    obj = await env.R2.get(key, options)
  } catch (err) {
    // A conditional or range the bucket rejects must never surface as 5xx:
    // fall back to one unconditional full read (200).
    try {
      obj = await env.R2.get(key)
    } catch (err2) {
      return null
    }
    if (obj === null) return null
    const headers = r2Headers(key, obj)
    headers['content-length'] = String(obj.size)
    const body = request.method === 'HEAD' ? null : obj.body
    return new Response(body, { headers })
  }
  if (obj === null) return null
  if (obj.body === undefined || obj.body === null) {
    // The conditional failed (if-none-match hit): metadata only -> 304.
    const headers = r2Headers(key, obj)
    delete headers['content-type']
    return new Response(null, { status: 304, headers })
  }
  const headers = r2Headers(key, obj)
  let status = 200
  // R2 reports a range even on full reads, so only a range the client
  // actually asked for may downgrade the response to 206.
  if (rangeHeader && obj.range && obj.range.offset !== undefined) {
    const length = obj.range.length !== undefined ? obj.range.length : obj.size - obj.range.offset
    headers['content-range'] = `bytes ${obj.range.offset}-${obj.range.offset + length - 1}/${obj.size}`
    headers['content-length'] = String(length)
    status = 206
  } else if (rangeHeader && obj.range && obj.range.suffix !== undefined) {
    headers['content-range'] = `bytes ${obj.size - obj.range.suffix}-${obj.size - 1}/${obj.size}`
    headers['content-length'] = String(obj.range.suffix)
    status = 206
  } else {
    headers['content-length'] = String(obj.size)
  }
  const body = request.method === 'HEAD' ? null : obj.body
  return new Response(body, { status, headers })
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url)
    const path = url.pathname

    // Canonical root: no object lives at the bare host root, so / answers a
    // protocol-correct 404 instead of demo HTML (the reader and the egress
    // probes treat any 200 as content).
    if (path === '/' || path === '/index.html') {
      return json({ error: 'NotFound', path }, 404)
    }

    // Health
    if (path === '/health') {
      return json({ ok: true, service: 'nastech-agent', time: new Date().toISOString() })
    }

    const key = path.replace(/^\/+/, '')

    // R2 bucket first: every published object (channel records, artifacts,
    // pins, the termux repo) lives in the bucket and serves with real
    // 200/206/304 responses, never a redirect.
    const fromBucket = await serveFromBucket(env, key, request)
    if (fromBucket) return fromBucket

    // Publication keys fall back to the KV store (seeded channel records).
    // Unknown objects answer a protocol-correct 404, never a redirect.
    if (path.startsWith('/releases/')) {
      const value = await env.NASTECH_ASSETS.get(key, 'text')
      if (value !== null) {
        const isArchive = key.endsWith('/') || key.startsWith('releases/tag/')
        return new Response(value, {
          headers: {
            'content-type': isArchive ? 'application/octet-stream' : 'application/json; charset=utf-8',
            'cache-control': 'no-cache',
            'access-control-allow-origin': '*'
          }
        })
      }
      // Channel records missing -> ChannelNotFound (branch fallback for main).
      const channelMatch = key.match(/^releases\/channels\/([A-Za-z0-9_.-]+)\.json$/)
      if (channelMatch) {
        return json({ error: 'ChannelNotFound', channel: channelMatch[1] }, 404)
      }
      return json({ error: 'NotFound', path }, 404)
    }

    return json({ error: 'NotFound', path }, 404)
  }
}
