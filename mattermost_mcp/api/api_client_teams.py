"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_all_teams(self, **kwargs) -> Any:
        """Get teams

        Path: /api/v4/teams
        Method: GET
        """
        url = "/api/v4/teams"
        return self.request("GET", url, params=kwargs)

    def create_team(self, **kwargs) -> Any:
        """Create a team

        Path: /api/v4/teams
        Method: POST
        """
        url = "/api/v4/teams"
        return self.request("POST", url, data=kwargs)

    def get_team(self, team_id: str, **kwargs) -> Any:
        """Get a team

        Path: /api/v4/teams/{team_id}
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}"
        return self.request("GET", url, params=kwargs)

    def update_team(self, team_id: str, **kwargs) -> Any:
        """Update a team

        Path: /api/v4/teams/{team_id}
        Method: PUT
        """
        url = f"/api/v4/teams/{team_id}"
        return self.request("PUT", url, data=kwargs)

    def soft_delete_team(self, team_id: str, **kwargs) -> Any:
        """Delete a team

        Path: /api/v4/teams/{team_id}
        Method: DELETE
        """
        url = f"/api/v4/teams/{team_id}"
        return self.request("DELETE", url, params=kwargs)

    def patch_team(self, team_id: str, **kwargs) -> Any:
        """Patch a team

        Path: /api/v4/teams/{team_id}/patch
        Method: PUT
        """
        url = f"/api/v4/teams/{team_id}/patch"
        return self.request("PUT", url, data=kwargs)

    def update_team_privacy(self, team_id: str, **kwargs) -> Any:
        """Update teams's privacy

        Path: /api/v4/teams/{team_id}/privacy
        Method: PUT
        """
        url = f"/api/v4/teams/{team_id}/privacy"
        return self.request("PUT", url, data=kwargs)

    def restore_team(self, team_id: str, **kwargs) -> Any:
        """Restore a team

        Path: /api/v4/teams/{team_id}/restore
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/restore"
        return self.request("POST", url, data=kwargs)

    def get_team_by_name(self, team_name: str, **kwargs) -> Any:
        """Get a team by name

        Path: /api/v4/teams/name/{team_name}
        Method: GET
        """
        url = f"/api/v4/teams/name/{team_name}"
        return self.request("GET", url, params=kwargs)

    def search_teams(self, **kwargs) -> Any:
        """Search teams

        Path: /api/v4/teams/search
        Method: POST
        """
        url = "/api/v4/teams/search"
        return self.request("POST", url, data=kwargs)

    def team_exists(self, team_name: str, **kwargs) -> Any:
        """Check if team exists

        Path: /api/v4/teams/name/{team_name}/exists
        Method: GET
        """
        url = f"/api/v4/teams/name/{team_name}/exists"
        return self.request("GET", url, params=kwargs)

    def get_teams_for_user(self, user_id: str, **kwargs) -> Any:
        """Get a user's teams

        Path: /api/v4/users/{user_id}/teams
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/teams"
        return self.request("GET", url, params=kwargs)

    def get_team_members(self, team_id: str, **kwargs) -> Any:
        """Get team members

        Path: /api/v4/teams/{team_id}/members
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/members"
        return self.request("GET", url, params=kwargs)

    def add_team_member(self, team_id: str, **kwargs) -> Any:
        """Add user to team

        Path: /api/v4/teams/{team_id}/members
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/members"
        return self.request("POST", url, data=kwargs)

    def add_team_member_from_invite(self, **kwargs) -> Any:
        """Add user to team from invite

        Path: /api/v4/teams/members/invite
        Method: POST
        """
        url = "/api/v4/teams/members/invite"
        return self.request("POST", url, data=kwargs)

    def add_team_members(self, team_id: str, **kwargs) -> Any:
        """Add multiple users to team

        Path: /api/v4/teams/{team_id}/members/batch
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/members/batch"
        return self.request("POST", url, data=kwargs)

    def get_team_members_for_user(self, user_id: str, **kwargs) -> Any:
        """Get team members for a user

        Path: /api/v4/users/{user_id}/teams/members
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/teams/members"
        return self.request("GET", url, params=kwargs)

    def get_team_member(self, team_id: str, user_id: str, **kwargs) -> Any:
        """Get a team member

        Path: /api/v4/teams/{team_id}/members/{user_id}
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/members/{user_id}"
        return self.request("GET", url, params=kwargs)

    def remove_team_member(self, team_id: str, user_id: str, **kwargs) -> Any:
        """Remove user from team

        Path: /api/v4/teams/{team_id}/members/{user_id}
        Method: DELETE
        """
        url = f"/api/v4/teams/{team_id}/members/{user_id}"
        return self.request("DELETE", url, params=kwargs)

    def get_team_members_by_ids(self, team_id: str, **kwargs) -> Any:
        """Get team members by ids

        Path: /api/v4/teams/{team_id}/members/ids
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/members/ids"
        return self.request("POST", url, data=kwargs)

    def get_team_stats(self, team_id: str, **kwargs) -> Any:
        """Get a team stats

        Path: /api/v4/teams/{team_id}/stats
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/stats"
        return self.request("GET", url, params=kwargs)

    def regenerate_team_invite_id(self, team_id: str, **kwargs) -> Any:
        """Regenerate the Invite ID from a Team

        Path: /api/v4/teams/{team_id}/regenerate_invite_id
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/regenerate_invite_id"
        return self.request("POST", url, data=kwargs)

    def get_team_icon(self, team_id: str, **kwargs) -> Any:
        """Get the team icon

        Path: /api/v4/teams/{team_id}/image
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/image"
        return self.request("GET", url, params=kwargs)

    def set_team_icon(self, team_id: str, **kwargs) -> Any:
        """Sets the team icon

        Path: /api/v4/teams/{team_id}/image
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/image"
        return self.request("POST", url, data=kwargs)

    def remove_team_icon(self, team_id: str, **kwargs) -> Any:
        """Remove the team icon

        Path: /api/v4/teams/{team_id}/image
        Method: DELETE
        """
        url = f"/api/v4/teams/{team_id}/image"
        return self.request("DELETE", url, params=kwargs)

    def update_team_member_roles(self, team_id: str, user_id: str, **kwargs) -> Any:
        """Update a team member roles

        Path: /api/v4/teams/{team_id}/members/{user_id}/roles
        Method: PUT
        """
        url = f"/api/v4/teams/{team_id}/members/{user_id}/roles"
        return self.request("PUT", url, data=kwargs)

    def update_team_member_scheme_roles(
        self, team_id: str, user_id: str, **kwargs
    ) -> Any:
        """Update the scheme-derived roles of a team member.

        Path: /api/v4/teams/{team_id}/members/{user_id}/schemeRoles
        Method: PUT
        """
        url = f"/api/v4/teams/{team_id}/members/{user_id}/schemeRoles"
        return self.request("PUT", url, data=kwargs)

    def get_teams_unread_for_user(self, user_id: str, **kwargs) -> Any:
        """Get team unreads for a user

        Path: /api/v4/users/{user_id}/teams/unread
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/teams/unread"
        return self.request("GET", url, params=kwargs)

    def get_team_unread(self, user_id: str, team_id: str, **kwargs) -> Any:
        """Get unreads for a team

        Path: /api/v4/users/{user_id}/teams/{team_id}/unread
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/unread"
        return self.request("GET", url, params=kwargs)

    def invite_users_to_team(self, team_id: str, **kwargs) -> Any:
        """Invite users to the team by email

        Path: /api/v4/teams/{team_id}/invite/email
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/invite/email"
        return self.request("POST", url, data=kwargs)

    def invite_guests_to_team(self, team_id: str, **kwargs) -> Any:
        """Invite guests to the team by email

        Path: /api/v4/teams/{team_id}/invite-guests/email
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/invite-guests/email"
        return self.request("POST", url, data=kwargs)

    def invalidate_email_invites(self, **kwargs) -> Any:
        """Invalidate active email invitations

        Path: /api/v4/teams/invites/email
        Method: DELETE
        """
        url = "/api/v4/teams/invites/email"
        return self.request("DELETE", url, params=kwargs)

    def import_team(self, team_id: str, **kwargs) -> Any:
        """Import a Team from other application

        Path: /api/v4/teams/{team_id}/import
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/import"
        return self.request("POST", url, data=kwargs)

    def get_team_invite_info(self, invite_id: str, **kwargs) -> Any:
        """Get invite info for a team

        Path: /api/v4/teams/invite/{invite_id}
        Method: GET
        """
        url = f"/api/v4/teams/invite/{invite_id}"
        return self.request("GET", url, params=kwargs)

    def update_team_scheme(self, team_id: str, **kwargs) -> Any:
        """Set a team's scheme

        Path: /api/v4/teams/{team_id}/scheme
        Method: PUT
        """
        url = f"/api/v4/teams/{team_id}/scheme"
        return self.request("PUT", url, data=kwargs)

    def team_members_minus_group_members(self, team_id: str, **kwargs) -> Any:
        """Team members minus group members.

        Path: /api/v4/teams/{team_id}/members_minus_group_members
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/members_minus_group_members"
        return self.request("GET", url, params=kwargs)
