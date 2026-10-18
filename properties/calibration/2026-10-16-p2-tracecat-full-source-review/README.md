# Tracecat full P2 source review

**Review dates:** 2026-10-16 through 2026-10-17
**Frozen source:** `TracecatHQ/tracecat@c84d52528a489821f355fc63976fbc7783ae0ad5`
**Tree:** `b4af14482f3483605e41307d54f2b777b63bbd84`
**Inventory:** P2 exact-pin source inventory v5, 115 Tracecat rows
**Status:** complete raw-site review for this frozen inventory member

## Result

| Decision | Rows |
|---|---:|
| Skip, with source reason | 78 |
| Unresolved; contract not adopted | 29 |
| Adopted rows | 8 |
| Total reviewed | 115 |

This is complete for the 115 Tracecat rows in v5’s registered file and extractor selection. It does not claim that every regex in every repository file was inventoried. The initial inventory-location/source pass added no proof or product outcome. The three rows adopted in that pass repeat existing Tracecat contracts:

- The MCP stdio environment-key declaration versus Python’s final-line-feed behavior; downstream security impact remains unconfirmed.
- The MCP server-name slash/backslash exclusion; no path traversal or security impact is claimed.
- The registry origin-slug component alphabet; the existing composed-helper gate already covers the normalization path.

Later source-to-sink passes adopted five additional questions: two path-component contracts, the RBAC scope-pattern contract, a table/column identifier quote-exclusion contract, and a sandbox environment-key separator contract.
The mount-only artifact provider's helper is documented in its [P6 bundle](../2026-10-16-autonomous-tracecat-artifact-path-segment/README.md);
workspace-sync's component normalizer is documented in its [P6 bundle](../2026-10-16-autonomous-tracecat-workspace-sync-path-segment/README.md).
Both path-component questions add contract-backed local gates, not security findings. Their inputs are
workspace artifact/configuration data; the contracts exclude attacker
reachability, full export-root enforcement, symlink ancestry, races, and
collisions.

The RBAC question traces the custom-scope POST request through its Pydantic
schema, repeated service validator, and `fnmatch` consumer. Its exact-source
gate found that the request schema rejects a final line feed even though the
standalone Python helper accepts one; the schema rejects it before the pinned
route reaches the helper. The property excludes `?` and `[]`; weakening both
allowlists makes `?` broaden a wildcard grant in the exact matcher. This is a
useful local regression gate, not a current vulnerability or impact finding.

The table-identifier question follows `TableCreate` and `TableColumnCreate`
through the public and internal `table:create` routes to the exact service
validators and dynamic DDL. The request-layer theorem excludes double quotes,
which the column DDL helper wraps as SQL identifier delimiters. The service
also rejects quotes before DDL. The schema helper accepts a final line feed
because of Python `$` semantics, but the service rejects it; this is not a
sink acceptance or SQL-injection finding. Its exact-source Pydantic/service
gate checked 2,227 deterministic inputs with zero mismatches, and its
source-weakened quote mutation reproduced. See the [table identifier P6
bundle](../2026-10-17-autonomous-tracecat-table-identifier/README.md).

The 29 unresolved rows include other live authorization and credential handling, expression and Git URL parsing, sandbox configuration, log/error redaction, and workspace-sync references. They remain outside contract and product-question counts until their full input source, trust class, property, and sink are evidenced. The SQL identifier row is now a narrowly scoped adopted request-layer contract; no SQL-injection or impact finding is claimed. The stdio MCP tool-name filter is recorded as a compatibility skip: current [Anthropic user-defined tool names](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) use the same character grammar with a 128-character maximum, while Tracecat limits names to 64; the Tracecat path adds each admitted name as one allowed-tool string and also inserts separately normalized server descriptions into the prompt. The agent sandbox environment-key validator is also a skip: the exact runtime caller omits its optional config, so `AgentSandboxConfig.env_vars` remains empty; direct mode builds a fixed environment. The two OAuth scope UUID patterns are also skips: they populate claimed identity sets, while workspace and organization authorization resolve database roles/memberships and Watchtower intersects ambiguous org claims with memberships after the issuer’s single-org check. The workflow email sender/recipient regex is a skip: a CPython 3.12.15 replay of the exact pinned builder showed embedded header-injection values fail before SMTP, while a final LF is normalized by EmailMessage. That composition does not make the regex alone a security contract; see [email-header-replay.json](email-header-replay.json). The 78 skips are supported by the pinned source: tests, benchmarks/evaluation tools, historical migrations, presentation or diagnostic parsing, code metadata normalization, and sites without a product security boundary. The Amazon S3 bucket pattern is an unused declaration at this pin.
The sandbox environment-key validator in `tracecat/sandbox/executor.py` is a separate adopted contract. Authenticated workflow configuration supplies `core.script.run_python.env_vars`; the nsjail builder validates keys before adding them to the child environment and `--env` arguments. The contract is limited to the POSIX invariant that a name excludes `=`. It does not call the full accepted grammar POSIX-compliant: Python `.match()` with `$` admits one terminal LF. The unbounded shape-1 proof is UNSAT, its `TRACE=TOKEN` equals-sign mutation reproduces, and the exact-source gate checks 4,232 cases with zero mismatches. Python's subprocess layer independently rejects `=` in environment names, so no current bypass or impact is claimed. See the [sandbox environment-key P6 bundle](../2026-10-17-autonomous-tracecat-sandbox-env-equals/README.md).

## Review record

`review-pass1.json` records the inventory-location triage. `review.json` records the follow-up source and caller pass. The same model performed both passes; this is not independent third-party or human review. Each final row is bound to the inventory regex identity and pattern and includes source references. `evidence.json` records the exact source file digests, Git blob IDs, and extracted pinned source windows.

The review followed the autonomous adoption requirements in [AUTONOMOUS-CONTRACTS.md](../../../docs/AUTONOMOUS-CONTRACTS.md). Existing adopted contracts were not relabeled or widened during this review.

## Reproduction

The exact source checkout was clean at the recorded commit and tree. The evidence builder checked all 115 identities and patterns against inventory v5 and bound 52 source files to the exact pinned Git blobs:

```sh
.venv/bin/python scripts/build-p2-source-review-evidence.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-16-p2-source-inventory-v5/inventory.json \
  --sites properties/calibration/2026-10-16-p2-source-inventory-v5/sites.ndjson \
  --reviews properties/calibration/2026-10-16-p2-tracecat-full-source-review/review.json \
  --checkout /tmp/tracecat-p2-review-20261016 \
  --repo-id TracecatHQ/tracecat \
  --pin c84d52528a489821f355fc63976fbc7783ae0ad5 \
  --output properties/calibration/2026-10-16-p2-tracecat-full-source-review/evidence.json
```

The builder completed with 115 reviewed rows, 78 skips, 29 unresolved rows, and 8 adopted rows. The five additional questions and their proof/gates are recorded separately; the source-review pass itself did not run a solver.

## Limitations and next work

- Same-model second pass improves coverage but is not an independent reviewer.
- Source inventory v5 remains incomplete for the other cohort member Everclaw; this Tracecat review does not close its submodule gap.
- The 29 unresolved rows need prioritization and source-backed contracts, starting with the remaining authorization, credential, redaction, SQL, Git, and path sinks.
- Review duration, tokens, cost, and human active time were not measured.
