---
name: monday-api-reference
description: Navigate the Monday.com GraphQL API with schema introspection, query building, pagination patterns, complexity budgets, and the all_monday_api escape hatch.
standards-version: 1.9.0
---

# Monday API Reference

## Trigger

- User asks how to call a specific Monday.com API endpoint
- User needs to build a custom GraphQL query or mutation
- User wants to understand rate limits or complexity budgets
- User needs to perform an operation not covered by dedicated MCP tools
- User asks about API authentication or versioning

## Required Inputs

- The operation the user wants to perform
- Whether it is a read (query) or write (mutation) operation

## Workflow

1. Use `get_graphql_schema` with `operationType: "read"` or `"write"` to browse available operations.
2. Use `get_type_details` to inspect a specific GraphQL type's fields and arguments.
3. Use `get_column_type_info` for column-specific schema details.
4. Build the query/mutation with proper arguments and requested fields.
5. Execute via `all_monday_api` with the `query` string and `variables` JSON string.
6. Parse the response, handling `errors` and `data` fields.

## Key References

- [API Overview](https://developer.monday.com/api-reference/)
- [GraphQL Introduction](https://developer.monday.com/api-reference/docs/introduction-to-graphql)
- [Rate Limits](https://developer.monday.com/api-reference/docs/rate-limits)
- [Complexity](https://developer.monday.com/api-reference/reference/complexity)
- [API Versioning](https://developer.monday.com/api-reference/docs/api-versioning)

## Example Interaction

**User:** I need to query all items on board 12345 that have status "Done" and get their names and timeline values.

**Agent:**

```
1. get_board_info(boardId: "12345") to find column IDs for status and timeline
2. Build query using items_page with column_values filter
3. all_monday_api(query: "query { boards(ids: [12345]) { items_page(limit: 50, query_params: {rules: [{column_id: \"status\", compare_value: [1]}]}) { items { id name column_values(ids: [\"timeline\"]) { id text } } } } }", variables: "{}")
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `get_graphql_schema` | Browse available queries and mutations |
| `get_type_details` | Inspect a specific GraphQL type |
| `get_column_type_info` | Get column type metadata and valid settings |
| `all_monday_api` | Execute any GraphQL query or mutation |

**Typical flow:**

```
get_graphql_schema(operationType: "read")
  -> identify the query/type you need
get_type_details(typeName: "Board")
  -> see available fields and arguments
all_monday_api(query: "...", variables: "{}")
  -> execute and get results
```

**Checking complexity budget:**

Add the `complexity` field to any query to see cost:
```graphql
query {
  complexity { before after reset_in_x_seconds }
  boards(ids: [12345]) { name }
}
```

## Common Pitfalls

- Monday.com API has a complexity budget of 10,000,000 points per minute (may vary by plan)
- Deeply nested queries (items -> subitems -> column_values) consume complexity rapidly
- Always request only the fields you need to minimize complexity cost
- The `variables` parameter in `all_monday_api` must be a JSON **string**, not an object
- API versions follow a `YYYY-MM` format; check current version for breaking changes
- Pagination: use `cursor`-based pagination with `items_page`, not offset-based `page`

## See Also

- [monday-column-types-guide](../monday-column-types-guide/SKILL.md)
- [monday-board-management](../monday-board-management/SKILL.md)
- [monday-item-operations](../monday-item-operations/SKILL.md)
