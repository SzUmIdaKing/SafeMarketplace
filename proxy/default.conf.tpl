server {
    listen                      443 ssl;

    ssl_certificate             /etc/nginx/nginx.crt;
    ssl_certificate_key         /etc/nginx/nginx.key;
    
    ssl_protocols               TLSv1.2 TLSv1.3;
    ssl_ciphers                 HIGH:!aNULL:!MD5;
    
    ssl_prefer_server_ciphers   on;
    ssl_session_cache           shared:SSL:10m;
    ssl_session_timeout         10m;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options nosniff always;
    add_header X-XSS-Protection "1; mode=block" always;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}
