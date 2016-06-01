FROM nginx:1.10.0
MAINTAINER Ben Keith <keitwb@gmail.com>

ENTRYPOINT ["/bin/bash", "-ec"]
CMD ["\
  envsubst '$APP_HOSTNAME:$ADMIN_HOSTNAME' < /etc/nginx/conf.d/kv.template > /etc/nginx/conf.d/kv.conf &&\
  exec nginx -g 'daemon off;' \
  "]

RUN rm /etc/nginx/conf.d/default.conf
ARG PROTOCOL
COPY kv-${PROTOCOL}.template /etc/nginx/conf.d/kv.template
