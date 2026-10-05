import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import type * as NastechApi from '@/nastech'
import { $desktopOnboarding, type DesktopOnboardingState, type OnboardingContext } from '@/store/onboarding'

import { FlowPanel } from './flow'

// Only the catalog fetch is replaced; the model assignment keeps its real path
// down to window.nastechDesktop.api so the test observes the wire body.
vi.mock('@/nastech', async importOriginal => ({
  ...(await importOriginal<typeof NastechApi>()),
  getGlobalModelOptions: async () => ({
    providers: [
      { free_tier: false, models: ['gpt-5.6-terra'], name: 'OpenAI OAuth (ChatGPT)', slug: 'openai' },
      { models: ['deepseek/deepseek-v4-flash-0731'], name: 'Nastech Portal', slug: 'nastech' }
    ]
  })
}))

// The real picker is a cmdk/Radix dialog; stand in a button that reports the
// same {provider, model} selection shape the real one emits.
vi.mock('@/components/model-picker', () => ({
  ModelPickerDialog: ({
    onSelect,
    open
  }: {
    onSelect: (selection: { model: string; provider: string }) => void
    open: boolean
  }) =>
    open ? (
      <button onClick={() => onSelect({ model: 'deepseek/deepseek-v4-flash-0731', provider: 'nastech' })} type="button">
        pick-nastech-model
      </button>
    ) : null
}))

const ctx: OnboardingContext = { requestGateway: async () => undefined as never }

function confirmingModelState(): DesktopOnboardingState {
  return {
    configured: false,
    flow: {
      status: 'confirming_model',
      currentModel: 'gpt-5.6-terra',
      label: 'OpenAI OAuth (ChatGPT)',
      providerSlug: 'openai',
      saving: false
    },
    mode: 'oauth',
    providers: null,
    reason: null,
    requested: false,
    firstRunSkipped: false,
    manual: false,
    localEndpoint: false,
    freeTierReady: false
  }
}

function Harness() {
  const state = $desktopOnboarding.get()

  return (
    <QueryClientProvider client={new QueryClient({ defaultOptions: { queries: { retry: false } } })}>
      <FlowPanel ctx={ctx} flow={state.flow} leaving={false} onBegin={() => undefined} />
    </QueryClientProvider>
  )
}

beforeEach(() => {
  $desktopOnboarding.set(confirmingModelState())
})

afterEach(() => {
  cleanup()
  $desktopOnboarding.set({ ...confirmingModelState(), configured: null, flow: { status: 'idle' } })
})

describe('ConfirmingModelPanel model pick', () => {
  it('persists a cross-provider pick against the picked model provider, not the sign-in provider', async () => {
    const calls: { body?: unknown; path: string }[] = []

    Object.defineProperty(window, 'nastechDesktop', {
      configurable: true,
      value: {
        api: async ({ body, path }: { body?: unknown; path: string }) => {
          calls.push({ body, path })

          if (path === '/api/model/set') {
            return { ok: true, provider: 'nastech', model: 'deepseek/deepseek-v4-flash-0731' }
          }

          throw new Error(`unexpected api path: ${path}`)
        }
      }
    })

    render(<Harness />)

    // The Pro badge only renders once the catalog query has resolved — the
    // relabel below reads the picked provider's name from that catalog.
    await screen.findByText('Pro')

    // The user signed in with OpenAI OAuth; the picker offers a deepseek
    // model that only Nastech Portal serves.
    fireEvent.click(screen.getByRole('button', { name: 'Change' }))
    fireEvent.click(await screen.findByRole('button', { name: 'pick-nastech-model' }))

    await waitFor(() => expect(calls.some(c => c.path === '/api/model/set')).toBe(true))

    expect(calls.find(c => c.path === '/api/model/set')?.body).toMatchObject({
      scope: 'main',
      provider: 'nastech',
      model: 'deepseek/deepseek-v4-flash-0731'
    })

    const flow = $desktopOnboarding.get().flow
    expect(flow.status).toBe('confirming_model')

    if (flow.status === 'confirming_model') {
      expect(flow.providerSlug).toBe('nastech')
      expect(flow.label).toBe('Nastech Portal')
    }
  })
})
