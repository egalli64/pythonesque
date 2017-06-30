"""
CodeEval Cash register
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/54/
"""
import unittest
from ce.c054 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('NICKEL,PENNY', solution(15.94, 16))

    def test_provided_2(self):
        self.assertEqual('ERROR', solution(17, 16))

    def test_provided_3(self):
        self.assertEqual('ZERO', solution(35, 35))

    def test_provided_4(self):
        self.assertEqual('FIVE', solution(45, 50))

    def test_rounding(self):
        self.assertEqual('FIFTY,TWENTY,TWO,ONE,HALF DOLLAR,QUARTER,DIME', solution(134.61, 208.46))
if __name__ == '__main__':
    unittest.main()
