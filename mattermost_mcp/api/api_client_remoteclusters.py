"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_remote_clusters(self, **kwargs) -> Any:
        """Get a list of remote clusters.
        
        Path: /api/v4/remotecluster
        Method: GET
        """
        url = "/api/v4/remotecluster"
        return self.request("GET", url, params=kwargs)

    def create_remote_cluster(self, **kwargs) -> Any:
        """Create a new remote cluster.
        
        Path: /api/v4/remotecluster
        Method: POST
        """
        url = "/api/v4/remotecluster"
        return self.request("POST", url, data=kwargs)

    def get_remote_cluster(self, remote_id: str, **kwargs) -> Any:
        """Get a remote cluster.
        
        Path: /api/v4/remotecluster/{remote_id}
        Method: GET
        """
        url = "/api/v4/remotecluster/{remote_id}".format(remote_id=remote_id)
        return self.request("GET", url, params=kwargs)

    def delete_remote_cluster(self, remote_id: str, **kwargs) -> Any:
        """Delete a remote cluster.
        
        Path: /api/v4/remotecluster/{remote_id}
        Method: DELETE
        """
        url = "/api/v4/remotecluster/{remote_id}".format(remote_id=remote_id)
        return self.request("DELETE", url, params=kwargs)

    def patch_remote_cluster(self, remote_id: str, **kwargs) -> Any:
        """Patch a remote cluster.
        
        Path: /api/v4/remotecluster/{remote_id}
        Method: PATCH
        """
        url = "/api/v4/remotecluster/{remote_id}".format(remote_id=remote_id)
        return self.request("PATCH", url, data=kwargs)

    def generate_remote_cluster_invite(self, remote_id: str, **kwargs) -> Any:
        """Generate invite code.
        
        Path: /api/v4/remotecluster/{remote_id}/generate_invite
        Method: POST
        """
        url = "/api/v4/remotecluster/{remote_id}/generate_invite".format(remote_id=remote_id)
        return self.request("POST", url, data=kwargs)

    def accept_remote_cluster_invite(self, **kwargs) -> Any:
        """Accept a remote cluster invite code.
        
        Path: /api/v4/remotecluster/accept_invite
        Method: POST
        """
        url = "/api/v4/remotecluster/accept_invite"
        return self.request("POST", url, data=kwargs)

    def remote_cluster_ping(self, **kwargs) -> Any:
        """Receive a ping from a remote cluster.
        
        Path: /api/v4/remotecluster/ping
        Method: POST
        """
        url = "/api/v4/remotecluster/ping"
        return self.request("POST", url, data=kwargs)

    def remote_cluster_accept_message(self, **kwargs) -> Any:
        """Receive a remote cluster message.
        
        Path: /api/v4/remotecluster/msg
        Method: POST
        """
        url = "/api/v4/remotecluster/msg"
        return self.request("POST", url, data=kwargs)

    def remote_cluster_confirm_invite(self, **kwargs) -> Any:
        """Confirm an invite with a remote cluster.
        
        Path: /api/v4/remotecluster/confirm_invite
        Method: POST
        """
        url = "/api/v4/remotecluster/confirm_invite"
        return self.request("POST", url, data=kwargs)

    def upload_remote_cluster_data(self, upload_id: str, **kwargs) -> Any:
        """Upload file data for a remote upload session.
        
        Path: /api/v4/remotecluster/upload/{upload_id}
        Method: POST
        """
        url = "/api/v4/remotecluster/upload/{upload_id}".format(upload_id=upload_id)
        return self.request("POST", url, data=kwargs)

    def remote_set_profile_image(self, user_id: str, **kwargs) -> Any:
        """Set profile image for a remote user.
        
        Path: /api/v4/remotecluster/{user_id}/image
        Method: POST
        """
        url = "/api/v4/remotecluster/{user_id}/image".format(user_id=user_id)
        return self.request("POST", url, data=kwargs)
