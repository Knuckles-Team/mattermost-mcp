"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def list_channel_bookmarks_for_channel(self, channel_id: str, **kwargs) -> Any:
        """Get channel bookmarks for Channel

        Path: /api/v4/channels/{channel_id}/bookmarks
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/bookmarks"
        return self.request("GET", url, params=kwargs)

    def create_channel_bookmark(self, channel_id: str, **kwargs) -> Any:
        """Create channel bookmark

        Path: /api/v4/channels/{channel_id}/bookmarks
        Method: POST
        """
        url = f"/api/v4/channels/{channel_id}/bookmarks"
        return self.request("POST", url, data=kwargs)

    def delete_channel_bookmark(
        self, channel_id: str, bookmark_id: str, **kwargs
    ) -> Any:
        """Delete channel bookmark

        Path: /api/v4/channels/{channel_id}/bookmarks/{bookmark_id}
        Method: DELETE
        """
        url = f"/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}"
        return self.request("DELETE", url, params=kwargs)

    def update_channel_bookmark(
        self, channel_id: str, bookmark_id: str, **kwargs
    ) -> Any:
        """Update channel bookmark

        Path: /api/v4/channels/{channel_id}/bookmarks/{bookmark_id}
        Method: PATCH
        """
        url = f"/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}"
        return self.request("PATCH", url, data=kwargs)

    def update_channel_bookmark_sort_order(
        self, channel_id: str, bookmark_id: str, **kwargs
    ) -> Any:
        """Update channel bookmark's order

        Path: /api/v4/channels/{channel_id}/bookmarks/{bookmark_id}/sort_order
        Method: POST
        """
        url = f"/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}/sort_order"
        return self.request("POST", url, data=kwargs)
