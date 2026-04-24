---
name: monday-notifications
description: Send bell and email notifications to Monday.com users for alerts, reminders, and targeted communication.
standards-version: 1.6.3
---

# Monday Notifications

## Trigger

- User wants to notify someone about an item or event
- User needs to send a reminder or alert to a team member
- User asks to ping someone about a task
- User wants to send an email notification through Monday.com

## Required Inputs

- Target user ID (recipient of the notification)
- Item ID (the item the notification relates to)
- Notification text (the message content)
- Notification type: `bell` (in-app) or `email`

## Workflow

1. Use `list_users_and_teams` to find the target user's ID if only a name is provided.
2. Use `get_board_items_page` or `search` to find the relevant item ID if needed.
3. Use `create_notification` with the user ID, item ID, notification text, and type.
4. Confirm the notification was sent.

## Key References

- [Notifications API](https://developer.monday.com/api-reference/reference/notifications)

## Example Interaction

**User:** Notify Sarah that the "API Migration" task needs her review.

**Agent:**

```
1. list_users_and_teams() to find Sarah's user ID (e.g., 67890)
2. search(searchTerm: "API Migration") to find the item ID
3. create_notification(userId: "67890", itemId: "...", text: "This task needs your review", notificationType: "bell")
```

**User:** Send an email notification to the whole team about the deadline change.

**Agent:**

```
1. list_users_and_teams() to get team member IDs
2. For each team member:
   create_notification(userId: "...", itemId: "...", text: "Deadline has been moved to April 15", notificationType: "email")
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `create_notification` | Send a bell or email notification to a user |
| `list_users_and_teams` | Resolve user names to IDs for targeting |
| `search` | Find item IDs to associate with notifications |
| `get_board_items_page` | Find items when search is ambiguous |

## Common Pitfalls

- Notifications require a valid item ID -- you cannot send a notification without an item context
- Email notifications are rate-limited; avoid bulk sends to large teams in rapid succession
- Bell notifications appear in the user's Monday.com notification center
- Notification text is plain text -- HTML or Markdown formatting is not rendered
- Users can mute notifications per board; muted users will not see bell notifications
- Only account admins can send notifications on behalf of other users

## See Also

- [monday-updates-and-communication](../monday-updates-and-communication/SKILL.md)
- [monday-user-and-team-management](../monday-user-and-team-management/SKILL.md)
- [monday-item-operations](../monday-item-operations/SKILL.md)
