"""
HackerRank Cracking the Coding Interview DFS: Connected Cell in a Grid
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/hackerrank-dfs-connected-cell-in-grid.html
      https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid
"""

import unittest
from hr.ctci.connected_cell_in_a_grid import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        data = [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 0]
        ]
        self.assertEqual(5, solution(data))

    def test_provided_2(self):
        data = [
            [0, 0, 1, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        self.assertEqual(8, solution(data))

    def test_3(self):
        data = [
            [0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 0, 1, 0],
            [0, 1, 0, 1, 1],
            [0, 1, 1, 1, 0]
        ]
        self.assertEqual(15, solution(data))


if __name__ == '__main__':
    unittest.main()
