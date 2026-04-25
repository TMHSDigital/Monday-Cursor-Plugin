---
name: monday-form-builder
description: Create Monday.com forms with questions, conditional logic, and response boards for data collection and intake workflows.
standards-version: 1.7.0
---

# Monday Form Builder

## Trigger

- User wants to create a form for data collection
- User needs to add, update, or delete form questions
- User asks to configure conditional logic on form questions
- User wants to update form settings or appearance
- User needs to view or manage an existing form

## Required Inputs

- Form name and description (for creation)
- Board ID to connect as the response destination
- Question definitions: type, title, required flag
- Form token (for updating or viewing existing forms)

## Workflow

1. Use `get_board_info` to check if a response board exists, or use `create_board` to create one.
2. Use `create_form` with the form name, description, and linked board ID.
3. Use `form_questions_editor` to add questions -- map each question to a board column.
4. Use `update_form` to configure form settings (appearance, submission message, redirect URL).
5. For conditional logic: use `form_questions_editor` with condition rules on question visibility.
6. Use `get_form` to retrieve the form URL and verify the configuration.

## Key References

- [Monday Forms](https://support.monday.com/hc/en-us/articles/360013378579-monday-com-Forms)
- [Forms API](https://developer.monday.com/api-reference/reference/forms)

## Example Interaction

**User:** Create a bug report form that feeds into our "Bug Tracker" board.

**Agent:**

```
1. search(searchTerm: "Bug Tracker", searchType: "BOARD") to find board ID
2. get_board_info(boardId: "...") to see existing columns
3. create_form(name: "Bug Report", boardId: "...", description: "Submit a bug report")
4. form_questions_editor(formToken: "...", action: "create", questions: [
     {title: "Bug Title", type: "text", required: true, columnId: "name"},
     {title: "Severity", type: "dropdown", required: true, columnId: "status"},
     {title: "Steps to Reproduce", type: "long_text", required: true, columnId: "long_text"},
     {title: "Screenshot", type: "file", required: false, columnId: "files"}
   ])
5. get_form(formToken: "...") to retrieve shareable URL
```

**User:** Add a conditional question: if severity is "Critical", ask for a workaround.

**Agent:**

```
1. form_questions_editor(formToken: "...", action: "create", questions: [
     {title: "Available Workaround?", type: "text", columnId: "text0",
      condition: {questionId: "severity_q", value: "Critical"}}
   ])
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `create_form` | Create a new form linked to a board |
| `get_form` | Retrieve form details, URL, and configuration |
| `update_form` | Update form settings, appearance, submission messages |
| `form_questions_editor` | Add, update, or delete individual form questions |
| `get_board_info` | Check board columns for question-to-column mapping |
| `create_board` | Create a response board if one doesn't exist |
| `create_column` | Add columns to the response board for new question types |

## Common Pitfalls

- Each form question maps to a board column -- the column must exist before mapping
- Form tokens are different from form IDs -- use the token for API operations
- Conditional logic only supports single-level conditions (no nested AND/OR)
- File upload questions require a file column on the response board
- Form submissions create items on the linked board -- column types must match question types
- Public forms are accessible to anyone with the URL -- no authentication required
- Form appearance customization (colors, logo) requires a Pro plan or higher

## See Also

- [monday-board-management](../monday-board-management/SKILL.md)
- [monday-column-types-guide](../monday-column-types-guide/SKILL.md)
- [monday-workflow-automation](../monday-workflow-automation/SKILL.md)
