web: sh -c 'cd gen_zone && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn gen_zone.wsgi:application'
