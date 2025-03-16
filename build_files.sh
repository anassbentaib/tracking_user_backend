#!/bin/bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput

# Ensure gunicorn is run from the installed directory
export PATH="$HOME/.local/bin:$PATH"
gunicorn --bind 0.0.0.0:8000 user-tracking.wsgi:application
