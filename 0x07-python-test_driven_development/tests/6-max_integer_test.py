#!/usr/bin/python3
"""
Unittest for the function max_integer
"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Class to have the methods to tests """
    def test_max_integer(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_one_element(self):
        result = max_integer([17])
        self.assertEqual(result, 17)

    def test_empty_list(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_not_int(self):
        with self.assertRaises(TypeError):
            max_integer(["string", 5])

if __name__ == "__main__":
    unittest.main()
