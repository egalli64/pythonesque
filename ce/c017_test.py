"""
CodeEval Sum of integers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/codeeval-sum-of-integers.html
      https://www.codeeval.com/open_challenges/17/
"""
import unittest
from ce.c017 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(8, solution('-10,2,3,-2,0,5,-15'))

    def test_provided_2(self):
        self.assertEqual(12, solution('2,3,-2,-1,10'))

    def test_plain(self):
        self.assertEqual(5, solution('2,3'))

    def test_a_negative_first(self):
        self.assertEqual(3, solution('-2,3'))

    def test_a_negative_second(self):
        self.assertEqual(2, solution('2,-3'))

    def test_both_negative(self):
        self.assertEqual(-2, solution('-2,-3'))

    def test_a_negative_in_between(self):
        self.assertEqual(2, solution('1,-1,2'))


if __name__ == '__main__':
    unittest.main()
