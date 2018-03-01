"""
Maximizing the Value of an Arithmetic Expression

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 6 - Dynamic Programming 2 - 3-Partition problem
"""
import unittest

from algs200x.w6.c_max_expr import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(6, solution([1, 5], ['+']))

    def test_provided_2(self):
        self.assertEqual(200, solution([5, 8, 7, 4, 8, 9], ['-', '+', '*', '-', '+']))

    def test_quiz(self):
        self.assertEqual(9168, solution([7, 6, 3, 2, 7, 4, 2, 4, 2, 9, 6, 8],
                                        ['+', '+', '-', '-', '-', '*', '+', '+', '-', '*', '*']))

    def test_wrong_operation(self):
        self.assertRaises(KeyError, solution, [1, 5], ['^'])


if __name__ == '__main__':
    unittest.main()
