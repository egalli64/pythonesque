"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Divide-and-Conquer: Binary Search
"""
from a_binary_search import solution


class TestSolution:
    def test_given(self):
        results = solution([1, 5, 8, 12, 13], [8, 1, 23, 1, 11])
        assert results == [2, 0, -1, 0, -1]

    def test_extra(self):
        with open("algs200x/w4/a_binary_search.in") as file:
            _, *data = map(int, next(file).split())
            _, *targets = map(int, next(file).split())

        xs = solution(data, targets)
        assert xs[:15] == [-1, -1, 22432, 17123, 26375, 10448, -1, 29812, -1, -1, -1, 25889, -1, -1, -1]
        assert xs[-15:] == [6702, 475, 16071, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
