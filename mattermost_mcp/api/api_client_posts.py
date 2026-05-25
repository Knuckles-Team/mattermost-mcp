from mattermost_mcp.api.api_client_base import ApiClientBase

class Api(ApiClientBase):
    def create_post(self, channel_id: str, message: str, root_id: str = None) -> dict:
        """Post a message."""
        return self.request("POST", "/api/v4/posts", data={
            "channel_id": channel_id,
            "message": message,
            "root_id": root_id
        })

    def delete_post(self, post_id: str) -> dict:
        """Delete post."""
        return self.request("DELETE", f"/api/v4/posts/{post_id}")
