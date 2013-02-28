from pyiso.utils.iso_download import download, download_iso
from pyiso.utils.etree import etree
from os.path import abspath
from shutil import move

class AOCCollector(object):
	def __init__(self):
		self._html = 'http://64.9.200.113:8080/thredds/aoc.html'
		self._iso = 'http://64.9.200.113:8080/thredds/iso/SST/'
		self._iso_dir = '../ISOs/Satellite/'
		self._tmp_dir = './pyiso/iso_tmp/'
		self._parser = etree.HTMLParser()

	def download_isos(self):
		"""
			Should download all Agg files from the html and put them in the correct glos catalog folder

		"""
		resp = download(self._html)
		tree = etree.HTML(resp)

		datasets = list()
		iso_files = dict()

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
			iso_files[ds] = download_iso(url, catalog=self._html, dataset=ds)

		self.__move_to_ISO_dir(iso_files)

	def __move_to_ISO_dir(self, files):
		"""
			Uses shutil.move to move files from iso_tmp to ISO/Satellite
		"""
		if not isinstance(files, dict):
			raise ValueError('files needs to be of type dict')

		for key in files.keys():
			dpath = abspath(self._iso_dir)
			spath = abspath(self._tmp_dir + files[key])
			move(spath, dpath)


