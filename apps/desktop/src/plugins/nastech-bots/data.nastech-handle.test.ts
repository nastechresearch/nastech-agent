/**
 * @nastech belongs to the default bot only while its source has no real
 * (pre-reservation) `nastech` profile. With one, the roster shows exactly one
 * @nastech — the real profile — and the default answers to @default, so a
 * typed @nastech reaches the same profile the backend's message_agent does.
 */

import { describe, expect, it, vi } from 'vitest'

import { botHandle, botMentionTag, claimDefaultHandles, mergeMultiSourceRoster, resolveRosterMentions } from './data'
import { previewKind } from './row-helpers'
import type { RosterRow } from './types'

vi.mock('@nastech/plugin-sdk', async () => {
  const { atom } = await import('nanostores')

  return { atom, host: {}, queryClient: undefined, useQuery: vi.fn(), useValue: vi.fn() }
})

vi.mock('./shared', () => ({ getPluginCtx: () => null, ID: 'nastech-bots' }))

function roster(names: string[]): RosterRow[] {
  const local = { profiles: names.map(name => ({ name })) }

  // What Electron's buildAgentRoster reports for a single local source: bare-name handles.
  const union = {
    agents: names.map(profile => ({
      connectionId: 'local',
      connectionKind: 'local' as const,
      connectionLabel: 'This device',
      handle: profile,
      profile,
      targetProfile: profile
    })),
    primaryConnectionId: 'local'
  }

  return mergeMultiSourceRoster(local, union, 'local').profiles as RosterRow[]
}

describe('the @nastech handle', () => {
  it.each([
    [['default', 'researcher'], 'default'],
    [['default', 'nastech', 'researcher'], 'nastech']
  ])('roster %j shows one @nastech and a typed @nastech reaches %s', (names, owner) => {
    const rows = roster(names)
    const handles = rows.map(row => botHandle(row.name, row))

    expect(handles.filter(handle => handle === 'nastech')).toHaveLength(1)
    expect(rows.map(row => botMentionTag(row)).filter(tag => tag === 'nastech')).toHaveLength(1)
    expect(resolveRosterMentions('@nastech ping', rows, { name: 'researcher' }).map(row => row.name)).toEqual([owner])
  })

  it('names the default @default once a real nastech profile holds the handle', () => {
    const rows = roster(['default', 'nastech', 'researcher'])
    const byName = Object.fromEntries(rows.map(row => [row.name, botHandle(row.name, row)]))

    expect(byName).toEqual({ default: 'default', nastech: 'nastech', researcher: 'researcher' })
    expect(resolveRosterMentions('@default ping', rows, { name: 'researcher' }).map(row => row.name)).toEqual(['default'])
  })

  it('keeps each source separate: a remote nastech profile does not rename the local default', () => {
    const rows = claimDefaultHandles<Partial<RosterRow>>([
      { connectionId: 'local', name: 'default' },
      { connectionId: 'mini', name: 'default' },
      { connectionId: 'mini', name: 'nastech' }
    ])

    expect(rows.map(row => botHandle(String(row.name), row))).toEqual(['nastech', 'default', 'nastech'])
  })

  it("never lets a source's stale 'nastech' handle on its default answer @nastech", () => {
    // An older backend labels its default @nastech even beside a real nastech profile.
    const rows = claimDefaultHandles<RosterRow>([
      { connectionId: 'mini', handle: 'nastech', name: 'default', remoteSource: true },
      { connectionId: 'mini', handle: 'nastech', name: 'nastech', remoteSource: true },
      { connectionId: 'local', name: 'researcher' }
    ])

    expect(resolveRosterMentions('@nastech ping', rows, { name: 'researcher' }).map(row => row.name)).toEqual(['nastech'])
  })

  it('names a DM sender in a row preview by its roster handle', () => {
    const rows = claimDefaultHandles<RosterRow>(
      ['default', 'nastech', 'researcher'].map(name => ({ connectionId: 'local', name }))
    )

    const sender = (name: string, list: RosterRow[]) =>
      previewKind(`Message from 🤖 ${name} (@x): hi`, list, 'local').fromBot

    expect([sender('default', rows), sender('nastech', rows)]).toEqual(['default', 'nastech'])
    // No real nastech profile: the default is still @nastech (#89484).
    expect(sender('default', claimDefaultHandles<RosterRow>([{ connectionId: 'local', name: 'default' }]))).toBe(
      'nastech'
    )
  })
})
