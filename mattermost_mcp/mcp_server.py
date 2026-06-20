"""Main FastMCP server and tool registration."""

import sys
from typing import Any

from agent_utilities.mcp_utilities import (
    create_mcp_server,
    load_config,
    register_tool_surface,
)
from fastmcp.utilities.logging import get_logger
from starlette.requests import Request
from starlette.responses import JSONResponse

from mattermost_mcp.api_client import Api
from mattermost_mcp.auth import get_client
from mattermost_mcp.mcp.mcp_access_control import register_access_control_tools
from mattermost_mcp.mcp.mcp_actions import register_actions_tools
from mattermost_mcp.mcp.mcp_agents import register_agents_tools
from mattermost_mcp.mcp.mcp_audit_logging import register_audit_logging_tools
from mattermost_mcp.mcp.mcp_boards import register_boards_tools
from mattermost_mcp.mcp.mcp_bookmarks import register_bookmarks_tools
from mattermost_mcp.mcp.mcp_bots import register_bots_tools
from mattermost_mcp.mcp.mcp_brand import register_brand_tools
from mattermost_mcp.mcp.mcp_channels import register_channels_tools
from mattermost_mcp.mcp.mcp_cloud import register_cloud_tools
from mattermost_mcp.mcp.mcp_cluster import register_cluster_tools
from mattermost_mcp.mcp.mcp_commands import register_commands_tools
from mattermost_mcp.mcp.mcp_compliance import register_compliance_tools
from mattermost_mcp.mcp.mcp_content_flagging import register_content_flagging_tools
from mattermost_mcp.mcp.mcp_custom_profile_attributes import (
    register_custom_profile_attributes_tools,
)
from mattermost_mcp.mcp.mcp_dataretention import register_dataretention_tools
from mattermost_mcp.mcp.mcp_elasticsearch import register_elasticsearch_tools
from mattermost_mcp.mcp.mcp_emoji import register_emoji_tools
from mattermost_mcp.mcp.mcp_exports import register_exports_tools
from mattermost_mcp.mcp.mcp_files import register_files_tools
from mattermost_mcp.mcp.mcp_groups import register_groups_tools
from mattermost_mcp.mcp.mcp_imports import register_imports_tools
from mattermost_mcp.mcp.mcp_ip_filters import register_ip_filters_tools
from mattermost_mcp.mcp.mcp_jobs import register_jobs_tools
from mattermost_mcp.mcp.mcp_ldap import register_ldap_tools
from mattermost_mcp.mcp.mcp_limits import register_limits_tools
from mattermost_mcp.mcp.mcp_logs import register_logs_tools
from mattermost_mcp.mcp.mcp_metrics import register_metrics_tools
from mattermost_mcp.mcp.mcp_oauth import register_oauth_tools
from mattermost_mcp.mcp.mcp_outgoing_oauth_connections import (
    register_outgoing_oauth_connections_tools,
)
from mattermost_mcp.mcp.mcp_permissions import register_permissions_tools
from mattermost_mcp.mcp.mcp_plugins import register_plugins_tools
from mattermost_mcp.mcp.mcp_posts import register_posts_tools
from mattermost_mcp.mcp.mcp_preferences import register_preferences_tools
from mattermost_mcp.mcp.mcp_properties import register_properties_tools
from mattermost_mcp.mcp.mcp_reactions import register_reactions_tools
from mattermost_mcp.mcp.mcp_recaps import register_recaps_tools
from mattermost_mcp.mcp.mcp_remoteclusters import register_remoteclusters_tools
from mattermost_mcp.mcp.mcp_reports import register_reports_tools
from mattermost_mcp.mcp.mcp_roles import register_roles_tools
from mattermost_mcp.mcp.mcp_saml import register_saml_tools
from mattermost_mcp.mcp.mcp_scheduled_post import register_scheduled_post_tools
from mattermost_mcp.mcp.mcp_schemes import register_schemes_tools
from mattermost_mcp.mcp.mcp_service_terms import register_service_terms_tools
from mattermost_mcp.mcp.mcp_sharedchannels import register_sharedchannels_tools
from mattermost_mcp.mcp.mcp_status import register_status_tools
from mattermost_mcp.mcp.mcp_system import register_system_tools
from mattermost_mcp.mcp.mcp_teams import register_teams_tools
from mattermost_mcp.mcp.mcp_uploads import register_uploads_tools
from mattermost_mcp.mcp.mcp_usage import register_usage_tools
from mattermost_mcp.mcp.mcp_users import register_users_tools
from mattermost_mcp.mcp.mcp_views import register_views_tools
from mattermost_mcp.mcp.mcp_webhooks import register_webhooks_tools

__version__ = "0.15.0"
logger = get_logger(name="mattermost_mcp")

# Keep imported registrars as module attributes so ruff (F401) does not strip
# them and register_tool_surface auto-discovery (vars(module)) can find them.
__all__ = [
    "get_mcp_instance",
    "mcp_server",
    "register_access_control_tools",
    "register_actions_tools",
    "register_agents_tools",
    "register_audit_logging_tools",
    "register_boards_tools",
    "register_bookmarks_tools",
    "register_bots_tools",
    "register_brand_tools",
    "register_channels_tools",
    "register_cloud_tools",
    "register_cluster_tools",
    "register_commands_tools",
    "register_compliance_tools",
    "register_content_flagging_tools",
    "register_custom_profile_attributes_tools",
    "register_dataretention_tools",
    "register_elasticsearch_tools",
    "register_emoji_tools",
    "register_exports_tools",
    "register_files_tools",
    "register_groups_tools",
    "register_imports_tools",
    "register_ip_filters_tools",
    "register_jobs_tools",
    "register_ldap_tools",
    "register_limits_tools",
    "register_logs_tools",
    "register_metrics_tools",
    "register_oauth_tools",
    "register_outgoing_oauth_connections_tools",
    "register_permissions_tools",
    "register_plugins_tools",
    "register_posts_tools",
    "register_preferences_tools",
    "register_properties_tools",
    "register_reactions_tools",
    "register_recaps_tools",
    "register_remoteclusters_tools",
    "register_reports_tools",
    "register_roles_tools",
    "register_saml_tools",
    "register_scheduled_post_tools",
    "register_schemes_tools",
    "register_service_terms_tools",
    "register_sharedchannels_tools",
    "register_status_tools",
    "register_system_tools",
    "register_teams_tools",
    "register_uploads_tools",
    "register_usage_tools",
    "register_users_tools",
    "register_views_tools",
    "register_webhooks_tools",
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
