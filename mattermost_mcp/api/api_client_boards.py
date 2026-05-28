"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def create_board(self, **kwargs) -> Any:
        """Create a board channel

        Path: /api/v4/boards
        Method: POST
        """
        url = "/api/v4/boards"
        return self.request("POST", url, data=kwargs)
