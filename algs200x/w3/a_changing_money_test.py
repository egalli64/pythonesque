"""
Changing Money

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/half-dozen-of-greedy-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""
import unittest

from algs200x.w3.a_changing_money import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(2, solution(2))

    def test_provided_2(self):
        self.assertEqual(6, solution(28))

    def test_provided_ex(self):
        self.assertEqual(102, solution(997))


if __name__ == '__main__':
    unittest.main()
