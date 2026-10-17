# Mattermost MCP

[![Status](https://img.shields.io/badge/status-active-success)](https://github.com/genius-agents/mattermost-mcp)
[![Version](https://img.shields.io/badge/version-2.1.0-blue)](pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Mattermost enterprise messaging collaboration server. Built with the highest architectural standards, incorporating dynamic facades, custom API routing, and FastMCP tool decoration.

> **Documentation** — Installation, deployment, usage across the API, CLI, and MCP
> interfaces, the companion agent server, and guidance for provisioning the Mattermost
> platform are maintained in the
> [official documentation](https://knuckles-team.github.io/mattermost-mcp/).

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [MCP Tools](#mcp-tools)
- [Architecture](#architecture)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Mattermost MCP provides a high-performance, model-optimized interface to Mattermost capabilities. It isolates the model from underlying API transport complexity, ensuring safe, idempotent, and highly traceable system interactions.

---

## Features

- **Dynamic Facade Orchestration**: Integrates multi-inheritance clients cleanly under a single facade.
- **Battle-Tested Resilience**: Out-of-the-box credential authentication, connection polling, and request retry strategies.
- **FastMCP Declarative Tools**: Fast, native schema registration with full inline validation.
- **Complete Test Intent Diversity**: Deep, automated unit, integration, and mock tests ensuring high code coverage.

---

## ⚙️ Dynamic Tool Selection & Visibility

This MCP server supports dynamic toolset selection and visibility filtering at runtime. This allows the operator to restrict the set of exposed tools to prevent blowing up the LLM's context window.

The operator can configure tool filtering via multiple input channels:

- **CLI Arguments:** Pass `--tools` or `--toolsets` (or their disabled counterparts `--disabled-tools` and `--disabled-toolsets`) during startup.
- **Environment Variables:** Define standard environment variables:
  - `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS`
  - `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS`
- **HTTP SSE Request Headers:** Pass custom headers during transport initialization:
  - `x-mcp-enabled-tools` / `x-mcp-disabled-tools`
  - `x-mcp-enabled-tags` / `x-mcp-disabled-tags`
- **HTTP SSE Request Query Parameters:** Append query parameters directly to the operator's transport connection URL:
  - `?tools=tool1,tool2`
  - `?tags=tag1`

When query strings or parameters are provided, an LLM-free **Knowledge Graph resolution layer** (using `DynamicToolOrchestrator`) matches query intents against known tool tags, names, or descriptions, with safe fallback and automated 24-hour background cache refreshing.


---

## Installation

Pick the extra that matches what the operator want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `mattermost-mcp[mcp]` | Connector-focused MCP server (`agent-connector-sdk` — FastMCP/FastAPI + `epistemic-graph[full]`) | The operator only run the **MCP server** (smallest install / image) |
| `mattermost-mcp[agent]` | Agent runtime (`agent-connector-sdk` — model orchestration + `epistemic-graph[full]`) | The operator run the **integrated agent** |
| `mattermost-mcp[all]` | Everything (`mcp` + `agent` + `logfire`) | Development / both surfaces |

```bash
# Connector-focused MCP server (includes the shared graph engine)
uv pip install "mattermost-mcp[mcp]"

# Agent runtime (adds model orchestration to the shared graph engine)
uv pip install "mattermost-mcp[agent]"

# Everything (development)
uv pip install "mattermost-mcp[all]"      # or: python -m pip install "mattermost-mcp[all]"
```

### Container images (`:mcp` vs `:agent`)

One multi-stage `docker/Dockerfile` builds two right-sized images, selected by `--target`:

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `example/mattermost-mcp:mcp` | `--target mcp` | `mattermost-mcp[mcp]` — **connector-focused**, includes `epistemic-graph[full]`; no model-orchestration stack | `mattermost-mcp` |
| `example/mattermost-mcp@sha256:<digest>` | `--target agent` (default) | `mattermost-mcp[agent]` — **agent runtime**, model orchestration + `epistemic-graph[full]` | `mattermost-agent` |

```bash
docker build --target mcp   -t example/mattermost-mcp:mcp    docker/   # connector-focused MCP server
docker build --target agent -t example/mattermost-mcp:agent-local docker/   # agent runtime
```

`docker/mcp.compose.yml` runs the connector-focused `:mcp` server; `docker/agent.compose.yml` runs the
agent (`immutable agent digest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`epistemic-graph`)

Both `[mcp]` and `[agent]` carry the **epistemic-graph** engine through the required
Agent Connector SDK core dependency (`epistemic-graph[full]`). The `[mcp]` extra keeps
the server connector-focused; `[agent]` also enables model orchestration. Local
deployments can use the bundled engine. For production or shared state, run
**epistemic-graph as a dedicated database service** and configure the runtime to use it.
Deployment recipes (single-node + Raft HA), connection configuration, and architecture
diagrams are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).

---

## Usage

The operator can start the FastMCP server in stdio mode via Python module execution:

```python
import asyncio
from mattermost_mcp.mcp_server import get_mcp_instance

async def main():
    mcp = get_mcp_instance()
    # Execute stdio loop or launch server
    print("MCP Server ready.")

if __name__ == "__main__":
    asyncio.run(main())
```

For direct shell start, run:

```bash
python -m mattermost_mcp.mcp_server
```

---

## Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `MATTERMOST_URL` | `http://localhost:8065` | Mattermost Server API v4 endpoint URL |
| `MATTERMOST_TOKEN` | secret-injected | Personal Access Token or Bot Token |
| `MATTERMOST_MCP_BASE_URL` | `http://localhost:8065` | Fallback API base URL (used when MATTERMOST_URL is unset) |
| `MATTERMOST_MCP_USERNAME` | `mattermost_username` | Username for login-based auth (alternative to token) |
| `MATTERMOST_MCP_PASSWORD` | secret-injected | Password for login-based auth (alternative to token) |
| `TLS_PROFILE` | `private-ca` | AgentConfig named transport profile |
| `TLS_PROFILE_REF` | `secret://transport/provider` | Direct runtime profile reference |
| `TLS_PROFILES_REF` | `secret://transport/catalog` | Named runtime profile catalog |
| `ACCESS_CONTROLTOOL` | `True` | These names match the authoritative "Toggle Env Var" column in the README MCP tools table (condensed action-routed surface). |
| `ACTIONSTOOL` | `True` |  |
| `AGENTSTOOL` | `True` |  |
| `AUDIT_LOGGINGTOOL` | `True` |  |
| `BOARDSTOOL` | `True` |  |
| `BOOKMARKSTOOL` | `True` |  |
| `BOTSTOOL` | `True` |  |
| `BRANDTOOL` | `True` |  |
| `CHANNELSTOOL` | `True` |  |
| `CLOUDTOOL` | `True` |  |
| `CLUSTERTOOL` | `True` |  |
| `COMMANDSTOOL` | `True` |  |
| `COMPLIANCETOOL` | `True` |  |
| `CONTENT_FLAGGINGTOOL` | `True` |  |
| `CUSTOM_PROFILE_ATTRIBUTESTOOL` | `True` |  |
| `DATARETENTIONTOOL` | `True` |  |
| `ELASTICSEARCHTOOL` | `True` |  |
| `EMOJITOOL` | `True` |  |
| `EXPORTSTOOL` | `True` |  |
| `FILESTOOL` | `True` |  |
| `GROUPSTOOL` | `True` |  |
| `IMPORTSTOOL` | `True` |  |
| `IP_FILTERSTOOL` | `True` |  |
| `JOBSTOOL` | `True` |  |
| `LDAPTOOL` | `True` |  |
| `LIMITSTOOL` | `True` |  |
| `LOGSTOOL` | `True` |  |
| `METRICSTOOL` | `True` |  |
| `OAUTHTOOL` | `True` |  |
| `OUTGOING_OAUTH_CONNECTIONSTOOL` | `True` |  |
| `PERMISSIONSTOOL` | `True` |  |
| `PLUGINSTOOL` | `True` |  |
| `POSTSTOOL` | `True` |  |
| `PREFERENCESTOOL` | `True` |  |
| `PROPERTIESTOOL` | `True` |  |
| `REACTIONSTOOL` | `True` |  |
| `RECAPSTOOL` | `True` |  |
| `REMOTECLUSTERSTOOL` | `True` |  |
| `REPORTSTOOL` | `True` |  |
| `ROLESTOOL` | `True` |  |
| `SAMLTOOL` | `True` |  |
| `SCHEDULED_POSTTOOL` | `True` |  |
| `SCHEMESTOOL` | `True` |  |
| `SERVICE_TERMSTOOL` | `True` |  |
| `SHAREDCHANNELSTOOL` | `True` |  |
| `STATUSTOOL` | `True` |  |
| `SYSTEMTOOL` | `True` |  |
| `TEAMSTOOL` | `True` |  |
| `UPLOADSTOOL` | `True` |  |
| `USAGETOOL` | `True` |  |
| `USERSTOOL` | `True` |  |
| `VIEWSTOOL` | `True` |  |
| `WEBHOOKSTOOL` | `True` |  |
| `MATTERMOST_TLS_PROFILE` | — |  |
| `MATTERMOST_TLS_PROFILE_REF` | — |  |
| `KGTOOL` | `True` |  |
| `MATTERMOST_MCP_MCP_IMAGE` | — | Required for the corresponding Compose deployment: image@sha256:digest. |
| `MATTERMOST_MCP_AGENT_IMAGE` | — |  |
| `MATTERMOST_OPENAPI_SOURCE` | — | Required when running generate_mattermost_mcp.py. |
| `MATTERMOST_MCP_PACKAGE_DIR` | `./mattermost_mcp` | Optional output override; when unset, defaults to the repository package directory. |

#### Inherited agent-connector-sdk variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `TRANSPORT` | `stdio` | MCP transport: `stdio` \| `streamable-http` \| `sse` |
| `HOST` | `127.0.0.1` | Loopback bind host (set an authenticated ingress explicitly) |
| `PORT` | `8000` | Bind port (HTTP transports) |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `EUNOMIA_TYPE` | `none` | Authorization mode: `none` \| `embedded` \| `remote` |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` | Embedded Eunomia policy file |
| `EUNOMIA_REMOTE_URL` | — | Remote Eunomia authorization server URL |
| `ENABLE_OTEL` | `False` | Enable OpenTelemetry export |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | — | OTLP collector endpoint |
| `MCP_CLIENT_AUTH` | — | Outbound MCP child auth: `oidc-client-credentials` \| `basic` \| `none` |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET_REF` | `secret://identity/oidc-client-secret` | Runtime secret reference for the OIDC service account |
| `MCP_BASIC_AUTH_USERNAME` | — | HTTP Basic username (`MCP_CLIENT_AUTH=basic`) |
| `MCP_BASIC_AUTH_PASSWORD_REF` | `secret://identity/mcp-basic-password` | Runtime secret reference for HTTP Basic auth (`MCP_CLIENT_AUTH=basic`) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | — | Operator-configured LLM provider for the agent |
| `MODEL_ID` | — | Operator-configured model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_68 package + 23 inherited variable(s). Auto-generated from `.env.example` + the shared agent-connector-sdk set — do not edit._
<!-- ENV-VARS-TABLE:END -->


Every variable the server reads. A local template is provided inside
[.env.example](.env.example) — copy it to `.env` and fill in the operator's endpoint/credentials.

### Connection & Credentials
| Variable | Description | Default |
|----------|-------------|---------|
| `MATTERMOST_URL` | Mattermost Server API v4 endpoint URL | `http://localhost:8065` |
| `MATTERMOST_TOKEN` | Personal Access Token or Bot Token | — |

### MCP server / transport
| Variable | Description | Default |
|----------|-------------|---------|
| `TRANSPORT` | `stdio`, `streamable-http`, or `sse` | `stdio` |
| `HOST` | Bind host (HTTP transports) | `0.0.0.0` |
| `PORT` | Bind port (HTTP transports) | `8000` |
| `MCP_TOOL_MODE` | Tool surface: `condensed`, `verbose`, or `both` | `condensed` |
| `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS` | Comma-separated tool allow/deny list | — |
| `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS` | Comma-separated tag allow/deny list | — |
| `DEBUG` | Verbose logging | `False` |
| `PYTHONUNBUFFERED` | Unbuffered stdout (recommended in containers) | `1` |

### Tool toggles
Each action-routed tool can be disabled individually via its toggle env var (set to `false`).
The full list is in the [MCP Tools](#mcp-tools) table above (e.g. `CHANNELSTOOL`, `POSTSTOOL`,
`USERSTOOL`, `TEAMSTOOL`).

### Agent CLI (full `[agent]` runtime only)
| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_URL` | URL of the MCP server the agent connects to | `http://localhost:8000/mcp` |
| `PROVIDER` | LLM provider (e.g. `openai`) | `openai` |
| `MODEL_ID` | Model id (e.g. `gpt-4o`) | `gpt-4o` |
| `ENABLE_WEB_UI` | Serve the AG-UI web interface | `True` |

---

## MCP Tools

The following declarative FastMCP tools are registered and available to upstream AI agents:

<!-- This table is auto-generated by `python -m agent_connector_sdk.mcp.readme_tools` — do not edit by hand. -->

<!-- MCP-TOOLS-TABLE:START -->

#### Intent tools

| MCP Tool | Kind | Description |
|----------|------|-------------|
| `mattermost_ingest_channels` | intent | Ingest a team's channels as typed :Channel nodes (+ :inTeam links). |
| `mattermost_ingest_posts` | intent | Ingest a channel's messages as :Document nodes (+ channel/author links). |
| `mattermost_ingest_teams` | intent | Ingest Mattermost teams into epistemic-graph as typed :Team nodes. |
| `mattermost_ingest_users` | intent | Ingest Mattermost users as shared :Person / :Bot nodes. |
| `mattermost_mcp_access_control` | intent | Manage Mattermost MCP access_control operations. |
| `mattermost_mcp_actions` | intent | Manage Mattermost MCP actions operations. |
| `mattermost_mcp_agents` | intent | Manage Mattermost MCP agents operations. |
| `mattermost_mcp_audit_logging` | intent | Manage Mattermost MCP audit_logging operations. |
| `mattermost_mcp_boards` | intent | Manage Mattermost MCP boards operations. |
| `mattermost_mcp_bookmarks` | intent | Manage Mattermost MCP bookmarks operations. |
| `mattermost_mcp_bots` | intent | Manage Mattermost MCP bots operations. |
| `mattermost_mcp_brand` | intent | Manage Mattermost MCP brand operations. |
| `mattermost_mcp_channels` | intent | Manage Mattermost MCP channels operations. |
| `mattermost_mcp_cloud` | intent | Manage Mattermost MCP cloud operations. |
| `mattermost_mcp_cluster` | intent | Manage Mattermost MCP cluster operations. |
| `mattermost_mcp_commands` | intent | Manage Mattermost MCP commands operations. |
| `mattermost_mcp_compliance` | intent | Manage Mattermost MCP compliance operations. |
| `mattermost_mcp_content_flagging` | intent | Manage Mattermost MCP content_flagging operations. |
| `mattermost_mcp_custom_profile_attributes` | intent | Manage Mattermost MCP custom_profile_attributes operations. |
| `mattermost_mcp_dataretention` | intent | Manage Mattermost MCP dataretention operations. |
| `mattermost_mcp_elasticsearch` | intent | Manage Mattermost MCP elasticsearch operations. |
| `mattermost_mcp_emoji` | intent | Manage Mattermost MCP emoji operations. |
| `mattermost_mcp_exports` | intent | Manage Mattermost MCP exports operations. |
| `mattermost_mcp_files` | intent | Manage Mattermost MCP files operations. |
| `mattermost_mcp_groups` | intent | Manage Mattermost MCP groups operations. |
| `mattermost_mcp_imports` | intent | Manage Mattermost MCP imports operations. |
| `mattermost_mcp_ip_filters` | intent | Manage Mattermost MCP ip_filters operations. |
| `mattermost_mcp_jobs` | intent | Manage Mattermost MCP jobs operations. |
| `mattermost_mcp_ldap` | intent | Manage Mattermost MCP ldap operations. |
| `mattermost_mcp_limits` | intent | Manage Mattermost MCP limits operations. |
| `mattermost_mcp_logs` | intent | Manage Mattermost MCP logs operations. |
| `mattermost_mcp_metrics` | intent | Manage Mattermost MCP metrics operations. |
| `mattermost_mcp_oauth` | intent | Manage Mattermost MCP oauth operations. |
| `mattermost_mcp_outgoing_oauth_connections` | intent | Manage Mattermost MCP outgoing_oauth_connections operations. |
| `mattermost_mcp_permissions` | intent | Manage Mattermost MCP permissions operations. |
| `mattermost_mcp_plugins` | intent | Manage Mattermost MCP plugins operations. |
| `mattermost_mcp_posts` | intent | Manage Mattermost MCP posts operations. |
| `mattermost_mcp_preferences` | intent | Manage Mattermost MCP preferences operations. |
| `mattermost_mcp_properties` | intent | Manage Mattermost MCP properties operations. |
| `mattermost_mcp_reactions` | intent | Manage Mattermost MCP reactions operations. |
| `mattermost_mcp_recaps` | intent | Manage Mattermost MCP recaps operations. |
| `mattermost_mcp_remoteclusters` | intent | Manage Mattermost MCP remoteclusters operations. |
| `mattermost_mcp_reports` | intent | Manage Mattermost MCP reports operations. |
| `mattermost_mcp_roles` | intent | Manage Mattermost MCP roles operations. |
| `mattermost_mcp_saml` | intent | Manage Mattermost MCP saml operations. |
| `mattermost_mcp_scheduled_post` | intent | Manage Mattermost MCP scheduled_post operations. |
| `mattermost_mcp_schemes` | intent | Manage Mattermost MCP schemes operations. |
| `mattermost_mcp_service_terms` | intent | Manage Mattermost MCP service_terms operations. |
| `mattermost_mcp_sharedchannels` | intent | Manage Mattermost MCP sharedchannels operations. |
| `mattermost_mcp_status` | intent | Manage Mattermost MCP status operations. |
| `mattermost_mcp_system` | intent | Manage Mattermost MCP system operations. |
| `mattermost_mcp_teams` | intent | Manage Mattermost MCP teams operations. |
| `mattermost_mcp_uploads` | intent | Manage Mattermost MCP uploads operations. |
| `mattermost_mcp_usage` | intent | Manage Mattermost MCP usage operations. |
| `mattermost_mcp_users` | intent | Manage Mattermost MCP users operations. |
| `mattermost_mcp_views` | intent | Manage Mattermost MCP views operations. |
| `mattermost_mcp_webhooks` | intent | Manage Mattermost MCP webhooks operations. |

_57 intent tool(s) · 0 operation(s). Call an operation as `act(action='<operation>', params={...})` (`ask` for reads); `find(action='describe', params={'action': '<operation>'})` returns its arguments. An operation is enabled unless its `<DOMAIN>TOOL` toggle is set false. Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

See [docs/overview.md](docs/overview.md) or [docs/concepts.md](docs/concepts.md) for deeper operational examples.

---

## Architecture

This package uses the standardized Agent-Utilities dynamic facade architecture:

```mermaid
graph TD
    User([User Agent]) --> Server[FastMCP Server]
    Server --> Facade[Api Dynamic Facade]
    Facade --> ClientBase[ApiClientBase]
    Facade --> Auth[Credentials Auth Handler]
    ClientBase --> Service([External Service API])
```

---

## Deployment

### Bare-Metal (Standard pip)
1. Set up the operator's Python virtual environment (>= 3.10).
2. Install the package: `pip install .[all]`
3. Export credentials:
   ```bash
   export MATTERMOST_URL="http://localhost:8065"
   ```
4. Run: `python -m mattermost_mcp.mcp_server`

### Container (Docker Compose)
A standard compose structure is provided inside the `docker/` folder. Build and deploy:

```bash
docker compose -f docker/compose.yml up --build -d
```

---

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`mattermost-mcp` can run as a local stdio process or container, or behind a remote
network boundary. The
[Deployment guide](https://knuckles-team.github.io/mattermost-mcp/deployment/) carries
the detailed transport contract.

- **Local container** — launch a reviewed immutable image as a least-privilege
  stdio child with no listener or published port.
- **Remote URL** — connect through an operator-supplied authenticated HTTPS
  ingress. Keep its URL, outbound identity references, trust profile, and exact
  `MCP_ALLOWED_HOSTS` in `AgentConfig`.
<!-- END GENERATED: additional-deployment-options -->

## MCP Configuration Examples

<!-- MCP-CONFIG-EXAMPLES:START -->

> **Install the connector-focused `[mcp]` extra.** Examples use `mattermost-mcp[mcp]` to add
> FastMCP / FastAPI through `agent-connector-sdk`; the required Agent Connector SDK core
> still carries `epistemic-graph[full]`. The `[agent-runtime]` extra additionally
> enables model orchestration.

#### stdio Transport (local IDEs — Cursor, Claude Desktop, VS Code)

```json
{
  "mcpServers": {
    "mattermost-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "mattermost-mcp[mcp]",
        "mattermost-mcp"
      ],
      "env": {
        "ACCESS_CONTROLTOOL": "True",
        "ACTIONSTOOL": "True",
        "AGENTSTOOL": "True",
        "AUDIT_LOGGINGTOOL": "True",
        "BOARDSTOOL": "True",
        "BOOKMARKSTOOL": "True",
        "BOTSTOOL": "True",
        "BRANDTOOL": "True",
        "CHANNELSTOOL": "True",
        "CLOUDTOOL": "True",
        "CLUSTERTOOL": "True",
        "COMMANDSTOOL": "True",
        "COMPLIANCETOOL": "True",
        "CONTENT_FLAGGINGTOOL": "True",
        "CUSTOM_PROFILE_ATTRIBUTESTOOL": "True",
        "DATARETENTIONTOOL": "True",
        "ELASTICSEARCHTOOL": "True",
        "EMOJITOOL": "True",
        "EXPORTSTOOL": "True",
        "FILESTOOL": "True",
        "GROUPSTOOL": "True",
        "IMPORTSTOOL": "True",
        "IP_FILTERSTOOL": "True",
        "JOBSTOOL": "True",
        "KGTOOL": "True",
        "LDAPTOOL": "True",
        "LIMITSTOOL": "True",
        "LOGSTOOL": "True",
        "MATTERMOST_MCP_BASE_URL": "http://localhost:8065",
        "MATTERMOST_MCP_PACKAGE_DIR": "./mattermost_mcp",
        "MATTERMOST_MCP_PASSWORD": "mattermost_password",
        "MATTERMOST_MCP_USERNAME": "mattermost_username",
        "MATTERMOST_TOKEN": "mattermost_api_access_token",
        "MATTERMOST_URL": "http://localhost:8065",
        "METRICSTOOL": "True",
        "OAUTHTOOL": "True",
        "OUTGOING_OAUTH_CONNECTIONSTOOL": "True",
        "PERMISSIONSTOOL": "True",
        "PLUGINSTOOL": "True",
        "POSTSTOOL": "True",
        "PREFERENCESTOOL": "True",
        "PROPERTIESTOOL": "True",
        "REACTIONSTOOL": "True",
        "RECAPSTOOL": "True",
        "REMOTECLUSTERSTOOL": "True",
        "REPORTSTOOL": "True",
        "ROLESTOOL": "True",
        "SAMLTOOL": "True",
        "SCHEDULED_POSTTOOL": "True",
        "SCHEMESTOOL": "True",
        "SERVICE_TERMSTOOL": "True",
        "SHAREDCHANNELSTOOL": "True",
        "STATUSTOOL": "True",
        "SYSTEMTOOL": "True",
        "TEAMSTOOL": "True",
        "UPLOADSTOOL": "True",
        "USAGETOOL": "True",
        "USERSTOOL": "True",
        "VIEWSTOOL": "True",
        "WEBHOOKSTOOL": "True"
      }
    }
  }
}
```

Runtime references require an alias-aware launcher such as GraphOS. Other
launchers must omit those entries and inject the resolved values through their
own runtime secret boundary.

#### Streamable-HTTP Transport (networked / production)

```json
{
  "mcpServers": {
    "mattermost-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "mattermost-mcp[mcp]",
        "mattermost-mcp",
        "--transport",
        "streamable-http",
        "--port",
        "8000"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "ACCESS_CONTROLTOOL": "True",
        "ACTIONSTOOL": "True",
        "AGENTSTOOL": "True",
        "AUDIT_LOGGINGTOOL": "True",
        "BOARDSTOOL": "True",
        "BOOKMARKSTOOL": "True",
        "BOTSTOOL": "True",
        "BRANDTOOL": "True",
        "CHANNELSTOOL": "True",
        "CLOUDTOOL": "True",
        "CLUSTERTOOL": "True",
        "COMMANDSTOOL": "True",
        "COMPLIANCETOOL": "True",
        "CONTENT_FLAGGINGTOOL": "True",
        "CUSTOM_PROFILE_ATTRIBUTESTOOL": "True",
        "DATARETENTIONTOOL": "True",
        "ELASTICSEARCHTOOL": "True",
        "EMOJITOOL": "True",
        "EXPORTSTOOL": "True",
        "FILESTOOL": "True",
        "GROUPSTOOL": "True",
        "IMPORTSTOOL": "True",
        "IP_FILTERSTOOL": "True",
        "JOBSTOOL": "True",
        "KGTOOL": "True",
        "LDAPTOOL": "True",
        "LIMITSTOOL": "True",
        "LOGSTOOL": "True",
        "MATTERMOST_MCP_BASE_URL": "http://localhost:8065",
        "MATTERMOST_MCP_PACKAGE_DIR": "./mattermost_mcp",
        "MATTERMOST_MCP_PASSWORD": "mattermost_password",
        "MATTERMOST_MCP_USERNAME": "mattermost_username",
        "MATTERMOST_TOKEN": "mattermost_api_access_token",
        "MATTERMOST_URL": "http://localhost:8065",
        "METRICSTOOL": "True",
        "OAUTHTOOL": "True",
        "OUTGOING_OAUTH_CONNECTIONSTOOL": "True",
        "PERMISSIONSTOOL": "True",
        "PLUGINSTOOL": "True",
        "POSTSTOOL": "True",
        "PREFERENCESTOOL": "True",
        "PROPERTIESTOOL": "True",
        "REACTIONSTOOL": "True",
        "RECAPSTOOL": "True",
        "REMOTECLUSTERSTOOL": "True",
        "REPORTSTOOL": "True",
        "ROLESTOOL": "True",
        "SAMLTOOL": "True",
        "SCHEDULED_POSTTOOL": "True",
        "SCHEMESTOOL": "True",
        "SERVICE_TERMSTOOL": "True",
        "SHAREDCHANNELSTOOL": "True",
        "STATUSTOOL": "True",
        "SYSTEMTOOL": "True",
        "TEAMSTOOL": "True",
        "UPLOADSTOOL": "True",
        "USAGETOOL": "True",
        "USERSTOOL": "True",
        "VIEWSTOOL": "True",
        "WEBHOOKSTOOL": "True"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed Streamable-HTTP instance by `url`:

```json
{
  "mcpServers": {
    "mattermost-mcp": {
      "url": "http://localhost:8000/mattermost-mcp/mcp"
    }
  }
}
```

Run a reviewed container image as a least-privilege stdio child (no
listener or published port):

```bash
docker run -i --rm \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=256 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  -e TRANSPORT=stdio \
  -e ACCESS_CONTROLTOOL=True \
  -e ACTIONSTOOL=True \
  -e AGENTSTOOL=True \
  -e AUDIT_LOGGINGTOOL=True \
  -e BOARDSTOOL=True \
  -e BOOKMARKSTOOL=True \
  -e BOTSTOOL=True \
  -e BRANDTOOL=True \
  -e CHANNELSTOOL=True \
  -e CLOUDTOOL=True \
  -e CLUSTERTOOL=True \
  -e COMMANDSTOOL=True \
  -e COMPLIANCETOOL=True \
  -e CONTENT_FLAGGINGTOOL=True \
  -e CUSTOM_PROFILE_ATTRIBUTESTOOL=True \
  -e DATARETENTIONTOOL=True \
  -e ELASTICSEARCHTOOL=True \
  -e EMOJITOOL=True \
  -e EXPORTSTOOL=True \
  -e FILESTOOL=True \
  -e GROUPSTOOL=True \
  -e IMPORTSTOOL=True \
  -e IP_FILTERSTOOL=True \
  -e JOBSTOOL=True \
  -e KGTOOL=True \
  -e LDAPTOOL=True \
  -e LIMITSTOOL=True \
  -e LOGSTOOL=True \
  -e MATTERMOST_MCP_BASE_URL=http://localhost:8065 \
  -e MATTERMOST_MCP_PACKAGE_DIR=./mattermost_mcp \
  -e MATTERMOST_MCP_PASSWORD=mattermost_password \
  -e MATTERMOST_MCP_USERNAME=mattermost_username \
  -e MATTERMOST_TOKEN=mattermost_api_access_token \
  -e MATTERMOST_URL=http://localhost:8065 \
  -e METRICSTOOL=True \
  -e OAUTHTOOL=True \
  -e OUTGOING_OAUTH_CONNECTIONSTOOL=True \
  -e PERMISSIONSTOOL=True \
  -e PLUGINSTOOL=True \
  -e POSTSTOOL=True \
  -e PREFERENCESTOOL=True \
  -e PROPERTIESTOOL=True \
  -e REACTIONSTOOL=True \
  -e RECAPSTOOL=True \
  -e REMOTECLUSTERSTOOL=True \
  -e REPORTSTOOL=True \
  -e ROLESTOOL=True \
  -e SAMLTOOL=True \
  -e SCHEDULED_POSTTOOL=True \
  -e SCHEMESTOOL=True \
  -e SERVICE_TERMSTOOL=True \
  -e SHAREDCHANNELSTOOL=True \
  -e STATUSTOOL=True \
  -e SYSTEMTOOL=True \
  -e TEAMSTOOL=True \
  -e UPLOADSTOOL=True \
  -e USAGETOOL=True \
  -e USERSTOOL=True \
  -e VIEWSTOOL=True \
  -e WEBHOOKSTOOL=True \
  registry.example.invalid/mattermost-mcp@sha256:<digest> mattermost-mcp
```

For containerized network HTTP, supply an authenticated TLS ingress (or
direct server TLS), exact `MCP_ALLOWED_HOSTS`, and an exact trusted-proxy
CIDR policy through the operator-owned deployment profile. The generator
does not emit an unauthenticated non-loopback listener.

_Auto-generated from the code-read env surface (package vars) — do not edit._
<!-- MCP-CONFIG-EXAMPLES:END -->

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/mattermost-mcp/) and is
the recommended reference for installation, deployment, and day-to-day operation.

| Page | Contents |
|---|---|
| [Installation](https://knuckles-team.github.io/mattermost-mcp/installation/) | pip, source, extras, prebuilt Docker image |
| [Deployment](https://knuckles-team.github.io/mattermost-mcp/deployment/) | run the MCP server and agent, Compose, Caddy + Technitium, env config |
| [Usage](https://knuckles-team.github.io/mattermost-mcp/usage/) | the MCP tools, the `Api` client, the CLI |
| [Backing Platform](https://knuckles-team.github.io/mattermost-mcp/platform/) | deploy Mattermost with Docker |
| [Overview](https://knuckles-team.github.io/mattermost-mcp/overview/) | dynamic facade and FastMCP integration |
| [Architecture](https://knuckles-team.github.io/mattermost-mcp/architecture/) | dynamic facade, FastMCP, agent server |
| [Concepts](https://knuckles-team.github.io/mattermost-mcp/concepts/) | concept registry (`CONCEPT:MM-*`) |

---

## Contributing

Please audit all code changes against the repository's contribution and review requirements, and run:

```bash
pre-commit run --all-files
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for complete details.


<!-- BEGIN agent-connector-sdk-deployment (generated; do not edit between markers) -->

## Deploy with `agent-connector-sdk-deployment`

Provision this package with the consolidated **`agent-connector-sdk-deployment`**
workflow. It selects an installed-package, editable-source, or immutable-container
path; records only runtime secret and TLS-profile references in `AgentConfig`; and
runs doctor, registration, policy, observability, and rollback gates. Ask your agent
to **"deploy `mattermost-mcp` with agent-connector-sdk-deployment"**.

| Install mode | Command |
|------|---------|
| Installed package | `uv tool install "mattermost-mcp[mcp]"`, then run `mattermost-mcp` |
| Editable source | `uv pip install -e ".[agent]"`, then run `mattermost-mcp` |
| Immutable container | deploy `registry.example.invalid/mattermost-mcp@sha256:<digest>` through the operator-selected orchestrator |

The repository embeds no deployment profile, credential value, certificate path, or
environment-specific endpoint. Supply those at runtime through `AgentConfig` and the
configured secret provider.

<!-- END agent-connector-sdk-deployment -->

<!-- GOVERNED-CAPABILITY:START -->
## Governed capability contract

This package ships a compact canonical skill surface with specialist procedures
kept as referenced workflows. The current MCP tools, skill metadata,
`connector_manifest.yml`, ontology, mappings, shapes, fixtures, migrations,
tool-schema fingerprints, and certification metadata form one versioned
capability contract. Validate them together; do not rely on stale tool names or
historical per-task skill wrappers.

Runtime endpoints, credentials, certificate trust, tenant identity, retention,
and observability policy are deployment inputs and are never packaged values.
See [Configuration, trust, and privacy](docs/configuration.md) before enabling a
network transport, connector ingestion, GraphOS delegation, or trace export.
<!-- GOVERNED-CAPABILITY:END -->
