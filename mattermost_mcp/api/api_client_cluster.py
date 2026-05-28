"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_cluster_status(self, **kwargs) -> Any:
        """Get cluster status

        Path: /api/v4/cluster/status
        Method: GET
        """
        url = "/api/v4/cluster/status"
        return self.request("GET", url, params=kwargs)
