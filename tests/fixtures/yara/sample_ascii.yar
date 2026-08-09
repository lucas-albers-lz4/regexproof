rule fixture_ascii_regex
{
    strings:
        $r = /[a-z]+\d{2,4}/
    condition:
        $r
}

rule fixture_ascii_text
{
    strings:
        $t = "hello_world"
    condition:
        $t
}
