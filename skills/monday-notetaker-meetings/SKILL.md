---
name: monday-notetaker-meetings
description: Access meeting notes, transcripts, summaries, and action items from Monday.com Notetaker for team meetings.
standards-version: 1.7.0
---

# Monday Notetaker Meetings

## Trigger

- User asks about recent meeting notes or transcripts
- User wants a summary of a specific meeting
- User needs to find action items from a meeting
- User asks what was discussed in a meeting
- User wants to review meeting recordings or participant lists

## Required Inputs

- Meeting name or date range (for searching)
- Meeting ID (for specific meeting details)
- Optional: filter by participants, date, or keywords

## Workflow

1. Use `get_notetaker_meetings` to list recent meetings or search by date range.
2. Identify the target meeting from the results.
3. Review the meeting summary, transcript, and extracted action items.
4. If the user wants action items tracked, use `create_item` to add them to a board.
5. If the user wants meeting notes documented, use `create_doc` and `add_content_to_doc` to create a formatted doc.

## Key References

- [Monday Notetaker](https://support.monday.com/hc/en-us/articles/26489798498834-monday-AI-Notetaker)
- [Meeting Management](https://support.monday.com/hc/en-us/articles/26489798498834)

## Example Interaction

**User:** What were the action items from yesterday's standup?

**Agent:**

```
1. get_notetaker_meetings(dateFrom: "2026-03-29", dateTo: "2026-03-29")
2. Find the standup meeting in results
3. Extract action items from the meeting summary
4. Present: "3 action items from yesterday's standup:
   - Fix auth timeout issue (assigned to Alex)
   - Update API docs (assigned to Sarah)
   - Review PR #142 (assigned to Mike)"
```

**User:** Create tasks from the meeting action items on our sprint board.

**Agent:**

```
1. get_board_info(boardId: "...") to get column structure
2. For each action item:
   create_item(boardId: "...", name: "Fix auth timeout issue", columnValues: "{\"person\": {\"personsAndTeams\": [{\"id\": ..., \"kind\": \"person\"}]}}")
```

## MCP Usage

| Tool | When to use |
|------|------------|
| `get_notetaker_meetings` | List meetings, get transcripts, summaries, and action items |
| `create_item` | Convert action items into board tasks |
| `create_doc` | Create a formatted meeting notes document |
| `add_content_to_doc` | Append meeting content to an existing doc |
| `create_update` | Post meeting summary as an update on a relevant item |
| `list_users_and_teams` | Resolve participant names to user IDs |

## Common Pitfalls

- Notetaker must be enabled and invited to meetings for transcripts to be available
- Meeting data may take a few minutes to process after the meeting ends
- Action items are AI-extracted and may need manual review for accuracy
- Transcript quality depends on audio quality and speaker identification
- Meeting search by date uses UTC -- account for timezone differences
- Not all meeting platforms are supported; check Monday.com docs for current integrations

## See Also

- [monday-docs-management](../monday-docs-management/SKILL.md)
- [monday-sprint-planning](../monday-sprint-planning/SKILL.md)
- [monday-updates-and-communication](../monday-updates-and-communication/SKILL.md)
