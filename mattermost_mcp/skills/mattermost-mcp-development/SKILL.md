---
name: mattermost-mcp-development
skill_type: skill
domain: development
description: >-
  Develop, test, gate, and release the mattermost-mcp connector. Use this
  skill when changing the connector's API mappings, MCP tools, packaging,
  documentation, or repository gates.
license: MIT
tags: [mattermost-mcp, development, connector, test, gates]
tier: repository
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---

# mattermost-mcp development

This repository owns the Mattermost transport, mappings, MCP tools, and
agent entry points. Shared connector contracts and transports belong to
`scion-sdk`; admission, serving, and durable graph state belong to
their owning repositories. Read `AGENTS.md` before changing code and keep
provider credentials and endpoints out of source, logs, and skill content.

## Steps

1. Find the owning spec row with `git grep -n "<term>" -- specs` and verify a requirement row exists before any code changes.
2. Create the environment with `uv sync --locked` and verify the command exits with status 0.
3. Make the change in the connector only, reusing the existing SDK clients, and verify with `git diff --stat` that only intended paths changed.
4. Run the focused tests with `uv run --all-extras pytest tests/test_mcp_server.py -q` and verify they pass.
5. Run the repository gate with `uvx pre-commit run --all-files` and verify every hook reports Passed.

## Failure recovery

| Failure | Cause | Recovery |
|---|---|---|
| A pre-commit hook fails | The change violates a shared connector-standard, secrets, spec or tests-fast check | Read the hook output, fix the reported file, stage the exact path with `git add -- <path>` and commit again without bypassing hooks |
| `uv sync --locked` fails | uv.lock is out of date with pyproject.toml | Run `uv lock` to refresh the lockfile and commit both files together |
| No spec row matches the change | The requirement is not yet written down | Extend the nearest row in `specs/` first, then cite its id in the `Spec:` trailer |

## Rapid delivery: the 5-minute contract

Specs are already designed. Deliver small, reviewable slices and cite the
owning spec row in the commit trailer.

- Find the owning row first with `git grep -n "<term>" -- specs` and extend
  that spec before adding new requirement text.
- Reuse existing SDK clients, transport policies, and tool factories. Do not
  create a second implementation of a connector capability.
- Keep changes scoped to this connector. A change owned by the SDK, Arbora,
  or the knowledge graph belongs in that repository instead.
- Every delivered requirement needs a bound test. Generated `status.json`
  files are produced by `pipelines-hook spec-status`; never hand-edit them.
- One logical change per commit, with `Spec: <ID>` and the assisting agent
  trailer adjacent in the final paragraph.

## Setup and gates

Use the pinned environment from `uv sync --locked`. Run the repository
gate from the checkout root:

```bash
uvx pre-commit run --all-files
```

For focused feedback, run the relevant tests with the repository's pinned
environment, for example:

```bash
uv run --all-extras pytest tests/test_mcp_server.py -q
uv run --all-extras pytest tests/test_api_client.py -q
```

The canonical `.pre-commit-config.yaml` delegates connector-standard,
secrets, spec, and tests-fast checks to `Knuckles-Team/pipelines` at
`rev: main`. Do not replace those shared hooks with local copies or bypass
a failing check.

## Connector-specific checks

- Keep the MCP and agent surfaces aligned with `scion-sdk`.
- Validate environment and TLS settings before making provider calls.
- Mock external Mattermost calls in tests; never use live credentials in a
  local gate.
- Keep `mattermost_mcp/skills/` package data intact when adding skills.
- Documentation lives under `docs/` and is published by the shared Pages
  workflow; source status records live under `specs/`.

## Delivery discipline

Work in a real Git worktree based on `origin/main`. Inspect the complete diff,
stage only reviewed paths, and verify `git status --short` after every gate.
Do not use `git stash`, `git add -A`, or `git add .`; do not claim Pages
publication until a successful exact-source workflow run and the public page
are both observed.
