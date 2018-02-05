"""
Number Operations
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-number-operations.html
      https://www.codeeval.com/open_challenges/190/
"""

import unittest
from ce.c190 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('NO', solution('44 6 1 49 47'))

    def test_provided_2(self):
        self.assertEqual('YES', solution('34 1 49 2 21'))

    def test_provided_3(self):
        self.assertEqual('NO', solution('31 38 27 51 18'))


if __name__ == '__main__':
    unittest.main()
