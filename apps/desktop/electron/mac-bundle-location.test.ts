import { describe, expect, it } from 'vitest'

import { ephemeralMacBundleLocation, isAppTranslocated, resolveMacAppBundle } from './mac-bundle-location'

describe('resolveMacAppBundle', () => {
  it('resolves packaged .app bundles on macOS including App Translocation paths', () => {
    expect(resolveMacAppBundle('/Applications/Nastech Agent.app/Contents/MacOS/Nastech Agent', 'darwin')).toBe(
      '/Applications/Nastech Agent.app'
    )
    expect(
      resolveMacAppBundle(
        '/private/var/folders/ab/cd/T/AppTranslocation/1F2E3D4C/d/Nastech Agent.app/Contents/MacOS/Nastech Agent',
        'darwin'
      )
    ).toBe('/private/var/folders/ab/cd/T/AppTranslocation/1F2E3D4C/d/Nastech Agent.app')
  })

  it('returns null off macOS or for non-bundle executables', () => {
    expect(resolveMacAppBundle('/Applications/Nastech Agent.app/Contents/MacOS/Nastech Agent', 'linux')).toBeNull()
    expect(resolveMacAppBundle('/Applications/Nastech Agent.app/Contents/MacOS/Nastech Agent', 'win32')).toBeNull()
    expect(resolveMacAppBundle('/usr/local/bin/electron', 'darwin')).toBeNull()
    expect(resolveMacAppBundle('', 'darwin')).toBeNull()
  })
})

describe('ephemeralMacBundleLocation', () => {
  const readOnly = () => {
    throw Object.assign(new Error('read-only file system'), { code: 'EROFS' })
  }

  it('reports a translocated copy and a read-only mount, and leaves a root-owned folder to Squirrel', () => {
    const translocated = '/private/var/folders/x/T/AppTranslocation/9A8B/d/Nastech Agent.app'

    expect(isAppTranslocated(translocated)).toBe(true)
    expect(ephemeralMacBundleLocation(translocated, () => undefined)).toBe('app-translocation')
    expect(ephemeralMacBundleLocation('/Volumes/Nastech Agent/Nastech Agent.app', readOnly)).toBe('read-only-volume')
    expect(
      ephemeralMacBundleLocation('/opt/nastech/Nastech Agent.app', () => {
        throw Object.assign(new Error('permission denied'), { code: 'EACCES' })
      })
    ).toBeNull()
  })

  it('knows nothing of the prompt-only Downloads and Desktop rules', () => {
    for (const folder of ['Downloads', 'Desktop']) {
      const bundle = `/Users/alice/${folder}/Nastech Agent.app`

      expect(isAppTranslocated(bundle)).toBe(false)
      expect(ephemeralMacBundleLocation(bundle, () => undefined)).toBeNull()
    }
  })
})
