from pyiso.utils.utils import download, download_iso, move_iso
from pyiso.utils.etree import etree

class GLCFSCollector(object):
	def __init__(self):
		self._html = 'http://64.9.200.113:8080'
		self._forcing = '/thredds/glcfs/forcing/glcfs_forcing_all.html'
		self._forecast = '/thredds/glcfs/glcfs_forecast.html'
		self._nowcast = '/thredds/glcfs/nowcast/glcfs_nowcast_all.html'

	def download_isos(self):
		"""
			Download all of the best isos from the forcing url
			Get ready for some text parsing ninjutsu
		"""
		self.__download_forcing()
		self.__download_forecast()
		self.__download_nowcast()

	def __download_forcing(self):
		# get all of the catalogs at the forcing url
		fnames = self.__download(self._html + self._forcing)
		for name in fnames:
			move_iso(name, 'Models/GLCFS/Forcing/')

	def __download_forecast(self):

		names = self.__download(self._html + self._forecast)
		for name in names:
			nname = list(name.partition('_-_'))
			nname.append(nname[2])
			nname[2] = 'Forecast_-_'
			nname = ''.join(nname)
			if nname.find('2D') > 0:
				move_iso(name, 'Models/GLCFS/Forecast-2D', nname)
			else:
				move_iso(name, 'Models/GLCFS/Forecast-3D', nname)

	def __download_nowcast(self):
		names = self.__download(self._html + self._nowcast)
		for name in names:
			if name.find('2D') > 0:
				move_iso(name, 'Models/GLCFS/Nowcast-2D')
			else:
				move_iso(name, 'Models/GLCFS/Nowcast-3D')
		# for name in names:
		# 	nname = list(name.partition('_-_'))
		# 	nname.append(nname[2])
		# 	nname[2] = 'Nowcast_-_'
		# 	nname = ''.join(nname)
		# 	if nname.find('2D') > 0:
		# 		move_iso(name, 'Models/GLCFS/Nowcast-2D', nname)
		# 	else:
		# 		move_iso(name, 'Models/GLCFS/Nowcast-3D', nname)

	def __download(self, catalog_url):
		retval = list()
		#get catalogs
		resp = download(catalog_url)
		tree = etree.HTML(resp)

		for a in tree.findall('.//a[@href]'):
			cat = self._html + a.attrib.get('href')
			if cat.find('/catalog/') > 0:
				resp = download(cat)
				catree = etree.HTML(resp)
				dataset = ''
				for a2 in catree.findall('.//a[@href]'):
					if a2.attrib.get('href').find('best') > 0:
						index = a2.attrib.get('href').find('=') + 1
						dataset = a2.attrib.get('href')[index:]

				dsname = dataset.rpartition('/')[2]
				url = cat.replace('catalog.html',dsname)
				url = url.replace('/catalog/','/iso/')

				#download iso
				iso = download_iso(url,catalog=cat,dataset=dataset)
				if iso is not None:
					retval.append(iso)

		return retval
