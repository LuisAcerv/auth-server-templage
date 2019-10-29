#!/bin/bash

set -e

echo '\e[1;32m'Running Zupp Virtual Machine'\e[0m'
docker stop zuppvm || true && docker rm -f zuppvm || true
docker run -t -d --name zuppvm ubuntu:18.04

docker exec -ti zuppvm /bin/bash -c """
echo  Configuring zuppvm && \
apt-get update && \
apt-get install wget -y && \
apt-get install nano -y && \

echo  '\e[1;32m'Downloading multichain'\e[0m' && \
cd /tmp && \
wget https://www.multichain.com/download/multichain-2.0.3.tar.gz && \
tar -xvzf multichain-2.0.3.tar.gz && \
cd multichain-2.0.3 && \
mv multichaind multichain-cli multichain-util /usr/local/bin && \

echo  '\e[1;32m'Creating main chain'\e[0m' && \
multichain-util create mainchain-dev && \
multichaind mainchain-dev -daemon && \

echo Configuring...
cd ..
cd ..
mkdir mainchain-dev && cd mainchain-dev
multichain-cli mainchain-dev getinfo >> chaininfo.json
echo Zupp virtual machine is running
"""