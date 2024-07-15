import unittest
from unittest_function import convert_to_celsius

class TestConvertToCelsius(unittest.TestCase):
    #passes
    def test_convert_to_celsius(self):
        self.assertEqual(convert_to_celsius(32), 0)
        self.assertEqual(convert_to_celsius(212), 100)
    #does not pass
    def test_convert_to_celsius_fail(self):
        self.assertEqual(convert_to_celsius(100), 0)