# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import math
import unittest

class TestMathModule(unittest.TestCase):
    '''Test the math module functions.'''
    #Testing the square root function
    def test_sqrt(self):
        self.assertEqual(math.sqrt(9), 3)
        self.assertEqual(math.sqrt(16), 4)
    #Testing the floor function
    def test_floor(self):
        self.assertEqual(math.floor(3.14), 3)
        self.assertEqual(math.floor(3.99), 3)
    #Testing the multiplication function
    def test_mult(self):
        self.assertEqual(math.prod([2, 3, 4]), 24)
        self.assertEqual(math.prod([3, 4, 5]), 60)