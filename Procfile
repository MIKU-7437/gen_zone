web: pip install -r requirements.txt && python gen_zone/manage.py migrate --noinput && python gen_zone/manage.py makemigrations --noinput && python gen_zone/manage.py migrate --noinput && gunicorn gen_zone.wsgi:application
