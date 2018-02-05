"""
Template for Python 3 problems by CodeEval
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-time-to-eat.html
      https://www.codeeval.com/open_challenges/214/
"""

import unittest
from ce.c214 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('14:44:45 09:53:27 02:26:31', solution('02:26:31 14:44:45 09:53:27'))

    def test_provided_2(self):
        self.assertEqual('21:25:41 05:33:44', solution('05:33:44 21:25:41'))


if __name__ == '__main__':
    unittest.main()
