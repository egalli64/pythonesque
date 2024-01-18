"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
has23: https://codingbat.com/prob/p177892
"""
import unittest
from has23 import has23


class TestHas23(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(has23([2, 5]), True)

    def test_given_2(self):
        self.assertEqual(has23([4, 3]), True)

    def test_given_3(self):
        self.assertEqual(has23([4, 5]), False)


if __name__ == "__main__":
    unittest.main()
