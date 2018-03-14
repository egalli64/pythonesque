"""
HackerRank Cracking the Coding Interview DP: Coin Change
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/03/hackerrank-dp-coin-change.html
      https://www.hackerrank.com/challenges/ctci-coin-change/problem
"""

import unittest
from hr.ctci.dp_coin_change import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(4, solution([1, 2, 3], 4))

    def test_provided_2(self):
        self.assertEqual(5, solution([2, 5, 3, 6], 10))

    def test_simple(self):
        self.assertEqual(6, solution([1, 2, 3, 4], 5))


if __name__ == '__main__':
    unittest.main()
