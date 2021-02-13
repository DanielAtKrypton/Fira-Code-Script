# Example: 
# pwsh ./Start-Windows-App.ps1 "C:\Program Files\Mozilla Firefox\firefox.exe" www.wikipedia.com 
function Inform-Program-Launch($file_path){
    $child_item = Get-ChildItem $file_path
    $program_name = (Get-Culture).TextInfo.ToTitleCase($child_item.BaseName)
    Write-Host 🚀 'Launching ' -NoNewLine
    $boldify = "`e[1m"
    $deboldify = "`e[0m"
    Write-Host "$boldify$program_name$deboldify" -ForeGroundColor Blue -NoNewLine
    Write-Host ...❕
}

function Start-Windows-App($_file_path, $app_args){
    $file_path = wslpath $_file_path
    Inform-Program-Launch $file_path
    Start-Process -FilePath $file_path $app_args
}
$args = [Environment]::GetCommandLineArgs()
# $args[0] = pwsh
# $args[1] = this file
Write-Host $args[0]
if ($args.length -gt 2){
   $app_args = $args[2..($args.length-1)]
}
else{
   $app_args = @()
}
Start-Windows-App @app_args