"""Hand-written MCP tools. Every API operation is served from the client by
agent-connector-sdk (one typed tool per operation, from operation_manifest.json)."""

from mattermost_mcp.mcp.mcp_kg import register_kg_tools

__all__ = ["register_kg_tools"]
