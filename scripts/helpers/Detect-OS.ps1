Function Detect-OS() {
    try { 
        $env_os=(Get-ChildItem -Path Env:OS -ErrorAction Stop)
    } catch {
        $env_os=(Get-ChildItem -Path Env:NAME -ErrorAction Stop)
    }
    $os_string = $env_os[0].Value
    if ($os_string.EndsWith("Linux")){
        $os = "Linux"
    }elseif ($os_string.StartsWith("Windows")) {
        $os = "Windows"
    }
    return $os
}