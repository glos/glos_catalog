#!/bin/bash

pushd ~/sensor-web-harvester
git pull
mvn clean package -DskipTests && cp -v target/sensor-web-harvester*.jar ../harvester
popd

