"""
HackerRank Algorithms Implementation Day of the Programmer

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/day-of-the-programmer/problem
"""
import unittest
from day_programmer import solution


class TestSolution(unittest.TestCase):
    def test_provided_0(self):
        self.assertEqual('13.09.2017', solution(2017))

    def test_provided_1(self):
        self.assertEqual('12.09.2016', solution(2016))

    def test_provided_2(self):
        self.assertEqual('12.09.1800', solution(1800))


if __name__ == '__main__':
    unittest.main()

