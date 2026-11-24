"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w6

Week 6 - Dynamic Programming /2: Maximum Amount of Gold
"""
from a_gold import solution


class TestSolution:
    def test_given(self):
        assert solution(10, [1, 4, 8]) == 9

    def test_file(self):
        with open("algs200x/w6/a_gold.in") as file:
            knapsack = int(next(file).split()[0])  # len bars discarded
            bars = list[int](map(int, next(file).split()))

        assert solution(knapsack, bars) == 2335
