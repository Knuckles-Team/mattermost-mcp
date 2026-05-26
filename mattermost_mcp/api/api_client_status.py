"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_user_status(self, user_id: str, **kwargs) -> Any:
        """Get user status
        
        Path: /api/v4/users/{user_id}/status
        Method: GET
        """
        url = "/api/v4/users/{user_id}/status".format(user_id=user_id)
        return self.request("GET", url, params=kwargs)

    def update_user_status(self, user_id: str, **kwargs) -> Any:
        """Update user status
        
        Path: /api/v4/users/{user_id}/status
        Method: PUT
        """
        url = "/api/v4/users/{user_id}/status".format(user_id=user_id)
        return self.request("PUT", url, data=kwargs)

    def get_users_statuses_by_ids(self, **kwargs) -> Any:
        """Get user statuses by id
        
        Path: /api/v4/users/status/ids
        Method: POST
        """
        url = "/api/v4/users/status/ids"
        return self.request("POST", url, data=kwargs)

    def update_user_custom_status(self, user_id: str, **kwargs) -> Any:
        """Update user custom status
        
        Path: /api/v4/users/{user_id}/status/custom
        Method: PUT
        """
        url = "/api/v4/users/{user_id}/status/custom".format(user_id=user_id)
        return self.request("PUT", url, data=kwargs)

    def unset_user_custom_status(self, user_id: str, **kwargs) -> Any:
        """Unsets user custom status
        
        Path: /api/v4/users/{user_id}/status/custom
        Method: DELETE
        """
        url = "/api/v4/users/{user_id}/status/custom".format(user_id=user_id)
        return self.request("DELETE", url, params=kwargs)

    def remove_recent_custom_status(self, user_id: str, **kwargs) -> Any:
        """Delete user's recent custom status
        
        Path: /api/v4/users/{user_id}/status/custom/recent
        Method: DELETE
        """
        url = "/api/v4/users/{user_id}/status/custom/recent".format(user_id=user_id)
        return self.request("DELETE", url, params=kwargs)

    def post_user_recent_custom_status_delete(self, user_id: str, **kwargs) -> Any:
        """Delete user's recent custom status
        
        Path: /api/v4/users/{user_id}/status/custom/recent/delete
        Method: POST
        """
        url = "/api/v4/users/{user_id}/status/custom/recent/delete".format(user_id=user_id)
        return self.request("POST", url, data=kwargs)
