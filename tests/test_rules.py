"""Tests for rules/*.mdc files."""

from pathlib import Path

import pytest

from conftest import parse_frontmatter


def collect_rule_files(rules_dir: Path) -> list[Path]:
    return sorted(rules_dir.glob("*.mdc"))


@pytest.fixture(scope="session")
def rule_files(rules_dir: Path) -> list[Path]:
    files = collect_rule_files(rules_dir)
    assert len(files) > 0, "No .mdc rule files found"
    return files


def pytest_generate_tests(metafunc):
    if "rule_file" in metafunc.fixturenames:
        rd = Path(__file__).resolve().parent.parent / "rules"
        files = collect_rule_files(rd)
        metafunc.parametrize(
            "rule_file", files, ids=[f.stem for f in files]
        )


class TestRuleDiscovery:
    def test_rules_directory_exists(self, rules_dir: Path):
        assert rules_dir.is_dir()

    def test_at_least_one_rule(self, rule_files: list[Path]):
        assert len(rule_files) >= 1


class TestRuleContent:
    def test_has_frontmatter(self, rule_file: Path):
        text = rule_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        assert isinstance(fm, dict)

    def test_frontmatter_has_description(self, rule_file: Path):
        text = rule_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        assert "description" in fm, f"{rule_file.stem}: frontmatter missing 'description'"

    def test_frontmatter_has_always_apply(self, rule_file: Path):
        text = rule_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        assert "alwaysApply" in fm, f"{rule_file.stem}: frontmatter missing 'alwaysApply'"

    def test_always_apply_is_boolean(self, rule_file: Path):
        text = rule_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        assert isinstance(fm["alwaysApply"], bool), (
            f"{rule_file.stem}: alwaysApply must be boolean, got {type(fm['alwaysApply']).__name__}"
        )

    def test_globs_present_when_not_always_apply(self, rule_file: Path):
        text = rule_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if not fm.get("alwaysApply", True):
            assert "globs" in fm and fm["globs"], (
                f"{rule_file.stem}: alwaysApply is false but 'globs' is missing or empty"
            )

    def test_globs_is_list(self, rule_file: Path):
        text = rule_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if "globs" in fm:
            assert isinstance(fm["globs"], list), (
                f"{rule_file.stem}: globs must be a list"
            )

    def test_description_non_empty(self, rule_file: Path):
        text = rule_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        assert len(fm.get("description", "")) >= 10, (
            f"{rule_file.stem}: description too short"
        )
