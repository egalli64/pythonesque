"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
sum_double https://codingbat.com/prob/p141905
"""
import unittest
from sum_double import sum_double


class TestSumDouble(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(sum_double(1, 2), 3)

    def test_given_2(self):
        self.assertEqual(sum_double(3, 2), 5)

    def test_given_3(self):
        self.assertEqual(sum_double(2, 2), 8)


if __name__ == "__main__":
    unittest.main()
