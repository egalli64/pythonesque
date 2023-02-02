"""
Not So Clever
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-not-so-clever.html
      https://www.codeeval.com/open_challenges/232/
"""

import unittest
from c232 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('3 4 2 1', solution('4 3 2 1 | 1'))

    def test_provided_2(self):
        self.assertEqual('4 3 5 2 1', solution('5 4 3 2 1 | 2'))


if __name__ == '__main__':
    unittest.main()
