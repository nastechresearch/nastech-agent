import { beforeEach, describe, expect, it } from 'vitest'

import type { StaleAuxAssignment } from '@/nastech'

import { dismissStaleAux, readStaleAuxDismissal, staleAuxFingerprint } from './stale-aux-dismissal'

const slots = (entries: Array<[string, string, string, string?]>): StaleAuxAssignment[] =>
  entries.map(([task, provider, model, base_url]) => ({ base_url, task, provider, model }))

describe('staleAuxFingerprint', () => {
  it('binds the acknowledgement to the main provider and the pinned slots', () => {
    const a = staleAuxFingerprint('nastech', slots([['vision', 'alibaba', 'qwen3.6-flash']]))
    const same = staleAuxFingerprint('nastech', slots([['vision', 'alibaba', 'qwen3.6-flash']]))

    expect(a).toBe(same)
    expect(a).not.toBe(staleAuxFingerprint('openrouter', slots([['vision', 'alibaba', 'qwen3.6-flash']])))
    expect(a).not.toBe(staleAuxFingerprint('nastech', slots([['vision', 'alibaba', 'qwen3.6-flash-v2']])))
    expect(a).not.toBe(staleAuxFingerprint('nastech', slots([['triage_specifier', 'alibaba', 'qwen3.6-flash']])))
  })

  it('is order-insensitive across slots', () => {
    const first = staleAuxFingerprint('nastech', [
      { task: 'vision', provider: 'alibaba', model: 'm1' },
      { task: 'curator', provider: 'kimi', model: 'm2' }
    ])

    const second = staleAuxFingerprint('nastech', [
      { task: 'curator', provider: 'kimi', model: 'm2' },
      { task: 'vision', provider: 'alibaba', model: 'm1' }
    ])

    expect(first).toBe(second)
  })

  it('includes the slot endpoint, so a repointed base_url re-arms the banner', () => {
    const pinned = staleAuxFingerprint(
      'nastech',
      slots([['vision', 'openai', 'gpt-4o-mini', 'https://api.example.com/v1']])
    )

    // Same task/provider/model on a different endpoint: different billing
    // surface, so a stored acknowledgement must not cover it.
    expect(pinned).not.toBe(
      staleAuxFingerprint('nastech', slots([['vision', 'openai', 'gpt-4o-mini', 'https://proxy.example.com/v1']]))
    )
    // Trailing slashes are the same endpoint, not a re-arm.
    expect(pinned).toBe(
      staleAuxFingerprint('nastech', slots([['vision', 'openai', 'gpt-4o-mini', 'https://api.example.com/v1/']]))
    )
    // Absent and empty endpoints agree (switch echoes carry no base_url).
    expect(staleAuxFingerprint('nastech', slots([['vision', 'openai', 'gpt-4o-mini']]))).toBe(
      staleAuxFingerprint('nastech', slots([['vision', 'openai', 'gpt-4o-mini', '']]))
    )
  })

  it('normalizes the main provider casing and surrounding whitespace', () => {
    expect(staleAuxFingerprint('  Nastech ', slots([]))).toBe(staleAuxFingerprint('nastech', slots([])))
  })
})

describe('stale-aux dismissal persistence', () => {
  beforeEach(() => {
    window.localStorage.clear()
  })

  it('persists per profile and re-arms when the pin configuration changes', () => {
    dismissStaleAux('research', 'nastech', slots([['vision', 'alibaba', 'qwen3.6-flash']]))

    expect(readStaleAuxDismissal('research')).toBe(
      staleAuxFingerprint('nastech', slots([['vision', 'alibaba', 'qwen3.6-flash']]))
    )
    // A different profile never sees the acknowledgement.
    expect(readStaleAuxDismissal('default')).toBeNull()
    // A different pin configuration is not the acknowledged one.
    expect(readStaleAuxDismissal('research')).not.toBe(
      staleAuxFingerprint('nastech', slots([['vision', 'alibaba', 'qwen3.6-flash-2']]))
    )
  })
})
