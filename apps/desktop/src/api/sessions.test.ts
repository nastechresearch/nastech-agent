import { beforeEach, describe, expect, it, vi } from 'vitest'

vi.mock('@/lib/gateway-rpc', () => ({ isMissingRestEndpoint: () => false }))
vi.mock('@/store/transcript-tail', () => ({ recordTranscriptTail: vi.fn() }))
vi.mock('./client', () => ({
  capabilityScoped: vi.fn(),
  getApiRequestConnection: vi.fn(() => 'prometheus'),
  nastechApi: vi.fn(),
  profileScoped: vi.fn(() => ({}))
}))

const client = await import('./client')
const { listSidebarSessions } = await import('./sessions')

const nastechApi = vi.mocked(client.nastechApi)

beforeEach(() => {
  vi.clearAllMocks()
  vi.mocked(client.getApiRequestConnection).mockReturnValue('prometheus')
})

describe('listSidebarSessions remote ownership', () => {
  it('stamps active remote rows so a later resume stays on their gateway', async () => {
    nastechApi.mockResolvedValue({
      cron: { sessions: [] },
      messaging: { sessions: [] },
      recents: {
        sessions: [{ id: 'remote-session', profile: 'default', source: 'desktop', title: 'Remote chat' }]
      }
    } as never)

    const result = await listSidebarSessions({
      recentsProfile: 'default',
      recentsLimit: 40,
      recentsExclude: [],
      cronLimit: 20,
      messagingLimit: 40,
      messagingExclude: []
    })

    expect(result.recents.sessions[0]).toMatchObject({ connection_id: 'prometheus', id: 'remote-session' })
  })
})
