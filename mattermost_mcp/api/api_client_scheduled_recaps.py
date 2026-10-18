"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_scheduled_recaps(self, **kwargs) -> Any:
        """Get current user's scheduled recaps

        Path: /api/v4/scheduled_recaps
        Method: GET
        """
        url = "/api/v4/scheduled_recaps"
        return self.request("GET", url, params=kwargs)

    def create_scheduled_recap(self, **kwargs) -> Any:
        """Create a scheduled recap

        Path: /api/v4/scheduled_recaps
        Method: POST
        """
        url = "/api/v4/scheduled_recaps"
        return self.request("POST", url, data=kwargs)

    def get_scheduled_recap(self, scheduled_recap_id: str, **kwargs) -> Any:
        """Get a scheduled recap

        Path: /api/v4/scheduled_recaps/{scheduled_recap_id}
        Method: GET
        """
        url = f"/api/v4/scheduled_recaps/{scheduled_recap_id}"
        return self.request("GET", url, params=kwargs)

    def update_scheduled_recap(self, scheduled_recap_id: str, **kwargs) -> Any:
        """Update a scheduled recap

        Path: /api/v4/scheduled_recaps/{scheduled_recap_id}
        Method: PUT
        """
        url = f"/api/v4/scheduled_recaps/{scheduled_recap_id}"
        return self.request("PUT", url, data=kwargs)

    def delete_scheduled_recap(self, scheduled_recap_id: str, **kwargs) -> Any:
        """Delete a scheduled recap

        Path: /api/v4/scheduled_recaps/{scheduled_recap_id}
        Method: DELETE
        """
        url = f"/api/v4/scheduled_recaps/{scheduled_recap_id}"
        return self.request("DELETE", url, params=kwargs)

    def pause_scheduled_recap(self, scheduled_recap_id: str, **kwargs) -> Any:
        """Pause a scheduled recap

        Path: /api/v4/scheduled_recaps/{scheduled_recap_id}/pause
        Method: POST
        """
        url = f"/api/v4/scheduled_recaps/{scheduled_recap_id}/pause"
        return self.request("POST", url, data=kwargs)

    def resume_scheduled_recap(self, scheduled_recap_id: str, **kwargs) -> Any:
        """Resume a scheduled recap

        Path: /api/v4/scheduled_recaps/{scheduled_recap_id}/resume
        Method: POST
        """
        url = f"/api/v4/scheduled_recaps/{scheduled_recap_id}/resume"
        return self.request("POST", url, data=kwargs)
