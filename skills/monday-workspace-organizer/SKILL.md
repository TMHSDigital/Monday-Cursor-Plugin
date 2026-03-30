---
name: monday-workspace-organizer
description: Organize Monday.com workspaces, folders, and board hierarchy for clean project structure.
---

# Monday Workspace Organizer

## Trigger

- User wants to create or configure a workspace
- User needs to organize boards into folders
- User wants to move boards, folders, or dashboards between workspaces
- User asks about workspace structure or contents

## Required Inputs

- Workspace name or ID
- Folder name (for creation)
- Object type and ID (for move operations)

## Workflow

1. Use `list_workspaces` to see existing workspaces (supports search and pagination).
2. Use `workspace_info` to see boards, docs, and folders within a specific workspace.
3. For creation: use `create_workspace` with name and kind (`open`, `closed`, or `template`).
4. For folders: use `create_folder` with workspace ID, name, and optional parent folder.
5. For updates: use `update_workspace` or `update_folder` to rename, recolor, or restructure.
6. For moving objects: use `move_object` with object type (`Board`, `Folder`, or `Overview`), ID, and destination.

## Key References

- [Workspaces API](https://developer.monday.com/api-reference/reference/workspaces)
- [Folders API](https://developer.monday.com/api-reference/reference/folders)

## Example Interaction

**User:** Create an "Engineering" workspace with "Frontend" and "Backend" folders, then move board 12345 into the Frontend folder.

**Agent:**

```
1. create_workspace(name: "Engineering", workspaceKind: "open")
2. create_folder(workspaceId: "...", name: "Frontend")
3. create_folder(workspaceId: "...", name: "Backend")
4. move_object(objectType: "Board", id: "12345", parentFolderId: "...", workspaceId: "...")
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `list_workspaces` | List or search workspaces |
| `workspace_info` | View boards, docs, folders in a workspace |
| `create_workspace` | Create a new workspace |
| `update_workspace` | Rename, change kind, or update description |
| `create_folder` | Create a folder within a workspace |
| `update_folder` | Rename, recolor, reposition, or reparent a folder |
| `move_object` | Move boards, folders, or overviews between locations |

## Common Pitfalls

- `workspace_info` returns up to 100 of each object type; if you get exactly 100, there are likely more
- The Main workspace has no workspace ID (returns `null` in API responses)
- Folder colors are enums like `BRIGHT_BLUE`, `DONE_GREEN`, not hex values
- Moving a board to another workspace also requires specifying a folder within that workspace

## See Also

- [monday-board-management](../monday-board-management/SKILL.md)
- [monday-dashboard-builder](../monday-dashboard-builder/SKILL.md)
