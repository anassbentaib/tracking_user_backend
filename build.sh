#!/bin/bash

# Exit on error
set -o errexit  

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt  

# Run migrations
python manage.py migrate  

# Collect static files
python manage.py collectstatic --noinput  

# Create a superuser (optional, only if needed)
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell
