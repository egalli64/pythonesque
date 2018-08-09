"""
HackerRank Algorithms Data Structures Arrays 2D Array DS
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/2d-array/problem
"""

import unittest
from max_hourglass import solution


class TestSolution(unittest.TestCase):

    def test_provided_0(self):
        data = [[1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0 ,0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]
        self.assertEqual(7, solution(data))

    def test_provided_1(self):
        data = [[-9, -9, -9, 1, 1, 1],
                [0, -9, 0, 4, 3, 2],
                [-9, -9, -9, 1, 2, 3],
                [0, 0, 8, 6, 6, 0],
                [0, 0, 0, -2, 0, 0],
                [0, 0, 1, 2, 4, 0]]
        self.assertEqual(28, solution(data))

if __name__ == '__main__':
    unittest.main()
