"""MCP tools for users operations."""
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field
from mattermost_mcp.auth import get_client

def register_users_tools(mcp: FastMCP):
    """Register Mattermost MCP users tools.
    CONCEPT:MM-001
    """
    @mcp.tool(tags={"users"})
    async def mattermost_mcp_users(
        action: str = Field(description="Action to perform. Must be one of: 'get_users', 'get_me'"),
        params_json: str = Field(default="{}", description="JSON string of parameters."),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP users operations."""
        if ctx:
            await ctx.info("Executing users operations...")
        import json
        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        
        if action == "get_users":
            return client.get_users(**kwargs)
        if action == "get_me":
            return client.get_me(**kwargs)
        
        raise ValueError(f"Unknown action: {action}")
