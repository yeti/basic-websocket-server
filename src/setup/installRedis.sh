#!/bin/bash

echo "===> Installing Redis"
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make

mv src/redis-server /usr/local/bin/
mv src/redis-cli /usr/local/bin/

mkdir /etc/redis
mkdir /var/redis

mv utils/redis_init_script /etc/init.d/redis_6379
mv redis.conf /etc/redis/6379.conf
. ../configureRedis.sh

mkdir /var/redis/6379

update-rc.d redis_6379 defaults

echo "======> Starting Redis"
/etc/init.d/redis_6379 start

cd ../

echo "======> Clean up Redis build files"
rm -rf ./redis-stable*
