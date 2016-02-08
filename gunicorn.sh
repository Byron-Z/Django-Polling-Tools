#!/bin/bash

DJANGODIR=/opt/survey             		# Django project directory
USER=root                                       # the user to run as
GROUP=root                                      # the group to run as
NUM_WORKERS=1                                   # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=survey.settings          # which settings file should Django use
DJANGO_WSGI_MODULE=survey.wsgi                  # WSGI module name
LOG=/var/log/gunicorn.log			# Log path

# Start your Django Unicorn
exec /usr/local/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=127.0.0.1:8001 \
  --log-level=warning \
  --log-file=$LOG \
  --reload
