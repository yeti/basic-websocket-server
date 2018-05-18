# Basic Websocket Server

## What OS is this compatible with?
This will set itself up _ONLY_ on Ubuntu 16.04 (Xenial).

## What is packaged here?
We have a shell pipeline in `src/setup` that installs the _bare_minimum_ required to install/setup the following things:

* pyenv (with Python 3.5.2)
* redis
* nginx
* A python Websocket server that wraps redis PUBSUB functionality

The end result is a server that accepts PUBLISH traffic at `ws://<url-to-server>/<channel>:8766` and SUBSCRIBE traffic at `ws://<url-to-server>/<channel>:8768`.

## How do I set this baby up _in the cloud_?

SSH into your cloud VPS _as `root`_. Then do the following:

```
mkdir /server
git clone git://github.com/yeti/basic-websocket-server.git /server
mv /server/src/* /server
. /server/setup/setup.sh
```

Then run the PUBSUB servers!
```
python /server/src/publisher.py & python /server/src/subscriber.py &
```

## How do I try this out locally?
Have the following things installed on your local machine:

* Vagrant
* Docker (if on Mac, do Docker for Mac and make sure it's running)

Fork a copy of the websocket server from [here](https://github.com/yeti/basic-websocket-server.git).

Then, run the following:

```
git clone git@github.com:<your-username>/basic-websocket-server.git
cd basic-websocket-server
vagrant up
```

Vagrant automatically runs `/server/setup/setup.sh` in its provisioning sequence.

To run the server:
```
vagrant ssh
sudo su
python /server/publisher.py & python /server/subscriber.py &
```

## How to Contribute

Fork this project and follow the `How do I try this out locally?` instructions
to have a local copy to test and work on.

## Authentication/Authorization

This server accepts a Base64-encoded '<username>:<password>' type string through the `Sec-WebSocket-Protocol` request
handler, ONLY IF the `AUTHORIZATION_TOKEN` env var is set while running. If `AUTHORIZATION_TOKEN` is
not set, then the server is completely public.

`AUTHORIZATION_TOKEN` must be an Argon2 hash of the desired username and
password sent through `Sec-WebSocket-Protocol`. To generate it, have Python interpret
the `print_argon2_token.py` file directly like so:

```
python /path/to/print_argon2_token.py <username>:<password>
```

This will print out the token that you can then set `AUTHORIZATION_TOKEN` to.

## Configuration Files

* `src/ws.conf`: This is the Nginx configuration for the Websocket Servers. On
                 production, feel free to edit this to do things like enable
                 encryption behind SSL.
* `src/ws.ini`:  This is a Supervisor configuration. Since the websocket servers
                 are written with Python 3.5.2 but Supervisor requires
                 Python 2.6-2.7, it's slightly less intuitive to hook supervisor
                 up well. It is possible however, since the `setup.sh` routine
                 installs pyenv, to install Python 2.7 and setup Supervisor to
                 point to this file.
