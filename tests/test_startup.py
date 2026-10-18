import pytest


@pytest.mark.concept("MM-002")
def test_startup():
    # Basic import test
    import mattermost_mcp

    import tomllib
    from pathlib import Path

    project = tomllib.loads(
        (Path(__file__).resolve().parents[1] / "pyproject.toml").read_text(encoding="utf-8")
    )
    assert mattermost_mcp.__version__ == project["project"]["version"]
