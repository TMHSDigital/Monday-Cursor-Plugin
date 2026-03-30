---
name: monday-resource-management
description: Manage team assignments, workload distribution, and capacity planning across Monday.com boards and projects.
---

# Monday Resource Management

## Trigger

- User wants to see who is assigned to what tasks
- User asks about team workload or capacity
- User needs to balance work across team members
- User wants to assign or reassign resources to tasks
- User asks about over-allocated or under-utilized team members

## Required Inputs

- Board ID or project name
- Team or user names/IDs for workload analysis
- Person column ID (for assignment queries)
- Optional: date range for capacity analysis

## Workflow

1. Use `list_users_and_teams` to get team member details and IDs.
2. Use `get_board_info` to identify person and timeline columns on the project board.
3. Use `board_insights` to analyze workload distribution (tasks per person, status breakdown by assignee).
4. Use `get_board_items_page` to get detailed assignment data with filters.
5. Use `show-assign` to render an assignment view showing who owns what.
6. For reassignment: use `change_item_column_values` to update person column values.
7. For capacity planning: cross-reference assignments with timeline data to detect overallocation.

## Key References

- [People Column](https://developer.monday.com/api-reference/reference/column-types#people)
- [Workload View](https://support.monday.com/hc/en-us/articles/360002254779-Workload-View)

## Example Interaction

**User:** Who has the most tasks on the "Q2 Development" board?

**Agent:**

```
1. search(searchTerm: "Q2 Development", searchType: "BOARD")
2. board_insights(boardId: "...", question: "Number of items assigned to each person")
3. show-chart(chartType: "bar", data: [{"label": "Alex", "value": 12}, {"label": "Sarah", "value": 8}, {"label": "Mike", "value": 15}])
4. Present: "Mike has the most tasks (15). Consider reassigning some to Sarah (8 tasks)."
```

**User:** Reassign 3 of Mike's tasks to Sarah.

**Agent:**

```
1. get_board_items_page(boardId: "...", filters for Mike's items, limit: 3)
2. For each item:
   change_item_column_values(boardId: "...", itemId: "...", columnValues: "{\"person\": {\"personsAndTeams\": [{\"id\": SARAH_ID, \"kind\": \"person\"}]}}")
3. Confirm: "3 tasks reassigned from Mike to Sarah."
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `show-assign` | Render assignment UI showing team member allocations |
| `list_users_and_teams` | Get user IDs and team membership |
| `board_insights` | Analyze workload distribution and task counts per person |
| `get_board_items_page` | Query items filtered by assignee |
| `change_item_column_values` | Assign or reassign people to items |
| `get_board_info` | Identify person and timeline columns |
| `show-chart` | Visualize workload distribution across team |

**GraphQL recipes for gap operations:**

Get items assigned to a specific person:
```graphql
query { boards(ids: [1234567890]) { items_page(limit: 50, query_params: {rules: [{column_id: "person", compare_value: [12345]}]}) { items { id name column_values(ids: ["person", "status", "timeline"]) { value } } } } }
```

Get all people column values:
```graphql
query { boards(ids: [1234567890]) { items_page(limit: 200) { items { id name column_values(ids: ["person"]) { value } } } } }
```

## Common Pitfalls

- Person column values use `{"personsAndTeams": [{"id": ..., "kind": "person|team"}]}` format
- Reassigning clears the previous assignee unless you include both old and new in the array
- Workload view calculations depend on timeline + effort/story points columns being populated
- Teams and persons are different kinds -- filter accordingly when querying
- Capacity planning requires both assignment data and timeline data to be meaningful
- Cross-board workload analysis requires querying multiple boards and aggregating manually

## See Also

- [monday-project-tracking](../monday-project-tracking/SKILL.md)
- [monday-user-and-team-management](../monday-user-and-team-management/SKILL.md)
- [monday-board-insights](../monday-board-insights/SKILL.md)
