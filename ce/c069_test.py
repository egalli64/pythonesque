"""
CodeEval Distinct Subsequences
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/69/
"""
import unittest

from c069 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(5, solution('babgbag', 'bag'))

    def test_provided_2(self):
        self.assertEqual(3, solution('rabbbit', 'rabbit'))

if __name__ == '__main__':
    unittest.main()
