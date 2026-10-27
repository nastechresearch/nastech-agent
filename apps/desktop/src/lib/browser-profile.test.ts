import { afterEach, beforeEach, expect, it, vi } from 'vitest'

import { $connection } from '@/store/session'
import { clearWebappSession, seedWebappSession } from '@/test/webapp-session'
import { browserOpensWebappWindows } from '@/test/webapp-windows'

import { installBrowserDesktopBridge } from './browser-desktop-bridge'

const bootstrap = window as Window & {
  __NASTECH_AUTH_REQUIRED__?: boolean
  __NASTECH_BASE_PATH__?: string
}

beforeEach(() => {
  window.localStorage.clear()
  bootstrap.__NASTECH_BASE_PATH__ = '/nastech'
  seedWebappSession('test-session')
  window.history.replaceState(null, '', '/nastech?profile=active#/session-1')
})

afterEach(() => {
  Reflect.deleteProperty(window, 'nastechDesktop')
  delete bootstrap.__NASTECH_AUTH_REQUIRED__
  delete bootstrap.__NASTECH_BASE_PATH__
  clearWebappSession()
  document.documentElement.removeAttribute('data-nastech-desktop-host')
  window.localStorage.clear()
  window.history.replaceState(null, '', '/#/')
  $connection.set(null)
  vi.restoreAllMocks()
})

it('persists the default separately from the active chat and synchronizes only the same server across tabs', async () => {
  expect(installBrowserDesktopBridge()).toBe(true)
  const profile = window.nastechDesktop.profile
  const originalUrl = window.location.href
  const changed = vi.fn()
  const unsubscribe = profile.onDefaultChanged(changed)
  const route = { connectionId: 'local', profile: 'research' }

  await expect(profile.setDefault(route)).resolves.toEqual(route)
  expect(window.location.href).toBe(originalUrl)
  await expect(profile.get()).resolves.toEqual({ profile: 'active' })
  expect(changed).toHaveBeenLastCalledWith(route)
  await profile.remember('work')
  await expect(profile.getDefault()).resolves.toEqual(route)

  Reflect.deleteProperty(window, 'nastechDesktop')
  expect(installBrowserDesktopBridge()).toBe(true)
  await expect(window.nastechDesktop.profile.getDefault()).resolves.toEqual(route)
  Reflect.deleteProperty(window, 'nastechDesktop')
  bootstrap.__NASTECH_BASE_PATH__ = '/another-server'
  expect(installBrowserDesktopBridge()).toBe(true)
  await expect(window.nastechDesktop.profile.getDefault()).resolves.toBeNull()

  const key = window.localStorage.key(0)!
  const updated = { ...route, profile: 'review' }
  window.localStorage.setItem(key, JSON.stringify(updated))
  const storageEvent = () => Object.assign(new Event('storage'), { key, storageArea: window.localStorage })
  window.dispatchEvent(storageEvent())
  expect(changed).toHaveBeenLastCalledWith(updated)
  unsubscribe()
  changed.mockClear()
  window.dispatchEvent(storageEvent())
  expect(changed).not.toHaveBeenCalled()
})

it('records a live profile pick in the URL without dropping the router entry state', async () => {
  const entry = { idx: 3, key: 'entry', usr: { from: 'sidebar' } }
  window.history.replaceState(entry, '', '/nastech?profile=active#/session-1')
  expect(installBrowserDesktopBridge()).toBe(true)

  await window.nastechDesktop.profile.remember('work')

  expect(new URLSearchParams(window.location.search).get('profile')).toBe('work')
  expect(window.location.hash).toBe('#/session-1')
  expect(window.history.state).toEqual(entry)
})

it('opens the requested profile on this host without carrying another session or spectator flags', async () => {
  // A gated host opens the window directly; a launch-link tab hands it a session first.
  bootstrap.__NASTECH_AUTH_REQUIRED__ = true
  window.history.replaceState(null, '', '/nastech?profile=active&win=secondary&watch=1#/session-1')
  const { open } = browserOpensWebappWindows()
  expect(installBrowserDesktopBridge()).toBe(true)

  const originalUrl = window.location.href
  await window.nastechDesktop.openWindow()
  const peer = new URL(String(open.mock.calls[0][0]))
  expect(peer.searchParams.get('profile')).toBe('active')
  expect(peer.searchParams.has('watch')).toBe(false)
  expect(peer.searchParams.has('win')).toBe(false)
  expect(peer.hash).toBe('#/')
  expect(window.location.href).toBe(originalUrl)
  open.mockClear()

  await window.nastechDesktop.openWindow({ connectionId: 'local', profile: 'research' })
  const target = new URL(String(open.mock.calls[0][0]))
  expect(target.origin).toBe(window.location.origin)
  expect(target.pathname).toBe('/nastech')
  expect(target.searchParams.get('profile')).toBe('research')
  expect(target.searchParams.has('watch')).toBe(false)
  expect(target.searchParams.has('win')).toBe(false)
  expect(target.hash).toBe('#/')

  await window.nastechDesktop.openWindow({ connectionId: null, profile: 'default' })
  expect(new URL(String(open.mock.calls[1][0])).searchParams.get('profile')).toBe('default')
  open.mockClear()
  await expect(window.nastechDesktop.openWindow({ connectionId: 'another-host', profile: 'research' })).rejects.toThrow(
    'No connection with id'
  )
  await expect(
    window.nastechDesktop.profile.setDefault({ connectionId: 'another-host', profile: 'research' })
  ).rejects.toThrow('No connection with id')
  expect(open).not.toHaveBeenCalled()
})
