#!/bin/sh

until timeout 5s celery -A celery_app:app inspect ping; do
    >&2 echo "Celery workers not available"
done

echo 'Starting flower'
celery -A celery_app:app flower --port=5555 --broker=redis://redis:6379/0
