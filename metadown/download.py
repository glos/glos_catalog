from metadown.collectors.thredds import ThreddsCollector
from metadown.collectors.geonetwork import GeoNetworkCollector
from metadown.downloader import XmlDownloader

import os
import sys

def main(base_download_path):

    # selects: The ID in THREDDS needs to contain one of these strings to be identified.
    # skips: The LINK path in the actual thredds catalog webpage can't be equal to any of these strings
    
    # We only want the Agg selects
    selects = ["SST-Agg"]
    # Don't process the "files/" lists
    skips = ["files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/mtri/aoc.html", selects=selects, skips=skips).run()
    download_path = os.path.join(base_download_path, "Satellite")
    XmlDownloader.run(isos, download_path)

    # We only want the Agg selects
    selects = ["CHL-Agg"]
    # Don't process the "files/" lists
    skips = ["files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/mtri/chl.html", selects=selects, skips=skips).run()
    download_path = os.path.join(base_download_path, "Satellite")
    XmlDownloader.run(isos, download_path)

    # We only want the Agg selects
    selects = ["NC-Agg"]
    # Don't process the "files/" lists
    skips = ["files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/mtri/natcolor.html", selects=selects, skips=skips).run()
    download_path = os.path.join(base_download_path, "Satellite")
    XmlDownloader.run(isos, download_path)

    # We only want the all year best selects
    selects = ["2D_best", "3D_best", "2D_-_All_Years_best", "3D_-_All_Years_best"]
    # Don't process the "files/" lists
    skips = ["files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/glcfs/glcfs.html", selects=selects, skips=skips).run()
    download_path = os.path.join(base_download_path, "Models", "GLCFS")
    XmlDownloader.run(isos, download_path)

    # We only want the Agg and Latest
    selects = ["Nowcast-Agg", "Lastest-Forecast"]
    # Don't process the "files/" lists
    skips = ["Nowcast - Individual Files/", "Forecast - Individual Files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/hecwfs/hecwfs.html", selects=selects, skips=skips).run()
    download_path = os.path.join(base_download_path, "Models", "HECWFS")
    XmlDownloader.run(isos, download_path)
    
    # We only want the Agg and Latest
    selects = ["Nowcast-Agg", "Lastest-Forecast"]
    # Don't process the "files/" lists
    skips = ["Nowcast - Individual Files/", "Forecast - Individual Files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/slrfvm/slrfvm.html", selects=selects, skips=skips).run()
    download_path = os.path.join(base_download_path, "Models", "SLRFVM")
    XmlDownloader.run(isos, download_path)

    isos = GeoNetworkCollector("http://data.glos.us/metadata").run()
    download_path = os.path.join(base_download_path, "GeoNetwork")
    XmlDownloader.run(isos, download_path, namer=GeoNetworkCollector.namer, modifier=GeoNetworkCollector.modifier)   

main(sys.argv[1])

exit(0)
