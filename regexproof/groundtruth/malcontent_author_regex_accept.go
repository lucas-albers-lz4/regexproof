// Minimal real-engine accept/reject adapter for differential-fuzz.py.
// The pinned source declaration is verified by the gate before this program
// is built; Go's regexp package is the product engine used by that declaration.
package main

import (
	"io"
	"os"
	"regexp"
)

func main() {
	input, err := io.ReadAll(os.Stdin)
	if err != nil {
		os.Exit(2)
	}
	pattern := regexp.MustCompile(`(.*?) \((http.*)\)`)
	if pattern.FindStringSubmatch(string(input)) == nil {
		os.Exit(1)
	}
}
