---
name: monday-workflow-automation
description: Create and manage Monday.com automation recipes with triggers, conditions, and actions for workflow automation.
standards-version: 1.9.0
---

# Monday Workflow Automation

## Trigger

- User wants to automate a workflow on a board
- User asks to set up "when X happens, do Y" rules
- User needs to create, list, or delete automation recipes
- User wants to configure triggers, conditions, or actions
- User asks about available automation templates

## Required Inputs

- Board ID where the automation will be applied
- Trigger type (e.g., status change, date arrived, item created)
- Action type (e.g., notify, move item, create update)
- Conditions (optional filters for when the automation fires)

## Workflow

1. Use `get_board_info` to understand the board structure and column IDs.
2. Use `all_monday_api` to query available automation recipes and templates.
3. Construct the automation recipe with trigger, optional conditions, and actions.
4. Use `all_monday_api` to create the automation via GraphQL mutation.
5. Verify the automation was created by listing board automations.
6. Test by performing the trigger action on a test item.

## Key References

- [Automations API](https://developer.monday.com/api-reference/reference/automations)
- [Custom Automations](https://support.monday.com/hc/en-us/articles/360002249179-Board-Automations)
- [Automation Recipes](https://support.monday.com/hc/en-us/articles/360002249179)

## Example Interaction

**User:** When a task status changes to "Done", notify the project manager.

**Agent:**

```
1. get_board_info(boardId: "...") to get status column ID and verify structure
2. list_users_and_teams() to find project manager's user ID
3. all_monday_api with mutation to create automation:
   - Trigger: status column changes to "Done"
   - Action: send notification to user ID
4. Confirm: "Automation created. When any item's status changes to Done, the PM will get a notification."
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `all_monday_api` | Create, list, update, and delete automation recipes (no dedicated tools) |
| `get_board_info` | Get column IDs for trigger/condition configuration |
| `list_users_and_teams` | Resolve user IDs for notification actions |
| `get_column_type_info` | Understand column value formats for conditions |

**GraphQL recipes for automation operations:**

List automations on a board:
```graphql
query { boards(ids: [1234567890]) { automations { id is_active trigger { output_column_ids type } actions { type } } } }
```

Create a status-change automation:
```graphql
mutation { create_automation(board_id: 1234567890, automation: {trigger: {type: "status_change", config: {columnId: "status", value: "Done"}}, actions: [{type: "notify", config: {userId: 54321, text: "Task completed"}}]}) { id } }
```

Enable or disable an automation:
```graphql
mutation { update_automation(board_id: 1234567890, automation_id: 9876, attribute: is_active, value: "false") { id is_active } }
```

Delete an automation:
```graphql
mutation { delete_automation(board_id: 1234567890, automation_id: 9876) { id } }
```

## Common Pitfalls

- Automation API availability depends on your Monday.com plan (Pro or Enterprise)
- Automations are board-scoped -- they cannot span multiple boards natively
- Complex conditions with multiple AND/OR clauses may require custom integrations
- Automation triggers fire for all matching changes, including API-driven updates
- Recursive automations (action triggers another automation) can create infinite loops
- Rate limits apply to actions triggered by automations -- batch operations may be throttled
- Test automations on a non-production board first to avoid unintended side effects

## See Also

- [monday-webhook-management](../monday-webhook-management/SKILL.md)
- [monday-board-management](../monday-board-management/SKILL.md)
- [monday-notifications](../monday-notifications/SKILL.md)
