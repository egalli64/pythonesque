"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 Divide-and-Conquer - Finding the Closest Pair of Points
"""
import math
import pytest

from f1_closest_naive import solution


class TestSolution:
    def test_given_1(self):
        assert solution([(0, 0), (3, 4)]) == 5.0

    def test_given_2(self):
        assert solution([(7, 7), (1, 100), (4, 8), (7, 7)]) == 0.0

    def test_given_3(self):
        actual = solution(
            [(4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1), (-1, -1), (3, -1), (-4, 2), (-2, 4)])
        assert actual == pytest.approx(math.sqrt(2))
