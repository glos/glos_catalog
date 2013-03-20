"""
	Utility to download an iso file from a provided html link into the iso_tmp folder
"""

from urllib2 import Request, urlopen
from urllib import urlencode
from os import remove
from os.path import abspath
from shutil import move

TMP_DIR='./pyiso/iso_tmp/'
ISO_DIR='../ISOs/'

def download(html, headers=None, **kwargs):
	"""
		Downloads from the html and returns the response as a string
			- html is a string of the url
			- headers is an optional dict that contains http headers
			- kwargs is a dictionary of query parameters
	"""
	# type assurance
	if not isinstance(html, str) and not isinstance(html, unicode):
		raise ValueError('html must be a string or unicode')

	if headers is not None:
		if not isinstance(headers, dict):
			raise ValueError('headers must be a dict object')
	else:
		headers = dict()

	if len(kwargs) > 0:
		query = urlencode(kwargs)
		url = html + '?' + query
	else:
		url = html

	request = Request(url=url, headers=headers)

	try:
		response = urlopen(request)
	except:
		return None

	reply = response.read()

	response.close()

	return reply

def download_iso(html, headers=None, **kwargs):
	global TMP_DIR
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

	if len(kwargs) > 0:
		query = urlencode(kwargs)
		url = html + '?' + query
	else:
		url = html

	# escape out spaces, just incase
	url = url.replace(' ', '')

	print '\nDownloading ISO: ' + url

	request = Request(url=url, headers=headers)

	try:
		response = urlopen(request)
	except:
		return None

	# write response into the iso_tmp folder; the name will be uri in the html
	name = html.rpartition('/')[2]
	if not name.endswith('.xml'):
		name += '.xml'

	path = abspath(TMP_DIR + name)

	isof = open(path, 'w+')
	isof.write(response.read())
	isof.close()

	response.close()

	return name

def move_iso(source, dest, dfile_name=None):
	global ISO_DIR, TMP_DIR
	"""
		Moves file to the glos_catalog ISO directory.
			- source: the name of the ISO file to move that lives inside the iso_tmp directory
			- dest: the destination directory/file to move to, the path should be relative to the ISO directory in glos_catalog
	"""
	if source is None or dest is None:
		return

	dpath = abspath(ISO_DIR + dest)
	if dfile_name is not None:
		dpath += '/' + dfile_name
		f = open(dpath, 'w+')
		f.close()
		remove(dpath)
	else:
		# create the file, then delete it, to prevent move from throwing an error
		f = open(dpath + '/' + source, 'w+')
		f.close()
		remove(dpath + '/' + source)

	spath = (TMP_DIR + source)
	
	move(spath,dpath)
