#!/bin/bash

set -e

echo '\e[1;32m'Creating seed network'\e[0m'
docker stop zuppvm || true && docker rm -f zuppvm || true
docker run -t -d --name zuppvm ubuntu:18.04

echo  '\e[1;32m'Configuring root node'\e[0m'
docker exec -ti zuppvm /bin/bash -c """
apt-get update && \
apt-get install wget -y && \
apt-get install nano -y && \
apt-get install ufw -y && \

echo  '\e[1;32m'Downloading multichain'\e[0m' && \
cd /tmp && \
wget https://zupp-assets.s3.amazonaws.com/multichain-2.0.3.tar.gz && \
tar -xvzf multichain-2.0.3.tar.gz && \
cd multichain-2.0.3 && \
mv multichaind multichain-cli multichain-util /usr/local/bin && \

echo  '\e[1;32m'Creating main chain'\e[0m' && \
multichain-util create root && \

echo Configuring...
cd ..
cd ..
mkdir root && cd root
multichain-cli root getinfo >> chaininfo.json

echo Setting-up RPC
cd
cd .multichain/root/
ls -la
cat multichain.conf
echo 'rpcallowip=0.0.0.0/0' >> multichain.conf
cat multichain.conf

echo Configure params

sed -i '/chain-description = MultiChain root     # Chain description, embedded in genesis block coinbase, max 90 chars./c\chain-description = Zupp root          # Chain description, embedded in genesis block coinbase, max 90 chars.' params.dat
sed -i '/anyone-can-send = false                 # Anyone can send, i.e. transaction signing not restricted by address./c\anyone-can-send = true                 # Anyone can send, i.e. transaction signing not restricted by address.' params.dat
sed -i '/anyone-can-receive = false              # Anyone can receive, i.e. transaction outputs not restricted by address./c\anyone-can-receive = true              # Anyone can receive, i.e. transaction outputs not restricted by address.' params.dat
sed -i '/anyone-can-create = false               # Anyone can create new streams./c\anyone-can-create = true               # Anyone can create new streams.' params.dat

cat params.dat

echo Starging node
multichaind root -daemon && \

sleep 8

echo Create zupp stream
multichain-cli root create stream zupp false
multichain-cli root subscribe zupp
multichain-cli root publish zupp 'Welcome to zupp' 48656C6C6F20576F726C64210A
exit
"""
[ -e app/blockchaininfo.json ] && rm app/blockchaininfo.json
[ -e app/.env ] && rm app/.env
docker exec -ti zuppvm /bin/bash -c 'cd && cat ~/.multichain/root/multichain.conf' >> app/.env
docker exec -ti zuppvm /bin/bash -c 'multichain-cli root getinfo' >> app/blockchaininfo.json
sed -i '1d' app/blockchaininfo.json 
echo '\e[1;32m'Zupp virtual machine is running'\e[0m'
