# Tracecat table identifier quote-exclusion contract

**Source:** `TracecatHQ/tracecat@c84d52528a489821f355fc63976fbc7783ae0ad5`
**Tree:** `b4af14482f3483605e41307d54f2b777b63bbd84`
**Inventory row:** `c1d1d6d2adfccca3b9f7d5215dfb428e` at
`tracecat/tables/schemas.py:17:21`
**Adoption:** agent-derived under the standing delegation in
[`AUTONOMOUS-CONTRACTS.md`](../../../docs/AUTONOMOUS-CONTRACTS.md)

## Contract and source path

The narrow guarantee is that the pinned `TableCreate.name` and
`TableColumnCreate.name` request validators exclude a double quote before
table or column creation. The public routes require `table:create`; the
internal table route reconstructs `TableCreate`, and the internal column
route uses `TableColumnCreate`. The exact service calls
`validate_identifier` before dynamic DDL. Column DDL wraps the identifier in
raw double quotes with `quote_identifier`.

The input is workspace table or column configuration from an authenticated
caller. This is a request-layer defense-in-depth property. The service
validator independently rejects double quotes before DDL, so this work does
not establish a current SQL injection, attacker reachability, or deployed
impact.

## Proof and gate

- `TC-table-identifier-double-quote-excluded`: shape-1 UNSAT, with no string
  length bound; the exact allowlist character language excludes `"`.
- `TC-table-identifier-quote-mutation`: SAT at `a"`; weakening the exact
  request-model allowlist admits the value to both minimal models, while the
  unchanged exact service validator still rejects it before DDL.
- The local Pydantic 2.12.5 replay rebuilt the exact pinned name fields and
  validator methods from source AST, then compared both request models and
  the service validator over 2,227 deterministic inputs. It found zero
  mismatches.
- The replay verified both public create routes, both internal create paths,
  the service validations, and the column `quote_identifier` call. It also
  records the Python `$` edge: the request model accepts a final line feed,
  but the service rejects it before DDL. This is not a sink acceptance.
- The P6 runner completed one UNSAT question, one reproduced mutation, one
  exact-source gate, and 2,227 differential cases. Measured phase sum:
  2.0391 seconds (source 19.0 ms, mutation 148.0 ms, solver 0.2 ms, gate
  1,871.9 ms). Source review and contract authoring were not timed; token use,
  cost, and human active time remain unknown.

The gate is wired into the proof CI job after installing the source-pinned
Pydantic runtime. Hosted CI has not yet been observed. No Tracecat source code
was changed, and no security impact, external report, maintainer confirmation,
or fix is claimed.

## Artifacts

- [`contract.json`](contract.json)
- [`P6 roster and state`](p6-wave/)
- [`product-gate.json`](product-gate.json)
- [`scorecard snapshot`](scorecard-after-tracecat-table-identifier.json)
- [`P2 v26 checkpoint`](../2026-10-17-p2-existing-evidence-20r2-v26/README.md)
- [`Tracecat complete source review`](../2026-10-16-p2-tracecat-full-source-review/README.md)
