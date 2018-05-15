#!/bin/bash
cd /server/setup
. ./installDeps.sh
. ./installPyenv.sh
. ./installRedis.sh
. ./pyenvSetup.sh
. ./installPythonDeps.sh
. ./nginxSetup.sh
