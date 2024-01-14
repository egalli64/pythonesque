"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
pos_neg https://codingbat.com/prob/p162058
"""
import unittest
from pos_neg import pos_neg


class TestPosNeg(unittest.TestCase):
    def test_given_1(self):
        self.assertTrue(pos_neg(1, -1, False))

    def test_given_2(self):
        self.assertTrue(pos_neg(-1, 1, False))

    def test_given_3(self):
        self.assertTrue(pos_neg(-4, -5, True))


if __name__ == "__main__":
    unittest.main()
