---
name: monday-updates-and-communication
description: Post updates and replies on Monday.com items and boards, use mentions, and read update history for collaboration.
---

# Monday Updates and Communication

## Trigger

- User wants to post an update or comment on a board item
- User needs to reply to an existing update
- User wants to read the update history of an item or board
- User asks to mention specific users or teams in an update
- User needs to post a board-level announcement

## Required Inputs

- Item ID or board ID for the target update
- Update body text (supports Markdown-like formatting)
- User IDs for mentions (optional)
- Parent update ID (for replies)

## Workflow

1. Use `get_board_info` or `get_board_items_page` to find the target item if only a name is given.
2. Use `list_users_and_teams` to resolve user IDs for mentions.
3. Use `create_update` to post the update with the body text, item ID, and optional mentions.
4. For replies: use `get_updates` to find the parent update ID, then `create_update` with `parentUpdateId`.
5. To read history: use `get_updates` with the item ID or board ID and desired pagination.
6. Summarize update threads if the user asks for a digest.

## Key References

- [Updates API](https://developer.monday.com/api-reference/reference/updates)
- [Update Formatting](https://developer.monday.com/api-reference/reference/updates#body-formatting)

## Example Interaction

**User:** Post an update on item 111222333 saying "Deployment complete" and mention @john.

**Agent:**

```
1. list_users_and_teams() to find John's user ID (e.g., 54321)
2. create_update(itemId: "111222333", body: "Deployment complete <mention data-id=\"54321\">@John Smith</mention>")
```

**User:** Show me the last 5 updates on that item.

**Agent:**

```
1. get_updates(itemId: "111222333", limit: 5)
2. Present formatted update list with authors and timestamps
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `create_update` | Post a new update or reply on an item |
| `get_updates` | Read update history for an item or board |
| `list_users_and_teams` | Resolve user IDs for @mentions |
| `get_board_items_page` | Find item IDs by name before posting |
| `all_monday_api` | Delete updates, edit existing updates, like updates |

**GraphQL recipes for gap operations:**

Delete an update:
```graphql
mutation { delete_update(id: 1234567890) { id } }
```

Edit an existing update:
```graphql
mutation { edit_update(id: 1234567890, body: "Updated text here") { id } }
```

Like an update:
```graphql
mutation { like_update(update_id: 1234567890) { id } }
```

## Common Pitfalls

- Mentions use HTML-like syntax: `<mention data-id="USER_ID">@Display Name</mention>`
- Update body supports basic HTML formatting (bold, italic, lists) -- not full Markdown
- Board-level updates require the board ID, not an item ID
- `get_updates` returns newest first by default; use `limit` and `page` for pagination
- Updates cannot be moved between items -- delete and recreate if posted on the wrong item
- Rich text attachments (files, images) in updates require separate asset upload mutations

## See Also

- [monday-item-operations](../monday-item-operations/SKILL.md)
- [monday-notifications](../monday-notifications/SKILL.md)
- [monday-docs-management](../monday-docs-management/SKILL.md)
