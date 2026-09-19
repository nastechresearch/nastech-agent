// @vitest-environment jsdom
import { act, cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import type { DesktopBootstrapEvent, DesktopBootstrapState, DesktopConnectionProbeResult } from '@/global'

import { DesktopInstallOverlay } from './desktop-install-overlay'

function bootstrapState(overrides: Partial<DesktopBootstrapState> = {}): DesktopBootstrapState {
  return {
    active: false,
    manifest: null,
    stages: {},
    error: null,
    log: [],
    startedAt: null,
    completedAt: null,
    setupChoice: null,
    unsupportedPlatform: null,
    ...overrides
  }
}

function installDesktopMock(state: DesktopBootstrapState) {
  const bootstrapListeners = new Set<(event: DesktopBootstrapEvent) => void>()

  const desktop = {
    getBootstrapState: vi.fn().mockResolvedValue(state),
    onBootstrapEvent: vi.fn((listener: (event: DesktopBootstrapEvent) => void) => {
      bootstrapListeners.add(listener)

      return () => bootstrapListeners.delete(listener)
    }),
    continueBootstrapLocal: vi.fn().mockResolvedValue({ ok: true }),
    probeConnectionConfig: vi.fn(),
    testConnectionConfig: vi.fn(),
    applyConnectionConfig: vi.fn(),
    oauthLoginConnectionConfig: vi.fn(),
    openExternal: vi.fn(),
    emitBootstrapEvent: (event: DesktopBootstrapEvent) => {
      for (const listener of bootstrapListeners) {
        listener(event)
      }
    }
  }

  Object.defineProperty(window, 'nastechDesktop', {
    configurable: true,
    value: desktop
  })

  return desktop
}

// Resolve the instant a node commits, via MutationObserver rather than
// waitFor's polling timer. findBy* only settles on a timer tick, by which
// point React has already drained its passive effects — that hides any bug
// living in the window between paint and effect.
function whenPresent(text: string): Promise<HTMLElement> {
  return new Promise(resolve => {
    const existing = screen.queryByText(text)

    if (existing) {
      resolve(existing)

      return
    }

    const observer = new MutationObserver(() => {
      const node = screen.queryByText(text)

      if (node) {
        observer.disconnect()
        resolve(node)
      }
    })

    observer.observe(document.body, { childList: true, subtree: true, characterData: true })
  })
}

beforeEach(() => {
  vi.restoreAllMocks()
})

afterEach(() => {
  cleanup()
  vi.useRealTimers()
  Reflect.deleteProperty(window, 'nastechDesktop')
})

describe('DesktopInstallOverlay first-run setup', () => {
  it('shows the remote/local choice without installer progress', async () => {
    installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'win32', activeRoot: 'C:\\Users\\me\\AppData\\Local\\nastech\\nastech-agent' }
      })
    )

    render(<DesktopInstallOverlay />)

    expect(await screen.findByText('Set up Nastech Desktop')).toBeTruthy()
    expect(screen.getByText('Connect to existing Nastech')).toBeTruthy()
    expect(screen.getByText('Install Nastech locally')).toBeTruthy()
    expect(screen.queryByText(/steps complete/i)).toBeNull()
    expect(screen.queryByText(/Fetching installer manifest/i)).toBeNull()
  })

  it('continues local bootstrap only when Install Nastech locally is selected', async () => {
    const desktop = installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'win32', activeRoot: 'C:\\Users\\me\\AppData\\Local\\nastech\\nastech-agent' }
      })
    )

    render(<DesktopInstallOverlay />)

    fireEvent.click(await screen.findByText('Install Nastech locally'))

    expect(desktop.continueBootstrapLocal).toHaveBeenCalledTimes(1)
    expect(screen.getByText('Set up Nastech Desktop')).toBeTruthy()

    act(() => {
      desktop.emitBootstrapEvent({ type: 'manifest', protocolVersion: 1, stages: [] })
    })

    await waitFor(() => expect(screen.queryByText('Set up Nastech Desktop')).toBeNull())
    expect(screen.getByText(/Fetching installer manifest/i)).toBeTruthy()
  })

  it('surfaces a recoverable error when the local-bootstrap bridge is unavailable', async () => {
    const desktop = installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'win32', activeRoot: 'C:\\Users\\me\\AppData\\Local\\nastech\\nastech-agent' }
      })
    )

    desktop.continueBootstrapLocal = undefined as never
    render(<DesktopInstallOverlay />)

    const install = (await screen.findByText('Install Nastech locally')).closest('button') as HTMLButtonElement
    fireEvent.click(install)

    expect(
      await screen.findByText('Local installation could not start. Restart Nastech Desktop and try again.')
    ).toBeTruthy()
    expect(install.disabled).toBe(false)
  })

  it('keeps the local-start error when the first snapshot commits under the click', async () => {
    const desktop = installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'win32', activeRoot: 'C:\\Users\\me\\AppData\\Local\\nastech\\nastech-agent' }
      })
    )

    desktop.continueBootstrapLocal = undefined as never
    render(<DesktopInstallOverlay />)

    // Click the instant the choice paints, before React drains the passive
    // effect that reacts to the first snapshot. A loaded runner hits this
    // window by accident; observing the DOM directly hits it every time.
    const install = (await whenPresent('Install Nastech locally')).closest('button') as HTMLButtonElement
    fireEvent.click(install)

    await act(async () => {
      await Promise.resolve()
    })

    expect(screen.queryByText('Local installation could not start. Restart Nastech Desktop and try again.')).toBeTruthy()
  })

  it('clears a stale local-start error when a repair presents a different root', async () => {
    const desktop = installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'win32', activeRoot: 'C:\\Users\\me\\AppData\\Local\\nastech\\nastech-agent' }
      })
    )

    desktop.continueBootstrapLocal = undefined as never
    render(<DesktopInstallOverlay />)

    fireEvent.click((await screen.findByText('Install Nastech locally')).closest('button') as HTMLButtonElement)
    expect(
      await screen.findByText('Local installation could not start. Restart Nastech Desktop and try again.')
    ).toBeTruthy()

    act(() => {
      desktop.emitBootstrapEvent({
        type: 'setup-choice',
        active: false,
        platform: 'win32',
        activeRoot: 'C:\\Users\\me\\AppData\\Local\\nastech\\nastech-agent-repaired'
      })
    })

    expect(screen.queryByText('Local installation could not start. Restart Nastech Desktop and try again.')).toBeNull()
  })

  it('opens the remote connection form from the first-run choice', async () => {
    installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'linux', activeRoot: '/home/me/.nastech/nastech-agent' }
      })
    )

    render(<DesktopInstallOverlay />)

    fireEvent.click(await screen.findByText('Connect to existing Nastech'))

    expect(await screen.findByText('Gateway URL')).toBeTruthy()
    expect(screen.getByText('Test connection')).toBeTruthy()
    expect(screen.getByText('Apply and reconnect')).toBeTruthy()
  })

  it('returns from the remote connection form to the first-run choice', async () => {
    installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'linux', activeRoot: '/home/me/.nastech/nastech-agent' }
      })
    )

    render(<DesktopInstallOverlay />)

    fireEvent.click(await screen.findByText('Connect to existing Nastech'))
    expect(await screen.findByText('Gateway URL')).toBeTruthy()

    fireEvent.click(screen.getByText('Back'))

    expect(await screen.findByText('Set up Nastech Desktop')).toBeTruthy()
    expect(screen.getByText('Install Nastech locally')).toBeTruthy()
  })

  it('requires a successful token connection test before applying remote config', async () => {
    const desktop = installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'linux', activeRoot: '/home/me/.nastech/nastech-agent' }
      })
    )

    desktop.probeConnectionConfig.mockResolvedValue({
      authMode: 'token',
      baseUrl: 'https://gateway.example.com/nastech',
      error: null,
      providers: [],
      reachable: true,
      version: '0.17.0'
    })
    desktop.testConnectionConfig.mockResolvedValue({
      baseUrl: 'https://gateway.example.com/nastech',
      ok: true,
      version: '0.17.0'
    })
    desktop.applyConnectionConfig.mockImplementation(async () => {
      desktop.emitBootstrapEvent({ type: 'dismissed' })

      return { mode: 'remote' }
    })

    render(<DesktopInstallOverlay />)

    fireEvent.click(await screen.findByText('Connect to existing Nastech'))
    fireEvent.change(await screen.findByPlaceholderText('https://gateway.example.com/nastech'), {
      target: { value: 'https://gateway.example.com/nastech' }
    })

    const apply = screen.getByText('Apply and reconnect').closest('button') as HTMLButtonElement
    expect(apply.disabled).toBe(true)

    await act(async () => {
      await new Promise(resolve => setTimeout(resolve, 550))
    })

    fireEvent.change(await screen.findByPlaceholderText('Paste session token'), {
      target: { value: 'session-secret' }
    })
    fireEvent.click(screen.getByText('Test connection'))

    await waitFor(() => {
      expect(desktop.testConnectionConfig).toHaveBeenCalledWith({
        mode: 'remote',
        remoteAuthMode: 'token',
        remoteToken: 'session-secret',
        remoteUrl: 'https://gateway.example.com/nastech'
      })
    })

    await screen.findByText('Connected to https://gateway.example.com/nastech (0.17.0).')
    expect(apply.disabled).toBe(false)

    fireEvent.click(screen.getByText('Apply and reconnect'))

    await waitFor(() => {
      expect(desktop.applyConnectionConfig).toHaveBeenCalledWith({
        mode: 'remote',
        remoteAuthMode: 'token',
        remoteToken: 'session-secret',
        remoteUrl: 'https://gateway.example.com/nastech'
      })
    })
    await waitFor(() => expect(screen.queryByText('Gateway URL')).toBeNull())
  })

  it('ignores a completed probe after the gateway URL becomes invalid', async () => {
    const desktop = installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'linux', activeRoot: '/home/me/.nastech/nastech-agent' }
      })
    )

    let resolveProbe: ((result: DesktopConnectionProbeResult) => void) | undefined

    const pendingProbe = new Promise<DesktopConnectionProbeResult>(resolve => {
      resolveProbe = resolve
    })

    desktop.probeConnectionConfig.mockReturnValue(pendingProbe)

    render(<DesktopInstallOverlay />)

    fireEvent.click(await screen.findByText('Connect to existing Nastech'))
    const urlInput = await screen.findByPlaceholderText('https://gateway.example.com/nastech')
    fireEvent.change(urlInput, { target: { value: 'https://gateway.example.com/nastech' } })

    await act(async () => {
      await new Promise(resolve => setTimeout(resolve, 550))
    })
    expect(desktop.probeConnectionConfig).toHaveBeenCalledTimes(1)

    fireEvent.change(urlInput, { target: { value: 'not-a-url' } })
    await act(async () => {
      resolveProbe?.({
        authMode: 'token',
        baseUrl: 'https://gateway.example.com/nastech',
        error: null,
        providers: [],
        reachable: true,
        version: '0.17.0'
      })
      await pendingProbe
    })

    expect(screen.queryByPlaceholderText('Paste session token')).toBeNull()
    expect((screen.getByText('Test connection').closest('button') as HTMLButtonElement).disabled).toBe(true)
    expect((screen.getByText('Apply and reconnect').closest('button') as HTMLButtonElement).disabled).toBe(true)
  })

  it('does not enable Apply when credentials change during a connection test', async () => {
    const desktop = installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'linux', activeRoot: '/home/me/.nastech/nastech-agent' }
      })
    )

    desktop.probeConnectionConfig.mockResolvedValue({
      authMode: 'token',
      baseUrl: 'https://gateway.example.com/nastech',
      error: null,
      providers: [],
      reachable: true,
      version: '0.17.0'
    })

    let resolveTest: ((result: { baseUrl: string; ok: boolean; version: string }) => void) | undefined

    const pendingTest = new Promise<{ baseUrl: string; ok: boolean; version: string }>(resolve => {
      resolveTest = resolve
    })

    desktop.testConnectionConfig.mockReturnValue(pendingTest)

    render(<DesktopInstallOverlay />)

    fireEvent.click(await screen.findByText('Connect to existing Nastech'))
    fireEvent.change(await screen.findByPlaceholderText('https://gateway.example.com/nastech'), {
      target: { value: 'https://gateway.example.com/nastech' }
    })

    await act(async () => {
      await new Promise(resolve => setTimeout(resolve, 550))
    })

    const tokenInput = await screen.findByPlaceholderText('Paste session token')
    const apply = screen.getByText('Apply and reconnect').closest('button') as HTMLButtonElement

    fireEvent.change(tokenInput, { target: { value: 'token-a' } })
    fireEvent.click(screen.getByText('Test connection'))
    await waitFor(() => expect(desktop.testConnectionConfig).toHaveBeenCalledTimes(1))

    fireEvent.change(tokenInput, { target: { value: 'token-b' } })

    await act(async () => {
      resolveTest?.({ baseUrl: 'https://gateway.example.com/nastech', ok: true, version: '0.17.0' })
      await pendingTest
    })

    expect(screen.queryByText('Connected to https://gateway.example.com/nastech (0.17.0).')).toBeNull()
    expect(apply.disabled).toBe(true)
  })

  it('restores remote apply controls when applying the tested connection fails', async () => {
    const desktop = installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'linux', activeRoot: '/home/me/.nastech/nastech-agent' }
      })
    )

    desktop.probeConnectionConfig.mockResolvedValue({
      authMode: 'token',
      baseUrl: 'https://gateway.example.com/nastech',
      error: null,
      providers: [],
      reachable: true,
      version: '0.17.0'
    })
    desktop.testConnectionConfig.mockResolvedValue({
      baseUrl: 'https://gateway.example.com/nastech',
      ok: true,
      version: '0.17.0'
    })
    desktop.applyConnectionConfig.mockRejectedValue(new Error('remote apply failed'))

    render(<DesktopInstallOverlay />)

    fireEvent.click(await screen.findByText('Connect to existing Nastech'))
    fireEvent.change(await screen.findByPlaceholderText('https://gateway.example.com/nastech'), {
      target: { value: 'https://gateway.example.com/nastech' }
    })

    await act(async () => {
      await new Promise(resolve => setTimeout(resolve, 550))
    })

    fireEvent.change(await screen.findByPlaceholderText('Paste session token'), {
      target: { value: 'session-secret' }
    })
    fireEvent.click(screen.getByText('Test connection'))
    await screen.findByText('Connected to https://gateway.example.com/nastech (0.17.0).')

    const apply = screen.getByText('Apply and reconnect').closest('button') as HTMLButtonElement
    fireEvent.click(apply)

    expect(await screen.findByText('remote apply failed')).toBeTruthy()
    expect(apply.disabled).toBe(false)
    expect(screen.getByText('Gateway URL')).toBeTruthy()
  })

  it('signs in, tests, and applies a password-style remote gateway', async () => {
    const desktop = installDesktopMock(
      bootstrapState({
        setupChoice: { platform: 'linux', activeRoot: '/home/me/.nastech/nastech-agent' }
      })
    )

    desktop.probeConnectionConfig.mockResolvedValue({
      authMode: 'oauth',
      baseUrl: 'https://gateway.example.com/nastech',
      error: null,
      providers: [{ displayName: 'Username & Password', name: 'password', supportsPassword: true }],
      reachable: true,
      version: '0.17.0'
    })
    desktop.oauthLoginConnectionConfig.mockResolvedValue({
      baseUrl: 'https://gateway.example.com/nastech',
      connected: true,
      ok: true
    })
    desktop.testConnectionConfig.mockResolvedValue({
      baseUrl: 'https://gateway.example.com/nastech',
      ok: true,
      version: null
    })
    desktop.applyConnectionConfig.mockResolvedValue({ mode: 'remote' })

    render(<DesktopInstallOverlay />)

    fireEvent.click(await screen.findByText('Connect to existing Nastech'))
    fireEvent.change(await screen.findByPlaceholderText('https://gateway.example.com/nastech'), {
      target: { value: 'https://gateway.example.com/nastech' }
    })

    await act(async () => {
      await new Promise(resolve => setTimeout(resolve, 550))
    })

    expect(screen.queryByText('Sign in with Username & Password')).toBeNull()
    fireEvent.click(await screen.findByText('Sign in'))

    await waitFor(() => {
      expect(desktop.oauthLoginConnectionConfig).toHaveBeenCalledWith('https://gateway.example.com/nastech')
    })

    fireEvent.click(screen.getByText('Test connection'))

    await waitFor(() => {
      expect(desktop.testConnectionConfig).toHaveBeenCalledWith({
        mode: 'remote',
        remoteAuthMode: 'oauth',
        remoteToken: undefined,
        remoteUrl: 'https://gateway.example.com/nastech'
      })
    })

    await screen.findByText('Connected to https://gateway.example.com/nastech.')
    const apply = screen.getByText('Apply and reconnect').closest('button') as HTMLButtonElement
    expect(apply.disabled).toBe(false)
    fireEvent.click(apply)

    await waitFor(() => {
      expect(desktop.applyConnectionConfig).toHaveBeenCalledWith({
        mode: 'remote',
        remoteAuthMode: 'oauth',
        remoteToken: undefined,
        remoteUrl: 'https://gateway.example.com/nastech'
      })
    })
  })

  it('offers remote connection from the unsupported packaged install screen', async () => {
    const desktop = installDesktopMock(
      bootstrapState({
        unsupportedPlatform: {
          platform: 'darwin',
          activeRoot: '/Users/me/.nastech/nastech-agent',
          installCommand: 'curl -fsSL https://example.invalid/install.sh | sh',
          docsUrl: 'https://example.invalid/docs'
        }
      })
    )

    render(<DesktopInstallOverlay />)

    expect(await screen.findByText('Nastech needs a one-time install')).toBeTruthy()

    fireEvent.click(screen.getByText('Connect existing'))

    expect(await screen.findByText('Gateway URL')).toBeTruthy()

    desktop.probeConnectionConfig.mockResolvedValue({
      authMode: 'token',
      baseUrl: 'https://gateway.example.com/nastech',
      error: null,
      providers: [],
      reachable: true,
      version: '0.17.0'
    })
    desktop.testConnectionConfig.mockResolvedValue({
      baseUrl: 'https://gateway.example.com/nastech',
      ok: true,
      version: '0.17.0'
    })
    desktop.applyConnectionConfig.mockImplementation(async () => {
      desktop.emitBootstrapEvent({ type: 'dismissed' })

      return { mode: 'remote' }
    })

    fireEvent.change(screen.getByPlaceholderText('https://gateway.example.com/nastech'), {
      target: { value: 'https://gateway.example.com/nastech' }
    })

    await act(async () => {
      await new Promise(resolve => setTimeout(resolve, 550))
    })

    fireEvent.change(await screen.findByPlaceholderText('Paste session token'), {
      target: { value: 'session-secret' }
    })
    fireEvent.click(screen.getByText('Test connection'))
    await screen.findByText('Connected to https://gateway.example.com/nastech (0.17.0).')
    fireEvent.click(screen.getByText('Apply and reconnect'))

    await waitFor(() => expect(screen.queryByText('Gateway URL')).toBeNull())
    expect(screen.queryByText('Nastech needs a one-time install')).toBeNull()
  })
})
