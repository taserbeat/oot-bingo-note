#!/bin/bash

cd $(dirname $0)

if [ -e ./.venv/ ]; then
    rm -r ./.venv/
fi

export PIPENV_VENV_IN_PROJECT=true
pipenv sync --dev
