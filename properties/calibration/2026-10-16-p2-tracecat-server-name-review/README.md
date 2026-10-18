# Targeted Tracecat server-name source review

This review adopts one source-backed contract for one of 115 Tracecat rows in
the frozen P2 inventory. It is not a complete Tracecat review. The exact
inventory row is `tracecat/integrations/mcp_validation.py:267:11`, regex ID
`60bada10a610fde520e8e96c90887d71`, source-site ID
`6054f97be853956788ff86afb5fd537445a87cd5`.

At the pinned source, the comment and validation error limit MCP server names
to alphanumeric characters, hyphens, and underscores. The stdio preset
resolution path passes the persisted MCP integration slug to
`validate_mcp_command_config(name=...)`, which calls this validator. The
adopted contract proves only the useful alphabet-level subset that accepted
names exclude `/` and `\`; it does not prove the whole grammar or make a claim
about path traversal or security impact.

The exact source windows, inventory digest, source-file hashes, and review
decision are in [`evidence.json`](evidence.json); the compact review record is
in [`review.json`](review.json). The corresponding proof and P6 gate are in
the [server-name bundle](../2026-10-16-autonomous-tracecat-server-name/README.md).
