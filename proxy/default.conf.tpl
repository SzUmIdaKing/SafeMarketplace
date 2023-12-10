server {
    listen                      443 ssl;

    ssl_certificate             /etc/nginx/nginx.crt;
    ssl_certificate_key         /etc/nginx/nginx.key;
    
    ssl_protocols               TLSv1.2 TLSv1.3;
    ssl_ciphers                 HIGH:!aNULL:!MD5;
    
    ssl_prefer_server_ciphers   on;
    ssl_session_cache           shared:SSL:10m;
    ssl_session_timeout         10m;

    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options SAMEORIGIN;
    add_header X-XSS-Protection "1; mode=block";
    add_header Content-Security-Policy "default-src 'self'; script-src 'self' https://cdn.tailwindcss.com/ 'unsafe-inline'; style-src 'self' 'unsafe-inline';";


    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}