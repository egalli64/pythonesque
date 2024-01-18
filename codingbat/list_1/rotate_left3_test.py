"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
rotate_left3: https://codingbat.com/prob/p148661
"""
import unittest
from rotate_left3 import rotate_left3


class TestRotateLeft3(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(rotate_left3([1, 2, 3]), [2, 3, 1])

    def test_given_2(self):
        self.assertEqual(rotate_left3([5, 11, 9]), [11, 9, 5])

    def test_given_3(self):
        self.assertEqual(rotate_left3([7, 0, 0]), [0, 0, 7])


if __name__ == "__main__":
    unittest.main()
