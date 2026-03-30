"""Tests for .cursor-plugin/plugin.json manifest."""

import json
from pathlib import Path

import pytest


class TestPluginManifest:
    def test_plugin_json_exists(self, plugin_json: Path):
        assert plugin_json.exists(), f"Missing {plugin_json}"

    def test_plugin_json_valid(self, plugin_json: Path):
        data = json.loads(plugin_json.read_text(encoding="utf-8"))
        assert isinstance(data, dict)

    @pytest.fixture()
    def manifest(self, plugin_json: Path) -> dict:
        return json.loads(plugin_json.read_text(encoding="utf-8"))

    @pytest.mark.parametrize(
        "field",
        ["name", "version", "description", "author", "skills", "rules", "logo"],
    )
    def test_required_fields(self, manifest: dict, field: str):
        assert field in manifest, f"plugin.json missing required field '{field}'"

    def test_name_is_kebab_case(self, manifest: dict):
        name = manifest["name"]
        assert name == name.lower(), "Plugin name should be lowercase"
        assert " " not in name, "Plugin name should not contain spaces"

    def test_version_format(self, manifest: dict):
        import re

        assert re.match(
            r"^\d+\.\d+\.\d+$", manifest["version"]
        ), f"Version '{manifest['version']}' is not semver"

    def test_description_non_empty(self, manifest: dict):
        assert len(manifest["description"]) >= 10

    def test_logo_file_exists(self, manifest: dict, root_dir: Path):
        logo_path = root_dir / manifest["logo"]
        assert logo_path.exists(), f"Logo file not found at {logo_path}"

    def test_skills_directory_exists(self, manifest: dict, root_dir: Path):
        skills_path = root_dir / manifest["skills"].strip("./")
        assert skills_path.is_dir(), f"Skills directory not found at {skills_path}"

    def test_rules_directory_exists(self, manifest: dict, root_dir: Path):
        rules_path = root_dir / manifest["rules"].strip("./")
        assert rules_path.is_dir(), f"Rules directory not found at {rules_path}"
