from pyiso.utils.utils import download, download_iso, move_iso
from pyiso.utils.etree import etree

class HECWFSCollector(object):
	def __init__(self):
		self._html = 'http://64.9.200.113:8080/thredds/hecwfs/hecwfs.html'
		self._latest = 'http://64.9.200.113:8080/thredds/iso/FVCOM/'
		self._agg = 'http://64.9.200.113:8080/thredds/iso/'
		self._iso = 'Models/HECWFS'

	def download_isos(self):
		# get datasets
		resp = download(self._html)
		tree = etree.HTML(resp)

		for a in tree.findall('.//a[@href]'):
			dataset = a.attrib.get('href')
			# will have to correct for a typo in the address
			dataset = dataset.replace('Lastest','Latest')
			if dataset.find('dataset') > 0:
				dataset = dataset[dataset.find('=')+1:]
				# get iso
				if dataset.find('Agg') > 0:
					url = self._agg + dataset + '.nc'
				else:
					url = self._latest + dataset + '.nc'

				fname = download_iso(url, catalog=self._html, dataset=dataset)
				# move iso
				move_iso(fname, self._iso)

