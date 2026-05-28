"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_ancillary_permissions_post(self, **kwargs) -> Any:
        """Return all system console subsection ancillary permissions

        Path: /api/v4/permissions/ancillary
        Method: POST
        """
        url = "/api/v4/permissions/ancillary"
        return self.request("POST", url, data=kwargs)
