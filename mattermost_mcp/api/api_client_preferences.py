"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_preferences(self, user_id: str, **kwargs) -> Any:
        """Get the user's preferences

        Path: /api/v4/users/{user_id}/preferences
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/preferences"
        return self.request("GET", url, params=kwargs)

    def update_preferences(self, user_id: str, **kwargs) -> Any:
        """Save the user's preferences

        Path: /api/v4/users/{user_id}/preferences
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/preferences"
        return self.request("PUT", url, data=kwargs)

    def delete_preferences(self, user_id: str, **kwargs) -> Any:
        """Delete user's preferences

        Path: /api/v4/users/{user_id}/preferences/delete
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/preferences/delete"
        return self.request("POST", url, data=kwargs)

    def get_preferences_by_category(self, user_id: str, category: str, **kwargs) -> Any:
        """List a user's preferences by category

        Path: /api/v4/users/{user_id}/preferences/{category}
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/preferences/{category}"
        return self.request("GET", url, params=kwargs)

    def get_preferences_by_category_by_name(
        self, user_id: str, category: str, preference_name: str, **kwargs
    ) -> Any:
        """Get a specific user preference

        Path: /api/v4/users/{user_id}/preferences/{category}/name/{preference_name}
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/preferences/{category}/name/{preference_name}"
        return self.request("GET", url, params=kwargs)
