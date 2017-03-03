"""
CodeEval Bit Positions
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/19/
"""
import unittest
from ce.c019 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('true', solution('86,2,3'))

    def test_provided_2(self):
        self.assertEqual('false', solution('125,1,2'))

    def test_double_negative(self):
        self.assertEqual('true', solution('0,1,2'))

if __name__ == '__main__':
    unittest.main()
