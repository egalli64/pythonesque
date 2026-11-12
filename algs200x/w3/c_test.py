"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w3

Week 3 - greedy algorithms: Maximizing Revenue in Online Ad Placement
"""
from c_online_ad import solution


class TestSolution:
    def test_given_1(self):
        assert solution([23], [39]) == 897

    def test_given_2(self):
        assert solution([1, 3, -5], [-2, 4, 1]) == 23

    def test_extra(self):
        with open("algs200x/w3/c_online_ad.in") as file:
            next(file)  # discard header
            profits = list(map(int, next(file).split()))
            clicks = list(map(int, next(file).split()))
            assert solution(profits, clicks) == 1085191604334
