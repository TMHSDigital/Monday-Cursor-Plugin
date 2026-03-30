"""Tests for ROADMAP.md structure and version entries."""

import re
from pathlib import Path

import pytest

SEMVER_HEADER_RE = re.compile(r"^#{1,3}\s+v?(\d+\.\d+\.\d+)", re.MULTILINE)


class TestRoadmap:
    def test_roadmap_exists(self, roadmap_md: Path):
        assert roadmap_md.exists(), "ROADMAP.md not found"

    @pytest.fixture()
    def roadmap_text(self, roadmap_md: Path) -> str:
        return roadmap_md.read_text(encoding="utf-8")

    def test_has_version_entries(self, roadmap_text: str):
        versions = SEMVER_HEADER_RE.findall(roadmap_text)
        assert len(versions) >= 1, "ROADMAP.md has no version headers (e.g. ## v0.1.0)"

    def test_contains_initial_version(self, roadmap_text: str):
        assert re.search(
            r"v?0\.1\.0", roadmap_text
        ), "ROADMAP.md should reference v0.1.0"

    def test_contains_target_version(self, roadmap_text: str):
        assert re.search(
            r"v?1\.0\.0", roadmap_text
        ), "ROADMAP.md should reference v1.0.0"

    def test_versions_are_ascending(self, roadmap_text: str):
        raw = SEMVER_HEADER_RE.findall(roadmap_text)
        if len(raw) < 2:
            pytest.skip("Fewer than 2 version entries, ordering check skipped")
        tuples = [tuple(int(x) for x in v.split(".")) for v in raw]
        assert tuples == sorted(tuples), (
            f"Version headers are not in ascending order: {raw}"
        )
