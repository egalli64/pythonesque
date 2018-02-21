"""
Longest Common Subsequence of Three Sequences

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/longest-common-subsequence-of-three.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""
import unittest

from algs200x.w5.e_lcs3 import solution_dp


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(2, solution_dp([1, 2, 3], [2, 1, 3], [1, 3, 5]))

    def test_provided_2(self):
        self.assertEqual(3, solution_dp([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]))

    def test_simple(self):
        self.assertEqual(1, solution_dp([1], [1, 2], [1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
