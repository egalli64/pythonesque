"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
round_sum: https://codingbat.com/prob/p179960
"""
import unittest
from round_sum import round_sum


class TestRoundSum(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(round_sum(16, 17, 18), 60)

    def test_given_2(self):
        self.assertEqual(round_sum(12, 13, 14), 30)

    def test_given_3(self):
        self.assertEqual(round_sum(6, 4, 4), 10)


if __name__ == "__main__":
    unittest.main()
