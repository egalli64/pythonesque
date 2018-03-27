"""
HackerRank Python Implementation Between Two Sets

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/between-two-sets/problem
"""

import unittest
from between_two_sets import solution


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(3, solution([2, 4], [16, 32, 96]))


if __name__ == '__main__':
    unittest.main()

