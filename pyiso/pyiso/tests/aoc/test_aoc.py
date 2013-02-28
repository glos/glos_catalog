import unittest
from pyiso.aoc.aoc import AOCCollector

class AOCTest(unittest.TestCase):

	def test_aoc(self):
		aoc = AOCCollector()
		aoc.download_isos()