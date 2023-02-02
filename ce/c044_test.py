"""
CodeEval Following Integer
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/codeeval-following-integer.html
      https://www.codeeval.com/open_challenges/44/
"""
import unittest
from c044 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(151, solution('115'))

    def test_provided_2(self):
        self.assertEqual(2048, solution('842'))

    def test_provided_3(self):
        self.assertEqual(80000, solution('8000'))

if __name__ == '__main__':
    unittest.main()
