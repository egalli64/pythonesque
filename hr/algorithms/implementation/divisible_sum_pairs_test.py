"""
HackerRank Algorithms Implementation Divisible Sum Pairs

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/03/hackerrank-divisible-sum-pairs.html
      https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
"""
import unittest
from divisible_sum_pairs import solution, solution_naive


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(5, solution(3, [1, 3, 2, 6, 1, 2]))

    def test_naive_provided_1(self):
        self.assertEqual(5, solution(3, [1, 3, 2, 6, 1, 2]))

    def test_extra_1(self):
        self.assertEqual(5, solution(3, [1, 2, 3, 4, 5, 6]))

    def test_naive_extra_1(self):
        self.assertEqual(5, solution(3, [1, 2, 3, 4, 5, 6]))

    def test_extra_2(self):
        self.assertEqual(1, solution(3, [0, 0]))

    def test_extra_3(self):
        self.assertEqual(2, solution(3, [1, 2, 2]))

    def test_naive_extra_4(self):
        self.assertEqual(9, solution_naive(4, [1, 1, 2, 2, 2, 3, 3, 3]))

    def test_extra_4(self):
        self.assertEqual(9, solution(4, [1, 1, 2, 2, 2, 3, 3, 3]))

if __name__ == '__main__':
    unittest.main()

