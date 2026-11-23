"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 5 - Dynamic Programming /1: Longest Common Subsequence of Two Sequences
"""
from d_lcs2 import solution


class TestSolution:
    def test_given_1(self):
        assert solution([2, 7, 5], [2, 5]) == 2

    def test_given_2(self):
        assert solution([7], [1, 2, 3, 4]) == 0

    def test_given_3(self):
        assert solution([2, 7, 8, 3], [5, 2, 8, 7]) == 2

    def test_extra_1(self):
        assert solution('abcdef', 'acbcf') == 4

    def test_extra_2(self):
        assert solution('apptab', 'pitiasb') == 4

    def test_file(self):
        with open('algs200x/w5/d_lcs2.in') as file:
            next(file)  # skip header
            lhs = list[int](map(int, next(file).split()))
            next(file)  # skip header
            rhs = list[int](map(int, next(file).split()))

        assert solution(lhs, rhs) == 45
