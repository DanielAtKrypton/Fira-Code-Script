# python -m src.main
# ttx ./assets/SCRPT12N.TTF

$temp="./temporary_folder"
# mkdir $temp

# hublatest -c ./assets/fira_code_config.ini

# # delete downloaded zip becaause extraction already took place.
# Get-ChildItem $temp/download_files/* -Include *.zip -Recurse | Remove-Item

# # generate open ttx format for each font
# Get-ChildItem $temp/download_files/tonsky/FiraCode/extracted_files/ttf/*.ttf `
# -Include *-Bold.ttf,*-Regular.ttf | ForEach-Object {ttx -d $temp $_}

python -m fira_code_i_script.main -i $temp/FiraCode-Bold.ttx
# mkdir ./dist