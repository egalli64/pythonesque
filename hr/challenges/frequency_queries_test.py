"""
HackerRank Frequency Queries
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/frequency-queries/problem

You are given queries. Each query is of the form two integers described below:
- : Insert x in your data structure.
- : Delete one occurence of y from your data structure, if present.
- : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.
"""

import unittest

from frequency_queries import freqQuery


class TestSolution(unittest.TestCase):

    def test_add(self):
        actual = freqQuery([[1, 42], [1, 42], [3, 2]])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_delete(self):
        actual = freqQuery([[2, 42], [1, 42], [1, 42], [3, 2]])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_sample_0(self):
        actual = freqQuery([[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]])
        expected = [0, 1]
        self.assertEqual(actual, expected)

    def test_sample_2(self):
        actual = freqQuery([[1, 3], [2, 3], [3, 2], [1, 4], [1, 5], [1, 5], [1, 4], [3, 2], [2, 4], [3, 2]])
        expected = [0, 1, 1]
        self.assertEqual(actual, expected)


