# Security Policy

## Scope

This plugin contains **markdown files only** (skills, rules, documentation). There is no executable code, no MCP server, and no runtime dependencies beyond pytest for development.

The primary security concern is **accidental exposure of Monday.com API tokens** in source files, which the `monday-api-token-safety` rule actively flags.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.1.x   | Yes       |

## Reporting a Vulnerability

If you discover a security issue, please report it via [GitHub Security Advisory](https://github.com/TMHSDigital/Monday-Cursor-Plugin/security/advisories/new).

**Do not** open a public issue for security vulnerabilities.

### Timeline

- **Acknowledgment:** Within 48 hours
- **Triage:** Within 7 days
- **Fix:** Depends on severity; critical issues prioritized

## User Practices

- Never commit real API tokens to version control
- Use `.env` files with `.gitignore` protection
- Review the `monday-api-token-safety` rule's guidance
- Rotate tokens if you suspect exposure
- Use scoped tokens with minimum required permissions
