"""
HackerRank Algorithms Implementation Electronics Shop

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/electronics-shop/problem
"""
import unittest
from electronics_shop import solution


class TestSolution(unittest.TestCase):
    def test_provided_0(self):
        self.assertEqual(9, solution([3, 1], [5, 2, 8], 10))

    def test_provided_1(self):
        self.assertEqual(-1, solution([4], [5], 5))

if __name__ == '__main__':
    unittest.main()

