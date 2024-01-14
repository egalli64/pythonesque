"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
front_back https://codingbat.com/prob/p153599
"""
import unittest
from front_back import front_back


class TestMissingChar(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(front_back('code'), 'eodc')

    def test_given_2(self):
        self.assertEqual(front_back('a'), 'a')

    def test_given_3(self):
        self.assertEqual(front_back('ab'), 'ba')


if __name__ == "__main__":
    unittest.main()
