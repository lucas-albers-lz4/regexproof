#!./perl
# Minimal .t smoke for perl_tre extractor.
use strict;
like("abc", qr/a+b?c+/, "basic qr");
ok("def" =~ /d.f/, "match op");
unlike("xyz", qr/a+/, "unlike");
