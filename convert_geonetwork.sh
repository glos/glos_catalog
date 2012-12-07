#!/bin/bash
for f in `find ISOs/GeoNetwork -name metadata.xml`; do
    sed -i -e 's/gmd:MD_Metadata/gmi:MI_Metadata/g' -e 's/gmi:MI_Metadata\ /gmi:MI_Metadata\ xmlns:gmi="http:\/\/www.isotc211.org\/2005\/gmi"\ /g' $f
done