"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
first_last6: https://codingbat.com/prob/p181624
"""
import unittest
from first_last6 import first_last6


class TestFirstLast6(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(first_last6([1, 2, 6]), True)

    def test_given_2(self):
        self.assertEqual(first_last6([6, 1, 2, 3]), True)

    def test_given_3(self):
        self.assertEqual(first_last6([13, 6, 1, 2, 3]), False)


if __name__ == "__main__":
    unittest.main()
