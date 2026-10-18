# Tracecat MCP stdio environment-key validation

**Source:** `TracecatHQ/tracecat@c84d52528a489821f355fc63976fbc7783ae0ad5`,
already in the frozen `2026-09-12-calibration-20-r2` cohort. The source review
is deliberately limited to one inventory site; it does not review all 115
Tracecat regex rows.

## Declared behavior and source path

At `tracecat/integrations/mcp_validation.py:178`,
`validate_mcp_env_key` says keys must match `[A-Za-z_][A-Za-z0-9_]*` and uses
`re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", key)`. CPython's `$` also matches just
before one final line feed, so `TRACE_TOKEN\n` passes the validator even
though that character is outside Tracecat's documented pattern language.
The regex is also used through `validate_mcp_command_config`.

This is a Tracecat configuration-validation gap. The contract does not claim
that every POSIX implementation rejects newline characters in environment
names: POSIX permits implementation-specific names. It records only the
stricter grammar Tracecat itself declares. The source flow is `stdio_env` in
`MCPStdioIntegrationCreate`, validation in `MCPIntegrationService`, encrypted
persistence, decryption, then `env` passed to `StdioTransport`. The integration
create scope is required. The exact accepted key also reached a local POSIX
child-process environment in the gate.

The evidence does **not** establish command injection, privilege escalation,
or a security-impacting behavior in an MCP server. The `StdioTransport` call
passes an environment mapping; command and arguments are launched through
the stdio transport path. No deployed Tracecat instance, real MCP server, or
external maintainer was contacted.

The roster uses the line symbol `re.match` as its stable source selector; the
exact inventory identity remains `tracecat/integrations/mcp_validation.py:178:11`
with regex ID `280c0b240b92090a7bdb58b6a70cff57`. The scoped review and pinned
source windows are in
[`2026-10-15-p2-tracecat-mcp-env-key-review/`](../2026-10-15-p2-tracecat-mcp-env-key-review/).

## Proof and regression gate

The harness models CPython's anchored source language over ASCII keys of
length 1–64. Z3 found `_\n`, and the exact pinned
`validate_mcp_command_config` accepted it. A source mutation that changes the
terminal `$` to `\Z` rejects the witness; reintroducing `$` accepts it again.
The separate pinned-source gate checked 1,442 keys against an independent
language model with zero mismatches, repeated the configuration and child
environment replay, and exercised the same mutation.

This question is recorded as a counterexample finder and remains pending
product triage in the wave state. It is not a confirmed security impact or a
third-party report. The existing Tracecat source tests and docs were reviewed
as evidence; the full Tracecat test suite was not run.

Reproduce the proof and source gate from the repo root:

```sh
.venv/bin/python scripts/z3-verify.py \
  TC-mcp-env-key-accepts-terminal-lf \
  TC-mcp-env-key-dollar-anchor-mutation \
  --require-ground-truth --json

.venv/bin/python scripts/tracecat-mcp-env-key-regression-gate.py \
  --source-root /tmp/regexproof-pinned-sources/tracecat-c84d52528a489821f355fc63976fbc7783ae0ad5 \
  --output properties/calibration/2026-10-15-autonomous-tracecat-mcp-env-key/p6-wave/product-gate.json
```

The P6 roster, input snapshot, gate configuration, generated report, and
resumable state are under [`p6-wave/`](p6-wave/).
