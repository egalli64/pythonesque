"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
near_hundred https://codingbat.com/prob/p124676
"""
import unittest
from near_hundred import near_hundred


class TestNearHundred(unittest.TestCase):
    def test_given_1(self):
        self.assertTrue(near_hundred(93))

    def test_given_2(self):
        self.assertTrue(near_hundred(90))

    def test_given_3(self):
        self.assertFalse(near_hundred(89))


if __name__ == "__main__":
    unittest.main()
