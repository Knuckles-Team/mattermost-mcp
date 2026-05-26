"""CONCEPT:MM-001 Dynamic client facade orchestration and resource mappings."""

# !/usr/bin/env python
from mattermost_mcp.api.api_client_access_control import Api as AccessControlApi
from mattermost_mcp.api.api_client_actions import Api as ActionsApi
from mattermost_mcp.api.api_client_agents import Api as AgentsApi
from mattermost_mcp.api.api_client_audit_logging import Api as AuditLoggingApi
from mattermost_mcp.api.api_client_boards import Api as BoardsApi
from mattermost_mcp.api.api_client_bookmarks import Api as BookmarksApi
from mattermost_mcp.api.api_client_bots import Api as BotsApi
from mattermost_mcp.api.api_client_brand import Api as BrandApi
from mattermost_mcp.api.api_client_channels import Api as ChannelsApi
from mattermost_mcp.api.api_client_cloud import Api as CloudApi
from mattermost_mcp.api.api_client_cluster import Api as ClusterApi
from mattermost_mcp.api.api_client_commands import Api as CommandsApi
from mattermost_mcp.api.api_client_compliance import Api as ComplianceApi
from mattermost_mcp.api.api_client_content_flagging import Api as ContentFlaggingApi
from mattermost_mcp.api.api_client_custom_profile_attributes import (
    Api as CustomProfileAttributesApi,
)
from mattermost_mcp.api.api_client_dataretention import Api as DataretentionApi
from mattermost_mcp.api.api_client_elasticsearch import Api as ElasticsearchApi
from mattermost_mcp.api.api_client_emoji import Api as EmojiApi
from mattermost_mcp.api.api_client_exports import Api as ExportsApi
from mattermost_mcp.api.api_client_files import Api as FilesApi
from mattermost_mcp.api.api_client_groups import Api as GroupsApi
from mattermost_mcp.api.api_client_imports import Api as ImportsApi
from mattermost_mcp.api.api_client_ip_filters import Api as IpFiltersApi
from mattermost_mcp.api.api_client_jobs import Api as JobsApi
from mattermost_mcp.api.api_client_ldap import Api as LdapApi
from mattermost_mcp.api.api_client_limits import Api as LimitsApi
from mattermost_mcp.api.api_client_logs import Api as LogsApi
from mattermost_mcp.api.api_client_metrics import Api as MetricsApi
from mattermost_mcp.api.api_client_oauth import Api as OauthApi
from mattermost_mcp.api.api_client_outgoing_oauth_connections import (
    Api as OutgoingOauthConnectionsApi,
)
from mattermost_mcp.api.api_client_permissions import Api as PermissionsApi
from mattermost_mcp.api.api_client_plugins import Api as PluginsApi
from mattermost_mcp.api.api_client_posts import Api as PostsApi
from mattermost_mcp.api.api_client_preferences import Api as PreferencesApi
from mattermost_mcp.api.api_client_properties import Api as PropertiesApi
from mattermost_mcp.api.api_client_reactions import Api as ReactionsApi
from mattermost_mcp.api.api_client_recaps import Api as RecapsApi
from mattermost_mcp.api.api_client_remoteclusters import Api as RemoteclustersApi
from mattermost_mcp.api.api_client_reports import Api as ReportsApi
from mattermost_mcp.api.api_client_roles import Api as RolesApi
from mattermost_mcp.api.api_client_saml import Api as SamlApi
from mattermost_mcp.api.api_client_scheduled_post import Api as ScheduledPostApi
from mattermost_mcp.api.api_client_schemes import Api as SchemesApi
from mattermost_mcp.api.api_client_service_terms import Api as ServiceTermsApi
from mattermost_mcp.api.api_client_sharedchannels import Api as SharedchannelsApi
from mattermost_mcp.api.api_client_status import Api as StatusApi
from mattermost_mcp.api.api_client_system import Api as SystemApi
from mattermost_mcp.api.api_client_teams import Api as TeamsApi
from mattermost_mcp.api.api_client_uploads import Api as UploadsApi
from mattermost_mcp.api.api_client_usage import Api as UsageApi
from mattermost_mcp.api.api_client_users import Api as UsersApi
from mattermost_mcp.api.api_client_views import Api as ViewsApi
from mattermost_mcp.api.api_client_webhooks import Api as WebhooksApi

__version__ = "0.15.0"


class Api(
    AccessControlApi,
    ActionsApi,
    AgentsApi,
    AuditLoggingApi,
    BoardsApi,
    BookmarksApi,
    BotsApi,
    BrandApi,
    ChannelsApi,
    CloudApi,
    ClusterApi,
    CommandsApi,
    ComplianceApi,
    ContentFlaggingApi,
    CustomProfileAttributesApi,
    DataretentionApi,
    ElasticsearchApi,
    EmojiApi,
    ExportsApi,
    FilesApi,
    GroupsApi,
    ImportsApi,
    IpFiltersApi,
    JobsApi,
    LdapApi,
    LimitsApi,
    LogsApi,
    MetricsApi,
    OauthApi,
    OutgoingOauthConnectionsApi,
    PermissionsApi,
    PluginsApi,
    PostsApi,
    PreferencesApi,
    PropertiesApi,
    ReactionsApi,
    RecapsApi,
    RemoteclustersApi,
    ReportsApi,
    RolesApi,
    SamlApi,
    ScheduledPostApi,
    SchemesApi,
    ServiceTermsApi,
    SharedchannelsApi,
    StatusApi,
    SystemApi,
    TeamsApi,
    UploadsApi,
    UsageApi,
    UsersApi,
    ViewsApi,
    WebhooksApi,
):
    pass
