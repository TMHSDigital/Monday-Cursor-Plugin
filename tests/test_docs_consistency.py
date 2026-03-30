"""Tests that README.md and CLAUDE.md reflect actual skill/rule counts."""

from pathlib import Path


class TestDocsConsistency:
    def _count_skills(self, skills_dir: Path) -> int:
        return len(list(skills_dir.glob("*/SKILL.md")))

    def _count_rules(self, rules_dir: Path) -> int:
        return len(list(rules_dir.glob("*.mdc")))

    def test_claude_md_exists(self, claude_md: Path):
        assert claude_md.exists(), "CLAUDE.md not found"

    def test_readme_exists(self, readme: Path):
        assert readme.exists(), "README.md not found"

    def test_claude_md_skill_count(self, claude_md: Path, skills_dir: Path):
        count = self._count_skills(skills_dir)
        text = claude_md.read_text(encoding="utf-8")
        expected = f"{count} skills"
        assert expected in text, (
            f"CLAUDE.md should contain '{expected}' but it doesn't "
            f"(found {count} skill directories on disk)"
        )

    def test_claude_md_rule_count(self, claude_md: Path, rules_dir: Path):
        count = self._count_rules(rules_dir)
        text = claude_md.read_text(encoding="utf-8")
        expected = f"{count} rules"
        assert expected in text, (
            f"CLAUDE.md should contain '{expected}' but it doesn't "
            f"(found {count} rule files on disk)"
        )

    def test_readme_skill_count(self, readme: Path, skills_dir: Path):
        count = self._count_skills(skills_dir)
        text = readme.read_text(encoding="utf-8")
        expected = f"{count} skills"
        assert expected in text, (
            f"README.md should contain '{expected}' but it doesn't "
            f"(found {count} skill directories on disk)"
        )

    def test_readme_rule_count(self, readme: Path, rules_dir: Path):
        count = self._count_rules(rules_dir)
        text = readme.read_text(encoding="utf-8")
        expected = f"{count} rules"
        assert expected in text, (
            f"README.md should contain '{expected}' but it doesn't "
            f"(found {count} rule files on disk)"
        )

    def test_plugin_json_description_skill_count(
        self, plugin_json: Path, skills_dir: Path
    ):
        import json

        count = self._count_skills(skills_dir)
        data = json.loads(plugin_json.read_text(encoding="utf-8"))
        desc = data.get("description", "")
        expected = f"{count} skills"
        assert expected in desc, (
            f"plugin.json description should contain '{expected}' "
            f"(found {count} skill directories on disk)"
        )

    def test_plugin_json_description_rule_count(
        self, plugin_json: Path, rules_dir: Path
    ):
        import json

        count = self._count_rules(rules_dir)
        data = json.loads(plugin_json.read_text(encoding="utf-8"))
        desc = data.get("description", "")
        expected = f"{count} rules"
        assert expected in desc, (
            f"plugin.json description should contain '{expected}' "
            f"(found {count} rule files on disk)"
        )
