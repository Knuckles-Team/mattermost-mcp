from mattermost_mcp.api.api_client_base import ApiClientBase

class Api(ApiClientBase):
    def get_teams(self) -> list:
        """Get Mattermost teams."""
        return self.request("GET", "/api/v4/teams")

    def get_team_members(self, team_id: str) -> list:
        """Get team members."""
        return self.request("GET", f"/api/v4/teams/{team_id}/members")
