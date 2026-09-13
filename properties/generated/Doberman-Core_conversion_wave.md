# Doberman-Core Python command-execution conversion wave

Pin: `fu351/Doberman-Core` @ `53ae43c5298a2426c6696147fdd75e2a4aef10e2`.
Family: `PY-doberman-command-exec`. Wave: `doberman_w1`.
Product engine: Python `re` at the pinned call sites; declared domain is ASCII.

## 15 read → 2 asked

| Site | Decision | Reason |
|---|---|---|
| `commands.py:266` `_WINDOWS_ROOT_RE` | **asked**, shape 2 | Exact drive-root whitelist; root/home deletion BLOCK sink. |
| `commands.py:434` `_DISK_WIPE` | **asked**, shape 1 | Disk-wipe token alphabet excludes shell separators and whitespace before BLOCK. |
| `commands.py:79` `_SUBSTITUTION` | defer | Nested substitution is parser/composition behavior; current backend rejects the construct. |
| `commands.py:818-819` fetch/pipe pair | defer | Word-boundary patterns are outside the current Python backend; use behavioral differential testing. |
| `normalize.py:161` `_SUSPECTED_EGRESS_VERB` | defer | Lookarounds are outside the current backend and the committed inventory lacks this direct row. |
| Remaining reviewed rows | skip or behavioral-test-only | Tokenizer semantics, portability normalization, advisory classifiers, or duplicate dynamic flags. |

Both product properties are UNSAT in their declared domains. Mutation guards
flip both families to SAT. Python `re` edge-case replay covers the exact source
patterns; no SAT vulnerability witness was produced, so no public disclosure is
appropriate.

The three deferred primary questions remain candidates for a separate behavioral
or backend work item and are not counted as product properties in this wave.
