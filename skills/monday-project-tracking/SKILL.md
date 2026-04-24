---
name: monday-project-tracking
description: Track project timelines, dependencies, critical path, milestones, and status across Monday.com boards for project management.
standards-version: 1.6.3
---

# Monday Project Tracking

## Trigger

- User asks about project status, progress, or health
- User wants to view or manage timelines and dependencies
- User needs to identify the critical path or bottlenecks
- User asks about milestones, deadlines, or overdue items
- User wants a project status report or overview

## Required Inputs

- Board ID or project name
- Optional: specific group, date range, or status filter
- Timeline column ID (for dependency and critical path analysis)

## Workflow

1. Use `search` or `get_user_context` to find the project board.
2. Use `get_board_info` to identify timeline, status, dependency, and person columns.
3. Use `board_insights` for high-level project health (completion %, overdue items, blockers).
4. Use `get_board_items_page` with filters for detailed item-level data (timelines, statuses).
5. Analyze dependencies and identify the critical path by examining timeline overlaps and link columns.
6. Present results using `show-table` for detailed views or `show-chart`/`show-battery` for summaries.

## Key References

- [Timeline Column](https://developer.monday.com/api-reference/reference/column-types#timeline)
- [Dependency Column](https://developer.monday.com/api-reference/reference/column-types#dependency)
- [Project Views](https://support.monday.com/hc/en-us/articles/360002172956-Gantt-Chart-View)

## Example Interaction

**User:** What's the status of the "Website Redesign" project?

**Agent:**

```
1. search(searchTerm: "Website Redesign", searchType: "BOARD")
2. board_insights(boardId: "...", question: "Overall project completion percentage and overdue items")
3. show-battery(value: 68, label: "Website Redesign Progress")
4. Present: "68% complete. 4 items overdue, 2 items blocked. Critical path: Design Review -> Dev Handoff -> QA."
```

**User:** Show me all overdue tasks with their owners.

**Agent:**

```
1. get_board_info(boardId: "...") to get timeline and person column IDs
2. get_board_items_page(boardId: "...", filters: {rules: [{column_id: "timeline", compare_value: ["past"]}]})
3. show-table with item name, owner, timeline, and status columns
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `board_insights` | Get project health metrics, completion rates, overdue counts |
| `get_board_items_page` | Query items with timeline, status, and dependency filters |
| `get_board_info` | Identify column IDs for timeline, dependency, and status |
| `show-table` | Display project items with timeline and status details |
| `show-chart` | Visualize status distribution or timeline breakdowns |
| `show-battery` | Show overall project completion percentage |
| `change_item_column_values` | Update timelines, statuses, or dependencies |
| `all_monday_api` | Query dependency relationships, Gantt view data |

**GraphQL recipes for gap operations:**

Query items with timeline data:
```graphql
query { boards(ids: [1234567890]) { items_page(limit: 100) { items { id name column_values(ids: ["timeline", "status", "person"]) { id type value } } } } }
```

Get dependency column values:
```graphql
query { boards(ids: [1234567890]) { items_page(limit: 100) { items { id name column_values(ids: ["dependency"]) { value } } } } }
```

## Common Pitfalls

- Timeline columns store `{from, to}` date pairs -- both must be set for Gantt views to work
- Dependency columns use item IDs as links -- items must be on the same board or connected boards
- Critical path calculation is not built-in; derive it from dependency chains and timeline overlaps
- Overdue detection compares timeline end dates against today -- timezone settings matter
- Large projects (500+ items) should use pagination with `get_board_items_page` cursor
- Milestone items are regular items with same-day start/end timelines, not a separate entity

## See Also

- [monday-sprint-planning](../monday-sprint-planning/SKILL.md)
- [monday-resource-management](../monday-resource-management/SKILL.md)
- [monday-board-insights](../monday-board-insights/SKILL.md)
