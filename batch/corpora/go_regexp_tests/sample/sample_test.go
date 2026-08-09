package regexp_tests_sample

import "regexp"

var pinned = regexp.MustCompile(`[a-z]{3,8}`)

var findTests = []struct {
	pat  string
	text string
}{
	{`^abcdefg`, "abcdefg"},
	{`a+`, "baaab"},
	{"abcd..", "abcdef"},
}

var goodRe = []string{
	`a*`,
	`[a-z]+`,
}

func Example() {
	_ = regexp.MustCompile(`foo.?`)
}
