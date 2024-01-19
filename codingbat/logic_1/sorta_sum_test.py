"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
sorta_sum: https://codingbat.com/prob/p116620
"""
import unittest
from sorta_sum import sorta_sum


class TestSortaSum(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(sorta_sum(3, 4), 7)

    def test_given_2(self):
        self.assertEqual(sorta_sum(9, 4), 20)

    def test_given_3(self):
        self.assertEqual(sorta_sum(10, 11), 21)


if __name__ == "__main__":
    unittest.main()
