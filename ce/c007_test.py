"""
CodeEval Prefix Expressions
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/codeeval-prefix-expressions.html
      https://www.codeeval.com/open_challenges/7/
"""
import unittest
from c007 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(20, solution('* + 2 3 4'))

if __name__ == '__main__':
    unittest.main()
