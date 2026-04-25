---
name: monday-board-management
description: Create, configure, manage, duplicate, archive, and delete Monday.com boards including columns, groups, views, and permissions.
standards-version: 1.7.0
---

# Monday Board Management

## Trigger

- User wants to create a new board
- User needs to add, modify, or delete columns or groups
- User wants to duplicate, archive, or delete a board
- User asks about board permissions or structure
- User needs to configure board views or settings

## Required Inputs

- Board name (for creation) or board ID (for modification)
- Board kind: `public`, `private`, or `share`
- Workspace ID (optional, defaults to Main workspace)
- Column definitions: type + title for each column

## Workflow

1. If the target board is unknown, use `search` (searchType: `BOARD`) to find it, or `get_user_context` for recently accessed boards.
2. Use `get_board_info` to inspect current board structure (columns, groups, views, owners).
3. For creation: use `create_board` with name, kind, optional workspace/folder.
4. For columns: use `create_column` with board ID, column type, and title. Check `get_column_type_info` for valid types and settings.
5. For groups: use `create_group` with board ID and group name.
6. For operations not covered by dedicated MCP tools (duplicate, archive, delete, permissions, delete groups/columns), use `all_monday_api` with the appropriate GraphQL mutation.
7. Confirm the result by re-fetching board info.

## Key References

- [Boards API](https://developer.monday.com/api-reference/reference/boards)
- [Columns API](https://developer.monday.com/api-reference/reference/columns)
- [Groups API](https://developer.monday.com/api-reference/reference/groups)

## Example Interaction

**User:** Create a project tracking board with status, timeline, and person columns in my "Engineering" workspace.

**Agent:**

```
1. search for "Engineering" workspace via list_workspaces
2. create_board(boardName: "Project Tracking", boardKind: "public", workspaceId: "...")
3. create_column(boardId: "...", columnType: "status", columnTitle: "Status")
4. create_column(boardId: "...", columnType: "timeline", columnTitle: "Timeline")
5. create_column(boardId: "...", columnType: "people", columnTitle: "Owner")
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `create_board` | Create a new board |
| `create_group` | Add a group to a board |
| `create_column` | Add a column to a board |
| `get_board_info` | Inspect board structure, columns, groups, views |
| `get_column_type_info` | Look up column type schema before creating |
| `search` | Find boards by name |
| `all_monday_api` | Archive, delete, duplicate boards; set permissions; delete groups/columns |

**GraphQL recipes for gap operations:**

Archive a board:
```graphql
mutation { archive_board(board_id: 1234567890) { id } }
```

Delete a board:
```graphql
mutation { delete_board(board_id: 1234567890) { id } }
```

Duplicate a board:
```graphql
mutation { duplicate_board(board_id: 1234567890, duplicate_type: duplicate_board_with_structure) { board { id } } }
```

Set board permissions:
```graphql
mutation { set_board_permission(board_id: 1234567890, basic_role_name: viewer) { edit_permissions } }
```

## Common Pitfalls

- `create_board` has a rate limit of 40 mutations per minute
- `duplicate_board` is asynchronous and may return partial data initially
- Board permissions mutation requires Enterprise plan and board owner role
- Column type names are specific enums (e.g., `status`, `timeline`, `people`, not `person`)
- When creating columns, use `get_column_type_info` to get valid `columnSettings` JSON

## See Also

- [monday-item-operations](../monday-item-operations/SKILL.md)
- [monday-column-types-guide](../monday-column-types-guide/SKILL.md)
- [monday-workspace-organizer](../monday-workspace-organizer/SKILL.md)
