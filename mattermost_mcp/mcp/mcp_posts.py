"""MCP tools for posts operations."""
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field
from mattermost_mcp.auth import get_client

def register_posts_tools(mcp: FastMCP):
    """Register Mattermost MCP posts tools.
    CONCEPT:MM-001
    """
    @mcp.tool(tags={"posts"})
    async def mattermost_mcp_posts(
        action: str = Field(description="Action to perform. Must be one of: 'create_post', 'delete_post'"),
        params_json: str = Field(default="{}", description="JSON string of parameters."),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        """Manage Mattermost MCP posts operations."""
        if ctx:
            await ctx.info("Executing posts operations...")
        import json
        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        
        if action == "create_post":
            return client.create_post(**kwargs)
        if action == "delete_post":
            return client.delete_post(**kwargs)
        
        raise ValueError(f"Unknown action: {action}")
