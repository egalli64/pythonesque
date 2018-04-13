"""
HackerRank Algorithms Dynamic Programming Equal

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/04/hackerrank-equal.html
      https://www.hackerrank.com/challenges/equal/problem
"""

import unittest
from equal import solution


class TestSolution(unittest.TestCase):

    def test_provided_0(self):
        self.assertEqual(2, solution([2, 2, 3, 7]))

    def test_provided_1(self):
        self.assertEqual(3, solution([10, 7, 12]))

    def test_extra_0(self):
        self.assertEqual(5104, solution([512, 125, 928, 381, 890, 90, 512, 789, 469, 473, 908, 990, 195, 763, 102, 643, 458, 366, 684, 857, 126, 534, 974, 875, 459, 892, 686, 373, 127, 297, 576, 991, 774, 856, 372, 664, 946, 237, 806, 767, 62, 714, 758, 258, 477, 860, 253, 287, 579, 289, 496]))

    def test_extra_1(self):
        self.assertEqual(3, solution([1, 5, 5]))

    def test_extra_2(self):
        self.assertEqual(6, solution([2, 5, 5, 5, 5, 5]))

if __name__ == '__main__':
    unittest.main()
