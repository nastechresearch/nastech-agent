/**
 * Nastech Cloud agents: their public host is `<label>.agents.nastechresearch.github.io`
 * (staging `<label>.agents.staging-nastechresearch.github.io`), the URL the portal gives
 * each agent. Cloud updates an agent by replacing its image, so nothing may run
 * `nastech update` against one.
 */

const NASTECH_CLOUD_HOST_SUFFIXES = ['.agents.nastechresearch.github.io', '.agents.staging-nastechresearch.github.io']

/** Why an update target is skipped: the platform updates it. */
export const NASTECH_CLOUD_MANAGED = 'cloud-managed'

export function isNastechCloudUrl(url: null | string | undefined): boolean {
  if (!url) {
    return false
  }

  try {
    const host = new URL(url).hostname.toLowerCase()

    return NASTECH_CLOUD_HOST_SUFFIXES.some(suffix => host.endsWith(suffix))
  } catch {
    return false
  }
}
