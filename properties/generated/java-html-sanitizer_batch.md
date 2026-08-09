# java-html-sanitizer triage (java→pcre approximation)

- pin: `a979a97e65f3cda1921fe3bb27ff4f9457be5c8d`
- url: https://github.com/OWASP/java-html-sanitizer
- sites: 20 (encodable 14, rejected 6, fraction 0.7000)
- differential: ok=14 fail=0 zero_disagreement_pass=True
- reject_reasons: `{"ok": 14, "parse-error": 1, "quote": 1, "unicode-property": 4}`

See `sweep/corpus-wave4/java-features.md`.
