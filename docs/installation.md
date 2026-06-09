# Installation

`mattermost-mcp` is a standard Python package and a prebuilt container image. Pick the
path that matches how you want to run it.

## Requirements

- **Python 3.11 – 3.14**.
- A reachable **Mattermost server** (v4 REST API) — see [Backing Platform](platform.md)
  to deploy one locally.

## From PyPI (recommended)

```bash
pip install mattermost-mcp
```

### Optional extras

The base install is intentionally minimal. Install the extra for what you need:

| Extra | Install | Pulls in |
|---|---|---|
| `mcp` | `pip install "mattermost-mcp[mcp]"` | FastMCP MCP-server runtime (`agent-utilities[mcp]`) |
| `agent` | `pip install "mattermost-mcp[agent]"` | Pydantic-AI agent + Logfire tracing |
| `all` | `pip install "mattermost-mcp[all]"` | The MCP server and the agent together |
| `test` | `pip install "mattermost-mcp[test]"` | `pytest`, `pytest-asyncio`, `pytest-cov`, `pytest-xdist` |

```bash
# Typical: run the MCP server and the agent
pip install "mattermost-mcp[all]"
```

## From source

```bash
git clone https://github.com/Knuckles-Team/mattermost-mcp.git
cd mattermost-mcp
pip install -e ".[all]"          # editable install with the MCP server and agent
```

With [`uv`](https://docs.astral.sh/uv/):

```bash
uv pip install -e ".[all]"
uv run mattermost-mcp
```

## Prebuilt Docker image

A multi-stage, slim image is published on every release (installs
`mattermost-mcp[all]`, entrypoint `mattermost-mcp`):

```bash
docker pull knucklessg1/mattermost-mcp:latest

docker run --rm -i \
  -e MATTERMOST_URL=http://your-mattermost:8065 \
  -e MATTERMOST_TOKEN=your_personal_access_token \
  knucklessg1/mattermost-mcp:latest        # stdio transport (default)
```

For an HTTP server with a published port, and for the agent server, see
[Deployment](deployment.md).

## Verify the install

```bash
mattermost-mcp --help
python -c "import mattermost_mcp; print(mattermost_mcp.__version__)"
```

## Next steps

- **[Deployment](deployment.md)** — run it as a long-lived MCP server and agent behind Caddy + DNS.
- **[Usage](usage.md)** — call the tools, the API, and the CLI.
- **[Configuration](deployment.md#configuration-environment)** — every environment variable.
