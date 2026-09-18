import { cleanup, fireEvent, render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router'
import { afterEach, describe, expect, it, vi } from 'vitest'

import { WslgWindowControls } from './wslg-window-controls'

const windowControls = {
  close: vi.fn(),
  custom: true,
  minimize: vi.fn(),
  toggleMaximize: vi.fn()
}

const desktopWindow = window as unknown as { nastechDesktop?: Window['nastechDesktop'] }
const originalNastechDesktop = desktopWindow.nastechDesktop

function renderControls(isMaximized = false, path = '/', isFullscreen = false) {
  return render(
    <MemoryRouter initialEntries={[path]}>
      <WslgWindowControls isFullscreen={isFullscreen} isMaximized={isMaximized} />
    </MemoryRouter>
  )
}

afterEach(() => {
  cleanup()
  vi.clearAllMocks()

  if (originalNastechDesktop) {
    desktopWindow.nastechDesktop = originalNastechDesktop
  } else {
    delete desktopWindow.nastechDesktop
  }
})

describe('WslgWindowControls', () => {
  it('routes minimize, maximize and close through the desktop bridge', () => {
    desktopWindow.nastechDesktop = { windowControls } as unknown as Window['nastechDesktop']

    renderControls()

    fireEvent.click(screen.getByRole('button', { name: 'Minimize window' }))
    fireEvent.click(screen.getByRole('button', { name: 'Maximize window' }))
    fireEvent.click(screen.getByRole('button', { name: 'Close window' }))

    // Argument-free on purpose: contextBridge structured-clones arguments and a
    // React SyntheticEvent is not cloneable, so passing the event would throw
    // before the IPC send and the buttons would silently do nothing.
    expect(windowControls.minimize).toHaveBeenCalledExactlyOnceWith()
    expect(windowControls.toggleMaximize).toHaveBeenCalledExactlyOnceWith()
    expect(windowControls.close).toHaveBeenCalledExactlyOnceWith()
  })

  it('exposes restore semantics while maximized', () => {
    desktopWindow.nastechDesktop = { windowControls } as unknown as Window['nastechDesktop']

    renderControls(true)

    expect(screen.getByRole('button', { name: 'Restore window' })).toBeTruthy()
  })

  it.each(['/settings', '/agents', '/command-center'])('keeps OS controls available on %s', path => {
    desktopWindow.nastechDesktop = { windowControls } as unknown as Window['nastechDesktop']

    renderControls(false, path)

    fireEvent.click(screen.getByRole('button', { name: 'Minimize window' }))
    fireEvent.click(screen.getByRole('button', { name: 'Maximize window' }))
    fireEvent.click(screen.getByRole('button', { name: 'Close window' }))
    expect(windowControls.minimize).toHaveBeenCalledExactlyOnceWith()
    expect(windowControls.toggleMaximize).toHaveBeenCalledExactlyOnceWith()
    expect(windowControls.close).toHaveBeenCalledExactlyOnceWith()
  })

  it('stays hidden while the BrowserWindow is fullscreen', () => {
    desktopWindow.nastechDesktop = { windowControls } as unknown as Window['nastechDesktop']

    renderControls(false, '/', true)

    expect(screen.queryByLabelText('Window controls')).toBeNull()
  })

  it('stops pointerdown propagation without cancelling the click', () => {
    desktopWindow.nastechDesktop = { windowControls } as unknown as Window['nastechDesktop']
    renderControls()
    const event = new MouseEvent('pointerdown', { bubbles: true, cancelable: true })

    const button = screen.getByRole('button', { name: 'Maximize window' })
    fireEvent(button, event)
    fireEvent.click(button)

    // preventDefault on pointerdown kills the synthesized click under WSLg's
    // RAIL compositor, so the button must NOT cancel the default — only stop
    // propagation so the drag region doesn't swallow the press.
    expect(event.defaultPrevented).toBe(false)
    expect(windowControls.toggleMaximize).toHaveBeenCalledOnce()
  })

  it('pins an explicit pixel height instead of the contextually-zeroed titlebar var', () => {
    desktopWindow.nastechDesktop = { windowControls } as unknown as Window['nastechDesktop']

    renderControls()

    // The contrib shell zeroes --titlebar-height for content subtrees; the
    // cluster must set its own height in px so the buttons don't collapse.
    const cluster = screen.getByLabelText('Window controls')
    expect(cluster.style.height).toMatch(/^\d+px$/)
    expect(cluster.className).not.toContain('h-(--titlebar-height)')
  })
})
