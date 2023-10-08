#!/bin/bash -eu

cd $(dirname $0)/..

python3 -m venv .venv

source .venv/bin/activate

pip install -r ./python/requirements.txt

deactivate
