#!/usr/bin/python3
"""
task6
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unittest
    """
    def test_base(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_mixed(self):
        self.assertEqual(max_integer([2, 4, 1, 3]), 4)

    def test_baseN(self):
        self.assertEqual(max_integer([-1, -4, -4, -3]), -1)

    def test_no(self):
        self.assertEqual(max_integer([]), None)
    
    def test_zero(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_one(self):
        self.assertEqual(max_integer([10]), 10)

if __name__ == "__main__":
    unittest.main()
