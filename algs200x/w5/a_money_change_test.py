"""
Money Change Again

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/money-change-again.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""
import unittest

from algs200x.w5.a_money_change import solution_naive, solution_dp


class TestSolution(unittest.TestCase):
    def test_naive_0(self):
        self.assertEqual(2, solution_naive(6))

    def test_naive_1(self):
        self.assertEqual(2, solution_naive(2))

    # way too slow
    # def test_naive_2(self):
    #     self.assertEqual(9, solution_naive(34))

    def test_naive_slow(self):
        self.assertEqual(7, solution_naive(28))

    def test_dp_0(self):
        self.assertEqual(2, solution_dp(6))

    def test_dp_1(self):
        self.assertEqual(2, solution_dp(2))

    def test_dp_2(self):
        self.assertEqual(9, solution_dp(34))

    def test_dp_quiz(self):
        self.assertEqual(238, solution_dp(950))


if __name__ == '__main__':
    unittest.main()
