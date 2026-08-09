"""Minimal test_re.py fixture for AST extraction."""
import re

class ReTests:
    def test_basic_search(self):
        self.assertEqual(re.search(r'[a-z]+', 'hello').group(), 'hello')

    def test_compile(self):
        p = re.compile(r'\d{3}-\d{4}')
        self.assertTrue(p.match('555-1234'))

    def test_fullmatch(self):
        self.assertTrue(re.fullmatch(r'[A-Z]{2}\d{4}', 'AB1234'))

    def test_sub(self):
        result = re.sub(r'(\w+)\s+(\w+)', r'\2 \1', 'hello world')
        self.assertEqual(result, 'world hello')

    def test_split(self):
        re.split(r'\s+', 'one two three')

    def test_ignorecase(self):
        re.match(r'[a-z]+', 'HELLO', re.I)

    def test_dynamic_pattern(self):
        pat = get_pattern()
        re.search(pat, 'text')

    def test_fstring_pattern(self):
        name = 'foo'
        re.search(f'{name}bar', 'foobar')
