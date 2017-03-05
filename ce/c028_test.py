"""
CodeEval String Searching
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/28/
"""
import unittest
from ce.c028 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(True, solution('Hello,ell'))

    def test_provided_2(self):
        self.assertEqual(True, solution('This is good, is'))

    def test_provided_3(self):
        self.assertEqual(True, solution('CodeEval,C*Eval'))

    def test_provided_4(self):
        self.assertEqual(False, solution('Old,Young'))

    def test_escape_beg(self):
        self.assertEqual(True, solution('* is star,\*'))

    def test_escape_end(self):
        self.assertEqual(True, solution('little *,\*'))

    def test_escape_mid(self):
        self.assertEqual(True, solution('a *!,\*'))

    def test_escape_plus(self):
        self.assertEqual(True, solution('Star,*r'))

    def test_escape_plus_neg(self):
        self.assertEqual(False, solution('Star,*k'))

    def test_both_kind_of(self):
        self.assertEqual(True, solution('Little *!,L*\*!'))

    def test_escape_missing(self):
        self.assertEqual(False, solution('A star,\*'))

    def test_plain_quasi(self):
        self.assertEqual(False, solution('Hello,elp'))

    def test_anything(self):
        self.assertEqual(True, solution('Hello,*'))

    def test_anything_empty(self):
        self.assertEqual(True, solution(',*'))


if __name__ == '__main__':
    unittest.main()
