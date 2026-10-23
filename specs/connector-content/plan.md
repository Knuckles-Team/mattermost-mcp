# CONN-MATTERMOST-MCP-CONNECTOR-CONTENT — Design and implementation plan

Governing spec: [spec.md](spec.md).

## Architecture

`pyproject.toml` declares `mattermost-mcp` as the connector identity. `create_mcp_server` resolves the packaged content of `mattermost_mcp` from it.
