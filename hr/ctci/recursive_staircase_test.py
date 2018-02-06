"""
HackerRank Tutorials  Cracking the Coding Interview  Recursion: Davis' Staircase
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/hackerrank-recursion-davis-staircase.html
      https://www.hackerrank.com/challenges/ctci-recursive-staircase
"""

import unittest
from hr.ctci.recursive_staircase import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(1, solution(1))

    def test_provided_2(self):
        self.assertEqual(4, solution(3))

    def test_provided_3(self):
        self.assertEqual(44, solution(7))


if __name__ == '__main__':
    unittest.main()
