#!/bin/bash
python3 RandFIng/manage.py makemigrations
python3 RandFIng/manage.py migrate
python RandFIng/manage.py migrate --run-syncdb
python3 RandFIng/manage.py collectstatic
gunicorn --bind 127.0.0.1:8150 --chdir RandFIng/ RandFIng.wsgi:application
