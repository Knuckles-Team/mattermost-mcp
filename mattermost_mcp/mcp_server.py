"""Main FastMCP server and tool registration."""

import json
import sys
from pathlib import Path
from typing import Any

from agent_connector_sdk.config import load_config
from agent_connector_sdk.mcp.server import create_mcp_server
from agent_connector_sdk.mcp.tool_surface import register_tool_surface
from fastmcp.utilities.logging import get_logger
from starlette.requests import Request
from starlette.responses import JSONResponse

from mattermost_mcp.api_client import Api
from mattermost_mcp.auth import get_client
from mattermost_mcp.mcp.mcp_kg import register_kg_tools

__version__ = "2.4.1"
logger = get_logger(name="mattermost_mcp")

#: Typed inputs for every client method, generated from the Mattermost OpenAPI
#: source by scripts/build_operation_manifest.py (path, query and JSON body fields).
OPERATION_MANIFEST = json.loads(
    (Path(__file__).with_name("operation_manifest.json")).read_text(encoding="utf-8")
)

# Keep imported registrars as module attributes so ruff (F401) does not strip
# them and register_tool_surface auto-discovery (vars(module)) can find them.
__all__ = [
    "get_mcp_instance",
    "mcp_server",
    "register_kg_tools",
]


def get_mcp_instance() -> tuple[Any, ...]:
    load_config()
    args, mcp, middlewares = create_mcp_server(
        name="Mattermost MCP MCP",
        version=__version__,
        instructions="Mattermost MCP MCP Server - Managed dynamic operations.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    register_tool_surface(
        mcp,
        client_cls=Api,
        get_client=get_client,
        service="mattermost-mcp",
        tools_module=sys.modules[__name__],
        manifest=OPERATION_MANIFEST,
    )

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
