import os
import re
import yaml

source_dir = "/home/apps/workspace/open-source-libraries/mattermost/api/v4/source"
package_dir = "/home/apps/workspace/agent-packages/agents/mattermost-mcp/mattermost_mcp"
api_dir = os.path.join(package_dir, "api")
mcp_dir = os.path.join(package_dir, "mcp")

# Ensure target directories exist
os.makedirs(api_dir, exist_ok=True)
os.makedirs(mcp_dir, exist_ok=True)

files = [f for f in os.listdir(source_dir) if f.endswith(".yaml") or f.endswith(".yml")]
files = sorted(files)

# Exclude non-API specs
exclude_files = ["definitions.yaml", "introduction.yaml"]
api_files = [f for f in files if f not in exclude_files]

print(f"Generating Mattermost MCP modules for {len(api_files)} spec files...")

def camel_to_snake(name: str) -> str:
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    name = re.sub(r'[^a-z0-9_]', '_', name)
    name = re.sub(r'_+', '_', name)
    return name.strip('_')

def extract_path_params(path: str) -> list[str]:
    return re.findall(r"\{([a-zA-Z0-9_]+)\}", path)

def make_func_name(method: str, path: str, op_id: str | None) -> str:
    if op_id:
        return camel_to_snake(op_id)
    clean_path = path.replace("/api/v4", "")
    clean_path = re.sub(r'\{([a-zA-Z0-9_]+)\}', r'by_\1', clean_path)
    clean_path = re.sub(r'[^a-zA-Z0-9_]', '_', clean_path)
    clean_path = re.sub(r'_+', '_', clean_path).strip('_')
    return f"{method.lower()}_{clean_path.lower()}"

generated_modules = []

for file in api_files:
    module_name = os.path.splitext(file)[0]
    filepath = os.path.join(source_dir, file)
    
    with open(filepath, 'r') as f:
        try:
            content = yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading {file}: {e}")
            continue
            
    if not content:
        continue
        
    paths = [key for key in content.keys() if key.startswith("/")]
    if not paths:
        continue
        
    methods_code = []
    actions_list = []
    
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
                summary = op.get("summary", "").replace('"', '\\"').replace('\n', ' ')
                
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
                    req_call = f'self.request("{http_method.upper()}", url, params=kwargs)'
                else:
                    req_call = f'self.request("{http_method.upper()}", url, data=kwargs)'
                    
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
        
    generated_modules.append({
        "name": module_name,
        "actions": actions_list
    })
    
    # 1. Write the API client file
    api_filename = f"api_client_{module_name}.py"
    api_filepath = os.path.join(api_dir, api_filename)
    
    api_content = f"""\"\"\"
This file was automatically generated. Do not edit manually.
\"\"\"
from typing import Any
from mattermost_mcp.api.api_client_base import ApiClientBase


class Api(ApiClientBase):
"""
    api_content += "\n".join(methods_code)
    
    with open(api_filepath, 'w') as f:
        f.write(api_content)
        
    # 2. Write the MCP tool registration file
    mcp_filename = f"mcp_{module_name}.py"
    mcp_filepath = os.path.join(mcp_dir, mcp_filename)
    
    actions_list_str = ", ".join([f"'{a}'" for a in actions_list])
    
    mcp_content = f"""\"\"\"
This file was automatically generated. Do not edit manually.
\"\"\"
from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from mattermost_mcp.auth import get_client


def register_{module_name}_tools(mcp: FastMCP):
    \"\"\"Register Mattermost MCP {module_name} tools.\"\"\"

    @mcp.tool(tags=["{module_name}"])
    async def mattermost_mcp_{module_name}(
        action: str = Field(
            description="Action to perform. Must be one of: {actions_list_str}"
        ),
        params_json: str = Field(
            default="{{}}", description="JSON string of parameters."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(default=None, description="MCP context"),
    ) -> dict:
        \"\"\"Manage Mattermost MCP {module_name} operations.\"\"\"
        if ctx:
            await ctx.info("Executing {module_name} operation: " + str(action) + "...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {{"error": "Invalid params_json: " + str(e)}}

        kwargs = {{k: v for k, v in kwargs.items() if v is not None}}

        method = getattr(client, action, None)
        if not method:
            alt_action = action.replace("-", "_").replace(" ", "_").lower()
            method = getattr(client, alt_action, None)

        if not method:
            return {{"error": "Unknown action '" + str(action) + "' on client."}}

        try:
            res = method(**kwargs)
            if res is None:
                return {{"status": "success"}}
            return res
        except Exception as e:
            return {{"error": "Failed to execute operation " + str(action) + ": " + str(e)}}
"""
    with open(mcp_filepath, 'w') as f:
        f.write(mcp_content)

