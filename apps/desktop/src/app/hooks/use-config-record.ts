import { useQuery } from '@tanstack/react-query'

import { getNastechConfigRecord } from '@/nastech'
import { queryClient, writeCache } from '@/lib/query-client'
import { normalizeProfileKey } from '@/store/profile'
import type { NastechConfigRecord } from '@/types/nastech'

// One shared cache for the whole profile config record (`GET /api/config`).
// Every settings surface (MCP, model, config) reads and writes through this key
// so a save in one shows in the others, and revisiting a tab paints the cache
// instead of blanking on a fresh fetch.
//
// Distinct from session/hooks/use-nastech-config.ts, which is side-effecting —
// it pushes personality/cwd/voice/… into the session stores for live chat.
export const NASTECH_CONFIG_KEY = ['nastech-config-record'] as const

// Per-profile cache key. The base key (no profile suffix) is the app-wide
// active profile, unchanged for every caller that passes nothing. An explicit
// profile — the Capabilities profile-scope selector configuring ANOTHER
// profile — gets its own suffixed key so switching the selector refetches and
// never paints stale cross-profile config (the AGENTS.md scope-in-key rule).
export const nastechConfigKey = (profile?: null | string) =>
  profile == null ? NASTECH_CONFIG_KEY : ([...NASTECH_CONFIG_KEY, normalizeProfileKey(profile)] as const)

// staleTime 0 → serve cache instantly, background-revalidate on every mount.
// `profile` scopes both the query key and the fetch; omitting it preserves the
// exact app-wide behavior (base key, `profileScoped(undefined)` fallback).
export const useNastechConfigRecord = (profile?: null | string) =>
  useQuery({
    queryKey: nastechConfigKey(profile),
    // null/undefined both mean "no override" → fetch with undefined so
    // profileScoped falls back to the app-wide active profile (passing null
    // would wrongly target the primary backend).
    queryFn: () => getNastechConfigRecord(profile ?? undefined),
    staleTime: 0
  })

// setNastechConfigCache writes the app-wide (base-key) record. Pass a profile to
// write the suffixed per-profile cache instead — keeps the selector's optimistic
// write-through landing on the same key its query reads.
export const setNastechConfigCache = writeCache<NastechConfigRecord>(NASTECH_CONFIG_KEY)
export const nastechConfigCacheWriter = (profile?: null | string) =>
  writeCache<NastechConfigRecord>(nastechConfigKey(profile))

export const invalidateNastechConfig = (profile?: null | string) =>
  queryClient.invalidateQueries({ queryKey: nastechConfigKey(profile) })
