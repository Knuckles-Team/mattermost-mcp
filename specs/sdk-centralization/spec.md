# CONN-MATTERMOST-MCP-SDK-CENTRALIZATION — Shared SDK capabilities in mattermost-mcp

**Owner:** mattermost-mcp.

See [`requirements.md`](requirements.md) for each row and [`status.json`](status.json) for its generated state.

## Purpose

mattermost-mcp must use the scion-sdk capability for each concern the SDK centralizes. A connector copy of a centralized capability splits policy across the fleet.

## Why a new spec

Search: `git grep -n "SDK" -- specs` found no row that owns SDK capability use in mattermost-mcp. The SDK index spec `SCION-CENTRALIZED-CAPABILITIES` owns the capabilities. This spec owns the connector side of each one.

## Delivery mapping

Component: mattermost-mcp connector

Code: ../../mattermost_mcp/__init__.py

## User Scenarios & Testing

### User Story 1 - Requests use the governed SDK client (Priority: P1)

The fleet operator and the engine rely on this behaviour of `mattermost-mcp`: mattermost-mcp must send every vendor request through the SDK governed HTTP client with its resolved TLS profile and SDK auth. It is proven independently of the other stories.

**Acceptance Scenarios**:

1. **Given** the `mattermost-mcp` connector built from the default branch, **When** `tests/test_sdk_centralization.py::test_request_goes_through_the_governed_client` runs, **Then** a unit test shows the API client holds an httpx client and a request carries the configured credential through a mock transport.

### User Story 2 - SDK floor and dependency set (Priority: P1)

The fleet operator and the engine rely on this behaviour of `mattermost-mcp`: The package must require the compatible public `scion-sdk[mcp]>=0.6.4,<0.7.0` distribution while retaining `scion_sdk` imports and must not pin requests or httpx while nothing imports them directly. It is proven independently of the other stories.

**Acceptance Scenarios**:

1. **Given** the `mattermost-mcp` connector built from the default branch, **When** `tests/test_sdk_centralization.py::test_dependencies_have_no_unused_requests_pin` runs, **Then** pyproject.toml shows the floor and no unused requests pin.

### User Story 3 - Production wiring and hot path (Priority: P1)

The fleet operator and the engine rely on this behaviour of `mattermost-mcp`: `ApiClientBase.__init__` in `mattermost_mcp/api/api_client_base.py` calls `create_http_client`, and every domain client reaches it through `request`. It is proven independently of the other stories.

**Acceptance Scenarios**:

1. **Given** the `mattermost-mcp` connector built from the default branch, **When** `tests/test_sdk_centralization.py::test_transient_status_is_retried_by_the_sdk_client` runs, **Then** a test builds the client with a mock transport, sees a 503 then a 200, and gets one result.

### Edge Cases

- The vendor service is unreachable or rejects the credential: the connector returns the SDK typed error and never a partial result.
- An argument outside the documented inputs is refused with the SDK typed refusal and causes no effect on the vendor service.

## Requirements

- **FR-001**: Requests use the governed SDK client. Rows: `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R001`.
- **FR-002**: SDK floor and dependency set. Rows: `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R002`.
- **FR-003**: Production wiring and hot path. Rows: `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R003`.

## Success Criteria

- **SC-001**: A unit test shows the API client holds an httpx client and a request carries the configured credential through a mock transport. Rows: `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R001`.
- **SC-002**: pyproject.toml shows the floor and no unused requests pin. Rows: `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R002`.
- **SC-003**: A test builds the client with a mock transport, sees a 503 then a 200, and gets one result. Rows: `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R003`.

## Assumptions

- The `mattermost-mcp` package keeps the entry point and module layout named in the rows.
- The shared SDK supplies the transport, authentication, retry and certification helpers the rows reuse.

## Traceability

| Label | Rows | Design section | Test ID | Evidence |
|---|---|---|---|---|
| FR-001 | `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R001` | plan.md Production caller chain | T-001 | tests/test_sdk_centralization.py::test_request_goes_through_the_governed_client |
| FR-002 | `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R002` | plan.md Production caller chain | T-002 | tests/test_sdk_centralization.py::test_dependencies_have_no_unused_requests_pin |
| FR-003 | `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R003` | plan.md Production caller chain | T-003 | tests/test_sdk_centralization.py::test_transient_status_is_retried_by_the_sdk_client |
