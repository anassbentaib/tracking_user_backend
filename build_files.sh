#!/bin/bash
set -e  # Exit immediately if any command fails

echo "Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Running collectstatic..."
python3 manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:8000 user-tracking.wsgi
