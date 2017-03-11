"""
CodeEval Self Describing Numbers
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/codeeval-self-describing-numbers.html
      https://www.codeeval.com/open_challenges/40/
"""
import unittest
from ce.c040 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(1, solution('2020'))

    def test_provided_2(self):
        self.assertEqual(0, solution('22'))

    def test_provided_3(self):
        self.assertEqual(1, solution('1210'))


if __name__ == '__main__':
    unittest.main()
