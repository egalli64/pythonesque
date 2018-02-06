"""
HackerRank Cracking the Coding Interview  Merge Sort: Counting Inversions
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/hackerrank-merge-sort-counting.html
      https://www.hackerrank.com/challenges/ctci-merge-sort
"""

import unittest

from hr.ctci.merge_sort import count_inversions


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(0, count_inversions([1, 1, 1, 2, 2]))

    def test_provided_2(self):
        self.assertEqual(4, count_inversions([2, 1, 3, 1, 2]))


if __name__ == '__main__':
    unittest.main()
