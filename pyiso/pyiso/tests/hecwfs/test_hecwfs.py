import unittest
from pyiso.hecwfs.hecwfs import HECWFSCollector

class GLCFSTest(unittest.TestCase):
	def setUp(self):
		self._hecwfs = HECWFSCollector()

	def test_download(self):
		self._hecwfs.download_isos()