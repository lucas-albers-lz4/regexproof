# Tracecat MCP server-name separator invariant

**Source:** `TracecatHQ/tracecat@c84d52528a489821f355fc63976fbc7783ae0ad5`,
already in the frozen `2026-09-12-calibration-20-r2` cohort. The targeted P2
review covers exactly the `mcp_validation.py:267` inventory row; it does not
review all 115 Tracecat regex rows.

## Contract scope

`validate_mcp_server_name` declares that a server name contains only
alphanumeric characters, hyphens, and underscores. The helper is called from
`validate_mcp_command_config` when `name` is supplied. In the stdio preset
resolution path, Tracecat supplies the persisted `MCPIntegration.slug` as
`name`; the integration service derives that slug from workspace configuration.
The contract proves only that accepted values exclude `/` and `\`. It does not
prove the entire name grammar, the behavior of slug generation, or path safety
at any sink. Python `$` can still allow one final line feed, which this
separator theorem does not address.

## Proof and gate

Z3 proved the shape-1 single-character alphabet disjointness property UNSAT
with no string-length bound. The family mutation guard adds `/` to the exact
pinned allowlist and produces the expected SAT witness; the source-mutated
`validate_mcp_command_config` accepts it while the original rejects it.
The exact-source CPython gate checked 714 deterministic names against an
independent model with zero mismatches and confirmed that both validators
reject `/` and `\` on the frozen source.

The P6 wave completed with one UNSAT question, one local gate, one mutation
check, 714 differential cases, and a 0.6676-second phase sum. Review and
contract-authoring time were not included; token use, cost, and human active
time are unknown. No security impact or external outcome is claimed.

Reproduce the focused proof and pinned-source gate from the repo root:

```sh
.venv/bin/python scripts/z3-verify.py \
  TC-mcp-server-name-separators-excluded \
  TC-mcp-server-name-slash-allowlist-mutation \
  --require-ground-truth --json

.venv/bin/python scripts/tracecat-mcp-server-name-regression-gate.py \
  --source-root /tmp/regexproof-pinned-sources/tracecat-c84d52528a489821f355fc63976fbc7783ae0ad5 \
  --output properties/calibration/2026-10-16-autonomous-tracecat-server-name/p6-wave/product-gate.json
```

The adopted contract is `contract.json`. The frozen roster, gate config,
product-gate report, and resumable P6 state are under [`p6-wave/`](p6-wave/).
