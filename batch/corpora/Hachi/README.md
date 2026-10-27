# Hachi corpus (#417)

Pinned YARA rules from [`Kart1keya/Hachi`](https://github.com/Kart1keya/Hachi) at commit `73e083e22f020ffa18ca5f09321ea19c4f7c4da4`. The manifest key is `Hachi`; its `gate_decision_file` points to the existing owner-prefixed artifact `Kart1keya-Hachi_gate_decision.json`. Do not copy or alias that gate artifact under a second name.

This is a security-tool corpus. Its scanner and planned outputs are `private_first`. The Smith `go` is for YARA/compiler coverage only; it does not claim product contracts or ground-truth findings.

## Materialize and verify the pin

```bash
python3 scripts/materialize-corpus.py \
  --gate properties/generated/Kart1keya-Hachi_gate_decision.json

test "$(git -C batch/corpora/Hachi/rules rev-parse HEAD)" = \
  73e083e22f020ffa18ca5f09321ea19c4f7c4da4
```

## Measure and batch

```bash
python3 scripts/measure-corpus-fraction.py \
  --corpus Hachi --assert-determinism
python3 -m regexproof.batch \
  --corpus Hachi --jobs 4 --require-ground-truth
```

The deterministic YARA measurement extracted 3,087 sites and encoded 2,995 (0.9702), with zero unclassified parse errors. The 92 non-encodable sites are all present in `properties/triage/Hachi.ndjson`:

| Unencodable reason | Sites |
|---|---:|
| `fullword-boundary` | 62 |
| `wide-non-literal` | 29 |
| `pattern-too-long` | 1 |

The pinned checkout also contains 2 `py_re` sites; they are outside this YARA-only measurement. The normal batch output contains four `planned` inventory stubs, not product properties, and all are `private_first`. The PR dry-run confirms `publish: false` and `would_open_public_upstream_issue: false`.

Budget baseline: 500 MB disk, 2,048 MB memory, 5,000 patterns, 600 seconds wall time, and 120 seconds ReDoS wall time.
