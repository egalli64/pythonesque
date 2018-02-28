"""
0/1 knapsack

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/other-dynamic-programming-problems.html
"""
import unittest

from algs200x.w6.e_01_knapsack import solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(9, solution(7, [1, 3, 4, 5], [1, 4, 5, 7]))

    def test_2(self):
        self.assertEqual(220, solution(50, [10, 20, 30], [60, 100, 120]))

    def test_3(self):
        self.assertEqual(9, solution(10, [8, 1, 3], [8, 1, 3]))


if __name__ == '__main__':
    unittest.main()
