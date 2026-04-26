<!-- standards-version: 1.9.0 -->

# Monday Developer Tools -- Project Brain

Monday.com workflows for Cursor IDE. 21 skills, 8 rules, leveraging the official Monday MCP plugin (~45 tools).

## Directory Structure

```
Monday-Cursor-Plugin/
  .cursor-plugin/plugin.json       # Plugin manifest
  assets/logo.png                  # Plugin logo
  skills/*/SKILL.md                # 21 skills (kebab-case dirs)
  rules/*.mdc                      # 8 rules
  tests/                           # pytest structure tests
  docs/index.html                  # GitHub Pages site
  .github/                         # CI/CD, templates
  .cursorrules                     # Contributor conventions
  CLAUDE.md                        # This file
  README.md                        # Public docs
  CHANGELOG.md                     # Release history
  CONTRIBUTING.md                  # How to contribute
  ROADMAP.md                       # Versioned release plan
```

## Skills (21)

| Category | Skill | Description |
|----------|-------|-------------|
| **Core** | `monday-board-management` | Create, configure, duplicate, archive, delete boards; columns, groups, permissions |
| **Core** | `monday-item-operations` | Create, update, move, archive, delete items and subitems |
| **Core** | `monday-workspace-organizer` | Workspaces, folders, board hierarchy |
| **Core** | `monday-api-reference` | GraphQL schema, query building, pagination, complexity, escape hatch |
| **Views** | `monday-dashboard-builder` | Create dashboards, widgets, chart types |
| **Views** | `monday-board-insights` | Aggregate, filter, analyze board data |
| **Views** | `monday-chart-visualization` | Render pie/bar charts, battery widgets, tables |
| **Collab** | `monday-updates-and-communication` | Post updates, replies, mentions |
| **Collab** | `monday-docs-management` | Create, read, append Monday Docs |
| **Collab** | `monday-notifications` | Bell and email notifications |
| **Sprints** | `monday-sprint-planning` | Sprint boards, metadata, iteration planning |
| **Sprints** | `monday-sprint-review` | Completed sprint analysis, velocity |
| **Sprints** | `monday-notetaker-meetings` | Meeting notes, summaries, action items |
| **Automation** | `monday-workflow-automation` | Automation recipes, triggers, conditions, actions |
| **Automation** | `monday-form-builder` | Forms, questions, conditional logic |
| **Automation** | `monday-webhook-management` | Webhook CRUD, challenge verification, JWT auth |
| **PM** | `monday-project-tracking` | Timeline, dependencies, critical path, status |
| **PM** | `monday-resource-management` | Team assignment, workload, capacity |
| **Admin** | `monday-user-and-team-management` | Users, teams, permissions, roles |
| **Admin** | `monday-column-types-guide` | Column type reference, value formats |
| **Admin** | `monday-tags-and-assets` | Tag management, file/asset operations |

## Rules (8)

| Rule | Scope | What It Does |
|------|-------|-------------|
| `monday-api-token-safety` | Always | Flag hardcoded API tokens and OAuth secrets |
| `monday-graphql-best-practices` | `*.graphql`, `*.gql`, `*.ts`, `*.js` | Flag over-fetching, missing pagination, unbounded queries |
| `monday-rate-limit-awareness` | `*.ts`, `*.js`, `*.py` | Flag missing retry/backoff, unbounded API loops |
| `monday-column-value-format` | `*.ts`, `*.js`, `*.py` | Flag malformed column value JSON |
| `monday-webhook-validation` | `*.ts`, `*.js`, `*.py` | Flag missing challenge verification, exposed webhook URLs |
| `monday-mcp-tool-preference` | Always | Flag raw API calls when MCP tools are available |
| `monday-board-structure` | `*.json`, `*.ts` | Flag board anti-patterns (too many columns, missing groups) |
| `monday-error-handling` | `*.ts`, `*.js`, `*.py` | Flag unchecked API responses, missing error parsing |

## Monday MCP Tools (~45)

The plugin leverages the official Monday.com MCP (`plugin-monday.com-monday`). Install it from the Cursor marketplace.

