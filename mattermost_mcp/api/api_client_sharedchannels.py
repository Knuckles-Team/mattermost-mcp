"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_all_shared_channels(self, team_id: str, **kwargs) -> Any:
        """Get all shared channels for team.

        Path: /api/v4/sharedchannels/{team_id}
        Method: GET
        """
        url = f"/api/v4/sharedchannels/{team_id}"
        return self.request("GET", url, params=kwargs)

    def get_shared_channel_remotes_by_remote_cluster(
        self, remote_id: str, **kwargs
    ) -> Any:
        """Get shared channel remotes by remote cluster.

        Path: /api/v4/remotecluster/{remote_id}/sharedchannelremotes
        Method: GET
        """
        url = f"/api/v4/remotecluster/{remote_id}/sharedchannelremotes"
        return self.request("GET", url, params=kwargs)

    def get_remote_cluster_info(self, remote_id: str, **kwargs) -> Any:
        """Get remote cluster info by ID for user.

        Path: /api/v4/sharedchannels/remote_info/{remote_id}
        Method: GET
        """
        url = f"/api/v4/sharedchannels/remote_info/{remote_id}"
        return self.request("GET", url, params=kwargs)

    def invite_remote_cluster_to_channel(
        self, remote_id: str, channel_id: str, **kwargs
    ) -> Any:
        """Invites a remote cluster to a channel.

        Path: /api/v4/remotecluster/{remote_id}/channels/{channel_id}/invite
        Method: POST
        """
        url = f"/api/v4/remotecluster/{remote_id}/channels/{channel_id}/invite"
        return self.request("POST", url, data=kwargs)

    def uninvite_remote_cluster_to_channel(
        self, remote_id: str, channel_id: str, **kwargs
    ) -> Any:
        """Uninvites a remote cluster to a channel.

        Path: /api/v4/remotecluster/{remote_id}/channels/{channel_id}/uninvite
        Method: POST
        """
        url = f"/api/v4/remotecluster/{remote_id}/channels/{channel_id}/uninvite"
        return self.request("POST", url, data=kwargs)

    def get_shared_channel_remotes(self, channel_id: str, **kwargs) -> Any:
        """Get remote clusters for a shared channel

        Path: /api/v4/sharedchannels/{channel_id}/remotes
        Method: GET
        """
        url = f"/api/v4/sharedchannels/{channel_id}/remotes"
        return self.request("GET", url, params=kwargs)

    def can_user_direct_message(
        self, user_id: str, other_user_id: str, **kwargs
    ) -> Any:
        """Check if user can DM another user in shared channels context

        Path: /api/v4/sharedchannels/users/{user_id}/can_dm/{other_user_id}
        Method: GET
        """
        url = f"/api/v4/sharedchannels/users/{user_id}/can_dm/{other_user_id}"
        return self.request("GET", url, params=kwargs)
