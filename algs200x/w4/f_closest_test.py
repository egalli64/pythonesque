"""
Finding the Closest Pair of Points

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      http://thisthread.blogspot.com/2018/02/the-closest-pair-of-points.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""
import unittest
import math

from algs200x.w4.f_closest import solution_naive, solution_dac


class TestSolution(unittest.TestCase):
    def test_naive_1(self):
        self.assertEqual(5.0, solution_naive([(0, 0), (3, 4)]))

    def test_naive_2(self):
        self.assertEqual(0.0, solution_naive([(7, 7), (1, 100), (4, 8), (7, 7)]))

    def test_naive_3(self):
        self.assertEqual(math.sqrt(2), solution_naive([(4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1), (-1, -1), (3, -1), (-4, 2), (-2, 4)]))

    def test_dac_1(self):
        self.assertEqual(5.0, solution_dac([(0, 0), (3, 4)]))

    def test_dac_2(self):
        self.assertEqual(0.0, solution_dac([(7, 7), (1, 100), (4, 8), (7, 7)]))

    def test_dac_3(self):
        self.assertEqual(math.sqrt(2), solution_dac([(4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1), (-1, -1), (3, -1), (-4, 2), (-2, 4)]))

    def test_dac_empty(self):
        self.assertEqual(0, solution_dac([]))


if __name__ == '__main__':
    unittest.main()
