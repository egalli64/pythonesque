"""
Mersenne prime
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-mersenne-prime.html
      https://www.codeeval.com/open_challenges/240/
"""

import unittest
from ce.c240 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('3', solution('4'))

    def test_provided_2(self):
        self.assertEqual('3, 7, 31, 127', solution('308'))

    def test_three_tho(self):
        self.assertEqual('3, 7, 31, 127, 2047', solution('3000'))

    def test_three_hund(self):
        self.assertEqual('3, 7, 31', solution('100'))


if __name__ == '__main__':
    unittest.main()
