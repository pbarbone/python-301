# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

from mymath import subtract_divide, CustomZeroDivsionError
import unittest

class TestSubtractDivide(unittest.TestCase):
    def test_subtract_divide(self):
        self.assertEqual(subtract_divide(10, 4, 2), 5)
        self.assertEqual(subtract_divide(10, 10, 5), 2)

    def test_custom_zero_division_error(self):
        with self.assertRaises(CustomZeroDivsionError) as error:
            subtract_divide(10, 5, 5)
        self.assertEqual(str(error.exception), "This won't work because 5 - 5 = 0.")
