from pyiso.collectors.thredds import ThreddsCollector
from pyiso.collectors.geo import GeoCollector
from pyiso.collectors.insitu import InSituCollector

import requests
from urlparse import urlsplit
import os
import codecs


def main():

    base_download_path = "/home/dev/Development/glos_catalog/ISOs"

    # The ID in THREDDS needs to contain one of these strings to be identified.
    
    # We only want the Agg and FMRC datasets
    datasets = ["SST-Agg", "SST-FMRC"]
    # Don't process the "files/" lists
    skips = ["files/"]
    aoc = ThreddsCollector("http://tds.glos.us:8080/thredds/aoc.html", datasets=datasets, skips=skips).run()
    for d in aoc:
        f = os.path.basename(urlsplit(d).path) + ".xml"
        with open(os.path.join(base_download_path, "Satellite", f), "w") as handle:
            handle.write(requests.get(d).text)
    
    
    # We only want the all year best datasets
    datasets = ["2D_best", "3D_best", "2D_-_All_Years_best", "3D_-_All_Years_best"]
    # Don't process the "files/" lists
    skips = ["files/"]
    aoc = ThreddsCollector("http://tds.glos.us:8080/thredds/glcfs/glcfs.html", datasets=datasets, skips=skips).run()
    for d in aoc:
        f = os.path.basename(urlsplit(d).path) + ".xml"
        with open(os.path.join(base_download_path, "Models", "GLCFS", f), "w") as handle:
            handle.write(requests.get(d).text)

    
    # We only want the Agg and Latest
    datasets = ["Nowcast-Agg", "Lastest-Forecast"]
    # Don't process the "files/" lists
    skips = ["Nowcast - Individual Files/", "Forecast - Individual Files/"]
    aoc = ThreddsCollector("http://tds.glos.us:8080/thredds/hecwfs/hecwfs.html", datasets=datasets, skips=skips).run()
    for d in aoc:
        f = os.path.basename(urlsplit(d).path) + ".xml"
        with open(os.path.join(base_download_path, "Models", "HECWFS", f), "w") as handle:
            handle.write(requests.get(d).text)
    
    
    # We only want the Agg and Latest
    datasets = ["Nowcast-Agg", "Lastest-Forecast"]
    # Don't process the "files/" lists
    skips = ["Nowcast - Individual Files/", "Forecast - Individual Files/"]
    aoc = ThreddsCollector("http://tds.glos.us:8080/thredds/slrfvm/slrfvm.html", datasets=datasets, skips=skips).run()
    for d in aoc:
        f = os.path.basename(urlsplit(d).path) + ".xml"
        with open(os.path.join(base_download_path, "Models", "SLRFVM", f), "w") as handle:
            handle.write(requests.get(d).text)
    
    
    isos = GeoCollector("http://data.glos.us/metadata").run()
    for d in isos:
        # Get the ID
        uid = urlsplit(d).query
        uid = uid[uid.index("=")+1:]
        f = "GeoNetwork-" + uid + ".xml"
        new_file = os.path.join(base_download_path, "GeoNetwork", f)
        with codecs.open(new_file, "w", "utf-8") as handle:
            handle.write(requests.get(d).text)
    
    isos = InSituCollector("http://64.9.200.113:8080/isos", "ndbc").run()
    for d in isos:
        f = os.path.basename(urlsplit(d).path)
        with open(os.path.join(base_download_path, "In-situ", "ndbc", f), "w") as handle:
            handle.write(requests.get(d).text)
    

    isos = InSituCollector("http://64.9.200.113:8080/isos", "storet").run()
    for d in isos:
        f = os.path.basename(urlsplit(d).path)
        with open(os.path.join(base_download_path, "In-situ", "storet", f), "w") as handle:
            handle.write(requests.get(d).text)

main()

exit(0)
