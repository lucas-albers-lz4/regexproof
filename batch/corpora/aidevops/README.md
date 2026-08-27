# aidevops corpus

Pinned `marcusquinn/aidevops` at
`8666b6c6c52472b5535aa295f2df593918152cb1` for the aidevops conversion wave
([`sweep/aidevops-conversion/plan.md`](../../../sweep/aidevops-conversion/plan.md)).

Plan-time probe: **12,880** sites / **11,330** posix-shell / 1,817 files
(GO on `large-under-saturated`, not security-boundary).
Runtime gate: `properties/generated/aidevops_gate_decision.json`
(dated copy of the 2026-08-13 GO probe decision).

**Not** in `WAVE_CORPORA` — local batch / conversion only.

## Materialize

```bash
python scripts/materialize-corpus.py --gate \
  properties/generated/aidevops_gate_decision.json \
  --allowlist-file /tmp/aidevops-allowlist.txt
# or:
PIN=8666b6c6c52472b5535aa295f2df593918152cb1
git clone --filter=blob:none https://github.com/marcusquinn/aidevops.git /tmp/marcusquinn-aidevops-aidevops
git -C /tmp/marcusquinn-aidevops-aidevops fetch --depth 1 origin "$PIN"
git -C /tmp/marcusquinn-aidevops-aidevops checkout "$PIN"
ln -sfn /tmp/marcusquinn-aidevops-aidevops batch/corpora/aidevops/rules
test "$(git -C /tmp/marcusquinn-aidevops-aidevops rev-parse HEAD)" = "$PIN"
```

`--allowlist-file` is required: the probe `regex_sites_per_file` includes
top-level `tests/` (inflation ACK). The allowlist does not restrict the
clone; Gate 1 still drops `tests/` before ranking. Example:

```bash
printf '%s\n' '.agents/hooks/task-id-collision-guard.sh' \
  > /tmp/aidevops-allowlist.txt
```

Gate: `properties/generated/aidevops_gate_decision.json` (`go`).
Probe (plan-time only): `properties/generated/marcusquinn-aidevops_gate_decision.json`.

Extractor: `shell_posix` (walks `**/*` + `_is_shell_script`; ignores glob).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus aidevops \
  --assert-determinism
python -m regexproof.batch --corpus aidevops
```

Do **not** pass `--with-redos` for conversion wave P1. Leave
`WAVE_CORPORA` unchanged. Commit `_batch_summary.json` only with a
conversion-ledger regen in the same PR. Gate 0 stop if encodable
fraction < 0.30.
