#!/bin/bash

# Create and activate a virtual environment
echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip to avoid dependency issues
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static..."
python manage.py collectstatic --noinput --clear
