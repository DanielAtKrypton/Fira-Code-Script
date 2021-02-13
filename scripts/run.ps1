$temp="temporary_folder"
if(!(Test-Path -Path $temp )){
    New-Item -ItemType directory -Path $temp
}
ttx -d $temp ./assets/SCRPT12N.TTF

hublatest -c ./assets/fira_code_config.ini

# delete downloaded zip becaause extraction already took place.
Get-ChildItem $temp/download_files/* -Include *.zip -Recurse | Remove-Item

# generate open ttx format for each font
Get-ChildItem $temp/download_files/tonsky/FiraCode/extracted_files/ttf/*.ttf `
-Include *-Bold.ttf,*-Regular.ttf | ForEach-Object {ttx -d $temp $_}

# remove source ttf fonts.
del $temp/*.ttf

python -m fira_code_script.main -i "$temp/FiraCode-Regular.ttx" -m "process_raw_font"
python -m fira_code_script.main -i "$temp/FiraCode-Bold.ttx" -m "process_raw_font"
python -m fira_code_script.main -i "$temp/SCRPT12N.ttx" -m "process_italic_font"

rm  "$temp/FiraCode-Regular.ttx" "$temp/FiraCode-Bold.ttx" "$temp/SCRPT12N.ttx"

# generate open ttf format for each font
Get-ChildItem $temp/*.ttx | ForEach-Object {ttx -d $temp $_}

$dist="dist"
if(!(Test-Path -Path $dist )){
    New-Item -ItemType directory -Path $dist
}
mv $temp/*.ttf $dist