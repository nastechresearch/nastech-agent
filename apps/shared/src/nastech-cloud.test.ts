import { describe, expect, it } from 'vitest'

import { isNastechCloudUrl } from './nastech-cloud'

describe('isNastechCloudUrl', () => {
  it('recognises production and staging agent hosts, nothing else', () => {
    expect(isNastechCloudUrl('https://ares-3009.agents.nastechresearch.github.io')).toBe(true)
    expect(isNastechCloudUrl('https://ares--app.agents.staging-nastechresearch.github.io/')).toBe(true)
    expect(isNastechCloudUrl('https://agents.nastechresearch.github.io.evil.example')).toBe(false)
    expect(isNastechCloudUrl('https://my-box.tailnet.ts.net')).toBe(false)
    expect(isNastechCloudUrl('not a url')).toBe(false)
    expect(isNastechCloudUrl(undefined)).toBe(false)
  })
})
