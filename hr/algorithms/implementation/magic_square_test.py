"""
HackerRank Algorithms Implementation Forming a Magic Square

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/magic-square-forming/problem
"""
import unittest
from magic_square import solution


class TestSolution(unittest.TestCase):
    def test_provided_0(self):
        self.assertEqual(1, solution([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))

    def test_provided_1(self):
        self.assertEqual(4, solution([[4, 8, 2], [4, 5, 7], [6, 1, 6]]))

if __name__ == '__main__':
    unittest.main()

