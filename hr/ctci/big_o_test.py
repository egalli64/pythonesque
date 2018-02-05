"""
HackerRank Tutorials  Cracking the Coding Interview  Time Complexity: Primality
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/ctci-big-o/
"""

import unittest
from hr.ctci.big_o import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(False, solution(12))

    def test_provided_2(self):
        self.assertEqual(True, solution(5))

    def test_provided_3(self):
        self.assertEqual(True, solution(7))

    def test_negative(self):
        self.assertEqual(False, solution(-3))

    def test_smallest(self):
        self.assertEqual(True, solution(2))

    def test_cataldi(self):
        self.assertEqual(True, solution(524287))


if __name__ == '__main__':
    unittest.main()
