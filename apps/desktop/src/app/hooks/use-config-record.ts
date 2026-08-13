import { useQuery } from '@tanstack/react-query'

import { getNastechConfigRecord } from '@/nastech'
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

// staleTime 0 → serve cache instantly, background-revalidate on every mount.
export const useNastechConfigRecord = () =>
  useQuery({ queryKey: NASTECH_CONFIG_KEY, queryFn: getNastechConfigRecord, staleTime: 0 })

export const setNastechConfigCache = writeCache<NastechConfigRecord>(NASTECH_CONFIG_KEY)

export const invalidateNastechConfig = () => queryClient.invalidateQueries({ queryKey: NASTECH_CONFIG_KEY })
