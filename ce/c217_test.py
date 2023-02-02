"""
One zero, two zeros...
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-one-zero-two-zeros.html
      https://www.codeeval.com/open_challenges/217/
"""

import unittest
from c217 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(3, solution('1 8'))

    def test_provided_2(self):
        self.assertEqual(1, solution('2 4'))


if __name__ == '__main__':
    unittest.main()
