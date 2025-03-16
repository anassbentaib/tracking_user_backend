#!/bin/bash
set -e  # Stop the script if any command fails

echo "Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Running collectstatic..."
python3 manage.py collectstatic --noinput

echo "Ensuring Gunicorn is installed..."
python3 -m pip show gunicorn || python3 -m pip install gunicorn

echo "Fixing PATH issue..."
export PATH="/python312/bin:$PATH"

echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:8000 user-tracking.wsgi
