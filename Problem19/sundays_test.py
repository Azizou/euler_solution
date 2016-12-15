import unittest
from sundays import *

class TestSundaysMethods(unittest.TestCase):

	def setUp(self):
		pass

	def test_is_leap_year(self):
		self.assertTrue(is_leap_year(2016))
		self.assertTrue(is_leap_year(1908))
		self.assertTrue(is_leap_year(1916))
		self.assertTrue(is_leap_year(2000))
		self.assertFalse(is_leap_year(1900))
		# self.assertTrue(is_leap_year(2016))
		# self.assertTrue(is_leap_year(2016))
		# self.assertTrue(is_leap_year(2016))
		# self.assertTrue(is_leap_year(2016))
		# self.assertTrue(is_leap_year(2016))
		# self.assertTrue(is_leap_year(2016))

	def test_count_leap_years(self):
		self.assertEqual(0, count_leap_years(1900,1900))
		self.assertEqual(0, count_leap_years(1900,1901))
		self.assertEqual(0, count_leap_years(1900,1902))
		self.assertEqual(0, count_leap_years(1900,1903))
		self.assertEqual(0, count_leap_years(1900,1904))
		self.assertEqual(1, count_leap_years(1900,1905))
		self.assertEqual(1, count_leap_years(1900,1906))
		self.assertEqual(1, count_leap_years(1900,1907))
		self.assertEqual(1, count_leap_years(1900,1908))
		self.assertEqual(2, count_leap_years(1900,1909))
		# self.assertEqual(2, count_leap_years(1900,1900))
		# self.assertEqual(0, count_leap_years(1900,1906))

	def test_monts_to_days(self):
		self.assertEqual(0, months_to_days(1,1900))
		self.assertEqual(31, months_to_days(2,1900))
		self.assertEqual(31+28, months_to_days(3,1900))
		self.assertEqual(31+29, months_to_days(3,1904))

	def test_first_day_of_year(self):
		self.assertEqual(0,first_day_of_year(1900))
		self.assertEqual(1,first_day_of_year(1901))
		self.assertEqual(4,first_day_of_year(1904))
		self.assertEqual(6,first_day_of_year(1905))
		self.assertEqual(0,first_day_of_year(1906))
		self.assertEqual(4,first_day_of_year(1909))

	def test_first_day_of_month(self):
		self.assertEqual(0,first_day_of_month(1,1900))
		self.assertEqual(1,first_day_of_month(1,1901))
		self.assertEqual(4,first_day_of_month(1,1904))
		self.assertEqual(6,first_day_of_month(1,1905))
		self.assertEqual(0,first_day_of_month(1,1906))
		self.assertEqual(3,first_day_of_month(2,1900))

if __name__ == '__main__':
	unittest.main()