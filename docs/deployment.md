# Deployment

<!-- BEGIN GENERATED: deployment-options -->
## Deployment Options

`mattermost-mcp` exposes its MCP server (console script `mattermost-mcp`) four ways. Pick the row that
matches where the server runs relative to your MCP client, then copy the matching
`mcp_config.json` below. Replace the `<your-…>` placeholders with the values from the **Configuration / Environment Variables** section.

| # | Option | Transport | Where it runs | `mcp_config.json` key |
|---|--------|-----------|---------------|------------------------|
| 1 | stdio | `stdio` | client launches a subprocess | `command` |
| 2 | Streamable-HTTP (local) | `streamable-http` | a local network port | `command` or `url` |
| 3 | Local container / uv | `stdio` or `streamable-http` | Docker / Podman / uv on this host | `command` or `url` |
| 4 | Remote URL | `streamable-http` | a remote host behind Caddy | `url` |

### 1. stdio (local subprocess)

The client launches the server over stdio via `uvx` — best for local IDEs
(Cursor, Claude Desktop, VS Code):

```json
{
  "mcpServers": {
    "mattermost-mcp": {
      "command": "uvx",
      "args": ["--from", "mattermost-mcp", "mattermost-mcp"],
      "env": {
        "MATTERMOST_URL": "<your-mattermost_url>",
        "MATTERMOST_TOKEN": "<your-mattermost_token>"
      }
    }
  }
}
```

### 2. Streamable-HTTP (local process)

Run the server as a long-lived HTTP process:

```bash
uvx --from mattermost-mcp mattermost-mcp --transport streamable-http --host 0.0.0.0 --port 8000
curl -s http://localhost:8000/health        # {"status":"OK"}
```

Then either let the client launch it:

```json
{
  "mcpServers": {
    "mattermost-mcp": {
      "command": "uvx",
      "args": ["--from", "mattermost-mcp", "mattermost-mcp", "--transport", "streamable-http", "--port", "8000"],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "MATTERMOST_URL": "<your-mattermost_url>",
        "MATTERMOST_TOKEN": "<your-mattermost_token>"
      }
    }
  }
}
```

…or connect to the already-running process by URL:

```json
{
  "mcpServers": {
    "mattermost-mcp": { "url": "http://localhost:8000/mcp" }
  }
}
```

### 3. Local container / uv

**(a) Launch a container directly from `mcp_config.json`** (stdio over the container —
no ports to manage). Swap `docker` for `podman` for a daemonless runtime:

```json
{
  "mcpServers": {
    "mattermost-mcp": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "TRANSPORT=stdio",
        "-e", "MATTERMOST_URL=<your-mattermost_url>",
        "-e", "MATTERMOST_TOKEN=<your-mattermost_token>",
        "knucklessg1/mattermost-mcp:latest"
      ]
    }
  }
}
```

**(b) Run a local streamable-http container, then connect by URL:**

```bash
docker run -d --name mattermost-mcp -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e PORT=8000 \
  -e MATTERMOST_URL="<your-mattermost_url>" \
  -e MATTERMOST_TOKEN="<your-mattermost_token>" \
  knucklessg1/mattermost-mcp:latest
# or, from a clone of this repo:
docker compose -f docker/mcp.compose.yml up -d
```

```json
{
  "mcpServers": {
    "mattermost-mcp": { "url": "http://localhost:8000/mcp" }
  }
}
```

**(c) From a local checkout with `uv`:**

```bash
uv run mattermost-mcp --transport streamable-http --port 8000
```

### 4. Remote URL (deployed behind Caddy)

When the server is deployed remotely (e.g. as a Docker service) and published through
Caddy on the internal `*.arpa` zone, connect with the `"url"` key — no local process or
image required:

```json
{
  "mcpServers": {
    "mattermost-mcp": { "url": "http://mattermost-mcp.arpa/mcp" }
  }
}
```

Caddy reverse-proxies `http://mattermost-mcp.arpa` to the container's `:8000`
streamable-http listener; `http://mattermost-mcp.arpa/health` returns
`{"status":"OK"}` when the service is live.
<!-- END GENERATED: deployment-options -->

This page covers running `mattermost-mcp` as a long-lived server: the transports, a
Docker Compose stack, the companion agent server, putting it behind a Caddy reverse
proxy, and giving it a DNS name with Technitium. To provision the **Mattermost server**
it connects to, see [Backing Platform](platform.md).

> `mattermost-mcp` ships both an **MCP server** (console script `mattermost-mcp`) and a
> **Pydantic-AI agent server** (console script `mattermost-agent`). The MCP server is a
> typed, deterministic tool surface a policy router / agent calls; the agent server
> consumes that tool surface and can serve a conversational web UI.

## Run the MCP server

The transport is selected with `--transport` (or the `TRANSPORT` env var):

=== "stdio (default)"

    ```bash
    mattermost-mcp
    ```
    For IDE / desktop MCP clients that launch the server as a subprocess.

