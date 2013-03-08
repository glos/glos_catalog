# executes all of the collectors
from pyiso.collectors.aoc import AOCCollector
from pyiso.collectors.geo import GeoCollector
from pyiso.collectors.glcfs import GLCFSCollector
from pyiso.collectors.hecwfs import HECWFSCollector
from pyiso.collectors.insitu import InSituCollector
from pyiso.collectors.slrfvm import SLRFVMCollector

def main():
	col_list = [AOCCollector(),GeoCollector(),GLCFSCollector(),HECWFSCollector(),InSituCollector(),SLRFVMCollector()]
	for coll in col_list:
		coll.download_isos()


main()

exit(0)
