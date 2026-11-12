"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w3

Week 3 - greedy algorithms: Maximizing the Value of a Loot
Find the most valuable combination of fractionable items
"""
import pytest

from b_max_loot import solution


class TestSolution:
    def test_given_1(self):
        assert solution(50, [(60, 20), (100, 50), (120, 30)]) == 180.0

    def test_given_2(self):
        assert solution(10, [(500, 30)]) == pytest.approx(166.6667)

    def test_extra(self):
        with open("algs200x/w3/b_max_loot.in") as file:
            size, capacity = map(int, next(file).split())
            items = [tuple(map(int, next(file).split())) for _ in range(size)]

        assert solution(capacity, items) == pytest.approx(66152.572, rel=0, abs=0.0005)
