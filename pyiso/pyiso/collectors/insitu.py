from pyiso.utils.utils import download, download_iso, move_iso
from pyiso.utils.etree import etree
from zipfile import ZipFile
from shutil import move
from os import path, makedirs, walk, remove

class InSituCollector(object):
	def __init__(self):
		self._html = 'http://64.9.200.113:8080/isos/'
		self._sources = 'sources.html'
		self._iso_dirs = {
			'NDBC': 'In-situ/ndbc',
			'STORET': 'In-situ/storet'
			}
		self._storet_zip_dir = './pyiso/iso_tmp/STORET/'
		if not path.exists(self._storet_zip_dir):
			makedirs(self._storet_zip_dir)

	def download_isos(self):
		resp = download(self._html+self._sources)
		tree = etree.HTML(resp)

		for source in tree.findall(".//li"):
			if source.text in self._iso_dirs:
				# get list of files in source
				dirlist = download(self._html+source.text+'/list.html')
				dirtree = etree.HTML(dirlist)
				for iso in dirtree.findall('.//li'):
					sname = download_iso(self._html+source.text+'/'+iso.text.strip())
					if source.text != 'STORET':
						move_iso(sname, self._iso_dirs[source.text])
					elif sname is not None:
						# storet needs to be compressed before being moved as a single archive
						if path.exists(self._storet_zip_dir + sname):
							remove(self._storet_zip_dir + sname)
						move('./pyiso/iso_tmp/' + sname, self._storet_zip_dir)

				if source.text == 'STORET':
					# archive the storet directory in iso_tmp and move it to the ISOs directory
					f = file(path.abspath('./pyiso/iso_tmp/storet.zip'), 'w')
					with ZipFile(f, 'w') as zip_file:
						fileiter = (f
							for root, _, files in walk(self._storet_zip_dir)
							for f in files)
						xmlfilter = (f for f in fileiter if f.endswith('.xml'))
						for xml in xmlfilter:
							zip_file.write(self._storet_zip_dir + xml, arcname=xml)

					# move the zip file
					dest = '../ISOs/' + self._iso_dirs[source.text] + '/storet.zip'
					if path.exists(dest):
						remove(dest)

					move('./pyiso/iso_tmp/storet.zip', dest)

