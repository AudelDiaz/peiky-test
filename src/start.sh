!#/bin/bash
cd usr/src/app
./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic --no-input
gunicorn -w 4 stores_app.wsgi:application -b :8000 -t 3600 --reload