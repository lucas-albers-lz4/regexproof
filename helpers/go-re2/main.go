// go-re2: RE2 parse + replay helper (Phase 1 mandated).
//
// Usage:
//   go-re2 parse <pattern>          → JSON {ok, op_count} or {ok:false, error}
//   go-re2 match <pattern> <flags>  → reads stdin; exit 0 if MatchString
//
// flags: "i" enables case-insensitive (?i) prefix.
package main

import (
	"encoding/json"
	"fmt"
	"io"
	"os"
	"regexp"
	"regexp/syntax"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "usage: go-re2 parse|match ...")
		os.Exit(2)
	}
	switch os.Args[1] {
	case "parse":
		if len(os.Args) < 3 {
			fail("parse requires pattern")
		}
		pattern := os.Args[2]
		re, err := syntax.Parse(pattern, syntax.Perl)
		if err != nil {
			writeJSON(map[string]any{"ok": false, "error": err.Error()})
			os.Exit(1)
		}
		writeJSON(map[string]any{"ok": true, "op_count": countOps(re), "helper": "go-re2"})
	case "match":
		if len(os.Args) < 4 {
			fail("match requires pattern and flags")
		}
		pattern := os.Args[2]
		flags := os.Args[3]
		if containsFlag(flags, 'i') {
			pattern = "(?i)" + pattern
		}
		re, err := regexp.Compile(pattern)
		if err != nil {
			fmt.Fprintln(os.Stderr, err)
			os.Exit(2)
		}
		data, _ := io.ReadAll(os.Stdin)
		if re.Match(data) {
			os.Exit(0)
		}
		os.Exit(1)
	default:
		fail("unknown command")
	}
}

func containsFlag(flags string, ch rune) bool {
	for _, c := range flags {
		if c == ch {
			return true
		}
	}
	return false
}

func countOps(re *syntax.Regexp) int {
	n := 1
	for _, s := range re.Sub {
		n += countOps(s)
	}
	return n
}

func writeJSON(v any) {
	enc := json.NewEncoder(os.Stdout)
	_ = enc.Encode(v)
}

func fail(msg string) {
	fmt.Fprintln(os.Stderr, msg)
	os.Exit(2)
}
