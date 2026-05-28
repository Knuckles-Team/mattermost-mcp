"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_recaps_for_user(self, **kwargs) -> Any:
        """Get current user's recaps

        Path: /api/v4/recaps
        Method: GET
        """
        url = "/api/v4/recaps"
        return self.request("GET", url, params=kwargs)

    def create_recap(self, **kwargs) -> Any:
        """Create a channel recap

        Path: /api/v4/recaps
        Method: POST
        """
        url = "/api/v4/recaps"
        return self.request("POST", url, data=kwargs)

    def mark_recaps_as_viewed(self, **kwargs) -> Any:
        """Mark all of the authenticated user's finished recaps as viewed

        Path: /api/v4/recaps/mark_viewed
        Method: POST
        """
        url = "/api/v4/recaps/mark_viewed"
        return self.request("POST", url, data=kwargs)

    def get_recap(self, recap_id: str, **kwargs) -> Any:
        """Get a specific recap

        Path: /api/v4/recaps/{recap_id}
        Method: GET
        """
        url = f"/api/v4/recaps/{recap_id}"
        return self.request("GET", url, params=kwargs)

    def delete_recap(self, recap_id: str, **kwargs) -> Any:
        """Delete a recap

        Path: /api/v4/recaps/{recap_id}
        Method: DELETE
        """
        url = f"/api/v4/recaps/{recap_id}"
        return self.request("DELETE", url, params=kwargs)

    def mark_recap_as_read(self, recap_id: str, **kwargs) -> Any:
        """Mark a recap as read

        Path: /api/v4/recaps/{recap_id}/read
        Method: POST
        """
        url = f"/api/v4/recaps/{recap_id}/read"
        return self.request("POST", url, data=kwargs)

    def regenerate_recap(self, recap_id: str, **kwargs) -> Any:
        """Regenerate a recap

        Path: /api/v4/recaps/{recap_id}/regenerate
        Method: POST
        """
        url = f"/api/v4/recaps/{recap_id}/regenerate"
        return self.request("POST", url, data=kwargs)
