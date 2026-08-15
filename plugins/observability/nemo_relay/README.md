# NeMo Relay Observability

Optional Nastech observability plugin that configures exporters and maps
Nastech-specific observer hooks to NeMo Relay marks and ATIF state. Nastech core
owns Relay session, turn, LLM, and tool execution scopes.

NeMo Relay is NVIDIA's runtime layer for agent execution boundaries. It does
not replace Nastech Agent's planner, tools, memory, model provider routing, or
CLI UX. Nastech core emits NeMo Relay lifecycle events for provider and tool
execution, while this plugin enables rich exporters and observer marks for
sessions, turns, approval prompts, and delegated subagents.

With this plugin enabled, Nastech Agent can:

- Export the Relay scopes and LLM/tool lifecycles emitted by Nastech core.
- Add Nastech session, turn, approval, and subagent mark events.
- Export raw lifecycle events as Agent Trajectory Observability Format (ATOF)
  JSONL for debugging and offline inspection.
- Export Agent Trajectory Interchange Format (ATIF) trajectories for replay,
  evaluation, and harness analysis workflows.
- Correlate parent sessions, delegated subagents, tool calls, and provider
  calls through shared session, turn, and trajectory metadata.

See the NeMo Relay overview for the broader runtime model:
https://docs.nvidia.com/nemo/relay/about-nemo-relay/overview

ATOF is NVIDIA's canonical JSONL event stream representation for NeMo Relay
lifecycle events. The format is documented in the NeMo Agent Toolkit:
https://github.com/NVIDIA/NeMo-Agent-Toolkit/blob/develop/packages/nvidia_nat_atif/atof-event-format.md

ATIF is the trajectory representation produced from those events. NVIDIA and
Harbor upstreamed ATIF v1.7 support for complex harness workflows, including
subagent trajectory embedding, trajectory IDs, multi-LLM-call step metadata, and
deterministic no-LLM orchestration steps:
https://github.com/harbor-framework/harbor/blob/main/rfcs/0001-trajectory-format.md

## Enablement

Enable the plugin before setting export options:

```bash
nastech plugins enable observability/nemo_relay
```

The `NASTECH_NEMO_RELAY_*` environment variables below only configure an
already-enabled plugin. They do not enable plugin discovery by themselves.

For isolated test homes, enable the plugin in the same `NASTECH_HOME` that the
agent run will use:

```bash
env NASTECH_HOME=/tmp/nastech-nemo-relay-test \
  nastech plugins enable observability/nemo_relay
```

Runs started with `--ignore_user_config` skip the enabled-plugin state from
`NASTECH_HOME`, so local E2E tests should omit that flag unless the test harness
loads `observability/nemo_relay` explicitly another way.

`NASTECH_HOME` is the Nastech profile/config home used by both
`nastech plugins enable ...` and the later `nastech chat ...` run. If unset,
Nastech uses the user's default home, usually `~/.nastech`. For isolated smoke
tests, choose any writable temporary directory and use the same value for every
command in that test:

```bash
export NASTECH_HOME=/tmp/nastech-nemo-relay-test
nastech plugins enable observability/nemo_relay
nastech chat --query 'Reply exactly ok' --provider custom --model qwen3.6:35b
```

For source checkouts, make sure the `nastech` command you run is built from the
checkout that contains this plugin. A globally installed older CLI will not see
new bundled plugins from your working tree.

```bash
uv sync
uv run nastech plugins enable observability/nemo_relay
uv run nastech chat --query 'Reply exactly ok' --provider custom --model qwen3.6:35b
```

To ship the updated CLI into another environment, build and install a fresh
wheel from this checkout. On platforms for which Relay publishes a native
wheel, Nastech installs its supported NeMo Relay runtime as a normal dependency:

```bash
uv build --wheel
python -m pip install --force-reinstall dist/nastech_agent-*.whl
nastech plugins enable observability/nemo_relay
```

The plugin remains opt-in even though the runtime dependency is installed by
default. Enabling this plugin controls rich observability and adaptive
behavior; it does not control Nastech shared client metrics.

## Session-Span Segmentation (Continuous Sessions)

