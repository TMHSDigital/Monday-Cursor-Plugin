---
name: monday-column-types-guide
description: Deep reference for all Monday.com column types including value formats, creation settings, and common patterns for status, timeline, people, formula, mirror, and more.
---

# Monday Column Types Guide

## Trigger

- User needs to create a column of a specific type
- User is unsure how to format column values for `create_item` or `change_item_column_values`
- User asks about formula, mirror, or connect-boards columns
- User wants to understand column type capabilities

## Required Inputs

- Column type name (e.g., `status`, `timeline`, `people`, `date`)
- Board ID (when creating or inspecting columns)

## Workflow

1. Use `get_column_type_info` with the column type to see its schema, settings, and value format.
2. For existing boards, use `get_board_info` to see current columns and their IDs.
3. Use `create_column` to add a new column with the correct type and optional settings.
4. When setting values, format the JSON string according to the column type's specification.

## Key References

- [Column Types](https://developer.monday.com/api-reference/reference/columns)
- [Column Values v2](https://developer.monday.com/api-reference/reference/column-values-v2)

## Example Interaction

**User:** What's the correct JSON format for setting a timeline column value?

**Agent:** Timeline columns use start and end dates:

```json
{"timeline": {"from": "2026-03-01", "to": "2026-03-31"}}
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `get_column_type_info` | Get schema, settings, and value format for any column type |
| `get_board_info` | See existing columns on a board with their IDs and types |
| `create_column` | Create a new column on a board |
| `change_item_column_values` | Set column values on items |

## Column Value Quick Reference

| Column Type | JSON Format | Example |
|-------------|-------------|---------|
| `status` | `{"label": "..."}` | `{"status": {"label": "Done"}}` |
| `date` | `{"date": "YYYY-MM-DD"}` | `{"date4": {"date": "2026-03-30"}}` |
| `timeline` | `{"from": "...", "to": "..."}` | `{"timeline": {"from": "2026-03-01", "to": "2026-03-31"}}` |
| `people` | `{"personsAndTeams": [...]}` | `{"people": {"personsAndTeams": [{"id": 123, "kind": "person"}]}}` |
| `numbers` | Numeric value | `{"numbers": "42"}` |
| `text` | String value | `{"text0": "Hello"}` |
| `long_text` | `{"text": "..."}` | `{"long_text": {"text": "Detailed description"}}` |
| `checkbox` | `{"checked": "true"}` | `{"checkbox": {"checked": "true"}}` |
| `dropdown` | `{"labels": [...]}` | `{"dropdown": {"labels": ["Option A"]}}` |
| `email` | `{"email": "...", "text": "..."}` | `{"email": {"email": "a@b.com", "text": "Contact"}}` |
| `link` | `{"url": "...", "text": "..."}` | `{"link": {"url": "https://...", "text": "Link"}}` |
| `rating` | Rating value 1-5 | `{"rating": {"rating": 4}}` |
| `hour` | `{"hour": N, "minute": N}` | `{"hour": {"hour": 14, "minute": 30}}` |

## Common Pitfalls

- Column IDs are not the same as column titles; always fetch with `get_board_info` first
- The outer key in column values JSON is the **column ID**, not the column type
- Status labels must match exactly (case-sensitive) with configured label values
- People column requires both `id` and `kind` (`"person"` or `"team"`)
- Formula and mirror columns are read-only; you cannot set their values directly
- Connect-boards columns require the linked item's ID, not the board ID
- Numbers column values should be passed as strings, not integers

## See Also

- [monday-item-operations](../monday-item-operations/SKILL.md)
- [monday-board-management](../monday-board-management/SKILL.md)
- [monday-api-reference](../monday-api-reference/SKILL.md)
