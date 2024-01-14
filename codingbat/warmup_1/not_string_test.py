"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
not_string https://codingbat.com/prob/p189441
"""
import unittest
from not_string import not_string


class TestNotString(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(not_string('candy'), 'not candy')

    def test_given_2(self):
        self.assertEqual(not_string('x'), 'not x')

    def test_given_3(self):
        self.assertEqual(not_string('not bad'), 'not bad')


if __name__ == "__main__":
    unittest.main()