Relay export is close-driven: a span exports when its scope pops. Continuous
gateway sessions keep the session scope open indefinitely, so the session root
span and session-level marks stay unexported until `/new` or idle-end, and a
crash loses the open segment. Opt-in segmentation rotates the session scope at
turn boundaries via `config.yaml`:

```yaml
gateway:
  telemetry:
    session_segments:
      on_compaction: false   # rotate when the session compacts
      max_turns: 0           # 0 = unlimited; N = rotate after N turns
```

Both defaults are off (no rotation — identical to previous behavior). Rotated
segments share the `session_id` attribute and carry
`nastech.session.segment` / `nastech.session.segment_reason`
(`compaction` | `max_turns`) metadata. Rotation only happens at turn
boundaries, never mid-turn. See the built-in plugins page on the docs site for
the full behavior table.

## Export Configuration

The plugin can configure exporters directly from `NASTECH_NEMO_RELAY_*`
environment variables, or delegate exporter setup to a NeMo Relay
`plugins.toml` component config.

Use environment variables for local smoke tests, CI jobs, and one-off CLI
runs. Use `plugins.toml` when you want one NeMo Relay configuration document to
own observability components such as ATOF, ATIF, OpenTelemetry, and
OpenInference.

### Environment Variables

Useful local export settings after the plugin is enabled:

```bash
export NASTECH_NEMO_RELAY_ATOF_ENABLED=1
export NASTECH_NEMO_RELAY_ATOF_OUTPUT_DIRECTORY=.nemo-relay/atof
export NASTECH_NEMO_RELAY_ATIF_ENABLED=1
export NASTECH_NEMO_RELAY_ATIF_OUTPUT_DIRECTORY=.nemo-relay/atif
```

Optional overrides:

- `NASTECH_NEMO_RELAY_ATOF_FILENAME`
- `NASTECH_NEMO_RELAY_ATOF_MODE` (`append` or `overwrite`)
- `NASTECH_NEMO_RELAY_ATIF_FILENAME_TEMPLATE`
- `NASTECH_NEMO_RELAY_ATIF_AGENT_NAME`
- `NASTECH_NEMO_RELAY_ATIF_AGENT_VERSION`
- `NASTECH_NEMO_RELAY_ATIF_MODEL_NAME`
- `NASTECH_NEMO_RELAY_ATIF_SUBAGENT_EXPORT_MODE` (`embedded` by default; set `all` to also write standalone child files)

### NeMo Relay Component Config

To initialize NeMo Relay from a component config, create a `plugins.toml` file
and point Nastech at it:

```bash
export NASTECH_NEMO_RELAY_PLUGINS_TOML=.nemo-relay/plugins.toml
```

Minimal ATOF and ATIF config:

```toml
version = 1

[[components]]
kind = "observability"
enabled = true

[components.config]
version = 1

[components.config.atof]
enabled = true
output_directory = ".nemo-relay/atof"
filename = "events.jsonl"
mode = "overwrite"

[components.config.atif]
enabled = true
output_directory = ".nemo-relay/atif"
filename_template = "trajectory-{session_id}.json"
agent_name = "Nastech Agent"
agent_version = "local"
```

When `NASTECH_NEMO_RELAY_PLUGINS_TOML` is set and initializes successfully, NeMo
Relay owns exporter lifecycle through that config. The direct
`NASTECH_NEMO_RELAY_ATOF_*` fallback setup is skipped. If the same
`plugins.toml` observability config enables `atif`, the direct
`NASTECH_NEMO_RELAY_ATIF_*` fallback setup is also skipped so Nastech does not
double-export trajectories on teardown. If `plugins.toml` initialization fails,
Nastech keeps the direct env-var fallbacks active for that run.

Nastech core routes provider and tool execution through NeMo Relay managed APIs
regardless of whether this plugin is enabled. To install adaptive interceptors
on those boundaries, include an adaptive component in the same `plugins.toml`:

```toml
[[components]]
kind = "adaptive"
enabled = true

[components.config.tool_parallelism]
mode = "observe_only"
```

The observer hooks emit session, turn, approval, and subagent marks. They do not
create a second LLM or tool lifecycle. `tool_parallelism.mode = "observe_only"`
keeps tool scheduling observational while still intercepting the core-managed
execution boundary.

