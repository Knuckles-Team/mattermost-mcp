"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_o_auth_apps(self, **kwargs) -> Any:
        """Get OAuth apps

        Path: /api/v4/oauth/apps
        Method: GET
        """
        url = "/api/v4/oauth/apps"
        return self.request("GET", url, params=kwargs)

    def create_o_auth_app(self, **kwargs) -> Any:
        """Register OAuth app

        Path: /api/v4/oauth/apps
        Method: POST
        """
        url = "/api/v4/oauth/apps"
        return self.request("POST", url, data=kwargs)

    def get_o_auth_app(self, app_id: str, **kwargs) -> Any:
        """Get an OAuth app

        Path: /api/v4/oauth/apps/{app_id}
        Method: GET
        """
        url = f"/api/v4/oauth/apps/{app_id}"
        return self.request("GET", url, params=kwargs)

    def update_o_auth_app(self, app_id: str, **kwargs) -> Any:
        """Update an OAuth app

        Path: /api/v4/oauth/apps/{app_id}
        Method: PUT
        """
        url = f"/api/v4/oauth/apps/{app_id}"
        return self.request("PUT", url, data=kwargs)

    def delete_o_auth_app(self, app_id: str, **kwargs) -> Any:
        """Delete an OAuth app

        Path: /api/v4/oauth/apps/{app_id}
        Method: DELETE
        """
        url = f"/api/v4/oauth/apps/{app_id}"
        return self.request("DELETE", url, params=kwargs)

    def regenerate_o_auth_app_secret(self, app_id: str, **kwargs) -> Any:
        """Regenerate OAuth app secret

        Path: /api/v4/oauth/apps/{app_id}/regen_secret
        Method: POST
        """
        url = f"/api/v4/oauth/apps/{app_id}/regen_secret"
        return self.request("POST", url, data=kwargs)

    def get_o_auth_app_info(self, app_id: str, **kwargs) -> Any:
        """Get info on an OAuth app

        Path: /api/v4/oauth/apps/{app_id}/info
        Method: GET
        """
        url = f"/api/v4/oauth/apps/{app_id}/info"
        return self.request("GET", url, params=kwargs)

    def get_authorization_server_metadata(self, **kwargs) -> Any:
        """Get OAuth 2.0 Authorization Server Metadata

        Path: /.well-known/oauth-authorization-server
        Method: GET
        """
        url = "/.well-known/oauth-authorization-server"
        return self.request("GET", url, params=kwargs)

    def register_o_auth_client(self, **kwargs) -> Any:
        """Register OAuth client using Dynamic Client Registration

        Path: /api/v4/oauth/apps/register
        Method: POST
        """
        url = "/api/v4/oauth/apps/register"
        return self.request("POST", url, data=kwargs)

    def get_authorized_o_auth_apps_for_user(self, user_id: str, **kwargs) -> Any:
        """Get authorized OAuth apps

        Path: /api/v4/users/{user_id}/oauth/apps/authorized
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/oauth/apps/authorized"
        return self.request("GET", url, params=kwargs)
