"""Tests for skills/*/SKILL.md files."""

from pathlib import Path

import pytest

from conftest import parse_frontmatter

REQUIRED_SECTIONS = [
    "Trigger",
    "Required Inputs",
    "Workflow",
    "Key References",
    "Example Interaction",
    "MCP Usage",
    "Common Pitfalls",
    "See Also",
]


def collect_skill_files(skills_dir: Path) -> list[Path]:
    return sorted(skills_dir.glob("*/SKILL.md"))


@pytest.fixture(scope="session")
def skill_files(skills_dir: Path) -> list[Path]:
    files = collect_skill_files(skills_dir)
    assert len(files) > 0, "No SKILL.md files found"
    return files


def skill_ids(skills_dir: Path) -> list[str]:
    return [f.parent.name for f in collect_skill_files(skills_dir)]


def pytest_generate_tests(metafunc):
    if "skill_file" in metafunc.fixturenames:
        sd = Path(__file__).resolve().parent.parent / "skills"
        files = collect_skill_files(sd)
        metafunc.parametrize(
            "skill_file", files, ids=[f.parent.name for f in files]
        )


class TestSkillDiscovery:
    def test_skill_directories_exist(self, skills_dir: Path):
        assert skills_dir.is_dir()

    def test_at_least_one_skill(self, skill_files: list[Path]):
        assert len(skill_files) >= 1


class TestSkillContent:
    def test_has_frontmatter(self, skill_file: Path):
        text = skill_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        assert isinstance(fm, dict)

    def test_frontmatter_has_name(self, skill_file: Path):
        text = skill_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        assert "name" in fm, f"{skill_file.parent.name}: frontmatter missing 'name'"

    def test_frontmatter_has_description(self, skill_file: Path):
        text = skill_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        assert "description" in fm, f"{skill_file.parent.name}: frontmatter missing 'description'"

    def test_description_length(self, skill_file: Path):
        text = skill_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        desc = fm.get("description", "")
        assert len(desc) >= 20, (
            f"{skill_file.parent.name}: description too short ({len(desc)} chars)"
        )

    def test_name_matches_directory(self, skill_file: Path):
        text = skill_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        dir_name = skill_file.parent.name
        assert fm["name"] == dir_name, (
            f"Frontmatter name '{fm['name']}' != directory name '{dir_name}'"
        )

    @pytest.mark.parametrize("section", REQUIRED_SECTIONS)
    def test_required_section(self, skill_file: Path, section: str):
        text = skill_file.read_text(encoding="utf-8")
        header = f"## {section}"
        assert header in text, (
            f"{skill_file.parent.name}: missing required section '{header}'"
        )
