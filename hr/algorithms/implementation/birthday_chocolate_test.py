"""
HackerRank Algorithms Implementation Birthday Chocolate

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/the-birthday-bar/problem
"""

import unittest
from birthday_chocolate import solution


class TestSolution(unittest.TestCase):

    def test_provided_0(self):
        self.assertEqual(2, solution([1, 2, 1, 3, 2], 3, 2))

    def test_provided_1(self):
        self.assertEqual(0, solution([1, 1, 1, 1, 1, 1], 3, 2))

    def test_provided_2(self):
        self.assertEqual(1, solution([4], 4, 1))


if __name__ == '__main__':
    unittest.main()

