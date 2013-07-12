from pyiso.collectors.thredds import ThreddsCollector
from pyiso.collectors.geo import GeoCollector
from pyiso.collectors.insitu import InSituCollector
from pyiso.downloader import IsoDownloader

import requests
import os
import codecs


def main():

    base_download_path = "/home/dev/Development/glos_catalog/ISOs"

    # datasets: The ID in THREDDS needs to contain one of these strings to be identified.
    # skips: The LINK path in the actual thredds catalog webpage can't be equal to any of these strings
    
    # We only want the Agg datasets
    datasets = ["SST-Agg"]
    # Don't process the "files/" lists
    skips = ["files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/mtri/aoc.html", datasets=datasets, skips=skips).run()
    download_path = os.path.join(base_download_path, "Satellite")
    IsoDownloader.run(isos, download_path)

    # We only want the Agg datasets
    datasets = ["CHL-Agg"]
    # Don't process the "files/" lists
    skips = ["files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/mtri/chl.html", datasets=datasets, skips=skips).run()
    download_path = os.path.join(base_download_path, "Satellite")
    IsoDownloader.run(isos, download_path)

    # We only want the Agg datasets
    datasets = ["NC-Agg"]
    # Don't process the "files/" lists
    skips = ["files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/mtri/natcolor.html", datasets=datasets, skips=skips).run()
    download_path = os.path.join(base_download_path, "Satellite")
    IsoDownloader.run(isos, download_path)

    # We only want the all year best datasets
    datasets = ["2D_best", "3D_best", "2D_-_All_Years_best", "3D_-_All_Years_best"]
    # Don't process the "files/" lists
    skips = ["files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/glcfs/glcfs.html", datasets=datasets, skips=skips).run()
    download_path = os.path.join(base_download_path, "Models", "GLCFS")
    IsoDownloader.run(isos, download_path)

    # We only want the Agg and Latest
    datasets = ["Nowcast-Agg", "Lastest-Forecast"]
    # Don't process the "files/" lists
    skips = ["Nowcast - Individual Files/", "Forecast - Individual Files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/hecwfs/hecwfs.html", datasets=datasets, skips=skips).run()
    download_path = os.path.join(base_download_path, "Models", "HECWFS")
    IsoDownloader.run(isos, download_path)
    
    # We only want the Agg and Latest
    datasets = ["Nowcast-Agg", "Lastest-Forecast"]
    # Don't process the "files/" lists
    skips = ["Nowcast - Individual Files/", "Forecast - Individual Files/"]
    isos = ThreddsCollector("http://tds.glos.us:8080/thredds/slrfvm/slrfvm.html", datasets=datasets, skips=skips).run()
    download_path = os.path.join(base_download_path, "Models", "SLRFVM")
    IsoDownloader.run(isos, download_path)

    isos = GeoCollector("http://data.glos.us/metadata").run()
    download_path = os.path.join(base_download_path, "GeoNetwork")
    IsoDownloader.run(isos, download_path, namer=GeoCollector.namer, modifier=GeoCollector.modifier)
    
    isos = InSituCollector("http://64.9.200.113:8080/isos", "ndbc").run()
    download_path = os.path.join(base_download_path, "In-situ", "ndbc")
    IsoDownloader.run(isos, download_path)
    
    isos = InSituCollector("http://64.9.200.113:8080/isos", "storet").run()
    download_path = os.path.join(base_download_path, "In-situ", "storet")
    IsoDownloader.run(isos, download_path)
    

main()

exit(0)
