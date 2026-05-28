"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def create_scheduled_post(self, **kwargs) -> Any:
        """Creates a scheduled post

        Path: /api/v4/posts/schedule
        Method: POST
        """
        url = "/api/v4/posts/schedule"
        return self.request("POST", url, data=kwargs)

    def get_user_scheduled_posts(self, team_id: str, **kwargs) -> Any:
        """Gets all scheduled posts for a user for the specified team..

        Path: /api/v4/posts/scheduled/team/{team_id}
        Method: GET
        """
        url = f"/api/v4/posts/scheduled/team/{team_id}"
        return self.request("GET", url, params=kwargs)

    def update_scheduled_post(self, scheduled_post_id: str, **kwargs) -> Any:
        """Update a scheduled post

        Path: /api/v4/posts/schedule/{scheduled_post_id}
        Method: PUT
        """
        url = f"/api/v4/posts/schedule/{scheduled_post_id}"
        return self.request("PUT", url, data=kwargs)

    def delete_scheduled_post(self, scheduled_post_id: str, **kwargs) -> Any:
        """Delete a scheduled post

        Path: /api/v4/posts/schedule/{scheduled_post_id}
        Method: DELETE
        """
        url = f"/api/v4/posts/schedule/{scheduled_post_id}"
        return self.request("DELETE", url, params=kwargs)
