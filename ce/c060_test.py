"""
Template for Python 3 CodeEval problems
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/
"""
import unittest

from ce.c060 import is_valid, around


class TestCodeEval(unittest.TestCase):

    def test_is_valid(self):
        self.assertEqual(True, is_valid((19, 54)))

    def test_is_valid_not(self):
        self.assertEqual(False, is_valid((19, 55)))

    def test_is_valid_not_neg(self):
        self.assertEqual(False, is_valid((-19, -55)))

    def test_around_origin(self):
        self.assertEqual([(-1, 0), (0, -1), (1, 0), (0, 1)], around((0, 0)))

    def test_around(self):
        self.assertEqual([(18, 54), (19, 53), (20, 54), (19, 55)], around((19, 54)))

    def test_around_neg(self):
        self.assertEqual([(-20, 54), (-19, 53), (-18, 54), (-19, 55)], around((-19, 54)))

if __name__ == '__main__':
    unittest.main()
