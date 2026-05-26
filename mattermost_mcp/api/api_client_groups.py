"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_groups(self, **kwargs) -> Any:
        """Get groups
        
        Path: /api/v4/groups
        Method: GET
        """
        url = "/api/v4/groups"
        return self.request("GET", url, params=kwargs)

    def create_group(self, **kwargs) -> Any:
        """Create a custom group
        
        Path: /api/v4/groups
        Method: POST
        """
        url = "/api/v4/groups"
        return self.request("POST", url, data=kwargs)

    def get_group(self, group_id: str, **kwargs) -> Any:
        """Get a group
        
        Path: /api/v4/groups/{group_id}
        Method: GET
        """
        url = "/api/v4/groups/{group_id}".format(group_id=group_id)
        return self.request("GET", url, params=kwargs)

    def delete_group(self, group_id: str, **kwargs) -> Any:
        """Deletes a custom group
        
        Path: /api/v4/groups/{group_id}
        Method: DELETE
        """
        url = "/api/v4/groups/{group_id}".format(group_id=group_id)
        return self.request("DELETE", url, params=kwargs)

    def patch_group(self, group_id: str, **kwargs) -> Any:
        """Patch a group
        
        Path: /api/v4/groups/{group_id}/patch
        Method: PUT
        """
        url = "/api/v4/groups/{group_id}/patch".format(group_id=group_id)
        return self.request("PUT", url, data=kwargs)

    def restore_group(self, group_id: str, **kwargs) -> Any:
        """Restore a previously deleted group.
        
        Path: /api/v4/groups/{group_id}/restore
        Method: POST
        """
        url = "/api/v4/groups/{group_id}/restore".format(group_id=group_id)
        return self.request("POST", url, data=kwargs)

    def link_group_syncable_for_team(self, group_id: str, team_id: str, **kwargs) -> Any:
        """Link a team to a group
        
        Path: /api/v4/groups/{group_id}/teams/{team_id}/link
        Method: POST
        """
        url = "/api/v4/groups/{group_id}/teams/{team_id}/link".format(group_id=group_id, team_id=team_id)
        return self.request("POST", url, data=kwargs)

    def unlink_group_syncable_for_team(self, group_id: str, team_id: str, **kwargs) -> Any:
        """Unlink a team from a group
        
        Path: /api/v4/groups/{group_id}/teams/{team_id}/link
        Method: DELETE
        """
        url = "/api/v4/groups/{group_id}/teams/{team_id}/link".format(group_id=group_id, team_id=team_id)
        return self.request("DELETE", url, params=kwargs)

    def link_group_syncable_for_channel(self, group_id: str, channel_id: str, **kwargs) -> Any:
        """Link a channel to a group
        
        Path: /api/v4/groups/{group_id}/channels/{channel_id}/link
        Method: POST
        """
        url = "/api/v4/groups/{group_id}/channels/{channel_id}/link".format(group_id=group_id, channel_id=channel_id)
        return self.request("POST", url, data=kwargs)

    def unlink_group_syncable_for_channel(self, group_id: str, channel_id: str, **kwargs) -> Any:
        """Unlink a channel from a group
        
        Path: /api/v4/groups/{group_id}/channels/{channel_id}/link
        Method: DELETE
        """
        url = "/api/v4/groups/{group_id}/channels/{channel_id}/link".format(group_id=group_id, channel_id=channel_id)
        return self.request("DELETE", url, params=kwargs)

    def get_group_syncable_for_team_id(self, group_id: str, team_id: str, **kwargs) -> Any:
        """Get a team syncable for a group
        
        Path: /api/v4/groups/{group_id}/teams/{team_id}
        Method: GET
        """
        url = "/api/v4/groups/{group_id}/teams/{team_id}".format(group_id=group_id, team_id=team_id)
        return self.request("GET", url, params=kwargs)

    def get_group_syncable_for_channel_id(self, group_id: str, channel_id: str, **kwargs) -> Any:
        """Get a channel syncable for a group
        
        Path: /api/v4/groups/{group_id}/channels/{channel_id}
        Method: GET
        """
        url = "/api/v4/groups/{group_id}/channels/{channel_id}".format(group_id=group_id, channel_id=channel_id)
        return self.request("GET", url, params=kwargs)

    def get_group_syncables_teams(self, group_id: str, **kwargs) -> Any:
        """Get team syncables for a group
        
        Path: /api/v4/groups/{group_id}/teams
        Method: GET
        """
        url = "/api/v4/groups/{group_id}/teams".format(group_id=group_id)
        return self.request("GET", url, params=kwargs)

    def get_group_syncables_channels(self, group_id: str, **kwargs) -> Any:
        """Get channel syncables for a group
        
        Path: /api/v4/groups/{group_id}/channels
        Method: GET
        """
        url = "/api/v4/groups/{group_id}/channels".format(group_id=group_id)
        return self.request("GET", url, params=kwargs)

    def patch_group_syncable_for_team(self, group_id: str, team_id: str, **kwargs) -> Any:
        """Patch a team syncable for a group
        
        Path: /api/v4/groups/{group_id}/teams/{team_id}/patch
        Method: PUT
        """
        url = "/api/v4/groups/{group_id}/teams/{team_id}/patch".format(group_id=group_id, team_id=team_id)
        return self.request("PUT", url, data=kwargs)

    def patch_group_syncable_for_channel(self, group_id: str, channel_id: str, **kwargs) -> Any:
        """Patch a channel syncable for a group
        
        Path: /api/v4/groups/{group_id}/channels/{channel_id}/patch
        Method: PUT
        """
        url = "/api/v4/groups/{group_id}/channels/{channel_id}/patch".format(group_id=group_id, channel_id=channel_id)
        return self.request("PUT", url, data=kwargs)

    def get_group_users(self, group_id: str, **kwargs) -> Any:
        """Get group users
        
        Path: /api/v4/groups/{group_id}/members
        Method: GET
        """
        url = "/api/v4/groups/{group_id}/members".format(group_id=group_id)
        return self.request("GET", url, params=kwargs)

    def add_group_members(self, group_id: str, **kwargs) -> Any:
        """Adds members to a custom group
        
        Path: /api/v4/groups/{group_id}/members
        Method: POST
        """
        url = "/api/v4/groups/{group_id}/members".format(group_id=group_id)
        return self.request("POST", url, data=kwargs)

    def delete_group_members(self, group_id: str, **kwargs) -> Any:
        """Removes members from a custom group
        
        Path: /api/v4/groups/{group_id}/members
        Method: DELETE
        """
        url = "/api/v4/groups/{group_id}/members".format(group_id=group_id)
        return self.request("DELETE", url, params=kwargs)

    def get_group_stats(self, group_id: str, **kwargs) -> Any:
        """Get group stats
        
        Path: /api/v4/groups/{group_id}/stats
        Method: GET
        """
        url = "/api/v4/groups/{group_id}/stats".format(group_id=group_id)
        return self.request("GET", url, params=kwargs)

    def get_groups_by_channel(self, channel_id: str, **kwargs) -> Any:
        """Get channel groups
        
        Path: /api/v4/channels/{channel_id}/groups
        Method: GET
        """
        url = "/api/v4/channels/{channel_id}/groups".format(channel_id=channel_id)
        return self.request("GET", url, params=kwargs)

    def get_groups_by_team(self, team_id: str, **kwargs) -> Any:
        """Get team groups
        
        Path: /api/v4/teams/{team_id}/groups
        Method: GET
        """
        url = "/api/v4/teams/{team_id}/groups".format(team_id=team_id)
        return self.request("GET", url, params=kwargs)

    def get_groups_associated_to_channels_by_team(self, team_id: str, **kwargs) -> Any:
        """Get team groups by channels
        
        Path: /api/v4/teams/{team_id}/groups_by_channels
        Method: GET
        """
        url = "/api/v4/teams/{team_id}/groups_by_channels".format(team_id=team_id)
        return self.request("GET", url, params=kwargs)

    def get_groups_by_user_id(self, user_id: str, **kwargs) -> Any:
        """Get groups for a userId
        
        Path: /api/v4/users/{user_id}/groups
        Method: GET
        """
        url = "/api/v4/users/{user_id}/groups".format(user_id=user_id)
        return self.request("GET", url, params=kwargs)

    def get_groups_by_names(self, **kwargs) -> Any:
        """Get groups by name
        
        Path: /api/v4/groups/names
        Method: POST
        """
        url = "/api/v4/groups/names"
        return self.request("POST", url, data=kwargs)
