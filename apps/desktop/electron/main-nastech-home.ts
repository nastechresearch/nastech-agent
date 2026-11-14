// The Nastech home the desktop main process runs against, resolved once at boot.
// Resolving it here also registers it with the file-preview read guard, so the
// home's (and every profile's) credential stores are refused before any IPC
// read can be served.

import { resolveDesktopNastechHome } from './data-paths'
import { directoryExists } from './fs-probes'
import { setSensitiveNastechHome } from './hardening'
import { readWindowsUserEnvVar } from './windows-user-env'

export function resolveMainNastechHome(home: string): string {
  const nastechHome = resolveDesktopNastechHome({
    home,
    directoryExists,
    readWindowsHome: (): string | null => readWindowsUserEnvVar('NASTECH_HOME')
  })

  setSensitiveNastechHome(nastechHome)

  return nastechHome
}
