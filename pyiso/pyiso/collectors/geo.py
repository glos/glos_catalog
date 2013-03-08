from pyiso.utils.utils import download, download_iso
from pyiso.utils.etree import etree
from shutil import abspath
import os

class GeoCollector(object):
	def __init__(self):
		self._html = 'http://data.glos.us/metadata/srv/en/csv.search?'
		self._meta = 'http://data.glos.us/metadata/srv/en/iso19139.xml?id='
		self._iso_path = '../ISOs/GeoNetwork/'
		self._meta_folder = '/metadata/'
		self._meta_file = 'metadata.xml'
		self._file_identifier = '{http://www.isotc211.org/2005/gmd}fileIdentifier'
		self._character_string = '{http://www.isotc211.org/2005/gco}CharacterString'

	def download_isos(self):
		return
		# download zip file
		resp = download(self._html)
		f = open('./pyiso/iso_tmp/geo.txt', 'w+')
		f.write(resp)
		f.close()

		for line in open('./pyiso/iso_tmp/geo.txt','r'):
			line_spl = line.split('\t')
			if line_spl[1].strip() == 'id':
				continue
			else:
				iid = int(line_spl[1].strip())
				html = self._meta + str(iid)
				# download the iso
				xmlstr = download(html)
				try:
					tree = etree.fromstring(xmlstr)
					# need the file identifier
					fi = tree.find('.//' + self._file_identifier + '/' + self._character_string)
					fname = fi.text
					path = self._iso_path + fname + self._meta_folder
					path = abspath(path)
					print '\nWriting to: ' + path
					if not os.path.exists(path):
						os.makedirs(path)

					f = open(path + '/' + self._meta_file, 'w+')
					f.write(xmlstr)
					f.close()
				except:
					path = abspath(self._iso_path + 'corrupt_metadata_ids.txt')
					f = open(path, 'a+')
					f.write('\nCorrupted xml for id: ' + str(iid))
					f.close()



