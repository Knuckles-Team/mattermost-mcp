"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_brand_image(self, **kwargs) -> Any:
        """Get brand image
        
        Path: /api/v4/brand/image
        Method: GET
        """
        url = "/api/v4/brand/image"
        return self.request("GET", url, params=kwargs)

    def upload_brand_image(self, **kwargs) -> Any:
        """Upload brand image
        
        Path: /api/v4/brand/image
        Method: POST
        """
        url = "/api/v4/brand/image"
        return self.request("POST", url, data=kwargs)

    def delete_brand_image(self, **kwargs) -> Any:
        """Delete current brand image
        
        Path: /api/v4/brand/image
        Method: DELETE
        """
        url = "/api/v4/brand/image"
        return self.request("DELETE", url, params=kwargs)
