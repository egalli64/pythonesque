"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
reverse3: https://codingbat.com/prob/p192962
"""
import unittest
from reverse3 import reverse3


class TestReverse3(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(reverse3([1, 2, 3]), [3, 2, 1])

    def test_given_2(self):
        self.assertEqual(reverse3([5, 11, 9]), [9, 11, 5])

    def test_given_3(self):
        self.assertEqual(reverse3([7, 0, 0]), [0, 0, 7])


if __name__ == "__main__":
    unittest.main()
