#!/bin/bash
echo "======> Configuring Redis"
sed -i 's!daemonize no!daemonize yes!' /etc/redis/6379.conf
sed -i 's!logfile ""!logfile /var/log/redis_6379.log!' /etc/redis/6379.conf
sed -i 's!loglevel notice!loglevel debug!' /etc/redis/6379.conf
sed -i 's!dir ./!dir /var/redis/6379!' /etc/redis/6379.conf
