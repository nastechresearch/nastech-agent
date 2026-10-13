import { vi } from 'vitest'

import type { NastechApiRequest } from '@/global'

/** Install a fake `window.nastechDesktop.api`, the preload bridge every REST helper sends through. */
export function installRestBridge(answer: (request: NastechApiRequest) => object) {
  const api = vi.fn(async (request: NastechApiRequest) => answer(request))

  Object.defineProperty(window, 'nastechDesktop', { configurable: true, value: { api } })

  return api
}
