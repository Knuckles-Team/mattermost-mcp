"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_bots(self, **kwargs) -> Any:
        """Get bots

        Path: /api/v4/bots
        Method: GET
        """
        url = "/api/v4/bots"
        return self.request("GET", url, params=kwargs)

    def create_bot(self, **kwargs) -> Any:
        """Create a bot

        Path: /api/v4/bots
        Method: POST
        """
        url = "/api/v4/bots"
        return self.request("POST", url, data=kwargs)

    def get_bot(self, bot_user_id: str, **kwargs) -> Any:
        """Get a bot

        Path: /api/v4/bots/{bot_user_id}
        Method: GET
        """
        url = f"/api/v4/bots/{bot_user_id}"
        return self.request("GET", url, params=kwargs)

    def patch_bot(self, bot_user_id: str, **kwargs) -> Any:
        """Patch a bot

        Path: /api/v4/bots/{bot_user_id}
        Method: PUT
        """
        url = f"/api/v4/bots/{bot_user_id}"
        return self.request("PUT", url, data=kwargs)

    def disable_bot(self, bot_user_id: str, **kwargs) -> Any:
        """Disable a bot

        Path: /api/v4/bots/{bot_user_id}/disable
        Method: POST
        """
        url = f"/api/v4/bots/{bot_user_id}/disable"
        return self.request("POST", url, data=kwargs)

    def enable_bot(self, bot_user_id: str, **kwargs) -> Any:
        """Enable a bot

        Path: /api/v4/bots/{bot_user_id}/enable
        Method: POST
        """
        url = f"/api/v4/bots/{bot_user_id}/enable"
        return self.request("POST", url, data=kwargs)

    def assign_bot(self, bot_user_id: str, user_id: str, **kwargs) -> Any:
        """Assign a bot to a user

        Path: /api/v4/bots/{bot_user_id}/assign/{user_id}
        Method: POST
        """
        url = f"/api/v4/bots/{bot_user_id}/assign/{user_id}"
        return self.request("POST", url, data=kwargs)

    def convert_bot_to_user(self, bot_user_id: str, **kwargs) -> Any:
        """Convert a bot into a user

        Path: /api/v4/bots/{bot_user_id}/convert_to_user
        Method: POST
        """
        url = f"/api/v4/bots/{bot_user_id}/convert_to_user"
        return self.request("POST", url, data=kwargs)
