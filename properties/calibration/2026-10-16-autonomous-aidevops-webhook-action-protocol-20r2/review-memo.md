# Source review memo: webhook receiver action protocol

This is a complete census of the 11 POSIX-shell regex records for `.agents/scripts/pulse-merge-webhook-receiver.sh` in the corrected exact-pin v5 inventory. The ranks follow source line and column order; there was no random allocation or solver-informed selection.

The pinned receiver documentation says the Python HTTP server verifies the raw GitHub HMAC before parsing request fields, then emits a versioned local action protocol; the shell side validates action fields before cache invalidation or `process_pr`. The polling routine remains the documented backstop. These regexes are downstream checks, so outcomes will be described as local workflow guarantees. The admission GO decision for Aidevops is scale-based and explicitly has `security-boundary=false`; this census does not claim a security finding or prospective cohort yield.

Four contracts were adopted for separately useful checks: configured secret-variable names before indirect lookup/unset; owner/repository token validation; 40-hex check SHA validation; and positive decimal PR-number validation before dispatch. Six rows were skipped as internal or duplicate subchecks. The positive-integer config helper at line 189 remains unresolved because its documented decimal domain does not specify leading-zero handling and Bash numeric comparison has octal semantics.
