#!/bin/bash

source ~/.bash_profile

pushd ~/harvester
java -jar sensor-web-harvester-0.12-SNAPSHOT.jar -metadata $1
java -jar sensor-web-harvester-0.12-SNAPSHOT.jar -writeiso $1
cd ~/harvester/iso
git checkout master && git add . && git commit -m "$2 - Auto SWH commit" && git pull && git push origin master
popd

if [ ! -z "$2" ]; then
  cd ~/glos_catalog/basex
  bash populate_git.sh /home/harvester/glos_catalog/ISOs $2
fi
