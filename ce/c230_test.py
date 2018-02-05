"""
Football
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-football.html
      https://www.codeeval.com/open_challenges/230/
"""

import unittest
from ce.c230 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('1:1,2,3; 2:1; 3:1,2; 4:1,3;', solution('1 2 3 4 | 3 1 | 4 1'))

    def test_provided_2(self):
        self.assertEqual('11:1; 19:1,2; 21:2; 23:2; 29:3; 31:3; 39:3;', solution('19 11 | 19 21 23 | 31 39 29'))

    def test_key_numbers(self):
        self.assertEqual('1:1,2,3; 2:2; 4:3; 10:1;', solution('1 10 | 2 1 | 4 1'))


if __name__ == '__main__':
    unittest.main()