=== "streamable-http"

    ```bash
    mattermost-mcp --transport streamable-http --host 0.0.0.0 --port 8000
    ```
    A network server with a `/health` endpoint and `/mcp` route.

=== "sse"

    ```bash
    mattermost-mcp --transport sse --host 0.0.0.0 --port 8000
    ```

Health check (HTTP transports):

```bash
curl -s http://localhost:8000/health        # {"status":"OK"}
```

## Configuration (environment)

`mattermost-mcp` is configured entirely from the environment. The **required** set:

| Var | Default | Meaning |
|---|---|---|
| `MATTERMOST_URL` | `http://localhost:8065` | Mattermost Server v4 API endpoint URL |
| `MATTERMOST_TOKEN` | _(none)_ | Personal Access Token or Bot Token |

Plus `HOST` / `PORT` / `TRANSPORT` for HTTP transports. The full template, ready to
copy to `.env`, is documented in
[`.env.example`](https://github.com/Knuckles-Team/mattermost-mcp/blob/main/.env.example).
The connector remains inactive when `MATTERMOST_TOKEN` is absent.

## Docker Compose

The repo ships [`docker/mcp.compose.yml`](https://github.com/Knuckles-Team/mattermost-mcp/blob/main/docker/mcp.compose.yml).
It reads a sibling `.env` and publishes the HTTP server on `:8000`:

```yaml
services:
  mattermost-mcp:
    image: knucklessg1/mattermost-mcp:latest
    container_name: mattermost-mcp
    hostname: mattermost-mcp
    restart: always
    env_file:
      - ../.env
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
      - MATTERMOST_URL
      - MATTERMOST_TOKEN
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
```

```bash
cp .env.example .env          # then edit MATTERMOST_* values
docker compose -f docker/mcp.compose.yml up -d
docker compose -f docker/mcp.compose.yml logs -f
```

## Agent server

`mattermost-mcp` also ships a Pydantic-AI agent (console script `mattermost-agent`)
that connects to the running MCP server over HTTP and optionally serves a web UI. The
repo provides [`docker/agent.compose.yml`](https://github.com/Knuckles-Team/mattermost-mcp/blob/main/docker/agent.compose.yml),
which runs the MCP server and the agent together: the agent reaches the MCP server by
container name via `MCP_URL` and publishes its own web UI on `:9035`.

```yaml
services:
  mattermost-mcp-mcp:
    image: knucklessg1/mattermost-mcp:latest
    container_name: mattermost-mcp-mcp
    hostname: mattermost-mcp-mcp
    restart: always
    env_file:
      - ../.env
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports:
      - "8000:8000"

  mattermost-mcp-agent:
    image: knucklessg1/mattermost-mcp:latest
    container_name: mattermost-mcp-agent
    hostname: mattermost-mcp-agent
    restart: always
    depends_on:
      - mattermost-mcp-mcp
    env_file:
      - ../.env
    command: [ "mattermost-agent" ]
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=9035
      - MCP_URL=http://mattermost-mcp-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
    ports:
      - "9035:9035"
```

```bash
docker compose -f docker/agent.compose.yml up -d
curl -s http://localhost:9035/health        # agent health
```

Run the agent directly against an existing MCP server:

```bash
mattermost-agent --mcp-url http://localhost:8000/mcp --host 0.0.0.0 --port 9035 --web
```

## Behind a Caddy reverse proxy

Expose the HTTP server on a hostname with automatic TLS. Add to your `Caddyfile`:

```caddy
# Internal (self-signed) — homelab .arpa zone
mattermost-mcp.arpa {
    tls internal
    reverse_proxy mattermost-mcp:8000
}
```

```caddy
# Public — automatic Let's Encrypt
mattermost-mcp.example.com {
    reverse_proxy mattermost-mcp:8000
}
```

Reload Caddy:

```bash
docker compose -f services/caddy/compose.yml exec caddy caddy reload --config /etc/caddy/Caddyfile
```

## DNS with Technitium

Point the hostname at the host running Caddy. Via the Technitium API:

```bash
curl -s "http://technitium.arpa:5380/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=mattermost-mcp.arpa" \
  --data-urlencode "zone=arpa" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=10.0.0.10" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `mattermost-mcp.arpa → <caddy-host-ip>` in the Technitium web
console (`http://technitium.arpa:5380`). The ecosystem
[`technitium-dns-mcp`](https://knuckles-team.github.io/technitium-dns-mcp/) automates
this as a tool.

## Register with an MCP client

Add to your client's `mcp_config.json` (multiplexer nickname `mm`):

```json
{
  "mcpServers": {
    "mattermost-mcp": {
      "command": "uv",
      "args": ["run", "mattermost-mcp"],
      "env": {
        "MATTERMOST_URL": "http://your-mattermost:8065",
        "MATTERMOST_TOKEN": "your_personal_access_token"
      }
    }
  }
}
```

For a remote HTTP server, point the client at `http://mattermost-mcp.arpa/mcp` instead.
