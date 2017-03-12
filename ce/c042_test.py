"""
CodeEval Ugly Numbers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/42/
"""
import unittest
from ce.c042 import solution


class TestCodeEval(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(0, solution('1'))

    def test_provided_2(self):
        self.assertEqual(1, solution('9'))

    def test_provided_3(self):
        self.assertEqual(6, solution('011'))

    def test_provided_4(self):
        self.assertEqual(64, solution('12345'))

if __name__ == '__main__':
    unittest.main()
