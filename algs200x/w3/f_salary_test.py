"""
Maximizing Your Salary

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""
import unittest

from algs200x.w3.f_salary import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual('221', solution(['21', '2']))

    def test_provided_2(self):
        self.assertEqual('99641', solution(['9', '4', '6', '1', '9']))

    def test_provided_3(self):
        self.assertEqual('923923', solution(['23', '39', '92']))


if __name__ == '__main__':
    unittest.main()
