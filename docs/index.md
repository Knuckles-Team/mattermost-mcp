# mattermost-mcp

Mattermost team-collaboration **API + MCP Server** for the agent-utilities ecosystem
— a typed, deterministic tool surface and Pydantic-AI agent over the Mattermost
Server v4 REST API.

!!! info "Official documentation"
    This site is the canonical reference for `mattermost-mcp`, maintained alongside
    every release.

[![PyPI](https://img.shields.io/pypi/v/mattermost-mcp)](https://pypi.org/project/mattermost-mcp/)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
[![License](https://img.shields.io/pypi/l/mattermost-mcp)](https://github.com/Knuckles-Team/mattermost-mcp/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/source-GitHub-181717?logo=github)](https://github.com/Knuckles-Team/mattermost-mcp)

## Overview

`mattermost-mcp` wraps the Mattermost Server v4 REST API with a dynamic-facade client
and exposes it as both an MCP server and an optional Pydantic-AI agent. It provides:

- **`Api`** — a multi-inheritance REST facade (`mattermost_mcp.api_client`) covering
  channels, teams, posts, users, bots, files, and the full administrative surface.
- **A broad MCP tool set** — FastMCP tools tagged under the `MM` prefix, with runtime
  toolset selection and visibility filtering to keep the model's context window lean.
- **A Pydantic-AI agent** (`mattermost-agent`) that consumes the MCP server and can
  serve a web UI for conversational operations.

The package connects to Mattermost when credentials are supplied and remains inactive
when those credentials are absent.

## Explore the documentation

<div class="grid cards" markdown>

- :material-rocket-launch: **[Installation](installation.md)** — pip, source, extras, and the prebuilt Docker image.
- :material-server-network: **[Deployment](deployment.md)** — run the MCP server and agent, Docker Compose, Caddy + Technitium.
- :material-console: **[Usage](usage.md)** — the MCP tools, the `Api` client, and the CLI.
- :material-database-cog: **[Backing Platform](platform.md)** — deploy Mattermost with Docker.
- :material-sitemap: **[Architecture](architecture.md)** — dynamic facade, FastMCP, agent server.
- :material-tag-multiple: **[Concepts](concepts.md)** — the `CONCEPT:MM-*` registry.

</div>

## Quick start

```bash
pip install "mattermost-mcp[mcp]"
mattermost-mcp                   # stdio MCP server (default transport)
```

Connect it to a Mattermost server:

```bash
export MATTERMOST_URL=http://your-mattermost:8065
export MATTERMOST_TOKEN=your_personal_access_token
mattermost-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

See **[Installation](installation.md)** and **[Deployment](deployment.md)** for the
full matrix (PyPI extras, Docker image, all transports, the agent server, reverse
proxy, DNS).
