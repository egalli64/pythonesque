"""
CodeEval Longest Common Subsequence
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-longest-common-subsequence.html
      https://www.codeeval.com/open_challenges/6/
"""
import unittest
from c006 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('MJAU', solution('XMJYAUZ;MZJAWXU'))

    def test_simple(self):
        self.assertEqual('HI', solution('AHOI;HI'))

if __name__ == '__main__':
    unittest.main()
