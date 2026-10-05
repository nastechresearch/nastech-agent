/**
 * NASTECH_DESKTOP_IGNORE_EXISTING=1 (`nastech desktop --ignore-existing`) keeps
 * Desktop off installed runtimes (ACTIVE_NASTECH_ROOT, or the install a
 * published user-bin launcher reports). Backend resolution
 * then falls through to bootstrap-needed, which shows the first-run choice
 * (connect a remote, or install) instead of starting a local serve.
 *
 * The bundled payload, NASTECH_DESKTOP_NASTECH_ROOT, an unpackaged checkout and
 * NASTECH_DESKTOP_NASTECH resolve before this rung and are not affected.
 *
 * A runtime this launch installed is always used. Skipping it would send the
 * post-install re-resolve (and every later resolve) back to the installer.
 */
export function createInstalledRuntimeGate(env: NodeJS.ProcessEnv, log: (message: string) => void) {
  let installedThisLaunch = false

  return {
    /** The ACTIVE_NASTECH_ROOT rung: probe the installed runtime unless the flag skips it. */
    async resolve<T>(root: string, probe: () => Promise<T | null>): Promise<T | null> {
      if (env.NASTECH_DESKTOP_IGNORE_EXISTING === '1' && !installedThisLaunch) {
        log(`[bootstrap] NASTECH_DESKTOP_IGNORE_EXISTING=1; skipping the installed runtime at ${root}`)

        return null
      }

      return probe()
    },

    /** Re-resolve after a successful bootstrap; the new runtime is exempt from the flag. */
    afterInstall<T>(resolveBackend: () => Promise<T>): Promise<T> {
      installedThisLaunch = true

      return resolveBackend()
    }
  }
}
