---
name: monday-webhook-management
description: Create, list, and delete Monday.com webhooks with challenge verification, JWT authentication, and event handling.
---

# Monday Webhook Management

## Trigger

- User wants to receive real-time notifications when board events occur
- User needs to set up a webhook for item changes, status updates, or column changes
- User asks about webhook authentication or challenge verification
- User wants to list or delete existing webhooks
- User needs to debug webhook delivery issues

## Required Inputs

- Board ID to subscribe to events on
- Webhook URL (the endpoint that will receive events)
- Event type to subscribe to (e.g., `change_column_value`, `create_item`)
- Optional: specific column ID to filter events

## Workflow

1. Ensure the webhook endpoint is publicly accessible and handles the challenge flow.
2. Use `all_monday_api` to create a webhook subscription with board ID, URL, and event type.
3. Monday.com sends a challenge request to the URL -- the endpoint must respond with the challenge token.
4. Use `all_monday_api` to list existing webhooks on the board for verification.
5. Test by triggering the subscribed event and checking webhook delivery.
6. Use `all_monday_api` to delete webhooks that are no longer needed.

## Key References

- [Webhooks API](https://developer.monday.com/api-reference/reference/webhooks)
- [Webhook Events](https://developer.monday.com/api-reference/reference/webhooks#supported-events)
- [Webhook Authentication](https://developer.monday.com/api-reference/reference/webhooks#authentication)

## Example Interaction

**User:** Set up a webhook to notify my server when items change status on board 1234567890.

**Agent:**

```
1. Verify the endpoint handles challenge verification:
   POST /webhook -> responds with { "challenge": "<received_token>" }
2. all_monday_api:
   mutation { create_webhook(board_id: 1234567890, url: "https://myserver.com/webhook", event: change_column_value, config: "{\"columnId\": \"status\"}") { id board_id } }
3. Monday sends challenge to the URL -- endpoint must respond correctly
4. Confirm: "Webhook created. Your server will receive POST requests when status changes on this board."
```

**User:** List all webhooks on this board.

**Agent:**

```
1. all_monday_api:
   query { webhooks(board_id: 1234567890) { id event board_id config } }
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `all_monday_api` | All webhook operations -- create, list, delete (no dedicated MCP tools) |
| `get_board_info` | Get column IDs for event filtering configuration |

**GraphQL recipes for webhook operations:**

Create a webhook:
```graphql
mutation { create_webhook(board_id: 1234567890, url: "https://example.com/hook", event: change_column_value, config: "{\"columnId\": \"status\"}") { id board_id } }
```

List webhooks on a board:
```graphql
query { webhooks(board_id: 1234567890) { id event board_id config } }
```

Delete a webhook:
```graphql
mutation { delete_webhook(id: 9876543) { id board_id } }
```

**Supported webhook events:**

| Event | Fires when |
|-------|-----------|
| `change_column_value` | Any column value changes (filterable by column ID) |
| `change_status_column_value` | Status column changes specifically |
| `change_subitem_column_value` | Subitem column value changes |
| `create_item` | New item is created |
| `delete_item` | Item is deleted |
| `create_update` | Update/comment is posted |

**Challenge verification (endpoint must implement):**

```json
// Incoming POST from Monday.com
{ "challenge": "abc123xyz" }

// Required response (200 OK)
{ "challenge": "abc123xyz" }
```

**JWT authentication (verify webhook signatures):**

Webhook payloads include a JWT in the `Authorization` header. Verify using your app's signing secret:
```
Authorization: Bearer <jwt_token>
```

## Common Pitfalls

- The webhook URL must be publicly accessible -- localhost will not work
- Challenge verification must respond within 5 seconds or the webhook creation fails
- JWT verification is required in production to prevent spoofed webhook events
- Webhook events are delivered at-least-once -- implement idempotency in your handler
- Column-specific filtering requires the column ID, not the column title
- Webhooks are board-scoped -- you need separate webhooks for each board
- Failed deliveries are retried with exponential backoff, then disabled after repeated failures

## See Also

- [monday-workflow-automation](../monday-workflow-automation/SKILL.md)
- [monday-api-reference](../monday-api-reference/SKILL.md)
- [monday-board-management](../monday-board-management/SKILL.md)
