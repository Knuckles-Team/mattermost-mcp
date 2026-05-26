"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def save_reaction(self, **kwargs) -> Any:
        """Create a reaction
        
        Path: /api/v4/reactions
        Method: POST
        """
        url = "/api/v4/reactions"
        return self.request("POST", url, data=kwargs)

    def get_reactions(self, post_id: str, **kwargs) -> Any:
        """Get a list of reactions to a post
        
        Path: /api/v4/posts/{post_id}/reactions
        Method: GET
        """
        url = "/api/v4/posts/{post_id}/reactions".format(post_id=post_id)
        return self.request("GET", url, params=kwargs)

    def delete_reaction(self, user_id: str, post_id: str, emoji_name: str, **kwargs) -> Any:
        """Remove a reaction from a post
        
        Path: /api/v4/users/{user_id}/posts/{post_id}/reactions/{emoji_name}
        Method: DELETE
        """
        url = "/api/v4/users/{user_id}/posts/{post_id}/reactions/{emoji_name}".format(user_id=user_id, post_id=post_id, emoji_name=emoji_name)
        return self.request("DELETE", url, params=kwargs)

    def get_bulk_reactions(self, **kwargs) -> Any:
        """Bulk get the reaction for posts
        
        Path: /api/v4/posts/ids/reactions
        Method: POST
        """
        url = "/api/v4/posts/ids/reactions"
        return self.request("POST", url, data=kwargs)
