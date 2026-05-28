"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def list_imports(self, **kwargs) -> Any:
        """List import files

        Path: /api/v4/imports
        Method: GET
        """
        url = "/api/v4/imports"
        return self.request("GET", url, params=kwargs)

    def delete_import(self, import_name: str, **kwargs) -> Any:
        """Delete an import file

        Path: /api/v4/imports/{import_name}
        Method: DELETE
        """
        url = f"/api/v4/imports/{import_name}"
        return self.request("DELETE", url, params=kwargs)
