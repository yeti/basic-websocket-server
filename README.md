# Basic Websocket Server

## What OS is this compatible with?
This will set itself up _ONLY_ on Ubuntu 16.04 (Xenial).

## What is packaged here?
We have a shell pipeline in `src/setup` that installs the _bare_minimum_ required to install/setup the following things:

* Pyenv (with Python 3.5.2)
* Redis
* Nginx
* A Python Websocket server that wraps Redis PUBSUB functionality

The end result is a server that accepts PUBLISH requests at `ws://<url-to-server>/<channel>:8766` and SUBSCRIBE requests at `ws://<url-to-server>/<channel>:8768`.

## How do I set this baby up _in the cloud_?

SSH into your cloud VPS _as `root`_. Then do the following:
 
