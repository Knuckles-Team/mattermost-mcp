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


def register_kg_tools(mcp: FastMCP):
    """Register Mattermost native KG ingestion tools."""

    @mcp.tool(tags=["kg", "misc"])
    async def mattermost_ingest_teams(
        params_json: str = Field(
            default="{}",
            description="JSON string of get_all_teams filters (e.g. page, per_page).",
        ),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> dict:
        """Ingest Mattermost teams into epistemic-graph as typed :Team nodes."""
        import json

        from mattermost_mcp.kg_ingest import ingest_teams

        kwargs = {
            k: v for k, v in json.loads(params_json or "{}").items() if v is not None
        }
        if ctx:
            await ctx.info("Ingesting Mattermost teams...")
        teams = _records(client.get_all_teams(**kwargs))
        return {"listed": len(teams), "ingested": ingest_teams(teams)}

    @mcp.tool(tags=["kg", "misc"])
    async def mattermost_ingest_channels(
        team_id: str = Field(description="Team id whose channels to ingest."),
        params_json: str = Field(
            default="{}",
            description="JSON string of get_public_channels_for_team filters.",
        ),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> dict:
        """Ingest a team's channels as typed :Channel nodes (+ :inTeam links)."""
        import json

        from mattermost_mcp.kg_ingest import ingest_channels

        kwargs = {
            k: v for k, v in json.loads(params_json or "{}").items() if v is not None
        }
        if ctx:
            await ctx.info(f"Ingesting channels for team {team_id}...")
        channels = _records(client.get_public_channels_for_team(team_id, **kwargs))
        return {"listed": len(channels), "ingested": ingest_channels(channels)}

    @mcp.tool(tags=["kg", "misc"])
    async def mattermost_ingest_users(
        params_json: str = Field(
            default="{}",
            description="JSON string of get_users filters (e.g. page, per_page, in_team).",
        ),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> dict:
        """Ingest Mattermost users as shared :Person / :Bot nodes."""
        import json

        from mattermost_mcp.kg_ingest import ingest_users

        kwargs = {
            k: v for k, v in json.loads(params_json or "{}").items() if v is not None
        }
        if ctx:
            await ctx.info("Ingesting Mattermost users...")
        users = _records(client.get_users(**kwargs))
        return {"listed": len(users), "ingested": ingest_users(users)}

    @mcp.tool(tags=["kg", "misc"])
    async def mattermost_ingest_posts(
        channel_id: str = Field(description="Channel id whose posts to ingest."),
        params_json: str = Field(
            default="{}",
            description="JSON string of get_posts_for_channel filters (e.g. per_page, page).",
        ),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> dict:
        """Ingest a channel's messages as :Document nodes (+ channel/author links)."""
        import json

        from mattermost_mcp.kg_ingest import ingest_posts

        kwargs = {
            k: v for k, v in json.loads(params_json or "{}").items() if v is not None
        }
        if ctx:
            await ctx.info(f"Ingesting posts for channel {channel_id}...")
        posts = _records(client.get_posts_for_channel(channel_id, **kwargs))
        return {
            "listed": len(posts),
            "ingested": ingest_posts(posts, channel_id=channel_id),
        }

    return None
