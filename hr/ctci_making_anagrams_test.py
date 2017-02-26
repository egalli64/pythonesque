"""
HackerRank Tutorials  Cracking the Coding Interview  Strings: Making Anagrams
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-strings-making-anagrams.html
      https://www.hackerrank.com/challenges/ctci-making-anagrams
"""

import unittest
from hr.ctci_making_anagrams import solution


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(4, solution('cde', 'abc'))

    def test_many_a(self):
        self.assertEqual(3, solution('aaaa', 'a'))

if __name__ == '__main__':
    unittest.main()
