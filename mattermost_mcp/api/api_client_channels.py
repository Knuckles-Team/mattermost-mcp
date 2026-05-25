from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_channels(self, team_id: str) -> list:
        """Get team channels."""
        return self.request("GET", f"/api/v4/teams/{team_id}/channels")

    def create_channel(
        self, team_id: str, name: str, display_name: str, channel_type: str = "O"
    ) -> dict:
        """Create channel."""
        return self.request(
            "POST",
            "/api/v4/channels",
            data={
                "team_id": team_id,
                "name": name,
                "display_name": display_name,
                "type": channel_type,
            },
        )
