#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python alx_travel_app/manage.py collectstatic --no-input
python alx_travel_app/manage.py migrate
