import unittest
from pyiso.collectors.insitu import InSituCollector

class TestInsitu(unittest.TestCase):
	def setUp(self):
		self._insitu = InSituCollector()

	def test_insitu(self):
		self._insitu.download_isos()