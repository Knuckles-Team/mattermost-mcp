# Backing Platform — Mattermost

`mattermost-mcp` is a **client** of a Mattermost server. This page provides a Docker
recipe for deploying one locally to serve as the target of `MATTERMOST_URL`. For
production topologies, follow the upstream
[Mattermost documentation](https://docs.mattermost.com/).

!!! note "Backing-system recipe"
    Each connector in the ecosystem follows the same convention — a
    `docs/platform.md` recipe for the system it integrates with, accompanied by a
    sample Compose stack that mirrors [`services/`](https://github.com/Knuckles-Team).
    Systems offered only as a managed service have no local recipe.

## Single-node deployment (Compose)

Mattermost publishes the `mattermost/mattermost-team-edition` image. The following
stack runs the server with a PostgreSQL backend and publishes the web/API on `:8065`:

```yaml
# docker/mattermost-platform.compose.yml
services:
  mattermost:
    image: mattermost/mattermost-team-edition:latest
    container_name: mattermost
    hostname: mattermost
    restart: unless-stopped
    depends_on:
      - mattermost-db
    ports:
      - "8065:8065"            # web UI and v4 REST API
    environment:
      - MM_SERVICESETTINGS_SITEURL=http://localhost:8065
      - MM_SQLSETTINGS_DRIVERNAME=postgres
      - MM_SQLSETTINGS_DATASOURCE=postgres://mmuser:mmuser_password@mattermost-db:5432/mattermost?sslmode=disable
    volumes:
      - mattermost_config:/mattermost/config
      - mattermost_data:/mattermost/data

  mattermost-db:
    image: postgres:16-alpine
    container_name: mattermost-db
    hostname: mattermost-db
    restart: unless-stopped
    environment:
      - POSTGRES_DB=mattermost
      - POSTGRES_USER=mmuser
      - POSTGRES_PASSWORD=mmuser_password
    volumes:
      - mattermost_db:/var/lib/postgresql/data

volumes:
  mattermost_config:
  mattermost_data:
  mattermost_db:
```

```bash
docker compose -f docker/mattermost-platform.compose.yml up -d

# Wait for the server to answer
curl -s http://localhost:8065/api/v4/system/ping        # {"status":"OK"}
```

After first boot, create the initial admin account in the web UI
(`http://localhost:8065`), then generate a **Personal Access Token** (or a **Bot**
token) to use as `MATTERMOST_TOKEN`.

## Connect mattermost-mcp

```bash
export MATTERMOST_URL=http://localhost:8065
export MATTERMOST_TOKEN=your_personal_access_token

mattermost-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

## Combined deployment

A combined stack places Mattermost, its database, and the MCP server on one Docker
network, so the server reaches Mattermost by container name:

```yaml
# docker/stack.compose.yml
services:
  mattermost-db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_DB=mattermost
      - POSTGRES_USER=mmuser
      - POSTGRES_PASSWORD=mmuser_password
    volumes: ["mattermost_db:/var/lib/postgresql/data"]

  mattermost:
    image: mattermost/mattermost-team-edition:latest
    depends_on: [mattermost-db]
    ports: ["8065:8065"]
    environment:
      - MM_SERVICESETTINGS_SITEURL=http://localhost:8065
      - MM_SQLSETTINGS_DRIVERNAME=postgres
      - MM_SQLSETTINGS_DATASOURCE=postgres://mmuser:mmuser_password@mattermost-db:5432/mattermost?sslmode=disable
    volumes: ["mattermost_config:/mattermost/config", "mattermost_data:/mattermost/data"]

  mattermost-mcp:
    image: knucklessg1/mattermost-mcp:latest
    depends_on: [mattermost]
    environment:
      - MATTERMOST_URL=http://mattermost:8065
      - MATTERMOST_TOKEN=${MATTERMOST_TOKEN}
      - TRANSPORT=streamable-http
      - HOST=0.0.0.0
      - PORT=8000
    ports: ["8000:8000"]

volumes:
  mattermost_config:
  mattermost_data:
  mattermost_db:
```

```bash
docker compose -f docker/stack.compose.yml up -d
```
