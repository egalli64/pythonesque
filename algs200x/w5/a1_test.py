"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 5 - Dynamic Programming /1: Money Change Again
"""
import pytest

from a1_money_recursive import solution


class TestSolution:
    def test_given_1(self):
        assert solution(2) == 2

    @pytest.mark.skip(reason="too slow")
    def test_given_2(self):
        assert solution(34) == 9

    def test_extra_1(self):
        assert solution(6) == 2

    def test_extra_2(self):
        assert solution(28) == 7
