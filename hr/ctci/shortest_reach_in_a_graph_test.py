"""
HackerRank Cracking the Coding Interview BFS: Shortest Reach in a Graph
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
"""

import unittest
from hr.ctci.shortest_reach_in_a_graph import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual([6, 6, -1], solution(4, [(1, 2), (1, 3)], 1))

    def test_provided_2(self):
        self.assertEqual([-1, 6], solution(3, [(2, 3)], 2))

    def test_simple(self):
        self.assertEqual([], solution(1, [], 1))

    def test_four(self):
        self.assertEqual([12, 18, 6], solution(4, [(1, 4), (2, 4), (2, 3)], 1))

    def test_five_b(self):
        self.assertEqual([-1, 6, 6, 12], solution(5, [(1, 4), (1, 3), (3, 4), (4, 5)], 1))


if __name__ == '__main__':
    unittest.main()
