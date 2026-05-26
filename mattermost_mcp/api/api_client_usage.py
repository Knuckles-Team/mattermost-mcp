"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_posts_usage(self, **kwargs) -> Any:
        """Get current usage of posts
        
        Path: /api/v4/usage/posts
        Method: GET
        """
        url = "/api/v4/usage/posts"
        return self.request("GET", url, params=kwargs)

    def get_storage_usage(self, **kwargs) -> Any:
        """Get the total file storage usage for the instance in bytes.
        
        Path: /api/v4/usage/storage
        Method: GET
        """
        url = "/api/v4/usage/storage"
        return self.request("GET", url, params=kwargs)

    def get_teams_usage(self, **kwargs) -> Any:
        """Get current usage of teams
        
        Path: /api/v4/usage/teams
        Method: GET
        """
        url = "/api/v4/usage/teams"
        return self.request("GET", url, params=kwargs)
