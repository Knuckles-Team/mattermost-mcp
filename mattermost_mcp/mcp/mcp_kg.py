"""Native knowledge-graph ingestion MCP tools for mattermost-mcp (Wire-First).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. These tools list Mattermost objects via
the real client and push them into the ONE epistemic-graph engine as typed nodes / message
documents (:mod:`mattermost_mcp.kg_ingest`) and file-attachment blobs
(:mod:`mattermost_mcp.kg_media`). Best-effort: when no engine is reachable the ingest legs
no-op and the tool returns ``{"ingested": None}``.
"""

from typing import Any

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def _records(res: Any) -> list[dict[str, Any]]:
    """Normalise a client response into a list of plain dicts."""
    data = getattr(res, "data", res)
    if isinstance(data, dict):
        # e.g. get_posts_for_channel -> {"order":[...], "posts":{id: post}}
        if "posts" in data and isinstance(data["posts"], dict):
            data = list(data["posts"].values())
        else:
            data = [data]
    if not isinstance(data, list):
        return []
    out: list[dict[str, Any]] = []
    for r in data:
        if r is None:
            continue
        out.append(r.model_dump() if hasattr(r, "model_dump") else r)
    return out


def _filters(**values: Any) -> dict[str, Any]:
    return {k: v for k, v in values.items() if v is not None}


def register_kg_tools(mcp: FastMCP):
    """Register Mattermost native KG ingestion tools (typed list filters)."""

    @mcp.tool(tags=["kg", "misc"])
    async def mattermost_ingest_teams(
        page: int | None = Field(default=None, description="Page to list (0-based)."),
        per_page: int | None = Field(default=None, description="Teams per page."),
        include_total_count: bool | None = Field(default=None),
        exclude_policy_constrained: bool | None = Field(default=None),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> dict:
        """Ingest Mattermost teams into epistemic-graph as typed :Team nodes."""
        from mattermost_mcp.kg_ingest import ingest_teams

        if ctx:
            await ctx.info("Ingesting Mattermost teams...")
        teams = _records(
            client.get_all_teams(
                **_filters(
                    page=page,
                    per_page=per_page,
                    include_total_count=include_total_count,
                    exclude_policy_constrained=exclude_policy_constrained,
                )
            )
        )
        return {"listed": len(teams), "ingested": await ingest_teams(teams)}

    @mcp.tool(tags=["kg", "misc"])
    async def mattermost_ingest_channels(
        team_id: str = Field(description="Team id whose channels to ingest."),
        page: int | None = Field(default=None, description="Page to list (0-based)."),
        per_page: int | None = Field(default=None, description="Channels per page."),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> dict:
        """Ingest a team's channels as typed :Channel nodes (+ :inTeam links)."""
        from mattermost_mcp.kg_ingest import ingest_channels

        if ctx:
            await ctx.info(f"Ingesting channels for team {team_id}...")
        channels = _records(
            client.get_public_channels_for_team(
                team_id, **_filters(page=page, per_page=per_page)
            )
        )
        return {"listed": len(channels), "ingested": await ingest_channels(channels)}

    @mcp.tool(tags=["kg", "misc"])
    async def mattermost_ingest_users(
        page: int | None = Field(default=None, description="Page to list (0-based)."),
        per_page: int | None = Field(default=None, description="Users per page."),
        in_team: str | None = Field(
            default=None, description="Only users in this team id."
        ),
        not_in_team: str | None = Field(default=None),
        in_channel: str | None = Field(
            default=None, description="Only users in this channel id."
        ),
        not_in_channel: str | None = Field(default=None),
        in_group: str | None = Field(default=None),
        without_team: bool | None = Field(default=None),
        active: bool | None = Field(default=None),
        inactive: bool | None = Field(default=None),
        role: str | None = Field(
            default=None, description="Only users with this system role."
        ),
        sort: str | None = Field(
            default=None, description="Sort order, e.g. last_activity_at."
        ),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> dict:
        """Ingest Mattermost users as shared :Person / :Bot nodes."""
        from mattermost_mcp.kg_ingest import ingest_users

        if ctx:
            await ctx.info("Ingesting Mattermost users...")
        users = _records(
            client.get_users(
                **_filters(
                    page=page,
                    per_page=per_page,
                    in_team=in_team,
                    not_in_team=not_in_team,
                    in_channel=in_channel,
                    not_in_channel=not_in_channel,
                    in_group=in_group,
                    without_team=without_team,
                    active=active,
                    inactive=inactive,
                    role=role,
                    sort=sort,
                )
            )
        )
        return {"listed": len(users), "ingested": await ingest_users(users)}

    @mcp.tool(tags=["kg", "misc"])
    async def mattermost_ingest_posts(
        channel_id: str = Field(description="Channel id whose posts to ingest."),
        page: int | None = Field(default=None, description="Page to list (0-based)."),
        per_page: int | None = Field(default=None, description="Posts per page."),
        since: int | None = Field(
            default=None, description="Only posts modified since this Unix time (ms)."
        ),
        before: str | None = Field(
            default=None, description="Posts before this post id."
        ),
        after: str | None = Field(
            default=None, description="Posts after this post id."
        ),
        include_deleted: bool | None = Field(default=None),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> dict:
        """Ingest a channel's messages as :Document nodes (+ channel/author links)."""
        from mattermost_mcp.kg_ingest import ingest_posts

        if ctx:
            await ctx.info(f"Ingesting posts for channel {channel_id}...")
        posts = _records(
            client.get_posts_for_channel(
                channel_id,
                **_filters(
                    page=page,
                    per_page=per_page,
                    since=since,
                    before=before,
                    after=after,
                    include_deleted=include_deleted,
                ),
            )
        )
        return {
            "listed": len(posts),
            "ingested": await ingest_posts(posts, channel_id=channel_id),
        }

    return None
