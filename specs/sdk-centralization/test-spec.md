# CONN-MATTERMOST-MCP-SDK-CENTRALIZATION — Test specification

Governing spec: [spec.md](spec.md).

| Test ID | Requirement | Proving test | Expected observation |
|---|---|---|---|
| T-001 | `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R001` | `tests/test_sdk_centralization.py::test_request_goes_through_the_governed_client` | A unit test shows the API client holds an httpx client and a request carries the configured credential through a mock transport |
| T-002 | `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R002` | `tests/test_sdk_centralization.py::test_dependencies_have_no_unused_requests_pin` | pyproject.toml shows the floor and no unused requests pin |
| T-003 | `CONN-MATTERMOST-MCP-SDK-CENTRALIZATION-R003` | `tests/test_sdk_centralization.py::test_transient_status_is_retried_by_the_sdk_client` | A test builds the client with a mock transport, sees a 503 then a 200, and gets one result |

## Negative and boundary cases

Each proving test above includes the refusal or error case that its row names. A vendor outage or an unauthorised call must return the SDK typed error.

## Quality and release proof

Run `uv run pytest tests` and `pre-commit run --all-files` from the repository root. A planned test is added by the code change that lands the row.
