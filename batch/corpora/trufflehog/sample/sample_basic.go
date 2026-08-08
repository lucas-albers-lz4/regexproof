package sample

import "regexp"

var pat = regexp.MustCompile(`[a-z]{3,8}`)
var pat2 = regexp.MustCompile("foo[0-9]+bar")
