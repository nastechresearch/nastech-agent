import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import type { NastechReadDirResult } from '@/global'
import type * as NastechModule from '@/nastech'

import { $pluginRecords, publishPlugin, setPluginEnabled } from './plugins-store'
import { discoverRuntimePlugins, loadRuntimePlugin, watchRuntimePlugins } from './runtime-loader'

// getStatus would supply the connected backend's nastech_home — a REMOTE path in
// remote mode. The disk scanner must NOT derive the plugin root from it (#66899).
const getStatus = vi.fn(async () => ({ nastech_home: '/remote/box/.nastech' }))

vi.mock('@/nastech', async importActual => ({
  ...(await importActual<typeof NastechModule>()),
  getStatus: () => getStatus()
}))

const desktopPluginsRoot = vi.fn<() => Promise<string>>()
const agentPluginsRoot = vi.fn<() => Promise<string>>()
const readDir = vi.fn<(path: string) => Promise<NastechReadDirResult>>()
const readFileText = vi.fn<(path: string) => Promise<{ text: string }>>()
const watchDirectory = vi.fn<(path: string) => Promise<{ id: string }>>()
const watchPreviewFile = vi.fn<(path: string) => Promise<{ id: string }>>()
const onPreviewFileChanged = vi.fn()

beforeEach(() => {
  desktopPluginsRoot.mockReset()
  agentPluginsRoot.mockReset()
  readDir.mockReset()
  readFileText.mockReset()
  watchDirectory.mockReset()
  watchPreviewFile.mockReset()
  onPreviewFileChanged.mockReset()
  getStatus.mockClear()
  ;(window as unknown as { nastechDesktop: unknown }).nastechDesktop = {
    agentPluginsRoot,
    desktopPluginsRoot,
    onPreviewFileChanged,
    readDir,
    readFileText,
    watchDirectory,
    watchPreviewFile
  }
})

afterEach(() => {
  delete (window as unknown as { nastechDesktop?: unknown }).nastechDesktop
})

describe('scanDiskPlugins (#66899)', () => {
  it('scans the Electron-resolved local roots, never the backend nastech_home', async () => {
    desktopPluginsRoot.mockResolvedValue('/local/.nastech/desktop-plugins')
    agentPluginsRoot.mockResolvedValue('/local/.nastech/plugins')
    readDir.mockResolvedValue({ entries: [] })

    await discoverRuntimePlugins()

    expect(desktopPluginsRoot).toHaveBeenCalled()
    expect(readDir).toHaveBeenCalledWith('/local/.nastech/desktop-plugins')
    expect(readDir).toHaveBeenCalledWith('/local/.nastech/plugins')
    // The remote backend's nastech_home must never feed the local plugin scan.
    expect(getStatus).not.toHaveBeenCalled()
    expect(readDir).not.toHaveBeenCalledWith('/remote/box/.nastech/desktop-plugins')
  })

  it('no-ops when the resolvers yield no local root', async () => {
    desktopPluginsRoot.mockResolvedValue('')
    agentPluginsRoot.mockResolvedValue('')

    await discoverRuntimePlugins()

    expect(readDir).not.toHaveBeenCalled()
  })

  it('probes desktop/plugin.js inside agent-plugin packages (unified packaging)', async () => {
    desktopPluginsRoot.mockResolvedValue('/local/.nastech/desktop-plugins')
    agentPluginsRoot.mockResolvedValue('/local/.nastech/plugins')
    readDir.mockImplementation(async dir =>
      dir === '/local/.nastech/plugins'
        ? { entries: [{ isDirectory: true, name: 'my-feature', path: '/local/.nastech/plugins/my-feature' }] }
        : { entries: [] }
    )
    // No desktop half in this package — probe must target desktop/plugin.js.
    readFileText.mockRejectedValue(new Error('ENOENT'))

    await discoverRuntimePlugins()

    expect(readFileText).toHaveBeenCalledWith('/local/.nastech/plugins/my-feature/desktop/plugin.js')
    // The Python half's files must never be probed as a desktop entry.
    expect(readFileText).not.toHaveBeenCalledWith('/local/.nastech/plugins/my-feature/plugin.js')
  })

  it('still scans the standalone root when agentPluginsRoot is absent (older shell)', async () => {
    delete (window.nastechDesktop as unknown as { agentPluginsRoot?: unknown }).agentPluginsRoot
    desktopPluginsRoot.mockResolvedValue('/local/.nastech/desktop-plugins')
    readDir.mockResolvedValue({ entries: [] })

    await discoverRuntimePlugins()

    expect(readDir).toHaveBeenCalledWith('/local/.nastech/desktop-plugins')
    expect(readDir).toHaveBeenCalledTimes(1)
  })

  it('loads a unified desktop half OPT-IN: inventoried but not activated by default', async () => {
    desktopPluginsRoot.mockResolvedValue('/local/.nastech/desktop-plugins')
    agentPluginsRoot.mockResolvedValue('/local/.nastech/plugins')
    readDir.mockImplementation(async dir =>
      dir === '/local/.nastech/plugins'
        ? { entries: [{ isDirectory: true, name: 'uni', path: '/local/.nastech/plugins/uni' }] }
        : { entries: [] }
    )

    const register = vi.fn()

    ;(globalThis as unknown as { __uniRegister: unknown }).__uniRegister = register
    readFileText.mockResolvedValue({
      text: 'export default { id: "uni", register: globalThis.__uniRegister }'
    })
    watchPreviewFile.mockResolvedValue({ id: 'w-uni' })

    // The loader evaluates plugins via blob-URL import(), which vite's module
    // runner can't resolve in tests — reroute to a data: URL, which node's
    // native ESM loader handles.
    const createObjectURL = vi
      .spyOn(URL, 'createObjectURL')
      .mockImplementation(
        blob =>
          `data:text/javascript;base64,${Buffer.from((blob as unknown as { parts: string[] }).parts.join('')).toString('base64')}`
      )

    const revokeObjectURL = vi.spyOn(URL, 'revokeObjectURL').mockImplementation(() => undefined)
    const RealBlob = globalThis.Blob
    vi.stubGlobal(
      'Blob',
      class {
        parts: string[]
        constructor(parts: string[]) {
          this.parts = parts
        }
      }
    )

    try {
      await discoverRuntimePlugins()

      // Inventoried for Settings → Plugins, but the root's opt-in posture wins:
      // ~/.nastech/plugins stays installed-but-inert until the user toggles it.
      expect($pluginRecords.get().uni).toMatchObject({ kind: 'disk', status: 'disabled' })
      expect(register).not.toHaveBeenCalled()

      // The user's explicit enable still activates it.
      await setPluginEnabled('uni', true)
      expect(register).toHaveBeenCalledTimes(1)
      expect($pluginRecords.get().uni.status).toBe('loaded')
    } finally {
      createObjectURL.mockRestore()
      revokeObjectURL.mockRestore()
      vi.stubGlobal('Blob', RealBlob)
      delete (globalThis as unknown as { __uniRegister?: unknown }).__uniRegister
    }
  })
})

