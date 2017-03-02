"""
CodeEval Detecting Cycles
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-detecting-cycles.html
      https://www.codeeval.com/open_challenges/5/
"""
import unittest
from ce.c005 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('6 3 1', solution('2 0 6 3 1 6 3 1 6 3 1'))

    def test_provided_2(self):
        self.assertEqual('49', solution('3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49'))

    def test_provided_3(self):
        self.assertEqual('1 2 3', solution('1 2 3 1 2 3 1 2 3'))

    def test_tail(self):
        self.assertEqual('1 2', solution('1 2 3 1 2'))

if __name__ == '__main__':
    unittest.main()
