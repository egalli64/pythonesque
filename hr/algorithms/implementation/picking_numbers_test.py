"""
HackerRank Algorithms Implementation Picking Numbers

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/picking-numbers/problem
"""
import unittest
from picking_numbers import solution


class TestSolution(unittest.TestCase):
    def test_provided_0(self):
        self.assertEqual(3, solution([4, 6, 5, 3, 3, 1]))

    def test_provided_1(self):
        self.assertEqual(5, solution([1, 2, 2, 3, 1, 2]))

    def test_extra_1(self):
        self.assertEqual(2, solution([98, 3, 99, 1, 97, 2]))


if __name__ == '__main__':
    unittest.main()

