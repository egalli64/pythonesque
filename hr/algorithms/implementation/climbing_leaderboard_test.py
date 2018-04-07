"""
HackerRank Algorithms Implementation Climbing the Leaderboard

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/04/hackerrank-climbing-leaderboard.html
      https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""
import unittest
from climbing_leaderboard import solution_bisect, solution


class TestSolution(unittest.TestCase):

    def test_provided_0(self):
        self.assertEqual([6, 4, 2, 1], solution([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))

    def test_provided_0b(self):
        self.assertEqual([6, 4, 2, 1], solution_bisect([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))

    def test_extra_0(self):
        self.assertEqual([2, 2, 2, 1], solution([100], [5, 25, 50, 120]))

    def test_extra_0b(self):
        self.assertEqual([2, 2, 2, 1], solution_bisect([100], [5, 25, 50, 120]))

    def test_extra_1(self):
        self.assertEqual([1, 1, 1], solution([100], [100, 100, 1000]))

    def test_extra_1b(self):
        self.assertEqual([1, 1, 1], solution_bisect([100], [100, 100, 1000]))

if __name__ == '__main__':
    unittest.main()

