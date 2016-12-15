import unittest
from sundays import *

class TestSundaysMethods(unittest.TestCase):

	def setUp(self):
		pass

	def test_is_leap_year(self):
		self.assertTrue(is_leap_year(2016))