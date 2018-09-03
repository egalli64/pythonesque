"""
HackerRank  Interview Preparation Kit  Arrays  Minimum Swaps 2
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/minimum-swaps-2/problem
"""
import unittest
from minimum_swaps_2 import solution


class TestSolution(unittest.TestCase):

    def test_provided_0(self):
        self.assertEqual(3, solution([4, 3, 1, 2]))

    def test_provided_1(self):
        self.assertEqual(3, solution([2, 3, 4, 1, 5]))

    def test_provided_2(self):
        self.assertEqual(3, solution([1, 3, 5, 2, 4, 6, 8]))


if __name__ == '__main__':
    unittest.main()
