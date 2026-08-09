rule fixture_wide_only
{
    strings:
        $w = "kernel32" wide
    condition:
        $w
}

rule fixture_ascii_wide
{
    strings:
        $aw = "VirtualAlloc" ascii wide
    condition:
        $aw
}