### Dynamic Plugins

Nastech uses the dynamic-plugin activation API available in NeMo Relay 0.6 and
later. Configure native or worker plugins with Nastech-owned
`[[dynamic_plugins]]` entries that match the Python binding's activation-spec
fields:

```toml
[[dynamic_plugins]]
plugin_id = "example-plugin"
kind = "rust_dynamic"
manifest_ref = "./example-plugin/relay-plugin.toml"

[dynamic_plugins.config]
mode = "enabled"
```

For a worker plugin, also provide the lifecycle-managed `environment_ref`:

```toml
[[dynamic_plugins]]
plugin_id = "example-worker"
kind = "worker"
manifest_ref = "./example-worker/relay-plugin.toml"
environment_ref = "/absolute/path/from-nemo-relay-plugins-inspect"

[dynamic_plugins.config]
mode = "enabled"
```

Provision the worker first with `nemo-relay plugins add`, then copy
`data.source.environment_ref` from the JSON output of
`nemo-relay plugins inspect <plugin-id> --json`. Relay rejects arbitrary Python
environments at activation time.

Relative `manifest_ref` and `environment_ref` values resolve relative to the
physical `plugins.toml` file.

Relay's canonical gateway `[[plugins.dynamic]]` records are not interchangeable
with this Nastech-owned section. The gateway combines those records with
separate lifecycle state for enablement, trust policy, and worker environments;
the Python binding does not yet expose that resolver. Nastech rejects
`[[plugins.dynamic]]` with an actionable diagnostic instead of silently
ignoring it or bypassing lifecycle policy. Use `[[dynamic_plugins]]` until Relay
exposes shared file-and-lifecycle resolution to embedding hosts.

Nastech activates these plugins before registering its managed LLM and tool
execution middleware and retains the activation for the runtime lifetime.
During shutdown it closes session exporters, flushes Relay subscribers, and
then closes the activation so callbacks are removed before plugin code is
unloaded.

For the full generic Nastech middleware contract, see
[`docs/middleware/README.md`](../../../docs/middleware/README.md).

## Canonical Local Examples

The observe-only examples in this section use the NeMo Relay runtime installed
with Nastech and a local Ollama model served through the OpenAI-compatible API.

```bash
export NASTECH_HOME=/tmp/nastech-nemo-relay-docs/nastech-home
mkdir -p "$NASTECH_HOME"

cat > "$NASTECH_HOME/config.yaml" <<'YAML'
model:
  provider: custom
  default: qwen3.6:35b
  base_url: http://127.0.0.1:11434/v1
  api_key: ollama
plugins:
  enabled:
    - observability/nemo_relay
delegation:
  max_spawn_depth: 2
  max_concurrent_children: 2
  child_timeout_seconds: 180
  model: qwen3.6:35b
  provider: custom
  base_url: http://127.0.0.1:11434/v1
  api_key: ollama
YAML
```

### Delegated Subagent Tool Call

This run starts a parent Nastech session, delegates to a child subagent, has the
child call `terminal`, and writes both ATOF and ATIF.

```bash
export NASTECH_NEMO_RELAY_ATOF_ENABLED=1
export NASTECH_NEMO_RELAY_ATOF_OUTPUT_DIRECTORY=/tmp/nastech-nemo-relay-docs/subagent/atof
export NASTECH_NEMO_RELAY_ATOF_FILENAME=nested-subagent-atof.jsonl
export NASTECH_NEMO_RELAY_ATOF_MODE=overwrite
export NASTECH_NEMO_RELAY_ATIF_ENABLED=1
export NASTECH_NEMO_RELAY_ATIF_OUTPUT_DIRECTORY=/tmp/nastech-nemo-relay-docs/subagent/atif
export NASTECH_NEMO_RELAY_ATIF_FILENAME_TEMPLATE='nested-subagent-atif-{session_id}.json'
export NASTECH_NEMO_RELAY_ATIF_AGENT_NAME='Nastech Agent E2E'
export NASTECH_NEMO_RELAY_ATIF_AGENT_VERSION=docs-example
export NASTECH_NEMO_RELAY_ATIF_SUBAGENT_EXPORT_MODE=all

nastech chat \
  --query 'Use delegate_task exactly once. Ask the child subagent to use the terminal tool exactly once to run printf docs_nested_leaf_function. After the child returns, reply with exactly: parent received nested subagent result.' \
  --provider custom \
  --model qwen3.6:35b \
  --toolsets delegation,terminal \
  --max-turns 10 \
  --quiet \
  --accept-hooks
```

