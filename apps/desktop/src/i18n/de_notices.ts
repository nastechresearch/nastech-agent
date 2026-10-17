import { deSessionCommands } from './de_session_commands'
import type { TranslationOverrides } from './define-locale'

// Shell notices (remote-display toast, butterbar, keep-awake offer), spread into de.ts.
export const deNotices = {
  remoteDisplayBanner: {
    message: reason =>
      `Software-Rendering aktiv — Remote-Display erkannt (${reason}). GPU-Beschleunigung ist deaktiviert, um Flackern zu verhindern.`
  },
  butterbar: {
    goTo: (index, total) => `Hinweis ${index} von ${total} anzeigen`,
    legal: {
      before: 'Die Nutzung von Nastech Agent unterliegt unseren ',
      terms: 'Nutzungsbedingungen',
      between: ' und unserer ',
      privacy: 'Datenschutzerklärung',
      after: '.'
    }
  },
  promptNotices: {
    legacySendUnconfirmed:
      'Dieser Server konnte das frühere Senden dieser Nachricht nicht bestätigen; sie wurde möglicherweise bereits ausgeführt. Prüfe die Unterhaltung, bevor du sie erneut sendest.',
    mcpReloadDeferred:
      'Dieser Chat ist beschäftigt: Die MCP-Änderung gilt, sobald sein Durchlauf endet und MCP erneut geladen wird, oder wenn du den Chat wieder öffnest',
    mcpReloadNotInChat: server => `${server} ist in diesem Chat nicht aktiviert`,
    mcpReloadUnavailable: servers => `Keine Verbindung: ${servers}`,
    sessionCommands: deSessionCommands
  },
  keepAwakeOffer: {
    title: 'Ihr Computer ist eingeschlafen, während Nastech gearbeitet hat',
    message:
      'Nastech kann den Computer wach halten, solange eine Aufgabe läuft. Der Bildschirm schaltet sich weiterhin aus, und im Akkubetrieb kann der Computer trotzdem einschlafen.',
    action: 'Während der Arbeit wach halten'
  }
} satisfies Pick<TranslationOverrides, 'remoteDisplayBanner' | 'butterbar' | 'promptNotices' | 'keepAwakeOffer'>
