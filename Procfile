web: gunicorn gen_zone.wsgi
web: python gen_zone/manage.py makemigrations --noinput && python gen_zone/manage.py migrate --noinput && gunicorn gen_zone.wsgi
