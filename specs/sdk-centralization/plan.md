# CONN-MATTERMOST-MCP-SDK-CENTRALIZATION — Implementation plan

Governing spec: [spec.md](spec.md). Rows: [requirements.md](requirements.md).

## Summary

This plan states how `mattermost-mcp` delivers the rows of `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION`. The live caller is the `mattermost-mcp` console script. The owner is the `mattermost_mcp` package. The rows reuse the `scion-sdk` helpers and add no second authority. The plan changes no runtime code.

## Technical Context

- **Language/Version**: Python >=3.12
- **Primary Dependencies**: scion-sdk[mcp]>=0.6.4,<0.7.0; fastmcp; further pins in `pyproject.toml` (scion-sdk[mcp]>=0.6.4,<0.7.0)
- **Storage**: N/A, the connector keeps no store of its own
- **Testing**: pytest; each row names the proving test as `path::name`
- **Target Platform**: Linux container and stdio or streamable HTTP MCP clients
- **Project Type**: connector
- **Performance Goals**: N/A, the vendor service sets the latency
- **Constraints**: vendor calls go through the SDK governed client; no connector-local transport
- **Scale/Scope**: 3 active row(s) in this spec

## Constitution Check

- Organization constitution 1.5.0, spec-first change: pass. Every behaviour is a row of this spec with a bound or planned test.
- Repository article R-I, connector scope: pass. The rows stay inside this connector's one external system and reuse the SDK for shared capabilities.

## Project Structure

- `mattermost_mcp/mcp_server.py` (existing)
- `mattermost_mcp/api/api_client_base.py` (existing)
- `tests/test_sdk_centralization.py` (existing)
- `pyproject.toml` (existing)

## Phase 0: Research

No unknowns. Every row names its code and test; the caller chain of each row was read from the code.

## Phase 1: Design

### Summary

This plan states how `mattermost-mcp` delivers the rows of `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION`. The live caller is the `mattermost-mcp` console script. The owner is the `mattermost_mcp` package. The rows reuse the `scion-sdk` helpers and add no second authority. The plan changes no runtime code.

### Technical Context

- **Language/Version**: Python >=3.12
- **Primary Dependencies**: scion-sdk[mcp]>=0.6.4,<0.7.0; fastmcp; further pins in `pyproject.toml` (scion-sdk[mcp]>=0.6.4,<0.7.0)
- **Storage**: N/A, the connector keeps no store of its own
- **Testing**: pytest; each row names the proving test as `path::name`
- **Target Platform**: Linux container and stdio or streamable HTTP MCP clients
- **Project Type**: connector
- **Performance Goals**: N/A, the vendor service sets the latency
- **Constraints**: vendor calls go through the SDK governed client; no connector-local transport
- **Scale/Scope**: 3 active row(s) in this spec

### Constitution Check

- Organization constitution 1.5.0, spec-first change: pass. Every behaviour is a row of this spec with a bound or planned test.
- Repository article R-I, connector scope: pass. The rows stay inside this connector's one external system and reuse the SDK for shared capabilities.

### Project Structure

- `mattermost_mcp/mcp_server.py` (existing)
- `mattermost_mcp/api/api_client_base.py` (existing)
- `tests/test_sdk_centralization.py` (existing)
- `pyproject.toml` (existing)

### Phase 0: Research

No unknowns. Every row names its code and test; the caller chain of each row was read from the code.

### Phase 1: Design

### Summary

This plan states how `mattermost-mcp` delivers the rows of `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION`. The live caller is the `mattermost-mcp` console script. The owner is the `mattermost_mcp` package. The rows reuse the `scion-sdk` helpers and add no second authority. The plan changes no runtime code.

### Technical Context

- **Language/Version**: Python >=3.12
- **Primary Dependencies**: scion-sdk[mcp]>=0.6.4,<0.7.0; fastmcp; further pins in `pyproject.toml` (scion-sdk[mcp]>=0.6.4,<0.7.0)
- **Storage**: N/A, the connector keeps no store of its own
- **Testing**: pytest; each row names the proving test as `path::name`
- **Target Platform**: Linux container and stdio or streamable HTTP MCP clients
- **Project Type**: connector
- **Performance Goals**: N/A, the vendor service sets the latency
- **Constraints**: vendor calls go through the SDK governed client; no connector-local transport
- **Scale/Scope**: 3 active row(s) in this spec

### Constitution Check

- Organization constitution 1.5.0, spec-first change: pass. Every behaviour is a row of this spec with a bound or planned test.
- Repository article R-I, connector scope: pass. The rows stay inside this connector's one external system and reuse the SDK for shared capabilities.

### Project Structure

