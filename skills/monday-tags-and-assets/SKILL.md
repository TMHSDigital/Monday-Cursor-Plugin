---
name: monday-tags-and-assets
description: Manage tags for item categorization and handle file/asset uploads, downloads, and organization on Monday.com.
standards-version: 1.6.3
---

# Monday Tags and Assets

## Trigger

- User wants to create, list, or assign tags to items
- User needs to upload files or assets to a board item
- User wants to download or list assets attached to items
- User asks about tag-based filtering or categorization
- User needs to manage file columns or asset storage

## Required Inputs

- Board ID and item ID for tag/asset operations
- Tag name(s) (for creation or assignment)
- File path or URL (for asset uploads)
- Tag column ID or file column ID

## Workflow

1. Use `get_board_info` to identify tag and file column IDs on the target board.
2. For tags:
   a. Use `all_monday_api` to query existing tags or create new ones.
   b. Assign tags to items via `change_item_column_values` with the tags column.
3. For assets:
   a. Use `all_monday_api` to list assets on an item.
   b. For uploads, use `all_monday_api` with the `add_file_to_column` mutation.
   c. For downloads, retrieve asset URLs from item column values.
4. For tag-based filtering, use `get_board_items_page` with tag column filters.

## Key References

- [Tags API](https://developer.monday.com/api-reference/reference/tags)
- [Assets API](https://developer.monday.com/api-reference/reference/file-assets)
- [File Column](https://developer.monday.com/api-reference/reference/column-types#file)

## Example Interaction

**User:** Add the tags "urgent" and "backend" to item 111222333.

**Agent:**

```
1. get_board_info(boardId: "...") to find the tags column ID (e.g., "tags")
2. all_monday_api:
   query { tags { id name } }
   to find existing tag IDs for "urgent" and "backend"
3. change_item_column_values(boardId: "...", itemId: "111222333", columnValues: "{\"tags\": {\"tag_ids\": [101, 102]}}")
```

**User:** What files are attached to this item?

**Agent:**

```
1. all_monday_api:
   query { items(ids: [111222333]) { assets { id name url file_extension file_size created_at } } }
2. Present: "2 files attached:
   - design-spec.pdf (1.2 MB, uploaded Mar 28)
   - screenshot.png (340 KB, uploaded Mar 29)"
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `all_monday_api` | All tag and asset operations -- query, create, upload, delete |
| `change_item_column_values` | Assign tags to items via the tags column |
| `get_board_info` | Find tag and file column IDs |
| `get_board_items_page` | Filter items by tag values |

**GraphQL recipes for tag operations:**

List all tags in the account:
```graphql
query { tags { id name color } }
```

Create a new tag (tags are created by assigning them):
```graphql
mutation { change_column_value(board_id: 1234567890, item_id: 111222333, column_id: "tags", value: "{\"tag_ids\": [101]}") { id } }
```

Create a tag via tag creation:
```graphql
mutation { create_or_get_tag(tag_name: "urgent") { id name } }
```

**GraphQL recipes for asset operations:**

List assets on an item:
```graphql
query { items(ids: [111222333]) { assets { id name url file_extension file_size created_at } } }
```

Upload a file to a file column (requires multipart form):
```graphql
mutation add_file($file: File!) { add_file_to_column(item_id: 111222333, column_id: "files", file: $file) { id name url } }
```

Delete an asset:
```graphql
mutation { delete_asset(asset_id: 9876543) { id } }
```

## Common Pitfalls

- Tags are account-wide, not board-scoped -- reuse existing tags when possible
- Tag column values use `{"tag_ids": [id1, id2]}` format -- setting tags replaces all existing tags
- To add a tag without removing existing ones, first read current tag IDs and include them
- File uploads via GraphQL require multipart form data -- not a standard JSON mutation
- Asset URLs are temporary signed URLs -- they expire and should not be stored long-term
- Large file uploads may timeout; check Monday.com's file size limits (currently 500 MB)
- The `files` column type is different from the `file` column type -- check `get_board_info`

## See Also

- [monday-item-operations](../monday-item-operations/SKILL.md)
- [monday-column-types-guide](../monday-column-types-guide/SKILL.md)
- [monday-api-reference](../monday-api-reference/SKILL.md)
