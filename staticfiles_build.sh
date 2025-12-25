#!/usr/bin/env bash
# Build step for Railway
python manage.py collectstatic --noinput
python manage.py migrate
