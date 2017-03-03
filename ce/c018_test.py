"""
CodeEval Multiples of a Number
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/18/
"""
import unittest
from ce.c018 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(16, solution('13,8'))

    def test_provided_2(self):
        self.assertEqual(32, solution('17,16'))

if __name__ == '__main__':
    unittest.main()
