"""
Template for HackerRank problems
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/ctci-fibonacci-numbers
"""

import unittest
from hr.ctci.fibonacci_numbers import fibonacci


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual(2, fibonacci(3))

    def test_zero(self):
        self.assertEqual(0, fibonacci(0))

    def test_biggest(self):
        self.assertEqual(832040, fibonacci(30))


if __name__ == '__main__':
    unittest.main()
