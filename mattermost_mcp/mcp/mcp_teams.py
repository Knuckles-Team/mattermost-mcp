"""MCP tools for teams operations."""

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_teams_tools(mcp: FastMCP):
    """Register Mattermost MCP teams tools.
    CONCEPT:MM-001
    """

    @mcp.tool(tags={"teams"})
    async def mattermost_mcp_teams(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_teams', 'get_team_members'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP teams operations."""
        if ctx:
            await ctx.info("Executing teams operations...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_teams":
            return client.get_teams(**kwargs)
        if action == "get_team_members":
            return client.get_team_members(**kwargs)

        raise ValueError(f"Unknown action: {action}")
