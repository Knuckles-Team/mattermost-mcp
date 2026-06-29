# Mattermost MCP

[![Status](https://img.shields.io/badge/status-active-success)](https://github.com/genius-agents/mattermost-mcp)
[![Version](https://img.shields.io/badge/version-1.0.0-blue)](pyproject.toml)
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

This MCP server supports dynamic toolset selection and visibility filtering at runtime. This allows you to restrict the set of exposed tools in order to prevent blowing up the LLM's context window.

You can configure tool filtering via multiple input channels:

- **CLI Arguments:** Pass `--tools` or `--toolsets` (or their disabled counterparts `--disabled-tools` and `--disabled-toolsets`) during startup.
- **Environment Variables:** Define standard environment variables:
  - `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS`
  - `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS`
- **HTTP SSE Request Headers:** Pass custom headers during transport initialization:
  - `x-mcp-enabled-tools` / `x-mcp-disabled-tools`
  - `x-mcp-enabled-tags` / `x-mcp-disabled-tags`
- **HTTP SSE Request Query Parameters:** Append query parameters directly to your transport connection URL:
  - `?tools=tool1,tool2`
  - `?tags=tag1`

When query strings or parameters are supplied, an LLM-free **Knowledge Graph resolution layer** (using `DynamicToolOrchestrator`) matches query intents against known tool tags, names, or descriptions, with safe fallback and automated 24-hour background cache refreshing.


---

## Installation

Pick the extra that matches what you want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `mattermost-mcp[mcp]` | Slim MCP server only (`agent-utilities[mcp]` — FastMCP/FastAPI) | You only run the **MCP server** (smallest install / image) |
| `mattermost-mcp[agent]` | Full agent runtime (`agent-utilities[agent,logfire]` — Pydantic AI + the epistemic-graph engine) | You run the **integrated agent** |
| `mattermost-mcp[all]` | Everything (`mcp` + `agent` + `logfire`) | Development / both surfaces |

```bash
# MCP server only (recommended for tool hosting — slim deps)
uv pip install "mattermost-mcp[mcp]"

# Full agent runtime (Pydantic AI + epistemic-graph engine)
uv pip install "mattermost-mcp[agent]"

# Everything (development)
uv pip install "mattermost-mcp[all]"      # or: python -m pip install "mattermost-mcp[all]"
```

### Container images (`:mcp` vs `:agent`)

One multi-stage `docker/Dockerfile` builds two right-sized images, selected by `--target`:

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `knucklessg1/mattermost-mcp:mcp` | `--target mcp` | `mattermost-mcp[mcp]` — **slim**, no engine/`pydantic-ai`/`dspy`/`llama-index`/`tree-sitter` | `mattermost-mcp` |
| `knucklessg1/mattermost-mcp:latest` | `--target agent` (default) | `mattermost-mcp[agent]` — **full** agent runtime + epistemic-graph engine | `mattermost-agent` |

```bash
docker build --target mcp   -t knucklessg1/mattermost-mcp:mcp    docker/   # slim MCP server
docker build --target agent -t knucklessg1/mattermost-mcp:latest docker/   # full agent
```

`docker/mcp.compose.yml` runs the slim `:mcp` server; `docker/agent.compose.yml` runs the
agent (`:latest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`epistemic-graph`)

The **full agent** (`[agent]` / `:latest`) embeds the **epistemic-graph** engine (pulled in
transitively via `agent-utilities[agent]`). For production — or to share one knowledge graph
across multiple agents — run **epistemic-graph as its own database container** and point the
agent at it instead of embedding it. Deployment recipes (single-node + Raft HA), connection
config, and the full database architecture (with diagrams) are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).
The slim `[mcp]` server does **not** require the database.

---

## Usage

You can launch the FastMCP server in stdio mode via Python module execution:

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

For direct shell launch, execute:

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
| `MATTERMOST_TOKEN` | `mattermost_api_access_token` | Personal Access Token or Bot Token |
| `MATTERMOST_MCP_BASE_URL` | `http://localhost:8065` | Fallback API base URL (used when MATTERMOST_URL is unset) |
| `MATTERMOST_MCP_USERNAME` | `mattermost_username` | Username for login-based auth (alternative to token) |
| `MATTERMOST_MCP_PASSWORD` | `mattermost_password` | Password for login-based auth (alternative to token) |
| `MATTERMOST_MCP_SSL_VERIFY` | `True` | Verify TLS certificates for the Mattermost connection |
| `ACCESS_CONTROLTOOL` | `True` | MCP tools table (condensed action-routed surface). |
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

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `TRANSPORT` | `stdio` | MCP transport: `stdio` | `streamable-http` | `sse` |
| `HOST` | `0.0.0.0` | Bind host (HTTP transports) |
| `PORT` | `8000` | Bind port (HTTP transports) |
| `MCP_TOOL_MODE` | `condensed` | Tool surface: `condensed` | `verbose` | `both` |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `EUNOMIA_TYPE` | `none` | Authorization mode: `none` | `embedded` | `remote` |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` | Embedded Eunomia policy file |
| `EUNOMIA_REMOTE_URL` | — | Remote Eunomia authorization server URL |
| `ENABLE_OTEL` | `False` | Enable OpenTelemetry export |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | — | OTLP collector endpoint |
| `MCP_CLIENT_AUTH` | — | Outbound MCP auth (`oidc-client-credentials` for fleet calls) |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET` | — | OIDC client secret (service-account auth) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_59 package + 22 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
<!-- ENV-VARS-TABLE:END -->


Every variable the server reads. A local template is supplied inside
[.env.example](.env.example) — copy it to `.env` and fill in your endpoint/credentials.

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

<!-- This table is auto-generated by `python -m agent_utilities.mcp.readme_tools` — do not edit by hand. -->

<!-- MCP-TOOLS-TABLE:START -->

#### Condensed action-routed tools (default — `MCP_TOOL_MODE=condensed`)

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `mattermost_mcp_access_control` | `ACCESS_CONTROLTOOL` | Manage Mattermost MCP access_control operations. |
| `mattermost_mcp_actions` | `ACTIONSTOOL` | Manage Mattermost MCP actions operations. |
| `mattermost_mcp_agents` | `AGENTSTOOL` | Manage Mattermost MCP agents operations. |
| `mattermost_mcp_audit_logging` | `AUDIT_LOGGINGTOOL` | Manage Mattermost MCP audit_logging operations. |
| `mattermost_mcp_boards` | `BOARDSTOOL` | Manage Mattermost MCP boards operations. |
| `mattermost_mcp_bookmarks` | `BOOKMARKSTOOL` | Manage Mattermost MCP bookmarks operations. |
| `mattermost_mcp_bots` | `BOTSTOOL` | Manage Mattermost MCP bots operations. |
| `mattermost_mcp_brand` | `BRANDTOOL` | Manage Mattermost MCP brand operations. |
| `mattermost_mcp_channels` | `CHANNELSTOOL` | Manage Mattermost MCP channels operations. |
| `mattermost_mcp_cloud` | `CLOUDTOOL` | Manage Mattermost MCP cloud operations. |
| `mattermost_mcp_cluster` | `CLUSTERTOOL` | Manage Mattermost MCP cluster operations. |
| `mattermost_mcp_commands` | `COMMANDSTOOL` | Manage Mattermost MCP commands operations. |
| `mattermost_mcp_compliance` | `COMPLIANCETOOL` | Manage Mattermost MCP compliance operations. |
| `mattermost_mcp_content_flagging` | `CONTENT_FLAGGINGTOOL` | Manage Mattermost MCP content_flagging operations. |
| `mattermost_mcp_custom_profile_attributes` | `CUSTOM_PROFILE_ATTRIBUTESTOOL` | Manage Mattermost MCP custom_profile_attributes operations. |
| `mattermost_mcp_dataretention` | `DATARETENTIONTOOL` | Manage Mattermost MCP dataretention operations. |
| `mattermost_mcp_elasticsearch` | `ELASTICSEARCHTOOL` | Manage Mattermost MCP elasticsearch operations. |
| `mattermost_mcp_emoji` | `EMOJITOOL` | Manage Mattermost MCP emoji operations. |
| `mattermost_mcp_exports` | `EXPORTSTOOL` | Manage Mattermost MCP exports operations. |
| `mattermost_mcp_files` | `FILESTOOL` | Manage Mattermost MCP files operations. |
| `mattermost_mcp_groups` | `GROUPSTOOL` | Manage Mattermost MCP groups operations. |
| `mattermost_mcp_imports` | `IMPORTSTOOL` | Manage Mattermost MCP imports operations. |
| `mattermost_mcp_ip_filters` | `IP_FILTERSTOOL` | Manage Mattermost MCP ip_filters operations. |
| `mattermost_mcp_jobs` | `JOBSTOOL` | Manage Mattermost MCP jobs operations. |
| `mattermost_mcp_ldap` | `LDAPTOOL` | Manage Mattermost MCP ldap operations. |
| `mattermost_mcp_limits` | `LIMITSTOOL` | Manage Mattermost MCP limits operations. |
| `mattermost_mcp_logs` | `LOGSTOOL` | Manage Mattermost MCP logs operations. |
| `mattermost_mcp_metrics` | `METRICSTOOL` | Manage Mattermost MCP metrics operations. |
| `mattermost_mcp_oauth` | `OAUTHTOOL` | Manage Mattermost MCP oauth operations. |
| `mattermost_mcp_outgoing_oauth_connections` | `OUTGOING_OAUTH_CONNECTIONSTOOL` | Manage Mattermost MCP outgoing_oauth_connections operations. |
| `mattermost_mcp_permissions` | `PERMISSIONSTOOL` | Manage Mattermost MCP permissions operations. |
| `mattermost_mcp_plugins` | `PLUGINSTOOL` | Manage Mattermost MCP plugins operations. |
| `mattermost_mcp_posts` | `POSTSTOOL` | Manage Mattermost MCP posts operations. |
| `mattermost_mcp_preferences` | `PREFERENCESTOOL` | Manage Mattermost MCP preferences operations. |
| `mattermost_mcp_properties` | `PROPERTIESTOOL` | Manage Mattermost MCP properties operations. |
| `mattermost_mcp_reactions` | `REACTIONSTOOL` | Manage Mattermost MCP reactions operations. |
| `mattermost_mcp_recaps` | `RECAPSTOOL` | Manage Mattermost MCP recaps operations. |
| `mattermost_mcp_remoteclusters` | `REMOTECLUSTERSTOOL` | Manage Mattermost MCP remoteclusters operations. |
| `mattermost_mcp_reports` | `REPORTSTOOL` | Manage Mattermost MCP reports operations. |
| `mattermost_mcp_roles` | `ROLESTOOL` | Manage Mattermost MCP roles operations. |
| `mattermost_mcp_saml` | `SAMLTOOL` | Manage Mattermost MCP saml operations. |
| `mattermost_mcp_scheduled_post` | `SCHEDULED_POSTTOOL` | Manage Mattermost MCP scheduled_post operations. |
| `mattermost_mcp_schemes` | `SCHEMESTOOL` | Manage Mattermost MCP schemes operations. |
| `mattermost_mcp_service_terms` | `SERVICE_TERMSTOOL` | Manage Mattermost MCP service_terms operations. |
| `mattermost_mcp_sharedchannels` | `SHAREDCHANNELSTOOL` | Manage Mattermost MCP sharedchannels operations. |
| `mattermost_mcp_status` | `STATUSTOOL` | Manage Mattermost MCP status operations. |
| `mattermost_mcp_system` | `SYSTEMTOOL` | Manage Mattermost MCP system operations. |
| `mattermost_mcp_teams` | `TEAMSTOOL` | Manage Mattermost MCP teams operations. |
| `mattermost_mcp_uploads` | `UPLOADSTOOL` | Manage Mattermost MCP uploads operations. |
| `mattermost_mcp_usage` | `USAGETOOL` | Manage Mattermost MCP usage operations. |
| `mattermost_mcp_users` | `USERSTOOL` | Manage Mattermost MCP users operations. |
| `mattermost_mcp_views` | `VIEWSTOOL` | Manage Mattermost MCP views operations. |
| `mattermost_mcp_webhooks` | `WEBHOOKSTOOL` | Manage Mattermost MCP webhooks operations. |

#### Verbose 1:1 API-mapped tools (`MCP_TOOL_MODE=verbose` or `both`)

<details>
<summary>578 per-operation tools — one per public API method (click to expand)</summary>

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `mattermost_accept_remote_cluster_invite` | `APITOOL` | Accept a remote cluster invite code. |
| `mattermost_acknowledge_notification` | `APITOOL` | Acknowledge receiving of a notification |
| `mattermost_add_audit_log_certificate` | `APITOOL` | Upload audit log certificate |
| `mattermost_add_channel_member` | `APITOOL` | Add user(s) to channel |
| `mattermost_add_channels_to_retention_policy` | `APITOOL` | Add channels to a granular data retention policy |
| `mattermost_add_group_members` | `APITOOL` | Adds members to a custom group |
| `mattermost_add_team_member` | `APITOOL` | Add user to team |
| `mattermost_add_team_member_from_invite` | `APITOOL` | Add user to team from invite |
| `mattermost_add_team_members` | `APITOOL` | Add multiple users to team |
| `mattermost_add_teams_to_retention_policy` | `APITOOL` | Add teams to a granular data retention policy |
| `mattermost_add_user_to_group_syncables` | `APITOOL` | Create memberships for LDAP configured channels and teams for this user |
| `mattermost_apply_i_p_filters` | `APITOOL` | Get all IP filters |
| `mattermost_assign_access_control_policy_to_channels` | `APITOOL` | Assign an access control policy to channels |
| `mattermost_assign_bot` | `APITOOL` | Assign a bot to a user |
| `mattermost_attach_device_extra_props` | `APITOOL` | Attach mobile device and extra props to the session object |
| `mattermost_autocomplete_channels_for_team` | `APITOOL` | Autocomplete channels |
| `mattermost_autocomplete_channels_for_team_for_search` | `APITOOL` | Autocomplete channels for search |
| `mattermost_autocomplete_emoji` | `APITOOL` | Autocomplete custom emoji |
| `mattermost_autocomplete_users` | `APITOOL` | Autocomplete users |
| `mattermost_burn_post` | `APITOOL` | Burn a burn-on-read post |
| `mattermost_can_user_direct_message` | `APITOOL` | Check if user can DM another user in shared channels context |
| `mattermost_cancel_job` | `APITOOL` | Cancel a job. |
| `mattermost_channel_members_minus_group_members` | `APITOOL` | Channel members minus group members. |
| `mattermost_check_access_control_policy_expression` | `APITOOL` | Check an access control policy expression |
| `mattermost_check_c_w_s_connection` | `APITOOL` | Check CWS connection |
| `mattermost_check_integrity` | `APITOOL` | Perform a database integrity check |
| `mattermost_clear_server_busy` | `APITOOL` | Clears the server busy (high load) flag |
| `mattermost_complete_onboarding` | `APITOOL` | Complete first admin onboarding |
| `mattermost_connect_web_socket` | `APITOOL` | Open a WebSocket connection |
| `mattermost_convert_bot_to_user` | `APITOOL` | Convert a bot into a user |
| `mattermost_convert_group_message_to_channel` | `APITOOL` | Convert group message to private channel |
| `mattermost_convert_user_to_bot` | `APITOOL` | Convert a user into a bot |
| `mattermost_create_access_control_policy` | `APITOOL` | Create an access control policy |
| `mattermost_create_board` | `APITOOL` | Create a board channel |
| `mattermost_create_bot` | `APITOOL` | Create a bot |
| `mattermost_create_c_p_a_field` | `APITOOL` | Create a Custom Profile Attribute field |
| `mattermost_create_channel` | `APITOOL` | Create a channel |
| `mattermost_create_channel_bookmark` | `APITOOL` | Create channel bookmark |
| `mattermost_create_channel_view` | `APITOOL` | Create channel view |
| `mattermost_create_command` | `APITOOL` | Create a command |
| `mattermost_create_compliance_report` | `APITOOL` | Create report |
| `mattermost_create_data_retention_policy` | `APITOOL` | Create a new granular data retention policy |
| `mattermost_create_direct_channel` | `APITOOL` | Create a direct message channel |
| `mattermost_create_emoji` | `APITOOL` | Create a custom emoji |
| `mattermost_create_group` | `APITOOL` | Create a custom group |
| `mattermost_create_group_channel` | `APITOOL` | Create a group message channel |
| `mattermost_create_incoming_webhook` | `APITOOL` | Create an incoming webhook |
| `mattermost_create_job` | `APITOOL` | Create a new job. |
| `mattermost_create_o_auth_app` | `APITOOL` | Register OAuth app |
| `mattermost_create_outgoing_o_auth_connection` | `APITOOL` | Create a connection |
| `mattermost_create_outgoing_webhook` | `APITOOL` | Create an outgoing webhook |
| `mattermost_create_post` | `APITOOL` | Create a post |
| `mattermost_create_post_ephemeral` | `APITOOL` | Create a ephemeral post |
| `mattermost_create_property_field` | `APITOOL` | Create a property field |
| `mattermost_create_recap` | `APITOOL` | Create a channel recap |
| `mattermost_create_remote_cluster` | `APITOOL` | Create a new remote cluster. |
| `mattermost_create_scheduled_post` | `APITOOL` | Creates a scheduled post |
| `mattermost_create_scheme` | `APITOOL` | Create a scheme |
| `mattermost_create_sidebar_category_for_team_for_user` | `APITOOL` | Create user's sidebar category |
| `mattermost_create_team` | `APITOOL` | Create a team |
| `mattermost_create_terms_of_service` | `APITOOL` | Creates a new terms of service |
| `mattermost_create_upload` | `APITOOL` | Create an upload |
| `mattermost_create_user` | `APITOOL` | Create a user |
| `mattermost_create_user_access_token` | `APITOOL` | Create a user access token |
| `mattermost_database_recycle` | `APITOOL` | Recycle database connections |
| `mattermost_delete_a_i_bridge_test_helper` | `APITOOL` | Reset AI bridge E2E test helper |
| `mattermost_delete_access_control_policy` | `APITOOL` | Delete an access control policy |
| `mattermost_delete_acknowledgement_for_post` | `APITOOL` | Delete a post acknowledgement |
| `mattermost_delete_brand_image` | `APITOOL` | Delete current brand image |
| `mattermost_delete_c_p_a_field` | `APITOOL` | Delete a Custom Profile Attribute field |
| `mattermost_delete_channel` | `APITOOL` | Delete a channel |
| `mattermost_delete_channel_bookmark` | `APITOOL` | Delete channel bookmark |
| `mattermost_delete_channel_view` | `APITOOL` | Delete a channel view |
| `mattermost_delete_command` | `APITOOL` | Delete a command |
| `mattermost_delete_data_retention_policy` | `APITOOL` | Delete a granular data retention policy |
| `mattermost_delete_draft` | `APITOOL` | Delete synced draft |
| `mattermost_delete_draft_for_thread` | `APITOOL` | Delete synced thread draft |
| `mattermost_delete_emoji` | `APITOOL` | Delete a custom emoji |
| `mattermost_delete_export` | `APITOOL` | Delete an export file |
| `mattermost_delete_group` | `APITOOL` | Deletes a custom group |
| `mattermost_delete_group_members` | `APITOOL` | Removes members from a custom group |
| `mattermost_delete_import` | `APITOOL` | Delete an import file |
| `mattermost_delete_incoming_webhook` | `APITOOL` | Delete an incoming webhook |
| `mattermost_delete_ldap_private_certificate` | `APITOOL` | Remove private key |
| `mattermost_delete_ldap_public_certificate` | `APITOOL` | Remove public certificate |
| `mattermost_delete_o_auth_app` | `APITOOL` | Delete an OAuth app |
| `mattermost_delete_outgoing_o_auth_connection` | `APITOOL` | Delete a connection |
| `mattermost_delete_outgoing_webhook` | `APITOOL` | Delete an outgoing webhook |
| `mattermost_delete_post` | `APITOOL` | Delete a post |
| `mattermost_delete_preferences` | `APITOOL` | Delete user's preferences |
| `mattermost_delete_property_field` | `APITOOL` | Delete a property field |
| `mattermost_delete_reaction` | `APITOOL` | Remove a reaction from a post |
| `mattermost_delete_recap` | `APITOOL` | Delete a recap |
| `mattermost_delete_remote_cluster` | `APITOOL` | Delete a remote cluster. |
| `mattermost_delete_saml_idp_certificate` | `APITOOL` | Remove IDP certificate |
| `mattermost_delete_saml_private_certificate` | `APITOOL` | Remove private key |
| `mattermost_delete_saml_public_certificate` | `APITOOL` | Remove public certificate |
| `mattermost_delete_scheduled_post` | `APITOOL` | Delete a scheduled post |
| `mattermost_delete_scheme` | `APITOOL` | Delete a scheme |
| `mattermost_delete_user` | `APITOOL` | Deactivate a user account. |
| `mattermost_demote_user_to_guest` | `APITOOL` | Demote a user to a guest |
| `mattermost_detach_plugin` | `APITOOL` | Detach a reattached plugin process |
| `mattermost_disable_bot` | `APITOOL` | Disable a bot |
| `mattermost_disable_plugin` | `APITOOL` | Disable plugin |
| `mattermost_disable_user_access_token` | `APITOOL` | Disable personal access token |
| `mattermost_do_post_action` | `APITOOL` | Perform a post action |
| `mattermost_download_compliance_report` | `APITOOL` | Download a report |
| `mattermost_download_export` | `APITOOL` | Download an export file |
| `mattermost_download_job` | `APITOOL` | Download the results of a job. |
| `mattermost_download_system_logs` | `APITOOL` | Download system logs |
| `mattermost_enable_bot` | `APITOOL` | Enable a bot |
| `mattermost_enable_plugin` | `APITOOL` | Enable plugin |
| `mattermost_enable_user_access_token` | `APITOOL` | Enable personal access token |
| `mattermost_execute_command` | `APITOOL` | Execute a command |
| `mattermost_generate_c_f_post_report` | `APITOOL` | Generate and download a flagged post report |
| `mattermost_generate_mfa_secret` | `APITOOL` | Generate MFA secret |
| `mattermost_generate_remote_cluster_invite` | `APITOOL` | Generate invite code. |
| `mattermost_generate_support_packet` | `APITOOL` | Download a zip file which contains helpful and useful information for troubleshooting your mattermost instance. |
| `mattermost_get_a_i_bridge_test_helper` | `APITOOL` | Get AI bridge E2E test helper state |
| `mattermost_get_access_control_policy` | `APITOOL` | Get an access control policy |
| `mattermost_get_access_control_policy_autocomplete_fields` | `APITOOL` | Get autocomplete fields for access control policies |
| `mattermost_get_agents` | `APITOOL` | Get available agents |
| `mattermost_get_agents_status` | `APITOOL` | Get agents bridge status |
| `mattermost_get_all_channels` | `APITOOL` | Get a list of all channels |
| `mattermost_get_all_roles` | `APITOOL` | Get a list of all the roles |
| `mattermost_get_all_shared_channels` | `APITOOL` | Get all shared channels for team. |
| `mattermost_get_all_teams` | `APITOOL` | Get teams |
| `mattermost_get_analytics_old` | `APITOOL` | Get analytics |
| `mattermost_get_ancillary_permissions_post` | `APITOOL` | Return all system console subsection ancillary permissions |
| `mattermost_get_applied_schema_migrations` | `APITOOL` | Get applied database schema migrations |
| `mattermost_get_audits` | `APITOOL` | Get audits |
| `mattermost_get_authorization_server_metadata` | `APITOOL` | Get OAuth 2.0 Authorization Server Metadata |
| `mattermost_get_authorized_o_auth_apps_for_user` | `APITOOL` | Get authorized OAuth apps |
| `mattermost_get_bot` | `APITOOL` | Get a bot |
| `mattermost_get_bots` | `APITOOL` | Get bots |
| `mattermost_get_brand_image` | `APITOOL` | Get brand image |
| `mattermost_get_bulk_reactions` | `APITOOL` | Bulk get the reaction for posts |
| `mattermost_get_c_e_l_visual_a_s_t` | `APITOOL` | Get the visual AST for a CEL expression |
| `mattermost_get_c_f_config` | `APITOOL` | Get the system content flagging configuration |
| `mattermost_get_c_f_fields` | `APITOOL` | Get content flagging property fields |
| `mattermost_get_c_f_flag_config` | `APITOOL` | Get content flagging configuration |
| `mattermost_get_c_f_post` | `APITOOL` | Get a flagged post with all its content. |
| `mattermost_get_c_f_post_field_values` | `APITOOL` | Get content flagging property field values for a post |
| `mattermost_get_c_f_team_status` | `APITOOL` | Get content flagging status for a team |
| `mattermost_get_c_p_a_group` | `APITOOL` | Get Custom Profile Attribute property group data |
| `mattermost_get_channel` | `APITOOL` | Get a channel |
| `mattermost_get_channel_access_control_attributes` | `APITOOL` | Get access control attributes for a channel |
| `mattermost_get_channel_by_name` | `APITOOL` | Get a channel by name |
| `mattermost_get_channel_by_name_for_team_name` | `APITOOL` | Get a channel by name and team name |
| `mattermost_get_channel_member` | `APITOOL` | Get channel member |
| `mattermost_get_channel_member_counts_by_group` | `APITOOL` | Channel members counts for each group that has atleast one member in the channel |
| `mattermost_get_channel_members` | `APITOOL` | Get channel members |
| `mattermost_get_channel_members_by_ids` | `APITOOL` | Get channel members by ids |
| `mattermost_get_channel_members_for_user` | `APITOOL` | Get channel memberships and roles for a user |
| `mattermost_get_channel_members_timezones` | `APITOOL` | Get timezones in a channel |
| `mattermost_get_channel_members_with_team_data_for_user` | `APITOOL` | Get all channel members from all teams for a user |
| `mattermost_get_channel_moderations` | `APITOOL` | Get information about channel's moderation. |
| `mattermost_get_channel_policies_for_user` | `APITOOL` | Get the policies which are applied to a user's channels |
| `mattermost_get_channel_stats` | `APITOOL` | Get channel statistics |
| `mattermost_get_channel_unread` | `APITOOL` | Get unread messages |
| `mattermost_get_channel_view` | `APITOOL` | Get a channel view |
| `mattermost_get_channels_for_access_control_policy` | `APITOOL` | Get channels for an access control policy |
| `mattermost_get_channels_for_retention_policy` | `APITOOL` | Get the channels for a granular data retention policy |
| `mattermost_get_channels_for_scheme` | `APITOOL` | Get a page of channels which use this scheme. |
| `mattermost_get_channels_for_team_for_user` | `APITOOL` | Get channels for user |
| `mattermost_get_channels_for_user` | `APITOOL` | Get all channels from all teams |
| `mattermost_get_channels_member_count` | `APITOOL` | Get member counts for multiple channels |
| `mattermost_get_client_config` | `APITOOL` | Get client configuration |
| `mattermost_get_client_license` | `APITOOL` | Get client license |
| `mattermost_get_cloud_customer` | `APITOOL` | Get cloud customer |
| `mattermost_get_cloud_limits` | `APITOOL` | Get cloud workspace limits |
| `mattermost_get_cloud_products` | `APITOOL` | Get cloud products |
| `mattermost_get_cluster_status` | `APITOOL` | Get cluster status |
| `mattermost_get_command_by_id` | `APITOOL` | Get a command |
| `mattermost_get_compliance_report` | `APITOOL` | Get a report |
| `mattermost_get_compliance_reports` | `APITOOL` | Get reports |
| `mattermost_get_config` | `APITOOL` | Get configuration |
| `mattermost_get_data_retention_policies` | `APITOOL` | Get the granular data retention policies |
| `mattermost_get_data_retention_policies_count` | `APITOOL` | Get the number of granular data retention policies |
| `mattermost_get_data_retention_policy` | `APITOOL` | Get the global data retention policy |
| `mattermost_get_data_retention_policy_by_i_d` | `APITOOL` | Get a granular data retention policy |
| `mattermost_get_default_profile_image` | `APITOOL` | Return user's default (generated) profile image |
| `mattermost_get_deleted_channels_for_team` | `APITOOL` | Get deleted channels |
| `mattermost_get_drafts` | `APITOOL` | Get synced drafts for a team |
| `mattermost_get_edit_history_for_post` | `APITOOL` | Get post edit history |
| `mattermost_get_emoji` | `APITOOL` | Get a custom emoji |
| `mattermost_get_emoji_by_name` | `APITOOL` | Get a custom emoji by name |
| `mattermost_get_emoji_image` | `APITOOL` | Get custom emoji image |
| `mattermost_get_emoji_list` | `APITOOL` | Get a list of custom emoji |
| `mattermost_get_emojis_by_names` | `APITOOL` | Get custom emojis by name |
| `mattermost_get_endpoint_for_installation_information` | `APITOOL` | GET endpoint for Installation information |
| `mattermost_get_environment_config` | `APITOOL` | Get configuration made through environment variables |
| `mattermost_get_file` | `APITOOL` | Get a file |
| `mattermost_get_file_info` | `APITOOL` | Get metadata for a file |
| `mattermost_get_file_infos_for_post` | `APITOOL` | Get file info for post |
| `mattermost_get_file_link` | `APITOOL` | Get a public file link |
| `mattermost_get_file_preview` | `APITOOL` | Get a file's preview |
| `mattermost_get_file_public` | `APITOOL` | Get a public file |
| `mattermost_get_file_thumbnail` | `APITOOL` | Get a file's thumbnail |
| `mattermost_get_flagged_posts_for_user` | `APITOOL` | Get a list of flagged posts |
| `mattermost_get_group` | `APITOOL` | Get a group |
| `mattermost_get_group_message_members_common_teams` | `APITOOL` | Get common teams for members of a Group Message. |
| `mattermost_get_group_stats` | `APITOOL` | Get group stats |
| `mattermost_get_group_syncable_for_channel_id` | `APITOOL` | Get a channel syncable for a group |
| `mattermost_get_group_syncable_for_team_id` | `APITOOL` | Get a team syncable for a group |
| `mattermost_get_group_syncables_channels` | `APITOOL` | Get channel syncables for a group |
| `mattermost_get_group_syncables_teams` | `APITOOL` | Get team syncables for a group |
| `mattermost_get_group_users` | `APITOOL` | Get group users |
| `mattermost_get_groups` | `APITOOL` | Get groups |
| `mattermost_get_groups_associated_to_channels_by_team` | `APITOOL` | Get team groups by channels |
| `mattermost_get_groups_by_channel` | `APITOOL` | Get channel groups |
| `mattermost_get_groups_by_names` | `APITOOL` | Get groups by name |
| `mattermost_get_groups_by_team` | `APITOOL` | Get team groups |
| `mattermost_get_groups_by_user_id` | `APITOOL` | Get groups for a userId |
| `mattermost_get_i_p_filters` | `APITOOL` | Get all IP filters |
| `mattermost_get_image_by_url` | `APITOOL` | Get an image by url |
| `mattermost_get_incoming_webhook` | `APITOOL` | Get an incoming webhook |
| `mattermost_get_incoming_webhooks` | `APITOOL` | List incoming webhooks |
| `mattermost_get_invoice_for_subscription_as_pdf` | `APITOOL` | Get cloud invoice PDF |
| `mattermost_get_invoices_for_subscription` | `APITOOL` | Get cloud subscription invoices |
| `mattermost_get_job` | `APITOOL` | Get a job. |
| `mattermost_get_jobs` | `APITOOL` | Get the jobs. |
| `mattermost_get_jobs_by_type` | `APITOOL` | Get the jobs of the given type. |
| `mattermost_get_known_users` | `APITOOL` | Get user IDs of known users |
| `mattermost_get_l_l_m_services` | `APITOOL` | Get available LLM services |
| `mattermost_get_latest_version` | `APITOOL` | Get latest public server release information |
| `mattermost_get_ldap_groups` | `APITOOL` | Returns a list of LDAP groups |
| `mattermost_get_license_load_metric` | `APITOOL` | Get license load metric |
| `mattermost_get_login_type` | `APITOOL` | Get login authentication type |
| `mattermost_get_logs` | `APITOOL` | Get logs |
| `mattermost_get_managed_categories` | `APITOOL` | Get managed category mappings |
| `mattermost_get_marketplace_plugins` | `APITOOL` | Gets all the marketplace plugins |
| `mattermost_get_marketplace_visited_by_admin` | `APITOOL` | Get if the Plugin Marketplace has been visited by at least an admin. |
| `mattermost_get_notices` | `APITOOL` | Get notices for logged in user in specified team |
| `mattermost_get_o_auth_app` | `APITOOL` | Get an OAuth app |
| `mattermost_get_o_auth_app_info` | `APITOOL` | Get info on an OAuth app |
| `mattermost_get_o_auth_apps` | `APITOOL` | Get OAuth apps |
| `mattermost_get_onboarding_complete` | `APITOOL` | Get first admin onboarding completion status |
| `mattermost_get_outgoing_o_auth_connection` | `APITOOL` | Get a connection |
| `mattermost_get_outgoing_webhook` | `APITOOL` | Get an outgoing webhook |
| `mattermost_get_outgoing_webhooks` | `APITOOL` | List outgoing webhooks |
| `mattermost_get_ping` | `APITOOL` | Check system health |
| `mattermost_get_pinned_posts` | `APITOOL` | Get a channel's pinned posts |
| `mattermost_get_plugin_statuses` | `APITOOL` | Get plugins status |
| `mattermost_get_plugins` | `APITOOL` | Get plugins |
| `mattermost_get_post` | `APITOOL` | Get a post |
| `mattermost_get_post_info` | `APITOOL` | Get post info |
| `mattermost_get_post_thread` | `APITOOL` | Get a thread |
| `mattermost_get_posts_around_last_unread` | `APITOOL` | Get posts around oldest unread |
| `mattermost_get_posts_by_ids` | `APITOOL` | Get posts by a list of ids |
| `mattermost_get_posts_for_channel` | `APITOOL` | Get posts for a channel |
| `mattermost_get_posts_for_reporting` | `APITOOL` | Get posts for reporting and compliance purposes using cursor-based pagination |
| `mattermost_get_posts_for_view` | `APITOOL` | Get posts for a view |
| `mattermost_get_posts_usage` | `APITOOL` | Get current usage of posts |
| `mattermost_get_preferences` | `APITOOL` | Get the user's preferences |
| `mattermost_get_preferences_by_category` | `APITOOL` | List a user's preferences by category |
| `mattermost_get_preferences_by_category_by_name` | `APITOOL` | Get a specific user preference |
| `mattermost_get_prev_trial_license` | `APITOOL` | Get last trial license used |
| `mattermost_get_preview_modal_data` | `APITOOL` | Get cloud preview modal data |
| `mattermost_get_private_channels_for_team` | `APITOOL` | Get private channels |
| `mattermost_get_profile_image` | `APITOOL` | Get user's profile image |
| `mattermost_get_property_fields` | `APITOOL` | Get property fields |
| `mattermost_get_property_values` | `APITOOL` | Get property values for a target |
| `mattermost_get_public_channels_by_ids_for_team` | `APITOOL` | Get a list of channels by ids |
| `mattermost_get_public_channels_for_team` | `APITOOL` | Get public channels |
| `mattermost_get_reactions` | `APITOOL` | Get a list of reactions to a post |
| `mattermost_get_recap` | `APITOOL` | Get a specific recap |
| `mattermost_get_recaps_for_user` | `APITOOL` | Get current user's recaps |
| `mattermost_get_recommended_channels_for_team` | `APITOOL` | Get recommended public channels for the current user |
| `mattermost_get_redirect_location` | `APITOOL` | Get redirect location |
| `mattermost_get_remote_cluster` | `APITOOL` | Get a remote cluster. |
| `mattermost_get_remote_cluster_info` | `APITOOL` | Get remote cluster info by ID for user. |
| `mattermost_get_remote_clusters` | `APITOOL` | Get a list of remote clusters. |
| `mattermost_get_role` | `APITOOL` | Get a role |
| `mattermost_get_role_by_name` | `APITOOL` | Get a role |
| `mattermost_get_roles_by_names` | `APITOOL` | Get a list of roles by name |
| `mattermost_get_saml_certificate_status` | `APITOOL` | Get certificate status |
| `mattermost_get_saml_metadata` | `APITOOL` | Get metadata |
| `mattermost_get_saml_metadata_from_idp` | `APITOOL` | Get metadata from Identity Provider |
| `mattermost_get_scheme` | `APITOOL` | Get a scheme |
| `mattermost_get_schemes` | `APITOOL` | Get the schemes. |
| `mattermost_get_server_busy_expires` | `APITOOL` | Get server busy expiry time. |
| `mattermost_get_server_limits` | `APITOOL` | Gets the server limits for the server |
| `mattermost_get_sessions` | `APITOOL` | Get user's sessions |
| `mattermost_get_shared_channel_remotes` | `APITOOL` | Get remote clusters for a shared channel |
| `mattermost_get_shared_channel_remotes_by_remote_cluster` | `APITOOL` | Get shared channel remotes by remote cluster. |
| `mattermost_get_sidebar_categories_for_team_for_user` | `APITOOL` | Get user's sidebar categories |
| `mattermost_get_sidebar_category_for_team_for_user` | `APITOOL` | Get sidebar category |
| `mattermost_get_sidebar_category_order_for_team_for_user` | `APITOOL` | Get user's sidebar category order |
| `mattermost_get_storage_usage` | `APITOOL` | Get the total file storage usage for the instance in bytes. |
| `mattermost_get_subscription` | `APITOOL` | Get cloud subscription |
| `mattermost_get_supported_timezone` | `APITOOL` | Retrieve a list of supported timezones |
| `mattermost_get_system_property_values` | `APITOOL` | Get property values for the system |
| `mattermost_get_team` | `APITOOL` | Get a team |
| `mattermost_get_team_by_name` | `APITOOL` | Get a team by name |
| `mattermost_get_team_icon` | `APITOOL` | Get the team icon |
| `mattermost_get_team_invite_info` | `APITOOL` | Get invite info for a team |
| `mattermost_get_team_member` | `APITOOL` | Get a team member |
| `mattermost_get_team_members` | `APITOOL` | Get team members |
| `mattermost_get_team_members_by_ids` | `APITOOL` | Get team members by ids |
| `mattermost_get_team_members_for_user` | `APITOOL` | Get team members for a user |
| `mattermost_get_team_policies_for_user` | `APITOOL` | Get the policies which are applied to a user's teams |
| `mattermost_get_team_stats` | `APITOOL` | Get a team stats |
| `mattermost_get_team_unread` | `APITOOL` | Get unreads for a team |
| `mattermost_get_teams_for_retention_policy` | `APITOOL` | Get the teams for a granular data retention policy |
| `mattermost_get_teams_for_scheme` | `APITOOL` | Get a page of teams which use this scheme. |
| `mattermost_get_teams_for_user` | `APITOOL` | Get a user's teams |
| `mattermost_get_teams_unread_for_user` | `APITOOL` | Get team unreads for a user |
| `mattermost_get_teams_usage` | `APITOOL` | Get current usage of teams |
| `mattermost_get_terms_of_service` | `APITOOL` | Get latest terms of service |
| `mattermost_get_total_users_stats` | `APITOOL` | Get total count of users in the system |
| `mattermost_get_total_users_stats_filtered` | `APITOOL` | Get total count of users in the system matching the specified filters |
| `mattermost_get_upload` | `APITOOL` | Get an upload session |
| `mattermost_get_uploads_for_user` | `APITOOL` | Get uploads for a user |
| `mattermost_get_user` | `APITOOL` | Get a user |
| `mattermost_get_user_access_token` | `APITOOL` | Get a user access token |
| `mattermost_get_user_access_tokens` | `APITOOL` | Get user access tokens |
| `mattermost_get_user_access_tokens_for_user` | `APITOOL` | Get user access tokens |
| `mattermost_get_user_audits` | `APITOOL` | Get user's audits |
| `mattermost_get_user_by_auth_data` | `APITOOL` | Get a user by auth data |
| `mattermost_get_user_by_email` | `APITOOL` | Get a user by email |
| `mattermost_get_user_by_username` | `APITOOL` | Get a user by username |
| `mattermost_get_user_count_for_reporting` | `APITOOL` | Gets the full count of users that match the filter. |
| `mattermost_get_user_scheduled_posts` | `APITOOL` | Gets all scheduled posts for a user for the specified team.. |
| `mattermost_get_user_status` | `APITOOL` | Get user status |
| `mattermost_get_user_terms_of_service` | `APITOOL` | Fetches user's latest terms of service action if the latest action was for acceptance. |
| `mattermost_get_user_thread` | `APITOOL` | Get a thread followed by the user |
| `mattermost_get_user_threads` | `APITOOL` | Get all threads that user is following |
| `mattermost_get_users` | `APITOOL` | Get users |
| `mattermost_get_users_by_group_channel_ids` | `APITOOL` | Get users by group channels ids |
| `mattermost_get_users_by_ids` | `APITOOL` | Get users by ids |
| `mattermost_get_users_by_usernames` | `APITOOL` | Get users by usernames |
| `mattermost_get_users_for_reporting` | `APITOOL` | Get a list of paged and sorted users for admin reporting purposes |
| `mattermost_get_users_statuses_by_ids` | `APITOOL` | Get user statuses by id |
| `mattermost_get_users_with_invalid_emails` | `APITOOL` | Get users with invalid emails |
| `mattermost_get_webapp_plugins` | `APITOOL` | Get webapp plugins |
| `mattermost_hosted_customer_signup_available` | `APITOOL` | Check hosted signup availability |
| `mattermost_import_team` | `APITOOL` | Import a Team from other application |
| `mattermost_install_marketplace_plugin` | `APITOOL` | Installs a marketplace plugin |
| `mattermost_install_plugin_from_url` | `APITOOL` | Install plugin from url |
| `mattermost_invalidate_caches` | `APITOOL` | Invalidate all the caches |
| `mattermost_invalidate_email_invites` | `APITOOL` | Invalidate active email invitations |
| `mattermost_invite_guests_to_team` | `APITOOL` | Invite guests to the team by email |
| `mattermost_invite_remote_cluster_to_channel` | `APITOOL` | Invites a remote cluster to a channel. |
| `mattermost_invite_users_to_team` | `APITOOL` | Invite users to the team by email |
| `mattermost_is_allowed_to_upgrade_to_enterprise` | `APITOOL` | Check if the user is allowed to upgrade to Enterprise Edition |
| `mattermost_keep_c_f_post` | `APITOOL` | Keep a flagged post |
| `mattermost_link_group_syncable_for_channel` | `APITOOL` | Link a channel to a group |
| `mattermost_link_group_syncable_for_team` | `APITOOL` | Link a team to a group |
| `mattermost_link_ldap_group` | `APITOOL` | Link a LDAP group |
| `mattermost_list_all_c_p_a_fields` | `APITOOL` | List all the Custom Profile Attributes fields |
| `mattermost_list_autocomplete_commands` | `APITOOL` | List autocomplete commands |
| `mattermost_list_c_p_a_values` | `APITOOL` | List Custom Profile Attribute values |
| `mattermost_list_channel_bookmarks_for_channel` | `APITOOL` | Get channel bookmarks for Channel |
| `mattermost_list_channel_views` | `APITOOL` | List channel views |
| `mattermost_list_command_autocomplete_suggestions` | `APITOOL` | List commands' autocomplete data |
| `mattermost_list_commands` | `APITOOL` | List commands for a team |
| `mattermost_list_exports` | `APITOOL` | List export files |
| `mattermost_list_imports` | `APITOOL` | List import files |
| `mattermost_list_outgoing_o_auth_connections` | `APITOOL` | List all connections |
| `mattermost_login` | `APITOOL` | Login to Mattermost server |
| `mattermost_login_by_cws_token` | `APITOOL` | Auto-Login to Mattermost server using CWS token |
| `mattermost_login_intune` | `APITOOL` | Login with Microsoft Intune MAM |
| `mattermost_login_s_s_o_code_exchange` | `APITOOL` | Exchange SSO login code for session tokens |
| `mattermost_login_with_desktop_token` | `APITOOL` | Login using desktop token |
| `mattermost_logout` | `APITOOL` | Logout from the Mattermost server |
| `mattermost_lookup_interactive_dialog` | `APITOOL` | Lookup dialog elements |
| `mattermost_manual_test` | `APITOOL` | Run manual testing helpers |
| `mattermost_mark_all_direct_messages_read` | `APITOOL` | Mark all direct and group messages as read |
| `mattermost_mark_all_team_channels_read` | `APITOOL` | Mark all channels and threads in a team as read |
| `mattermost_mark_channels_read_for_user` | `APITOOL` | Mark multiple channels as read |
| `mattermost_mark_notices_viewed` | `APITOOL` | Update notices as 'viewed' |
| `mattermost_mark_recap_as_read` | `APITOOL` | Mark a recap as read |
| `mattermost_mark_recaps_as_viewed` | `APITOOL` | Mark all of the authenticated user's finished recaps as viewed |
| `mattermost_migrate_auth_to_ldap` | `APITOOL` | Migrate user accounts authentication type to LDAP. |
| `mattermost_migrate_auth_to_saml` | `APITOOL` | Migrate user accounts authentication type to SAML. |
| `mattermost_migrate_config` | `APITOOL` | Migrate config storage |
| `mattermost_migrate_id_ldap` | `APITOOL` | Migrate Id LDAP |
| `mattermost_move_channel` | `APITOOL` | Move a channel |
| `mattermost_move_command` | `APITOOL` | Move a command |
| `mattermost_move_thread` | `APITOOL` | Move a post (and any posts within that post's thread) |
| `mattermost_my_i_p` | `APITOOL` | Get all IP filters |
| `mattermost_notify_admin` | `APITOOL` | Save notify-admin intent |
| `mattermost_open_interactive_dialog` | `APITOOL` | Open a dialog |
| `mattermost_patch_bot` | `APITOOL` | Patch a bot |
| `mattermost_patch_c_p_a_field` | `APITOOL` | Patch a Custom Profile Attribute field |
| `mattermost_patch_c_p_a_values` | `APITOOL` | Patch Custom Profile Attribute values |
| `mattermost_patch_c_p_a_values_for_user` | `APITOOL` | Update custom profile attribute values for a user |
| `mattermost_patch_channel` | `APITOOL` | Patch a channel |
| `mattermost_patch_channel_moderations` | `APITOOL` | Update a channel's moderation settings. |
| `mattermost_patch_config` | `APITOOL` | Patch configuration |
| `mattermost_patch_data_retention_policy` | `APITOOL` | Patch a granular data retention policy |
| `mattermost_patch_group` | `APITOOL` | Patch a group |
| `mattermost_patch_group_syncable_for_channel` | `APITOOL` | Patch a channel syncable for a group |
| `mattermost_patch_group_syncable_for_team` | `APITOOL` | Patch a team syncable for a group |
| `mattermost_patch_post` | `APITOOL` | Patch a post |
| `mattermost_patch_remote_cluster` | `APITOOL` | Patch a remote cluster. |
| `mattermost_patch_role` | `APITOOL` | Patch a role |
| `mattermost_patch_scheme` | `APITOOL` | Patch a scheme |
| `mattermost_patch_team` | `APITOOL` | Patch a team |
| `mattermost_patch_user` | `APITOOL` | Patch a user |
| `mattermost_permanent_delete_all_users` | `APITOOL` | Permanent delete all users |
| `mattermost_pin_post` | `APITOOL` | Pin a post to the channel |
| `mattermost_post_c_f_post_flag` | `APITOOL` | Flag a post |
| `mattermost_post_c_f_post_reviewer` | `APITOOL` | Assign a content reviewer to a flagged post |
| `mattermost_post_endpoint_for_cws_webhooks` | `APITOOL` | POST endpoint for CWS Webhooks |
| `mattermost_post_log` | `APITOOL` | Add log message |
| `mattermost_post_user_recent_custom_status_delete` | `APITOOL` | Delete user's recent custom status |
| `mattermost_presign_export` | `APITOOL` | Create a presigned URL for export download |
| `mattermost_promote_guest_to_user` | `APITOOL` | Promote a guest to user |
| `mattermost_publish_user_typing` | `APITOOL` | Publish a user typing websocket event. |
| `mattermost_purge_elasticsearch_indexes` | `APITOOL` | Purge all Elasticsearch indexes |
| `mattermost_query_logs` | `APITOOL` | Query server logs with filters |
| `mattermost_reattach_plugin` | `APITOOL` | Reattach a plugin process |
| `mattermost_regen_command_token` | `APITOOL` | Generate a new token |
| `mattermost_regen_outgoing_hook_token` | `APITOOL` | Regenerate the token for the outgoing webhook. |
| `mattermost_regenerate_o_auth_app_secret` | `APITOOL` | Regenerate OAuth app secret |
| `mattermost_regenerate_recap` | `APITOOL` | Regenerate a recap |
| `mattermost_regenerate_team_invite_id` | `APITOOL` | Regenerate the Invite ID from a Team |
| `mattermost_register_o_auth_client` | `APITOOL` | Register OAuth client using Dynamic Client Registration |
| `mattermost_register_terms_of_service_action` | `APITOOL` | Records user action when they accept or decline custom terms of service |
| `mattermost_reload_config` | `APITOOL` | Reload configuration |
| `mattermost_remote_cluster_accept_message` | `APITOOL` | Receive a remote cluster message. |
| `mattermost_remote_cluster_confirm_invite` | `APITOOL` | Confirm an invite with a remote cluster. |
| `mattermost_remote_cluster_ping` | `APITOOL` | Receive a ping from a remote cluster. |
| `mattermost_remote_set_profile_image` | `APITOOL` | Set profile image for a remote user. |
| `mattermost_remove_audit_log_certificate` | `APITOOL` | Remove audit log certificate |
| `mattermost_remove_c_f_post` | `APITOOL` | Remove a flagged post |
| `mattermost_remove_channels_from_retention_policy` | `APITOOL` | Delete channels from a granular data retention policy |
| `mattermost_remove_license_file` | `APITOOL` | Remove license file |
| `mattermost_remove_plugin` | `APITOOL` | Remove plugin |
| `mattermost_remove_recent_custom_status` | `APITOOL` | Delete user's recent custom status |
| `mattermost_remove_sidebar_category_for_team_for_user` | `APITOOL` | Delete sidebar category |
| `mattermost_remove_team_icon` | `APITOOL` | Remove the team icon |
| `mattermost_remove_team_member` | `APITOOL` | Remove user from team |
| `mattermost_remove_teams_from_retention_policy` | `APITOOL` | Delete teams from a granular data retention policy |
| `mattermost_remove_user_from_channel` | `APITOOL` | Remove user from channel |
| `mattermost_request_trial_license` | `APITOOL` | Request and install a trial license for your server |
| `mattermost_reset_password` | `APITOOL` | Reset password |
| `mattermost_reset_password_failed_attempts` | `APITOOL` | Reset the failed password attempts for a user |
| `mattermost_reset_saml_auth_data_to_email` | `APITOOL` | Reset AuthData to Email |
| `mattermost_restart_server` | `APITOOL` | Restart the system after an upgrade from Team Edition to Enterprise Edition |
| `mattermost_restore_channel` | `APITOOL` | Restore a channel |
| `mattermost_restore_group` | `APITOOL` | Restore a previously deleted group. |
| `mattermost_restore_post_version` | `APITOOL` | Restores a past version of a post |
| `mattermost_restore_team` | `APITOOL` | Restore a team |
| `mattermost_reveal_post` | `APITOOL` | Reveal a burn-on-read post |
| `mattermost_revoke_all_sessions` | `APITOOL` | Revoke all active sessions for a user |
| `mattermost_revoke_session` | `APITOOL` | Revoke a user session |
| `mattermost_revoke_sessions_from_all_users` | `APITOOL` | Revoke all sessions from all users. |
| `mattermost_revoke_user_access_token` | `APITOOL` | Revoke a user access token |
| `mattermost_rewrite_message` | `APITOOL` | Rewrite a message using AI |
| `mattermost_save_acknowledgement_for_post` | `APITOOL` | Acknowledge a post |
| `mattermost_save_reaction` | `APITOOL` | Create a reaction |
| `mattermost_search_access_control_policies` | `APITOOL` | Search access control policies |
| `mattermost_search_all_channels` | `APITOOL` | Search all private and open type channels across all teams |
| `mattermost_search_c_f_team_reviewers` | `APITOOL` | Search content reviewers in a team |
| `mattermost_search_channels` | `APITOOL` | Search channels |
| `mattermost_search_channels_for_access_control_policy` | `APITOOL` | Search channels for an access control policy |
| `mattermost_search_channels_for_retention_policy` | `APITOOL` | Search for the channels in a granular data retention policy |
| `mattermost_search_emoji` | `APITOOL` | Search custom emoji |
| `mattermost_search_files` | `APITOOL` | Search files across the teams of the current user |
| `mattermost_search_group_channels` | `APITOOL` | Search Group Channels |
| `mattermost_search_posts` | `APITOOL` | Search for team posts |
| `mattermost_search_posts_in_all_teams` | `APITOOL` | Search posts across all teams |
| `mattermost_search_team_files` | `APITOOL` | Search files in a team |
| `mattermost_search_teams` | `APITOOL` | Search teams |
| `mattermost_search_teams_for_retention_policy` | `APITOOL` | Search for the teams in a granular data retention policy |
| `mattermost_search_user_access_tokens` | `APITOOL` | Search tokens |
| `mattermost_search_users` | `APITOOL` | Search users |
| `mattermost_send_password_reset_email` | `APITOOL` | Send password reset email |
| `mattermost_send_verification_email` | `APITOOL` | Send verification email |
| `mattermost_set_a_i_bridge_test_helper` | `APITOOL` | Configure AI bridge E2E test helper |
| `mattermost_set_channel_members` | `APITOOL` | Set channel members |
| `mattermost_set_default_profile_image` | `APITOOL` | Delete user's profile image |
| `mattermost_set_post_reminder` | `APITOOL` | Set a post reminder |
| `mattermost_set_post_unread` | `APITOOL` | Mark as unread from a post. |
| `mattermost_set_profile_image` | `APITOOL` | Set user's profile image |
| `mattermost_set_server_busy` | `APITOOL` | Set the server busy (high load) flag |
| `mattermost_set_team_icon` | `APITOOL` | Sets the team icon |
| `mattermost_set_thread_unread_by_post_id` | `APITOOL` | Mark a thread that user is following as unread based on a post id |
| `mattermost_simulate_access_control_policy_for_users` | `APITOOL` | Simulate an access control policy decision for an explicit user list |
| `mattermost_soft_delete_team` | `APITOOL` | Delete a team |
| `mattermost_start_batch_users_export` | `APITOOL` | Starts a job to export the users to a report file. |
| `mattermost_start_following_thread` | `APITOOL` | Start following a thread |
| `mattermost_stop_following_thread` | `APITOOL` | Stop following a thread |
| `mattermost_submit_interactive_dialog` | `APITOOL` | Submit a dialog |
| `mattermost_submit_performance_report` | `APITOOL` | Report client performance metrics |
| `mattermost_switch_account_type` | `APITOOL` | Switch login method |
| `mattermost_sync_ldap` | `APITOOL` | Sync with LDAP |
| `mattermost_team_exists` | `APITOOL` | Check if team exists |
| `mattermost_team_members_minus_group_members` | `APITOOL` | Team members minus group members. |
| `mattermost_test_access_control_policy_expression` | `APITOOL` | Test an access control policy expression |
| `mattermost_test_elasticsearch` | `APITOOL` | Test Elasticsearch configuration |
| `mattermost_test_email` | `APITOOL` | Send a test email |
| `mattermost_test_ldap` | `APITOOL` | Test LDAP configuration |
| `mattermost_test_ldap_connection` | `APITOOL` | Test LDAP connection with specific settings |
| `mattermost_test_ldap_diagnostics` | `APITOOL` | Test LDAP diagnostics with specific settings |
| `mattermost_test_notification` | `APITOOL` | Send a test notification |
| `mattermost_test_s3_connection` | `APITOOL` | Test AWS S3 connection |
| `mattermost_test_site_u_r_l` | `APITOOL` | Checks the validity of a Site URL |
| `mattermost_trigger_notify_admin_posts` | `APITOOL` | Trigger notify-admin posts |
| `mattermost_unassign_access_control_policy_from_channels` | `APITOOL` | Unassign an access control policy from channels |
| `mattermost_uninvite_remote_cluster_to_channel` | `APITOOL` | Uninvites a remote cluster to a channel. |
| `mattermost_unlink_group_syncable_for_channel` | `APITOOL` | Unlink a channel from a group |
| `mattermost_unlink_group_syncable_for_team` | `APITOOL` | Unlink a team from a group |
| `mattermost_unlink_ldap_group` | `APITOOL` | Delete a link for LDAP group |
| `mattermost_unpin_post` | `APITOOL` | Unpin a post to the channel |
| `mattermost_unset_user_custom_status` | `APITOOL` | Unsets user custom status |
| `mattermost_update_access_control_policies_active` | `APITOOL` | Activate or deactivate access control policies |
| `mattermost_update_access_control_policy_active_status` | `APITOOL` | Activate or deactivate an access control policy |
| `mattermost_update_c_f_config` | `APITOOL` | Update the system content flagging configuration |
| `mattermost_update_channel` | `APITOOL` | Update a channel |
| `mattermost_update_channel_bookmark` | `APITOOL` | Update channel bookmark |
| `mattermost_update_channel_bookmark_sort_order` | `APITOOL` | Update channel bookmark's order |
| `mattermost_update_channel_member_autotranslation` | `APITOOL` | Update channel member autotranslation setting |
| `mattermost_update_channel_member_scheme_roles` | `APITOOL` | Update the scheme-derived roles of a channel member. |
| `mattermost_update_channel_notify_props` | `APITOOL` | Update channel notifications |
| `mattermost_update_channel_privacy` | `APITOOL` | Update channel's privacy |
| `mattermost_update_channel_roles` | `APITOOL` | Update channel roles |
| `mattermost_update_channel_scheme` | `APITOOL` | Set a channel's scheme |
| `mattermost_update_channel_view` | `APITOOL` | Update a channel view |
| `mattermost_update_channel_view_sort_order` | `APITOOL` | Update a channel view's sort order |
| `mattermost_update_cloud_customer` | `APITOOL` | Update cloud customer |
| `mattermost_update_cloud_customer_address` | `APITOOL` | Update cloud customer address |
| `mattermost_update_command` | `APITOOL` | Update a command |
| `mattermost_update_config` | `APITOOL` | Update configuration |
| `mattermost_update_incoming_webhook` | `APITOOL` | Update an incoming webhook |
| `mattermost_update_job_status` | `APITOOL` | Update the status of a job |
| `mattermost_update_marketplace_visited_by_admin` | `APITOOL` | Stores that the Plugin Marketplace has been visited by at least an admin. |
| `mattermost_update_o_auth_app` | `APITOOL` | Update an OAuth app |
| `mattermost_update_outgoing_o_auth_connection` | `APITOOL` | Update a connection |
| `mattermost_update_outgoing_webhook` | `APITOOL` | Update an outgoing webhook |
| `mattermost_update_post` | `APITOOL` | Update a post |
| `mattermost_update_preferences` | `APITOOL` | Save the user's preferences |
| `mattermost_update_property_field` | `APITOOL` | Update a property field |
| `mattermost_update_property_values` | `APITOOL` | Update property values for a target |
| `mattermost_update_scheduled_post` | `APITOOL` | Update a scheduled post |
| `mattermost_update_sidebar_categories_for_team_for_user` | `APITOOL` | Update user's sidebar categories |
| `mattermost_update_sidebar_category_for_team_for_user` | `APITOOL` | Update sidebar category |
| `mattermost_update_sidebar_category_order_for_team_for_user` | `APITOOL` | Update user's sidebar category order |
| `mattermost_update_system_property_values` | `APITOOL` | Update property values for the system |
| `mattermost_update_team` | `APITOOL` | Update a team |
| `mattermost_update_team_member_roles` | `APITOOL` | Update a team member roles |
| `mattermost_update_team_member_scheme_roles` | `APITOOL` | Update the scheme-derived roles of a team member. |
| `mattermost_update_team_privacy` | `APITOOL` | Update teams's privacy |
| `mattermost_update_team_scheme` | `APITOOL` | Set a team's scheme |
| `mattermost_update_thread_read_for_user` | `APITOOL` | Mark a thread that user is following read state to the timestamp |
| `mattermost_update_threads_read_for_user` | `APITOOL` | Mark all threads that user is following as read |
| `mattermost_update_user` | `APITOOL` | Update a user |
| `mattermost_update_user_active` | `APITOOL` | Activate or deactivate a user |
| `mattermost_update_user_auth` | `APITOOL` | Update a user's authentication method |
| `mattermost_update_user_custom_status` | `APITOOL` | Update user custom status |
| `mattermost_update_user_mfa` | `APITOOL` | Update a user's MFA |
| `mattermost_update_user_password` | `APITOOL` | Update a user's password |
| `mattermost_update_user_roles` | `APITOOL` | Update a user's roles |
| `mattermost_update_user_status` | `APITOOL` | Update user status |
| `mattermost_upgrade_to_enterprise` | `APITOOL` | Executes an inplace upgrade from Team Edition to Enterprise Edition |
| `mattermost_upgrade_to_enterprise_status` | `APITOOL` | Get the current status for the inplace upgrade from Team Edition to Enterprise Edition |
| `mattermost_upload_brand_image` | `APITOOL` | Upload brand image |
| `mattermost_upload_data` | `APITOOL` | Perform a file upload |
| `mattermost_upload_file` | `APITOOL` | Upload a file |
| `mattermost_upload_ldap_private_certificate` | `APITOOL` | Upload private key |
| `mattermost_upload_ldap_public_certificate` | `APITOOL` | Upload public certificate |
| `mattermost_upload_license_file` | `APITOOL` | Upload license file |
| `mattermost_upload_plugin` | `APITOOL` | Upload plugin |
| `mattermost_upload_remote_cluster_data` | `APITOOL` | Upload file data for a remote upload session. |
| `mattermost_upload_saml_idp_certificate` | `APITOOL` | Upload IDP certificate |
| `mattermost_upload_saml_private_certificate` | `APITOOL` | Upload private key |
| `mattermost_upload_saml_public_certificate` | `APITOOL` | Upload public certificate |
| `mattermost_upsert_draft` | `APITOOL` | Upsert synced draft |
| `mattermost_validate_business_email` | `APITOOL` | Validate business email |
| `mattermost_validate_expression_against_requester` | `APITOOL` | Validate if the current user matches a CEL expression |
| `mattermost_validate_outgoing_o_auth_connection` | `APITOOL` | Validate a connection configuration |
| `mattermost_validate_workspace_business_email` | `APITOOL` | Validate workspace business email |
| `mattermost_verify_user_email` | `APITOOL` | Verify user email |
| `mattermost_verify_user_email_without_token` | `APITOOL` | Verify user email by ID |
| `mattermost_view_channel` | `APITOOL` | View channel |

</details>

_53 action-routed tool(s) (default) · 578 verbose 1:1 tool(s). Each is enabled unless its `<DOMAIN>TOOL` toggle is set false; `MCP_TOOL_MODE` selects the surface (`condensed` default · `verbose` 1:1 · `both`). Auto-generated — do not edit._
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
1. Set up your Python virtual environment (>= 3.10).
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

`mattermost-mcp` can also run as a **local container** (Docker / Podman / `uv`) or be
consumed from a **remote deployment**. The
[Deployment guide](https://knuckles-team.github.io/mattermost-mcp/deployment/) has full, copy-paste
`mcp_config.json` for all four transports — **stdio**, **streamable-http**,
**local container / uv**, and **remote URL**:

- **Local container / uv** — launch the server from `mcp_config.json` via `uvx`,
  `docker run`, or `podman run`, or point at a local streamable-http container by `url`.
- **Remote URL** — connect to a server deployed behind Caddy at
  `http://mattermost-mcp.arpa/mcp` using the `"url"` key.
<!-- END GENERATED: additional-deployment-options -->

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

Please audit all code changes against ecosystem guidelines in [CONTRIBUTING.md](CONTRIBUTING.md) if available, and run:

```bash
pre-commit run --all-files
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for complete details.


<!-- BEGIN agent-os-genesis-deploy (generated; do not edit between markers) -->

## Deploy with `agent-os-genesis`

This package can be provisioned for you — skill-guided — by the **`agent-os-genesis`**
universal skill (its *single-package deploy mode*): it picks your install method, seeds
secrets to OpenBao/Vault (or `.env`), trusts your enterprise CA, registers the MCP
server, and verifies it — the same machinery that stands up the whole Agent OS, narrowed
to just this package. Ask your agent to **"deploy `mattermost-mcp` with agent-os-genesis"**.

| Install mode | Command |
|------|---------|
| Bare-metal, prod (PyPI) | `uvx mattermost-mcp` · or `uv tool install mattermost-mcp` |
| Bare-metal, dev (editable) | `uv pip install -e ".[all]"` · or `pip install -e ".[all]"` |
| Container, prod | deploy `knucklessg1/mattermost-mcp:latest` via docker-compose / swarm / podman / podman-compose / kubernetes |
| Container, dev (editable) | deploy `docker/compose.dev.yml` (source-mounted at `/src`; edits live on restart) |

Secrets are read-existing + seeded via `vault_sync` — you are only prompted for what's missing.

<!-- END agent-os-genesis-deploy -->
