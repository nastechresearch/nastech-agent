import { afterEach, describe, expect, it, vi } from 'vitest'

import { createBrowserClipboardBridge } from './browser-clipboard'
import { installClipboardShim, writeClipboardText } from './clipboard'

const desktopWindow = window as unknown as { nastechDesktop?: Window['nastechDesktop'] }

function installClipboard(writeText: (text: string) => Promise<void>) {
  Object.defineProperty(navigator, 'clipboard', {
    configurable: true,
    value: { writeText }
  })
}

afterEach(() => {
  Reflect.deleteProperty(desktopWindow, 'nastechDesktop')
  Reflect.deleteProperty(navigator, 'clipboard')
  vi.restoreAllMocks()
  delete document.documentElement.dataset.nastechDesktopHost
})

describe('installClipboardShim', () => {
  it('routes an Electron write through IPC first', async () => {
    const nativeWrite = vi.fn().mockResolvedValue(undefined)
    const ipcWrite = vi.fn().mockResolvedValue(true)
    installClipboard(nativeWrite)
    desktopWindow.nastechDesktop = { writeClipboard: ipcWrite } as unknown as Window['nastechDesktop']

    installClipboardShim()
    await navigator.clipboard.writeText('payload')

    expect(ipcWrite).toHaveBeenCalledWith('payload')
    expect(nativeWrite).not.toHaveBeenCalled()
  })

  it('uses the native write only after the Electron IPC write fails', async () => {
    const nativeWrite = vi.fn().mockResolvedValue(undefined)
    const ipcWrite = vi.fn().mockRejectedValue(new Error('main process gone'))
    installClipboard(nativeWrite)
    desktopWindow.nastechDesktop = { writeClipboard: ipcWrite } as unknown as Window['nastechDesktop']

    installClipboardShim()
    await navigator.clipboard.writeText('payload')

    expect(ipcWrite).toHaveBeenCalledWith('payload')
    expect(nativeWrite).toHaveBeenCalledWith('payload')
  })
})

describe('writeClipboardText', () => {
  it('writes through Electron IPC first, so a copy from an unfocused document still lands', async () => {
    const nativeWrite = vi.fn().mockRejectedValue(new Error('Document is not focused'))
    const ipcWrite = vi.fn().mockResolvedValue(true)
    installClipboard(nativeWrite)
    desktopWindow.nastechDesktop = { writeClipboard: ipcWrite } as unknown as Window['nastechDesktop']

    await writeClipboardText('payload')

    expect(ipcWrite).toHaveBeenCalledTimes(1)
    expect(nativeWrite).not.toHaveBeenCalled()
  })

  it('writes a browser-hosted copy through the native clipboard once', async () => {
    const nativeWrite = vi.fn().mockResolvedValue(undefined)
    installClipboard(nativeWrite)
    document.documentElement.dataset.nastechDesktopHost = 'browser'
    desktopWindow.nastechDesktop = createBrowserClipboardBridge({
      saveBuffer: async () => ''
    }) as Window['nastechDesktop']
    installClipboardShim()

    await writeClipboardText('payload')

    expect(nativeWrite).toHaveBeenCalledTimes(1)
    expect(nativeWrite).toHaveBeenCalledWith('payload')
  })

  it('attempts IPC and native once when an installed Electron shim fails', async () => {
    const nativeWrite = vi.fn().mockRejectedValue(new Error('lost focus'))
    const bridgeWrite = vi.fn().mockResolvedValue(false)
    installClipboard(nativeWrite)
    desktopWindow.nastechDesktop = { writeClipboard: bridgeWrite } as unknown as Window['nastechDesktop']
    installClipboardShim()
    await expect(writeClipboardText('payload')).rejects.toThrow()
    expect(nativeWrite).toHaveBeenCalledTimes(1)
    expect(bridgeWrite).toHaveBeenCalledTimes(1)
  })

  it('does not retry the same native API through the installed browser bridge', async () => {
    const nativeWrite = vi.fn().mockRejectedValue(new Error('permission denied'))
    installClipboard(nativeWrite)
    document.documentElement.dataset.nastechDesktopHost = 'browser'
    desktopWindow.nastechDesktop = createBrowserClipboardBridge({
      saveBuffer: async () => ''
    }) as Window['nastechDesktop']
    installClipboardShim()
    await expect(writeClipboardText('payload')).rejects.toThrow('permission denied')
    expect(nativeWrite).toHaveBeenCalledTimes(1)
  })

  it('reports an unavailable bridge as a failed copy', async () => {
    const bridgeWrite = vi.fn().mockResolvedValue(false)
    desktopWindow.nastechDesktop = { writeClipboard: bridgeWrite } as unknown as Window['nastechDesktop']

    await expect(writeClipboardText('payload')).rejects.toThrow('Clipboard write is unavailable')
  })
})
