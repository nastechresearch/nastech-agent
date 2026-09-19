import { useQuery } from '@tanstack/react-query'

import { getNastechConfigRecord, type ProfileScope, profileScopeKey } from '@/nastech'
import { queryClient, writeCache } from '@/lib/query-client'
import type { NastechConfigRecord } from '@/types/nastech'

// One shared cache for the whole profile config record (`GET /api/config`).
// Every settings surface (MCP, model, config) reads and writes through this key
// so a save in one shows in the others, and revisiting a tab paints the cache
// instead of blanking on a fresh fetch.
//
// Distinct from session/hooks/use-nastech-config.ts, which is side-effecting —
// it pushes personality/cwd/voice/… into the session stores for live chat.
export const NASTECH_CONFIG_KEY = ['nastech-config-record'] as const

// Per-scope cache key. The base key (no suffix) is the app-wide active
// profile, unchanged for every caller that passes nothing. An explicit scope —
// the Capabilities scope selector configuring ANOTHER profile, possibly on
// another registered gateway — gets its own suffixed key so switching the
// selector refetches and never paints stale cross-profile config (the
// AGENTS.md scope-in-key rule). profileScopeKey folds a remote pin's
// connection id into the suffix, so two gateways' same-named profiles never
// share a cache row.
export const nastechConfigKey = (profile?: ProfileScope) =>
  profile == null ? NASTECH_CONFIG_KEY : ([...NASTECH_CONFIG_KEY, profileScopeKey(profile)] as const)

// staleTime 0 → serve cache instantly, background-revalidate on every mount.
// `profile` scopes both the query key and the fetch; omitting it preserves the
// exact app-wide behavior (base key, `profileScoped(undefined)` fallback).
export const useNastechConfigRecord = (profile?: ProfileScope) =>
  useQuery({
    queryKey: nastechConfigKey(profile),
    // null/undefined both mean "no override" → fetch with undefined so
    // capabilityScoped falls back to the app-wide active profile (passing null
    // would wrongly target the primary backend).
    queryFn: () => getNastechConfigRecord(profile ?? undefined),
    staleTime: 0
  })

// setNastechConfigCache writes the app-wide (base-key) record. Pass a profile to
// write the suffixed per-profile cache instead — keeps the selector's optimistic
// write-through landing on the same key its query reads.
export const setNastechConfigCache = writeCache<NastechConfigRecord>(NASTECH_CONFIG_KEY)
export const nastechConfigCacheWriter = (profile?: ProfileScope) =>
  writeCache<NastechConfigRecord>(nastechConfigKey(profile))

export const invalidateNastechConfig = (profile?: ProfileScope) =>
  queryClient.invalidateQueries({ queryKey: nastechConfigKey(profile) })
