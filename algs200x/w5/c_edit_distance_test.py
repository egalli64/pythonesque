"""
Computing the Edit Distance Between Two Strings

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/computing-edit-distance-between-two.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""
import unittest

from algs200x.w5.c_edit_distance import solution_dp


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(0, solution_dp('ab', 'ab'))

    def test_extra(self):
        self.assertEqual(2, solution_dp('a', 'abc'))

    def test_provided_2(self):
        self.assertEqual(3, solution_dp('short', 'ports'))


if __name__ == '__main__':
    unittest.main()
