# P1 baseline matrix (2026-08-11)

| property | stock | ms | noodler | ms | cvc5 | witness |
|---|---|---|---|---|---|---|
| P1-ampersand | unsat | 5977.6 | unsat | 30.4 | unsat | n/a |
| P1-backtick | unsat | 5833.0 | unsat | 33.6 | unsat | n/a |
| P1-dollar | unsat | 5905.8 | unsat | 31.8 | unsat | n/a |
| P1-equals | unsat | 5256.3 | unsat | 31.3 | unsat | n/a |
| P1-mutated-star | sat | 35.3 | sat | 68.8 | sat | DIFF |
| P1-newline | unsat | 4247.5 | unsat | 32.8 | unsat | n/a |
| P1-pipe | unsat | 4891.4 | unsat | 32.5 | unsat | n/a |
| P1-semicolon | unsat | 5188.7 | unsat | 31.3 | unsat | n/a |
| P1-space | unsat | 4866.8 | unsat | 31.5 | unsat | n/a |
| P1-tab | unsat | 4288.4 | unsat | 31.0 | unsat | n/a |
| P2-actor-whitelist | unsat | 1153.9 | unsat | 22.3 | unsat | n/a |
| P2-mutated-space | sat | 11.7 | sat | 34.5 | sat | DIFF |
| P3-mutated-correct-capture | unsat | 0.1 | unsat | 12.4 | unsat | n/a |
| P3-sed-capture-truncation | sat | 7.4 | sat | 27.0 | sat | DIFF |
| P4-escape-image-del | unsat | 0.3 | unsat | 12.2 | unsat | n/a |
| P4-escape-image-newline | unsat | 0.3 | unsat | 13.2 | unsat | n/a |
| P4-escape-image-tab | unsat | 0.4 | unsat | 12.1 | unsat | n/a |
| P4-mutated-tab | sat | 0.4 | sat | 12.1 | sat | MATCH |
| P4-nul-passthrough-demo | sat | 0.5 | sat | 12.4 | sat | MATCH |
| P5-handle-safe | unsat | 25.5 | unsat | 25.7 | unsat | n/a |
| P5-mutated-lowercase | sat | 1.7 | sat | 13.2 | sat | MATCH |
| P6-prefix-match-demo | unsat | 0.2 | unsat | 11.9 | unsat | n/a |
| P6-prefix-match-helper | sat | 0.4 | sat | 12.1 | sat | MATCH |
| crs-cross-engine-control | unsat | 0.1 | unsat | 11.8 | unsat | n/a |
| crs-cross-engine-widen-R1 | sat | 4.6 | sat | 18.4 | sat | MATCH |
| P2-len64 | unknown | 30044.2 | unsat | 17.6 | unsat | n/a |
| P4-monolithic | unknown | 30032.4 | unsat | 19.2 | unknown | n/a |
| P2-len64-reloop-17-64 (S11) | n/a (z3py no ReLoop) | 0 | unsat | 59.8 | PARSE-ERROR | n/a |
