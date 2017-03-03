"""
Template for HackerRank problems
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/hackerrank-binary-search-ice-cream.html
      https://www.hackerrank.com/
"""

import unittest
from hr.ctci_ice_cream_parlor import solution


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('1 4', solution(4, [1, 4, 5, 3, 2]))

    def test_provided_2(self):
        self.assertEqual('1 2', solution(4, [2, 2, 4, 3]))

    def test_expensive(self):
        self.assertEqual('3 4', solution(10, [2, 2, 4, 6]))

    def test_neighbor(self):
        self.assertEqual('3 4', solution(8, [1, 2, 4, 4, 8]))

if __name__ == '__main__':
    unittest.main()
