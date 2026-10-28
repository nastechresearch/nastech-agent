// Wires the machine's UI preferences store (ui-preferences.ts) into Electron:
// every app window hears about a change, whoever made it.
import { BrowserWindow, ipcMain } from 'electron'

import { registerUiPreferencesIpc } from './ui-preferences'

/** `nastechHome` is main's resolved ROOT home (never a profile's), the one the
 *  Webapp's Python server resolves too. */
export function registerMachineUiPreferences(nastechHome: string): () => void {
  return registerUiPreferencesIpc({
    ipcMain,
    nastechHome,
    broadcast: snapshot => {
      for (const window of BrowserWindow.getAllWindows()) {
        window.webContents.send('nastech:ui-preferences:changed', snapshot)
      }
    }
  })
}
