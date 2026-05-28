"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_all_roles(self, **kwargs) -> Any:
        """Get a list of all the roles

        Path: /api/v4/roles
        Method: GET
        """
        url = "/api/v4/roles"
        return self.request("GET", url, params=kwargs)

    def get_role(self, role_id: str, **kwargs) -> Any:
        """Get a role

        Path: /api/v4/roles/{role_id}
        Method: GET
        """
        url = f"/api/v4/roles/{role_id}"
        return self.request("GET", url, params=kwargs)

    def get_role_by_name(self, role_name: str, **kwargs) -> Any:
        """Get a role

        Path: /api/v4/roles/name/{role_name}
        Method: GET
        """
        url = f"/api/v4/roles/name/{role_name}"
        return self.request("GET", url, params=kwargs)

    def patch_role(self, role_id: str, **kwargs) -> Any:
        """Patch a role

        Path: /api/v4/roles/{role_id}/patch
        Method: PUT
        """
        url = f"/api/v4/roles/{role_id}/patch"
        return self.request("PUT", url, data=kwargs)

    def get_roles_by_names(self, **kwargs) -> Any:
        """Get a list of roles by name

        Path: /api/v4/roles/names
        Method: POST
        """
        url = "/api/v4/roles/names"
        return self.request("POST", url, data=kwargs)
