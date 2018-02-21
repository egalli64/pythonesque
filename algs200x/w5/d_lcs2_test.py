"""
Longest Common Subsequence of Two Sequences

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/longest-common-subsequence-of-two.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""
import unittest

from algs200x.w5.d_lcs2 import solution_dp


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(2, solution_dp([2, 7, 5], [2, 5]))

    def test_provided_2(self):
        self.assertEqual(0, solution_dp([7], [1, 2, 3, 4]))

    def test_provided_3(self):
        self.assertEqual(2, solution_dp([2, 7, 8, 3], [5, 2, 8, 7]))

    def test_extra(self):
        self.assertEqual(4, solution_dp('abcdef', 'acbcf'))

    def test_extra_2(self):
        self.assertEqual(4, solution_dp('apptab', 'pitiasb'))


if __name__ == '__main__':
    unittest.main()
