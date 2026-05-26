"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_server_limits(self, **kwargs) -> Any:
        """Gets the server limits for the server
        
        Path: /api/v4/limits/server
        Method: GET
        """
        url = "/api/v4/limits/server"
        return self.request("GET", url, params=kwargs)
