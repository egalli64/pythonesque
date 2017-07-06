"""
CodeEval Type Ahead
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/07/codeeval-type-ahead.html
      https://www.codeeval.com/open_challenges/55/
"""
import unittest

from ce.c055 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided(self):
        self.assertEqual('lamb,0.375;teacher,0.250;children,0.125;eager,0.125;rule,0.125', solution(2, 'the'))

    def test_lamb(self):
        self.assertEqual('at,0.200;its,0.200;love,0.200;was,0.200;you,0.200', solution(2, 'lamb'))

    def test_the_lamb(self):
        self.assertEqual('love,0.333;was,0.333;you,0.333', solution(3, 'the lamb'))

    def test_at(self):
        self.assertEqual('school,1.000', solution(2, 'at'))

if __name__ == '__main__':
    unittest.main()
