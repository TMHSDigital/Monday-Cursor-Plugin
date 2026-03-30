---
name: monday-sprint-planning
description: Set up sprint boards, configure sprint metadata, plan iterations, and organize tasks for agile development on Monday.com.
---

# Monday Sprint Planning

## Trigger

- User wants to set up sprint boards for a project
- User needs to create or configure a new sprint iteration
- User asks about sprint structure, capacity, or iteration planning
- User wants to view sprint metadata or backlog
- User needs to assign tasks to an upcoming sprint

## Required Inputs

- Sprint board ID or project name
- Sprint name and dates (start/end) for new sprints
- Task board ID (the board containing sprint tasks)
- Sprint duration and capacity (optional)

## Workflow

1. Use `get_monday_dev_sprints_boards` to discover existing sprint/tasks board pairs.
2. If no sprint boards exist, use `create_board` to create a sprints board and a tasks board with appropriate columns (sprint, status, story points, assignee).
3. Use `get_sprints_metadata` to view current and upcoming sprint details (dates, status, items).
4. For new sprint creation: use `create_item` on the sprints board with sprint name, start date, and end date.
5. Assign tasks to the sprint by updating the sprint column on task items via `change_item_column_values`.
6. Use `board_insights` on the tasks board to check sprint capacity and workload distribution.

## Key References

- [Monday Dev Sprints](https://support.monday.com/hc/en-us/articles/4403498498578-monday-dev)
- [Sprint Planning](https://support.monday.com/hc/en-us/articles/4403498529426-Sprint-planning)

## Example Interaction

**User:** Set up Sprint 5 starting April 1 for 2 weeks.

**Agent:**

```
1. get_monday_dev_sprints_boards() to find the sprints board
2. get_sprints_metadata(sprintsBoardId: "...") to check existing sprints
3. create_item(boardId: "...", name: "Sprint 5", columnValues: "{\"date\": {\"from\": \"2026-04-01\", \"to\": \"2026-04-14\"}}")
4. board_insights(boardId: "...", question: "How many unassigned items are in the backlog?")
```

**User:** What sprints are planned for this project?

**Agent:**

```
1. get_monday_dev_sprints_boards() to find sprint boards
2. get_sprints_metadata(sprintsBoardId: "...") to list all sprints with dates and status
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `get_monday_dev_sprints_boards` | Discover sprint/tasks board pairs |
| `get_sprints_metadata` | View sprint details -- dates, status, item counts |
| `create_board` | Create new sprint or tasks boards |
| `create_item` | Create a new sprint iteration on the sprints board |
| `change_item_column_values` | Assign tasks to a sprint |
| `board_insights` | Analyze backlog size, capacity, workload |
| `create_column` | Add sprint-related columns (story points, sprint link) |

## Common Pitfalls

- Sprint boards and tasks boards are paired -- `get_monday_dev_sprints_boards` returns both
- Sprint dates use the `timeline` or `date` column format depending on board setup
- Assigning items to sprints uses the sprint column (a connect/link column type)
- Story point columns are typically `numbers` type -- don't confuse with `rating`
- Changing sprint dates after items are assigned does not automatically reschedule tasks
- Velocity calculations require completed sprint data -- see `monday-sprint-review`

## See Also

- [monday-sprint-review](../monday-sprint-review/SKILL.md)
- [monday-project-tracking](../monday-project-tracking/SKILL.md)
- [monday-item-operations](../monday-item-operations/SKILL.md)
