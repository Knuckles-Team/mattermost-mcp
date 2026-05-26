"""
This file was automatically generated. Do not edit manually.
"""
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_c_f_flag_config(self, **kwargs) -> Any:
        """Get content flagging configuration
        
        Path: /api/v4/content_flagging/flag/config
        Method: GET
        """
        url = "/api/v4/content_flagging/flag/config"
        return self.request("GET", url, params=kwargs)

    def get_c_f_team_status(self, team_id: str, **kwargs) -> Any:
        """Get content flagging status for a team
        
        Path: /api/v4/content_flagging/team/{team_id}/status
        Method: GET
        """
        url = "/api/v4/content_flagging/team/{team_id}/status".format(team_id=team_id)
        return self.request("GET", url, params=kwargs)

    def post_c_f_post_flag(self, post_id: str, **kwargs) -> Any:
        """Flag a post
        
        Path: /api/v4/content_flagging/post/{post_id}/flag
        Method: POST
        """
        url = "/api/v4/content_flagging/post/{post_id}/flag".format(post_id=post_id)
        return self.request("POST", url, data=kwargs)

    def get_c_f_fields(self, **kwargs) -> Any:
        """Get content flagging property fields
        
        Path: /api/v4/content_flagging/fields
        Method: GET
        """
        url = "/api/v4/content_flagging/fields"
        return self.request("GET", url, params=kwargs)

    def get_c_f_post_field_values(self, post_id: str, **kwargs) -> Any:
        """Get content flagging property field values for a post
        
        Path: /api/v4/content_flagging/post/{post_id}/field_values
        Method: GET
        """
        url = "/api/v4/content_flagging/post/{post_id}/field_values".format(post_id=post_id)
        return self.request("GET", url, params=kwargs)

    def get_c_f_post(self, post_id: str, **kwargs) -> Any:
        """Get a flagged post with all its content.
        
        Path: /api/v4/content_flagging/post/{post_id}
        Method: GET
        """
        url = "/api/v4/content_flagging/post/{post_id}".format(post_id=post_id)
        return self.request("GET", url, params=kwargs)

    def remove_c_f_post(self, post_id: str, **kwargs) -> Any:
        """Remove a flagged post
        
        Path: /api/v4/content_flagging/post/{post_id}/remove
        Method: PUT
        """
        url = "/api/v4/content_flagging/post/{post_id}/remove".format(post_id=post_id)
        return self.request("PUT", url, data=kwargs)

    def keep_c_f_post(self, post_id: str, **kwargs) -> Any:
        """Keep a flagged post
        
        Path: /api/v4/content_flagging/post/{post_id}/keep
        Method: PUT
        """
        url = "/api/v4/content_flagging/post/{post_id}/keep".format(post_id=post_id)
        return self.request("PUT", url, data=kwargs)

    def get_c_f_config(self, **kwargs) -> Any:
        """Get the system content flagging configuration
        
        Path: /api/v4/content_flagging/config
        Method: GET
        """
        url = "/api/v4/content_flagging/config"
        return self.request("GET", url, params=kwargs)

    def update_c_f_config(self, **kwargs) -> Any:
        """Update the system content flagging configuration
        
        Path: /api/v4/content_flagging/config
        Method: PUT
        """
        url = "/api/v4/content_flagging/config"
        return self.request("PUT", url, data=kwargs)

    def search_c_f_team_reviewers(self, team_id: str, **kwargs) -> Any:
        """Search content reviewers in a team
        
        Path: /api/v4/content_flagging/team/{team_id}/reviewers/search
        Method: GET
        """
        url = "/api/v4/content_flagging/team/{team_id}/reviewers/search".format(team_id=team_id)
        return self.request("GET", url, params=kwargs)

    def post_c_f_post_reviewer(self, post_id: str, content_reviewer_id: str, **kwargs) -> Any:
        """Assign a content reviewer to a flagged post
        
        Path: /api/v4/content_flagging/post/{post_id}/assign/{content_reviewer_id}
        Method: POST
        """
        url = "/api/v4/content_flagging/post/{post_id}/assign/{content_reviewer_id}".format(post_id=post_id, content_reviewer_id=content_reviewer_id)
        return self.request("POST", url, data=kwargs)

    def generate_c_f_post_report(self, post_id: str, **kwargs) -> Any:
        """Generate and download a flagged post report
        
        Path: /api/v4/content_flagging/post/{post_id}/report
        Method: POST
        """
        url = "/api/v4/content_flagging/post/{post_id}/report".format(post_id=post_id)
        return self.request("POST", url, data=kwargs)
