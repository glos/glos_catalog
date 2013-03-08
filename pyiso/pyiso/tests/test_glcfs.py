import unittest
from pyiso.collectors.glcfs import GLCFSCollector

class GLCFSTest(unittest.TestCase):
	def setUp(self):
		self._glcfs = GLCFSCollector()

	def test_download(self):
		self._glcfs.download_isos()
		pass