describe('watchRuntimePlugins dir watch (#66899)', () => {
  it('watches both Electron-resolved local roots, never the backend nastech_home', async () => {
    desktopPluginsRoot.mockResolvedValue('/local/.nastech/desktop-plugins')
    agentPluginsRoot.mockResolvedValue('/local/.nastech/plugins')
    readDir.mockResolvedValue({ entries: [] })
    watchDirectory.mockResolvedValue({ id: 'watch-1' })

    watchRuntimePlugins()
    // Drain the async scan + startDirWatches chains.
    await vi.waitFor(() => expect(watchDirectory).toHaveBeenCalledTimes(2))

    expect(watchDirectory).toHaveBeenCalledWith('/local/.nastech/desktop-plugins')
    expect(watchDirectory).toHaveBeenCalledWith('/local/.nastech/plugins')
    expect(watchDirectory).not.toHaveBeenCalledWith('/remote/box/.nastech/desktop-plugins')
    expect(getStatus).not.toHaveBeenCalled()
  })
})

describe('bundled-shadowed disk copies', () => {
  it('skips a disk copy of a bundled plugin but publishes a visible inventory row', async () => {
    // The bundled twin is already registered (build-time glob).
    publishPlugin({ id: 'nastech-bots', name: 'Bot Mode', kind: 'bundled', status: 'loaded' })

    // Same blob→data: URL reroute as the opt-in test above.
    const createObjectURL = vi
      .spyOn(URL, 'createObjectURL')
      .mockImplementation(
        blob =>
          `data:text/javascript;base64,${Buffer.from((blob as unknown as { parts: string[] }).parts.join('')).toString('base64')}`
      )

    const revokeObjectURL = vi.spyOn(URL, 'revokeObjectURL').mockImplementation(() => undefined)
    const RealBlob = globalThis.Blob
    vi.stubGlobal(
      'Blob',
      class {
        parts: string[]
        constructor(parts: string[]) {
          this.parts = parts
        }
      }
    )

    try {
      const id = await loadRuntimePlugin(
        'export default { id: "nastech-bots", name: "Bot Mode", register() {} }',
        'nastech-bots',
        { file: '/local/.nastech/desktop-plugins/nastech-bots/plugin.js' }
      )

      // Skipped — the bundled copy stays the only live registration...
      expect(id).toBeNull()
      expect($pluginRecords.get()['nastech-bots']).toMatchObject({ kind: 'bundled', status: 'loaded' })

      // ...but the stale folder is DISCOVERABLE: an inventory row names it,
      // carries its path (reveal/delete affordance), and can never activate.
      expect($pluginRecords.get()['nastech-bots:disk-shadowed']).toMatchObject({
        kind: 'disk',
        status: 'disabled',
        file: '/local/.nastech/desktop-plugins/nastech-bots/plugin.js'
      })
    } finally {
      createObjectURL.mockRestore()
      revokeObjectURL.mockRestore()
      vi.stubGlobal('Blob', RealBlob)
    }
  })
})