- `mattermost_mcp/mcp_server.py` (existing)
- `mattermost_mcp/api/api_client_base.py` (existing)
- `tests/test_sdk_centralization.py` (existing)
- `pyproject.toml` (existing)

### Phase 0: Research

No unknowns. Every row names its code and test; the caller chain of each row was read from the code.

### Phase 1: Design

### Summary

This plan states how `mattermost-mcp` delivers the rows of `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION`. The live caller is the `mattermost-mcp` console script. The owner is the `mattermost_mcp` package. The rows reuse the `scion-sdk` helpers and add no second authority. The plan changes no runtime code.

### Technical Context

- **Language/Version**: Python >=3.12
- **Primary Dependencies**: scion-sdk[mcp]>=0.6.4,<0.7.0; fastmcp; further pins in `pyproject.toml` (scion-sdk[mcp]>=0.6.4,<0.7.0)
- **Storage**: N/A, the connector keeps no store of its own
- **Testing**: pytest; each row names the proving test as `path::name`
- **Target Platform**: Linux container and stdio or streamable HTTP MCP clients
- **Project Type**: connector
- **Performance Goals**: N/A, the vendor service sets the latency
- **Constraints**: vendor calls go through the SDK governed client; no connector-local transport
- **Scale/Scope**: 3 active row(s) in this spec

### Constitution Check

- Organization constitution 1.5.0, spec-first change: pass. Every behaviour is a row of this spec with a bound or planned test.
- Repository article R-I, connector scope: pass. The rows stay inside this connector's one external system and reuse the SDK for shared capabilities.

### Project Structure

- `mattermost_mcp/mcp_server.py` (existing)
- `mattermost_mcp/api/api_client_base.py` (existing)
- `tests/test_sdk_centralization.py` (existing)
- `pyproject.toml` (existing)

### Phase 0: Research

No unknowns. Every row names its code and test; the caller chain of each row was read from the code.

### Phase 1: Design

### Summary

This plan states how `mattermost-mcp` delivers the rows of `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION`. The live caller is the `mattermost-mcp` console script. The owner is the `mattermost_mcp` package. The rows reuse the `scion-sdk` helpers and add no second authority. The plan changes no runtime code.

### Technical Context

- **Language/Version**: Python >=3.12
- **Primary Dependencies**: scion-sdk[mcp]>=0.6.4,<0.7.0; fastmcp; further pins in `pyproject.toml` (scion-sdk[mcp]>=0.6.4,<0.7.0)
- **Storage**: N/A, the connector keeps no store of its own
- **Testing**: pytest; each row names the proving test as `path::name`
- **Target Platform**: Linux container and stdio or streamable HTTP MCP clients
- **Project Type**: connector
- **Performance Goals**: N/A, the vendor service sets the latency
- **Constraints**: vendor calls go through the SDK governed client; no connector-local transport
- **Scale/Scope**: 3 active row(s) in this spec

### Constitution Check

- Organization constitution 1.5.0, spec-first change: pass. Every behaviour is a row of this spec with a bound or planned test.
- Repository article R-I, connector scope: pass. The rows stay inside this connector's one external system and reuse the SDK for shared capabilities.

### Project Structure

- `mattermost_mcp/mcp_server.py` (existing)
- `mattermost_mcp/api/api_client_base.py` (existing)
- `tests/test_sdk_centralization.py` (existing)
- `pyproject.toml` (existing)

### Phase 0: Research

No unknowns. Every row names its code and test; the caller chain of each row was read from the code.

### Phase 1: Design

### Summary

This plan states how `mattermost-mcp` delivers the rows of `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION`. The live caller is the `mattermost-mcp` console script. The owner is the `mattermost_mcp` package. The rows reuse the `scion-sdk` helpers and add no second authority. The plan changes no runtime code.

### Technical Context

- **Language/Version**: Python >=3.12
- **Primary Dependencies**: scion-sdk[mcp]>=0.6.4,<0.7.0; fastmcp; further pins in `pyproject.toml` (scion-sdk[mcp]>=0.6.4,<0.7.0)
- **Storage**: N/A, the connector keeps no store of its own
- **Testing**: pytest; each row names the proving test as `path::name`
- **Target Platform**: Linux container and stdio or streamable HTTP MCP clients
- **Project Type**: connector
- **Performance Goals**: N/A, the vendor service sets the latency
- **Constraints**: vendor calls go through the SDK governed client; no connector-local transport
- **Scale/Scope**: 3 active row(s) in this spec

### Constitution Check

- Organization constitution 1.5.0, spec-first change: pass. Every behaviour is a row of this spec with a bound or planned test.
- Repository article R-I, connector scope: pass. The rows stay inside this connector's one external system and reuse the SDK for shared capabilities.

