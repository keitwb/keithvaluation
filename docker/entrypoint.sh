#!/bin/bash

if [[ -n $DO_DJANGO_SETUP ]]
then
  python /app/manage.py migrate
  python /app/manage.py collectstatic
fi

exec $@
