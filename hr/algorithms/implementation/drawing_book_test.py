"""
HackerRank Algorithms Implementation Drawing Book

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/drawing-book/problem
"""
import unittest
from drawing_book import solution


class TestSolution(unittest.TestCase):
    def test_provided_0(self):
        self.assertEqual(1, solution(6, 2))

    def test_provided_1(self):
        self.assertEqual(0, solution(5, 4))

    def test_extra_1(self):
        self.assertEqual(1, solution(6, 5))

    def test_extra_2(self):
        self.assertEqual(1, solution(7, 4))

if __name__ == '__main__':
    unittest.main()

