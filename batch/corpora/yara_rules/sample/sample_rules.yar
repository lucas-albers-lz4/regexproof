rule sample_plain_ascii
{
    meta:
        description = "Plain ASCII string match"
        author = "test"
    strings:
        $a = /https?:\/\/[a-zA-Z0-9\.\-]+/
        $b = "malware_config"
    condition:
        any of them
}

rule sample_wide_ascii
{
    meta:
        description = "Both wide and ascii domain"
    strings:
        $s1 = "CreateRemoteThread" ascii wide
        $s2 = /cmd\.exe/ ascii wide
    condition:
        any of them
}

rule sample_nocase
{
    meta:
        description = "Case-insensitive match"
    strings:
        $a = "Password" nocase
        $b = /admin(istrator)?/ nocase
    condition:
        any of them
}

rule sample_wide_only
{
    meta:
        description = "Wide-only domain"
    strings:
        $w = "kernel32.dll" wide
    condition:
        $w
}

rule sample_fullword
{
    meta:
        description = "Fullword modifier (alnum token bounds)"
    strings:
        $f = "evil" fullword ascii
    condition:
        $f
}

rule sample_complex_regex
{
    meta:
        description = "Complex regex patterns"
    strings:
        $r1 = /[A-Za-z0-9+\/]{40,}={0,2}/
        $r2 = /\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/
        $r3 = /[0-9a-fA-F]{32,64}/
    condition:
        any of them
}

rule sample_xor_reject
{
    meta:
        description = "xor modifier should be rejected as unsupported"
    strings:
        $x = "secret_key" xor
    condition:
        $x
}

rule sample_base64_reject
{
    meta:
        description = "base64 modifier should be rejected"
    strings:
        $b = "password" base64
    condition:
        $b
}