CLI output:

```text
session_id: docs-parent-session
parent received nested subagent result.
```

Sanitized ATOF excerpt:

```jsonl
{"kind":"scope","category":"tool","name":"delegate_task","scope_category":"start","metadata":{"session_id":"docs-parent-session","tool_call_id":"call_delegate"},"data":{"goal":"Run the command `printf docs_nested_leaf_function` using the terminal tool.","toolsets":["terminal"]}}
{"kind":"mark","name":"nastech.subagent.start","metadata":{"parent_session_id":"docs-parent-session","session_id":"docs-child-session","subagent_id":"sa-0-docs","child_role":"leaf"}}
{"kind":"scope","category":"tool","name":"terminal","scope_category":"end","metadata":{"session_id":"docs-child-session","tool_call_id":"call_terminal","status":"ok"},"data":"{\"output\":\"docs_nested_leaf_function\",\"exit_code\":0,\"error\":null}"}
{"kind":"scope","category":"tool","name":"delegate_task","scope_category":"end","metadata":{"session_id":"docs-parent-session","tool_call_id":"call_delegate","status":"ok"}}
```

Sanitized ATIF excerpt:

```json
{
  "schema_version": "ATIF-v1.7",
  "session_id": "docs-parent-session",
  "agent": {"name": "Nastech Agent E2E", "version": "docs-example", "model_name": "qwen3.6:35b"},
  "steps": [
    {
      "source": "agent",
      "tool_calls": [{"function_name": "delegate_task"}],
      "observation": {
        "results": [
          {
            "subagent_trajectory_ref": [{"session_id": "docs-child-session"}],
            "content": "{\"results\":[{\"status\":\"completed\",\"tool_trace\":[{\"tool\":\"terminal\",\"status\":\"ok\"}]}]}"
          }
        ]
      }
    },
    {"source": "agent", "message": "parent received nested subagent result."}
  ],
  "subagent_trajectories": [
    {
      "session_id": "docs-child-session",
      "steps": [
        {
          "source": "agent",
          "tool_calls": [{"function_name": "terminal", "arguments": {"command": "printf docs_nested_leaf_function"}}],
          "observation": {"results": [{"content": "{\"output\":\"docs_nested_leaf_function\",\"exit_code\":0,\"error\":null}"}]}
        }
      ]
    }
  ]
}
```

### Parallel Tool Calls

This run asks the model to emit two `read_file` tool calls in the same assistant
message. Nastech dispatches the read-only tools as one batch, and NeMo Relay
records both tool invocations.

```bash
mkdir -p /tmp/nastech-nemo-relay-docs/workdir
printf 'docs_parallel_alpha_function\n' > /tmp/nastech-nemo-relay-docs/workdir/alpha.txt
printf 'docs_parallel_beta_function\n' > /tmp/nastech-nemo-relay-docs/workdir/beta.txt
cd /tmp/nastech-nemo-relay-docs/workdir

export NASTECH_NEMO_RELAY_ATOF_ENABLED=1
export NASTECH_NEMO_RELAY_ATOF_OUTPUT_DIRECTORY=/tmp/nastech-nemo-relay-docs/parallel/atof
export NASTECH_NEMO_RELAY_ATOF_FILENAME=parallel-tools-atof.jsonl
export NASTECH_NEMO_RELAY_ATOF_MODE=overwrite
export NASTECH_NEMO_RELAY_ATIF_ENABLED=1
export NASTECH_NEMO_RELAY_ATIF_OUTPUT_DIRECTORY=/tmp/nastech-nemo-relay-docs/parallel/atif
export NASTECH_NEMO_RELAY_ATIF_FILENAME_TEMPLATE='parallel-tools-atif-{session_id}.json'
export NASTECH_NEMO_RELAY_ATIF_AGENT_NAME='Nastech Agent E2E'
export NASTECH_NEMO_RELAY_ATIF_AGENT_VERSION=docs-example

nastech chat \
  --query 'Use exactly two read_file tool calls in the same assistant message. Read alpha.txt and beta.txt. Do not call terminal. After both tool results are available, reply with exactly: parallel tools complete.' \
  --provider custom \
  --model qwen3.6:35b \
  --toolsets file \
  --max-turns 8 \
  --quiet \
  --accept-hooks
```

