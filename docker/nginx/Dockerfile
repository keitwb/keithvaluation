FROM ubuntu:14.04
MAINTAINER Ben Keith <keitwb@gmail.com>
EXPOSE 8000

ENTRYPOINT ["/entrypoint"]

RUN DEBIAN_FRONTEND=noninteractive apt-get update -q && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq nginx && \
    apt-get clean

RUN echo 'daemon off;' >> /etc/nginx/nginx.conf

COPY entrypoint /entrypoint
COPY keithvaluation.conf /tmp/site-template.conf
