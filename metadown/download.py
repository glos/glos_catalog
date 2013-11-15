from metadown.collectors.thredds import ThreddsCollector
from metadown.collectors.geonetwork import GeoNetworkCollector
from metadown.downloader import XmlDownloader

import os
import sys

def main(base_download_path):

    # selects: The ID in THREDDS needs to contain one of these strings to be identified.
    # skips: The LINK path in the actual thredds catalog webpage can't be equal to any of these strings
    
    # We only want the Agg selects
    selects = [".*SST-Agg"]
    isos = ThreddsCollector("http://tds.glos.us/thredds/mtri/aoc.html", selects=selects).run()
    download_path = os.path.join(base_download_path, "Satellite")
    XmlDownloader.run(isos, download_path)

    # We only want the Agg selects
    selects = [".*CHL-Agg"]
    isos = ThreddsCollector("http://tds.glos.us/thredds/mtri/chl.html", selects=selects).run()
    download_path = os.path.join(base_download_path, "Satellite")
    XmlDownloader.run(isos, download_path)

    # We only want the Agg selects
    selects = [".*NC-Agg"]
    isos = ThreddsCollector("http://tds.glos.us/thredds/mtri/natcolor.html", selects=selects).run()
    download_path = os.path.join(base_download_path, "Satellite")
    XmlDownloader.run(isos, download_path)

    # MTRI CDOM, DOC and SM Aggregates
    selects = [".*CDOM-Agg"]
    isos = ThreddsCollector("http://tds.glos.us/thredds/mtri/cdom.html", selects=selects).run()
    download_path = os.path.join(base_download_path, "Satellite")
    XmlDownloader.run(isos, download_path)
    selects = [".*DOC-Agg"]
    isos = ThreddsCollector("http://tds.glos.us/thredds/mtri/doc.html", selects=selects).run()
    download_path = os.path.join(base_download_path, "Satellite")
    XmlDownloader.run(isos, download_path)
    selects = [".*SM-Agg"]
    isos = ThreddsCollector("http://tds.glos.us/thredds/mtri/sm.html", selects=selects).run()
    download_path = os.path.join(base_download_path, "Satellite")
    XmlDownloader.run(isos, download_path)


    # We only want the all year best selects
    selects = [".*2D_best.*", ".*3D_best.*", ".*2D_-_All_Years_best.*", ".*3D_-_All_Years_best.*"]
    isos = ThreddsCollector("http://tds.glos.us/thredds/glcfs/glcfs.html", selects=selects).run()
    download_path = os.path.join(base_download_path, "Models", "GLCFS")
    XmlDownloader.run(isos, download_path)

    # We only want the Agg and Latest
    selects = [".*Nowcast-Agg.*", ".*Lastest-Forecast.*"]
    # Don't process the "files/" lists
    skips = [".*Nowcast - Individual Files/", ".*Forecast - Individual Files/"]
    isos = ThreddsCollector("http://tds.glos.us/thredds/hecwfs/hecwfs.html", selects=selects, skips=skips).run()
    download_path = os.path.join(base_download_path, "Models", "HECWFS")
    XmlDownloader.run(isos, download_path)
    
    # We only want the Agg and Latest
    selects = [".*Nowcast-Agg.*", ".*Lastest-Forecast.*"]
    # Don't process the "files/" lists
    skips = [".*Nowcast - Individual Files/", ".*Forecast - Individual Files/"]
    isos = ThreddsCollector("http://tds.glos.us/thredds/slrfvm/slrfvm.html", selects=selects, skips=skips).run()
    download_path = os.path.join(base_download_path, "Models", "SLRFVM")
    XmlDownloader.run(isos, download_path)

    isos = GeoNetworkCollector("http://data.glos.us/metadata").run()
    download_path = os.path.join(base_download_path, "GeoNetwork")
    XmlDownloader.run(isos, download_path, namer=GeoNetworkCollector.namer, modifier=GeoNetworkCollector.modifier)   

main(sys.argv[1])

exit(0)
