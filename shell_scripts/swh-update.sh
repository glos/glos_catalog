#!/bin/bash

pushd ~/harvester
java -jar sensor-web-harvester-0.12-SNAPSHOT.jar -updatesos $@
popd