### Project Structure

- `mattermost_mcp/api/api_client_base.py` (existing)

### Phase 0: Research

No unknowns. Every row names its code and test; the caller chain of each row was read from the code.

### Phase 1: Design

### Existing system and reuse

The SDK owns every capability named in the rows (`SCION-CENTRALIZED-CAPABILITIES-R001`, `SCION-CENTRALIZED-CAPABILITIES-R003`, `SCION-CENTRALIZED-CAPABILITIES-R008`). mattermost-mcp adds no module that repeats one. Each row deletes connector code and calls the SDK module.

### Live call path

`ApiClientBase.__init__` in `mattermost_mcp/api/api_client_base.py` calls `create_http_client`. Every domain client and MCP tool calls `ApiClientBase.request`.

### Compatibility

Tool names, arguments, URL joining, error types and result shapes stay identical.

### Phase 2: Task approach

`tasks.md` holds one task per row, producer first. Rows that depend on none run in parallel. A task is checked when its `Spec:` trailer is on the default branch.

### Complexity Tracking

None. The constitution check passed.

### Build contract

- `pre-commit run --all-files` runs ruff check, ruff format, the shared `connector-standard`, `spec`, `secrets` and `dependency-readiness` gates at the pinned shared revision.
- `uv run pytest tests` runs the proving tests; the shared complexity, duplication and KISS gates apply their org thresholds and this repository sets no local override.
- A change adds no scanner suppression and no duplicate implementation of an SDK helper.

### Production caller chain


### Cross-repo seams

None. The rows depend only on the published `scion-sdk` package, which the connector imports.

### Phase 2: Task approach

`tasks.md` holds one task per row, producer first. Rows that depend on none run in parallel. A task is checked when its `Spec:` trailer is on the default branch.

### Complexity Tracking

None. The constitution check passed.

### Build contract

- `pre-commit run --all-files` runs ruff check, ruff format, the shared `connector-standard`, `spec`, `secrets` and `dependency-readiness` gates at the pinned shared revision.
- `uv run pytest tests` runs the proving tests; the shared complexity, duplication and KISS gates apply their org thresholds and this repository sets no local override.
- A change adds no scanner suppression and no duplicate implementation of an SDK helper.

### Production caller chain

- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R001`: an MCP tool of `mattermost_mcp/mcp_server.py` calls a domain client under `mattermost_mcp/api/`, which calls `ApiClientBase.request` (`mattermost_mcp/api/api_client_base.py:61`); the session was built by `create_http_client` in `ApiClientBase.__init__` (`mattermost_mcp/api/api_client_base.py:47`).
- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R002`: the installer and the `dependency-readiness` pre-commit gate read `[project] dependencies` in `pyproject.toml`.
- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R003`: an MCP tool of `mattermost_mcp/mcp_server.py` calls a domain client, which calls `ApiClientBase.request` (`mattermost_mcp/api/api_client_base.py:61`); the governed session built at `mattermost_mcp/api/api_client_base.py:47` retries a transient status under the SDK policy.

### Cross-repo seams

None. The rows depend only on the published `scion-sdk` package, which the connector imports.

### Phase 2: Task approach

`tasks.md` holds one task per row, producer first. Rows that depend on none run in parallel. A task is checked when its `Spec:` trailer is on the default branch.

### Complexity Tracking

None. The constitution check passed.

### Build contract

- `pre-commit run --all-files` runs ruff check, ruff format, the shared `connector-standard`, `spec`, `secrets` and `dependency-readiness` gates at the pinned shared revision.
- `uv run pytest tests` runs the proving tests; the shared complexity, duplication and KISS gates apply their org thresholds and this repository sets no local override.
- A change adds no scanner suppression and no duplicate implementation of an SDK helper.

### Production caller chain

- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R001`: an MCP tool of `mattermost_mcp/mcp_server.py` calls a domain client under `mattermost_mcp/api/`, which calls `ApiClientBase.request` (`mattermost_mcp/api/api_client_base.py:61`); the session was built by `create_http_client` in `ApiClientBase.__init__` (`mattermost_mcp/api/api_client_base.py:47`).
- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R002`: the installer and the `dependency-readiness` pre-commit gate read `[project] dependencies` in `pyproject.toml`.
- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R003`: an MCP tool of `mattermost_mcp/mcp_server.py` calls a domain client, which calls `ApiClientBase.request` (`mattermost_mcp/api/api_client_base.py:61`); the governed session built at `mattermost_mcp/api/api_client_base.py:47` retries a transient status under the SDK policy.

### Cross-repo seams

