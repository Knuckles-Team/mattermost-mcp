from mattermost_mcp.api.api_client_base import ApiClientBase

class Api(ApiClientBase):
    def get_users(self) -> list:
        """Get users list."""
        return self.request("GET", "/api/v4/users")

    def get_me(self) -> dict:
        """Get current authenticated user info."""
        return self.request("GET", "/api/v4/users/me")