CLI output:

```text
session_id: docs-parallel-session
parallel tools complete.
```

Sanitized ATOF excerpt:

```jsonl
{"kind":"scope","category":"llm","name":"custom","scope_category":"end","data":{"assistant_message":{"tool_calls":[{"id":"call_alpha","name":"read_file","arguments":"{\"path\":\"alpha.txt\"}"},{"id":"call_beta","name":"read_file","arguments":"{\"path\":\"beta.txt\"}"}]},"finish_reason":"tool_calls"}}
{"kind":"scope","category":"tool","name":"read_file","scope_category":"start","timestamp":"2026-05-31T00:15:08.956732+00:00","metadata":{"session_id":"docs-parallel-session","tool_call_id":"call_alpha"},"data":{"path":"alpha.txt"}}
{"kind":"scope","category":"tool","name":"read_file","scope_category":"start","timestamp":"2026-05-31T00:15:08.956804+00:00","metadata":{"session_id":"docs-parallel-session","tool_call_id":"call_beta"},"data":{"path":"beta.txt"}}
{"kind":"scope","category":"tool","name":"read_file","scope_category":"end","metadata":{"session_id":"docs-parallel-session","tool_call_id":"call_beta","status":"ok"},"data":"{\"content\":\"     1|docs_parallel_beta_function\\n\"}"}
{"kind":"scope","category":"tool","name":"read_file","scope_category":"end","metadata":{"session_id":"docs-parallel-session","tool_call_id":"call_alpha","status":"ok"},"data":"{\"content\":\"     1|docs_parallel_alpha_function\\n\"}"}
```

Sanitized ATIF excerpt:

```json
{
  "schema_version": "ATIF-v1.7",
  "session_id": "docs-parallel-session",
  "agent": {"name": "Nastech Agent E2E", "version": "docs-example", "model_name": "qwen3.6:35b"},
  "steps": [
    {
      "source": "agent",
      "tool_calls": [
        {"tool_call_id": "call_alpha", "function_name": "read_file", "arguments": {"path": "alpha.txt"}},
        {"tool_call_id": "call_beta", "function_name": "read_file", "arguments": {"path": "beta.txt"}}
      ],
      "observation": {
        "results": [
          {"source_call_id": "call_beta", "content": "{\"content\":\"     1|docs_parallel_beta_function\\n\"}"},
          {"source_call_id": "call_alpha", "content": "{\"content\":\"     1|docs_parallel_alpha_function\\n\"}"}
        ]
      }
    },
    {"source": "agent", "message": "parallel tools complete."}
  ]
}
```

## ATOF Mapping

The plugin keeps NeMo Relay's native event model:

- Nastech sessions map to `agent` scopes.
- Nastech core managed provider calls map to `llm` scope start/end events.
- Nastech core managed tool calls map to `tool` scope start/end events.
- Turn, approval, subagent, and diagnostic fallback events map to `mark`
  events.

For subagent correlation, mark metadata includes parent and child session IDs,
subagent IDs, role/status fields when present, and derived
`parent_trajectory_id` / `child_trajectory_id` values. This keeps the ATOF
stream lossless for later ATIF conversion that can compact subagents into
separate trajectories.

## Adaptive Execution Example

Nastech core owns the LLM and tool boundaries and enters NeMo Relay managed
execution while a Nastech-managed Relay consumer is active. With no shared
metrics subscriber or explicitly configured Relay plugin, Nastech calls the
provider or tool directly. The `observability/nemo_relay` plugin retains the
managed path while its adaptive components are installed on those boundaries.

Minimal `plugins.toml`:

