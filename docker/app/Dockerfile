FROM ubuntu:22.04
MAINTAINER Ben Keith <keitwb@gmail.com>
EXPOSE 8000

RUN DEBIAN_FRONTEND=noninteractive apt-get update -q && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq \
      python3-pip \
      python3-tk \
      python3-dev \
      libjpeg8-dev \
      libmemcached-dev \
      zlib1g-dev \
      build-essential \
      sqlite3 &&\
    apt-get clean

ENTRYPOINT ["/app/docker/app/entrypoint"]
ENV DJANGO_SETTINGS_MODULE=keithvaluation.settings

RUN useradd --home-dir /build --create-home --system --user-group --shell /bin/bash django &&\
    mkdir -p /app &&\
    chown django:django /app

USER django
ENV PYTHONUSERBASE=/build/python-base PATH=$PATH:/build/python-base/bin PYTHONPATH=/app PYTHONIOENCODING=UTF-8
COPY requirements.txt /app/requirements.txt
RUN mkdir -p $PYTHONUSERBASE &&\
    pip install --user -r /app/requirements.txt

USER root
RUN mkdir -p /logs/django /build/dist /media /data &&\
    chown -R django.django /logs/django /app /build /media /data

COPY docker/app /app/docker/app/
COPY manage.py /app/
COPY keithvaluation /app/keithvaluation/
WORKDIR /app

VOLUME ["/build/dist", "/data"]
