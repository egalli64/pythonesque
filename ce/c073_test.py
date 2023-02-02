"""
CodeEval Decode Numbers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/73/
"""
import unittest

from c073 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(2, solution('12'))

    def test_provided_2(self):
        self.assertEqual(3, solution('123'))

    def test_extra(self):
        self.assertEqual(1, solution('75'))

if __name__ == '__main__':
    unittest.main()
