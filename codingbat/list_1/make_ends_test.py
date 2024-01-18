"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
make_ends: https://codingbat.com/prob/p124806
"""
import unittest
from make_ends import make_ends


class TestMakeEnds(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(make_ends([1, 2, 3]), [1, 3])

    def test_given_2(self):
        self.assertEqual(make_ends([1, 2, 3, 4]), [1, 4])

    def test_given_3(self):
        self.assertEqual(make_ends([7, 4, 6, 2]), [7, 2])


if __name__ == "__main__":
    unittest.main()
