import { normalizeBasePath } from '@nastech/shared'

import { webappSessionKey } from '@/lib/browser-launch-session'

type WebappWindow = Window & { __NASTECH_BASE_PATH__?: string; __NASTECH_UI_SURFACE__?: string }

/**
 * A Webapp tab after its private launch link, on an unauthenticated bind: the browser host's only
 * credential, as `readWebappSession` reads it back. Seeds the grant for the base path the window
 * carries at call time, so set `__NASTECH_BASE_PATH__` first.
 */
export function seedWebappSession(token: string): void {
  const win = window as WebappWindow
  win.__NASTECH_UI_SURFACE__ = 'webapp'
  sessionStorage.setItem(webappSessionKey(normalizeBasePath(win.__NASTECH_BASE_PATH__)), token)
}

export function clearWebappSession(): void {
  delete (window as WebappWindow).__NASTECH_UI_SURFACE__

  for (const key of Object.keys(sessionStorage)) {
    if (key.startsWith('nastech.webapp.session.v1:')) {sessionStorage.removeItem(key)}
  }
}
