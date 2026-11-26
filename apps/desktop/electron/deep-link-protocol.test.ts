import assert from 'node:assert/strict'

import { test } from 'vitest'

import { handleLaunchDeepLink, registerDeepLinkProtocol } from './deep-link-protocol'

function run(env: NodeJS.ProcessEnv, defaultApp = true) {
  const calls: unknown[][] = []
  const log: string[] = []
  registerDeepLinkProtocol({
    app: { setAsDefaultProtocolClient: (...args: unknown[]) => { calls.push(args);

 return true } },
    protocol: 'nastech',
    env,
    defaultApp,
    argv: ['/electron', '.'],
    execPath: '/electron',
    resolve: entry => `/checkout/${entry}`,
    log: line => log.push(line)
  })

  return { calls, log }
}

test('the E2E/dev guard leaves the OS nastech:// handler untouched; normal launches still register', () => {
  const skipped = run({ NASTECH_DESKTOP_SKIP_PROTOCOL_REGISTRATION: '1' })
  assert.deepEqual(skipped.calls, [])
  assert.match(skipped.log.join('\n'), /registration skipped/)

  assert.deepEqual(run({}).calls, [['nastech', '/electron', ['/checkout/.']]])
  assert.deepEqual(run({}, false).calls, [['nastech']])
})

function launch(url: string, ready = true) {
  let activated = 0
  const handled = handleLaunchDeepLink(url, ['nastech-dev', 'nastech'], { ready, activate: () => { activated += 1 } })

  return { handled, activated }
}

test('nastech://launch only focuses the app, whatever it carries, malformed tails included', () => {
  for (const url of ['nastech://launch', 'nastech://launch/', 'nastech://launch/chat/new?prompt=rm%20-rf', 'nastech://launch/%', 'nastech-dev://launch?x=1']) {
    assert.deepEqual(launch(url), { handled: true, activated: 1 }, url)
  }

  // A window still booting reveals itself; the link is consumed without an early show.
  assert.deepEqual(launch('nastech://launch', false), { handled: true, activated: 0 })

  for (const url of ['nastech://', 'nastech://open/launch', 'nastech://plugin/install?repo=launch', 'nastech://launcher', 'nastech://close-preview', 'other://launch', 'not a url']) {
    assert.deepEqual(launch(url), { handled: false, activated: 0 }, url)
  }
})
