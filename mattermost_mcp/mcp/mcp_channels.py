"""MCP tools for channels operations."""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_channels_tools(mcp: FastMCP):
    """Register Mattermost MCP channels tools.
    CONCEPT:MM-001
    """

    @mcp.tool(tags={"channels"})
    async def mattermost_mcp_channels(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_channels', 'create_channel'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP channels operations."""
        if ctx:
            await ctx.info("Executing channels operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_channels":
            return client.get_channels(**kwargs)
        if action == "create_channel":
            return client.create_channel(**kwargs)

        raise ValueError(f"Unknown action: {action}")
