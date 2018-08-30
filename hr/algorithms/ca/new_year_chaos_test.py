"""
HackerRank Algorithms Data Structures Arrays 2D Array DS
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/2d-array/problem
"""

import unittest
from new_year_chaos import solution


class TestSolution(unittest.TestCase):

    def test_provided_0a(self):
        self.assertEqual(3, solution([2, 1, 5, 3, 4]))

    def test_provided_0b(self):
        self.assertEqual(-1, solution([2, 5, 1, 3, 4]))

    def test_provided_1a(self):
        self.assertEqual(-1, solution([5, 1, 2, 3, 7, 8, 6, 4]))

    def test_provided_1b(self):
        self.assertEqual(7, solution([1, 2, 5, 3, 7, 8, 6, 4]))

    def test_provided_2(self):
        self.assertEqual(4, solution([1, 2, 5, 3, 4, 7, 8, 6]))


if __name__ == '__main__':
    unittest.main()
