rule fixture_unsupported_xor
{
    strings:
        $x = "secret" xor
    condition:
        $x
}

rule fixture_unsupported_base64
{
    strings:
        $b = "token" base64
    condition:
        $b
}

rule fixture_unsupported_base64wide
{
    strings:
        $bw = "apikey" base64wide
    condition:
        $bw
}
