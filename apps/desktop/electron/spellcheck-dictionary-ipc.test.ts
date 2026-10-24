import type { IpcMainInvokeEvent } from 'electron'
import { describe, expect, it, vi } from 'vitest'

import { normalizeDictionaryWord, registerSpellcheckDictionaryIpc } from './spellcheck-dictionary-ipc'

type Handler = (event: IpcMainInvokeEvent, payload?: unknown) => unknown

function rig() {
  const handle = vi.fn<(channel: string, handler: Handler) => void>()

  const session = {
    addWordToSpellCheckerDictionary: vi.fn(() => true),
    removeWordFromSpellCheckerDictionary: vi.fn(() => true)
  }

  const event = { sender: { session } } as unknown as IpcMainInvokeEvent

  registerSpellcheckDictionaryIpc({ handle }, { fromId: () => undefined })

  const handler = handle.mock.calls.find(([channel]) => channel === 'nastech:spellcheck:dictionary')![1]
  const call = (payload: unknown) => handler(event, payload)

  return { call, session }
}

describe('normalizeDictionaryWord', () => {
  it('accepts one word of letters, marks, digits, apostrophes and hyphens', () => {
    expect(normalizeDictionaryWord('Nastech')).toBe('Nastech')
    expect(normalizeDictionaryWord('  naïve  ')).toBe('naïve')
    expect(normalizeDictionaryWord("don't")).toBe("don't")
    expect(normalizeDictionaryWord('re-run')).toBe('re-run')
    expect(normalizeDictionaryWord('GPT4o')).toBe('GPT4o')
  })

  it('refuses anything that is not exactly one bounded word', () => {
    for (const raw of [
      '',
      '   ',
      'two words',
      'line\nbreak',
      'tab\tbed',
      'nul\u0000',
      '1234',
      '--',
      '<script>',
      '-Nastech',
      "'Nastech'",
      'Nastech-',
      'a/b',
      'x'.repeat(65),
      42,
      null,
      undefined,
      { word: 'x' }
    ]) {
      expect(normalizeDictionaryWord(raw)).toBeNull()
    }
  })
})

describe('nastech:spellcheck:dictionary', () => {
  it("adds and removes a word on the sender's own session", async () => {
    const { call, session } = rig()

    expect(await call({ op: 'add', word: ' Nastech ' })).toBe(true)
    expect(session.addWordToSpellCheckerDictionary).toHaveBeenCalledWith('Nastech')

    expect(await call({ op: 'remove', word: 'Nastech' })).toBe(true)
    expect(session.removeWordFromSpellCheckerDictionary).toHaveBeenCalledWith('Nastech')
  })

  it('refuses an invalid word or an unknown op without touching the dictionary', async () => {
    const { call, session } = rig()

    expect(await call({ op: 'add', word: 'two words' })).toBe(false)
    expect(await call({ op: 'list', word: 'Nastech' })).toBe(false)
    expect(await call({ op: 'constructor', word: 'Nastech' })).toBe(false)
    expect(await call(undefined)).toBe(false)

    expect(session.addWordToSpellCheckerDictionary).not.toHaveBeenCalled()
    expect(session.removeWordFromSpellCheckerDictionary).not.toHaveBeenCalled()
  })

  it("reports Chromium's own verdict (false for an in-memory session)", async () => {
    const { call, session } = rig()

    session.addWordToSpellCheckerDictionary.mockReturnValue(false)

    expect(await call({ op: 'add', word: 'Nastech' })).toBe(false)
  })
})
