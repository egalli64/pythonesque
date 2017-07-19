"""
CodeEval Word Search
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/65/
"""
import unittest

from ce.c065 import solution


class TestCodeEval(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(False, solution('ASADB'))

    def test_provided_2(self):
        self.assertEqual(True, solution('ABCCED'))

    def test_provided_3(self):
        self.assertEqual(False, solution('ABCF'))

    def test_extra(self):
        self.assertEqual(True, solution('EECSECBASA'))

if __name__ == '__main__':
    unittest.main()
