/** The `nastech --tui` launcher's environment as `session.create` options and the launch tool-progress
 *  pin: Ink's launch contract, read here and handed to the shared gateway client. */
import type { GatewayRpc } from './app/interfaces.js'
import { t } from './i18n/runtime.js'

export function localCreationOptions(env = process.env): Record<string, unknown> {
  const fields: Record<string, string | undefined> = {
    model: env.NASTECH_MODEL, provider: env.NASTECH_TUI_PROVIDER, cwd: env.NASTECH_CWD
  }

  const options: Record<string, unknown> = Object.fromEntries(Object.entries(fields).filter(([, value]) => value))

  if (env.NASTECH_TUI_TOOLSETS) { options.toolsets = env.NASTECH_TUI_TOOLSETS.split(',') }

  // `nastech --tui -s a,b`: the owner renders these into the session's frozen prompt.
  const skills = [...new Set((env.NASTECH_TUI_SKILLS ?? '').split(/[,\n]/).map(name => name.trim()).filter(Boolean))]

  if (skills.length) { options.skills = skills }

  // The launcher's shell environment (allowlisted by `nastech --tui`): this session's NASTECH_* behaviour
  // values and tool PATH/venv on the shared gateway, as main's own process had them.
  const clientEnv = parseClientEnv(env.NASTECH_TUI_CLIENT_ENV)

  if (clientEnv) { options.client_env = clientEnv }

  // The launcher exports `--max-turns 5` as the string "5": numbers ride as
  // ints (0 / -1 = unlimited), and a word ("none", "unlimited") stays text
  // for the policy to read — `Number` would turn it into NaN, sent as null.
  if (env.NASTECH_TUI_MAX_TURNS) {
    const turns = Number(env.NASTECH_TUI_MAX_TURNS)
    options.max_turns = Number.isInteger(turns) ? turns : env.NASTECH_TUI_MAX_TURNS.trim()
  }

  // `nastech --tui --yolo` / `--ignore-rules` export NASTECH_YOLO_MODE / NASTECH_IGNORE_RULES (the in-process
  // TUI read them); over the canonical gateway they must ride session.create as frozen launch flags or the
  // session prompts anyway / still loads rules, SOUL, memory and skills.auto_load.
  const truthy = (value?: string) => ['1', 'true', 'yes', 'on'].includes((value ?? '').trim().toLowerCase())

  // `--checkpoints` / `--pass-session-id` / `--accept-hooks` (and an exported NASTECH_ACCEPT_HOOKS=1)
  // are this session's creation policy too: the owner applies them, nothing reads them in-process.
  for (const [field, value] of [
    ['yolo', env.NASTECH_YOLO_MODE], ['ignore_rules', env.NASTECH_IGNORE_RULES],
    ['safe_mode', env.NASTECH_SAFE_MODE], ['ignore_user_config', env.NASTECH_IGNORE_USER_CONFIG],
    ['checkpoints', env.NASTECH_TUI_CHECKPOINTS], ['pass_session_id', env.NASTECH_TUI_PASS_SESSION_ID],
    ['accept_hooks', env.NASTECH_ACCEPT_HOOKS]
  ] as const) {
    if (truthy(value)) { options[field] = true }
  }

  return options
}

/** Whether the launch's own `--provider` route can carry a session on a profile `setup.status` calls
 *  unconfigured (a keyless `providers:` endpoint saves no `model:` block). The owner's
 *  `setup.runtime_check` resolves that provider; it counts only with a model, the launch's `-m` or the
 *  profile's, since a session created without one cannot be restored (#146478). */
export async function launchRouteServes(rpc: GatewayRpc, env = process.env): Promise<boolean> {
  const { model, provider } = localCreationOptions(env)

  if (!provider) { return false }

  const check = await rpc<{ model?: null | string; ok?: boolean }>('setup.runtime_check', { provider })

  return Boolean(check?.ok && (model || check.model))
}

function parseClientEnv(raw?: string): Record<string, string> | undefined {
  if (!raw) { return undefined }

  try {
    const value: unknown = JSON.parse(raw)

    if (value && typeof value === 'object' && !Array.isArray(value)
      && Object.values(value).every(item => typeof item === 'string')) {
      return value as Record<string, string>
    }
  } catch {
    // An unreadable hand-off sends nothing: the session keeps the gateway's environment.
  }

  return undefined
}

const TOOL_PROGRESS_MODES = new Set(['off', 'new', 'all', 'verbose'])

/** `nastech --tui -v` / `-Q` export NASTECH_TUI_TOOL_PROGRESS (verbose / off). The owner carries it as the
 * session-scoped tool-progress mode (`config.set key=verbose`, the same control `/verbose` writes), so a
 * fresh session is pinned right after creation. An unreadable value refuses the launch, never drops it. */
export function launchToolProgress(env = process.env): string | undefined {
  const raw = env.NASTECH_TUI_TOOL_PROGRESS?.trim().toLowerCase()

  if (!raw) { return undefined }

  if (!TOOL_PROGRESS_MODES.has(raw)) { throw new Error(t('canonical.launch.invalidToolProgress', raw)) }

  return raw
}
