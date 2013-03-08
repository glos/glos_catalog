import unittest
from pyiso.collectors.aoc import AOCCollector

class AOCTest(unittest.TestCase):
	def setUp(self):
		self._aoc = AOCCollector()

	def test_aoc(self):
		self._aoc.download_isos()
		pass