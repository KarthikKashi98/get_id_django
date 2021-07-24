release: python manage.py makemigrations ; python manage.py migrate
web: gunicorn --pythonpath djangoProject6 djangoProject6.wsgi --log-file -