web: gunicorn gen_zone.wsgi
web: python manage.py makemigrations --noinput && python manage.py migrate --noinput && gunicorn gen_zone.wsgi
