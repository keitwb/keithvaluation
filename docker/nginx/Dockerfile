FROM nginx:1.23
MAINTAINER Ben Keith <keitwb@gmail.com>

ENTRYPOINT ["/bin/bash", "-ec"]
CMD ["\
  envsubst '$APP_HOSTNAME:$ADMIN_HOSTNAME' < /etc/nginx/conf.d/kv.template > /etc/nginx/conf.d/kv.conf &&\
  echo 'User-agent: *' > /etc/nginx/robots.txt.template &&\
  echo 'Disallow: $DISALLOW' >> /etc/nginx/robots.txt.template &&\
  envsubst '$DISALLOW' < /etc/nginx/robots.txt.template > /etc/nginx/robots.txt &&\
  exec nginx -g 'daemon off;' \
  "]

ARG PROTOCOL
COPY kv-${PROTOCOL}.template /etc/nginx/conf.d/kv.template
