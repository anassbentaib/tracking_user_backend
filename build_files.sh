#!/bin/bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput

# Add Python bin directory to PATH
export PATH="/python312/bin:$PATH"


echo "Gunicorn Path: $(which gunicorn)"

# Start Gunicorn
gunicorn --bind 0.0.0.0:8000 user-tracking.wsgi:application
