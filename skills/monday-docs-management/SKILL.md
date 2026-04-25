---
name: monday-docs-management
description: Create, read, and append content to Monday Docs; manage version history and doc structure within workspaces.
standards-version: 1.7.0
---

# Monday Docs Management

## Trigger

- User wants to create a new Monday Doc
- User needs to read or view doc content
- User wants to add or append content to an existing doc
- User asks about doc version history
- User wants to attach a doc to an item or workspace

## Required Inputs

- Doc title (for creation)
- Workspace ID or item ID (for doc placement)
- Doc ID (for reading or appending)
- Content body in Markdown format (for appending)

## Workflow

1. Use `search` to find an existing doc by name, or `workspace_info` to list docs in a workspace.
2. For creation: use `create_doc` with a title and optional workspace or item attachment.
3. For reading: use `read_docs` with the doc ID to get content and metadata.
4. For appending: use `add_content_to_doc` with the doc ID and Markdown-formatted content.
5. For version history: use `read_docs` with version history options to see past revisions.
6. Confirm the result and share the doc link.

## Key References

- [Docs API](https://developer.monday.com/api-reference/reference/docs)
- [Monday Docs](https://support.monday.com/hc/en-us/articles/360002190259-monday-Docs)

## Example Interaction

**User:** Create a meeting notes doc in the "Product" workspace and add today's agenda.

**Agent:**

```
1. list_workspaces() to find "Product" workspace ID
2. create_doc(title: "Meeting Notes -- 2026-03-30", workspaceId: "...")
3. add_content_to_doc(docId: "...", content: "## Agenda\n\n- Review sprint progress\n- Discuss Q2 goals\n- Action items")
```

**User:** What's in our design spec doc?

**Agent:**

```
1. search(searchTerm: "design spec", searchType: "DOC")
2. read_docs(docId: "...")
3. Present doc content summary
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `create_doc` | Create a new doc in a workspace or attached to an item |
| `read_docs` | Read doc content or version history |
| `add_content_to_doc` | Append Markdown content to an existing doc |
| `search` | Find docs by name |
| `workspace_info` | List all docs in a workspace |
| `all_monday_api` | Delete docs, update doc settings |

**GraphQL recipes for gap operations:**

Delete a doc:
```graphql
mutation { delete_doc(doc_id: 1234567890) { id } }
```

List docs for a workspace:
```graphql
query { docs(workspace_ids: [123], limit: 25) { id title created_at created_by { name } } }
```

## Common Pitfalls

- `add_content_to_doc` appends content -- it does not replace existing content
- Doc content is Markdown-based but supports only a subset of Markdown syntax
- Docs attached to items appear in the item's "Files" or "Docs" view, not as standalone
- Version history retrieval may return large payloads for frequently edited docs
- Doc permissions inherit from the workspace unless explicitly overridden
- Search results for docs may include archived docs -- filter by status if needed

## See Also

- [monday-updates-and-communication](../monday-updates-and-communication/SKILL.md)
- [monday-workspace-organizer](../monday-workspace-organizer/SKILL.md)
- [monday-notetaker-meetings](../monday-notetaker-meetings/SKILL.md)
