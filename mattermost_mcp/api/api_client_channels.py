"""
This file was automatically generated. Do not edit manually.
"""

from typing import Any

from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
    def get_all_channels(self, **kwargs) -> Any:
        """Get a list of all channels

        Path: /api/v4/channels
        Method: GET
        """
        url = "/api/v4/channels"
        return self.request("GET", url, params=kwargs)

    def create_channel(self, **kwargs) -> Any:
        """Create a channel

        Path: /api/v4/channels
        Method: POST
        """
        url = "/api/v4/channels"
        return self.request("POST", url, data=kwargs)

    def create_direct_channel(self, **kwargs) -> Any:
        """Create a direct message channel

        Path: /api/v4/channels/direct
        Method: POST
        """
        url = "/api/v4/channels/direct"
        return self.request("POST", url, data=kwargs)

    def create_group_channel(self, **kwargs) -> Any:
        """Create a group message channel

        Path: /api/v4/channels/group
        Method: POST
        """
        url = "/api/v4/channels/group"
        return self.request("POST", url, data=kwargs)

    def search_all_channels(self, **kwargs) -> Any:
        """Search all private and open type channels across all teams

        Path: /api/v4/channels/search
        Method: POST
        """
        url = "/api/v4/channels/search"
        return self.request("POST", url, data=kwargs)

    def search_group_channels(self, **kwargs) -> Any:
        """Search Group Channels

        Path: /api/v4/channels/group/search
        Method: POST
        """
        url = "/api/v4/channels/group/search"
        return self.request("POST", url, data=kwargs)

    def get_public_channels_by_ids_for_team(self, team_id: str, **kwargs) -> Any:
        """Get a list of channels by ids

        Path: /api/v4/teams/{team_id}/channels/ids
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/channels/ids"
        return self.request("POST", url, data=kwargs)

    def get_channel_members_timezones(self, channel_id: str, **kwargs) -> Any:
        """Get timezones in a channel

        Path: /api/v4/channels/{channel_id}/timezones
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/timezones"
        return self.request("GET", url, params=kwargs)

    def get_channel(self, channel_id: str, **kwargs) -> Any:
        """Get a channel

        Path: /api/v4/channels/{channel_id}
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}"
        return self.request("GET", url, params=kwargs)

    def update_channel(self, channel_id: str, **kwargs) -> Any:
        """Update a channel

        Path: /api/v4/channels/{channel_id}
        Method: PUT
        """
        url = f"/api/v4/channels/{channel_id}"
        return self.request("PUT", url, data=kwargs)

    def delete_channel(self, channel_id: str, **kwargs) -> Any:
        """Delete a channel

        Path: /api/v4/channels/{channel_id}
        Method: DELETE
        """
        url = f"/api/v4/channels/{channel_id}"
        return self.request("DELETE", url, params=kwargs)

    def patch_channel(self, channel_id: str, **kwargs) -> Any:
        """Patch a channel

        Path: /api/v4/channels/{channel_id}/patch
        Method: PUT
        """
        url = f"/api/v4/channels/{channel_id}/patch"
        return self.request("PUT", url, data=kwargs)

    def update_channel_privacy(self, channel_id: str, **kwargs) -> Any:
        """Update channel's privacy

        Path: /api/v4/channels/{channel_id}/privacy
        Method: PUT
        """
        url = f"/api/v4/channels/{channel_id}/privacy"
        return self.request("PUT", url, data=kwargs)

    def restore_channel(self, channel_id: str, **kwargs) -> Any:
        """Restore a channel

        Path: /api/v4/channels/{channel_id}/restore
        Method: POST
        """
        url = f"/api/v4/channels/{channel_id}/restore"
        return self.request("POST", url, data=kwargs)

    def move_channel(self, channel_id: str, **kwargs) -> Any:
        """Move a channel

        Path: /api/v4/channels/{channel_id}/move
        Method: POST
        """
        url = f"/api/v4/channels/{channel_id}/move"
        return self.request("POST", url, data=kwargs)

    def get_channel_stats(self, channel_id: str, **kwargs) -> Any:
        """Get channel statistics

        Path: /api/v4/channels/{channel_id}/stats
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/stats"
        return self.request("GET", url, params=kwargs)

    def get_pinned_posts(self, channel_id: str, **kwargs) -> Any:
        """Get a channel's pinned posts

        Path: /api/v4/channels/{channel_id}/pinned
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/pinned"
        return self.request("GET", url, params=kwargs)

    def get_public_channels_for_team(self, team_id: str, **kwargs) -> Any:
        """Get public channels

        Path: /api/v4/teams/{team_id}/channels
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/channels"
        return self.request("GET", url, params=kwargs)

    def get_private_channels_for_team(self, team_id: str, **kwargs) -> Any:
        """Get private channels

        Path: /api/v4/teams/{team_id}/channels/private
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/channels/private"
        return self.request("GET", url, params=kwargs)

    def get_recommended_channels_for_team(self, team_id: str, **kwargs) -> Any:
        """Get recommended public channels for the current user

        Path: /api/v4/teams/{team_id}/channels/recommended
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/channels/recommended"
        return self.request("GET", url, params=kwargs)

    def get_deleted_channels_for_team(self, team_id: str, **kwargs) -> Any:
        """Get deleted channels

        Path: /api/v4/teams/{team_id}/channels/deleted
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/channels/deleted"
        return self.request("GET", url, params=kwargs)

    def autocomplete_channels_for_team(self, team_id: str, **kwargs) -> Any:
        """Autocomplete channels

        Path: /api/v4/teams/{team_id}/channels/autocomplete
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/channels/autocomplete"
        return self.request("GET", url, params=kwargs)

    def autocomplete_channels_for_team_for_search(self, team_id: str, **kwargs) -> Any:
        """Autocomplete channels for search

        Path: /api/v4/teams/{team_id}/channels/search_autocomplete
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/channels/search_autocomplete"
        return self.request("GET", url, params=kwargs)

    def get_managed_categories(self, team_id: str, **kwargs) -> Any:
        """Get managed category mappings

        Path: /api/v4/teams/{team_id}/channels/managed_categories
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/channels/managed_categories"
        return self.request("GET", url, params=kwargs)

    def search_channels(self, team_id: str, **kwargs) -> Any:
        """Search channels

        Path: /api/v4/teams/{team_id}/channels/search
        Method: POST
        """
        url = f"/api/v4/teams/{team_id}/channels/search"
        return self.request("POST", url, data=kwargs)

    def get_channel_by_name(self, team_id: str, channel_name: str, **kwargs) -> Any:
        """Get a channel by name

        Path: /api/v4/teams/{team_id}/channels/name/{channel_name}
        Method: GET
        """
        url = f"/api/v4/teams/{team_id}/channels/name/{channel_name}"
        return self.request("GET", url, params=kwargs)

    def get_channel_by_name_for_team_name(
        self, team_name: str, channel_name: str, **kwargs
    ) -> Any:
        """Get a channel by name and team name

        Path: /api/v4/teams/name/{team_name}/channels/name/{channel_name}
        Method: GET
        """
        url = f"/api/v4/teams/name/{team_name}/channels/name/{channel_name}"
        return self.request("GET", url, params=kwargs)

    def get_channel_members(self, channel_id: str, **kwargs) -> Any:
        """Get channel members

        Path: /api/v4/channels/{channel_id}/members
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/members"
        return self.request("GET", url, params=kwargs)

    def add_channel_member(self, channel_id: str, **kwargs) -> Any:
        """Add user(s) to channel

        Path: /api/v4/channels/{channel_id}/members
        Method: POST
        """
        url = f"/api/v4/channels/{channel_id}/members"
        return self.request("POST", url, data=kwargs)

    def set_channel_members(self, channel_id: str, **kwargs) -> Any:
        """Set channel members

        Path: /api/v4/channels/{channel_id}/members
        Method: PUT
        """
        url = f"/api/v4/channels/{channel_id}/members"
        return self.request("PUT", url, data=kwargs)

    def get_channel_members_by_ids(self, channel_id: str, **kwargs) -> Any:
        """Get channel members by ids

        Path: /api/v4/channels/{channel_id}/members/ids
        Method: POST
        """
        url = f"/api/v4/channels/{channel_id}/members/ids"
        return self.request("POST", url, data=kwargs)

    def get_channel_member(self, channel_id: str, user_id: str, **kwargs) -> Any:
        """Get channel member

        Path: /api/v4/channels/{channel_id}/members/{user_id}
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/members/{user_id}"
        return self.request("GET", url, params=kwargs)

    def remove_user_from_channel(self, channel_id: str, user_id: str, **kwargs) -> Any:
        """Remove user from channel

        Path: /api/v4/channels/{channel_id}/members/{user_id}
        Method: DELETE
        """
        url = f"/api/v4/channels/{channel_id}/members/{user_id}"
        return self.request("DELETE", url, params=kwargs)

    def update_channel_roles(self, channel_id: str, user_id: str, **kwargs) -> Any:
        """Update channel roles

        Path: /api/v4/channels/{channel_id}/members/{user_id}/roles
        Method: PUT
        """
        url = f"/api/v4/channels/{channel_id}/members/{user_id}/roles"
        return self.request("PUT", url, data=kwargs)

    def update_channel_member_scheme_roles(
        self, channel_id: str, user_id: str, **kwargs
    ) -> Any:
        """Update the scheme-derived roles of a channel member.

        Path: /api/v4/channels/{channel_id}/members/{user_id}/schemeRoles
        Method: PUT
        """
        url = f"/api/v4/channels/{channel_id}/members/{user_id}/schemeRoles"
        return self.request("PUT", url, data=kwargs)

    def update_channel_notify_props(
        self, channel_id: str, user_id: str, **kwargs
    ) -> Any:
        """Update channel notifications

        Path: /api/v4/channels/{channel_id}/members/{user_id}/notify_props
        Method: PUT
        """
        url = f"/api/v4/channels/{channel_id}/members/{user_id}/notify_props"
        return self.request("PUT", url, data=kwargs)

    def update_channel_member_autotranslation(
        self, channel_id: str, user_id: str, **kwargs
    ) -> Any:
        """Update channel member autotranslation setting

        Path: /api/v4/channels/{channel_id}/members/{user_id}/autotranslation
        Method: PUT
        """
        url = f"/api/v4/channels/{channel_id}/members/{user_id}/autotranslation"
        return self.request("PUT", url, data=kwargs)

    def mark_channels_read_for_user(self, user_id: str, **kwargs) -> Any:
        """Mark multiple channels as read

        Path: /api/v4/channels/members/{user_id}/mark_read
        Method: POST
        """
        url = f"/api/v4/channels/members/{user_id}/mark_read"
        return self.request("POST", url, data=kwargs)

    def get_channels_member_count(self, **kwargs) -> Any:
        """Get member counts for multiple channels

        Path: /api/v4/channels/stats/member_count
        Method: POST
        """
        url = "/api/v4/channels/stats/member_count"
        return self.request("POST", url, data=kwargs)

    def view_channel(self, user_id: str, **kwargs) -> Any:
        """View channel

        Path: /api/v4/channels/members/{user_id}/view
        Method: POST
        """
        url = f"/api/v4/channels/members/{user_id}/view"
        return self.request("POST", url, data=kwargs)

    def mark_all_direct_messages_read(self, user_id: str, **kwargs) -> Any:
        """Mark all direct and group messages as read

        Path: /api/v4/channels/members/{user_id}/direct/read
        Method: PUT
        """
        url = f"/api/v4/channels/members/{user_id}/direct/read"
        return self.request("PUT", url, data=kwargs)

    def get_channel_members_for_user(self, user_id: str, team_id: str, **kwargs) -> Any:
        """Get channel memberships and roles for a user

        Path: /api/v4/users/{user_id}/teams/{team_id}/channels/members
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/channels/members"
        return self.request("GET", url, params=kwargs)

    def get_channels_for_team_for_user(
        self, user_id: str, team_id: str, **kwargs
    ) -> Any:
        """Get channels for user

        Path: /api/v4/users/{user_id}/teams/{team_id}/channels
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/channels"
        return self.request("GET", url, params=kwargs)

    def get_channels_for_user(self, user_id: str, **kwargs) -> Any:
        """Get all channels from all teams

        Path: /api/v4/users/{user_id}/channels
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/channels"
        return self.request("GET", url, params=kwargs)

    def get_channel_unread(self, user_id: str, channel_id: str, **kwargs) -> Any:
        """Get unread messages

        Path: /api/v4/users/{user_id}/channels/{channel_id}/unread
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/channels/{channel_id}/unread"
        return self.request("GET", url, params=kwargs)

    def update_channel_scheme(self, channel_id: str, **kwargs) -> Any:
        """Set a channel's scheme

        Path: /api/v4/channels/{channel_id}/scheme
        Method: PUT
        """
        url = f"/api/v4/channels/{channel_id}/scheme"
        return self.request("PUT", url, data=kwargs)

    def channel_members_minus_group_members(self, channel_id: str, **kwargs) -> Any:
        """Channel members minus group members.

        Path: /api/v4/channels/{channel_id}/members_minus_group_members
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/members_minus_group_members"
        return self.request("GET", url, params=kwargs)

    def get_channel_member_counts_by_group(self, channel_id: str, **kwargs) -> Any:
        """Channel members counts for each group that has atleast one member in the channel

        Path: /api/v4/channels/{channel_id}/member_counts_by_group
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/member_counts_by_group"
        return self.request("GET", url, params=kwargs)

    def get_channel_moderations(self, channel_id: str, **kwargs) -> Any:
        """Get information about channel's moderation.

        Path: /api/v4/channels/{channel_id}/moderations
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/moderations"
        return self.request("GET", url, params=kwargs)

    def patch_channel_moderations(self, channel_id: str, **kwargs) -> Any:
        """Update a channel's moderation settings.

        Path: /api/v4/channels/{channel_id}/moderations/patch
        Method: PUT
        """
        url = f"/api/v4/channels/{channel_id}/moderations/patch"
        return self.request("PUT", url, data=kwargs)

    def get_sidebar_categories_for_team_for_user(
        self, user_id: str, team_id: str, **kwargs
    ) -> Any:
        """Get user's sidebar categories

        Path: /api/v4/users/{user_id}/teams/{team_id}/channels/categories
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories"
        return self.request("GET", url, params=kwargs)

    def create_sidebar_category_for_team_for_user(
        self, user_id: str, team_id: str, **kwargs
    ) -> Any:
        """Create user's sidebar category

        Path: /api/v4/users/{user_id}/teams/{team_id}/channels/categories
        Method: POST
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories"
        return self.request("POST", url, data=kwargs)

    def update_sidebar_categories_for_team_for_user(
        self, user_id: str, team_id: str, **kwargs
    ) -> Any:
        """Update user's sidebar categories

        Path: /api/v4/users/{user_id}/teams/{team_id}/channels/categories
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories"
        return self.request("PUT", url, data=kwargs)

    def get_sidebar_category_order_for_team_for_user(
        self, user_id: str, team_id: str, **kwargs
    ) -> Any:
        """Get user's sidebar category order

        Path: /api/v4/users/{user_id}/teams/{team_id}/channels/categories/order
        Method: GET
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories/order"
        return self.request("GET", url, params=kwargs)

    def update_sidebar_category_order_for_team_for_user(
        self, user_id: str, team_id: str, **kwargs
    ) -> Any:
        """Update user's sidebar category order

        Path: /api/v4/users/{user_id}/teams/{team_id}/channels/categories/order
        Method: PUT
        """
        url = f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories/order"
        return self.request("PUT", url, data=kwargs)

    def get_sidebar_category_for_team_for_user(
        self, user_id: str, team_id: str, category_id: str, **kwargs
    ) -> Any:
        """Get sidebar category

        Path: /api/v4/users/{user_id}/teams/{team_id}/channels/categories/{category_id}
        Method: GET
        """
        url = (
            f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories/{category_id}"
        )
        return self.request("GET", url, params=kwargs)

    def update_sidebar_category_for_team_for_user(
        self, user_id: str, team_id: str, category_id: str, **kwargs
    ) -> Any:
        """Update sidebar category

        Path: /api/v4/users/{user_id}/teams/{team_id}/channels/categories/{category_id}
        Method: PUT
        """
        url = (
            f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories/{category_id}"
        )
        return self.request("PUT", url, data=kwargs)

    def remove_sidebar_category_for_team_for_user(
        self, user_id: str, team_id: str, category_id: str, **kwargs
    ) -> Any:
        """Delete sidebar category

        Path: /api/v4/users/{user_id}/teams/{team_id}/channels/categories/{category_id}
        Method: DELETE
        """
        url = (
            f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories/{category_id}"
        )
        return self.request("DELETE", url, params=kwargs)

    def get_group_message_members_common_teams(self, channel_id: str, **kwargs) -> Any:
        """Get common teams for members of a Group Message.

        Path: /api/v4/channels/{channel_id}/common_teams
        Method: GET
        """
        url = f"/api/v4/channels/{channel_id}/common_teams"
        return self.request("GET", url, params=kwargs)

    def convert_group_message_to_channel(self, channel_id: str, **kwargs) -> Any:
        """Convert group message to private channel

        Path: /api/v4/channels/{channel_id}/convert_to_channel
        Method: POST
        """
        url = f"/api/v4/channels/{channel_id}/convert_to_channel"
        return self.request("POST", url, data=kwargs)
