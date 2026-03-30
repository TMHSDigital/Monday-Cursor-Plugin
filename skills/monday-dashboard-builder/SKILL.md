---
name: monday-dashboard-builder
description: Create dashboards, add widgets, configure chart types, and connect boards to build reporting views in Monday.com.
---

# Monday Dashboard Builder

## Trigger

- User wants to create a new dashboard
- User needs to add widgets (charts, tables, numbers) to a dashboard
- User asks to visualize board data in a reporting view
- User wants to connect multiple boards to a single dashboard
- User needs to configure widget settings or chart types

## Required Inputs

- Dashboard name (for creation)
- Dashboard ID (for adding widgets)
- Board ID(s) to connect as data sources
- Widget type and configuration (chart type, columns, grouping)

## Workflow

1. Use `list_workspaces` or `search` to find the target workspace for the dashboard.
2. Use `create_dashboard` with a name and optional description.
3. Use `all_widgets_schema` to discover available widget types and their configuration schemas.
4. Use `get_board_info` on each source board to identify column IDs for widget data mapping.
5. Use `create_widget` to add widgets to the dashboard, specifying board ID, widget type, and settings.
6. Repeat step 5 for each widget needed.
7. Confirm the dashboard by sharing the dashboard URL with the user.

## Key References

- [Dashboards API](https://developer.monday.com/api-reference/reference/dashboards)
- [Widgets API](https://developer.monday.com/api-reference/reference/dashboard-widgets)

## Example Interaction

**User:** Create a dashboard called "Q2 Sprint Overview" with a status breakdown chart from board 1234567890.

**Agent:**

```
1. create_dashboard(name: "Q2 Sprint Overview", description: "Sprint metrics for Q2")
2. all_widgets_schema() to find chart widget schema
3. get_board_info(boardId: "1234567890") to get status column ID
4. create_widget(dashboardId: "...", widgetType: "chart", boardIds: ["1234567890"], settings: {"column_id": "status", "chart_type": "pie"})
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `create_dashboard` | Create a new dashboard in a workspace |
| `create_widget` | Add a widget to a dashboard or board view |
| `all_widgets_schema` | Discover widget types and their JSON config schemas |
| `get_board_info` | Get column IDs and structure for widget data mapping |
| `search` | Find existing dashboards or boards to connect |
| `all_monday_api` | Delete dashboards, update dashboard attributes |

**GraphQL recipes for gap operations:**

Delete a dashboard:
```graphql
mutation { delete_board(board_id: 1234567890) { id } }
```

Query existing dashboards in a workspace:
```graphql
query { boards(workspace_ids: [123], board_kind: public, order_by: created_at) { id name board_kind } }
```

## Common Pitfalls

- Dashboard creation returns an ID -- save it before adding widgets
- Widget settings schemas vary per widget type; always check `all_widgets_schema` first
- Board IDs passed to `create_widget` must be accessible by the dashboard owner
- Chart widgets require a valid column ID from the source board as the data axis
- Number widgets need an aggregation function (SUM, AVG, COUNT, etc.)
- Dashboards are workspace-scoped; users outside the workspace cannot see them

## See Also

- [monday-board-insights](../monday-board-insights/SKILL.md)
- [monday-chart-visualization](../monday-chart-visualization/SKILL.md)
- [monday-board-management](../monday-board-management/SKILL.md)
