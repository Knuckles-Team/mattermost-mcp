#!/usr/bin/env python
from mattermost_mcp.api.api_client_base import ApiClientBase
from mattermost_mcp.api.api_client_teams import Api as TeamsApi
from mattermost_mcp.api.api_client_channels import Api as ChannelsApi
from mattermost_mcp.api.api_client_posts import Api as PostsApi
from mattermost_mcp.api.api_client_users import Api as UsersApi

__version__ = "0.15.0"

class Api(TeamsApi, ChannelsApi, PostsApi, UsersApi):
    pass
