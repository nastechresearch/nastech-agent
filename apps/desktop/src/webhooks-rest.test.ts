import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import { deleteWebhook } from './nastech'

describe('Webhook REST parity helpers', () => {
  let api: ReturnType<typeof vi.fn>

  beforeEach(() => {
    api = vi.fn().mockResolvedValue({})
    Object.defineProperty(window, 'nastechDesktop', {
      configurable: true,
      value: { api }
    })
  })

  afterEach(() => {
    vi.restoreAllMocks()
    Reflect.deleteProperty(window, 'nastechDesktop')
  })

  it('encodes the name when deleting a subscription', async () => {
    await deleteWebhook('my hook')

    expect(api).toHaveBeenCalledWith(expect.objectContaining({ method: 'DELETE', path: '/api/webhooks/my%20hook' }))
  })

  it('routes an explicitly owned delete to that profile, not the ambient scope', async () => {
    await deleteWebhook('my hook', 'coder')

    expect(api).toHaveBeenCalledWith(
      expect.objectContaining({ method: 'DELETE', path: '/api/webhooks/my%20hook', profile: 'coder' })
    )
  })
})
