---
name: monday-item-operations
description: Create, update, move, archive, and delete Monday.com items and subitems across boards and groups.
standards-version: 1.6.3
---

# Monday Item Operations

## Trigger

- User wants to create items or subitems on a board
- User needs to update column values on existing items
- User wants to move items between groups or boards
- User needs to archive or delete items
- User asks to query or filter items

## Required Inputs

- Board ID (always required)
- Item name (for creation)
- Column values as JSON string (for creation or update)
- Item ID (for update, move, delete operations)

## Workflow

1. Use `get_board_info` to understand board structure (column IDs, group IDs).
2. Use `get_column_type_info` if unsure about column value JSON format.
3. For querying: use `get_board_items_page` with optional filters, search terms, or specific item IDs.
4. For creation: use `create_item` with board ID, name, and column values JSON.
5. For subitems: use `create_item` with `parentItemId` set to the parent item's ID.
6. For updates: use `change_item_column_values` with board ID, item ID, and column values JSON.
7. For move/archive/delete: use `all_monday_api` with the appropriate mutation.

## Key References

- [Items API](https://developer.monday.com/api-reference/reference/items)
- [Subitems API](https://developer.monday.com/api-reference/reference/subitems)
- [Column Values](https://developer.monday.com/api-reference/reference/column-values-v2)

## Example Interaction

**User:** Add a new task "Fix login bug" with status "Working on it" and assign it to me.

**Agent:**

```
1. get_board_info(boardId: "...") to find column IDs for status and people
2. get_user_context() to get current user ID
3. create_item(boardId: "...", name: "Fix login bug", columnValues: "{\"status\": {\"label\": \"Working on it\"}, \"people\": {\"personsAndTeams\": [{\"id\": 12345, \"kind\": \"person\"}]}}")
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `create_item` | Create items, subitems, or duplicate from existing |
| `change_item_column_values` | Update column values on an existing item |
| `get_board_items_page` | Query items with filters, pagination, search |
| `get_board_info` | Get column IDs and group IDs before item operations |
| `get_column_type_info` | Understand column value JSON format |
| `all_monday_api` | Delete, archive, move items between groups/boards |

**GraphQL recipes for gap operations:**

Delete an item:
```graphql
mutation { delete_item(item_id: 1234567890) { id } }
```

Archive an item:
```graphql
mutation { archive_item(item_id: 1234567890) { id } }
```

Move item to another group:
```graphql
mutation { move_item_to_group(item_id: 1234567890, group_id: "new_group") { id } }
```

Move item to another board:
```graphql
mutation { move_item_to_board(board_id: 9876543210, group_id: "topics", item_id: 1234567890) { id } }
```

## Common Pitfalls

- Column values must be a JSON **string**, not a JSON object -- stringify before passing
- Status columns use `{"label": "Done"}` format, not index-based values
- People columns require `{"personsAndTeams": [{"id": ..., "kind": "person"}]}`
- Date columns use `{"date": "2026-03-30"}` format (ISO 8601)
- When filtering items, call `get_board_info` first to get `boardContextToken` for filter configuration
- Subitem creation requires the parent item's board ID, not the subitems board ID

## See Also

- [monday-board-management](../monday-board-management/SKILL.md)
- [monday-column-types-guide](../monday-column-types-guide/SKILL.md)
- [monday-board-insights](../monday-board-insights/SKILL.md)
