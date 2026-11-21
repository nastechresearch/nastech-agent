import assert from 'node:assert/strict'

import { test } from 'vitest'

import { hasWindowsPathPrefix, isExternalVenvHolder, isNastechOwnedVenvDaemon } from './venv-holder-select'

const SCRIPTS = 'C:\\Nastech\\venv\\Scripts'

test('matches the hindsight daemon shim (exe under venv Scripts + hindsight cmdline)', () => {
  assert.equal(
    isNastechOwnedVenvDaemon(
      'C:\\Nastech\\venv\\Scripts\\pythonw.exe',
      'C:\\Nastech\\venv\\Scripts\\pythonw.exe -m hindsight_api.main --daemon --idle-timeout 300 --port 9177',
      SCRIPTS
    ),
    true
  )
})

test('Windows path prefix match is ordinal case-insensitive', () => {
  assert.equal(
    isNastechOwnedVenvDaemon(
      'c:\\nastech\\venv\\scripts\\python.exe',
      'python.exe -m hindsight_api.main --daemon',
      'C:\\Nastech\\venv\\Scripts'
    ),
    true
  )
})

test('excludes external venv holders that are not the hindsight daemon', () => {
  // a user terminal running the nastech CLI from the venv — must NOT be killed
  assert.equal(
    isNastechOwnedVenvDaemon('C:\\Nastech\\venv\\Scripts\\nastech.exe', 'nastech chat -q "hi"', SCRIPTS),
    false
  )
  // an unrelated python script using the venv interpreter
  assert.equal(
    isNastechOwnedVenvDaemon('C:\\Nastech\\venv\\Scripts\\python.exe', 'python C:\\tools\\import.py', SCRIPTS),
    false
  )
})

test('excludes exes outside the venv even when the cmdline mentions hindsight', () => {
  assert.equal(
    isNastechOwnedVenvDaemon('C:\\Other\\pythonw.exe', 'pythonw -m hindsight_api.main --daemon', SCRIPTS),
    false
  )
})

test('prefix boundary: sibling dirs (ScriptsX) do not match', () => {
  assert.equal(hasWindowsPathPrefix('C:\\Nastech\\venv\\ScriptsX\\python.exe', SCRIPTS), false)
  assert.equal(hasWindowsPathPrefix('C:\\Nastech\\venv\\Scripts\\python.exe', SCRIPTS), true)
})

test('null/undefined fields never match', () => {
  assert.equal(isNastechOwnedVenvDaemon(null, 'x', SCRIPTS), false)
  assert.equal(isNastechOwnedVenvDaemon('C:\\Nastech\\venv\\Scripts\\pythonw.exe', null, SCRIPTS), false)
  assert.equal(isNastechOwnedVenvDaemon(undefined, undefined, SCRIPTS), false)
})

// --- isExternalVenvHolder (#62311) ------------------------------------------

test('matches the autostart gateway shim (nastech.exe under venv Scripts)', () => {
  assert.equal(
    isExternalVenvHolder(
      'C:\\Nastech\\venv\\Scripts\\nastech.exe',
      '"C:\\Nastech\\venv\\Scripts\\nastech.exe" gateway run --external-supervisor',
      SCRIPTS
    ),
    true
  )
})

test('matches the dashboard scheduled task (python -m nastech_cli / -m nastech)', () => {
  assert.equal(
    isExternalVenvHolder(
      'C:\\Nastech\\venv\\Scripts\\python.exe',
      '"C:\\Nastech\\venv\\Scripts\\python.exe" -m nastech_cli.main dashboard',
      SCRIPTS
    ),
    true
  )
  assert.equal(
    isExternalVenvHolder('C:\\Nastech\\venv\\Scripts\\pythonw.exe', 'pythonw.exe -m nastech serve', SCRIPTS),
    true
  )
})

test('never matches an unrelated process that merely borrows the venv interpreter', () => {
  // a user's own script running on the venv python — NOT Nastech, must NOT be killed
  assert.equal(
    isExternalVenvHolder('C:\\Nastech\\venv\\Scripts\\python.exe', 'python C:\\tools\\import.py', SCRIPTS),
    false
  )
  // hindsight daemon is selected by isNastechOwnedVenvDaemon, not here
  assert.equal(
    isExternalVenvHolder('C:\\Nastech\\venv\\Scripts\\pythonw.exe', 'pythonw -m hindsight_api.main --daemon', SCRIPTS),
    false
  )
})

test('never matches a process outside the venv, even with nastech in the cmdline', () => {
  // an editor / shell whose command line mentions the install root (#62445 regression guard)
  assert.equal(
    isExternalVenvHolder('C:\\Windows\\System32\\cmd.exe', 'cmd /c cd C:\\Nastech\\venv\\Scripts && dir', SCRIPTS),
    false
  )
  assert.equal(isExternalVenvHolder('C:\\Other\\nastech.exe', 'nastech gateway run', SCRIPTS), false)
})

test('sibling-dir and boundary safety for the external selector', () => {
  assert.equal(isExternalVenvHolder('C:\\Nastech\\venv\\ScriptsX\\nastech.exe', 'nastech gateway run', SCRIPTS), false)
  assert.equal(isExternalVenvHolder(null, 'nastech gateway run', SCRIPTS), false)
  assert.equal(isExternalVenvHolder('C:\\Nastech\\venv\\Scripts\\nastech.exe', null, SCRIPTS), false)
})
