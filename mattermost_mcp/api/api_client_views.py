"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def list_channel_views(self, channel_id: str, **kwargs) -> Any:
        """List channel views
        
        Path: /api/v4/channels/{channel_id}/views
        Method: GET
        """
        url = "/api/v4/channels/{channel_id}/views".format(channel_id=channel_id)
        return self.request("GET", url, params=kwargs)

    def create_channel_view(self, channel_id: str, **kwargs) -> Any:
        """Create channel view
        
        Path: /api/v4/channels/{channel_id}/views
        Method: POST
        """
        url = "/api/v4/channels/{channel_id}/views".format(channel_id=channel_id)
        return self.request("POST", url, data=kwargs)

    def get_channel_view(self, channel_id: str, view_id: str, **kwargs) -> Any:
        """Get a channel view
        
        Path: /api/v4/channels/{channel_id}/views/{view_id}
        Method: GET
        """
        url = "/api/v4/channels/{channel_id}/views/{view_id}".format(channel_id=channel_id, view_id=view_id)
        return self.request("GET", url, params=kwargs)

    def delete_channel_view(self, channel_id: str, view_id: str, **kwargs) -> Any:
        """Delete a channel view
        
        Path: /api/v4/channels/{channel_id}/views/{view_id}
        Method: DELETE
        """
        url = "/api/v4/channels/{channel_id}/views/{view_id}".format(channel_id=channel_id, view_id=view_id)
        return self.request("DELETE", url, params=kwargs)

    def update_channel_view(self, channel_id: str, view_id: str, **kwargs) -> Any:
        """Update a channel view
        
        Path: /api/v4/channels/{channel_id}/views/{view_id}
        Method: PATCH
        """
        url = "/api/v4/channels/{channel_id}/views/{view_id}".format(channel_id=channel_id, view_id=view_id)
        return self.request("PATCH", url, data=kwargs)

    def get_posts_for_view(self, channel_id: str, view_id: str, **kwargs) -> Any:
        """Get posts for a view
        
        Path: /api/v4/channels/{channel_id}/views/{view_id}/posts
        Method: GET
        """
        url = "/api/v4/channels/{channel_id}/views/{view_id}/posts".format(channel_id=channel_id, view_id=view_id)
        return self.request("GET", url, params=kwargs)

    def update_channel_view_sort_order(self, channel_id: str, view_id: str, **kwargs) -> Any:
        """Update a channel view's sort order
        
        Path: /api/v4/channels/{channel_id}/views/{view_id}/sort_order
        Method: POST
        """
        url = "/api/v4/channels/{channel_id}/views/{view_id}/sort_order".format(channel_id=channel_id, view_id=view_id)
        return self.request("POST", url, data=kwargs)
