"""
HackerRank Python Implementation Breaking the Records

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
"""

import unittest
from hr.algorithms.implementation.breaking_records import solution


class TestSolution(unittest.TestCase):
    def test_provided_0(self):
        self.assertEqual((2, 4), solution([10, 5, 20, 20, 4, 5, 2, 25, 1]))

    def test_provided_1(self):
        self.assertEqual((4, 0), solution([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))


if __name__ == '__main__':
    unittest.main()

