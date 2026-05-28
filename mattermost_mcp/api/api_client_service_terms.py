"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_terms_of_service(self, **kwargs) -> Any:
        """Get latest terms of service

        Path: /api/v4/terms_of_service
        Method: GET
        """
        url = "/api/v4/terms_of_service"
        return self.request("GET", url, params=kwargs)

    def create_terms_of_service(self, **kwargs) -> Any:
        """Creates a new terms of service

        Path: /api/v4/terms_of_service
        Method: POST
        """
        url = "/api/v4/terms_of_service"
        return self.request("POST", url, data=kwargs)
