#!/usr/bin/env python3
# -*- mode: python -*-

# Re test suite and benchmark suite v1.5

# The 3 possible outcomes for each pattern
[SUCCEED, FAIL, SYNTAX_ERROR] = range(3)

# Benchmark suite (needs expansion)
#
# The benchmark suite does not test correctness, just speed.  The
# first element of each tuple is the regex pattern; the second is a
# string to match it against.  The benchmarking code will embed the
# second string inside several sizes of padding, to test how regex
# matching performs on large strings.

benchmarks = [

    # test common prefix
    ('Python|Perl', 'Perl'),    # Alternation
    ('(Python|Perl)', 'Perl'),  # Grouped alternation

    ('Python|Perl|Tcl', 'Perl'),        # Alternation
    ('(Python|Perl|Tcl)', 'Perl'),      # Grouped alternation

    ('(Python)\\1', 'PythonPython'),    # Backreference
    ('([0a-z][a-z0-9]*,)+', 'a5,b7,c9,'), # Disable the fastmap optimization
    ('([a-z][a-z0-9]*,)+', 'a5,b7,c9,'), # A few sets

    ('Python', 'Python'),               # Simple text literal
    ('.*Python', 'Python'),             # Bad text literal
    ('.*Python.*', 'Python'),           # Worse text literal
    ('.*(Python)', 'Python'),           # Bad text literal with grouping

]

# Test suite (for verifying correctness)
#
# The test suite is a list of 5- or 3-tuples.  The 5 parts of a
# complete tuple are:
# element 0: a string containing the pattern
#         1: the string to match against the pattern
#         2: the expected result (SUCCEED, FAIL, SYNTAX_ERROR)
#         3: a string that will be eval()'ed to produce a test string.
#            This is an arbitrary Python expression; the available
#            variables are "found" (the whole match), and "g1", "g2", ...
#            up to "g99" contain the contents of each group, or the
#            string 'None' if the group wasn't given a value, or the
#            string 'Error' if the group index was out of range;
#            also "groups", the return value of m.group() (a tuple).
#         4: The expected result of evaluating the expression.
#            If the two don't match, an error is reported.
#
# If the regex isn't expected to work, the latter two elements can be omitted.

tests = [
    # Test ?P< and ?P= extensions
    ('(?P<foo_123', '', SYNTAX_ERROR),      # Unterminated group identifier
    ('(?P<1>a)', '', SYNTAX_ERROR),         # Begins with a digit
    ('(?P<!>a)', '', SYNTAX_ERROR),         # Begins with an illegal char
    ('(?P<foo!>a)', '', SYNTAX_ERROR),      # Begins with an illegal char

    # Same tests, for the ?P= form
    ('(?P<foo_123>a)(?P=foo_123', 'aa', SYNTAX_ERROR),
    ('(?P<foo_123>a)(?P=1)', 'aa', SYNTAX_ERROR),
    ('(?P<foo_123>a)(?P=!)', 'aa', SYNTAX_ERROR),
    ('(?P<foo_123>a)(?P=foo_124', 'aa', SYNTAX_ERROR),  # Backref to undefined group

    ('(?P<foo_123>a)', 'a', SUCCEED, 'g1', 'a'),
    ('(?P<foo_123>a)(?P=foo_123)', 'aa', SUCCEED, 'g1', 'a'),

    # Test octal escapes
    ('\\1', 'a', SYNTAX_ERROR),    # Backreference
    ('[\\1]', '\1', SUCCEED, 'found', '\1'),  # Character
    ('\\09', chr(0) + '9', SUCCEED, 'found', chr(0) + '9'),
    ('\\141', 'a', SUCCEED, 'found', 'a'),
    ('(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)\\119', 'abcdefghijklk9', SUCCEED, 'found+"-"+g11', 'abcdefghijklk9-k'),

    # Test \0 is handled everywhere
    (r'\0', '\0', SUCCEED, 'found', '\0'),
