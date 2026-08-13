# mobissh corpus

Pinned flavordrake/mobissh ecma allowlist for Smith GO admit
[#311](https://github.com/lucas-albers-lz4/regexproof/issues/311)
under umbrella [#305](https://github.com/lucas-albers-lz4/regexproof/issues/305).

SSH fleet-management tool. Top-60 ecma files measured **62/104 = 0.5962
encodable** (complete, deterministic).

## Materialize

```bash
PIN=ced24fa12d650e2aa6ea44a4e0a7f52bec548409
git clone --filter=blob:none https://github.com/flavordrake/mobissh.git /tmp/mobissh
git -C /tmp/mobissh fetch --depth 1 origin "$PIN"
git -C /tmp/mobissh checkout "$PIN"
ln -sfn /tmp/mobissh batch/corpora/mobissh/rules
test "$(git -C /tmp/mobissh rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/mobissh_gate_decision.json` (triage-trial).
Smith: `properties/generated/mobissh_smith_decision.json` (go).
Security-adjacent → `private_first` via `SECURITY_TOOL_CORPORA`.
