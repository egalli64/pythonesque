"""
Number of Inversions

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""
import unittest

from algs200x.w4.d_inversions import solution_naive, solution_merge


class TestSolution(unittest.TestCase):
    slow = [x for x in range(4000)] + [1]

    def test_naive_1(self):
        self.assertEqual(2, solution_naive([2, 3, 9, 2, 9]))

    def test_naive_slow_1(self):
        self.assertEqual(3998, solution_naive(self.slow.copy()))

    def test_merge_1(self):
        self.assertEqual(2, solution_merge([2, 3, 9, 2, 9]))

    def test_merge_slow_1(self):
        self.assertEqual(3998, solution_merge(self.slow.copy()))


if __name__ == '__main__':
    unittest.main()
