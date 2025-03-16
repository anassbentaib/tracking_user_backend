#!/bin/bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput

# Add Python bin directory to PATH dynamically
export PATH="$(python3 -m site --user-base)/bin:$PATH"

# Debug: Check if gunicorn is accessible
echo "Gunicorn Path: $(which gunicorn)"

# Start Gunicorn
gunicorn --bind 0.0.0.0:8000 user-tracking.wsgi:application
