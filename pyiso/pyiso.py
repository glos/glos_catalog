# executes all of the collectors
from pyiso.aoc.aoc import AOCCollector
from pyiso.geo.geo import GeoCollector
from pyiso.glcfs.glcfs import GLCFSCollector
from pyiso.hecwfs.hecwfs import HECWFSCollector
from pyiso.insitu.insitu import InSituCollector
from pyiso.slrfvm.slrfvm import SLRFVMCollector

def main():
	col_list = [AOCCollector(),GeoCollector(),GLCFSCollector(),HECWFSCollector(),InSituCollector(),SLRFVMCollector()]
	for coll in col_list:
		print 'downloading for ' + str(coll)
		coll.download_isos()


main()

exit(0)