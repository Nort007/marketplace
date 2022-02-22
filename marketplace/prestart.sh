#!/usr/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
