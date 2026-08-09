# Perl ground-truth helper

System-perl replay for Wave 3 SpamAssassin / perl t/re surfaces.
Never falls back to Python `re` (wrong engine = broken ground-truth gate).

## Provisioning

```bash
# Debian/Ubuntu CI: perl is usually preinstalled
perl -v                 # expect 5.38+ (pin documents 5.38.2; plan cited 5.40.1)
python helpers/perl/match.py version
python helpers/perl/match.py parse 'a+'
printf 'aaa' | python helpers/perl/match.py match 'a+' ''
```

Pin constant: `PERL_VERSION` in `match.py` (presence gate requires major.minor ≥ 5.38).

## Usage

```bash
python helpers/perl/match.py version
python helpers/perl/match.py parse '<pattern>'
printf '…' | python helpers/perl/match.py match '<pattern>' '<flags>'
```

Exit `0` = ok/match; `1` = parse fail / no match; `2` = perl missing or version mismatch.
