#!/bin/bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput

# Use full path to gunicorn
/python312/bin/gunicorn --bind 0.0.0.0:8000 user-tracking.wsgi:application
