"""
CodeEval String List
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/codeeval-string-list.html
      https://www.codeeval.com/open_challenges/38/
"""
import unittest
from ce.c038 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('a', solution('1,aa'))

    def test_provided_2(self):
        self.assertEqual('aa,ab,ba,bb', solution('2,ab'))

    def test_provided_3(self):
        self.assertEqual('ooo,oop,opo,opp,poo,pop,ppo,ppp', solution('3,pop'))

if __name__ == '__main__':
    unittest.main()
