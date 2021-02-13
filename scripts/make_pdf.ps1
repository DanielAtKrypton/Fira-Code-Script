$script = "$PSScriptRoot\helpers\delete_docs_build_folder.ps1"
& $script

docs/make latex
docs/build/latex/make
mv docs/build/latex/automatedtradesystem.pdf docs/artifacts -Force