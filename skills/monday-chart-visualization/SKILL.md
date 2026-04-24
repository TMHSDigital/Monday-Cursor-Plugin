---
name: monday-chart-visualization
description: Render pie charts, bar charts, battery/progress widgets, and interactive tables from Monday.com board data.
standards-version: 1.6.3
---

# Monday Chart Visualization

## Trigger

- User asks to visualize board data as a chart
- User wants a pie chart, bar chart, or progress indicator
- User needs to display board data in an interactive table
- User asks for a visual status breakdown or progress overview

## Required Inputs

- Board ID or data source for the visualization
- Chart type: `pie`, `bar`, `battery`, or `table`
- Column(s) to visualize (e.g., status column for pie, numbers column for bar)
- Optional: grouping, filtering, labels

## Workflow

1. Use `get_board_info` to identify column IDs and types for the target board.
2. Use `board_insights` or `get_board_items_page` to gather the data to visualize.
3. Choose the appropriate rendering tool:
   - `show-chart` for pie and bar charts
   - `show-battery` for progress/battery indicators
   - `show-table` for interactive tabular views
4. Pass the structured data and configuration to the rendering tool.
5. Present the rendered visualization to the user.

## Key References

- [Monday Views](https://developer.monday.com/api-reference/reference/views)
- [Chart Widget Types](https://developer.monday.com/api-reference/reference/dashboard-widgets)

## Example Interaction

**User:** Show me a pie chart of task statuses on board 9876543210.

**Agent:**

```
1. get_board_info(boardId: "9876543210") to find status column ID
2. board_insights(boardId: "9876543210", question: "Count of items by status")
3. show-chart(chartType: "pie", data: [{"label": "Done", "value": 15}, {"label": "Working on it", "value": 8}, {"label": "Stuck", "value": 3}])
```

**User:** What's the sprint completion percentage?

**Agent:**

```
1. board_insights(boardId: "...", question: "Percentage of items with status Done")
2. show-battery(value: 65, label: "Sprint Completion")
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `show-chart` | Render pie or bar charts from aggregated data |
| `show-battery` | Render battery/progress indicators (percentage-based) |
| `show-table` | Render interactive board data tables |
| `board_insights` | Aggregate data before charting |
| `get_board_items_page` | Get raw item data for custom visualizations |
| `get_board_info` | Identify columns and data types for chart axis mapping |

## Common Pitfalls

- `show-chart` expects pre-aggregated data -- aggregate with `board_insights` first, don't pass raw items
- Battery widgets display a single percentage value (0--100), not multiple data points
- Table rendering may truncate at high item counts; paginate data for large boards
- Pie charts work best with categorical data (status, labels); bar charts suit numerical comparisons
- Color mapping follows Monday's status label colors by default
- Charts are rendered in the IDE, not persisted on the Monday.com platform

## See Also

- [monday-board-insights](../monday-board-insights/SKILL.md)
- [monday-dashboard-builder](../monday-dashboard-builder/SKILL.md)
- [monday-project-tracking](../monday-project-tracking/SKILL.md)
