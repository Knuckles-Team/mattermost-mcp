"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def create_upload(self, **kwargs) -> Any:
        """Create an upload

        Path: /api/v4/uploads
        Method: POST
        """
        url = "/api/v4/uploads"
        return self.request("POST", url, data=kwargs)

    def get_upload(self, upload_id: str, **kwargs) -> Any:
        """Get an upload session

        Path: /api/v4/uploads/{upload_id}
        Method: GET
        """
        url = f"/api/v4/uploads/{upload_id}"
        return self.request("GET", url, params=kwargs)

    def upload_data(self, upload_id: str, **kwargs) -> Any:
        """Perform a file upload

        Path: /api/v4/uploads/{upload_id}
        Method: POST
        """
        url = f"/api/v4/uploads/{upload_id}"
        return self.request("POST", url, data=kwargs)
