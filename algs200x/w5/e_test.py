"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 5 - Dynamic Programming /1: Longest Common Subsequence of Three Sequences
"""
from e_lcs3 import solution


class TestSolution:
    def test_given_1(self):
        assert solution([1, 2, 3], [2, 1, 3], [1, 3, 5]) == 2

    def test_given_2(self):
        assert solution([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]) == 3

    def test_extra(self):
        assert solution([1], [1, 2], [1, 2, 3]) == 1

    def test_file(self):
        with open('algs200x/w5/e_lcs3.in') as file:
            next(file)  # discard size
            a = list[int](map(int, next(file).split()))
            next(file)  # discard size
            b = list[int](map(int, next(file).split()))
            next(file)  # discard size
            c = list[int](map(int, next(file).split()))

        assert solution(a, b, c) == 40
