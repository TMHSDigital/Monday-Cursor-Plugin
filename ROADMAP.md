# Roadmap

Versioned release plan for Monday Developer Tools.

| Version | Theme | Skills | Rules | Highlights | Status |
|---------|-------|--------|-------|------------|--------|
| **v0.1.0** | Foundation | 6 | 3 | Core board/item/workspace/API skills, token safety + GraphQL + rate limit rules, plugin scaffold, tests, CI | **Current** |
| **v0.2.0** | Views | +3 (9) | +1 (4) | Dashboard builder, board insights, chart visualization, column value format rule | Planned |
| **v0.3.0** | Collaboration | +3 (12) | +1 (5) | Updates and communication, docs management, notifications, webhook validation rule | Planned |
| **v0.4.0** | Sprints | +3 (15) | +1 (6) | Sprint planning, sprint review, notetaker meetings, error handling rule | Planned |
| **v0.5.0** | Automation | +3 (18) | +1 (7) | Workflow automation, form builder, webhook management, MCP tool preference rule | Planned |
| **v0.6.0** | PM | +3 (21) | +1 (8) | Project tracking, resource management, tags and assets, board structure rule | Planned |
| **v1.0.0** | Stable | 21 | 8 | Production release, polished docs site, comprehensive README | Planned |

## v0.1.0 -- Foundation

Skills:
- `monday-board-management` -- boards, columns, groups, permissions
- `monday-item-operations` -- items, subitems, column values
- `monday-workspace-organizer` -- workspaces, folders, hierarchy
- `monday-api-reference` -- GraphQL, schema, complexity, escape hatch
- `monday-column-types-guide` -- column types, value formats
- `monday-user-and-team-management` -- users, teams, roles

Rules:
- `monday-api-token-safety` -- flag hardcoded tokens
- `monday-graphql-best-practices` -- flag over-fetching, missing pagination
- `monday-rate-limit-awareness` -- flag missing backoff, unbounded loops

Infrastructure:
- Plugin scaffold (`.cursor-plugin/plugin.json`)
- pytest structure tests (7 files)
- GitHub Actions (validate, CodeQL, Pages, stale, release-drafter)
- Community files (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY)
- CLAUDE.md project brain
- GitHub Pages docs site

## v0.2.0 -- Views and Reporting

Skills:
- `monday-dashboard-builder` -- dashboards, widgets, chart types
- `monday-board-insights` -- aggregation, filtering, analysis
- `monday-chart-visualization` -- pie/bar charts, battery widgets, tables

Rules:
- `monday-column-value-format` -- flag malformed column value JSON

## v0.3.0 -- Collaboration

Skills:
- `monday-updates-and-communication` -- updates, replies, mentions
- `monday-docs-management` -- Monday Docs, version history
- `monday-notifications` -- bell and email notifications

Rules:
- `monday-webhook-validation` -- flag missing challenge verification

## v0.4.0 -- Dev and Sprints

Skills:
- `monday-sprint-planning` -- sprint boards, metadata, iterations
- `monday-sprint-review` -- sprint analysis, velocity, burndown
- `monday-notetaker-meetings` -- meeting notes, transcripts

Rules:
- `monday-error-handling` -- flag unchecked API responses

## v0.5.0 -- Automation

Skills:
- `monday-workflow-automation` -- automation recipes, triggers, actions
- `monday-form-builder` -- forms, questions, conditional logic
- `monday-webhook-management` -- webhook CRUD, JWT auth

Rules:
- `monday-mcp-tool-preference` -- flag raw API calls when MCP tools exist

## v0.6.0 -- Project Management

Skills:
- `monday-project-tracking` -- timeline, dependencies, critical path
- `monday-resource-management` -- team assignment, workload, capacity
- `monday-tags-and-assets` -- tag management, file/asset operations

Rules:
- `monday-board-structure` -- flag board anti-patterns

## v1.0.0 -- Stable

All 21 skills and 8 rules complete. Production release with polished documentation.

## Completed

- [x] v0.1.0 Foundation

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add skills, rules, and improvements.
