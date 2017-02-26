"""
HackerRank Tutorials  Cracking the Coding Interview  Stacks: Balanced Brackets
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-stacks-balanced-brackets.html
      https://www.hackerrank.com/challenges/ctci-balanced-brackets
"""

import unittest
from hr.ctci_balanced_brackets import solution


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(True, solution('{[()]}'))

    def test_provided_2(self):
        self.assertEqual(False, solution('{[(])}'))

    def test_provided_3(self):
        self.assertEqual(True, solution('{{[[(())]]}}'))

    def test_too_close(self):
        self.assertEqual(False, solution('}}'))

if __name__ == '__main__':
    unittest.main()
