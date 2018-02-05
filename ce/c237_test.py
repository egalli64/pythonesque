"""
Panacea - truth or lie
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-panacea-truth-or-lie.html
      https://www.codeeval.com/open_challenges/237/
"""

import unittest
from ce.c237 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertTrue(solution('64 6e 78 | 100101100 11110'))

    def test_provided_2(self):
        self.assertTrue(solution('5e 7d 59 | 1101100 10010101 1100111'))

    def test_provided_3(self):
        self.assertFalse(solution('93 75 | 1000111 1011010 1100010'))


if __name__ == '__main__':
    unittest.main()
