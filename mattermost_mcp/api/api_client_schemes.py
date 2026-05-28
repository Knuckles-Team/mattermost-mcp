"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_schemes(self, **kwargs) -> Any:
        """Get the schemes.

        Path: /api/v4/schemes
        Method: GET
        """
        url = "/api/v4/schemes"
        return self.request("GET", url, params=kwargs)

    def create_scheme(self, **kwargs) -> Any:
        """Create a scheme

        Path: /api/v4/schemes
        Method: POST
        """
        url = "/api/v4/schemes"
        return self.request("POST", url, data=kwargs)

    def get_scheme(self, scheme_id: str, **kwargs) -> Any:
        """Get a scheme

        Path: /api/v4/schemes/{scheme_id}
        Method: GET
        """
        url = f"/api/v4/schemes/{scheme_id}"
        return self.request("GET", url, params=kwargs)

    def delete_scheme(self, scheme_id: str, **kwargs) -> Any:
        """Delete a scheme

        Path: /api/v4/schemes/{scheme_id}
        Method: DELETE
        """
        url = f"/api/v4/schemes/{scheme_id}"
        return self.request("DELETE", url, params=kwargs)

    def patch_scheme(self, scheme_id: str, **kwargs) -> Any:
        """Patch a scheme

        Path: /api/v4/schemes/{scheme_id}/patch
        Method: PUT
        """
        url = f"/api/v4/schemes/{scheme_id}/patch"
        return self.request("PUT", url, data=kwargs)

    def get_teams_for_scheme(self, scheme_id: str, **kwargs) -> Any:
        """Get a page of teams which use this scheme.

        Path: /api/v4/schemes/{scheme_id}/teams
        Method: GET
        """
        url = f"/api/v4/schemes/{scheme_id}/teams"
        return self.request("GET", url, params=kwargs)

    def get_channels_for_scheme(self, scheme_id: str, **kwargs) -> Any:
        """Get a page of channels which use this scheme.

        Path: /api/v4/schemes/{scheme_id}/channels
        Method: GET
        """
        url = f"/api/v4/schemes/{scheme_id}/channels"
        return self.request("GET", url, params=kwargs)
