from pyiso.utils.utils import download, download_iso, move_iso
from pyiso.utils.etree import etree

class AOCCollector(object):
	def __init__(self):
		self._html = 'http://64.9.200.113:8080/thredds/aoc.html'
		self._iso = 'http://64.9.200.113:8080/thredds/iso/SST/'
		self._iso_dir = 'Satellite/'
		#self._parser = etree.HTMLParser()

	def download_isos(self):
		"""
			Should download all Agg files from the html and put them in the correct glos catalog folder

		"""
		resp = download(self._html)
		tree = etree.HTML(resp)

		datasets = list()
		files = dict()

		# get all of the datasets to download
		for elm in tree.findall('.//a[@href]'):
			for key in elm.attrib.keys():
				val = elm.attrib[key]
				if val.find('dataset') > 0:
					ds = val[val.find('=')+1:]
					datasets.append(ds)

		# download isos
		for ds in datasets:
			url = self._iso + ds
			files[ds] = download_iso(url, catalog=self._html, dataset=ds)

		# move them
		for key in files.keys():
			move_iso(files[key],self._iso_dir)
