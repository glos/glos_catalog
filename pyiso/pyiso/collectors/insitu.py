from pyiso.utils.utils import download, download_iso, move_iso
from pyiso.utils.etree import etree

class InSituCollector(object):
	def __init__(self):
		self._html = 'http://64.9.200.113:8080/isos/'
		self._sources = 'sources.html'
		self._iso_dirs = {
			'NDBC': '../ISOs/In-situ/ndbc',
			'STORET': '../ISOs/In-situ/storet'
			}

	def download_isos(self):
		resp = download(self._html+self._sources)
		tree = etree.HTML(resp)

		for source in tree.findall(".//li"):
			# get list of files in source
			dirlist = download(self._html+source.text+'/list.html')
			dirtree = etree.HTML(dirlist)
			for iso in dirtree.findall('.//li'):
				print self._html + source.text + '/' + iso.text.strip()
				sname = download_iso(self._html+source.text+'/'+iso.text.strip())
				move_iso(sname, self._iso_dirs[source.text])

