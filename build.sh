#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
python alx_travel_app/manage.py makemigrations --noinput
python alx_travel_app/manage.py migrate --noinput

# Collect static files
python alx_travel_app/manage.py collectstatic --no-input

# Create superuser automatically
python alx_travel_app/create_superuser.py
