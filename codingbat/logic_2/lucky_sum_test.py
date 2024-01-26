"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
lucky_sum: https://codingbat.com/prob/p107863
"""
import unittest
from lucky_sum import lucky_sum, lucky_sum_alt


class TestLuckySum(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(lucky_sum(1, 2, 3), 6)

    def test_given_2(self):
        self.assertEqual(lucky_sum(1, 2, 13), 3)

    def test_given_3(self):
        self.assertEqual(lucky_sum(1, 13, 3), 1)

    def test_given_alt_1(self):
        self.assertEqual(lucky_sum_alt(1, 2, 3), 6)

    def test_given_alt_2(self):
        self.assertEqual(lucky_sum_alt(1, 2, 13), 3)

    def test_given_alt_3(self):
        self.assertEqual(lucky_sum_alt(1, 13, 3), 1)


if __name__ == "__main__":
    unittest.main()
