"""
HackerRank Tutorials  Cracking the Coding Interview  Hash Tables: Ransom Note
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-hash-tables-ransom-note.html
      https://www.hackerrank.com/challenges/ctci-ransom-note
"""
import unittest
from hr.ctci_ransom_note import solution


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(True, solution(['give', 'me', 'one', 'grand', 'today', 'night'],
                                        ['give', 'one', 'grand', 'today']))

if __name__ == '__main__':
    unittest.main()
