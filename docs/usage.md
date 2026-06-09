# Usage — API / CLI / MCP

`mattermost-mcp` exposes the same capability three ways: as **MCP tools** an agent
calls, as a **Python API** (`Api`) you import, and as a **CLI**. The conceptual model
and the dynamic-facade architecture are described in [Overview](overview.md).

## As an MCP server

Once [deployed](deployment.md), the server registers FastMCP tools tagged under the
`MM` prefix, covering channels, teams, posts, users, bots, files, and the broader
administrative surface. The exposed set can be narrowed at runtime with
`--tools` / `--toolsets` (or the `MCP_ENABLED_TOOLS` / `MCP_ENABLED_TAGS` environment
variables) to keep the model's context window lean.

| Group | Example tools |
|---|---|
| Identity | `get_me`, `get_users`, `get_user` |
| Teams | `get_teams`, `get_team`, `get_team_members` |
| Channels | `get_channels`, `get_channel`, `create_channel` |
| Posts | `create_post`, `get_posts_for_channel`, `get_post` |

Example agent prompts that map onto these tools:

- *"Which teams is the bot a member of?"* → `get_teams`
- *"List the channels in team `<team_id>`"* → `get_channels`
- *"Post 'Deploy complete' to channel `<channel_id>`"* → `create_post`

## As a Python API

`Api` is a dynamic-facade client (`mattermost_mcp.api_client`) that composes the
per-domain Mattermost clients (channels, teams, posts, users, …) under one object.

```python
from mattermost_mcp.api_client import Api

api = Api(
    base_url="http://your-mattermost:8065",
    token="your_personal_access_token",
    verify=True,
)

# Reads
me = api.get_me()                       # the connected bot/user
teams = api.get_teams()                 # teams the bot belongs to
channels = api.get_channels(teams[0]["id"])
```

Build a client straight from the environment:

```python
from mattermost_mcp.auth import get_client
api = get_client()        # reads MATTERMOST_URL / MATTERMOST_TOKEN from the environment / .env
```

### Writes

```python
post = api.create_post(
    channel_id="<channel_id>",
    message="Deploy complete",
)
```

## As a CLI

The MCP server is itself the primary command-line entry point:

```bash
# stdio MCP server (default transport)
mattermost-mcp

# network MCP server
mattermost-mcp --transport streamable-http --host 0.0.0.0 --port 8000

# inspect available flags (transport, host, port, tool filtering)
mattermost-mcp --help
```

The companion agent is exposed as `mattermost-agent`:

```bash
mattermost-agent --mcp-url http://localhost:8000/mcp --host 0.0.0.0 --port 9035 --web
```

See [Deployment](deployment.md) for the agent server, Docker Compose, reverse proxy,
and DNS.
