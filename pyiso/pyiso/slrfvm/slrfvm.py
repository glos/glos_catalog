from pyiso.hecwfs.hecwfs import HECWFSCollector

class SLRFVMCollector(HECWFSCollector):
	def __init__(self):
		super(SLRFVMCollector,self).__init__()
		self._html = 'http://64.9.200.113:8080/thredds/slrfvm/slrfvm.html'
		self._iso = 'Models/SLRFVM'
