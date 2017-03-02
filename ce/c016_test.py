"""
CodeEval Number of Ones
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/16/
"""
import unittest
from ce.c016 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(2, solution(10))

    def test_provided_2(self):
        self.assertEqual(3, solution(22))

    def test_provided_3(self):
        self.assertEqual(3, solution(56))

if __name__ == '__main__':
    unittest.main()
