from metadown.collectors.thredds import ThreddsCollector
from metadown.collectors.geonetwork import GeoNetworkCollector
from metadown.downloader import XmlDownloader

import os
import sys

def run_downloader(selects, url, dlpath, **kwargs):
    """
    Selects is list of selectors
    Url is url of base catalog page
    dlpath is download path
    kwargs is any other kwargs to ThreddsCollector
    """
    print "Downloading", url, "to", dlpath
    try:
        isos = ThreddsCollector(url, selects=selects, **kwargs).run()
        XmlDownloader.run(isos, dlpath)
    except Exception as e:
        print >>sys.stderr, "Problem with", url, "ex:", e

def main(base_download_path):

    # selects: The ID in THREDDS needs to contain one of these strings to be identified.
    # skips: The LINK path in the actual thredds catalog webpage can't be equal to any of these strings
    
    isos = GeoNetworkCollector("http://data.glos.us/metadata").run()
    download_path = os.path.join(base_download_path, "GeoNetwork")
    XmlDownloader.run(isos, download_path, namer=GeoNetworkCollector.namer, modifier=GeoNetworkCollector.modifier)   

main(sys.argv[1])

exit(0)
