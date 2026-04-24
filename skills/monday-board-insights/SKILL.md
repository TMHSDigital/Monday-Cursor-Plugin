---
name: monday-board-insights
description: Aggregate, filter, and analyze Monday.com board data for reporting, summaries, and decision-making.
standards-version: 1.6.3
---

# Monday Board Insights

## Trigger

- User wants a summary or report of board data
- User asks how many items are in a specific status
- User needs aggregated metrics (counts, averages, totals) from a board
- User wants to filter or segment board data
- User asks "how is the project going?" or similar status questions

## Required Inputs

- Board ID or board name to analyze
- Analysis question or metric of interest (e.g., "items by status", "overdue tasks")
- Optional: specific group, column, or filter criteria

## Workflow

1. Use `search` or `get_user_context` to find the target board if only a name is provided.
2. Use `get_board_info` to understand board structure (columns, groups).
3. Use `board_insights` with a natural language question to get aggregated data.
4. If deeper drill-down is needed, use `get_board_items_page` with filters to get raw item data.
5. Present results in a clear format -- use `show-table` or `show-chart` for visual output.
6. Offer follow-up analysis or export options.

## Key References

- [Board Insights](https://developer.monday.com/api-reference/reference/boards#board-insights)
- [Items Page](https://developer.monday.com/api-reference/reference/items-page)

## Example Interaction

**User:** How many tasks on the "Product Roadmap" board are overdue?

**Agent:**

```
1. search(searchTerm: "Product Roadmap", searchType: "BOARD") to get board ID
2. board_insights(boardId: "...", question: "How many items have a timeline end date before today?")
3. Present: "12 items are currently overdue. Here's the breakdown by group..."
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `board_insights` | Ask natural language questions about board data aggregations |
| `get_board_items_page` | Retrieve filtered/paginated items for detailed analysis |
| `get_board_info` | Understand board schema before querying |
| `search` | Find boards by name |
| `show-chart` | Visualize insight results as charts |
| `show-table` | Display insight results as a table |

**GraphQL recipes for gap operations:**

Get item count by group:
```graphql
query { boards(ids: [1234567890]) { groups { id title items_page(limit: 0) { cursor } } } }
```

Get items with specific status:
```graphql
query { boards(ids: [1234567890]) { items_page(limit: 50, query_params: {rules: [{column_id: "status", compare_value: ["Done"]}]}) { items { id name } } } }
```

## Common Pitfalls

- `board_insights` works best with clear, specific questions -- vague queries return vague results
- For boards with 10,000+ items, `board_insights` is faster than paginating all items manually
- Filters in `get_board_items_page` use column IDs, not column titles -- check `get_board_info` first
- Date comparisons depend on the board's timezone setting
- Subitem data is on a separate board; ask about subitems explicitly if needed

## See Also

- [monday-dashboard-builder](../monday-dashboard-builder/SKILL.md)
- [monday-chart-visualization](../monday-chart-visualization/SKILL.md)
- [monday-item-operations](../monday-item-operations/SKILL.md)