### Context and Search

| Tool | What It Does |
|------|-------------|
| `get_user_context` | Current user, favorites, relevant boards |
| `search` | Search boards, documents, folders |
| `list_users_and_teams` | Look up users and teams |

### Boards, Items, Updates

| Tool | What It Does |
|------|-------------|
| `get_board_info` | Board metadata, structure, owners, views |
| `get_board_items_page` | Paginated items with filters and search |
| `board_insights` | Aggregate and analyze board data |
| `create_board` | Create a new board |
| `create_group` | Add a group to a board |
| `create_column` | Add a column to a board |
| `create_item` | Create items, subitems, or duplicates |
| `change_item_column_values` | Update item column values |
| `get_updates` | Read updates on items or boards |
| `create_update` | Post updates with mentions |
| `get_board_activity` | Board activity log |

### Workspaces, Folders, Move

| Tool | What It Does |
|------|-------------|
| `list_workspaces` | List/search workspaces |
| `workspace_info` | Boards, docs, folders in a workspace |
| `create_workspace` | Create a workspace |
| `update_workspace` | Update workspace attributes |
| `create_folder` | Create a folder |
| `update_folder` | Update folder attributes |
| `move_object` | Move boards/folders/overviews |

### Docs

| Tool | What It Does |
|------|-------------|
| `read_docs` | Read doc content or version history |
| `create_doc` | Create a doc in workspace or attached to item |
| `add_content_to_doc` | Append markdown to a doc |

### Dashboards and Widgets

| Tool | What It Does |
|------|-------------|
| `create_dashboard` | Create a dashboard |
| `create_widget` | Add a widget to dashboard or board view |
| `all_widgets_schema` | Widget type JSON schemas |

### Forms

| Tool | What It Does |
|------|-------------|
| `create_form` | Create a form with response board |
| `get_form` | Get form by token |
| `update_form` | Update form settings, appearance, questions |
| `form_questions_editor` | Create/update/delete individual questions |

### Sprints and Meetings

| Tool | What It Does |
|------|-------------|
| `get_monday_dev_sprints_boards` | Discover sprint/tasks board pairs |
| `get_sprints_metadata` | Sprint table from sprints board |
| `get_sprint_summary` | Completed sprint analysis |
| `get_notetaker_meetings` | Meeting notes and transcripts |

### API and Schema

| Tool | What It Does |
|------|-------------|
| `get_graphql_schema` | Schema overview (read vs write) |
| `get_type_details` | Details for a GraphQL type |
| `get_column_type_info` | Column type metadata |
| `all_monday_api` | Run arbitrary GraphQL (escape hatch) |

### UI Components

| Tool | What It Does |
|------|-------------|
| `show-chart` | Render pie/bar charts |
| `show-battery` | Render battery/progress indicators |
| `show-table` | Render interactive board tables |
| `show-assign` | Render assignment UI |

### Notifications

| Tool | What It Does |
|------|-------------|
| `create_notification` | Send bell/email notifications |

## Key Conventions

- Skills: `skills/<kebab-name>/SKILL.md` with YAML frontmatter (`name`, `description`)
- Rules: `rules/<name>.mdc` with YAML frontmatter (`description`, `alwaysApply`, optional `globs`)
- Section order in skills: Trigger, Required Inputs, Workflow, Key References, Example Interaction, MCP Usage, Common Pitfalls, See Also
- No em dashes; use `--`
- No hardcoded secrets
- Column value JSON: outer key = column ID, not type name
- Use `all_monday_api` for operations without dedicated MCP tools

## Dev Workflow

```bash
# Install test deps
pip install -r requirements-test.txt

# Run structure tests
pytest tests/ -v

# No build step (pure markdown plugin)
```

## API Quick Reference

- Endpoint: `https://api.monday.com/v2` (GraphQL)
- Auth: `Authorization: <token>` header
- Complexity budget: 10,000,000 points/minute (varies by plan)
- Rate limits: `create_board`/`duplicate_board` capped at 40/minute
- Pagination: cursor-based via `items_page`
- API versioning: `YYYY-MM` format, check for breaking changes
