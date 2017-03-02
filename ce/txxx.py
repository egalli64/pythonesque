"""
Template for Python 3 CodeEval problems
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/
"""
import unittest
from ce.cxxx import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(None, solution('whatever'))

if __name__ == '__main__':
    unittest.main()
