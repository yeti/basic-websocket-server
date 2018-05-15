#!/bin/bash

echo "===> Setup Nginx"
cd /server
cp ws.conf /etc/nginx/sites-enabled

echo "===> Restart Nginx"

service nginx restart
