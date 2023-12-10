FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh
COPY ./nginx.crt /etc/nginx/nginx.crt
COPY ./nginx.key /etc/nginx/nginx.key

ENV APP_HOST=app
ENV APP_PORT=9000

USER root

RUN chown nginx:nginx /etc/nginx/nginx.key && \
    chmod 600 /etc/nginx/nginx.key && \
    mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

USER nginx

CMD ["/run.sh"]