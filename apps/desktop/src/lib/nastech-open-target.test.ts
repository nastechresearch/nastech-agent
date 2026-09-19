import { describe, expect, it } from 'vitest'

import {
  normalizeNastechOpenString,
  pathFromNastechDeepLink,
  pathFromOpenDeepLink,
  resolveNastechOpenPath
} from './nastech-open-target'

describe('normalizeNastechOpenString', () => {
  it('accepts hash-router paths and strips a leading hash', () => {
    expect(normalizeNastechOpenString('/index-network/intent/1')).toBe('/index-network/intent/1')
    expect(normalizeNastechOpenString('#/index-network/intent/1')).toBe('/index-network/intent/1')
  })

  it('maps plugin-scoped nastech:// deep links to the same path', () => {
    expect(normalizeNastechOpenString('nastech://index-network/intent/1')).toBe('/index-network/intent/1')
    expect(normalizeNastechOpenString('nastech://index-network/intent/1?focus=true')).toBe(
      '/index-network/intent/1?focus=true'
    )
  })

  it('maps nastech://open/… deep links by stripping the open host', () => {
    expect(normalizeNastechOpenString('nastech://open/index-network/intent/1')).toBe('/index-network/intent/1')
    expect(normalizeNastechOpenString('nastech://open/settings/plugins')).toBe('/settings/plugins')
  })

  it('rejects reserved nastech kinds and unsafe paths', () => {
    expect(normalizeNastechOpenString('nastech://blueprint/morning-brief')).toBeNull()
    expect(normalizeNastechOpenString('nastech://plugin/install')).toBeNull()
    expect(normalizeNastechOpenString('https://example.com/x')).toBeNull()
    expect(normalizeNastechOpenString('/../etc/passwd')).toBeNull()
    expect(normalizeNastechOpenString('index-network')).toBeNull()
  })
})

describe('resolveNastechOpenPath', () => {
  it('merges structured path + params', () => {
    expect(resolveNastechOpenPath({ path: '/index-network/intent/1', params: { focus: 'true' } })).toBe(
      '/index-network/intent/1?focus=true'
    )
  })

  it('resolves href the same as a bare string', () => {
    expect(resolveNastechOpenPath({ href: 'nastech://index-network/intent/1' })).toBe('/index-network/intent/1')
  })
})

describe('pathFromNastechDeepLink', () => {
  it('builds the navigate path from a plugin-scoped deep-link payload', () => {
    expect(pathFromNastechDeepLink('index-network', 'intent/1')).toBe('/index-network/intent/1')
  })

  it('builds the navigate path from nastech://open/… payloads', () => {
    expect(pathFromOpenDeepLink('index-network/intent/1')).toBe('/index-network/intent/1')
    expect(pathFromNastechDeepLink('open', 'agent/42')).toBe('/agent/42')
  })

  it('ignores reserved kinds', () => {
    expect(pathFromNastechDeepLink('blueprint', 'morning-brief')).toBeNull()
    expect(pathFromNastechDeepLink('plugin', 'install')).toBeNull()
  })
})
