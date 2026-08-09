# YARA ground-truth helper

Temp-file replay for Wave 2 encoding-domain probes (ASCII + UTF-16LE `wide`).
Never uses stdin — probe bytes may contain NUL.

## Provisioning

```bash
brew install yara   # spike pin 4.5.8; CI uses apt `yara` (4.x)
# or: apt install yara
yara -v
yarac -v            # compile checks use yarac (yara -c is --count)
python helpers/yara/match.py version
```

## Usage

```bash
python helpers/yara/match.py compile path/to/rule.yar
python helpers/yara/match.py match path/to/rule.yar path/to/sample.bin
```

Exit `0` = compile ok / rule matched; `1` = compile fail / no match; `2` = yara missing.
