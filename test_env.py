import unittest
import numpy as np

import env as en

class TestEnv(unittest.TestCase):
	"""docstring for TestCell"""
	def test_init_env(self):
		# ---testing the values expected
		env = en.init_env(2,2,(0,0),(1,1))
		self.assertAlmostEqual(env[1,1], True)
		self.assertAlmostEqual(env[0,0], True)
		self.assertAlmostEqual(env[0,1], False)
		self.assertAlmostEqual(env[1,0], False)

		# ---testing the types expected
		self.assertRaises(TypeError, en.init_env, 2, 2, 1, 1)
		self.assertRaises(TypeError, en.init_env, 2, 2, (1, 1), '(3, 3)')
		self.assertRaises(TypeError, en.init_env, 2, 2, (1,))
		self.assertRaises(TypeError, en.init_env, -1, 2, (1,1))
		



if __name__ == '__main__':
	unittest.main()