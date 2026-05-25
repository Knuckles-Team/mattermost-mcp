import warnings
import logging
import os
import sys
from typing import Any
from fastmcp import Context, FastMCP
from fastmcp.utilities.logging import get_logger
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv

from mattermost_mcp.mcp.mcp_teams import register_teams_tools
from mattermost_mcp.mcp.mcp_channels import register_channels_tools
from mattermost_mcp.mcp.mcp_posts import register_posts_tools
from mattermost_mcp.mcp.mcp_users import register_users_tools

__version__ = "0.15.0"
logger = get_logger(name="mattermost_mcp")

def get_mcp_instance() -> tuple[Any, ...]:
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="Mattermost MCP MCP",
        version=__version__,
        instructions="Mattermost MCP MCP Server - Managed dynamic operations.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    
    DEFAULT_TEAMSTOOL = to_boolean(os.getenv("TEAMSTOOL", "True"))
    if DEFAULT_TEAMSTOOL:
        register_teams_tools(mcp)
    
    DEFAULT_CHANNELSTOOL = to_boolean(os.getenv("CHANNELSTOOL", "True"))
    if DEFAULT_CHANNELSTOOL:
        register_channels_tools(mcp)
    
    DEFAULT_POSTSTOOL = to_boolean(os.getenv("POSTSTOOL", "True"))
    if DEFAULT_POSTSTOOL:
        register_posts_tools(mcp)
    
    DEFAULT_USERSTOOL = to_boolean(os.getenv("USERSTOOL", "True"))
    if DEFAULT_USERSTOOL:
        register_users_tools(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares

def mcp_server() -> None:
    mcp, args, middlewares = get_mcp_instance()
    print(f"Mattermost MCP MCP v{__version__}", file=sys.stderr)
    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    else:
        mcp.run(transport="stdio")

if __name__ == "__main__":
    mcp_server()
