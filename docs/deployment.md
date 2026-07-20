# Deployment

<!-- BEGIN GENERATED: deployment-options -->
## Deployment Options

`mattermost-mcp` supports local stdio, a loopback-only development listener, a
least-privilege stdio container, and a remote authenticated HTTPS boundary.
Provider endpoint, credential, selector, identity, and trust material are supplied
at runtime through `AgentConfig`; none is stored in this repository.

### Installed stdio process

```json
{
  "mcpServers": {
    "mattermost": {
      "command": "mattermost-mcp",
      "args": [],
      "env": {"MCP_TOOL_MODE": "intent"}
    }
  }
}
```

### Loopback development listener

```bash
mattermost-mcp --transport streamable-http --host 127.0.0.1 --port 8000
```

Do not expose this listener beyond loopback. Network deployments require direct TLS
or an explicitly trusted TLS-terminating ingress, configured authentication, exact
`MCP_ALLOWED_HOSTS`, and an exact trusted-proxy CIDR policy.

### Least-privilege local container

```bash
docker run -i --rm \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=256 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  -e TRANSPORT=stdio \
  registry.example.invalid/mattermost-mcp@sha256:<digest> mattermost-mcp
```

The operator projects the selected AgentConfig profile into the process at runtime;
the image remains immutable and contains no environment connection profile.

### Remote authenticated HTTPS endpoint

```json
{
  "mcpServers": {
    "mattermost": {"url": "https://service.example.invalid/mcp"}
  }
}
```

Store the real remote URL, outbound identity reference, and TLS-profile reference in
`AgentConfig`, not in MCP client JSON or documentation.
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
    image: example/mattermost-mcp@sha256:<digest>
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
    image: example/mattermost-mcp@sha256:<digest>
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
    image: example/mattermost-mcp@sha256:<digest>
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
# Internal (self-signed) — homelab .example.invalid zone
mattermost-mcp.example.invalid {
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
curl -s "http://technitium.example.invalid:5380/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=mattermost-mcp.example.invalid" \
  --data-urlencode "zone=arpa" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=192.0.2.10" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `mattermost-mcp.example.invalid → <caddy-host-ip>` in the Technitium web
console (`http://technitium.example.invalid:5380`). The ecosystem
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

For a remote HTTP server, point the client at `http://mattermost-mcp.example.invalid/mcp` instead.
