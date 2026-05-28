"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def list_commands(self, **kwargs) -> Any:
        """List commands for a team

        Path: /api/v4/commands
        Method: GET
        """
        url = "/api/v4/commands"
        return self.request("GET", url, params=kwargs)

    def create_command(self, **kwargs) -> Any:
        """Create a command

        Path: /api/v4/commands
        Method: POST
        """
        url = "/api/v4/commands"
        return self.request("POST", url, data=kwargs)

    def list_autocomplete_commands(self, team_id: str, **kwargs) -> Any:
        """List autocomplete commands

        Path: /api/v4/teams/{team_id}/commands/autocomplete
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/commands/autocomplete"
        return self.request("GET", url, params=kwargs)

    def list_command_autocomplete_suggestions(self, team_id: str, **kwargs) -> Any:
        """List commands' autocomplete data

        Path: /api/v4/teams/{team_id}/commands/autocomplete_suggestions
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/commands/autocomplete_suggestions"
        return self.request("GET", url, params=kwargs)

    def get_command_by_id(self, command_id: str, **kwargs) -> Any:
        """Get a command

        Path: /api/v4/commands/{command_id}
        Method: GET
        """
        url = f"/api/v4/commands/{command_id}"
        return self.request("GET", url, params=kwargs)

    def update_command(self, command_id: str, **kwargs) -> Any:
        """Update a command

        Path: /api/v4/commands/{command_id}
        Method: PUT
        """
        url = f"/api/v4/commands/{command_id}"
        return self.request("PUT", url, data=kwargs)

    def delete_command(self, command_id: str, **kwargs) -> Any:
        """Delete a command

        Path: /api/v4/commands/{command_id}
        Method: DELETE
        """
        url = f"/api/v4/commands/{command_id}"
        return self.request("DELETE", url, params=kwargs)

    def move_command(self, command_id: str, **kwargs) -> Any:
        """Move a command

        Path: /api/v4/commands/{command_id}/move
        Method: PUT
        """
        url = f"/api/v4/commands/{command_id}/move"
        return self.request("PUT", url, data=kwargs)

    def regen_command_token(self, command_id: str, **kwargs) -> Any:
        """Generate a new token

        Path: /api/v4/commands/{command_id}/regen_token
        Method: PUT
        """
        url = f"/api/v4/commands/{command_id}/regen_token"
        return self.request("PUT", url, data=kwargs)

    def execute_command(self, **kwargs) -> Any:
        """Execute a command

        Path: /api/v4/commands/execute
        Method: POST
        """
        url = "/api/v4/commands/execute"
        return self.request("POST", url, data=kwargs)
