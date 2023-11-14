FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./nginx/* /etc/nginx/
COPY ./run.sh /run.sh

ENV APP_HOST=app
ENV APP_PORT=9000

USER root

RUN apk add --no-cache openssl bash
RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    chmod +x /run.sh

VOLUME /vol/static
VOLUME /vol/www

USER nginx

CMD ["/run.sh"]