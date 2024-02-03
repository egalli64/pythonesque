"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 2: https://codingbat.com/python/List-2
count_evens: https://codingbat.com/prob/p189616
"""

import unittest
from count_evens import count_evens


class TestCountEvens(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(count_evens([2, 1, 2, 3, 4]), 3)

    def test_given_2(self):
        self.assertEqual(count_evens([2, 2, 0]), 3)

    def test_given_3(self):
        self.assertEqual(count_evens([1, 3, 5]), 0)


if __name__ == "__main__":
    unittest.main()
