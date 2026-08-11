# P1 baseline matrix (2026-08-11)

| property | stock | ms | noodler | ms | cvc5 | witness |
|---|---|---|---|---|---|---|
| P1-ampersand | unsat | 5686.7 | unsat | 31.1 | unsat | n/a |
| P1-backtick | unsat | 5401.7 | unsat | 31.3 | unsat | n/a |
| P1-dollar | unsat | 5044.4 | unsat | 33.4 | unsat | n/a |
| P1-equals | unsat | 5266.4 | unsat | 34.7 | unsat | n/a |
| P1-mutated-star | sat | 31.8 | sat | 68.6 | sat | DIFF |
| P1-newline | unsat | 4122.0 | unsat | 31.6 | unsat | n/a |
| P1-pipe | unsat | 4788.7 | unsat | 31.4 | unsat | n/a |
| P1-semicolon | unsat | 5077.2 | unsat | 31.5 | unsat | n/a |
| P1-space | unsat | 4746.0 | unsat | 31.7 | unsat | n/a |
| P1-tab | unsat | 4207.1 | unsat | 31.5 | unsat | n/a |
| P2-actor-whitelist | unsat | 1138.6 | unsat | 22.3 | unsat | n/a |
| P2-mutated-space | sat | 11.7 | sat | 33.8 | sat | DIFF |
| P3-mutated-correct-capture | unsat | 0.1 | unsat | 12.0 | unsat | n/a |
| P3-sed-capture-truncation | sat | 6.9 | sat | 27.1 | sat | DIFF |
| P4-escape-image-del | unsat | 0.3 | unsat | 12.3 | unsat | n/a |
| P4-escape-image-newline | unsat | 0.6 | unsat | 12.4 | unsat | n/a |
| P4-escape-image-tab | unsat | 0.4 | unsat | 12.0 | unsat | n/a |
| P4-mutated-tab | sat | 0.4 | sat | 12.4 | sat | MATCH |
| P4-nul-passthrough-demo | sat | 0.5 | sat | 12.4 | sat | MATCH |
| P5-handle-safe | unsat | 25.2 | unsat | 24.3 | unsat | n/a |
| P5-mutated-lowercase | sat | 1.7 | sat | 13.2 | sat | MATCH |
| P6-prefix-match-demo | unsat | 0.2 | unsat | 12.0 | unsat | n/a |
| P6-prefix-match-helper | sat | 0.4 | sat | 12.1 | sat | MATCH |
| crs-cross-engine-control | unsat | 0.1 | unsat | 12.2 | unsat | n/a |
| crs-cross-engine-widen-R1 | sat | 4.6 | sat | 18.4 | sat | MATCH |
| P2-len64 | unknown | 30100.2 | unsat | 17.8 | unsat | n/a |
| P4-monolithic | unknown | 30039.4 | unsat | 19.3 | unknown | n/a |
| P2-len64-reloop-17-64 (S11) | n/a (z3py no ReLoop) | 0 | unsat | 59.8 | PARSE-ERROR | n/a |
