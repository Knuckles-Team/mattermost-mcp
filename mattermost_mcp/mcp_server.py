"""Main FastMCP server and tool registration."""

import os
import sys
from typing import Any

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv
from fastmcp.utilities.logging import get_logger
from starlette.requests import Request
from starlette.responses import JSONResponse

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

    DEFAULT_ACCESS_CONTROLTOOL = to_boolean(os.getenv("ACCESS_CONTROLTOOL", "True"))
    if DEFAULT_ACCESS_CONTROLTOOL:
        register_access_control_tools(mcp)

    DEFAULT_ACTIONSTOOL = to_boolean(os.getenv("ACTIONSTOOL", "True"))
    if DEFAULT_ACTIONSTOOL:
        register_actions_tools(mcp)

    DEFAULT_AGENTSTOOL = to_boolean(os.getenv("AGENTSTOOL", "True"))
    if DEFAULT_AGENTSTOOL:
        register_agents_tools(mcp)

    DEFAULT_AUDIT_LOGGINGTOOL = to_boolean(os.getenv("AUDIT_LOGGINGTOOL", "True"))
    if DEFAULT_AUDIT_LOGGINGTOOL:
        register_audit_logging_tools(mcp)

    DEFAULT_BOARDSTOOL = to_boolean(os.getenv("BOARDSTOOL", "True"))
    if DEFAULT_BOARDSTOOL:
        register_boards_tools(mcp)

    DEFAULT_BOOKMARKSTOOL = to_boolean(os.getenv("BOOKMARKSTOOL", "True"))
    if DEFAULT_BOOKMARKSTOOL:
        register_bookmarks_tools(mcp)

    DEFAULT_BOTSTOOL = to_boolean(os.getenv("BOTSTOOL", "True"))
    if DEFAULT_BOTSTOOL:
        register_bots_tools(mcp)

    DEFAULT_BRANDTOOL = to_boolean(os.getenv("BRANDTOOL", "True"))
    if DEFAULT_BRANDTOOL:
        register_brand_tools(mcp)

    DEFAULT_CHANNELSTOOL = to_boolean(os.getenv("CHANNELSTOOL", "True"))
    if DEFAULT_CHANNELSTOOL:
        register_channels_tools(mcp)

    DEFAULT_CLOUDTOOL = to_boolean(os.getenv("CLOUDTOOL", "True"))
    if DEFAULT_CLOUDTOOL:
        register_cloud_tools(mcp)

    DEFAULT_CLUSTERTOOL = to_boolean(os.getenv("CLUSTERTOOL", "True"))
    if DEFAULT_CLUSTERTOOL:
        register_cluster_tools(mcp)

    DEFAULT_COMMANDSTOOL = to_boolean(os.getenv("COMMANDSTOOL", "True"))
    if DEFAULT_COMMANDSTOOL:
        register_commands_tools(mcp)

    DEFAULT_COMPLIANCETOOL = to_boolean(os.getenv("COMPLIANCETOOL", "True"))
    if DEFAULT_COMPLIANCETOOL:
        register_compliance_tools(mcp)

    DEFAULT_CONTENT_FLAGGINGTOOL = to_boolean(os.getenv("CONTENT_FLAGGINGTOOL", "True"))
    if DEFAULT_CONTENT_FLAGGINGTOOL:
        register_content_flagging_tools(mcp)

    DEFAULT_CUSTOM_PROFILE_ATTRIBUTESTOOL = to_boolean(
        os.getenv("CUSTOM_PROFILE_ATTRIBUTESTOOL", "True")
    )
    if DEFAULT_CUSTOM_PROFILE_ATTRIBUTESTOOL:
        register_custom_profile_attributes_tools(mcp)

    DEFAULT_DATARETENTIONTOOL = to_boolean(os.getenv("DATARETENTIONTOOL", "True"))
    if DEFAULT_DATARETENTIONTOOL:
        register_dataretention_tools(mcp)

    DEFAULT_ELASTICSEARCHTOOL = to_boolean(os.getenv("ELASTICSEARCHTOOL", "True"))
    if DEFAULT_ELASTICSEARCHTOOL:
        register_elasticsearch_tools(mcp)

    DEFAULT_EMOJITOOL = to_boolean(os.getenv("EMOJITOOL", "True"))
    if DEFAULT_EMOJITOOL:
        register_emoji_tools(mcp)

    DEFAULT_EXPORTSTOOL = to_boolean(os.getenv("EXPORTSTOOL", "True"))
    if DEFAULT_EXPORTSTOOL:
        register_exports_tools(mcp)

    DEFAULT_FILESTOOL = to_boolean(os.getenv("FILESTOOL", "True"))
    if DEFAULT_FILESTOOL:
        register_files_tools(mcp)

    DEFAULT_GROUPSTOOL = to_boolean(os.getenv("GROUPSTOOL", "True"))
    if DEFAULT_GROUPSTOOL:
        register_groups_tools(mcp)

    DEFAULT_IMPORTSTOOL = to_boolean(os.getenv("IMPORTSTOOL", "True"))
    if DEFAULT_IMPORTSTOOL:
        register_imports_tools(mcp)

    DEFAULT_IP_FILTERSTOOL = to_boolean(os.getenv("IP_FILTERSTOOL", "True"))
    if DEFAULT_IP_FILTERSTOOL:
        register_ip_filters_tools(mcp)

    DEFAULT_JOBSTOOL = to_boolean(os.getenv("JOBSTOOL", "True"))
    if DEFAULT_JOBSTOOL:
        register_jobs_tools(mcp)

    DEFAULT_LDAPTOOL = to_boolean(os.getenv("LDAPTOOL", "True"))
    if DEFAULT_LDAPTOOL:
        register_ldap_tools(mcp)

    DEFAULT_LIMITSTOOL = to_boolean(os.getenv("LIMITSTOOL", "True"))
    if DEFAULT_LIMITSTOOL:
        register_limits_tools(mcp)

    DEFAULT_LOGSTOOL = to_boolean(os.getenv("LOGSTOOL", "True"))
    if DEFAULT_LOGSTOOL:
        register_logs_tools(mcp)

    DEFAULT_METRICSTOOL = to_boolean(os.getenv("METRICSTOOL", "True"))
    if DEFAULT_METRICSTOOL:
        register_metrics_tools(mcp)

    DEFAULT_OAUTHTOOL = to_boolean(os.getenv("OAUTHTOOL", "True"))
    if DEFAULT_OAUTHTOOL:
        register_oauth_tools(mcp)

    DEFAULT_OUTGOING_OAUTH_CONNECTIONSTOOL = to_boolean(
        os.getenv("OUTGOING_OAUTH_CONNECTIONSTOOL", "True")
    )
    if DEFAULT_OUTGOING_OAUTH_CONNECTIONSTOOL:
        register_outgoing_oauth_connections_tools(mcp)

    DEFAULT_PERMISSIONSTOOL = to_boolean(os.getenv("PERMISSIONSTOOL", "True"))
    if DEFAULT_PERMISSIONSTOOL:
        register_permissions_tools(mcp)

    DEFAULT_PLUGINSTOOL = to_boolean(os.getenv("PLUGINSTOOL", "True"))
    if DEFAULT_PLUGINSTOOL:
        register_plugins_tools(mcp)

    DEFAULT_POSTSTOOL = to_boolean(os.getenv("POSTSTOOL", "True"))
    if DEFAULT_POSTSTOOL:
        register_posts_tools(mcp)

    DEFAULT_PREFERENCESTOOL = to_boolean(os.getenv("PREFERENCESTOOL", "True"))
    if DEFAULT_PREFERENCESTOOL:
        register_preferences_tools(mcp)

    DEFAULT_PROPERTIESTOOL = to_boolean(os.getenv("PROPERTIESTOOL", "True"))
    if DEFAULT_PROPERTIESTOOL:
        register_properties_tools(mcp)

    DEFAULT_REACTIONSTOOL = to_boolean(os.getenv("REACTIONSTOOL", "True"))
    if DEFAULT_REACTIONSTOOL:
        register_reactions_tools(mcp)

    DEFAULT_RECAPSTOOL = to_boolean(os.getenv("RECAPSTOOL", "True"))
    if DEFAULT_RECAPSTOOL:
        register_recaps_tools(mcp)

    DEFAULT_REMOTECLUSTERSTOOL = to_boolean(os.getenv("REMOTECLUSTERSTOOL", "True"))
    if DEFAULT_REMOTECLUSTERSTOOL:
        register_remoteclusters_tools(mcp)

    DEFAULT_REPORTSTOOL = to_boolean(os.getenv("REPORTSTOOL", "True"))
    if DEFAULT_REPORTSTOOL:
        register_reports_tools(mcp)

    DEFAULT_ROLESTOOL = to_boolean(os.getenv("ROLESTOOL", "True"))
    if DEFAULT_ROLESTOOL:
        register_roles_tools(mcp)

    DEFAULT_SAMLTOOL = to_boolean(os.getenv("SAMLTOOL", "True"))
    if DEFAULT_SAMLTOOL:
        register_saml_tools(mcp)

    DEFAULT_SCHEDULED_POSTTOOL = to_boolean(os.getenv("SCHEDULED_POSTTOOL", "True"))
    if DEFAULT_SCHEDULED_POSTTOOL:
        register_scheduled_post_tools(mcp)

    DEFAULT_SCHEMESTOOL = to_boolean(os.getenv("SCHEMESTOOL", "True"))
    if DEFAULT_SCHEMESTOOL:
        register_schemes_tools(mcp)

    DEFAULT_SERVICE_TERMSTOOL = to_boolean(os.getenv("SERVICE_TERMSTOOL", "True"))
    if DEFAULT_SERVICE_TERMSTOOL:
        register_service_terms_tools(mcp)

    DEFAULT_SHAREDCHANNELSTOOL = to_boolean(os.getenv("SHAREDCHANNELSTOOL", "True"))
    if DEFAULT_SHAREDCHANNELSTOOL:
        register_sharedchannels_tools(mcp)

    DEFAULT_STATUSTOOL = to_boolean(os.getenv("STATUSTOOL", "True"))
    if DEFAULT_STATUSTOOL:
        register_status_tools(mcp)

    DEFAULT_SYSTEMTOOL = to_boolean(os.getenv("SYSTEMTOOL", "True"))
    if DEFAULT_SYSTEMTOOL:
        register_system_tools(mcp)

    DEFAULT_TEAMSTOOL = to_boolean(os.getenv("TEAMSTOOL", "True"))
    if DEFAULT_TEAMSTOOL:
        register_teams_tools(mcp)

    DEFAULT_UPLOADSTOOL = to_boolean(os.getenv("UPLOADSTOOL", "True"))
    if DEFAULT_UPLOADSTOOL:
        register_uploads_tools(mcp)

    DEFAULT_USAGETOOL = to_boolean(os.getenv("USAGETOOL", "True"))
    if DEFAULT_USAGETOOL:
        register_usage_tools(mcp)

    DEFAULT_USERSTOOL = to_boolean(os.getenv("USERSTOOL", "True"))
    if DEFAULT_USERSTOOL:
        register_users_tools(mcp)

    DEFAULT_VIEWSTOOL = to_boolean(os.getenv("VIEWSTOOL", "True"))
    if DEFAULT_VIEWSTOOL:
        register_views_tools(mcp)

    DEFAULT_WEBHOOKSTOOL = to_boolean(os.getenv("WEBHOOKSTOOL", "True"))
    if DEFAULT_WEBHOOKSTOOL:
        register_webhooks_tools(mcp)

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
