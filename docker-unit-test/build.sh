#!/usr/bin/env bash

VERSION=3.7.4-stretch
if [ "$1" != "" ];then
  VERSION=$1
fi

cp ../Dockerfile ../Dockerfile2

sed -e "s/version-number/$VERSION/g" DockerfileTemplate > ../Dockerfile
docker build -t "tbk-sdk-python-unittest" ..

cp ../Dockerfile2 ../Dockerfile
rm -rf ../Dockerfile2
