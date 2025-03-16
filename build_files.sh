#!/bin/bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput

# Add Python 3.13 bin directory to PATH
export PATH="/Library/Frameworks/Python.framework/Versions/3.13/bin:$PATH"

# Start Gunicorn
gunicorn --bind 0.0.0.0:8000 user-tracking.wsgi:application
