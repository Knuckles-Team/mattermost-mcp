"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def download_system_logs(self, **kwargs) -> Any:
        """Download system logs
        
        Path: /api/v4/logs/download
        Method: GET
        """
        url = "/api/v4/logs/download"
        return self.request("GET", url, params=kwargs)
