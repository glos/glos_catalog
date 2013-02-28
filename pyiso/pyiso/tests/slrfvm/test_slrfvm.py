import unittest
from pyiso.slrfvm.slrfvm import SLRFVMCollector

class SLRFVMTest(unittest.TestCase):
	def setUp(self):
		self._slrfvm = SLRFVMCollector()

	def test_iso_download(self):
		self._slrfvm.download_isos()