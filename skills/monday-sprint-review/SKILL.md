---
name: monday-sprint-review
description: Analyze completed sprints for velocity, burndown, completion rates, and team performance on Monday.com.
standards-version: 1.7.0
---

# Monday Sprint Review

## Trigger

- User asks about sprint results or outcomes
- User wants velocity metrics or burndown data
- User needs a completed sprint summary
- User asks how the team performed in a sprint
- User wants to compare sprint performance over time

## Required Inputs

- Sprint board ID or project name
- Sprint ID or sprint name to review
- Optional: number of past sprints to compare for velocity trends

## Workflow

1. Use `get_monday_dev_sprints_boards` to find the sprint/tasks board pair.
2. Use `get_sprints_metadata` to identify the completed sprint(s) to analyze.
3. Use `get_sprint_summary` with the sprint board ID and sprint ID to get completion stats.
4. For velocity trends: call `get_sprint_summary` for multiple past sprints and calculate averages.
5. Present results using `show-chart` (bar chart for velocity) or `show-battery` (completion rate).
6. Highlight carryover items, blockers, and team performance insights.

## Key References

- [Sprint Reviews](https://support.monday.com/hc/en-us/articles/4403498529426-Sprint-planning#sprint-review)
- [Velocity Tracking](https://support.monday.com/hc/en-us/articles/4403498498578-monday-dev)

## Example Interaction

**User:** How did Sprint 4 go?

**Agent:**

```
1. get_monday_dev_sprints_boards() to find sprint boards
2. get_sprints_metadata(sprintsBoardId: "...") to find Sprint 4 ID
3. get_sprint_summary(sprintsBoardId: "...", sprintId: "...")
4. Present: "Sprint 4: 18/22 items completed (82%). 4 items carried over. Velocity: 34 story points."
5. show-battery(value: 82, label: "Sprint 4 Completion")
```

**User:** Show me velocity over the last 3 sprints.

**Agent:**

```
1. get_sprints_metadata to find last 3 completed sprint IDs
2. get_sprint_summary for each sprint
3. show-chart(chartType: "bar", data: [{"label": "Sprint 2", "value": 28}, {"label": "Sprint 3", "value": 31}, {"label": "Sprint 4", "value": 34}])
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `get_sprint_summary` | Get completion stats for a finished sprint |
| `get_monday_dev_sprints_boards` | Find sprint/tasks board pairs |
| `get_sprints_metadata` | List sprints and their statuses |
| `board_insights` | Deep-dive into task-level sprint data |
| `show-chart` | Visualize velocity trends as bar charts |
| `show-battery` | Display sprint completion as a progress indicator |
| `show-table` | Show carryover items or detailed sprint breakdown |

## Common Pitfalls

- `get_sprint_summary` only works for completed sprints -- active sprints return partial data
- Velocity is measured in story points; boards without story point columns cannot compute velocity
- Carryover items (moved to next sprint) may be double-counted if not tracked carefully
- Sprint completion percentage is items-based by default, not story-point-weighted
- Historical sprint data depends on items retaining their sprint column values after completion

## See Also

- [monday-sprint-planning](../monday-sprint-planning/SKILL.md)
- [monday-board-insights](../monday-board-insights/SKILL.md)
- [monday-chart-visualization](../monday-chart-visualization/SKILL.md)
