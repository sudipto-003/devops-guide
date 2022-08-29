#!/bin/bash

unlink /etc/nginx/sites-enabled/default

touch /etc/nginx/sites-available/reveser_proxy.conf
# mv reverse_proxy.conf /etc/nginx/sites-available/reverse_proxy.conf 
# cat reverse_proxy.conf >> /etc/nginx/sites-available/reverse_proxy.conf
# cat reverse_proxy.conf | tee /etc/nginx/sites-available/reverse-proxy.conf >> /dev/null

ln -s /etc/nginx/sites-available/reverse_proxy.conf /etc/nginx/sites-enabled/reverse_proxy.conf

service nginx configtest
service nginx restart