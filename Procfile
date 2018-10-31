release: python manage.py migrate --run-syncdb
release: python manage.py collectstatic --noinput
web: newrelic-admin run-program gunicorn artwork_image_processor_site.wsgi
