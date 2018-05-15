#!/bin/bash
echo "===> Installing Dependencies"
sudo apt-get update
sudo apt-get install -y git make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev vim nginx