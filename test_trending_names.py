import unittest
from trending_names import get_data

class TestTrendingNames(unittest.TestCase):
	# def test_get_data(self):
	# 	#There is only data for years 1880 to 2017
	# 	self.assertRaises(FileNotFoundError, get_data, 423)
	def test_name(self):
		self.assertRaises(NameError, get_data, 'dada')

# if __name__ == '__main__':
#     unittest.main()