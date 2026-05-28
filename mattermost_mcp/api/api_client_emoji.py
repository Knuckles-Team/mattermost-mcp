"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_emoji_list(self, **kwargs) -> Any:
        """Get a list of custom emoji

        Path: /api/v4/emoji
        Method: GET
        """
        url = "/api/v4/emoji"
        return self.request("GET", url, params=kwargs)

    def create_emoji(self, **kwargs) -> Any:
        """Create a custom emoji

        Path: /api/v4/emoji
        Method: POST
        """
        url = "/api/v4/emoji"
        return self.request("POST", url, data=kwargs)

    def get_emoji(self, emoji_id: str, **kwargs) -> Any:
        """Get a custom emoji

        Path: /api/v4/emoji/{emoji_id}
        Method: GET
        """
        url = f"/api/v4/emoji/{emoji_id}"
        return self.request("GET", url, params=kwargs)

    def delete_emoji(self, emoji_id: str, **kwargs) -> Any:
        """Delete a custom emoji

        Path: /api/v4/emoji/{emoji_id}
        Method: DELETE
        """
        url = f"/api/v4/emoji/{emoji_id}"
        return self.request("DELETE", url, params=kwargs)

    def get_emoji_by_name(self, emoji_name: str, **kwargs) -> Any:
        """Get a custom emoji by name

        Path: /api/v4/emoji/name/{emoji_name}
        Method: GET
        """
        url = f"/api/v4/emoji/name/{emoji_name}"
        return self.request("GET", url, params=kwargs)

    def get_emoji_image(self, emoji_id: str, **kwargs) -> Any:
        """Get custom emoji image

        Path: /api/v4/emoji/{emoji_id}/image
        Method: GET
        """
        url = f"/api/v4/emoji/{emoji_id}/image"
        return self.request("GET", url, params=kwargs)

    def search_emoji(self, **kwargs) -> Any:
        """Search custom emoji

        Path: /api/v4/emoji/search
        Method: POST
        """
        url = "/api/v4/emoji/search"
        return self.request("POST", url, data=kwargs)

    def autocomplete_emoji(self, **kwargs) -> Any:
        """Autocomplete custom emoji

        Path: /api/v4/emoji/autocomplete
        Method: GET
        """
        url = "/api/v4/emoji/autocomplete"
        return self.request("GET", url, params=kwargs)

    def get_emojis_by_names(self, **kwargs) -> Any:
        """Get custom emojis by name

        Path: /api/v4/emoji/names
        Method: POST
        """
        url = "/api/v4/emoji/names"
        return self.request("POST", url, data=kwargs)
