"""
Longest Lines
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-longest-lines.html
      https://www.codeeval.com/open_challenges/2/
"""

import unittest
from ce.c002 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('San Francisco\nHello World', solution(2, ['Hello World', 'CodeEval', 'Quick Fox', 'A', 'San Francisco']))

if __name__ == '__main__':
    unittest.main()