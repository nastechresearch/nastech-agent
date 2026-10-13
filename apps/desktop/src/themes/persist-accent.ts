import { setAccentOverride } from './accent-override'
import { normalizeHex } from './color'
import { nastechTheme } from './presets'
import { requestTheme } from './request'
import { retintTheme } from './retint'
import { installUserTheme } from './user-themes'

/**
 * Save an accent as the live profile's theme: a Nastech copy retinted to `accent`, installed as a user theme.
 * `null` or Nastech blue returns to the built-in Nastech theme. Clears the unsaved `$accentOverride` preview.
 * An unparseable colour changes nothing.
 */
export function persistAccent(accent: null | string): void {
  const hex = accent === null ? null : normalizeHex(accent)

  if (accent !== null && !hex) {
    return
  }

  const theme =
    hex === null || hex === normalizeHex(nastechTheme.colors.primary)
      ? nastechTheme
      : installUserTheme({
          ...retintTheme(nastechTheme, hex),
          name: `nastech-accent-${hex.slice(1)}`,
          label: `${nastechTheme.label} · ${hex}`
        })

  requestTheme(theme.name)
  setAccentOverride(null)
}
