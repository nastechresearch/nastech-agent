import { describe, expect, it } from 'vitest'

import { commandLineIsNastechRuntime } from './nastech-process'

// HX003: process identity comes from a whole argv TOKEN, never an argv substring.
describe('commandLineIsNastechRuntime (HX003 token matching)', () => {
  it('matches a real Nastech gateway command line', () => {
    expect(commandLineIsNastechRuntime('nastech\0gateway\0run')).toBe(true)
    expect(commandLineIsNastechRuntime('nastech gateway run')).toBe(true)
    expect(commandLineIsNastechRuntime('nastech --profile work gateway run')).toBe(true)
  })

  it('matches a Nastech launched by an interpreter (basename of a path token)', () => {
    expect(commandLineIsNastechRuntime('/venv/bin/python\0/venv/bin/nastech\0gateway\0run')).toBe(true)
    expect(commandLineIsNastechRuntime('C:\\Nastech\\nastech.exe gateway run')).toBe(true)
  })

  // The bug this replaces: a bare `.includes('nastech')` matched any of these.
  it('does NOT match an unrelated process whose path merely contains "nastech"', () => {
    expect(commandLineIsNastechRuntime('vim /home/user/nastech-notes.txt')).toBe(false)
    expect(commandLineIsNastechRuntime('/opt/hermesbrew/bin/tool --run')).toBe(false)
    expect(commandLineIsNastechRuntime('node /srv/nastech-dashboard/server.js')).toBe(false)
    expect(commandLineIsNastechRuntime('cat ~/.nastech/config.yaml')).toBe(false)
  })

  // G2 (#150283): the real unmanaged-gateway launch is `python -m nastech_cli.main … gateway
  // run`, which the executable-basename-only matcher REJECTED — so findRunningGatewayProfiles
  // missed a live gateway at first launch / profile repair. Mirror the canonical Python matcher
  // (gateway.status.looks_like_gateway_command_line): recognize the module entry point, by argv
  // TOKENS not a substring, carrying the gateway subcommand.
  it('matches a module-launched gateway (python -m nastech_cli.main … gateway run)', () => {
    expect(commandLineIsNastechRuntime('python\0-m\0nastech_cli.main\0-p\0x\0gateway\0run')).toBe(true)
    expect(commandLineIsNastechRuntime('python -m nastech_cli.main -p x gateway run')).toBe(true)
    expect(commandLineIsNastechRuntime('/venv/bin/python /venv/lib/nastech_cli/main.py gateway run')).toBe(true)
    expect(commandLineIsNastechRuntime('python -m nastech_cli.main --profile work gateway run')).toBe(true)
  })

  it('does NOT match a module entry without the gateway subcommand, nor an unrelated nastech-tool path', () => {
    // A nastech_cli.main invocation that is not a gateway (e.g. `chat`) is not a running gateway.
    expect(commandLineIsNastechRuntime('python -m nastech_cli.main chat')).toBe(false)
    // HX003: no substring; an unrelated tool whose path contains "nastech" is never a runtime.
    expect(commandLineIsNastechRuntime('/opt/nastech-tool/foo gateway run')).toBe(false)
    // `-p gateway` is a profile value, not a subcommand.
    expect(commandLineIsNastechRuntime('python -m nastech_cli.main -p gateway chat')).toBe(false)
  })
})
