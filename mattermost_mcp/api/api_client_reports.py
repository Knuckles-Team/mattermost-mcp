"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_users_for_reporting(self, **kwargs) -> Any:
        """Get a list of paged and sorted users for admin reporting purposes

        Path: /api/v4/reports/users
        Method: GET
        """
        url = "/api/v4/reports/users"
        return self.request("GET", url, params=kwargs)

    def get_user_count_for_reporting(self, **kwargs) -> Any:
        """Gets the full count of users that match the filter.

        Path: /api/v4/reports/users/count
        Method: GET
        """
        url = "/api/v4/reports/users/count"
        return self.request("GET", url, params=kwargs)

    def start_batch_users_export(self, **kwargs) -> Any:
        """Starts a job to export the users to a report file.

        Path: /api/v4/reports/users/export
        Method: POST
        """
        url = "/api/v4/reports/users/export"
        return self.request("POST", url, data=kwargs)

    def get_posts_for_reporting(self, **kwargs) -> Any:
        """Get posts for reporting and compliance purposes using cursor-based pagination

        Path: /api/v4/reports/posts
        Method: POST
        """
        url = "/api/v4/reports/posts"
        return self.request("POST", url, data=kwargs)
