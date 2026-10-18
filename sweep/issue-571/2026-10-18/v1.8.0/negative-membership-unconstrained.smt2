(set-logic QF_SLIA)
(declare-const s String)
(assert (not (str.in_re s (re.from_ecma2020 '(^|[^A-Za-z0-9_])(ACCEPT|ALLOW|PASS|DROP|REJECT|DENY|BLOCK)([^A-Za-z0-9_]|$)'))))
(check-sat)
