"""
	Utility to download an iso file from a provided html link into the iso_tmp folder
"""

from urllib2 import Request, urlopen
from urllib import urlencode
from os.path import abspath

class ISODownload(object):
	def __init__(self):
		pass

	def download_iso(self, html, headers=None, **kwargs):
		"""
			Will proceed to download from the given html link.
				- html is a string containing the http address
				- headers is an optional dict that contains any headers to be used
				- kwargs is a dictionary of query parameters that will be encoded for html
			The name of the created iso file is returned
		"""
		# type assurance
		if not isinstance(html, str) and not isinstance(html, unicode):
			raise ValueError("html must be a string or unicode")

		if headers is not None:
			if not isinstance(headers, dict):
				raise ValueError('headers must be a dict object')
		else:
			headers = dict()

		query = urlencode(kwargs)
		url = html + '?' + query

		print 'downloading from url: ' + url

		request = Request(url=url, headers=headers)

		response = urlopen(request)

		# write response into the iso_tmp folder; the name will be uri in the html
		html_spl = html.split('/')
		name = html_spl[len(html_spl)-1]
		if name.rfind('.') > 0:
			name = name[0:name.rfind('.')]
		name += '.xml'

		path = abspath('../iso_tmp/' + name)

		isof = open(path, 'w+')
		isof.write(response.read())
		isof.close()

		response.close()

		return name