print(f"Successfully generated {len(generated_modules)} modules in api/ and mcp/ directories!")

# 3. Generate api/__init__.py
api_init_filepath = os.path.join(api_dir, "__init__.py")
api_init_imports = ["from mattermost_mcp.api.api_client_base import ApiClientBase"]
api_init_all = ["ApiClientBase"]

for module_info in generated_modules:
    name_str = str(module_info["name"])
    cls_alias = "".join([part.capitalize() for part in name_str.split("_")])
    api_init_imports.append(f"from mattermost_mcp.api.api_client_{name_str} import Api as Api{cls_alias}")
    api_init_all.append(f"Api{cls_alias}")

api_init_content = f"""\"\"\"
This file was automatically generated. Do not edit manually.
\"\"\"
"""
api_init_content += "\n".join(api_init_imports) + "\n\n"
api_init_content += "__all__ = [\n" + ",\n".join([f"    \"{a}\"" for a in api_init_all]) + ",\n]\n"

with open(api_init_filepath, 'w') as f:
    f.write(api_init_content)

# 4. Generate mcp/__init__.py
mcp_init_filepath = os.path.join(mcp_dir, "__init__.py")
mcp_init_imports = []
mcp_init_all = []

for module_info in generated_modules:
    name_str = str(module_info["name"])
    mcp_init_imports.append(f"from mattermost_mcp.mcp.mcp_{name_str} import register_{name_str}_tools")
    mcp_init_all.append(f"register_{name_str}_tools")

mcp_init_content = f"""\"\"\"
This file was automatically generated. Do not edit manually.
\"\"\"
"""
mcp_init_content += "\n".join(mcp_init_imports) + "\n\n"
mcp_init_content += "__all__ = [\n" + ",\n".join([f"    \"{a}\"" for a in mcp_init_all]) + ",\n]\n"

with open(mcp_init_filepath, 'w') as f:
    f.write(mcp_init_content)

# 5. Generate api_client.py
api_client_filepath = os.path.join(package_dir, "api_client.py")
api_client_imports = []
api_client_classes = []

for module_info in generated_modules:
    name_str = str(module_info["name"])
    cls_alias = "".join([part.capitalize() for part in name_str.split("_")])
    api_client_imports.append(f"from mattermost_mcp.api.api_client_{name_str} import Api as {cls_alias}Api")
    api_client_classes.append(f"{cls_alias}Api")

api_client_classes_str = ", ".join(api_client_classes)

api_client_content = f"""\"\"\"CONCEPT:MM-001 Dynamic client facade orchestration and resource mappings.\"\"\"
# !/usr/bin/env python
"""
api_client_content += "\n".join(api_client_imports) + "\n\n"
api_client_content += "__version__ = \"0.15.0\"\n\n\n"
api_client_content += f"class Api({api_client_classes_str}):\n    pass\n"

with open(api_client_filepath, 'w') as f:
    f.write(api_client_content)

# 6. Generate mcp_server.py
mcp_server_filepath = os.path.join(package_dir, "mcp_server.py")
mcp_server_imports = []
mcp_server_calls = []

for module_info in generated_modules:
    name_str = str(module_info["name"])
    mcp_server_imports.append(f"from mattermost_mcp.mcp.mcp_{name_str} import register_{name_str}_tools")
    
    env_var_name = f"{name_str.upper()}TOOL"
    call_block = f"""    DEFAULT_{env_var_name} = to_boolean(os.getenv("{env_var_name}", "True"))
    if DEFAULT_{env_var_name}:
        register_{name_str}_tools(mcp)"""
    mcp_server_calls.append(call_block)

mcp_server_imports_str = "\n".join(mcp_server_imports)
mcp_server_calls_str = "\n\n".join(mcp_server_calls)

mcp_server_content = f"""\"\"\"Main FastMCP server and tool registration.\"\"\"
import os
import sys
from typing import Any

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv
from fastmcp.utilities.logging import get_logger
from starlette.requests import Request
from starlette.responses import JSONResponse

{mcp_server_imports_str}

__version__ = "0.15.0"
logger = get_logger(name="mattermost_mcp")


def get_mcp_instance() -> tuple[Any, ...]:
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="Mattermost MCP MCP",
        version=__version__,
        instructions="Mattermost MCP MCP Server - Managed dynamic operations.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({{"status": "OK"}})

{mcp_server_calls_str}

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares


def mcp_server() -> None:
    mcp, args, middlewares = get_mcp_instance()
    print(f"Mattermost MCP MCP v{{__version__}}", file=sys.stderr)
    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    mcp_server()
"""

with open(mcp_server_filepath, 'w') as f:
    f.write(mcp_server_content)

print("All code generation complete!")
