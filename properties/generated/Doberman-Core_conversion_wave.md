# Doberman-Core Python command-execution conversion wave

Pin: `fu351/Doberman-Core` @ `53ae43c5298a2426c6696147fdd75e2a4aef10e2`.
Family: `PY-doberman-command-exec`. Wave: `doberman_w1`.
Product engine: Python `re` at the pinned call sites; declared domain is ASCII,
including a terminal LF preserved inside a quoted argument.

## 15 read → 2 asked

| Site | Decision | Reason |
|---|---|---|
| `commands.py:266` `_WINDOWS_ROOT_RE` | **asked**, shape 2 | Terminal-newline acceptance at the root/home deletion BLOCK sink. |
| `commands.py:434` `_DISK_WIPE` | **asked**, shape 2 | Terminal-newline acceptance at the disk-wipe BLOCK sink. |
| `commands.py:79` `_SUBSTITUTION` | defer | Nested substitution is parser/composition behavior; current backend rejects the construct. |
| `commands.py:818-819` fetch/pipe pair | defer | Word-boundary patterns are outside the current Python backend; use behavioral differential testing. |
| `normalize.py:161` `_SUSPECTED_EGRESS_VERB` | defer | Lookarounds are outside the current backend and the committed inventory lacks this direct row. |
| Remaining reviewed rows | skip or behavioral-test-only | Tokenizer semantics, portability normalization, advisory classifiers, or duplicate dynamic flags. |

Both product properties are SAT in their declared domains and reproduce against
the pinned Python `re` implementation:

| Site | Witness class | Ground truth |
|---|---|---|
| `commands.py:266` `_WINDOWS_ROOT_RE` | `P:*\n` | reproduced |
| `commands.py:434` `_DISK_WIPE` | `mkfs\n` | reproduced |

Python's `$` accepts the match immediately before one terminal newline. The
surrounding Doberman preprocessing preserves that newline when it is inside a
quoted argument, so these are private-first security-tool findings rather than
proofs of the original whitelist claims. Mutation guards still flip both
families to SAT and now weaken the same full matcher used by each product
property.

The three deferred primary questions remain candidates for a separate behavioral
or backend work item and are not counted as product properties in this wave.
