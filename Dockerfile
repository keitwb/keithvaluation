FROM ubuntu:14.04
MAINTAINER Ben Keith <keitwb@gmail.com>
EXPOSE 80

RUN DEBIAN_FRONTEND=noninteractive apt-get update -q && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq python-pip python-tk python-dev python-setuptools libjpeg8-dev zlib1g-dev build-essential && \
    apt-get clean

ENTRYPOINT ["/app/docker/entrypoint.sh"]

RUN mkdir /app && \
    useradd -d /app -M -r django && \
    chown django.django -R /app

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app
CMD ["gunicorn", "-c", "/app/docker/gunicorn-config.py", "keithvaluation.wsgi"]
