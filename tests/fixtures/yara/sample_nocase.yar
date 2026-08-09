rule fixture_nocase
{
    strings:
        $nc = "Mimikatz" nocase
        $nc_regex = /sekurlsa::/ nocase
    condition:
        any of them
}
