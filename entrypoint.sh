#!/bin/sh

python="/app/venv/bin/python"

/app/venv/bin/gunicorn wsgi:app --workers $GUNICORN_WORKERS --bind 0.0.0.0:8000
