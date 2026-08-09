// Minimal mjsunit-style smoke for v8_mjsunit extractor.
assertEquals("a:b", "a b".split(/\s/).join(":"));
var re = new RegExp("foo[0-9]+");
assertTrue(/bar/i.test("BAR"));
// comment should not yield: /phantom/
/* new RegExp("also-phantom") */
