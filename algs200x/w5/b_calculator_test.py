"""
Primitive Calculator

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/primitive-calculator.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 5 - Dynamic Programming 1
"""
import unittest

from algs200x.w5.b_calculator import solution_naive, solution_dp


class TestSolution(unittest.TestCase):
    def test_naive_1(self):
        sequence = solution_naive(1)
        self.assertEqual(1, len(sequence))

    def test_naive_2(self):
        sequence = solution_naive(5)
        self.assertEqual(4, len(sequence))

    def test_naive_3(self):
        sequence = solution_naive(96234)
        self.assertNotEqual(15, len(sequence))  # expected failure!

    def test_dp_1(self):
        sequence = solution_dp(1)
        self.assertEqual(1, len(sequence))

    def test_dp_2(self):
        sequence = solution_dp(5)
        self.assertEqual(4, len(sequence))

    def test_dp_3x(self):
        sequence = solution_dp(11)
        self.assertEqual(5, len(sequence))

    def test_dp_3(self):
        sequence = solution_dp(96234)
        self.assertEqual(15, len(sequence))

    def test_dp_quiz(self):
        sequence = solution_dp(98734)
        self.assertEqual(19, len(sequence))


if __name__ == '__main__':
    unittest.main()
