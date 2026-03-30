"""Tests that internal links in skill 'See Also' sections resolve to real files."""

import re
from pathlib import Path

import pytest

RELATIVE_LINK_RE = re.compile(r"\((\.\./[^)]+/SKILL\.md)\)")


def collect_see_also_links(skills_dir: Path) -> list[tuple[str, str, Path]]:
    """Return (skill_name, raw_link, expected_path) for every relative link in See Also."""
    results = []
    for skill_file in sorted(skills_dir.glob("*/SKILL.md")):
        text = skill_file.read_text(encoding="utf-8")
        see_also_idx = text.find("## See Also")
        if see_also_idx == -1:
            continue
        see_also_text = text[see_also_idx:]
        for match in RELATIVE_LINK_RE.finditer(see_also_text):
            raw = match.group(1)
            resolved = (skill_file.parent / raw).resolve()
            results.append((skill_file.parent.name, raw, resolved))
    return results


def pytest_generate_tests(metafunc):
    if "link_info" in metafunc.fixturenames:
        sd = Path(__file__).resolve().parent.parent / "skills"
        links = collect_see_also_links(sd)
        ids = [f"{name}:{raw}" for name, raw, _ in links]
        metafunc.parametrize("link_info", links, ids=ids)


class TestInternalLinks:
    def test_has_see_also_links(self, skills_dir: Path):
        links = collect_see_also_links(skills_dir)
        assert len(links) > 0, "No relative links found in any See Also section"

    def test_linked_file_exists(self, link_info: tuple[str, str, Path]):
        skill_name, raw_link, resolved_path = link_info
        assert resolved_path.exists(), (
            f"{skill_name}: See Also link '{raw_link}' resolves to "
            f"'{resolved_path}' which does not exist"
        )
