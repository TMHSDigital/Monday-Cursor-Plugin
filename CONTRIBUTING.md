# Contributing

Thanks for your interest in improving Monday Developer Tools. This guide covers the workflow for adding skills, rules, and other improvements.

## Setup

1. Fork and clone the repository
2. Symlink to your local Cursor plugins directory:

**Windows (PowerShell as Admin):**

```powershell
New-Item -ItemType SymbolicLink `
  -Path "$env:USERPROFILE\.cursor\plugins\local\monday-cursor-plugin" `
  -Target (Resolve-Path .\Monday-Cursor-Plugin)
```

**macOS / Linux:**

```bash
ln -s "$(pwd)/Monday-Cursor-Plugin" ~/.cursor/plugins/local/monday-cursor-plugin
```

3. Install test dependencies:

```bash
pip install -r requirements-test.txt
```

## Adding a Skill

Create `skills/<skill-name>/SKILL.md` with:

```markdown
---
name: monday-<skill-name>
description: At least 20 characters describing the skill.
---

# <Title>

## Trigger
## Required Inputs
## Workflow
## Key References
## Example Interaction
## MCP Usage
## Common Pitfalls
## See Also
```

Requirements:

- Directory name must be kebab-case and start with `monday-`
- `name` in frontmatter must match the directory name
- `description` must be at least 20 characters
- All 8 sections are required (Trigger through See Also)
- See Also links use relative paths: `../other-skill/SKILL.md`
- MCP Usage section should include a table of relevant MCP tools

## Adding a Rule

Create `rules/monday-<rule-name>.mdc` with:

```markdown
---
description: What this rule flags.
alwaysApply: true
---

# <Title>

## Patterns to Flag
## What to Do
## Exceptions
```

Requirements:

- Filename must be kebab-case and start with `monday-`
- If `alwaysApply: false`, must include a `globs` array
- Body must have Patterns to Flag, What to Do, and Exceptions sections

## Running Tests

```bash
pytest tests/ -v --tb=short
```

All tests must pass before submitting a PR.

## Pull Request Checklist

- [ ] YAML frontmatter is valid (skills: `name` + `description`; rules: `description` + `alwaysApply`)
- [ ] Tested locally (plugin loads, tests pass)
- [ ] Plugin structure tests pass (`pytest tests/ -v`)
- [ ] Updated CHANGELOG.md
- [ ] No hardcoded credentials or secrets
- [ ] No em dashes used (use `--` instead)

## Content Guidelines

- No em dashes; use double hyphens `--`
- No hardcoded API tokens or secrets
- Column value JSON examples must use the column ID as the outer key
- GraphQL examples should use variables for dynamic values
- Reference MCP tools by their exact names
- For operations not covered by MCP tools, provide `all_monday_api` GraphQL recipes
