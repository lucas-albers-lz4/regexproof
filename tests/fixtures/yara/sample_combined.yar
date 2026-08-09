rule fixture_combined_modifiers
{
    strings:
        $nc_wide = "RunDLL32" nocase wide ascii
        $nc_fw = "inject" nocase fullword
    condition:
        any of them
}
