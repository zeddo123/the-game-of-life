import unittest
import numpy as np

import cell

class TestCell(unittest.TestCase):
	"""docstring for TestCell"""
	def test_number_of_neighbours(self):
		env = np.full((5,5), False, dtype=bool)
		self.assertAlmostEqual(cell.number_of_neighbours(env,0,0), 0)

		env[3,3] = True
		self.assertAlmostEqual(cell.number_of_neighbours(env,3,3), 0)
		self.assertAlmostEqual(cell.number_of_neighbours(env,2,3), 1)
		env[2,3] = True
		self.assertAlmostEqual(cell.number_of_neighbours(env,3,2), 2)



if __name__ == '__main__':
	unittest.main()