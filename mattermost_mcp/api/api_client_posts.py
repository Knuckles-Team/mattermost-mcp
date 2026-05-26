"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def create_post(self, **kwargs) -> Any:
        """Create a post

        Path: /api/v4/posts
        Method: POST
        """
        url = "/api/v4/posts"
        return self.request("POST", url, data=kwargs)

    def create_post_ephemeral(self, **kwargs) -> Any:
        """Create a ephemeral post

        Path: /api/v4/posts/ephemeral
        Method: POST
        """
        url = "/api/v4/posts/ephemeral"
        return self.request("POST", url, data=kwargs)

    def search_posts_in_all_teams(self, **kwargs) -> Any:
        """Search posts across all teams

        Path: /api/v4/posts/search
        Method: POST
        """
        url = "/api/v4/posts/search"
        return self.request("POST", url, data=kwargs)

    def get_post(self, post_id: str, **kwargs) -> Any:
        """Get a post

        Path: /api/v4/posts/{post_id}
        Method: GET
        """
        url = f"/api/v4/posts/{post_id}"
        return self.request("GET", url, params=kwargs)

    def update_post(self, post_id: str, **kwargs) -> Any:
        """Update a post

        Path: /api/v4/posts/{post_id}
        Method: PUT
        """
        url = f"/api/v4/posts/{post_id}"
        return self.request("PUT", url, data=kwargs)

    def delete_post(self, post_id: str, **kwargs) -> Any:
        """Delete a post

        Path: /api/v4/posts/{post_id}
        Method: DELETE
        """
        url = f"/api/v4/posts/{post_id}"
        return self.request("DELETE", url, params=kwargs)

    def set_post_unread(self, user_id: str, post_id: str, **kwargs) -> Any:
        """Mark as unread from a post.

        Path: /api/v4/users/{user_id}/posts/{post_id}/set_unread
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/posts/{post_id}/set_unread"
        return self.request("POST", url, data=kwargs)

    def patch_post(self, post_id: str, **kwargs) -> Any:
        """Patch a post

        Path: /api/v4/posts/{post_id}/patch
        Method: PUT
        """
        url = f"/api/v4/posts/{post_id}/patch"
        return self.request("PUT", url, data=kwargs)

    def get_post_thread(self, post_id: str, **kwargs) -> Any:
        """Get a thread

        Path: /api/v4/posts/{post_id}/thread
        Method: GET
        """
        url = f"/api/v4/posts/{post_id}/thread"
        return self.request("GET", url, params=kwargs)

    def get_flagged_posts_for_user(self, user_id: str, **kwargs) -> Any:
        """Get a list of flagged posts

        Path: /api/v4/users/{user_id}/posts/flagged
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/posts/flagged"
        return self.request("GET", url, params=kwargs)

    def get_file_infos_for_post(self, post_id: str, **kwargs) -> Any:
        """Get file info for post

        Path: /api/v4/posts/{post_id}/files/info
        Method: GET
        """
        url = f"/api/v4/posts/{post_id}/files/info"
        return self.request("GET", url, params=kwargs)

    def get_post_info(self, post_id: str, **kwargs) -> Any:
        """Get post info

        Path: /api/v4/posts/{post_id}/info
        Method: GET
        """
        url = f"/api/v4/posts/{post_id}/info"
        return self.request("GET", url, params=kwargs)

    def get_edit_history_for_post(self, post_id: str, **kwargs) -> Any:
        """Get post edit history

        Path: /api/v4/posts/{post_id}/edit_history
        Method: GET
        """
        url = f"/api/v4/posts/{post_id}/edit_history"
        return self.request("GET", url, params=kwargs)

    def get_posts_for_channel(self, channel_id: str, **kwargs) -> Any:
        """Get posts for a channel

        Path: /api/v4/channels/{channel_id}/posts
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/posts"
        return self.request("GET", url, params=kwargs)

    def get_posts_around_last_unread(
        self, user_id: str, channel_id: str, **kwargs
    ) -> Any:
        """Get posts around oldest unread

        Path: /api/v4/users/{user_id}/channels/{channel_id}/posts/unread
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/channels/{channel_id}/posts/unread"
        return self.request("GET", url, params=kwargs)

    def search_posts(self, team_id: str, **kwargs) -> Any:
        """Search for team posts

        Path: /api/v4/teams/{team_id}/posts/search
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/posts/search"
        return self.request("POST", url, data=kwargs)

    def pin_post(self, post_id: str, **kwargs) -> Any:
        """Pin a post to the channel

        Path: /api/v4/posts/{post_id}/pin
        Method: POST
        """
        url = f"/api/v4/posts/{post_id}/pin"
        return self.request("POST", url, data=kwargs)

    def unpin_post(self, post_id: str, **kwargs) -> Any:
        """Unpin a post to the channel

        Path: /api/v4/posts/{post_id}/unpin
        Method: POST
        """
        url = f"/api/v4/posts/{post_id}/unpin"
        return self.request("POST", url, data=kwargs)

    def do_post_action(self, post_id: str, action_id: str, **kwargs) -> Any:
        """Perform a post action

        Path: /api/v4/posts/{post_id}/actions/{action_id}
        Method: POST
        """
        url = f"/api/v4/posts/{post_id}/actions/{action_id}"
        return self.request("POST", url, data=kwargs)

    def get_posts_by_ids(self, **kwargs) -> Any:
        """Get posts by a list of ids

        Path: /api/v4/posts/ids
        Method: POST
        """
        url = "/api/v4/posts/ids"
        return self.request("POST", url, data=kwargs)

    def set_post_reminder(self, user_id: str, post_id: str, **kwargs) -> Any:
        """Set a post reminder

        Path: /api/v4/users/{user_id}/posts/{post_id}/reminder
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/posts/{post_id}/reminder"
        return self.request("POST", url, data=kwargs)

    def save_acknowledgement_for_post(
        self, user_id: str, post_id: str, **kwargs
    ) -> Any:
        """Acknowledge a post

        Path: /api/v4/users/{user_id}/posts/{post_id}/ack
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/posts/{post_id}/ack"
        return self.request("POST", url, data=kwargs)

    def delete_acknowledgement_for_post(
        self, user_id: str, post_id: str, **kwargs
    ) -> Any:
        """Delete a post acknowledgement

        Path: /api/v4/users/{user_id}/posts/{post_id}/ack
        Method: DELETE
        """
        url = f"/api/v4/users/{user_id}/posts/{post_id}/ack"
        return self.request("DELETE", url, params=kwargs)

    def move_thread(self, post_id: str, **kwargs) -> Any:
        """Move a post (and any posts within that post's thread)

        Path: /api/v4/posts/{post_id}/move
        Method: POST
        """
        url = f"/api/v4/posts/{post_id}/move"
        return self.request("POST", url, data=kwargs)

    def restore_post_version(
        self, post_id: str, restore_version_id: str, **kwargs
    ) -> Any:
        """Restores a past version of a post

        Path: /api/v4/posts/{post_id}/restore/{restore_version_id}
        Method: POST
        """
        url = f"/api/v4/posts/{post_id}/restore/{restore_version_id}"
        return self.request("POST", url, data=kwargs)

    def reveal_post(self, post_id: str, **kwargs) -> Any:
        """Reveal a burn-on-read post

        Path: /api/v4/posts/{post_id}/reveal
        Method: GET
        """
        url = f"/api/v4/posts/{post_id}/reveal"
        return self.request("GET", url, params=kwargs)

    def burn_post(self, post_id: str, **kwargs) -> Any:
        """Burn a burn-on-read post

        Path: /api/v4/posts/{post_id}/burn
        Method: DELETE
        """
        url = f"/api/v4/posts/{post_id}/burn"
        return self.request("DELETE", url, params=kwargs)

    def rewrite_message(self, **kwargs) -> Any:
        """Rewrite a message using AI

        Path: /api/v4/posts/rewrite
        Method: POST
        """
        url = "/api/v4/posts/rewrite"
        return self.request("POST", url, data=kwargs)
