"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
common_end: https://codingbat.com/prob/p147755
"""
import unittest
from common_end import common_end


class TestCommonEnd(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(common_end([1, 2, 3], [7, 3]), True)

    def test_given_2(self):
        self.assertEqual(common_end([1, 2, 3], [7, 3, 2]), False)

    def test_given_3(self):
        self.assertEqual(common_end([1, 2, 3], [1, 3]), True)


if __name__ == "__main__":
    unittest.main()
