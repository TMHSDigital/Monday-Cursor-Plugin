---
name: monday-user-and-team-management
description: Manage Monday.com users and teams including lookups, permissions, team membership, and current user context.
---

# Monday User and Team Management

## Trigger

- User wants to look up users or teams
- User needs their own user context (ID, favorites, recent boards)
- User wants to find team members for assignment
- User asks about user roles or permissions
- User needs to assign people to items or boards

## Required Inputs

- User IDs, team IDs, or name (for lookups)
- Context about what user data is needed

## Workflow

1. Use `get_user_context` to get the current authenticated user and their favorites/recent boards.
2. Use `list_users_and_teams` with the appropriate filters:
   - `getMe: true` for current user details
   - `userIds` for specific users
   - `name` for user name search
   - `teamIds` for specific teams
   - `teamsOnly: true` for teams only
   - `includeTeamMembers: true` to expand team membership
3. For assigning users to items, use the user ID with `change_item_column_values` on a people column.
4. For board-level user operations (owners, subscribers), use `all_monday_api`.

## Key References

- [Users API](https://developer.monday.com/api-reference/reference/users)
- [Teams API](https://developer.monday.com/api-reference/reference/teams)

## Example Interaction

**User:** Who's on the Design team? I want to assign the new task to one of them.

**Agent:**

```
1. list_users_and_teams(name: "Design", teamsOnly: true, includeTeamMembers: true)
2. Present team members to user
3. change_item_column_values(boardId: "...", itemId: "...", columnValues: "{\"people\": {\"personsAndTeams\": [{\"id\": SELECTED_USER_ID, \"kind\": \"person\"}]}}")
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `get_user_context` | Get current user info, favorites, and recent boards |
| `list_users_and_teams` | Look up users by ID/name, teams by ID, or browse all |
| `change_item_column_values` | Assign users to items via people columns |
| `show-assign` | Render interactive assignment UI widget |
| `all_monday_api` | Add/remove board subscribers, query user details not exposed by MCP |

**Priority order for `list_users_and_teams`:**

The tool resolves users in this priority:
1. `getMe: true` (current user)
2. `userIds` (specific user IDs)
3. `name` (search by name -- users only)
4. `teamIds` + `teamsOnly` (specific teams)
5. No params (all users -- use sparingly)

## Common Pitfalls

- `list_users_and_teams` name search only works for users, not teams
- Team IDs require `includeTeamMembers: true` to see individual members
- User IDs in people column values must be numbers, not strings
- The `show-assign` UI tool requires structured assignment data; fetch user info first
- Board subscriber operations are not available via dedicated MCP tools; use `all_monday_api`

## See Also

- [monday-item-operations](../monday-item-operations/SKILL.md)
- [monday-resource-management](../monday-resource-management/SKILL.md)
- [monday-board-management](../monday-board-management/SKILL.md)
