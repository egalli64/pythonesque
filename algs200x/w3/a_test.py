"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w3

Week 3 - greedy algorithms: Changing Money
"""
from a_changing_money import solution


class TestSolution:
    def test_given_1(self):
        assert solution(2) == 2

    def test_given_2(self):
        assert solution(28) == 6

    def test_extra(self):
        assert solution(997) == 102
