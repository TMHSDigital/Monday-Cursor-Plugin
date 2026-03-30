"""Shared fixtures for Monday-Cursor-Plugin test suite."""

from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def root_dir() -> Path:
    return Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def skills_dir(root_dir: Path) -> Path:
    return root_dir / "skills"


@pytest.fixture(scope="session")
def rules_dir(root_dir: Path) -> Path:
    return root_dir / "rules"


@pytest.fixture(scope="session")
def plugin_json(root_dir: Path) -> Path:
    return root_dir / ".cursor-plugin" / "plugin.json"


@pytest.fixture(scope="session")
def readme(root_dir: Path) -> Path:
    return root_dir / "README.md"


@pytest.fixture(scope="session")
def claude_md(root_dir: Path) -> Path:
    return root_dir / "CLAUDE.md"


@pytest.fixture(scope="session")
def roadmap_md(root_dir: Path) -> Path:
    return root_dir / "ROADMAP.md"


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from a markdown file.

    Expects the file to start with '---', followed by YAML, followed by '---'.
    Returns the parsed dict or raises ValueError.
    """
    import yaml

    stripped = text.strip()
    if not stripped.startswith("---"):
        raise ValueError("File does not start with YAML frontmatter delimiter '---'")

    parts = stripped.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Could not find closing '---' for YAML frontmatter")

    # parts[0] is empty (before first ---), parts[1] is the YAML block
    return yaml.safe_load(parts[1]) or {}
