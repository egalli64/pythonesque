"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
date_fashion: https://codingbat.com/prob/p129125
"""
import unittest
from date_fashion import date_fashion


class TestDateFashion(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(date_fashion(5, 10), 2)

    def test_given_2(self):
        self.assertEqual(date_fashion(5, 2), 0)

    def test_given_3(self):
        self.assertEqual(date_fashion(5, 5), 1)


if __name__ == "__main__":
    unittest.main()
