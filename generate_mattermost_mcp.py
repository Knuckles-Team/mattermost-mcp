import os
import re
from pathlib import Path

import yaml

source_dir = os.environ.get("MATTERMOST_OPENAPI_SOURCE")
if not source_dir:
    raise SystemExit("MATTERMOST_OPENAPI_SOURCE must reference the OpenAPI source")
package_dir = os.environ.get(
    "MATTERMOST_MCP_PACKAGE_DIR",
    str(Path(__file__).resolve().parent / "mattermost_mcp"),
)
api_dir = os.path.join(package_dir, "api")

# Ensure target directories exist
os.makedirs(api_dir, exist_ok=True)

files = [f for f in os.listdir(source_dir) if f.endswith(".yaml") or f.endswith(".yml")]
files = sorted(files)

# Exclude non-API specs
exclude_files = ["definitions.yaml", "introduction.yaml"]
api_files = [f for f in files if f not in exclude_files]

print(f"Generating Mattermost MCP modules for {len(api_files)} spec files...")


def camel_to_snake(name: str) -> str:
    name = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
    name = re.sub(r"[^a-z0-9_]", "_", name)
    name = re.sub(r"_+", "_", name)
    return name.strip("_")


def extract_path_params(path: str) -> list[str]:
    return re.findall(r"\{([a-zA-Z0-9_]+)\}", path)


def make_func_name(method: str, path: str, op_id: str | None) -> str:
    if op_id:
        return camel_to_snake(op_id)
    clean_path = path.replace("/api/v4", "")
    clean_path = re.sub(r"\{([a-zA-Z0-9_]+)\}", r"by_\1", clean_path)
    clean_path = re.sub(r"[^a-zA-Z0-9_]", "_", clean_path)
    clean_path = re.sub(r"_+", "_", clean_path).strip("_")
    return f"{method.lower()}_{clean_path.lower()}"


generated_modules = []

for file in api_files:
    module_name = os.path.splitext(file)[0]
    filepath = os.path.join(source_dir, file)

    with open(filepath) as f:
        try:
            content = yaml.safe_load(f)
        except Exception as e:
            print(f"Operation failed: {type(e).__name__}")
            continue

    if not content:
        continue

    paths = [key for key in content.keys() if key.startswith("/")]
    if not paths:
        continue

    methods_code = []
    actions_list = []
    seen_names: set[str] = set()
    duplicated: set[str] = set()
    for _path in paths:
        for _verb_name, _op in (content[_path] or {}).items():
            if _verb_name in ("get", "post", "put", "delete", "patch") and isinstance(
                _op, dict
            ):
                _name = make_func_name(_verb_name, _path, _op.get("operationId"))
                (duplicated if _name in seen_names else seen_names).add(_name)

    for path in paths:
        path_item = content[path]
        if not isinstance(path_item, dict):
            continue

        path_params = extract_path_params(path)

        for http_method in ["get", "post", "put", "delete", "patch"]:
            if http_method in path_item:
                op = path_item[http_method]
                if not isinstance(op, dict):
                    continue

                op_id = op.get("operationId")
                func_name = make_func_name(http_method, path, op_id)
                if func_name in duplicated and "{team_id}" in path:
                    # Mattermost reuses an operationId for the team-scoped variant
                    # (SearchFiles); name it <verb>_team_<rest>, as
                    # scripts/build_operation_manifest.py does.
                    verb, _, rest = func_name.partition("_")
                    func_name = f"{verb}_team_{rest}"
                summary = op.get("summary", "").replace('"', '\\"').replace("\n", " ")

                # Signature parameters
                sig_params = []
                for p in path_params:
                    sig_params.append(f"{p}: str")

                sig_str = ", ".join(sig_params)
                if sig_str:
                    sig_str = f"{sig_str}, "

                # Format templating dictionary for URL parameters
                format_dict_parts = [f"{p}={p}" for p in path_params]
                format_dict_str = ", ".join(format_dict_parts)

                if path_params:
                    url_val = f'"{path}".format({format_dict_str})'
                else:
                    url_val = f'"{path}"'

                # GET/DELETE uses params=kwargs, others use data=kwargs
                if http_method in ["get", "delete"]:
                    req_call = (
                        f'self.request("{http_method.upper()}", url, params=kwargs)'
                    )
                else:
                    req_call = (
                        f'self.request("{http_method.upper()}", url, data=kwargs)'
                    )

                method_def = f"""    def {func_name}(self, {sig_str}**kwargs) -> Any:
        \"\"\"{summary}

        Path: {path}
        Method: {http_method.upper()}
        \"\"\"
        url = {url_val}
        return {req_call}
"""
                methods_code.append(method_def)
                actions_list.append(func_name)

    if not methods_code:
        continue

    generated_modules.append({"name": module_name, "actions": actions_list})

    # 1. Write the API client file
    api_filename = f"api_client_{module_name}.py"
    api_filepath = os.path.join(api_dir, api_filename)

    api_content = """\"\"\"
This file was automatically generated. Do not edit manually.
\"\"\"
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
"""
    api_content += "\n".join(methods_code)

    with open(api_filepath, "w") as f:
        f.write(api_content)

print(f"Successfully generated {len(generated_modules)} client modules in api/!")

# 3. Generate api/__init__.py
api_init_filepath = os.path.join(api_dir, "__init__.py")
api_init_imports = ["from mattermost_mcp.api.api_client_base import ApiClientBase"]
api_init_all = ["ApiClientBase"]

for module_info in generated_modules:
    name_str = str(module_info["name"])
    cls_alias = "".join([part.capitalize() for part in name_str.split("_")])
    api_init_imports.append(
        f"from mattermost_mcp.api.api_client_{name_str} import Api as Api{cls_alias}"
    )
    api_init_all.append(f"Api{cls_alias}")

api_init_content = """\"\"\"
This file was automatically generated. Do not edit manually.
\"\"\"
"""
api_init_content += "\n".join(api_init_imports) + "\n\n"
api_init_content += (
    "__all__ = [\n" + ",\n".join([f'    "{a}"' for a in api_init_all]) + ",\n]\n"
)

with open(api_init_filepath, "w") as f:
    f.write(api_init_content)

# 5. Generate api_client.py
api_client_filepath = os.path.join(package_dir, "api_client.py")
api_client_imports = []
api_client_classes = []

for module_info in generated_modules:
    name_str = str(module_info["name"])
    cls_alias = "".join([part.capitalize() for part in name_str.split("_")])
    api_client_imports.append(
        f"from mattermost_mcp.api.api_client_{name_str} import Api as {cls_alias}Api"
    )
    api_client_classes.append(f"{cls_alias}Api")

api_client_classes_str = ", ".join(api_client_classes)

api_client_content = """\"\"\"CONCEPT:MM-OS.governance.mm Dynamic client facade orchestration and resource mappings.\"\"\"
# !/usr/bin/env python
"""
api_client_content += "\n".join(api_client_imports) + "\n\n"
_existing = (
    open(api_client_filepath).read() if os.path.exists(api_client_filepath) else ""
)
_version = re.search(r'__version__ = "([^"]+)"', _existing)
api_client_content += (
    f'__version__ = "{_version.group(1) if _version else "0.0.0"}"\n\n\n'
)
api_client_content += f"class Api({api_client_classes_str}):\n    pass\n"

with open(api_client_filepath, "w") as f:
    f.write(api_client_content)

print("All code generation complete!")
