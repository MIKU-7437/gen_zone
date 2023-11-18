web: gunicorn gen_zone.wsgi
web: pip install -r requirements.txt
web: python gen_zone/manage.py makemigrations --noinput && python gen_zone/manage.py migrate --noinput && gunicorn gen_zone.wsgi
