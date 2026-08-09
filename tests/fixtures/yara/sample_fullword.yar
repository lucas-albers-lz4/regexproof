rule fixture_fullword
{
    strings:
        $fw = "evil" fullword ascii
        $fw2 = /malicious/ fullword
    condition:
        any of them
}
