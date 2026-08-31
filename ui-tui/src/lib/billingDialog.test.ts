import type { BillingBlock } from '@nastech/shared/billing'
import { describe, expect, it } from 'vitest'

import { billingDialogCopy } from './billingDialog.js'

function makeBlock(overrides: Partial<BillingBlock> = {}): BillingBlock {
  return {
    billing_url: 'https://openrouter.ai/settings/credits',
    is_nastech: false,
    message: 'out of credits',
    model: 'x',
    provider: 'openrouter',
    provider_label: 'OpenRouter',
    ...overrides
  }
}

describe('billingDialogCopy', () => {
  it('routes Nastech to the /topup flow', () => {
    const copy = billingDialogCopy(
      makeBlock({ is_nastech: true, provider: 'nastech', provider_label: 'Nastech Portal' })
    )
    expect(copy.title).toContain('Nastech')
    expect(copy.confirmLabel).toBe('Top up')
    expect(copy.cancelLabel).toBe('Dismiss')
  })

  it('offers to open a third-party provider billing page', () => {
    const copy = billingDialogCopy(makeBlock())
    expect(copy.title).toContain('OpenRouter')
    expect(copy.confirmLabel).toBe('Open billing page')
  })

  it('falls back to switching providers when there is no URL', () => {
    const copy = billingDialogCopy(makeBlock({ billing_url: null, provider_label: 'DeepSeek' }))
    expect(copy.title).toContain('DeepSeek')
    expect(copy.confirmLabel).toBe('Switch provider')
  })
})