None. The rows depend only on the published `scion-sdk` package, which the connector imports.

### Phase 2: Task approach

`tasks.md` holds one task per row, producer first. Rows that depend on none run in parallel. A task is checked when its `Spec:` trailer is on the default branch.

### Complexity Tracking

None. The constitution check passed.

### Build contract

- `pre-commit run --all-files` runs ruff check, ruff format, the shared `connector-standard`, `spec`, `secrets` and `dependency-readiness` gates at the pinned shared revision.
- `uv run pytest tests` runs the proving tests; the shared complexity, duplication and KISS gates apply their org thresholds and this repository sets no local override.
- A change adds no scanner suppression and no duplicate implementation of an SDK helper.

### Production caller chain

- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R001`: an MCP tool of `mattermost_mcp/mcp_server.py` calls a domain client under `mattermost_mcp/api/`, which calls `ApiClientBase.request` (`mattermost_mcp/api/api_client_base.py:61`); the session was built by `create_http_client` in `ApiClientBase.__init__` (`mattermost_mcp/api/api_client_base.py:47`).
- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R002`: the installer and the `dependency-readiness` pre-commit gate read `[project] dependencies` in `pyproject.toml`.
- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R003`: an MCP tool of `mattermost_mcp/mcp_server.py` calls a domain client, which calls `ApiClientBase.request` (`mattermost_mcp/api/api_client_base.py:61`); the governed session built at `mattermost_mcp/api/api_client_base.py:47` retries a transient status under the SDK policy.

### Cross-repo seams

None. The rows depend only on the published `scion-sdk` package, which the connector imports.

### Phase 2: Task approach

`tasks.md` holds one task per row, producer first. Rows that depend on none run in parallel. A task is checked when its `Spec:` trailer is on the default branch.

### Complexity Tracking

None. The constitution check passed.

### Build contract

- `pre-commit run --all-files` runs ruff check, ruff format, the shared `connector-standard`, `spec`, `secrets` and `dependency-readiness` gates at the pinned shared revision.
- `uv run pytest tests` runs the proving tests; the shared complexity, duplication and KISS gates apply their org thresholds and this repository sets no local override.
- A change adds no scanner suppression and no duplicate implementation of an SDK helper.

### Production caller chain

- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R001`: an MCP tool of `mattermost_mcp/mcp_server.py` calls a domain client under `mattermost_mcp/api/`, which calls `ApiClientBase.request` (`mattermost_mcp/api/api_client_base.py:61`); the session was built by `create_http_client` in `ApiClientBase.__init__` (`mattermost_mcp/api/api_client_base.py:47`).
- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R002`: the installer and the `dependency-readiness` pre-commit gate read `[project] dependencies` in `pyproject.toml`.
- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R003`: an MCP tool of `mattermost_mcp/mcp_server.py` calls a domain client, which calls `ApiClientBase.request` (`mattermost_mcp/api/api_client_base.py:61`); the governed session built at `mattermost_mcp/api/api_client_base.py:47` retries a transient status under the SDK policy.

### Cross-repo seams

None. The rows depend only on the published `scion-sdk` package, which the connector imports.

## Phase 2: Task approach

`tasks.md` holds one task per row, producer first. Rows that depend on none run in parallel. A task is checked when its `Spec:` trailer is on the default branch.

## Complexity Tracking

None. The constitution check passed.

## Build contract

- `pre-commit run --all-files` runs ruff check, ruff format, the shared `connector-standard`, `spec`, `secrets` and `dependency-readiness` gates at the pinned shared revision.
- `uv run pytest tests` runs the proving tests; the shared complexity, duplication and KISS gates apply their org thresholds and this repository sets no local override.
- A change adds no scanner suppression and no duplicate implementation of an SDK helper.

## Production caller chain

- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R001`: an MCP tool of `mattermost_mcp/mcp_server.py` calls a domain client under `mattermost_mcp/api/`, which calls `ApiClientBase.request` (`mattermost_mcp/api/api_client_base.py:61`); the session was built by `create_http_client` in `ApiClientBase.__init__` (`mattermost_mcp/api/api_client_base.py:47`).
- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R002`: the installer and the `dependency-readiness` pre-commit gate read `[project] dependencies` in `pyproject.toml`.
- `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R003`: an MCP tool of `mattermost_mcp/mcp_server.py` calls a domain client, which calls `ApiClientBase.request` (`mattermost_mcp/api/api_client_base.py:61`); the governed session built at `mattermost_mcp/api/api_client_base.py:47` retries a transient status under the SDK policy.

## Cross-repo seams

None. The rows depend only on the published `scion-sdk` package, which the connector imports.
