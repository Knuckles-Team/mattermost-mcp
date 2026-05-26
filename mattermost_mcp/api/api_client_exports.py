"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def list_exports(self, **kwargs) -> Any:
        """List export files
        
        Path: /api/v4/exports
        Method: GET
        """
        url = "/api/v4/exports"
        return self.request("GET", url, params=kwargs)

    def download_export(self, export_name: str, **kwargs) -> Any:
        """Download an export file
        
        Path: /api/v4/exports/{export_name}
        Method: GET
        """
        url = "/api/v4/exports/{export_name}".format(export_name=export_name)
        return self.request("GET", url, params=kwargs)

    def delete_export(self, export_name: str, **kwargs) -> Any:
        """Delete an export file
        
        Path: /api/v4/exports/{export_name}
        Method: DELETE
        """
        url = "/api/v4/exports/{export_name}".format(export_name=export_name)
        return self.request("DELETE", url, params=kwargs)

    def presign_export(self, export_name: str, **kwargs) -> Any:
        """Create a presigned URL for export download
        
        Path: /api/v4/exports/{export_name}/presign-url
        Method: POST
        """
        url = "/api/v4/exports/{export_name}/presign-url".format(export_name=export_name)
        return self.request("POST", url, data=kwargs)
