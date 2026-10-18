"""Build mattermost_mcp/operation_manifest.json from the Mattermost OpenAPI source.

Usage:
    MATTERMOST_OPENAPI_SOURCE=<mattermost>/api/v4/source python scripts/build_operation_manifest.py

The source is the official Mattermost API v4 OpenAPI source (mattermost/mattermost
``api/v4/source``, published at api.mattermost.com) at the tag matching the deployed
server; SOURCE_VERSION below records which one generated the committed files.

One entry per OpenAPI operation, keyed by the generated client method name, with
its path and query parameters and the top-level properties of a JSON object
request body (sent as the body's own fields, matching the client's
``data=kwargs``). agent-connector-sdk types each operation tool from it.
"""

from __future__ import annotations

import json
import keyword
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "mattermost_mcp" / "operation_manifest.json"
EXCLUDED = {"definitions.yaml", "introduction.yaml"}
METHODS = ("get", "post", "put", "delete", "patch")
SOURCE_VERSION = "mattermost/mattermost v11.11.1 api/v4/source"
JSON_TYPES = {"string", "integer", "number", "boolean", "array", "object"}


def camel_to_snake(name: str) -> str:
    name = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
    name = re.sub(r"[^a-z0-9_]", "_", name)
    return re.sub(r"_+", "_", name).strip("_")


def func_name(method: str, path: str, op_id: str | None) -> str:
    """Identical to generate_mattermost_mcp.make_func_name."""
    if op_id:
        return camel_to_snake(op_id)
    clean = path.replace("/api/v4", "")
    clean = re.sub(r"\{([a-zA-Z0-9_]+)\}", r"by_\1", clean)
    clean = re.sub(r"[^a-zA-Z0-9_]", "_", clean)
    clean = re.sub(r"_+", "_", clean).strip("_")
    return f"{method.lower()}_{clean.lower()}"


def resolve(node: object, definitions: dict) -> dict:
    """Follow a local ``#/components/schemas/<Name>`` reference once."""
    seen = 0
    while isinstance(node, dict) and "$ref" in node and seen < 8:
        name = str(node["$ref"]).rsplit("/", 1)[-1]
        node = definitions.get(name, {})
        seen += 1
    return node if isinstance(node, dict) else {}


def usable(name: object) -> bool:
    """A wire name a typed keyword argument can carry (directly or via an alias)."""
    return str(name).isidentifier()


def python_name(name: str) -> str:
    """The keyword-argument name for a wire field.

    A Python keyword (``from``, ``in``...) cannot be a parameter name, so it is
    exposed as ``<name>_`` and aliased back to the wire name: the client's
    ``ApiClientBase.request`` restores ``from_`` to ``from`` before sending.
    """
    return f"{name}_" if keyword.iskeyword(name) else name


def schema_type(schema: dict) -> dict:
    declared = schema.get("type")
    return {"type": declared} if declared in JSON_TYPES else {}


def body_parameters(operation: dict, definitions: dict, taken: set[str]) -> list[dict]:
    content = (operation.get("requestBody") or {}).get("content") or {}
    media = (
        content.get("application/json") or next(iter(content.values()), {})
        if content
        else {}
    )
    schema = resolve((media or {}).get("schema") or {}, definitions)
    required = set(schema.get("required") or [])
    out = []
    for name, prop in (schema.get("properties") or {}).items():
        if not usable(name) or name in taken:
            continue
        out.append(
            {
                "name": name,
                "python_name": python_name(name),
                "in": "body",
                "required": name in required,
                "schema": schema_type(resolve(prop, definitions)),
            }
        )
    return out


def main() -> int:
    source = os.environ.get("MATTERMOST_OPENAPI_SOURCE")
    if not source:
        print(
            "MATTERMOST_OPENAPI_SOURCE must reference the OpenAPI source",
            file=sys.stderr,
        )
        return 2
    source_dir = Path(source)
    definitions_doc = (
        yaml.safe_load((source_dir / "definitions.yaml").read_text()) or {}
    )
    definitions = ((definitions_doc.get("components") or {}).get("schemas")) or {}
    entries: dict[str, dict] = {}
    for spec in sorted(source_dir.glob("*.y*ml")):
        if spec.name in EXCLUDED:
            continue
        content = yaml.safe_load(spec.read_text()) or {}
        for path, item in content.items():
            if not str(path).startswith("/") or not isinstance(item, dict):
                continue
            shared = item.get("parameters") or []
            for method in METHODS:
                operation = item.get(method)
                if not isinstance(operation, dict):
                    continue
                name = func_name(method, path, operation.get("operationId"))
                if name in entries:
                    # Mattermost reuses an operationId for the team-scoped variant
                    # (SearchFiles); the client names that one <verb>_team_<rest>.
                    verb, _, rest = name.partition("_")
                    team_name = f"{verb}_team_{rest}"
                    if "{team_id}" in entries[name]["path"]:
                        entries[team_name] = {
                            **entries.pop(name),
                            "method": team_name,
                            "name": team_name,
                        }
                    elif "{team_id}" in path:
                        name = team_name
                params = []
                taken: set[str] = set()
                for raw in [*shared, *(operation.get("parameters") or [])]:
                    param = resolve(raw, definitions) if "$ref" in raw else raw
                    pname = param.get("name")
                    where = param.get("in")
                    if (
                        not pname
                        or where not in {"path", "query"}
                        or not usable(pname)
                        or pname in taken
                    ):
                        continue
                    taken.add(pname)
                    params.append(
                        {
                            "name": pname,
                            "python_name": python_name(pname),
                            "in": where,
                            "required": bool(param.get("required")) or where == "path",
                            "schema": schema_type(
                                resolve(param.get("schema") or {}, definitions)
                            ),
                        }
                    )
                params += body_parameters(operation, definitions, taken)
                entries[name] = {
                    "method": name,
                    "name": name,
                    "http": method.upper(),
                    "path": path,
                    "summary": str(operation.get("summary") or name.replace("_", " ")),
                    "parameters": params,
                }
    OUTPUT.write_text(
        json.dumps(sorted(entries.values(), key=lambda e: e["method"]), indent=1) + "\n"
    )
    print(f"{len(entries)} operations -> {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
