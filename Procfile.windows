release: python manage.py migrate --run-syncdb
web: newrelic-admin run-program gunicorn artwork_image_processor_site.wsgi