"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_plugins(self, **kwargs) -> Any:
        """Get plugins

        Path: /api/v4/plugins
        Method: GET
        """
        url = "/api/v4/plugins"
        return self.request("GET", url, params=kwargs)

    def upload_plugin(self, **kwargs) -> Any:
        """Upload plugin

        Path: /api/v4/plugins
        Method: POST
        """
        url = "/api/v4/plugins"
        return self.request("POST", url, data=kwargs)

    def install_plugin_from_url(self, **kwargs) -> Any:
        """Install plugin from url

        Path: /api/v4/plugins/install_from_url
        Method: POST
        """
        url = "/api/v4/plugins/install_from_url"
        return self.request("POST", url, data=kwargs)

    def remove_plugin(self, plugin_id: str, **kwargs) -> Any:
        """Remove plugin

        Path: /api/v4/plugins/{plugin_id}
        Method: DELETE
        """
        url = f"/api/v4/plugins/{plugin_id}"
        return self.request("DELETE", url, params=kwargs)

    def enable_plugin(self, plugin_id: str, **kwargs) -> Any:
        """Enable plugin

        Path: /api/v4/plugins/{plugin_id}/enable
        Method: POST
        """
        url = f"/api/v4/plugins/{plugin_id}/enable"
        return self.request("POST", url, data=kwargs)

    def disable_plugin(self, plugin_id: str, **kwargs) -> Any:
        """Disable plugin

        Path: /api/v4/plugins/{plugin_id}/disable
        Method: POST
        """
        url = f"/api/v4/plugins/{plugin_id}/disable"
        return self.request("POST", url, data=kwargs)

    def get_webapp_plugins(self, **kwargs) -> Any:
        """Get webapp plugins

        Path: /api/v4/plugins/webapp
        Method: GET
        """
        url = "/api/v4/plugins/webapp"
        return self.request("GET", url, params=kwargs)

    def get_plugin_statuses(self, **kwargs) -> Any:
        """Get plugins status

        Path: /api/v4/plugins/statuses
        Method: GET
        """
        url = "/api/v4/plugins/statuses"
        return self.request("GET", url, params=kwargs)

    def get_marketplace_plugins(self, **kwargs) -> Any:
        """Gets all the marketplace plugins

        Path: /api/v4/plugins/marketplace
        Method: GET
        """
        url = "/api/v4/plugins/marketplace"
        return self.request("GET", url, params=kwargs)

    def install_marketplace_plugin(self, **kwargs) -> Any:
        """Installs a marketplace plugin

        Path: /api/v4/plugins/marketplace
        Method: POST
        """
        url = "/api/v4/plugins/marketplace"
        return self.request("POST", url, data=kwargs)

    def get_marketplace_visited_by_admin(self, **kwargs) -> Any:
        """Get if the Plugin Marketplace has been visited by at least an admin.

        Path: /api/v4/plugins/marketplace/first_admin_visit
        Method: GET
        """
        url = "/api/v4/plugins/marketplace/first_admin_visit"
        return self.request("GET", url, params=kwargs)

    def update_marketplace_visited_by_admin(self, **kwargs) -> Any:
        """Stores that the Plugin Marketplace has been visited by at least an admin.

        Path: /api/v4/plugins/marketplace/first_admin_visit
        Method: POST
        """
        url = "/api/v4/plugins/marketplace/first_admin_visit"
        return self.request("POST", url, data=kwargs)

    def reattach_plugin(self, **kwargs) -> Any:
        """Reattach a plugin process

        Path: /api/v4/plugins/reattach
        Method: POST
        """
        url = "/api/v4/plugins/reattach"
        return self.request("POST", url, data=kwargs)

    def detach_plugin(self, plugin_id: str, **kwargs) -> Any:
        """Detach a reattached plugin process

        Path: /api/v4/plugins/{plugin_id}/detach
        Method: POST
        """
        url = f"/api/v4/plugins/{plugin_id}/detach"
        return self.request("POST", url, data=kwargs)
