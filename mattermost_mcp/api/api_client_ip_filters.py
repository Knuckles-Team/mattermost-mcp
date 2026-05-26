"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_i_p_filters(self, **kwargs) -> Any:
        """Get all IP filters
        
        Path: /api/v4/ip_filtering
        Method: GET
        """
        url = "/api/v4/ip_filtering"
        return self.request("GET", url, params=kwargs)

    def apply_i_p_filters(self, **kwargs) -> Any:
        """Get all IP filters
        
        Path: /api/v4/ip_filtering
        Method: POST
        """
        url = "/api/v4/ip_filtering"
        return self.request("POST", url, data=kwargs)

    def my_i_p(self, **kwargs) -> Any:
        """Get all IP filters
        
        Path: /api/v4/ip_filtering/my_ip
        Method: GET
        """
        url = "/api/v4/ip_filtering/my_ip"
        return self.request("GET", url, params=kwargs)
