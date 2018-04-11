"""
HackerRank Algorithms Graph Theory Roads and Libraries

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/04/hackerrank-roads-and-libraries.html
      https://www.hackerrank.com/challenges/torque-and-development/problem
"""

import unittest
from roads_libraries import solution


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(4, solution(3, 2, 1, [(1, 2), (3, 1), (2, 3)]))

    def test_extra_1(self):
        self.assertEqual(8, solution(6, 2, 1, [(1, 3), (3, 4), (2, 4), (1, 2), (2, 3), (5, 6)]))


if __name__ == '__main__':
    unittest.main()

