import pytest


@pytest.mark.concept("MM-002")
def test_startup():
    # Basic import test
    import tomllib
    from pathlib import Path

    import mattermost_mcp

    project = tomllib.loads(
        (Path(__file__).resolve().parents[1] / "pyproject.toml").read_text(
            encoding="utf-8"
        )
    )
    assert mattermost_mcp.__version__ == project["project"]["version"]
