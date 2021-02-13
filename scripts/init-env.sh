#!/bin/bash -x

init-env(){
    python -m venv .venv
    . .venv/bin/activate
    # reactivate with zsh 
    # https://stackoverflow.com/questions/45216663/how-to-automatically-activate-virtualenvs-when-cding-into-a-directory
    current_dir=$(basename "$PWD")
    cd ..
    cd $current_dir
    python -m pip install --upgrade pip
    pip install wheel
    pip install pip-tools
    pip-sync ./requirements/requirements.txt
    pip install -e .[dev,test,docs]
}