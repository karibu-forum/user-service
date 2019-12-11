#!/bin/sh

echo "waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "postgresql started"

python manage.py runserver
