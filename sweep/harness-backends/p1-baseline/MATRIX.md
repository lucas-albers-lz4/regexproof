# P1 baseline matrix (2026-08-11)

| property | stock | ms | noodler | ms | cvc5 | witness |
|---|---|---|---|---|---|---|
| P1-ampersand | unsat | 5692.6 | unsat | 31.2 | unsat | n/a |
| P1-backtick | unsat | 5479.3 | unsat | 33.5 | unsat | n/a |
| P1-dollar | unsat | 5071.5 | unsat | 32.2 | unsat | n/a |
| P1-equals | unsat | 5238.1 | unsat | 31.2 | unsat | n/a |
| P1-mutated-star | sat | 31.7 | sat | 69.0 | sat | DIFF |
| P1-newline | unsat | 4173.5 | unsat | 31.4 | unsat | n/a |
| P1-pipe | unsat | 4805.5 | unsat | 31.3 | unsat | n/a |
| P1-semicolon | unsat | 5141.5 | unsat | 32.2 | unsat | n/a |
| P1-space | unsat | 4805.3 | unsat | 31.4 | unsat | n/a |
| P1-tab | unsat | 4247.7 | unsat | 31.1 | unsat | n/a |
| P2-actor-whitelist | unsat | 1171.6 | unsat | 22.3 | unsat | n/a |
| P2-mutated-space | sat | 11.6 | sat | 33.7 | sat | DIFF |
| P3-mutated-correct-capture | unsat | 0.1 | unsat | 11.9 | unsat | n/a |
| P3-sed-capture-truncation | sat | 7.0 | sat | 26.8 | sat | DIFF |
| P4-escape-image-del | unsat | 0.3 | unsat | 12.0 | unsat | n/a |
| P4-escape-image-newline | unsat | 0.4 | unsat | 13.0 | unsat | n/a |
| P4-escape-image-tab | unsat | 0.4 | unsat | 11.9 | unsat | n/a |
| P4-mutated-tab | sat | 0.4 | sat | 12.4 | sat | MATCH |
| P4-nul-passthrough-demo | sat | 0.5 | sat | 12.5 | sat | DIFF |
| P5-handle-safe | unsat | 25.2 | unsat | 24.4 | unsat | n/a |
| P5-mutated-lowercase | sat | 1.7 | sat | 13.0 | sat | MATCH |
| P6-prefix-match-demo | unsat | 0.2 | unsat | 11.8 | unsat | n/a |
| P6-prefix-match-helper | sat | 0.4 | sat | 12.1 | sat | MATCH |
| crs-cross-engine-control | unsat | 0.1 | unsat | 12.0 | unsat | n/a |
| crs-cross-engine-widen-R1 | sat | 4.6 | sat | 18.2 | sat | MATCH |
| P2-len64 | unknown | 30052.0 | unsat | 17.9 | unsat | n/a |
| P4-monolithic | unknown | 30031.2 | unsat | 18.8 | TIMEOUT | n/a |
| P2-len64-reloop-17-64 (S11) | n/a (z3py no ReLoop) | 0 | unsat | 59.5 | PARSE-ERROR | n/a |