```toml
version = 1

[[components]]
kind = "adaptive"
enabled = true

[components.config.tool_parallelism]
mode = "observe_only"
```

Enable it for Nastech:

```bash
export NASTECH_NEMO_RELAY_PLUGINS_TOML=/tmp/nastech-middleware-test/plugins.toml
```

Execution follows these boundaries with or without an adaptive component:

```text
Nastech provider call
  -> nemo_relay.llm.execute(...)
    -> Nastech provider adapter callback(...)

Nastech tool call
  -> nemo_relay.tools.execute(...)
    -> Nastech authorization and dispatch callback(...)
```

The plugin emits observer marks for sessions, turns, approvals, and subagents.
It does not register provider or tool lifecycle hooks, so each managed call
produces one Relay lifecycle.

### Local Adaptive E2E

This example enables both NeMo Relay observability export and adaptive execution
middleware for a local Nastech run. This path requires a NeMo Relay runtime that
supports `[components.config.tool_parallelism]`, as provided by NeMo Relay 0.6
and later.

```bash
export NASTECH_HOME=/tmp/nastech-middleware-test/nastech-home
mkdir -p "$NASTECH_HOME" /tmp/nastech-middleware-test/nemo-relay

cat > "$NASTECH_HOME/config.yaml" <<'YAML'
model:
  provider: custom
  default: qwen3.6:35b
  base_url: http://127.0.0.1:11434/v1
  api_key: ollama
plugins:
  enabled:
    - observability/nemo_relay
YAML

cat > /tmp/nastech-middleware-test/nemo-relay/plugins.toml <<'TOML'
version = 1

[[components]]
kind = "observability"
enabled = true

[components.config]
version = 1

[components.config.atof]
enabled = true
output_directory = "/tmp/nastech-middleware-test/atof"
filename = "middleware-events.jsonl"
mode = "overwrite"

[components.config.atif]
enabled = true
output_directory = "/tmp/nastech-middleware-test/atif"
filename_template = "middleware-trajectory-{session_id}.json"
agent_name = "Nastech Middleware E2E"
agent_version = "local"

[[components]]
kind = "adaptive"
enabled = true

[components.config.tool_parallelism]
mode = "observe_only"
TOML

export NASTECH_NEMO_RELAY_PLUGINS_TOML=/tmp/nastech-middleware-test/nemo-relay/plugins.toml

nastech chat \
  --query 'Use the terminal tool exactly once to run printf middleware_execution_ok. Then reply with exactly the command output.' \
  --provider custom \
  --model qwen3.6:35b \
  --toolsets terminal \
  --max-turns 4 \
  --quiet \
  --accept-hooks
```

Expected CLI output:

```text
session_id: middleware-demo-session
middleware_execution_ok
```

Expected ATOF shape:

```jsonl
{"kind":"scope","category":"llm","name":"custom","scope_category":"start","metadata":{"session_id":"middleware-demo-session"},"data":{"mode":"observe_only"}}
{"kind":"scope","category":"tool","name":"terminal","scope_category":"start","metadata":{"session_id":"middleware-demo-session","tool_call_id":"call_terminal"},"data":{"mode":"observe_only"}}
{"kind":"scope","category":"tool","name":"terminal","scope_category":"end","metadata":{"session_id":"middleware-demo-session","tool_call_id":"call_terminal","status":"ok"},"data":"{\"output\":\"middleware_execution_ok\",\"exit_code\":0,\"error\":null}"}
```

Expected ATIF shape:

```json
{
  "schema_version": "ATIF-v1.7",
  "session_id": "middleware-demo-session",
  "agent": {
    "name": "Nastech Middleware E2E",
    "version": "local",
    "model_name": "qwen3.6:35b"
  },
  "steps": [
    {
      "source": "agent",
      "tool_calls": [
        {
          "function_name": "terminal",
          "arguments": {"command": "printf middleware_execution_ok"}
        }
      ],
      "observation": {
        "results": [
          {
            "source_call_id": "call_terminal",
            "content": "{\"output\":\"middleware_execution_ok\",\"exit_code\":0,\"error\":null}"
          }
        ]
      }
    },
    {
      "source": "agent",
      "message": "middleware_execution_ok"
    }
  ]
}
```
